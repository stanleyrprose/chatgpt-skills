import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "evaluate-promotion-gate.py"
spec = importlib.util.spec_from_file_location("promotion_gate", SCRIPT)
pg = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = pg
spec.loader.exec_module(pg)


POLICY = {
    "version": 1,
    "candidate": {
        "same_invariant_independent_tasks": 2,
        "total_behavior_violations": 3,
        "minimum_independent_tasks_for_total": 2,
        "single_high_severity": True,
    },
    "promote": {
        "same_invariant_independent_tasks": 2,
        "require_reproducible": True,
        "require_fixture_ready": True,
    },
}


def write_observation(
    root: Path,
    *,
    name: str,
    observation_id: str,
    layer: str = "behavior",
    task_id: str = "task-1",
    routing_status: str = "pass",
    contract_status: str = "pass",
    severity: str = "normal",
    reproducible: str = "yes",
    fixture_ready: str = "no",
    state: str = "open",
    eligible: str = "true",
    skill: str = "diagnose",
    invariant_id: str = "evidence-before-change",
):
    path = root / f"{name}.md"
    path.write_text(
        f"""# Observation

```yaml
observation_id: "{observation_id}"
timestamp: "2026-09-20"
trigger_type: "other"
```

```promotion-gate
eligible: {eligible}
state: {state}
failure_layer: {layer}
skill: {skill}
invariant_id: {invariant_id}
task_id: {task_id}
routing_status: {routing_status}
contract_status: {contract_status}
severity: {severity}
reproducible: {reproducible}
fixture_ready: {fixture_ready}
```
""",
        encoding="utf-8",
    )
    return path


class PromotionGateTest(unittest.TestCase):
    def test_historical_observations_without_block_are_ignored(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "old.md").write_text(
                '```yaml\nobservation_id: "old"\n```\n',
                encoding="utf-8",
            )
            result = pg.evaluate(pg.scan_observations(root), POLICY)
            self.assertEqual("GREEN", result.status)
            self.assertEqual(0, result.observations_with_metadata)

    def test_routing_failure_is_watch_not_tier3_candidate(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_observation(
                root,
                name="routing",
                observation_id="routing-1",
                layer="routing",
                routing_status="fail",
                contract_status="unknown",
                skill="N/A",
                invariant_id="N/A",
            )
            result = pg.evaluate(pg.scan_observations(root), POLICY)
            self.assertEqual("WATCH", result.status)
            self.assertEqual(0, result.qualified_behavior_violations)
            self.assertEqual(1, result.layer_counts["routing"])

    def test_single_behavior_violation_is_watch(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_observation(root, name="one", observation_id="one")
            result = pg.evaluate(pg.scan_observations(root), POLICY)
            self.assertEqual("WATCH", result.status)
            self.assertEqual(1, result.qualified_behavior_violations)

    def test_repeated_invariant_across_independent_tasks_is_candidate(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_observation(root, name="one", observation_id="one", task_id="task-1")
            write_observation(root, name="two", observation_id="two", task_id="task-2")
            result = pg.evaluate(pg.scan_observations(root), POLICY)
            self.assertEqual("CANDIDATE", result.status)

    def test_repeated_fixture_ready_pattern_is_promote(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_observation(root, name="one", observation_id="one", task_id="task-1")
            write_observation(
                root,
                name="two",
                observation_id="two",
                task_id="task-2",
                fixture_ready="yes",
                reproducible="yes",
            )
            result = pg.evaluate(pg.scan_observations(root), POLICY)
            self.assertEqual("PROMOTE", result.status)

    def test_promote_policy_flags_are_independent(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_observation(
                root,
                name="one",
                observation_id="one",
                task_id="task-1",
                reproducible="no",
                fixture_ready="yes",
            )
            write_observation(
                root,
                name="two",
                observation_id="two",
                task_id="task-2",
                reproducible="no",
                fixture_ready="yes",
            )
            fixture_only = json.loads(json.dumps(POLICY))
            fixture_only["promote"]["require_reproducible"] = False
            self.assertEqual(
                "PROMOTE",
                pg.evaluate(pg.scan_observations(root), fixture_only).status,
            )
            self.assertEqual(
                "CANDIDATE",
                pg.evaluate(pg.scan_observations(root), POLICY).status,
            )

    def test_promote_requires_same_evidence_when_both_flags_enabled(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_observation(
                root,
                name="one",
                observation_id="one",
                task_id="task-1",
                reproducible="yes",
                fixture_ready="no",
            )
            write_observation(
                root,
                name="two",
                observation_id="two",
                task_id="task-2",
                reproducible="no",
                fixture_ready="yes",
            )
            self.assertEqual(
                "CANDIDATE",
                pg.evaluate(pg.scan_observations(root), POLICY).status,
            )

    def test_resolved_finding_is_not_active(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_observation(root, name="one", observation_id="one", state="resolved")
            result = pg.evaluate(pg.scan_observations(root), POLICY)
            self.assertEqual("GREEN", result.status)
            self.assertEqual(0, result.active_findings)

    def test_high_severity_behavior_is_candidate_but_not_promote(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_observation(
                root,
                name="one",
                observation_id="one",
                severity="high",
                fixture_ready="yes",
            )
            result = pg.evaluate(pg.scan_observations(root), POLICY)
            self.assertEqual("CANDIDATE", result.status)

    def test_malformed_metadata_fails_closed(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            path = write_observation(root, name="bad", observation_id="bad")
            text = path.read_text(encoding="utf-8")
            path.write_text(text.replace("fixture_ready: no\n", ""), encoding="utf-8")
            with self.assertRaises(pg.PromotionGateError):
                pg.scan_observations(root)

    def test_policy_loader_rejects_invalid_threshold(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "policy.json"
            bad = json.loads(json.dumps(POLICY))
            bad["candidate"]["same_invariant_independent_tasks"] = 0
            path.write_text(json.dumps(bad), encoding="utf-8")
            with self.assertRaises(pg.PromotionGateError):
                pg.load_policy(path)


if __name__ == "__main__":
    unittest.main()

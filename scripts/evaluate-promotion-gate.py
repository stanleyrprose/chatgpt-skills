#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OBSERVATIONS = ROOT / "observations"
DEFAULT_POLICY = ROOT / "promotion-gate-policy.json"

PROMOTION_BLOCK_RE = re.compile(r"(?ms)^```promotion-gate[ \t]*\n(.*?)^```[ \t]*$")
OBSERVATION_ID_RE = re.compile(
    r'(?m)^\s*observation_id:\s*(?:"([^"]+)"|\'([^\']+)\'|([^\s#]+))\s*$'
)

REQUIRED_FIELDS = (
    "eligible", "state", "failure_layer", "skill", "invariant_id", "task_id",
    "routing_status", "contract_status", "severity", "reproducible", "fixture_ready",
)
FAILURE_LAYERS = {"routing", "skill_contract", "behavior", "tool_runtime", "context", "other"}
STATES = {"open", "resolved"}
PASS_STATES = {"pass", "fail", "unknown", "n/a"}
SEVERITIES = {"normal", "high"}
YES_NO_STATES = {"yes", "no", "unknown", "n/a"}


class PromotionGateError(ValueError):
    pass


@dataclass(frozen=True)
class Observation:
    observation_id: str
    path: str
    eligible: bool
    state: str
    failure_layer: str
    skill: str
    invariant_id: str
    task_id: str
    routing_status: str
    contract_status: str
    severity: str
    reproducible: str
    fixture_ready: str


@dataclass(frozen=True)
class GateResult:
    status: str
    observations_with_metadata: int
    active_findings: int
    qualified_behavior_violations: int
    layer_counts: dict[str, int]
    repeated_patterns: list[dict[str, Any]]
    reasons: list[str]
    recommendations: list[str]


def _strip_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        value = value[1:-1]
    return value.strip()


def _parse_bool(value: str, *, field: str, path: Path) -> bool:
    normalized = value.casefold()
    if normalized == "true":
        return True
    if normalized == "false":
        return False
    raise PromotionGateError(f"{path}: {field} must be true or false")


def _parse_block(block: str, *, path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    for line_no, raw_line in enumerate(block.splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise PromotionGateError(f"{path}: promotion-gate line {line_no} must use 'key: value'")
        key, value = line.split(":", 1)
        key = key.strip()
        value = _strip_scalar(value)
        if not key or not value:
            raise PromotionGateError(f"{path}: promotion-gate line {line_no} has an empty key/value")
        if key in data:
            raise PromotionGateError(f"{path}: duplicate promotion-gate key {key!r}")
        data[key] = value

    unknown = sorted(set(data) - set(REQUIRED_FIELDS))
    if unknown:
        raise PromotionGateError(f"{path}: unknown promotion-gate fields: {', '.join(unknown)}")
    missing = [field for field in REQUIRED_FIELDS if field not in data]
    if missing:
        raise PromotionGateError(f"{path}: missing promotion-gate fields: {', '.join(missing)}")
    return data


def parse_observation(path: Path) -> Observation | None:
    text = path.read_text(encoding="utf-8", errors="replace")
    blocks = PROMOTION_BLOCK_RE.findall(text)
    if not blocks:
        return None
    if len(blocks) != 1:
        raise PromotionGateError(f"{path}: expected at most one promotion-gate block, found {len(blocks)}")

    observation_match = OBSERVATION_ID_RE.search(text)
    if not observation_match:
        raise PromotionGateError(f"{path}: promotion-gate observation must contain observation_id")
    observation_id = next(group for group in observation_match.groups() if group is not None)
    data = _parse_block(blocks[0], path=path)

    eligible = _parse_bool(data["eligible"], field="eligible", path=path)
    state = data["state"].casefold()
    layer = data["failure_layer"].casefold()
    routing_status = data["routing_status"].casefold()
    contract_status = data["contract_status"].casefold()
    severity = data["severity"].casefold()
    reproducible = data["reproducible"].casefold()
    fixture_ready = data["fixture_ready"].casefold()

    if state not in STATES:
        raise PromotionGateError(f"{path}: invalid state {state!r}")
    if layer not in FAILURE_LAYERS:
        raise PromotionGateError(f"{path}: invalid failure_layer {layer!r}")
    if routing_status not in PASS_STATES:
        raise PromotionGateError(f"{path}: invalid routing_status {routing_status!r}")
    if contract_status not in PASS_STATES:
        raise PromotionGateError(f"{path}: invalid contract_status {contract_status!r}")
    if severity not in SEVERITIES:
        raise PromotionGateError(f"{path}: invalid severity {severity!r}")
    if reproducible not in YES_NO_STATES:
        raise PromotionGateError(f"{path}: invalid reproducible value {reproducible!r}")
    if fixture_ready not in YES_NO_STATES:
        raise PromotionGateError(f"{path}: invalid fixture_ready value {fixture_ready!r}")

    return Observation(
        observation_id=observation_id,
        path=path.as_posix(),
        eligible=eligible,
        state=state,
        failure_layer=layer,
        skill=data["skill"],
        invariant_id=data["invariant_id"],
        task_id=data["task_id"],
        routing_status=routing_status,
        contract_status=contract_status,
        severity=severity,
        reproducible=reproducible,
        fixture_ready=fixture_ready,
    )


def scan_observations(directory: Path) -> list[Observation]:
    observations: list[Observation] = []
    ids: dict[str, Path] = {}
    for path in sorted(directory.glob("*.md")):
        observation = parse_observation(path)
        if observation is None:
            continue
        previous = ids.get(observation.observation_id)
        if previous is not None:
            raise PromotionGateError(
                f"duplicate observation_id {observation.observation_id!r}: {previous} and {path}"
            )
        ids[observation.observation_id] = path
        observations.append(observation)
    return observations


def load_policy(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("version") != 1:
        raise PromotionGateError(f"{path}: only policy version 1 is supported")

    candidate = payload.get("candidate")
    promote = payload.get("promote")
    if not isinstance(candidate, dict) or not isinstance(promote, dict):
        raise PromotionGateError(f"{path}: candidate/promote must be objects")

    integer_fields = (
        (candidate, "same_invariant_independent_tasks"),
        (candidate, "total_behavior_violations"),
        (candidate, "minimum_independent_tasks_for_total"),
        (promote, "same_invariant_independent_tasks"),
    )
    for section, field in integer_fields:
        value = section.get(field)
        if not isinstance(value, int) or value < 1:
            raise PromotionGateError(f"{path}: {field} must be an integer >= 1")

    for section, field in (
        (candidate, "single_high_severity"),
        (promote, "require_reproducible"),
        (promote, "require_fixture_ready"),
    ):
        if not isinstance(section.get(field), bool):
            raise PromotionGateError(f"{path}: {field} must be boolean")
    return payload


def _is_na(value: str) -> bool:
    return value.strip().casefold() in {"n/a", "na"}


def _qualified_behavior(observation: Observation) -> bool:
    return (
        observation.eligible
        and observation.state == "open"
        and observation.failure_layer == "behavior"
        and observation.routing_status == "pass"
        and observation.contract_status == "pass"
        and not _is_na(observation.skill)
        and not _is_na(observation.invariant_id)
        and not _is_na(observation.task_id)
    )


def evaluate(observations: list[Observation], policy: dict[str, Any]) -> GateResult:
    active = [item for item in observations if item.eligible and item.state == "open"]
    layer_counts = Counter(item.failure_layer for item in active)
    behavior = [item for item in active if _qualified_behavior(item)]

    groups: dict[tuple[str, str], list[Observation]] = defaultdict(list)
    for item in behavior:
        groups[(item.skill, item.invariant_id)].append(item)

    repeated_patterns: list[dict[str, Any]] = []
    for (skill, invariant_id), items in sorted(groups.items()):
        tasks = sorted({item.task_id for item in items})
        repeated_patterns.append(
            {
                "skill": skill,
                "invariant_id": invariant_id,
                "occurrences": len(items),
                "independent_tasks": len(tasks),
                "task_ids": tasks,
                "has_reproducible": any(item.reproducible == "yes" for item in items),
                "has_fixture_ready": any(item.fixture_ready == "yes" for item in items),
                "has_reproducible_fixture_ready": any(
                    item.reproducible == "yes" and item.fixture_ready == "yes" for item in items
                ),
            }
        )

    candidate_policy = policy["candidate"]
    promote_policy = policy["promote"]
    candidate_reasons: list[str] = []

    for pattern in repeated_patterns:
        if pattern["independent_tasks"] >= candidate_policy["same_invariant_independent_tasks"]:
            candidate_reasons.append(
                f"repeated {pattern['skill']}/{pattern['invariant_id']} across "
                f"{pattern['independent_tasks']} independent tasks"
            )

    distinct_behavior_tasks = len({item.task_id for item in behavior})
    if (
        len(behavior) >= candidate_policy["total_behavior_violations"]
        and distinct_behavior_tasks >= candidate_policy["minimum_independent_tasks_for_total"]
    ):
        candidate_reasons.append(
            f"{len(behavior)} qualified behavior violations across "
            f"{distinct_behavior_tasks} independent tasks"
        )

    if candidate_policy["single_high_severity"] and any(item.severity == "high" for item in behavior):
        candidate_reasons.append("at least one high-severity qualified behavior violation")

    promote_reasons: list[str] = []
    for pattern in repeated_patterns:
        if pattern["independent_tasks"] < promote_policy["same_invariant_independent_tasks"]:
            continue
        if promote_policy["require_reproducible"] and promote_policy["require_fixture_ready"]:
            evidence_ok = pattern["has_reproducible_fixture_ready"]
        elif promote_policy["require_reproducible"]:
            evidence_ok = pattern["has_reproducible"]
        elif promote_policy["require_fixture_ready"]:
            evidence_ok = pattern["has_fixture_ready"]
        else:
            evidence_ok = True
        if evidence_ok:
            promote_reasons.append(
                f"{pattern['skill']}/{pattern['invariant_id']} is repeated and "
                "has reproducible fixture-ready evidence"
            )

    if promote_reasons:
        status = "PROMOTE"
        reasons = promote_reasons
    elif candidate_reasons:
        status = "CANDIDATE"
        reasons = candidate_reasons
    elif active:
        status = "WATCH"
        reasons = ["active findings exist but Tier-3 promotion evidence is insufficient"]
    else:
        status = "GREEN"
        reasons = ["no active promotion-marked findings"]

    recommendations: list[str] = []
    if layer_counts["routing"]:
        recommendations.append("Routing findings exist: repair/evaluate Tier 2A routing metadata before Tier 3.")
    if layer_counts["skill_contract"]:
        recommendations.append("Skill-contract findings exist: repair Tier 2B canonical Skill contract before Tier 3.")
    if layer_counts["tool_runtime"]:
        recommendations.append("Tool/runtime findings exist: repair the capability/runtime boundary, not the Skill architecture.")
    if layer_counts["context"]:
        recommendations.append("Context findings exist: investigate context/state recovery before Tier 3.")
    if behavior:
        if status == "PROMOTE":
            recommendations.append("Tier-3 evidence threshold is met; explicit authorization is still required before implementation.")
        elif status == "CANDIDATE":
            recommendations.append("Review repeated behavior evidence and prepare a stable fixture before promoting Tier 3.")
        else:
            recommendations.append("Continue event-triggered observation; do not add Tier-3 infrastructure yet.")

    return GateResult(
        status=status,
        observations_with_metadata=len(observations),
        active_findings=len(active),
        qualified_behavior_violations=len(behavior),
        layer_counts=dict(sorted(layer_counts.items())),
        repeated_patterns=repeated_patterns,
        reasons=reasons,
        recommendations=recommendations,
    )


def render_text(result: GateResult) -> str:
    lines = [
        f"Skill Architecture Promotion Gate: {result.status}",
        f"Promotion-marked observations: {result.observations_with_metadata}",
        f"Active findings: {result.active_findings}",
        f"Qualified behavior violations: {result.qualified_behavior_violations}",
    ]
    if result.layer_counts:
        lines.append("Active layers: " + ", ".join(f"{name}={count}" for name, count in result.layer_counts.items()))
    else:
        lines.append("Active layers: none")

    if result.repeated_patterns:
        lines.append("Behavior patterns:")
        for pattern in result.repeated_patterns:
            lines.append(
                "  - "
                f"{pattern['skill']}/{pattern['invariant_id']}: "
                f"occurrences={pattern['occurrences']}, "
                f"independent_tasks={pattern['independent_tasks']}, "
                f"reproducible={str(pattern['has_reproducible']).lower()}, "
                f"fixture_ready={str(pattern['has_fixture_ready']).lower()}"
            )

    lines.append("Reasons:")
    lines.extend(f"  - {reason}" for reason in result.reasons)
    if result.recommendations:
        lines.append("Recommendations:")
        lines.extend(f"  - {item}" for item in result.recommendations)
    return "\n".join(lines)


def render_markdown(result: GateResult) -> str:
    lines = [
        "## Skill Architecture Promotion Gate",
        "",
        f"**Status: {result.status}**",
        "",
        f"- Promotion-marked observations: {result.observations_with_metadata}",
        f"- Active findings: {result.active_findings}",
        f"- Qualified behavior violations: {result.qualified_behavior_violations}",
    ]
    if result.layer_counts:
        lines.append("- Active layers: " + ", ".join(f"`{name}={count}`" for name, count in result.layer_counts.items()))
    else:
        lines.append("- Active layers: none")

    lines.extend(["", "### Reasons"])
    lines.extend(f"- {reason}" for reason in result.reasons)
    if result.recommendations:
        lines.extend(["", "### Recommendations"])
        lines.extend(f"- {item}" for item in result.recommendations)
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Evaluate event-triggered observations for Skill architecture promotion evidence."
    )
    parser.add_argument("--observations-dir", type=Path, default=DEFAULT_OBSERVATIONS)
    parser.add_argument("--policy", type=Path, default=DEFAULT_POLICY)
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = parser.parse_args(argv)

    try:
        observations = scan_observations(args.observations_dir)
        policy = load_policy(args.policy)
        result = evaluate(observations, policy)
    except (OSError, json.JSONDecodeError, PromotionGateError) as exc:
        print(f"Promotion Gate setup failed: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(asdict(result), indent=2, sort_keys=True))
    else:
        print(render_text(result))

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        try:
            with Path(summary_path).open("a", encoding="utf-8") as fh:
                fh.write(render_markdown(result))
        except OSError as exc:
            print(f"warning: could not write GitHub step summary: {exc}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

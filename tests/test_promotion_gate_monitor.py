import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


monitor = load_module(
    "promotion_gate_monitor",
    ROOT / "scripts" / "promotion-gate-monitor.py",
)
sender = load_module(
    "promotion_gate_sender",
    ROOT / "scripts" / "send-promotion-alert.py",
)


class DummyResult:
    def __init__(self, status):
        self.status = status
        self.observations_with_metadata = 1 if status != "GREEN" else 0
        self.active_findings = 1 if status != "GREEN" else 0
        self.qualified_behavior_violations = 1 if status in {"CANDIDATE", "PROMOTE"} else 0
        self.layer_counts = {"behavior": 1} if status != "GREEN" else {}
        self.repeated_patterns = (
            [
                {
                    "skill": "diagnose",
                    "invariant_id": "evidence-before-change",
                    "occurrences": 2,
                    "independent_tasks": 2,
                    "task_ids": ["task-1", "task-2"],
                    "has_reproducible": True,
                    "has_fixture_ready": True,
                    "has_reproducible_fixture_ready": True,
                }
            ]
            if status in {"CANDIDATE", "PROMOTE"}
            else []
        )
        self.reasons = [f"status is {status}"]
        self.recommendations = ["review evidence"]


class FakeEvaluator:
    DEFAULT_OBSERVATIONS = Path("unused-observations")
    DEFAULT_POLICY = Path("unused-policy")

    def __init__(self, status):
        self.status = status

    def scan_observations(self, _):
        return []

    def load_policy(self, _):
        return {}

    def evaluate(self, _observations, _policy):
        return DummyResult(self.status)


class PromotionGateMonitorTest(unittest.TestCase):
    def test_pending_candidate_remains_notify_required_until_receipt(self):
        with tempfile.TemporaryDirectory() as td:
            state_dir = Path(td)
            original = monitor._load_evaluator
            try:
                monitor._load_evaluator = lambda: FakeEvaluator("CANDIDATE")
                first = monitor.run(state_dir)
                second = monitor.run(state_dir)
            finally:
                monitor._load_evaluator = original
            self.assertEqual("true", first["notify_required"])
            self.assertEqual("true", second["notify_required"])
            self.assertEqual("false", second["semantic_changed"])

    def test_successful_send_marks_receipt_and_suppresses_duplicate(self):
        with tempfile.TemporaryDirectory() as td:
            state_dir = Path(td)
            original = monitor._load_evaluator
            try:
                monitor._load_evaluator = lambda: FakeEvaluator("PROMOTE")
                monitor.run(state_dir)
            finally:
                monitor._load_evaluator = original

            calls = []

            def transport(token, chat_id, text):
                calls.append((token, chat_id, text))
                return {"ok": True}

            sent = sender.send(
                state_dir / "latest.json",
                token="token",
                chat_id="123",
                transport=transport,
            )
            self.assertTrue(sent)
            self.assertEqual(1, len(calls))

            original = monitor._load_evaluator
            try:
                monitor._load_evaluator = lambda: FakeEvaluator("PROMOTE")
                result = monitor.run(state_dir)
            finally:
                monitor._load_evaluator = original
            self.assertEqual("false", result["notify_required"])

    def test_green_resets_notification_receipt(self):
        with tempfile.TemporaryDirectory() as td:
            state_dir = Path(td)
            latest = state_dir / "latest.json"
            latest.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "result": {"status": "CANDIDATE"},
                        "alert_fingerprint": "old",
                        "notification": {
                            "last_sent_fingerprint": "old",
                            "last_sent_at": "2026-09-20T00:00:00+00:00",
                        },
                    }
                ),
                encoding="utf-8",
            )
            original = monitor._load_evaluator
            try:
                monitor._load_evaluator = lambda: FakeEvaluator("GREEN")
                monitor.run(state_dir)
            finally:
                monitor._load_evaluator = original
            payload = json.loads(latest.read_text(encoding="utf-8"))
            self.assertIsNone(payload["notification"]["last_sent_fingerprint"])
            self.assertIsNone(payload["notification"]["last_sent_at"])

    def test_missing_telegram_secrets_keeps_alert_pending(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "latest.json"
            path.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "result": {
                            "status": "CANDIDATE",
                            "active_findings": 1,
                            "qualified_behavior_violations": 1,
                            "reasons": ["repeated violation"],
                            "recommendations": ["review evidence"],
                        },
                        "alert_fingerprint": "abc",
                        "notification": {
                            "last_sent_fingerprint": None,
                            "last_sent_at": None,
                        },
                    }
                ),
                encoding="utf-8",
            )
            old_token = sender.os.environ.pop("TELEGRAM_BOT_TOKEN", None)
            old_chat = sender.os.environ.pop("TELEGRAM_CHAT_ID", None)
            try:
                self.assertFalse(sender.send(path, token="", chat_id=""))
            finally:
                if old_token is not None:
                    sender.os.environ["TELEGRAM_BOT_TOKEN"] = old_token
                if old_chat is not None:
                    sender.os.environ["TELEGRAM_CHAT_ID"] = old_chat
            payload = json.loads(path.read_text(encoding="utf-8"))
            self.assertIsNone(payload["notification"]["last_sent_fingerprint"])

    def test_message_contains_gate_status_and_reason(self):
        payload = {
            "result": {
                "status": "PROMOTE",
                "active_findings": 2,
                "qualified_behavior_violations": 2,
                "reasons": ["same invariant repeated"],
                "recommendations": ["explicit review required"],
            }
        }
        message = sender.build_message(
            payload,
            repository="stanleyrprose/chatgpt-skills",
            run_url="https://example.invalid/run",
        )
        self.assertIn("PROMOTE", message)
        self.assertIn("same invariant repeated", message)
        self.assertIn("stanleyrprose/chatgpt-skills", message)


if __name__ == "__main__":
    unittest.main()

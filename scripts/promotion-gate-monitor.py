#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import sys
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STATE_DIR = ROOT / "state" / "promotion-gate"
EVALUATOR = ROOT / "scripts" / "evaluate-promotion-gate.py"
ALERT_STATUSES = {"CANDIDATE", "PROMOTE"}


def _load_evaluator():
    spec = importlib.util.spec_from_file_location("promotion_gate_evaluator", EVALUATOR)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load evaluator: {EVALUATOR}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _fingerprint(result: dict[str, Any]) -> str | None:
    if result["status"] not in ALERT_STATUSES:
        return None
    alert_material = {
        "status": result["status"],
        "reasons": result["reasons"],
        "repeated_patterns": result["repeated_patterns"],
        "recommendations": result["recommendations"],
    }
    return hashlib.sha256(_canonical_json(alert_material).encode("utf-8")).hexdigest()


def _read_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{path}: expected JSON object")
    return payload


def _append_history(path: Path, entry: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(_canonical_json(entry) + "\n")


def _write_outputs(values: dict[str, str]) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT")
    if not output_path:
        return
    with Path(output_path).open("a", encoding="utf-8") as fh:
        for key, value in values.items():
            fh.write(f"{key}={value}\n")


def run(state_dir: Path = DEFAULT_STATE_DIR) -> dict[str, Any]:
    evaluator = _load_evaluator()
    observations = evaluator.scan_observations(evaluator.DEFAULT_OBSERVATIONS)
    policy = evaluator.load_policy(evaluator.DEFAULT_POLICY)
    gate_result = evaluator.evaluate(observations, policy)
    result = asdict(gate_result)

    state_dir.mkdir(parents=True, exist_ok=True)
    latest_path = state_dir / "latest.json"
    history_path = state_dir / "history.jsonl"
    previous = _read_json(latest_path)

    previous_result = previous.get("result") if previous else None
    semantic_changed = previous_result != result
    alert_fingerprint = _fingerprint(result)

    previous_notification = previous.get("notification", {}) if previous else {}
    if not isinstance(previous_notification, dict):
        previous_notification = {}
    last_sent_fingerprint = previous_notification.get("last_sent_fingerprint")
    last_sent_at = previous_notification.get("last_sent_at")

    if result["status"] not in ALERT_STATUSES:
        last_sent_fingerprint = None
        last_sent_at = None

    payload = {
        "schema_version": 1,
        "result": result,
        "alert_fingerprint": alert_fingerprint,
        "notification": {
            "last_sent_fingerprint": last_sent_fingerprint,
            "last_sent_at": last_sent_at,
        },
    }

    latest_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    if semantic_changed:
        _append_history(
            history_path,
            {
                "recorded_at": datetime.now(timezone.utc).isoformat(),
                "result": result,
                "alert_fingerprint": alert_fingerprint,
            },
        )

    notify_required = bool(
        alert_fingerprint and alert_fingerprint != last_sent_fingerprint
    )

    outputs = {
        "status": result["status"],
        "semantic_changed": str(semantic_changed).lower(),
        "notify_required": str(notify_required).lower(),
        "alert_fingerprint": alert_fingerprint or "",
    }
    _write_outputs(outputs)

    print(f"Promotion Gate monitor: {result['status']}")
    print(f"Semantic result changed: {str(semantic_changed).lower()}")
    print(f"Telegram notification required: {str(notify_required).lower()}")
    return {
        **outputs,
        "latest_path": str(latest_path),
        "history_path": str(history_path),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Persist Promotion Gate state and decide whether Telegram notification is required."
    )
    parser.add_argument(
        "--state-dir",
        type=Path,
        default=DEFAULT_STATE_DIR,
        help="directory containing latest.json and history.jsonl",
    )
    args = parser.parse_args()
    try:
        run(args.state_dir)
    except (OSError, ValueError, json.JSONDecodeError, RuntimeError) as exc:
        print(f"Promotion Gate monitor failed: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STATE = ROOT / "state" / "promotion-gate" / "latest.json"
ALERT_STATUSES = {"CANDIDATE", "PROMOTE"}


def build_message(
    payload: dict[str, Any],
    *,
    repository: str | None = None,
    run_url: str | None = None,
) -> str:
    result = payload["result"]
    status = result["status"]
    emoji = "🚨" if status == "PROMOTE" else "⚠️"
    lines = [
        f"{emoji} ChatGPT Skills Promotion Gate: {status}",
        "",
        f"Active findings: {result['active_findings']}",
        f"Qualified behavior violations: {result['qualified_behavior_violations']}",
    ]
    if repository:
        lines.append(f"Repository: {repository}")
    if result.get("reasons"):
        lines.extend(["", "Reasons:"])
        lines.extend(f"- {reason}" for reason in result["reasons"][:5])
    if result.get("recommendations"):
        lines.extend(["", "Next action:"])
        lines.extend(f"- {item}" for item in result["recommendations"][:3])
    if run_url:
        lines.extend(["", f"GitHub Actions: {run_url}"])
    lines.extend(
        [
            "",
            "PROMOTE/CANDIDATE is evidence for review, not automatic authorization to change the architecture.",
        ]
    )
    return "\n".join(lines)


def _telegram_post(token: str, chat_id: str, text: str) -> dict[str, Any]:
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    body = urllib.parse.urlencode(
        {
            "chat_id": chat_id,
            "text": text,
            "disable_web_page_preview": "true",
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"Telegram Bot API HTTP {exc.code}") from None
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Telegram Bot API network error: {exc.reason}") from None
    if not payload.get("ok"):
        raise RuntimeError("Telegram Bot API returned ok=false")
    return payload


def send(
    state_path: Path = DEFAULT_STATE,
    *,
    token: str | None = None,
    chat_id: str | None = None,
    repository: str | None = None,
    run_url: str | None = None,
    transport=_telegram_post,
) -> bool:
    payload = json.loads(state_path.read_text(encoding="utf-8"))
    result = payload.get("result", {})
    status = result.get("status")
    fingerprint = payload.get("alert_fingerprint")
    notification = payload.setdefault("notification", {})

    if status not in ALERT_STATUSES or not fingerprint:
        print(f"Telegram alert not required for status {status!r}.")
        return False
    if notification.get("last_sent_fingerprint") == fingerprint:
        print("Telegram alert already sent for this fingerprint.")
        return False

    token = token or os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = chat_id or os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print(
            "Telegram alert pending: TELEGRAM_BOT_TOKEN and/or TELEGRAM_CHAT_ID "
            "GitHub Secret is not configured."
        )
        return False

    message = build_message(payload, repository=repository, run_url=run_url)
    transport(token, chat_id, message)

    notification["last_sent_fingerprint"] = fingerprint
    notification["last_sent_at"] = datetime.now(timezone.utc).isoformat()
    state_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Telegram alert sent for Promotion Gate {status}.")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Send a Promotion Gate CANDIDATE/PROMOTE alert through Telegram."
    )
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE)
    args = parser.parse_args()
    repository = os.environ.get("GITHUB_REPOSITORY")
    server = os.environ.get("GITHUB_SERVER_URL")
    run_id = os.environ.get("GITHUB_RUN_ID")
    run_url = (
        f"{server}/{repository}/actions/runs/{run_id}"
        if server and repository and run_id
        else None
    )
    try:
        send(args.state, repository=repository, run_url=run_url)
    except (OSError, ValueError, json.JSONDecodeError, RuntimeError) as exc:
        print(f"Telegram alert failed: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODEL_CASES = ROOT / "tests" / "skill-routing-cases.json"
BUILD_REGISTRY = ROOT / "scripts" / "build-registry.py"

SCAN_EXTS = {
    ".md",
    ".markdown",
    ".py",
    ".sh",
    ".bash",
    ".zsh",
    ".js",
    ".mjs",
    ".cjs",
    ".ts",
    ".ps1",
    ".rb",
    ".pl",
    ".txt",
    ".yaml",
    ".yml",
    ".json",
    ".toml",
}
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}
MAX_FILE_BYTES = 1_000_000
MODEL_MIN_OVERLAP = 2
MODEL_MIN_MARGIN = 1
SUPPRESS_MARKER = "skillscan:allow"

STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "before",
    "by",
    "for",
    "from",
    "in",
    "into",
    "is",
    "it",
    "of",
    "on",
    "or",
    "the",
    "this",
    "to",
    "with",
}

CRITICAL_PATTERNS = (
    (
        "EXEC01",
        re.compile(r"(?:curl|wget)\b[^\n|]{0,200}\|\s*(?:sudo\s+)?(?:ba|z|da|fi)?sh\b", re.IGNORECASE),
        "remote content is piped directly into a shell",
    ),
    (
        "EXEC02",
        re.compile(r"base64\s+(?:-d|-D|--decode)\b[^\n]{0,120}\|\s*(?:sudo\s+)?(?:ba|z)?sh\b", re.IGNORECASE),
        "base64-decoded data is piped into a shell",
    ),
    (
        "EXEC03",
        re.compile(r"(?:\bexec|\beval)\s*\([^\n]{0,160}(?:b64decode|fromhex|codecs\.decode|rot13)", re.IGNORECASE),
        "decoded content is executed dynamically",
    ),
    (
        "CRED01",
        re.compile(r"~/\.ssh\b|/\.ssh/|\bid_rsa\b|\bid_ed25519\b|\.aws/credentials", re.IGNORECASE),
        "skill touches high-risk credential files",
    ),
    (
        "CRED02",
        re.compile(r"security\s+(?:find-generic-password|find-internet-password|dump-keychain)", re.IGNORECASE),
        "skill queries the macOS keychain",
    ),
    (
        "EXEC04",
        re.compile(r"(?:iwr|irm|invoke-webrequest|downloadstring)[^\n]{0,160}\|\s*iex\b", re.IGNORECASE),
        "remote PowerShell content is piped into Invoke-Expression",
    ),
)

NETWORK_PATTERNS = (
    re.compile(r"^\s*(?:import|from)\s+(?:requests|httpx|aiohttp|urllib3?|socket|http\b)", re.IGNORECASE | re.MULTILINE),
    re.compile(r"\burllib\.request\b|\bhttp\.client\b|\bsocket\.(?:socket|create_connection)\b", re.IGNORECASE),
    re.compile(r"\bfetch\s*\(|\baxios\b|new\s+WebSocket\s*\(", re.IGNORECASE),
    re.compile(r"\b(?:curl|wget)\s+[^\n]*https?://", re.IGNORECASE),
)

ENV_ENUM_PATTERNS = (
    re.compile(r"dict\(os\.environ\)|os\.environ\.items\(\)|os\.environ\.copy\(\)", re.IGNORECASE),
    re.compile(r"JSON\.stringify\(process\.env\)|Object\.(?:entries|keys)\(process\.env\)", re.IGNORECASE),
    re.compile(r"(?<![\w-])printenv\b", re.IGNORECASE),
)


@dataclass(frozen=True)
class Finding:
    check: str
    severity: str
    path: str
    line: int
    message: str


def load_build_registry():
    spec = importlib.util.spec_from_file_location("build_registry", BUILD_REGISTRY)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load build-registry.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def normalize_exact(value: str) -> str:
    return " ".join(value.strip().casefold().split())


def active_skills(skills: list[dict], invocation: str | None = None) -> list[dict]:
    selected = [skill for skill in skills if skill["status"] == "active"]
    if invocation is not None:
        selected = [skill for skill in selected if skill["invocation"] == invocation]
    return selected


def lint_skills(skills: list[dict]) -> list[str]:
    errors: list[str] = []
    for skill in skills:
        path = ROOT / skill["path"]
        if path.parent.name != skill["name"]:
            errors.append(
                f"{skill['path']}: directory name must match frontmatter name {skill['name']!r}"
            )
        if skill["status"] == "active" and not path.is_file():
            errors.append(f"{skill['path']}: active skill path does not exist")
    return errors


def user_exact_map(skills: list[dict]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for skill in active_skills(skills, "user"):
        triggers = [skill["name"], *skill["aliases"]]
        for trigger in triggers:
            key = normalize_exact(str(trigger))
            previous = mapping.get(key)
            if previous is not None and previous != skill["name"]:
                raise ValueError(
                    f"user trigger collision: {trigger!r} maps to both {previous!r} and {skill['name']!r}"
                )
            mapping[key] = skill["name"]
    return mapping


def evaluate_user_exact_aliases(skills: list[dict]) -> list[str]:
    errors: list[str] = []
    mapping = user_exact_map(skills)
    for skill in active_skills(skills, "user"):
        for trigger in [skill["name"], *skill["aliases"]]:
            resolved = mapping.get(normalize_exact(str(trigger)))
            if resolved != skill["name"]:
                errors.append(
                    f"user exact trigger {trigger!r} should resolve to {skill['name']!r}, got {resolved!r}"
                )
    model_names = {skill["name"] for skill in active_skills(skills, "model")}
    leaked = sorted(set(mapping.values()) & model_names)
    if leaked:
        errors.append("user exact trigger map leaked model-invoked skills: " + ", ".join(leaked))
    return errors


def _stem(word: str) -> str:
    for suffix in ("ing", "ed", "es", "s"):
        if word.endswith(suffix) and len(word) - len(suffix) >= 3:
            return word[: -len(suffix)]
    return word


def tokens(text: str) -> set[str]:
    result: set[str] = set()
    for word in re.findall(r"[a-z0-9']+", text.casefold()):
        if len(word) < 3 or word in STOP_WORDS:
            continue
        result.add(_stem(word))
    return result


def model_score(prompt: str, description: str) -> int:
    return len(tokens(prompt) & tokens(description))


def load_model_cases(path: Path = MODEL_CASES) -> list[dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    cases = payload.get("model_semantic")
    if not isinstance(cases, list) or not cases:
        raise ValueError(f"{path.relative_to(ROOT)}: model_semantic must be a non-empty list")
    return cases


def evaluate_model_cases(skills: list[dict], cases: list[dict]) -> list[str]:
    errors: list[str] = []
    model_skills = active_skills(skills, "model")
    descriptions = {skill["name"]: str(skill["description"]) for skill in model_skills}
    names = set(descriptions)
    covered_expected: set[str] = set()

    for case in cases:
        case_id = str(case.get("id", "<missing-id>"))
        prompt = case.get("prompt")
        expected = case.get("expected")
        if not isinstance(prompt, str) or not prompt.strip():
            errors.append(f"{case_id}: prompt must be a non-empty string")
            continue
        if expected is not None and expected not in names:
            errors.append(f"{case_id}: expected model skill {expected!r} is not active")
            continue
        if expected is not None:
            covered_expected.add(expected)

        scores = {name: model_score(prompt, desc) for name, desc in descriptions.items()}
        if not scores:
            errors.append(f"{case_id}: no active model-invoked skills")
            continue
        ranked = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
        best_name, best_score = ranked[0]
        runner_up = ranked[1][1] if len(ranked) > 1 else 0

        if expected is None:
            if best_score >= MODEL_MIN_OVERLAP:
                errors.append(
                    f"{case_id}: negative case overlaps {best_name!r} too strongly ({best_score} tokens)"
                )
            continue

        expected_score = scores[expected]
        if expected_score < MODEL_MIN_OVERLAP:
            errors.append(
                f"{case_id}: expected {expected!r} has only {expected_score} overlapping tokens"
            )
        if best_name != expected:
            errors.append(
                f"{case_id}: routed lexically to {best_name!r}, expected {expected!r}; scores={scores}"
            )
        if expected_score - runner_up < MODEL_MIN_MARGIN:
            errors.append(
                f"{case_id}: expected {expected!r} does not clear runner-up by {MODEL_MIN_MARGIN}; scores={scores}"
            )

    missing = sorted(names - covered_expected)
    if missing:
        errors.append("active model-invoked skills missing positive routing cases: " + ", ".join(missing))
    return errors


def iter_skill_files(skill_dir: Path):
    for path in sorted(skill_dir.rglob("*")):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.casefold() not in SCAN_EXTS:
            continue
        try:
            if path.stat().st_size > MAX_FILE_BYTES:
                continue
        except OSError:
            continue
        yield path


def security_scan(skills: list[dict]) -> list[Finding]:
    findings: list[Finding] = []
    for skill in skills:
        skill_dir = (ROOT / skill["path"]).parent
        for path in iter_skill_files(skill_dir):
            text = path.read_text(encoding="utf-8", errors="replace")
            rel = path.relative_to(ROOT).as_posix()
            for line_no, line in enumerate(text.splitlines(), start=1):
                if SUPPRESS_MARKER in line:
                    continue
                for check, pattern, message in CRITICAL_PATTERNS:
                    if pattern.search(line):
                        findings.append(Finding(check, "CRITICAL", rel, line_no, message))

            has_network = any(pattern.search(text) for pattern in NETWORK_PATTERNS)
            has_env_enum = any(pattern.search(text) for pattern in ENV_ENUM_PATTERNS)
            if has_network and has_env_enum:
                findings.append(
                    Finding(
                        "EXFIL01",
                        "CRITICAL",
                        rel,
                        0,
                        "same skill file enumerates the process environment and makes network calls",
                    )
                )
    return findings


def run() -> int:
    build_registry = load_build_registry()
    try:
        skills = build_registry.discover()
        errors = lint_skills(skills)
        errors.extend(evaluate_user_exact_aliases(skills))
        errors.extend(evaluate_model_cases(skills, load_model_cases()))
        findings = security_scan(skills)
    except (OSError, ValueError, json.JSONDecodeError, RuntimeError) as exc:
        print(f"quality gate setup failed: {exc}", file=sys.stderr)
        return 1

    for finding in findings:
        location = f"{finding.path}:{finding.line}" if finding.line else finding.path
        print(
            f"[{finding.severity}] {finding.check} {location} — {finding.message}",
            file=sys.stderr,
        )
    errors.extend(
        f"security {finding.check} at {finding.path}:{finding.line or '-'} — {finding.message}"
        for finding in findings
        if finding.severity == "CRITICAL"
    )

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    user_count = len(active_skills(skills, "user"))
    model_count = len(active_skills(skills, "model"))
    print(
        "Skill CI Quality Gate PASS — "
        f"{len(skills)} skills linted; {user_count} user-invoked exact-trigger sets; "
        f"{model_count} model-invoked descriptions; security scan clean."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(run())

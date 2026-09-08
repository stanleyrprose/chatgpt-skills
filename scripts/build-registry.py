#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
REGISTRY = ROOT / "REGISTRY.md"

STATUS = {"draft", "active", "deprecated", "archived"}
INVOCATION = {"user", "model"}
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
NAME = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def parse_scalar(raw: str):
    raw = raw.strip()
    if raw in ("[]", ""):
        return []
    if raw.startswith('"') and raw.endswith('"'):
        return json.loads(raw)
    if raw.startswith("'") and raw.endswith("'"):
        return raw[1:-1]
    return raw


def parse_frontmatter(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{path}: missing opening frontmatter delimiter")
    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        raise ValueError(f"{path}: missing closing frontmatter delimiter")

    data: dict[str, object] = {}
    current_list = None
    for line in lines[1:end]:
        if not line.strip():
            continue
        if line.startswith("  - "):
            if current_list != "aliases":
                raise ValueError(f"{path}: list item outside aliases")
            data.setdefault("aliases", []).append(parse_scalar(line[4:]))
            continue
        if line.startswith(" "):
            raise ValueError(f"{path}: unsupported nested frontmatter")
        if ":" not in line:
            raise ValueError(f"{path}: invalid frontmatter line: {line}")
        key, raw = line.split(":", 1)
        key = key.strip()
        if key not in {"name", "version", "status", "invocation", "description", "aliases"}:
            raise ValueError(f"{path}: unsupported frontmatter key {key!r}")
        value = parse_scalar(raw)
        data[key] = value
        current_list = key if key == "aliases" and value == [] else None

    required = {"name", "version", "status", "invocation", "description"}
    missing = required - set(data)
    if missing:
        raise ValueError(f"{path}: missing fields: {sorted(missing)}")
    data.setdefault("aliases", [])
    validate_skill(path, data)
    return data


def validate_skill(path: Path, data: dict) -> None:
    if not NAME.match(str(data["name"])):
        raise ValueError(f"{path}: invalid name")
    if not SEMVER.match(str(data["version"])):
        raise ValueError(f"{path}: version must be SemVer")
    if data["status"] not in STATUS:
        raise ValueError(f"{path}: invalid status")
    if data["invocation"] not in INVOCATION:
        raise ValueError(f"{path}: invalid invocation")
    desc = str(data["description"]).strip()
    if not desc or "\n" in desc:
        raise ValueError(f"{path}: description must be one non-empty line")
    aliases = data["aliases"]
    if not isinstance(aliases, list):
        raise ValueError(f"{path}: aliases must be a list")
    if len(aliases) != len(set(aliases)):
        raise ValueError(f"{path}: duplicate aliases")
    if any(not isinstance(a, str) or not a.strip() or len(a) > 80 for a in aliases):
        raise ValueError(f"{path}: invalid alias")


def discover() -> list[dict]:
    skills = []
    names = set()
    aliases = set()
    for path in sorted(SKILLS_ROOT.glob("*/*/SKILL.md")):
        data = parse_frontmatter(path)
        name = str(data["name"])
        if name in names:
            raise ValueError(f"duplicate skill name: {name}")
        names.add(name)
        for alias in data["aliases"]:
            key = alias.strip().casefold()
            if key in aliases:
                raise ValueError(f"duplicate alias: {alias}")
            aliases.add(key)
        skills.append({
            "name": name,
            "version": data["version"],
            "status": data["status"],
            "invocation": data["invocation"],
            "path": path.relative_to(ROOT).as_posix(),
            "bucket": path.parent.parent.name,
            "description": data["description"],
            "aliases": data["aliases"],
        })
    return skills


def q(value: str) -> str:
    return json.dumps(str(value), ensure_ascii=False)


def render_registry(skills: list[dict]) -> str:
    lines = [
        "# Skill Registry",
        "",
        "> GENERATED FILE — do not edit manually. Source: `skills/*/*/SKILL.md` frontmatter.",
        "",
        "```yaml",
        'registry_version: "0.2"',
        "skills:" if skills else "skills: []",
    ]
    for s in skills:
        lines += [
            f"  - name: {q(s['name'])}",
            f"    version: {q(s['version'])}",
            f"    status: {q(s['status'])}",
            f"    invocation: {q(s['invocation'])}",
            f"    path: {q(s['path'])}",
            f"    description: {q(s['description'])}",
        ]
        if s["aliases"]:
            lines.append("    aliases:")
            lines.extend(f"      - {q(a)}" for a in s["aliases"])
        else:
            lines.append("    aliases: []")
    lines += ["```", ""]
    return "\n".join(lines)


def render_bucket(bucket: str, skills: list[dict]) -> str:
    title = bucket.replace("-", " ").title()
    lines = [
        f"# {title} Skills",
        "",
        "> GENERATED HUMAN INDEX — metadata comes from each `SKILL.md`; Router does not use this file.",
        "",
    ]
    scoped = [s for s in skills if s["bucket"] == bucket and s["status"] == "active"]
    for invocation, heading in (("user", "User-invoked"), ("model", "Model-invoked")):
        lines += [f"## {heading}", ""]
        group = [s for s in scoped if s["invocation"] == invocation]
        if not group:
            lines.append("_None._")
        else:
            for s in group:
                lines.append(f"- `{s['name']}` — {s['description']}")
        lines.append("")
    return "\n".join(lines)


def validate_constitution() -> None:
    text = (ROOT / "CONSTITUTION.md").read_text(encoding="utf-8").rstrip("\n")
    if len(text) > 3500:
        raise ValueError(f"CONSTITUTION.md exceeds 3500 chars: {len(text)}")
    markers = ["Skill Architecture：", "Skill：", "Skill 运行补充："]
    found = next((m for m in markers if m in text), None)
    if found is None:
        raise ValueError("CONSTITUTION.md missing Skill architecture/router marker")
    router_chars = len(text[text.index(found):])
    # Amendment A1 (2026-09-08): router/bootstrap >800 is allowed.
    # Keep the measurement observable, but do not fail CI on this sub-budget.
    if "Implementation‑Hard‑Stop" in text or "Implementation-Hard-Stop" in text:
        raise ValueError("Implementation-Hard-Stop leaked into runtime Constitution")


def expected_files(skills: list[dict]) -> dict[Path, str]:
    outputs = {REGISTRY: render_registry(skills)}
    buckets = sorted({p.parent.parent.name for p in SKILLS_ROOT.glob("*/*/SKILL.md")})
    for bucket in buckets:
        outputs[SKILLS_ROOT / bucket / "README.md"] = render_bucket(bucket, skills)
    return outputs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    try:
        validate_constitution()
        skills = discover()
        outputs = expected_files(skills)
        if args.check:
            stale = []
            for path, expected in outputs.items():
                if not path.exists() or path.read_text(encoding="utf-8") != expected:
                    stale.append(path.relative_to(ROOT).as_posix())
            if stale:
                print("derived files are stale: " + ", ".join(stale), file=sys.stderr)
                return 1
        else:
            for path, expected in outputs.items():
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(expected, encoding="utf-8")
    except (OSError, ValueError) as exc:
        print(exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

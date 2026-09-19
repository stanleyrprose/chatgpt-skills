# chatgpt-skills

Git-backed Global Constitution and reusable Skill Architecture for ChatGPT context governance.

## Architecture

```text
Global Constitution
    ↓
Global Reusable Skills
    ↓
Project Rules
    ↓
Project State
    ↓
Authorized Tools / Runtime / Evidence
```

This repository deliberately does **not** implement repo-local Skills, a deterministic router, RAG, a daemon, or an Agent OS.

## Important risk statement

Routing is prompt-based and inherently non-deterministic. False positives, false negatives, tool-read failures, sticky context, and attention spillover are expected failure modes. The design mitigates them with conservative routing, progressive disclosure, generated discovery metadata, state anchors, fallback rules, tests, and observation; it does not claim deterministic workflow guarantees.

## Canonical sources

- `CONSTITUTION.md` — authored/versioned Global Constitution; deployed to ChatGPT Custom Instructions.
- `skills/*/*/SKILL.md` — canonical metadata + HOW for each reusable Skill.
- `.agents/invocation.md` — cross-Skill invocation mechanics.
- `REGISTRY.md` — generated compact discovery index; do not hand-edit.
- `GOAL.md` — current implementation checkpoint.
- Project-specific rules/state stay in each project repository.

## Shared reference contracts

`shared/` contains plain references only; they are not Skills and do not grant Tool/MCP capability or authorization.

- `shared/research-routing-evidence-contract.md` — smallest-adequate research routing, claim-level evidence promotion, fallback, time semantics, and capability/authorization/persistence separation.
- `shared/agent-execution-integrity-contract.md` — task identity, reconciled checkpoints, duplicate-safe side effects, baseline-bound execution, evidence-bound review, bounded repair, and recovery semantics for long or cross-Agent work.

## Validation

CI is intentionally dependency-light and validates the authored Skill sources before accepting changes:

- `python3 scripts/build-registry.py --check` validates Constitution/frontmatter rules and derived Registry/README drift.
- `python3 scripts/skill_quality_gate.py` adds Skill metadata lint, requires explicit `Verification` / `Rationalization Traps` / `Red Flags` discipline sections for every active Skill, runs blocking static security checks, checks exact registered triggers for `invocation: user`, and runs deterministic description-routing evals for `invocation: model`.
- `python3 -m unittest discover -s tests -p "test_*.py"` runs the focused regression suite.

The model-routing eval is a CI sanity check over model-facing descriptions, not a deterministic runtime router. A clean static security scan is necessary but not sufficient; human review still owns ambiguous or novel patterns.

## Frozen baseline

v0.5 was frozen and implementation-authorized on 2026-09-08.

Current Constitution release: **v1.5.2 lossless migration target**.

Frozen PRD SHA-256:

`923ab0ab856d9cbbe81899c2bf895c4df7d12287d70254060f082f8fbdde864a`

## Maintenance rule

**One rule → one canonical home.** Pointers and short summaries are allowed; duplicated executable rule bodies are not.

## Implementation amendment

A1 (2026-09-08) explicitly retains decision-quality and PKS-capture behavior in `CONSTITUTION.md`, and makes the Router/bootstrap 800-character sub-budget non-blocking while retaining the 3500-character Constitution budget. See `docs/implementation-amendment-a1-2026-09-08.md`.

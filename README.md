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

## Skill authoring and contribution

- `docs/skill-anatomy.md` documents the cross-Skill authoring contract and evaluation model.
- `CONTRIBUTING.md` defines the minimal change workflow for this repository.
- `SECURITY.md` defines security-reporting and validation boundaries.

### License

Licensed under the **Apache License 2.0**. See `LICENSE`.

## Shared reference contracts

`shared/` contains plain references only; they are not Skills and do not grant Tool/MCP capability or authorization.

- `shared/research-routing-evidence-contract.md` — smallest-adequate research routing, claim-level evidence promotion, fallback, time semantics, and capability/authorization/persistence separation.
- `shared/agent-execution-integrity-contract.md` — task identity, reconciled checkpoints, duplicate-safe side effects, baseline-bound execution, evidence-bound review, bounded repair, and recovery semantics for long or cross-Agent work.
- `shared/project-constraints-ratchet-contract.md` — baseline-first quality constraints, direction-aware must-not-regress guardrails, evidence-based ratchets, bounded exceptions, and anti-weakening review rules.

## Validation

CI is intentionally dependency-light and validates the authored Skill sources before accepting changes:

- `python3 scripts/build-registry.py --check` validates Constitution/frontmatter rules and derived Registry/README drift.
- `python3 scripts/skill_quality_gate.py` adds Skill metadata lint, required discipline sections, blocking static security checks, exact user-trigger isolation, deterministic model-description routing evals, and deterministic per-Skill contract regressions that protect approved workflow invariants.
- `python3 scripts/evaluate-promotion-gate.py` reports `GREEN / WATCH / CANDIDATE / PROMOTE` from explicitly marked event-triggered observations; report states are non-blocking and do not authorize architecture changes.
- `scripts/promotion-gate-monitor.py` persists semantic Gate transitions; `.github/workflows/monitor-promotion-gate.yml` runs it every six hours and can notify Telegram through `@github_stan_bot` when `CANDIDATE/PROMOTE` requires attention. See `docs/promotion-gate-monitoring.md`.
- `python3 -m unittest discover -s tests -p "test_*.py"` runs the focused regression suite.

The model-routing eval is a CI sanity check over model-facing descriptions, not a deterministic runtime router. A clean static security scan is necessary but not sufficient; human review still owns ambiguous or novel patterns.

## Versioning and releases

Repository releases, the Constitution, and individual Skills use independent version surfaces.

- Current repository release: `v0.5.0`
- Current Constitution: `v1.5.2`
- Active Skills: `0.1.1`

See `CHANGELOG.md` and `docs/release-process.md`.

Release `v0.5.0` is the first public repository snapshot of the frozen v0.5 architecture.

## Frozen baseline

v0.5 was frozen and implementation-authorized on 2026-09-08.

Current Constitution release: **v1.5.2 lossless migration target**.

Frozen PRD SHA-256:

`923ab0ab856d9cbbe81899c2bf895c4df7d12287d70254060f082f8fbdde864a`

## Maintenance rule

**One rule → one canonical home.** Pointers and short summaries are allowed; duplicated executable rule bodies are not.

## Implementation amendment

A1 (2026-09-08) explicitly retains decision-quality and PKS-capture behavior in `CONSTITUTION.md`, and makes the Router/bootstrap 800-character sub-budget non-blocking while retaining the 3500-character Constitution budget. See `docs/implementation-amendment-a1-2026-09-08.md`.

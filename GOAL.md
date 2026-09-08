# GOAL — Implement ChatGPT Context Constitution + Git-Backed Skills v0.5

**Status:** IN PROGRESS
**Branch:** `bootstrap/v0.5-phase1`
**Frozen PRD:** `PRD-ChatGPT-Context-Constitution-and-Git-Backed-Skill-Architecture-v0.5-frozen.md`
**Frozen PRD SHA-256:** `923ab0ab856d9cbbe81899c2bf895c4df7d12287d70254060f082f8fbdde864a`
**Authorization:** User explicitly froze v0.5 and authorized implementation on 2026-09-08.

## Goal

Implement the frozen v0.5 architecture without expanding scope.

## Current checkpoint

Phase 0: COMPLETE — frozen + implementation authorized.
Phase 1: COMPLETE — structural baseline validated.
Phase 2: COMPLETE — five initial Skills + derived index validated.
Phase 3: IN PROGRESS — migration audit COMPLETE; Amendment A1 recorded; v1.5.1 target validated; branch CI PASS; exact UI deployment + activation smoke tests pending.
Phase 4: PENDING — real engineering E2E.
Phase 5: PENDING — first-10-task observation window.

## Frozen invariants

- `SKILL.md` frontmatter + body is the canonical Skill source.
- `REGISTRY.md` is generated/derived; never hand-maintained as a second truth source.
- Global Skills only; no repo-local Skill layer.
- User-invoked: `implement`, `to-spec`, `handoff`.
- Model-invoked: `diagnose`, `code-review`.
- At most one Primary; automatic Secondary must be model-invoked.
- Global Execution semantics do not imply `implement` outside software/repo engineering context.
- No DB, RAG, deterministic router service, daemon, or new MCP.
- Runtime-Hard-Stop and Implementation-Hard-Stop remain isolated.
- CI-007 decision-quality and CI-008 PKS-capture remain in `CONSTITUTION.md`.
- Router/bootstrap size is observable but not a hard CI gate; Constitution total ≤3500 remains the budget gate.

## Closure target

`bootstrap → skills → validate → PR → CI → Phase 3 deployment gate → E2E → observation handoff`

## Phase 3 gate evidence

- Migration audit: PASS, unresolved=0.
- CI-007/CI-008: present in `CONSTITUTION.md`.
- Constitution v1.5.1 length: 2594 Unicode chars.
- Router/bootstrap: measured at 760 chars; non-blocking per Amendment A1.
- Local Registry validator: PASS.
- Regression test: PASS.
- GitHub PR #1 head `91c2152`: two `validate` checks PASS.
- Derived deployment artifact: `dist/custom-instructions-v1.5.1.txt` (must match `CONSTITUTION.md`).

Remaining gate: save the exact artifact into ChatGPT Custom Instructions UI, then run Constitution activation / state-anchor / Project Discovery smoke tests.

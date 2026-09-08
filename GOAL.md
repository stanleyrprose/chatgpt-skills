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
Phase 3: COMPLETE — v1.5.2 lossless migration deployed by user; activation/state-anchor/Project Discovery smoke PASS.
Phase 4: IN PROGRESS — real engineering E2E candidate discovery/selection.
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
- Lossless source baseline: user-supplied current Custom Instructions archived and migrated.
- CI-007/CI-008/CI-011: explicit in `CONSTITUTION.md`.
- Constitution v1.5.2 length: 3326 Unicode chars.
- `dist/custom-instructions-v1.5.2.txt` == canonical `CONSTITUTION.md` by build validation.
- Constitution/code-bearing commit `515dd6c`: PR #1 `validate` checks PASS.
- UI deployment: user explicitly confirmed v1.5.2 was saved on 2026-09-08. No product API is available here to independently read back UI bytes; activation evidence is therefore behavioral + user confirmation, not UI introspection.
- Activation smoke: PASS — continuation semantics, Chinese default, direct connected-tool execution, no redundant re-confirmation.
- State-anchor smoke: PASS — `implement@0.1.0` Primary → `code-review@0.1.0` Secondary → pop to Primary.
- Project Discovery smoke: PASS — branch reads followed AGENTS → GOAL → frozen baseline → Constitution/Registry/Skill; no stale-memory substitution.

## Phase 4 entry condition

Use a real, non-toy engineering repository with existing Git history and a meaningful CI/test/verification path. Do not mutate the target repository merely to manufacture an E2E; choose an actual authorized engineering task or a safe read/review path that exercises Constitution → Skill → Project Rules → Project State → Tool/Evidence.

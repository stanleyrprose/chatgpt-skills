# GOAL — Implement ChatGPT Context Constitution + Git-Backed Skills v0.5

**Status:** IN PROGRESS
**Branch:** `main`
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
Phase 4: COMPLETE — real-repo E2E on `stanleyrprose/mac-browser-plane` PASS WITH ENVIRONMENT LIMITATION.
Phase 5: ACTIVE — first-10-real-task observation window is 1/10 after the P1 research-routing/evidence reference task on 2026-09-10.

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

`bootstrap → skills → validate → PR → CI → Phase 3 deployment gate → E2E → merge → Phase 5 observation window`

## Phase 3 gate evidence

- Migration audit: PASS, unresolved=0.
- Lossless source baseline: user-supplied current Custom Instructions archived and migrated.
- CI-007/CI-008/CI-011: explicit in `CONSTITUTION.md`.
- Constitution v1.5.2 length: 3326 Unicode chars.
- `dist/custom-instructions-v1.5.2.txt` == canonical `CONSTITUTION.md` by build validation.
- Constitution/code-bearing commit `515dd6c`: PR #1 `validate` checks PASS.
- UI deployment: user explicitly confirmed v1.5.2 was saved on 2026-09-08. No product API is available here to independently read back UI bytes; activation evidence is behavioral + user confirmation, not UI introspection.
- Activation smoke: PASS — continuation semantics, Chinese default, direct connected-tool execution, no redundant re-confirmation.
- State-anchor smoke: PASS — `implement@0.1.0` Primary → `code-review@0.1.0` Secondary → pop to Primary.
- Project Discovery smoke: PASS — branch reads followed AGENTS → GOAL → frozen baseline → Constitution/Registry/Skill; no stale-memory substitution.

## Phase 4 evidence

Target: `stanleyrprose/mac-browser-plane`.

Why it qualifies:
- real operational Browser Plane repo, not a toy;
- active Git history, branches, `src/`, `tests/`, `.github/` and runtime docs;
- Mac local workspace contained current uncommitted work on `feat/lightpanda-engine-router`.

E2E path exercised:
- Constitution → `implement` Primary → project `AGENTS.md` → missing `GOAL.md` handled gracefully → branch/current local state → affected code/tests → model Secondary `code-review`/`diagnose` → tool feedback/evidence.
- Local current-state evidence beat remote assumptions: CodexPro revealed six uncommitted Lightpanda-related files on the Mac branch; no mutation/commit was performed in that target repo.
- `tests/test_core.py`: 26/26 PASS.
- non-agent runnable set `tests/test_core.py tests/test_provider_launchd.py`: 27/27 PASS.
- full `pytest`: collection blocked by missing optional `agent` extra (`mcp==2.1.1`) in the current CodexPro Python environment; classified as environment coverage limitation, not Lightpanda regression evidence. No dependency was installed merely for the E2E.
- Lightpanda routing implementation/manifest/doctor were consistent: ephemeral C1 and read-only C3 may use Lightpanda with safe Chrome fallback; persistent/C2/interactive C3/screenshot/download/force require Chrome; Lightpanda remains optional readiness.
- CodexPro `show_changes` workspace-selection inconsistency was treated as a local tool degradation; no diff was guessed.
- Handoff completeness contract checked statically; `handoff` itself was not auto-invoked because it is user-invoked.

Result: **PASS WITH ENVIRONMENT LIMITATION**.

## P1 research-routing/evidence reference

Status: **COMPLETE (reference-only)** on 2026-09-10.

- Added `shared/research-routing-evidence-contract.md` as the canonical plain reference for smallest-adequate research routing and claim-level evidence semantics.
- Preserved the frozen v0.5 runtime architecture: no sixth Skill, no deterministic router, no DB/RAG/daemon, no new MCP, and no Tool permission expansion.
- The contract separates Route Plan, capability, authorization, discovery, original-source inspection, claim qualification, fallback, time semantics, and persistence.
- Upstream `mcncarl/yichen-skills` was used only as an architectural study source; no upstream code/schema/executable workflow/substantial text was copied because its license restricts redistribution/commercial use.
- Phase 5 real-task observation recorded in `observations/2026-09-10-phase5-01-p1-research-contract.md`.

## Phase 5 rule

Phase 5 is operational observation, not a build-time excuse to fabricate tasks. The next 10 genuine tasks that naturally use this architecture should be recorded per `OBSERVATION_TEMPLATE.md`; after task 10, perform the observation review and decide whether any Future Work is evidence-justified.

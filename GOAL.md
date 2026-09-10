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
Phase 5: ACTIVE — first-10-real-task observation window is 4/10 after the real SignalForge guarded execution E2E on 2026-09-10.

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

## P1 real research E2E

Status: **PASS (no contract change required)** on 2026-09-10.

- Real task: forecast Myanmar 5G market competition and derive MPT strategy under that forecast, with `as_of=2026-09-10`.
- Correctly escalated to `deep_research` because the decision required current competitive structure, historical/technical context, forward scenarios, and strategy implications.
- Claim-level evidence semantics prevented operator self-claims about market leadership from being promoted into an uncontested fact.
- Public research confirmed the national early-2027 5G target, 2.6 GHz/n41 direction, TDD synchronization requirements, operator readiness signals, macro power constraints, and MPT partnership/support changes.
- Two material uncertainties remained explicit rather than guessed: latest regulator-grade market-share ranking and final per-operator 2.6 GHz bandwidth allocation.
- No database, persisted claim ledger, extra search service, new Skill, or runtime change was needed.
- Observation recorded in `observations/2026-09-10-phase5-02-myanmar-5g-research-e2e.md`.

## P2 Agent Execution Integrity reference

Status: **COMPLETE (reference-only)** on 2026-09-10.

- Added `shared/agent-execution-integrity-contract.md` as the canonical plain reference for long/cross-Agent execution integrity.
- Defined three activation levels (`none`, `tracked`, `guarded`) so protocol overhead is paid only when interruption, stale state, cross-Agent handoff, or duplicate side effects materially matter.
- Defined task identity, reconciled checkpoints, drift classification, operation receipts, plan-to-baseline binding, evidence-bound review, cross-Agent handoff identity, bounded repair by reconciliation points, recovery, and terminal-state semantics.
- Replaced any strong exactly-once claim with duplicate-safe / effectively-once semantics: ambiguous side effects must be reconciled against actual target state before retry.
- Code review found and fixed two low-risk design issues before PR: operation identity now includes desired postcondition, and bounded repair no longer conflicts with authorized Autonomous Mode.
- Preserved the frozen v0.5 architecture: no new Skill, workflow engine, state service, queue, DB/RAG/daemon, MCP, CodexPro runtime change, or Tool permission expansion.
- Upstream `mcncarl/yichen-skills` was used only as an architectural study source; no fixed state machine, message envelope, schema, executable workflow, code, or substantial text was copied.
- Observation recorded in `observations/2026-09-10-phase5-03-p2-execution-integrity.md`.

## P2 real SignalForge guarded execution E2E

Status: **PASS WITH RUNTIME FINDINGS** on 2026-09-10.

- Applied the P2 guarded contract to a real SignalForge assurance task under stable task id `sf-p2-guarded-20260910-assurance-v1`.
- The local SignalForge `CHECKPOINT.md` was stale relative to GitHub main/GOAL; the mismatch was correctly classified as forward drift and execution resumed from stronger current evidence instead of replaying the old checkpoint.
- An executor failure before dispatch was distinguished from an ambiguous timeout. When the later Cloud-side `execute-handoff` call timed out while the local Codex process was still running, process and handoff state were reconciled and no duplicate executor was started.
- The run exposed a real terminal-receipt gap: after the local executor ended, `.ai-bridge/handoff-run-state.json` could remain `running` and no trustworthy finalized execution receipt was available.
- The run also exposed a real mutation-gate gap: Codex pushed and merged SignalForge PR #143 and PR #144 before the requested ChatGPT evidence-bound review, proving a plan-text instruction alone is not an enforcement boundary.
- SignalForge Auditor v1 itself added a useful read-only assurance surface for source health, bounded MPT/MYTEL coverage reconciliation, ATOM procurement-surface triggering, deadline consistency, signal trace integrity and delivery receipt integrity while keeping global external completeness explicitly unproven.
- Evidence-bound review found one over-strong independence claim. Follow-up SignalForge PR #145 narrowed the contract to implementation-independent plus `coverage_semantic_independence=PARTIAL`; targeted tests remained 12/12, full suite 275/275, and exact-head CI passed before merge to SignalForge `main@ecdfe9e59f337be22d8f88c811968b13c6d2554f`.
- No BKK production deployment or Telegram send was performed in this E2E.
- These observations justify evaluating narrow CodexPro runtime support for reliable terminal receipts and mutation-boundary enforcement; they do not authorize broader workflow infrastructure.
- Observation recorded in `observations/2026-09-10-phase5-04-signalforge-p2-e2e.md`.

## Phase 5 rule

Phase 5 is operational observation, not a build-time excuse to fabricate tasks. The next 10 genuine tasks that naturally use this architecture should be recorded per `OBSERVATION_TEMPLATE.md`; after task 10, perform the observation review and decide whether any Future Work is evidence-justified.

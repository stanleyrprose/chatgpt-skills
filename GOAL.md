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
Phase 5: ACTIVE — first-10-real-task observation window is 8/10 after the SignalForge provenance audit task on 2026-09-13.

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
- These observations justified a narrow CodexPro runtime evaluation rather than broader workflow infrastructure.
- Observation recorded in `observations/2026-09-10-phase5-04-signalforge-p2-e2e.md`.

## P2.1 evidence-driven CodexPro runtime fix

Status: **IMPLEMENTATION COMPLETE / UPSTREAM INTEGRATION PENDING** on 2026-09-11.

- Implemented only the two concrete runtime gaps demonstrated by the SignalForge E2E: reliable handoff lifecycle/terminal receipts and a handoff-scoped accidental remote-mutation gate.
- Final fork result: `stanleyrprose/codexpro@77b56d4512a5aa8cc081db67aa7cb94ce140f0da`; canonical upstream review remains `rebel0789/codexpro` PR #130 and was intentionally not self-merged.
- Signal lifecycle now uses non-terminal `interrupting` while child termination is in progress; terminal `interrupted` is written only after actual child exit. Stale in-flight receipts derive `orphaned` only when both parent and child are gone.
- Non-completed terminal process states carry `execution_outcome=unknown` and `reconcile_required=true`, preserving duplicate-safe retry semantics.
- Default handoff execution blocks standard remote Git/GitHub mutation paths and strips common GitHub token environment variables; explicit `--allow-remote-mutations` restores those paths. This is intentionally an accidental-side-effect guard, not a security sandbox.
- Code review caught and fixed two material lifecycle defects: a live child must prevent orphan classification, and Node `child.killed` cannot be used as proof of process exit; stubborn child termination now escalates based on actual exit/signal state.
- Verification PASS on macOS (`build`, targeted handoff smoke, MCP/full smoke, stress, `git diff --check`) and on exact head via the repository's Ubuntu + Windows GitHub Actions matrix, run `34510223428`.
- The user's fork initially had Actions enabled but no registered workflow; a repository Actions disable/enable refresh registered the existing CI workflow without changing source or upstream settings, after which the CI-only PR ran and was closed without merge.
- No npm publish, upstream merge, or local production hot-patch was performed. P2 returns to observation-only/frozen status unless a future real task supplies new evidence.
- Observation recorded in `observations/2026-09-11-phase5-05-p2-runtime-fix.md`.

## SignalForge Production Assurance v1 real task

Status: **PASS WITH EXPLICIT COMPLETENESS LIMITS** on 2026-09-11.

- Recovered current SignalForge state from GitHub/GOAL and the live Bangkok runtime rather than chat history; exact production application release was `bd86efcaa5699f1aa5082459cd57882b8ffe4e73`.
- Read-only production evidence returned `27/27 GREEN / backlog0 / 209 canonical / 45 raw signals / 21 known historical noise / 24 effective signals / 9 current opportunities / 4 immediate Telegram receipts / immediate pending0`.
- Only 7/27 sources have proven effective yield so far (4 actionable + 3 signal-only); remaining observation windows are too short to justify pruning before the existing 30-day gate.
- Network Auditor returned `PASS / findings0` while preserving `external_completeness=NOT_PROVEN`: MPT S13 bounded recent reconciliation PASS/missing0, MYTEL S41 15 official vs 15 canonical/missing0, ATOM official sitemap `NO_TRIGGER`.
- The preceding 24h showed 1330 source runs, 1581 evidence fetches, 2995 parsed items, 34 changed records and zero business signals. One S35 read timeout had already recovered to GREEN with no backlog.
- The naturally scheduled 08:30 Yangon Business Digest completed `0/SUCCESS`, sent provider message `8`, persisted the second daily success receipt, and a post-send dry-run returned `deduplicated=true / pending0`; no manual Telegram send was invoked by the audit.
- Current decision focus was `industry:1022` closing 2026-09-11 16:00, `energy:235` and `mofa:59800` closing 2026-09-18, with `doms:12735` deliberately kept REVIEW/deadline UNKNOWN rather than guessed.
- SignalForge report PR #152 passed exact-head CI and merged as `6ef5118bbf2b80547ce85662c765f9b81e84b5d6`; no runtime, database, source-acquisition, parser, qualification or delivery policy change was made.
- Observation recorded in `observations/2026-09-11-phase5-06-signalforge-production-assurance.md`.

## Skill CI Quality Gate

Status: **IMPLEMENTED / REMOTE CI PASS** on 2026-09-12.

- Added `scripts/skill_quality_gate.py` as a stdlib-only CI validator; no third-party dependency, runtime service, router daemon, DB, RAG, or MCP was introduced.
- Gate responsibilities are deliberately split by invocation mode: active `invocation:user` Skills get exact registered-trigger ownership checks only; active `invocation:model` Skills get deterministic description-routing evals with positive-case coverage plus negative/single-keyword cases.
- Static security scanning covers all discovered Skills regardless of status and blocks high-risk execution/credential/exfiltration patterns; this remains a pattern-based gate, not a complete security proof.
- Code review found and fixed two gate-integrity issues before closure: non-active Skills are now scanned, and every active model Skill must have at least one positive routing case.
- Local validation PASS: Registry/Constitution check, Quality Gate, Python compile, `git diff --check`, and 8/8 focused unittests.
- PR #10 remote `validate` checks PASS on runs `34704087220` and `34704098371` for implementation commit `82368d5`.
- Observation recorded in `observations/2026-09-12-phase5-07-skill-ci-quality-gate.md`.

## SignalForge deterministic-boundary / provenance audit

Status: **PASS / CODE MERGED / PRODUCTION UNCHANGED** on 2026-09-13.

- Recovered current SignalForge Git/GOAL state rather than relying on chat history; audit found no LLM scoring fallback in the core Signal/qualification/priority/Signal Quality path.
- Implemented only two read-model auditability gaps: unchanged Signal Quality v1 now exposes evidence `0–85` plus context `0–15` subtotals, and relevance categories expose whether they came from item text, source-policy name, or explicit source fallback.
- Model-invoked `code-review` caught one provenance-label ambiguity before closure; the fix distinguished item-text keyword evidence from source-policy-name keyword evidence without changing category decisions.
- SignalForge targeted tests passed 20/20, full suite 325/325, PR #168 exact-head verify run `34733280734` passed, and PR #168 squash-merged as `29c5280ca4e28f9fd502b60845f5f0f7b0a1d624`.
- No Bangkok deployment, production DB mutation, source refresh, Telegram send, score/band/priority change, Signal creation rule, schema, acquisition or topology change was performed.
- Observation recorded in `observations/2026-09-13-phase5-08-signalforge-provenance-audit.md`.

## Phase 5 rule

Phase 5 is operational observation, not a build-time excuse to fabricate tasks. The next 10 genuine tasks that naturally use this architecture should be recorded per `OBSERVATION_TEMPLATE.md`; after task 10, perform the observation review and decide whether any Future Work is evidence-justified.

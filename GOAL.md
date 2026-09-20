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
Phase 5: COMPLETE — 10/10 genuine tasks observed; final review on 2026-09-13 found no evidence requiring a v0.5 Skill-architecture expansion.

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

## MCP capability identity / scoping audit

Status: **PASS / CROSS-REPO CODE MERGED / PRODUCTION UNCHANGED** on 2026-09-13.

- Confirmed the CodexPro Browser bridge is a single fixed `mac-browser-mcp` stdio server with an exact ten-tool allowlist, not a multi-MCP aggregator; cross-server plain-name collision is therefore not a current failure mode.
- Confirmed SignalForge Provider already fail-closes provider/source/capability/tool/target-role/URL/SHA/TTL/run-limit identity and keeps C3 ambiguous replay gated by explicit `retry_safe`; the C3 evidence-only contract remains disabled and current production PIC usage is C0-scoped.
- Found and fixed one real cross-boundary invariant gap: actual Provider result bytes are now checked against the original per-request `max_bytes` both before Mac submit and independently before Bangkok acceptance.
- Corrected stale current CodexPro bridge documentation to the ten-tool + narrow SignalForge pull-SSH authority model; no capability was added or widened.
- Validation PASS: Mac targeted 16/16, full 74/74, live stdio discovery 10/10; SignalForge targeted 31/31, full 326/326; `git diff --check` PASS in both repos.
- Mac PR #45 exact-head tests PASS on runs `34749514994` and `34749534187`; SignalForge PR #169 exact-head verify PASS on run `34749539874`. GitHub merge APIs returned transient 5xx, so the exact tested heads were fast-forwarded to main and GitHub recorded both PRs as merged.
- Final repository heads: `mac-browser-plane@2d101f82f510c2c0bd7f8a3c05c297927803f095`; `signalforge@85681b3575e139c8ed2dd93550e2d00ee5087ccf`.
- No Mac runtime reinstall, Bangkok deployment, production DB mutation, source refresh or Telegram send was performed.
- Observation recorded in `observations/2026-09-13-phase5-09-mcp-capability-scoping.md`.

## AWR structured quota UI contract

Status: **PASS / CODE MERGED / PRODUCTION UNCHANGED** on 2026-09-13.

- Recovered current AWR state first and confirmed the requested Codex/SuperGrok quota rings were already implemented; the task did not rebuild completed UI.
- Found a real semantic-boundary defect: React treated any quota label containing `hour` as `5H`, so future hourly windows could be silently mislabeled.
- Added backward-compatible backend API quota semantics (`five_hour`, `weekly`, `monthly`, `other`) and made React filter/order/render from semantic kind; known old payload forms remain supported without broad substring guessing.
- Code review tightened fallback parsing so `24 hour`, `Hourly`, `Twenty Five Hour`, and `Biweekly` stay `other`; Codex 5H+Weekly and SuperGrok Weekly remain unchanged.
- Validation PASS: focused backend tests 2/2, frontend `npm run lint`, frontend `npm run build`, and `git diff --check`; PR #9 exact-head `unified-deliberation` run `34754261407` passed.
- Agent War Room PR #9 squash-merged as `7d45bc70ae0ea3a1d7e6bbce03735ff40ba9c024`.
- No CopilotKit/AG-UI/new UI runtime, auth change, credential mutation, DB/schema change, provider inference, or production deployment was introduced.
- Observation recorded in `observations/2026-09-13-phase5-10-awr-structured-ui-contract.md`.

## Phase 5 final observation review

Status: **COMPLETE — KEEP v0.5 FROZEN ARCHITECTURE** on 2026-09-13.

Evidence across the 10 genuine tasks supports the existing architecture rather than an expansion:

- **Routing:** explicit user-invoked vs model-invoked separation held across real engineering/research work. No repeated routing failure justifies a deterministic router service, sixth Skill, DB/RAG layer, or daemon.
- **Research/evidence:** the plain shared research contract was sufficient for a real Myanmar 5G strategy task; uncertainty and claim qualification were handled without a persisted claim system.
- **Execution integrity:** real long-task failures were correctly solved at the executor/runtime boundary (CodexPro lifecycle receipts and mutation guard), not by adding orchestration infrastructure to the Skill layer.
- **Production assurance:** SignalForge tasks repeatedly benefited from explicit evidence, provenance, completeness limits, and deterministic-vs-reasoning boundaries; these are reusable principles, not evidence for another Skill.
- **Quality control:** the Skill CI Quality Gate provided useful deterministic metadata/routing/security checks while preserving model routing at runtime.
- **Capability/security boundaries:** Browser MCP/SignalForge audits showed strong existing identity/scoping and exposed one concrete byte-budget gap; the right fix was a narrow invariant at both trust boundaries, not MCP namespacing or a multi-server router.
- **UI semantics:** AWR showed that structured meaning should live in the backend/API contract and rendering in React; the right fix was one semantic field, not a generative-UI framework.
- **Minimalism:** multiple tasks explicitly avoided tempting but unsupported architecture additions. In each case, a smaller local contract/test/invariant fixed the demonstrated problem.

Decision:

1. Keep the five-Skill v0.5 architecture frozen: user-invoked `implement`, `to-spec`, `handoff`; model-invoked `diagnose`, `code-review`.
2. Keep shared references as plain documents; do not promote P1/P2 or structured-UI ideas into new Skills/services without new recurring evidence.
3. End the mandatory first-10-task observation window. Future observations become **event-triggered only** under `OBSERVATION_TEMPLATE.md` when there is a routing anomaly, user correction, doc/code desync, tool degradation, security boundary finding, or similarly material evidence.
4. Future-work ideas remain conditional, not authorized: true model-based semantic routing eval only if deterministic metadata eval proves insufficient; MCP namespacing only if a real multi-server aggregation collision appears; broader structured UI schemas only when another concrete UI semantic-drift bug appears.

## Post-Phase-5 Skill discipline hardening

Status: **PASS WITH REMOTE CI ENVIRONMENT LIMITATION** on 2026-09-20.

- Studied `addyosmani/agent-skills` for transferable Skill-quality mechanisms and adopted only the narrow anti-rationalization / red-flag / verification pattern; no lifecycle-router, Persona framework, human-gate chain, new Skill, service, DB/RAG layer, daemon, MCP, or Tool permission change was introduced.
- All five active Skills were bumped from `0.1.0` to `0.1.1` and now carry explicit `Rationalization Traps`, `Red Flags`, and `Verification` sections while preserving the frozen v0.5 invocation mapping and Primary/Secondary model.
- `scripts/skill_quality_gate.py` now requires those three sections on every active Skill and requires at least two actionable list items per section; focused regression coverage was added.
- Independent review caught and fixed one real gate-integrity defect before closure: the initial Markdown-section regex was over-escaped and would not have matched normal headings.
- Exact local equivalents of the GitHub workflow passed on the PR branch: `build-registry.py --check` PASS, Skill CI Quality Gate PASS, and focused unittests 10/10 PASS.
- PR #14 remote `validate` jobs did not start because GitHub reported an account billing/spending-limit condition ("recent account payments have failed or spending limit needs to be increased"). This is recorded as an external CI environment limitation, not a code/test failure; no billing or spending setting was changed.
- True LLM behavioral eval remains deferred: the current deterministic gate now checks routing plus discipline-contract structure without adding token cost, non-deterministic model execution, or CI runtime dependencies.

## Public repository hardening

Status: **IMPLEMENTED / CI RESTORED** on 2026-09-20.

- Repository visibility was changed from private to public by explicit user instruction.
- Re-ran previously blocked main workflow run `35456087276`; after the repository became public, the `validate` job started normally and passed in 8 seconds, confirming the earlier billing/spending-limit error was an external private-runner limitation rather than a code failure.
- Added `docs/skill-anatomy.md` as the cross-Skill authoring contract while preserving each `SKILL.md` as the canonical per-Skill metadata/workflow source and keeping validators as machine enforcement.
- Added `CONTRIBUTING.md` and `SECURITY.md`, plus README pointers and explicit public-without-license status.
- Public hardening does not add a new Skill, router, service, RAG/DB/daemon, MCP, permission expansion, or LLM-in-CI dependency.
- No `LICENSE` file was added. License selection is intentionally deferred because choosing one grants reuse rights and requires an explicit maintainer legal/permission decision.
- Exact branch CI passed on runs `35487867705` and `35487884682`; after hardening the workflow to `actions/checkout@v6`, `contents: read`, and `persist-credentials: false`, exact-head run `35487922862` also PASSed.

## P1 project constraints / ratchet reference

Status: **IMPLEMENTED (reference-only)** on 2026-09-20.

- Added `shared/project-constraints-ratchet-contract.md` as a plain reference; it is not a Skill, CI service, policy engine, database, daemon, MCP, permission grant, or runtime.
- The contract requires baseline-first, direction-aware guardrails, separates the current guardrail from the improvement target, tightens guardrails only after verified improvement, and treats measurement changes/exceptions explicitly rather than silently weakening gates.
- Constraint evidence is split into external, project, and suite classes; maturity is written → scripted → tool-backed, with most projects expected to stop at the lowest sufficient level.
- Added anti-weakening review rules for threshold lowering, skipped tests/assertions, broad suppressions, denominator manipulation, missing-data relabeling, and stubs.
- Added a small optional `CONSTRAINTS.md` template and a SignalForge-oriented example without inventing current production values.
- Preserved the frozen five-Skill architecture and added no new runtime dependency or enforcement service.

## P1 deterministic Skill contract evals

Status: **IMPLEMENTED** on 2026-09-20.

- Added `tests/skill-contract-cases.json` with one deterministic contract set for every active Skill.
- Extended `scripts/skill_quality_gate.py` so every active Skill must have a contract fixture and every protected clause must remain present in the canonical `SKILL.md`; stale fixtures for non-active Skills also fail closed.
- Contract clauses protect already-approved workflow invariants such as evidence-before-fix, falsifiable hypotheses, independent code-review axes, implementation-authorization boundaries, exact handoff requirements, and Git/CI closure semantics.
- This is Tier 2 deterministic contract regression, not Tier 3 LLM behavioral eval: it detects semantic deletion/drift in Skill text but does not claim that a model will obey the Skill at runtime.
- Added focused unit coverage for current contracts, missing active-Skill coverage, and clause regression detection.
- No Skill body, invocation mode, Tool/MCP permission, runtime service, router, DB/RAG layer, or model-in-CI dependency was added.

## Phase 5 rule

Phase 5 is complete after 10 genuine tasks and the evidence review above. Do not manufacture further observation tasks. Record new observations only when a real event satisfies `OBSERVATION_TEMPLATE.md`; any architecture change still requires independent evidence and authorization.

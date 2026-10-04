  1 | # GOAL — Maintain ChatGPT Context Constitution + Git-Backed Skills
  2 | 
  3 | **Status:** IN PROGRESS
  4 | **Branch:** `main`
  5 | **Frozen PRD:** `PRD-ChatGPT-Context-Constitution-and-Git-Backed-Skill-Architecture-v0.5-frozen.md`
  6 | **Frozen PRD SHA-256:** `923ab0ab856d9cbbe81899c2bf895c4df7d12287d70254060f082f8fbdde864a`
  7 | **Authorization:** User explicitly froze v0.5 and authorized implementation on 2026-09-08. User explicitly authorized Amendment A2 adding `research-triad` on 2026-09-29 and Amendment A3 adding `douyin-tiktok-publish` on 2026-10-04.
  8 | 
  9 | ## Goal
 10 | 
 11 | Preserve the frozen v0.5 baseline while implementing only explicitly authorized amendments. Amendment A2 adds `research-triad`; Amendment A3 adds the bounded `douyin-tiktok-publish` personal workflow. Neither amendment authorizes broader framework expansion.
 12 | 
 13 | ## Current checkpoint
 14 | 
 15 | Phase 0: COMPLETE — frozen + implementation authorized.
 16 | Phase 1: COMPLETE — structural baseline validated.
 17 | Phase 2: COMPLETE — five initial Skills + derived index validated.
 18 | Phase 3: COMPLETE — v1.5.2 lossless migration deployed by user; activation/state-anchor/Project Discovery smoke PASS.
 19 | Phase 4: COMPLETE — real-repo E2E on `stanleyrprose/mac-browser-plane` PASS WITH ENVIRONMENT LIMITATION.
 20 | Phase 5: COMPLETE — 10/10 genuine tasks observed; final review on 2026-09-13 found no evidence requiring a v0.5 Skill-architecture expansion.
 21 | Amendment A2: COMPLETE — research-triad@0.1.0 merged through PR #30; exact-head and post-merge CI both PASS.
 22 | Amendment A3: IMPLEMENTED LOCALLY / VALIDATION PENDING — douyin-tiktok-publish@0.1.0.
 23 | 
 24 | ## Frozen invariants
 25 | 
 26 | - `SKILL.md` frontmatter + body is the canonical Skill source.
 27 | - `REGISTRY.md` is generated/derived; never hand-maintained as a second truth source.
 28 | - Global Skills only; no repo-local Skill layer.
 29 | - User-invoked current set: `implement`, `to-spec`, `handoff`, plus A2 `research-triad`.
 30 | - Model-invoked: `diagnose`, `code-review`, plus A3 `douyin-tiktok-publish`.
 31 | - At most one Primary; automatic Secondary must be model-invoked.
 32 | - Global Execution semantics do not imply `implement` outside software/repo engineering context.
 33 | - No DB, RAG, deterministic router service, daemon, or new MCP.
 34 | - Runtime-Hard-Stop and Implementation-Hard-Stop remain isolated.
 35 | - CI-007 decision-quality and CI-008 PKS-capture remain in `CONSTITUTION.md`.
 36 | - Router/bootstrap size is observable but not a hard CI gate; Constitution total ≤3500 remains the budget gate.
 37 | 
 38 | ## Closure target
 39 | 
 40 | `bootstrap → skills → validate → PR → CI → Phase 3 deployment gate → E2E → merge → Phase 5 observation window`
 41 | 
 42 | ## Phase 3 gate evidence
 43 | 
 44 | - Migration audit: PASS, unresolved=0.
 45 | - Lossless source baseline: user-supplied current Custom Instructions archived and migrated.
 46 | - CI-007/CI-008/CI-011: explicit in `CONSTITUTION.md`.
 47 | - Constitution v1.5.2 length: 3326 Unicode chars.
 48 | - `dist/custom-instructions-v1.5.2.txt` == canonical `CONSTITUTION.md` by build validation.
 49 | - Constitution/code-bearing commit `515dd6c`: PR #1 `validate` checks PASS.
 50 | - UI deployment: user explicitly confirmed v1.5.2 was saved on 2026-09-08. No product API is available here to independently read back UI bytes; activation evidence is behavioral + user confirmation, not UI introspection.
 51 | - Activation smoke: PASS — continuation semantics, Chinese default, direct connected-tool execution, no redundant re-confirmation.
 52 | - State-anchor smoke: PASS — `implement@0.1.0` Primary → `code-review@0.1.0` Secondary → pop to Primary.
 53 | - Project Discovery smoke: PASS — branch reads followed AGENTS → GOAL → frozen baseline → Constitution/Registry/Skill; no stale-memory substitution.
 54 | 
 55 | ## Phase 4 evidence
 56 | 
 57 | Target: `stanleyrprose/mac-browser-plane`.
 58 | 
 59 | Why it qualifies:
 60 | - real operational Browser Plane repo, not a toy;
 61 | - active Git history, branches, `src/`, `tests/`, `.github/` and runtime docs;
 62 | - Mac local workspace contained current uncommitted work on `feat/lightpanda-engine-router`.
 63 | 
 64 | E2E path exercised:
 65 | - Constitution → `implement` Primary → project `AGENTS.md` → missing `GOAL.md` handled gracefully → branch/current local state → affected code/tests → model Secondary `code-review`/`diagnose` → tool feedback/evidence.
 66 | - Local current-state evidence beat remote assumptions: CodexPro revealed six uncommitted Lightpanda-related files on the Mac branch; no mutation/commit was performed in that target repo.
 67 | - `tests/test_core.py`: 26/26 PASS.
 68 | - non-agent runnable set `tests/test_core.py tests/test_provider_launchd.py`: 27/27 PASS.
 69 | - full `pytest`: collection blocked by missing optional `agent` extra (`mcp==2.1.1`) in the current CodexPro Python environment; classified as environment coverage limitation, not Lightpanda regression evidence. No dependency was installed merely for the E2E.
 70 | - Lightpanda routing implementation/manifest/doctor were consistent: ephemeral C1 and read-only C3 may use Lightpanda with safe Chrome fallback; persistent/C2/interactive C3/screenshot/download/force require Chrome; Lightpanda remains optional readiness.
 71 | - CodexPro `show_changes` workspace-selection inconsistency was treated as a local tool degradation; no diff was guessed.
 72 | - Handoff completeness contract checked statically; `handoff` itself was not auto-invoked because it is user-invoked.
 73 | 
 74 | Result: **PASS WITH ENVIRONMENT LIMITATION**.
 75 | 
 76 | ## P1 research-routing/evidence reference
 77 | 
 78 | Status: **COMPLETE (reference-only)** on 2026-09-10.
 79 | 
 80 | - Added `shared/research-routing-evidence-contract.md` as the canonical plain reference for smallest-adequate research routing and claim-level evidence semantics.
 81 | - Preserved the frozen v0.5 runtime architecture: no sixth Skill, no deterministic router, no DB/RAG/daemon, no new MCP, and no Tool permission expansion.
 82 | - The contract separates Route Plan, capability, authorization, discovery, original-source inspection, claim qualification, fallback, time semantics, and persistence.
 83 | - Upstream `mcncarl/yichen-skills` was used only as an architectural study source; no upstream code/schema/executable workflow/substantial text was copied because its license restricts redistribution/commercial use.
 84 | - Phase 5 real-task observation recorded in `observations/2026-09-10-phase5-01-p1-research-contract.md`.
 85 | 
 86 | ## P1 real research E2E
 87 | 
 88 | Status: **PASS (no contract change required)** on 2026-09-10.
 89 | 
 90 | - Real task: forecast Myanmar 5G market competition and derive MPT strategy under that forecast, with `as_of=2026-09-10`.
 91 | - Correctly escalated to `deep_research` because the decision required current competitive structure, historical/technical context, forward scenarios, and strategy implications.
 92 | - Claim-level evidence semantics prevented operator self-claims about market leadership from being promoted into an uncontested fact.
 93 | - Public research confirmed the national early-2027 5G target, 2.6 GHz/n41 direction, TDD synchronization requirements, operator readiness signals, macro power constraints, and MPT partnership/support changes.
 94 | - Two material uncertainties remained explicit rather than guessed: latest regulator-grade market-share ranking and final per-operator 2.6 GHz bandwidth allocation.
 95 | - No database, persisted claim ledger, extra search service, new Skill, or runtime change was needed.
 96 | - Observation recorded in `observations/2026-09-10-phase5-02-myanmar-5g-research-e2e.md`.
 97 | 
 98 | ## P2 Agent Execution Integrity reference
 99 | 
100 | Status: **COMPLETE (reference-only)** on 2026-09-10.
101 | 
102 | - Added `shared/agent-execution-integrity-contract.md` as the canonical plain reference for long/cross-Agent execution integrity.
103 | - Defined three activation levels (`none`, `tracked`, `guarded`) so protocol overhead is paid only when interruption, stale state, cross-Agent handoff, or duplicate side effects materially matter.
104 | - Defined task identity, reconciled checkpoints, drift classification, operation receipts, plan-to-baseline binding, evidence-bound review, cross-Agent handoff identity, bounded repair by reconciliation points, recovery, and terminal-state semantics.
105 | - Replaced any strong exactly-once claim with duplicate-safe / effectively-once semantics: ambiguous side effects must be reconciled against actual target state before retry.
106 | - Code review found and fixed two low-risk design issues before PR: operation identity now includes desired postcondition, and bounded repair no longer conflicts with authorized Autonomous Mode.
107 | - Preserved the frozen v0.5 architecture: no new Skill, workflow engine, state service, queue, DB/RAG/daemon, MCP, CodexPro runtime change, or Tool permission expansion.
108 | - Upstream `mcncarl/yichen-skills` was used only as an architectural study source; no fixed state machine, message envelope, schema, executable workflow, code, or substantial text was copied.
109 | - Observation recorded in `observations/2026-09-10-phase5-03-p2-execution-integrity.md`.
110 | 
111 | ## P2 real SignalForge guarded execution E2E
112 | 
113 | Status: **PASS WITH RUNTIME FINDINGS** on 2026-09-10.
114 | 
115 | - Applied the P2 guarded contract to a real SignalForge assurance task under stable task id `sf-p2-guarded-20260910-assurance-v1`.
116 | - The local SignalForge `CHECKPOINT.md` was stale relative to GitHub main/GOAL; the mismatch was correctly classified as forward drift and execution resumed from stronger current evidence instead of replaying the old checkpoint.
117 | - An executor failure before dispatch was distinguished from an ambiguous timeout. When the later Cloud-side `execute-handoff` call timed out while the local Codex process was still running, process and handoff state were reconciled and no duplicate executor was started.
118 | - The run exposed a real terminal-receipt gap: after the local executor ended, `.ai-bridge/handoff-run-state.json` could remain `running` and no trustworthy finalized execution receipt was available.
119 | - The run also exposed a real mutation-gate gap: Codex pushed and merged SignalForge PR #143 and PR #144 before the requested ChatGPT evidence-bound review, proving a plan-text instruction alone is not an enforcement boundary.
120 | - SignalForge Auditor v1 itself added a useful read-only assurance surface for source health, bounded MPT/MYTEL coverage reconciliation, ATOM procurement-surface triggering, deadline consistency, signal trace integrity and delivery receipt integrity while keeping global external completeness explicitly unproven.
121 | - Evidence-bound review found one over-strong independence claim. Follow-up SignalForge PR #145 narrowed the contract to implementation-independent plus `coverage_semantic_independence=PARTIAL`; targeted tests remained 12/12, full suite 275/275, and exact-head CI passed before merge to SignalForge `main@ecdfe9e59f337be22d8f88c811968b13c6d2554f`.
122 | - No BKK production deployment or Telegram send was performed in this E2E.
123 | - These observations justified a narrow CodexPro runtime evaluation rather than broader workflow infrastructure.
124 | - Observation recorded in `observations/2026-09-10-phase5-04-signalforge-p2-e2e.md`.
125 | 
126 | ## P2.1 evidence-driven CodexPro runtime fix
127 | 
128 | Status: **IMPLEMENTATION COMPLETE / UPSTREAM INTEGRATION PENDING** on 2026-09-11.
129 | 
130 | - Implemented only the two concrete runtime gaps demonstrated by the SignalForge E2E: reliable handoff lifecycle/terminal receipts and a handoff-scoped accidental remote-mutation gate.
131 | - Final fork result: `stanleyrprose/codexpro@77b56d4512a5aa8cc081db67aa7cb94ce140f0da`; canonical upstream review remains `rebel0789/codexpro` PR #130 and was intentionally not self-merged.
132 | - Signal lifecycle now uses non-terminal `interrupting` while child termination is in progress; terminal `interrupted` is written only after actual child exit. Stale in-flight receipts derive `orphaned` only when both parent and child are gone.
133 | - Non-completed terminal process states carry `execution_outcome=unknown` and `reconcile_required=true`, preserving duplicate-safe retry semantics.
134 | - Default handoff execution blocks standard remote Git/GitHub mutation paths and strips common GitHub token environment variables; explicit `--allow-remote-mutations` restores those paths. This is intentionally an accidental-side-effect guard, not a security sandbox.
135 | - Code review caught and fixed two material lifecycle defects: a live child must prevent orphan classification, and Node `child.killed` cannot be used as proof of process exit; stubborn child termination now escalates based on actual exit/signal state.
136 | - Verification PASS on macOS (`build`, targeted handoff smoke, MCP/full smoke, stress, `git diff --check`) and on exact head via the repository's Ubuntu + Windows GitHub Actions matrix, run `34510223428`.
137 | - The user's fork initially had Actions enabled but no registered workflow; a repository Actions disable/enable refresh registered the existing CI workflow without changing source or upstream settings, after which the CI-only PR ran and was closed without merge.
138 | - No npm publish, upstream merge, or local production hot-patch was performed. P2 returns to observation-only/frozen status unless a future real task supplies new evidence.
139 | - Observation recorded in `observations/2026-09-11-phase5-05-p2-runtime-fix.md`.
140 | 
141 | ## SignalForge Production Assurance v1 real task
142 | 
143 | Status: **PASS WITH EXPLICIT COMPLETENESS LIMITS** on 2026-09-11.
144 | 
145 | - Recovered current SignalForge state from GitHub/GOAL and the live Bangkok runtime rather than chat history; exact production application release was `bd86efcaa5699f1aa5082459cd57882b8ffe4e73`.
146 | - Read-only production evidence returned `27/27 GREEN / backlog0 / 209 canonical / 45 raw signals / 21 known historical noise / 24 effective signals / 9 current opportunities / 4 immediate Telegram receipts / immediate pending0`.
147 | - Only 7/27 sources have proven effective yield so far (4 actionable + 3 signal-only); remaining observation windows are too short to justify pruning before the existing 30-day gate.
148 | - Network Auditor returned `PASS / findings0` while preserving `external_completeness=NOT_PROVEN`: MPT S13 bounded recent reconciliation PASS/missing0, MYTEL S41 15 official vs 15 canonical/missing0, ATOM official sitemap `NO_TRIGGER`.
149 | - The preceding 24h showed 1330 source runs, 1581 evidence fetches, 2995 parsed items, 34 changed records and zero business signals. One S35 read timeout had already recovered to GREEN with no backlog.
150 | - The naturally scheduled 08:30 Yangon Business Digest completed `0/SUCCESS`, sent provider message `8`, persisted the second daily success receipt, and a post-send dry-run returned `deduplicated=true / pending0`; no manual Telegram send was invoked by the audit.
151 | - Current decision focus was `industry:1022` closing 2026-09-11 16:00, `energy:235` and `mofa:59800` closing 2026-09-18, with `doms:12735` deliberately kept REVIEW/deadline UNKNOWN rather than guessed.
152 | - SignalForge report PR #152 passed exact-head CI and merged as `6ef5118bbf2b80547ce85662c765f9b81e84b5d6`; no runtime, database, source-acquisition, parser, qualification or delivery policy change was made.
153 | - Observation recorded in `observations/2026-09-11-phase5-06-signalforge-production-assurance.md`.
154 | 
155 | ## Skill CI Quality Gate
156 | 
157 | Status: **IMPLEMENTED / REMOTE CI PASS** on 2026-09-12.
158 | 
159 | - Added `scripts/skill_quality_gate.py` as a stdlib-only CI validator; no third-party dependency, runtime service, router daemon, DB, RAG, or MCP was introduced.
160 | - Gate responsibilities are deliberately split by invocation mode: active `invocation:user` Skills get exact registered-trigger ownership checks only; active `invocation:model` Skills get deterministic description-routing evals with positive-case coverage plus negative/single-keyword cases.
161 | - Static security scanning covers all discovered Skills regardless of status and blocks high-risk execution/credential/exfiltration patterns; this remains a pattern-based gate, not a complete security proof.
162 | - Code review found and fixed two gate-integrity issues before closure: non-active Skills are now scanned, and every active model Skill must have at least one positive routing case.
163 | - Local validation PASS: Registry/Constitution check, Quality Gate, Python compile, `git diff --check`, and 8/8 focused unittests.
164 | - PR #10 remote `validate` checks PASS on runs `34704087220` and `34704098371` for implementation commit `82368d5`.
165 | - Observation recorded in `observations/2026-09-12-phase5-07-skill-ci-quality-gate.md`.
166 | 
167 | ## SignalForge deterministic-boundary / provenance audit
168 | 
169 | Status: **PASS / CODE MERGED / PRODUCTION UNCHANGED** on 2026-09-13.
170 | 
171 | - Recovered current SignalForge Git/GOAL state rather than relying on chat history; audit found no LLM scoring fallback in the core Signal/qualification/priority/Signal Quality path.
172 | - Implemented only two read-model auditability gaps: unchanged Signal Quality v1 now exposes evidence `0–85` plus context `0–15` subtotals, and relevance categories expose whether they came from item text, source-policy name, or explicit source fallback.
173 | - Model-invoked `code-review` caught one provenance-label ambiguity before closure; the fix distinguished item-text keyword evidence from source-policy-name keyword evidence without changing category decisions.
174 | - SignalForge targeted tests passed 20/20, full suite 325/325, PR #168 exact-head verify run `34733280734` passed, and PR #168 squash-merged as `29c5280ca4e28f9fd502b60845f5f0f7b0a1d624`.
175 | - No Bangkok deployment, production DB mutation, source refresh, Telegram send, score/band/priority change, Signal creation rule, schema, acquisition or topology change was performed.
176 | - Observation recorded in `observations/2026-09-13-phase5-08-signalforge-provenance-audit.md`.
177 | 
178 | ## MCP capability identity / scoping audit
179 | 
180 | Status: **PASS / CROSS-REPO CODE MERGED / PRODUCTION UNCHANGED** on 2026-09-13.
181 | 
182 | - Confirmed the CodexPro Browser bridge is a single fixed `mac-browser-mcp` stdio server with an exact ten-tool allowlist, not a multi-MCP aggregator; cross-server plain-name collision is therefore not a current failure mode.
183 | - Confirmed SignalForge Provider already fail-closes provider/source/capability/tool/target-role/URL/SHA/TTL/run-limit identity and keeps C3 ambiguous replay gated by explicit `retry_safe`; the C3 evidence-only contract remains disabled and current production PIC usage is C0-scoped.
184 | - Found and fixed one real cross-boundary invariant gap: actual Provider result bytes are now checked against the original per-request `max_bytes` both before Mac submit and independently before Bangkok acceptance.
185 | - Corrected stale current CodexPro bridge documentation to the ten-tool + narrow SignalForge pull-SSH authority model; no capability was added or widened.
186 | - Validation PASS: Mac targeted 16/16, full 74/74, live stdio discovery 10/10; SignalForge targeted 31/31, full 326/326; `git diff --check` PASS in both repos.
187 | - Mac PR #45 exact-head tests PASS on runs `34749514994` and `34749534187`; SignalForge PR #169 exact-head verify PASS on run `34749539874`. GitHub merge APIs returned transient 5xx, so the exact tested heads were fast-forwarded to main and GitHub recorded both PRs as merged.
188 | - Final repository heads: `mac-browser-plane@2d101f82f510c2c0bd7f8a3c05c297927803f095`; `signalforge@85681b3575e139c8ed2dd93550e2d00ee5087ccf`.
189 | - No Mac runtime reinstall, Bangkok deployment, production DB mutation, source refresh or Telegram send was performed.
190 | - Observation recorded in `observations/2026-09-13-phase5-09-mcp-capability-scoping.md`.
191 | 
192 | ## AWR structured quota UI contract
193 | 
194 | Status: **PASS / CODE MERGED / PRODUCTION UNCHANGED** on 2026-09-13.
195 | 
196 | - Recovered current AWR state first and confirmed the requested Codex/SuperGrok quota rings were already implemented; the task did not rebuild completed UI.
197 | - Found a real semantic-boundary defect: React treated any quota label containing `hour` as `5H`, so future hourly windows could be silently mislabeled.
198 | - Added backward-compatible backend API quota semantics (`five_hour`, `weekly`, `monthly`, `other`) and made React filter/order/render from semantic kind; known old payload forms remain supported without broad substring guessing.
199 | - Code review tightened fallback parsing so `24 hour`, `Hourly`, `Twenty Five Hour`, and `Biweekly` stay `other`; Codex 5H+Weekly and SuperGrok Weekly remain unchanged.
200 | - Validation PASS: focused backend tests 2/2, frontend `npm run lint`, frontend `npm run build`, and `git diff --check`; PR #9 exact-head `unified-deliberation` run `34754261407` passed.
201 | - Agent War Room PR #9 squash-merged as `7d45bc70ae0ea3a1d7e6bbce03735ff40ba9c024`.
202 | - No CopilotKit/AG-UI/new UI runtime, auth change, credential mutation, DB/schema change, provider inference, or production deployment was introduced.
203 | - Observation recorded in `observations/2026-09-13-phase5-10-awr-structured-ui-contract.md`.
204 | 
205 | ## Phase 5 final observation review
206 | 
207 | Status: **COMPLETE — KEEP v0.5 FROZEN ARCHITECTURE** on 2026-09-13.
208 | 
209 | Evidence across the 10 genuine tasks supports the existing architecture rather than an expansion:
210 | 
211 | - **Routing:** explicit user-invoked vs model-invoked separation held across real engineering/research work. No repeated routing failure justifies a deterministic router service, sixth Skill, DB/RAG layer, or daemon.
212 | - **Research/evidence:** the plain shared research contract was sufficient for a real Myanmar 5G strategy task; uncertainty and claim qualification were handled without a persisted claim system.
213 | - **Execution integrity:** real long-task failures were correctly solved at the executor/runtime boundary (CodexPro lifecycle receipts and mutation guard), not by adding orchestration infrastructure to the Skill layer.
214 | - **Production assurance:** SignalForge tasks repeatedly benefited from explicit evidence, provenance, completeness limits, and deterministic-vs-reasoning boundaries; these are reusable principles, not evidence for another Skill.
215 | - **Quality control:** the Skill CI Quality Gate provided useful deterministic metadata/routing/security checks while preserving model routing at runtime.
216 | - **Capability/security boundaries:** Browser MCP/SignalForge audits showed strong existing identity/scoping and exposed one concrete byte-budget gap; the right fix was a narrow invariant at both trust boundaries, not MCP namespacing or a multi-server router.
217 | - **UI semantics:** AWR showed that structured meaning should live in the backend/API contract and rendering in React; the right fix was one semantic field, not a generative-UI framework.
218 | - **Minimalism:** multiple tasks explicitly avoided tempting but unsupported architecture additions. In each case, a smaller local contract/test/invariant fixed the demonstrated problem.
219 | 
220 | Decision:
221 | 
222 | 1. Keep the five-Skill v0.5 architecture frozen: user-invoked `implement`, `to-spec`, `handoff`; model-invoked `diagnose`, `code-review`.
223 | 2. Keep shared references as plain documents; do not promote P1/P2 or structured-UI ideas into new Skills/services without new recurring evidence.
224 | 3. End the mandatory first-10-task observation window. Future observations become **event-triggered only** under `OBSERVATION_TEMPLATE.md` when there is a routing anomaly, user correction, doc/code desync, tool degradation, security boundary finding, or similarly material evidence.
225 | 4. Future-work ideas remain conditional, not authorized: true model-based semantic routing eval only if deterministic metadata eval proves insufficient; MCP namespacing only if a real multi-server aggregation collision appears; broader structured UI schemas only when another concrete UI semantic-drift bug appears.
226 | 
227 | ## Post-Phase-5 Skill discipline hardening
228 | 
229 | Status: **PASS WITH REMOTE CI ENVIRONMENT LIMITATION** on 2026-09-20.
230 | 
231 | - Studied `addyosmani/agent-skills` for transferable Skill-quality mechanisms and adopted only the narrow anti-rationalization / red-flag / verification pattern; no lifecycle-router, Persona framework, human-gate chain, new Skill, service, DB/RAG layer, daemon, MCP, or Tool permission change was introduced.
232 | - All five active Skills were bumped from `0.1.0` to `0.1.1` and now carry explicit `Rationalization Traps`, `Red Flags`, and `Verification` sections while preserving the frozen v0.5 invocation mapping and Primary/Secondary model.
233 | - `scripts/skill_quality_gate.py` now requires those three sections on every active Skill and requires at least two actionable list items per section; focused regression coverage was added.
234 | - Independent review caught and fixed one real gate-integrity defect before closure: the initial Markdown-section regex was over-escaped and would not have matched normal headings.
235 | - Exact local equivalents of the GitHub workflow passed on the PR branch: `build-registry.py --check` PASS, Skill CI Quality Gate PASS, and focused unittests 10/10 PASS.
236 | - PR #14 remote `validate` jobs did not start because GitHub reported an account billing/spending-limit condition ("recent account payments have failed or spending limit needs to be increased"). This is recorded as an external CI environment limitation, not a code/test failure; no billing or spending setting was changed.
237 | - True LLM behavioral eval remains deferred: the current deterministic gate now checks routing plus discipline-contract structure without adding token cost, non-deterministic model execution, or CI runtime dependencies.
238 | 
239 | ## Public repository hardening
240 | 
241 | Status: **IMPLEMENTED / CI RESTORED** on 2026-09-20.
242 | 
243 | - Repository visibility was changed from private to public by explicit user instruction.
244 | - Re-ran previously blocked main workflow run `35456087276`; after the repository became public, the `validate` job started normally and passed in 8 seconds, confirming the earlier billing/spending-limit error was an external private-runner limitation rather than a code failure.
245 | - Added `docs/skill-anatomy.md` as the cross-Skill authoring contract while preserving each `SKILL.md` as the canonical per-Skill metadata/workflow source and keeping validators as machine enforcement.
246 | - Added `CONTRIBUTING.md` and `SECURITY.md`, plus README pointers and explicit public-without-license status.
247 | - Public hardening does not add a new Skill, router, service, RAG/DB/daemon, MCP, permission expansion, or LLM-in-CI dependency.
248 | - No `LICENSE` file was added. License selection is intentionally deferred because choosing one grants reuse rights and requires an explicit maintainer legal/permission decision.
249 | - Exact branch CI passed on runs `35487867705` and `35487884682`; after hardening the workflow to `actions/checkout@v6`, `contents: read`, and `persist-credentials: false`, exact-head run `35487922862` also PASSed.
250 | 
251 | ## P1 project constraints / ratchet reference
252 | 
253 | Status: **IMPLEMENTED (reference-only)** on 2026-09-20.
254 | 
255 | - Added `shared/project-constraints-ratchet-contract.md` as a plain reference; it is not a Skill, CI service, policy engine, database, daemon, MCP, permission grant, or runtime.
256 | - The contract requires baseline-first, direction-aware guardrails, separates the current guardrail from the improvement target, tightens guardrails only after verified improvement, and treats measurement changes/exceptions explicitly rather than silently weakening gates.
257 | - Constraint evidence is split into external, project, and suite classes; maturity is written → scripted → tool-backed, with most projects expected to stop at the lowest sufficient level.
258 | - Added anti-weakening review rules for threshold lowering, skipped tests/assertions, broad suppressions, denominator manipulation, missing-data relabeling, and stubs.
259 | - Added a small optional `CONSTRAINTS.md` template and a SignalForge-oriented example without inventing current production values.
260 | - Preserved the frozen five-Skill architecture and added no new runtime dependency or enforcement service.
261 | 
262 | ## P1 deterministic Skill contract evals
263 | 
264 | Status: **IMPLEMENTED** on 2026-09-20.
265 | 
266 | - Added `tests/skill-contract-cases.json` with one deterministic contract set for every active Skill.
267 | - Extended `scripts/skill_quality_gate.py` so every active Skill must have a contract fixture and every protected clause must remain present in the canonical `SKILL.md`; stale fixtures for non-active Skills also fail closed.
268 | - Contract clauses protect already-approved workflow invariants such as evidence-before-fix, falsifiable hypotheses, independent code-review axes, implementation-authorization boundaries, exact handoff requirements, and Git/CI closure semantics.
269 | - This is Tier 2 deterministic contract regression, not Tier 3 LLM behavioral eval: it detects semantic deletion/drift in Skill text but does not claim that a model will obey the Skill at runtime.
270 | - Added focused unit coverage for current contracts, missing active-Skill coverage, and clause regression detection.
271 | - No Skill body, invocation mode, Tool/MCP permission, runtime service, router, DB/RAG layer, or model-in-CI dependency was added.
272 | 
273 | ## v0.5.0 release readiness
274 | 
275 | Status: **READY EXCEPT LICENSE / NOT PUBLISHED** on 2026-09-20.
276 | 
277 | - Confirmed the public repository currently has no Git tags and no GitHub Releases.
278 | - Defined three independent version surfaces: repository release `v0.5.0`, Constitution `v1.5.2`, and per-Skill `0.1.1`; repository release numbering does not renumber the Constitution or Skills.
279 | - Added `CHANGELOG.md` with an Unreleased `v0.5.0` candidate summary.
280 | - Added `docs/release-process.md` with exact-SHA, CI, metadata, immutable-tag, and fix-forward gates.
281 | - The first release is intentionally blocked on explicit maintainer license selection; public visibility alone is not treated as permission to grant reuse rights.
282 | - No tag, GitHub Release, LICENSE, runtime behavior, Skill body, invocation mode, or Tool/MCP permission was changed.
283 | 
284 | ## v0.5.0 license and release candidate
285 | 
286 | Status: **LICENSE SELECTED / RELEASE CANDIDATE PREPARED** on 2026-09-20.
287 | 
288 | - Maintainer explicitly selected Apache-2.0 on 2026-09-20.
289 | - Added the unmodified Apache License 2.0 standard text as `LICENSE`; source: Apache Software Foundation canonical license text.
290 | - Finalized `CHANGELOG.md` for `v0.5.0 — 2026-09-20` and updated README/release-process license metadata.
291 | - No `NOTICE` file was added because this repository has no pre-existing NOTICE content that needs preservation and Apache-2.0 does not require every work to create one.
292 | - The release candidate changes no Skill body, invocation mode, Constitution behavior, Tool/MCP permission, runtime service, router, DB/RAG layer, or daemon.
293 | - Tag and GitHub Release creation occur only after this exact candidate is merged to `main` and exact-head CI passes.
294 | 
295 | ## v0.5.0 published release
296 | 
297 | Status: **PUBLISHED / VERIFIED** on 2026-09-20.
298 | 
299 | - Repository license: Apache-2.0, explicitly selected by the maintainer; GitHub license detection reports `Apache-2.0`.
300 | - Release tag: annotated `v0.5.0`; remote peeled commit is `cc3509d420aaaf3744353021f30f518cfb22c108`.
301 | - GitHub Release `v0.5.0 — Frozen v0.5 Skill Architecture` was published as a normal release (not draft, not prerelease).
302 | - Exact release commit main CI run `35500475472` PASSed before tag creation.
303 | - Post-publication verification at the tag PASSed: Registry check, Skill Quality Gate, and focused unittests 15/15.
304 | - The tag is immutable by release policy; later corrections must fix forward with a new patch release rather than retargeting `v0.5.0`.
305 | 
306 | ## Skill Architecture Promotion Gate
307 | 
308 | Status: **IMPLEMENTED AS DETERMINISTIC SENSOR** on 2026-09-20.
309 | 
310 | - Added `promotion-gate-policy.json` as the canonical machine-readable threshold policy and `scripts/evaluate-promotion-gate.py` as a stdlib-only evaluator.
311 | - Historical observations remain valid evidence but are not retroactively counted; only observation files with an explicit `promotion-gate` block enter the sensor.
312 | - Gate states are `GREEN / WATCH / CANDIDATE / PROMOTE`. All four are report states and exit successfully; malformed policy/metadata fails closed.
313 | - Qualified Tier-3 evidence requires an open `behavior` finding with both routing and canonical Skill contract marked PASS. Routing, Skill-contract, Tool/runtime, and context failures are reported back to their local layers instead of being misclassified as Tier-3 evidence.
314 | - Candidate evidence includes repeated same-invariant failure across independent tasks, aggregate qualified behavior violations across independent tasks, or a high-severity qualified behavior violation. `PROMOTE` additionally requires a repeated pattern with reproducible fixture-ready evidence.
315 | - `state: resolved` removes a verified-fixed finding from active promotion counts while preserving its Git history.
316 | - Added focused regression tests and a GitHub Actions step summary. `PROMOTE` never authorizes architecture mutation; explicit authorization remains required.
317 | - No LLM-in-CI evaluator, sixth Skill, router service, DB/RAG layer, daemon, scheduler, MCP, or permission expansion was added.
318 | 
319 | ## Promotion Gate scheduled monitoring + Telegram
320 | 
321 | Status: **CLOSED / VERIFIED END-TO-END** on 2026-09-20.
322 | 
323 | - Added `.github/workflows/monitor-promotion-gate.yml` with a six-hour schedule plus manual dispatch.
324 | - Added `scripts/promotion-gate-monitor.py` to persist only semantic Gate changes under `state/promotion-gate/latest.json` and append transition history to `history.jsonl`; unchanged scheduled runs do not create repository commits.
325 | - Added `scripts/send-promotion-alert.py` to notify only new `CANDIDATE/PROMOTE` alert fingerprints and to persist a successful `last_sent_fingerprint` receipt so duplicate alerts are suppressed.
326 | - A missing Telegram configuration does not lose Gate state: the alert remains pending and later runs retry until a send receipt is persisted.
327 | - Telegram Bot API errors are sanitized so the request URL/token is not echoed; checkout credentials are not persisted and the GitHub token is exposed only to narrow push steps through a temporary authorization header.
328 | - Repository secrets `TELEGRAM_BOT_TOKEN` (for `@github_stan_bot`) and numeric `TELEGRAM_CHAT_ID` were configured by the maintainer on 2026-09-20.
329 | - Added a manual `workflow_dispatch(test_telegram=true)` smoke-test path that sends an explicit TEST message without modifying Promotion Gate status, observations, or alert fingerprints.
330 | - Main validation run `35503983352` PASSed and the real Telegram smoke workflow run `35503992845` PASSed with log evidence `Telegram smoke test sent.`
331 | - User independently confirmed receipt of the TEST message in Telegram, closing the GitHub Actions → GitHub Secrets → Telegram Bot API → user chat delivery loop.
332 | - Current Promotion Gate remained `GREEN` during the smoke test, so no false `CANDIDATE/PROMOTE` alert or state mutation occurred.
333 | - No LLM call, sixth Skill, router service, DB/RAG layer, daemon, new MCP, or permission expansion outside the dedicated workflow's `contents: write` state-persistence need was added.
334 | 
335 | ## Phase 5 rule
336 | 
337 | Phase 5 is complete after 10 genuine tasks and the evidence review above. Do not manufacture further observation tasks. Record new observations only when a real event satisfies `OBSERVATION_TEMPLATE.md`; any architecture change still requires independent evidence and authorization.
338 | 
339 | 
340 | ## Agent Runtime Contract v1
341 | 
342 | Status: **IMPLEMENTED AS REFERENCE-ONLY CONTRACT** on 2026-09-22.
343 | 
344 | - Studied Google `google/ax` and separated transferable runtime semantics from its cluster-scale deployment architecture.
345 | - Added `shared/agent-runtime-contract.md` as the canonical cross-runtime reference for runtime identity, liveness/readiness, capability truth, caller authorization, job lifecycle, verification, evidence/artifacts, cancellation/retry semantics, optional checkpoint/resume, and permission/debug boundaries.
346 | - Kept `shared/agent-execution-integrity-contract.md` as the separate canonical owner of task identity, checkpoints, operation receipts, stale-baseline reconciliation, evidence-bound review, and duplicate-safe side-effect handling; the new runtime contract does not duplicate those responsibilities.
347 | - Verified Mac Browser Plane already satisfies most of the contract through `browser_doctor`, `capabilities.json`, `JobState`/JobStore, status/result/cancel surfaces, evidence artifacts, and the separate SignalForge Provider Invocation Contract; no Browser Plane runtime redesign is justified.
348 | - Verified AWR already exposes complementary product-specific runtime semantics through backend-owned operational health, durable Runtime/Run state, SQLite events, and Executor contracts; no refactor into Browser Plane abstractions is justified.
349 | - Checkpoint/resume remains optional rather than universal. Bounded C0-C3/OCR jobs do not gain new persistence machinery merely to mimic AX suspend/resume.
350 | - Explicitly rejected Kubernetes, Redis Streams, Agent Substrate, a new scheduler, queue, daemon, database, network listener, or second worker as YAGNI for the current Mac/VPS scale.
351 | - Default adoption rule is `map existing truth first; add runtime machinery only when a real caller ambiguity/failure demonstrates need`.
352 | - No Skill body, invocation mode, Constitution behavior, Tool/MCP permission, production runtime, deployment, or security boundary was changed.
353 | 
354 | 
355 | ## AX design absorption — Workspace + Reconciliation contracts
356 | 
357 | Status: **IMPLEMENTED AS REFERENCE-ONLY CONTRACTS** on 2026-09-22.
358 | 
359 | - Re-audited Google `google/ax` beyond its top-level primitives, including Task spec/status, Conditions, runner/workspace preparation, controller reconciliation, event worker semantics, watch streams, runtime-template fingerprinting, and two-phase deletion.
360 | - Added `shared/agent-workspace-contract.md` as canonical reference for source/tool/Skill/bootstrap/durability composition, spec-vs-realized status, prepare-once semantics, workspace fingerprints, mutable-worktree vs immutable baseline, multi-workspace composition, reuse/invalidation, and two-phase cleanup.
361 | - Added `shared/agent-reconciliation-contract.md` as canonical reference for desired-vs-observed state, conditions, drift classification, ownership, level-based ensure semantics, event/watch handling, durable ACK disposition, bounded retry/backoff, child-process truth, two-phase termination, and permission-ready fail-closed behavior.
362 | - Updated `shared/agent-runtime-contract.md` to v1.1 so runtime semantics explicitly include desired spec vs observed status, Conditions, event/watch semantics, two-phase termination, workspace binding, and child-command outcome.
363 | - Deliberately improved on several current AX behaviors rather than copying them: required policy/permission failure blocks Ready; task success cannot be inferred from runner liveness when command outcome matters; ACK requires a durable disposition; required workspace bindings must not silently disappear; deterministic bootstrap is preferred over Agent-assisted setup.
364 | - Kept `shared/agent-execution-integrity-contract.md` as canonical owner of task identity/checkpoints/operation receipts/review binding; the new contracts do not duplicate those responsibilities.
365 | - No Skill, router, scheduler, queue, daemon, DB/RAG layer, MCP, Kubernetes, Redis Streams, Agent Substrate, production runtime, deployment, or Tool permission was added.
366 | - Default rule remains: absorb the design broadly; implement runtime machinery only after a real operational failure/drift demonstrates the need.
367 | - First concrete low-risk realization completed in `stanleyrprose/codexpro`: PR #2 added read-only `resolved_revision`, `git_branch`, `dirty_state`, `workspace_fingerprint`, and fingerprint-basis fields to the existing workspace self-description. Ubuntu + Windows CI PASS; squash-merged into `fix/handoff-execution-integrity` as `750b5d6cb689d52ded9ddf8bad079b17baec0b09`. Fingerprint excludes mutable working-tree content and secrets; no local production install was performed.
368 | - Second concrete realization completed in `stanleyrprose/codexpro`: PR #3 binds generated handoffs to `plan_hash + baseline_revision + workspace_fingerprint + worktree_fingerprint` through `.ai-bridge/handoff-baseline.json`. The local executor re-observes the baseline immediately before launch and records terminal `stale_baseline` with `reconcile_required=true` instead of starting the Agent when plan/revision/environment/worktree drift is detected. Legacy plans without a receipt keep existing behavior; bounded `loop-handoff` validates the external baseline only on the first iteration. Local Mac build + generic smoke + execute/watch/loop smoke PASS; GitHub Ubuntu + Windows CI PASS; squash-merged into `fix/handoff-execution-integrity` as `bca481ddab4b2c05cf9fe9c5ab434354cf541755`.
369 | - Third concrete realization completed in `stanleyrprose/mac-browser-plane`: PR #55 adds a backward-compatible `runtime_projection` read model across existing Browser/OCR surfaces with separate `runtime_state / job_state / verification_state / artifacts`. `browser_doctor` remains the authoritative live readiness probe; ordinary jobs and immediate OCR calls do not infer READY and report runtime readiness as `unknown` unless re-observed. Successful browser/OCR execution does not imply business verification; OCR remains `SOURCE_CROSS_CHECK_REQUIRED`, while C1's non-empty-body gate is only an acquisition-quality check. Provider Result v1 manifest stays unchanged; C0 remains raw artifact; C1/C2/C3 and DOCUMENT_OCR JSON evidence can carry portable projection data with private Mac refs stripped. Provider failures are now separated into `PROVIDER_CONTRACT_MISMATCH`, `PROVIDER_NOT_READY`, `PROVIDER_EXECUTION_FAILED`, and `PROVIDER_RESULT_INVALID`. Clean detached-worktree validation PASS: focused 30/30, full pytest 109/109, compileall PASS, and GitHub PR checks PASS. Squash-merged into `feat/document-ocr-v1` as `4a9719513b7e640242ad22a96ba5bbbfcbd7ab92`. No new MCP tool, worker, daemon, DB schema, listener, Provider manifest version, or production deployment was added.
370 | - Fourth concrete realization completed in `stanleyrprose/signalforge`: PR #244 consumes optional Provider `runtime_projection` as evidence metadata without granting it business authority. Legacy JSON evidence without the projection remains compatible; a present projection is fail-closed if its contract/state is malformed, contradicts an accepted provider success, or leaks `private_ref`. DOCUMENT_OCR normalization now surfaces provider runtime/job/verification states and hard-sets `business_verification_required=true`; the External Official Review Packet displays those states while preserving `HUMAN_REVIEW_REQUIRED`, `verified_external=false`, and the existing separate promotion contract. No DB migration, Provider permission, scheduler/controller, or automatic business promotion was added. Clean Python 3.13 validation PASS: compileall, focused 19/19, full unittest 496/496, and GitHub verify PASS. Squash-merged to SignalForge `main` as `0ea9133214552f4c2dba8a009b56d299a2a9b54d`. Browser Plane production deployment remains intentionally separate.
371 | 
372 | 
373 | ## Amendment A2 — Research Triad Skill
374 | 
375 | Status: **COMPLETE / MERGED / CI PASS** on 2026-09-29.
376 | 
377 | - The maintainer explicitly authorized one post-v0.5 architecture expansion: add the sixth active Skill, user-invoked `research-triad@0.1.0`.
378 | - The Skill frames one Research Brief, then independently runs a GitHub lane, a public Web lane, and a Mac-local Antigravity/Hermes planning lane before central evidence reconciliation and synthesis.
379 | - GitHub discovery attempts at least three materially relevant repositories, but bounded insufficiency is preferred to padding weak matches.
380 | - Antigravity/Hermes first-pass inputs remain independent of GitHub/Web findings and of each other; their output is advisory analysis rather than factual evidence.
381 | - `shared/research-routing-evidence-contract.md` remains canonical for research mode, source roles, claim qualification, fallback, time semantics, authorization, and completion states.
382 | - The Skill is explicit user invocation only; ordinary research does not semantic-auto-route into the higher-cost triad workflow.
383 | - A2 does not authorize a deterministic router, RAG/DB, queue, daemon, scheduler, new MCP, Tool permission expansion, or default persistence.
384 | - Canonical amendment record: `docs/implementation-amendment-a2-2026-09-29.md`.
385 | 
386 | - A2 closure evidence: PR #30; branch head 81ae41e598cdb5dfef4d4b174bd03715a450fe00; merge 80756aedd27196f683e6562e06ebf584de38b2e3; branch CI 36529490025 PASS; post-merge main CI 36529604796 PASS.
387 | 
388 | ## Amendment A3 — Douyin to TikTok Public Publish Skill
389 | 
390 | Status: **IMPLEMENTED LOCALLY / VALIDATION PENDING** on 2026-10-04.
391 | 
392 | - The maintainer explicitly authorized the seventh active Skill, model-invoked `douyin-tiktok-publish@0.1.0`.
393 | - A supplied Douyin share URL for the established workflow becomes standing authorization for one durable job and exactly one TikTok PUBLIC COMMIT after the mandatory DRY_RUN gate.
394 | - The Skill orchestrates existing `AndroidAgent_DouyinOpAuto` capabilities instead of duplicating project commands, selectors, runtime state, or credentials.
395 | - Mac remains the content-production plane; Y700 remains the Android/TikTok runtime plane.
396 | - Duplicate-source protection, SHA-256 handoff verification, disk/thermal preflight, PUBLIC visibility verification, and ambiguous-COMMIT reconciliation remain mandatory.
397 | - Current PUBLIC post-publication evidence can be weaker than PRIVATE exact-profile verification; the Skill must disclose limited verification rather than overclaim success.
398 | - A3 adds no MCP, Tool permission, queue, database, scheduler, daemon, message broker, RAG layer, or object-storage dependency.
399 | - Canonical amendment record: `docs/implementation-amendment-a3-2026-10-04.md`.
400 | 
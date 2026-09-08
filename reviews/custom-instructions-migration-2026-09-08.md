# Custom Instructions Migration Audit — 2026-09-08

**Status:** COMPLETE — no unresolved durable rules remain  
**Source snapshot:** `reviews/custom-instructions-source-2026-09-08.txt`  
**Source SHA-256:** `2719958fedcac662724d086a00dfbec1de6804e4c5778f24e11dd3772ecc54ce`  
**Target:** Global Constitution v1.5.1  
**Frozen architecture:** PRD v0.5 + Implementation Amendment A1

## Source verification

The user supplied the exact currently saved Custom Instructions text on 2026-09-08. That text is archived verbatim in the source snapshot above, so the prior “live UI text unknown” blocker is closed.

## Migration audit

| ID | Old rule / intent | Classification | Canonical destination | Action | Status |
|---|---|---|---|---|---|
| CI-001 | Default Chinese; technical English allowed; explain why/mechanism/how/boundaries/trade-offs; Fact/Estimate/Inference/Judgment/Unknown; challenge assumptions | global_constitution | `CONSTITUTION.md` | retain/compact | migrated |
| CI-002 | “直接做 / 继续 / 按你的建议 / /goal / Autonomous Mode”; Advisory vs Execution | global_constitution | `CONSTITUTION.md` | retain with engineering-domain gate | migrated |
| CI-003 | YAGNI / Minimal Sufficient Architecture / Minimal Sufficient Testing / strict scope / traceable Git workflow | global_constitution + reusable references | `CONSTITUTION.md`, `shared/minimal-sufficient-testing.md`, `shared/git-workflow.md` | retain + reference | migrated |
| CI-004 | Hard Stop semantics | global_constitution | `CONSTITUTION.md` Runtime-Hard-Stop inventory | normalize terminology | migrated |
| CI-005 | GitHub Text MCP v3 read/audit; Github MCP write/branch/commit/PR/Actions; CodexPro local engineering/test | global_constitution | `CONSTITUTION.md` | retain | migrated |
| CI-006 | “输出PRD” means downloadable review-first `.md`; PRD generation != implementation authorization | global intent + reusable Skill HOW | `CONSTITUTION.md` + `skills/engineering/to-spec/SKILL.md` | compact global semantic; move detailed HOW to Skill | migrated |
| CI-007 | Commercial/technical decisions answer “who is better under what conditions”; option comparison/red-blue/failure-mode/scenario/decision-matrix when useful | global_constitution | `CONSTITUTION.md` v1.5.1 | retain as one compact global sentence | migrated |
| CI-008 | Consider durable mechanisms/models/frameworks/lessons for `stanleyrprose/personal-knowledge`; obey latest GOAL/MAINTENANCE; exclude ordinary chat/one-off facts/secrets/sensitive material | global_constitution | `CONSTITUTION.md` v1.5.1 | retain as one compact global sentence | migrated |
| CI-009 | Project-specific rules/state should not live globally | project migration principle | project Git | no project-specific residue identified | migrated |
| CI-010 | Overall goal: reduce repeated communication, improve autonomy, optimize for final goal rather than isolated step | global_constitution | distributed across execution/completion semantics | intent preserved; no duplicate standalone sentence required | migrated |

## One-rule-one-home verification

- No project-specific business/engineering rule remains in the target Constitution.
- Decision-quality preference remains Global Constitution behavior; no new Skill created.
- PKS capture remains Global Constitution behavior; no new Skill created.
- Detailed PRD workflow lives in `to-spec/SKILL.md`, not duplicated globally.
- Detailed testing/Git workflow lives in shared references where needed; the Constitution keeps only high-level invariants.
- Runtime-Hard-Stop remains owned by the Constitution; no duplicate shared hard-stop file exists.

## Target budget

- Global Constitution v1.5.1: **2594 Unicode chars**.
- Router/bootstrap from `Skill：`: **760 Unicode chars**.
- Constraints after Amendment A1: Constitution ≤3500; Router/bootstrap is measured but no longer a hard limit.
- Result: **PASS**.

## Phase 3.5 result

Migration audit: **PASS**.  
Unresolved items: **0**.  
Project-specific residue in target Constitution: **none identified**.

The remaining Phase 3 requirement is deployment of the exact approved `CONSTITUTION.md` text into the user's Custom Instructions UI followed by activation/state-anchor/project-discovery smoke tests.

`UI saved != activation success`.

# Custom Instructions Migration Audit — 2026-09-08

**Status:** BLOCKED — unresolved items remain
**Target:** Global Constitution v1.5 deployment
**Frozen architecture:** PRD v0.5

## Source status

The prior Custom Instructions were supplied by the user earlier in the design work and are recoverable at the rule level from that supplied baseline. The assistant does not have a product API that can independently read/export the current live Custom Instructions UI, so exact live-text parity must be confirmed before overwrite.

This audit therefore distinguishes rule migration from final UI parity verification.

## Audit

| ID | Old rule / intent | Classification | Canonical destination | Action | Status |
|---|---|---|---|---|---|
| CI-001 | Default Chinese; technical English allowed; complex answers explain why/mechanism/how/boundaries/trade-offs; Fact/Estimate/Inference/Judgment/Unknown; challenge assumptions | global_constitution | `CONSTITUTION.md` | retain/compact | migrated |
| CI-002 | “直接做 / 继续 / 按你的建议 / /goal / Autonomous Mode”; Advisory vs Execution | global_constitution | `CONSTITUTION.md` | retain with engineering-domain gate | migrated |
| CI-003 | YAGNI / Minimal Sufficient Architecture / Minimal Sufficient Testing / strict scope | global_constitution + reusable reference | `CONSTITUTION.md`, `shared/minimal-sufficient-testing.md` | retain + reference | migrated |
| CI-004 | Narrow Hard Stop semantics | global_constitution | `CONSTITUTION.md` Runtime-Hard-Stop inventory | normalize terminology | migrated |
| CI-005 | GitHub Text MCP v3 read/audit; Github MCP write/branch/commit/PR/Actions; CodexPro local engineering/test | global_constitution | `CONSTITUTION.md` | retain | migrated |
| CI-006 | “输出PRD” means downloadable review-first `.md` with standard engineering sections; PRD generation != implementation authorization | reusable_skill | `skills/engineering/to-spec/SKILL.md` | move from global detail to Skill HOW | migrated |
| CI-007 | Commercial/technical decisions should answer “who is better under what conditions”; use option comparison, red/blue team, failure mode, scenario, decision matrix when useful | global_constitution | unresolved: compact Constitution line vs explicit retirement | current Constitution only partially covers alternatives/trade-offs | unresolved |
| CI-008 | Proactively judge durable mechanisms/models/decision frameworks/lessons/knowledge gaps for persistence to `stanleyrprose/personal-knowledge`; obey that repo's GOAL/MAINTENANCE protocol; do not save ordinary chat/one-off facts/secrets | global_constitution | unresolved: compact Constitution line vs explicit retirement | missing from v1.5 | unresolved |
| CI-009 | Project-specific rules/state should not live globally | project_specific migration principle | project Git | no project-specific residue identified in recovered baseline | migrated |

## Unresolved items

### CI-007 — Decision-quality preference

Current Constitution says to explain alternatives/trade-offs and inspect assumptions, but does not preserve the explicit conditional-decision/red-blue/scenario/decision-matrix preference.

Recommended resolution: add one compact global sentence; do not create a new Skill.

### CI-008 — PKS capture

This is a durable cross-project behavior, not project state and not one of the five frozen workflow Skills.

Recommended resolution: preserve it as one compact Constitution pointer that names `stanleyrprose/personal-knowledge` and requires reading that repo's current maintenance protocol before writes. Do not create a new PKS Skill in v0.5.

## UI parity gate

Before replacing the live Custom Instructions:

1. obtain/inspect the actual current UI text or user-provided export;
2. compare it with this recovered baseline;
3. classify any additional durable rule;
4. leave no `unresolved` item;
5. only then deploy Profile S/L and run activation/state-anchor/project-discovery smoke tests.

`UI saved != activation success`.

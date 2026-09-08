# Custom Instructions Migration Audit — 2026-09-08

**Status:** COMPLETE — lossless migration verified; no unresolved durable rules remain  
**Source snapshot:** `reviews/custom-instructions-source-2026-09-08.txt`  
**Source SHA-256:** `6f8c259cd78f5e5a1540b122160e95c0b22502da97fe66aa20151e6f536823d5`  
**Target:** Global Constitution v1.5.2  
**Target SHA-256:** `b1fa9638126264abbefdc231eac8de5e1dd8f6873b3fda3a7d90a85e6eedcc24`  
**Frozen architecture:** PRD v0.5 + Implementation Amendment A1

## Migration rule

The user-supplied current Custom Instructions text is the migration source of truth. v1.5.2 preserves its behavior semantics first; deduplication/compression is allowed only when behavior is unchanged. Required Skill Architecture mechanics are appended without replacing legacy behavior.

## Audit

| ID | Durable behavior | Canonical destination | Status |
|---|---|---|---|
| CI-001 | Chinese default; technical terms allowed; first Chinese explanation when needed; structured deep answers; Fact/Estimate/Inference/Judgment/Unknown; challenge assumptions incl. incentives/boundaries | `CONSTITUTION.md` | migrated losslessly |
| CI-002 | “直接做 / 继续 / 按你的建议 / /goal / Autonomous Mode”; Advisory vs Execution; Execution must not degrade to steps-only | `CONSTITUTION.md` | migrated losslessly |
| CI-003 | YAGNI/MSA/MST; strict scope; traceable/recoverable/handoff; branch/atomic commit/checkpoint/PR/CI | `CONSTITUTION.md` + shared refs | migrated losslessly |
| CI-004 | Narrow Hard Stop; ordinary technical choices are not Hard Stop | `CONSTITUTION.md` | migrated losslessly |
| CI-005 | GitHub Text MCP v3 read; Github MCP write; Mac mini access prefers CodexPro; tools should execute rather than fall back to manual instructions | `CONSTITUTION.md` | migrated losslessly |
| CI-006 | “输出PRD” = downloadable review-first `.md`; generation != implementation authorization | `CONSTITUTION.md` + `to-spec/SKILL.md` | migrated |
| CI-007 | Conditional commercial/technical comparison; red-blue/failure-mode/scenario/decision-matrix | `CONSTITUTION.md` | migrated losslessly |
| CI-008 | PKS capture to `stanleyrprose/personal-knowledge` with GOAL/MAINTENANCE guardrails | `CONSTITUTION.md` | migrated losslessly |
| CI-009 | Project-specific rules/state stay in project Git; Memory/chat are non-authoritative aids | `CONSTITUTION.md` / project Git | migrated |
| CI-010 | Optimize for final goal; reduce repeated communication; improve autonomous execution | `CONSTITUTION.md` | migrated losslessly |
| CI-011 | “存入第二大脑/存到第二大脑/记一下” = invoke CodexPro → Mac `second-brain-write`; never treat as ChatGPT Memory | `CONSTITUTION.md` | migrated losslessly |
| CI-012 | New v0.5 Skill mechanics: user/model invocation, state anchors, Material Conflict, global Git degradation | `CONSTITUTION.md` + Skill repo | appended architecture mechanics |

## Verification

- Source baseline is archived verbatim.
- CI-007 and CI-008 remain explicit Constitution rules.
- CI-011 remains explicit Constitution execution semantics.
- No new Skill was created for CI-007/CI-008/CI-011.
- Four-layer architecture unchanged.
- Constitution length: **3326 Unicode chars** (≤3500 PASS).
- Router/bootstrap size is observable but non-blocking per Amendment A1.
- `dist/custom-instructions-v1.5.2.txt` must exactly match `CONSTITUTION.md`.

## Phase 3.5 result

Migration audit: **PASS**.  
Unresolved durable rules: **0**.

Remaining Phase 3 requirement: deploy exact v1.5.2 text into the ChatGPT Custom Instructions UI, then run activation / state-anchor / Project Discovery smoke tests.

# GOAL — Implement ChatGPT Context Constitution + Git-Backed Skills v0.5

**Status:** BLOCKED AT PHASE 3 MIGRATION GATE
**Branch:** `bootstrap/v0.5-phase1`
**Frozen PRD:** `PRD-ChatGPT-Context-Constitution-and-Git-Backed-Skill-Architecture-v0.5-frozen.md`
**Frozen PRD SHA-256:** `923ab0ab856d9cbbe81899c2bf895c4df7d12287d70254060f082f8fbdde864a`
**Authorization:** User explicitly froze v0.5 and authorized implementation on 2026-09-08.

## Goal

Implement the frozen v0.5 architecture without expanding scope.

## Current checkpoint

Phase 0: COMPLETE — frozen + implementation authorized.
Phase 1: COMPLETE — structural baseline validated.
Phase 2: COMPLETE — five initial Skills + derived Registry + regression test; CI PASS.
Phase 3: BLOCKED — Custom Instructions migration audit found unresolved long-term global rules.
Phase 4: PENDING — real engineering E2E.
Phase 5: PENDING — first-10-task observation window.

## Phase 3 Implementation-Hard-Stop

The old Custom Instructions baseline contains durable global behavior that the current v1.5 Constitution does not fully preserve:

1. PKS / long-term knowledge capture: proactively judge whether durable mechanisms/models/lessons should be persisted to `stanleyrprose/personal-knowledge`, using that repo's maintenance protocol.
2. Decision-quality preference: commercial/technical decisions should answer “who is better under what conditions”, with red/blue-team, scenario/failure-mode/decision-matrix framing when useful.
3. The assistant cannot independently read/export the live Custom Instructions UI, so exact deployed-old-text parity must be confirmed from the user's UI/export before overwrite.

Per frozen PRD §28 and Phase 3.5, deployment must not silently drop these rules or guess the live UI state.

See `reviews/custom-instructions-migration-2026-09-08.md`.

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

## Next decision required

Choose whether to preserve the two missing durable rules by a compact Constitution revision (recommended) or explicitly retire them. After that, confirm the actual old Custom Instructions text/UI before Phase 3 deployment.

# Implementation Amendment A1 — 2026-09-08

**Applies to:** frozen PRD v0.5 implementation
**Authority:** explicit user instruction during authorized `/goal` execution
**Architecture impact:** none

## Changes

1. `CI-007` decision-quality behavior **must remain in `CONSTITUTION.md`**.
2. `CI-008` PKS-capture behavior **must remain in `CONSTITUTION.md`**.
3. Router/bootstrap `≤800 Unicode chars` changes from a hard implementation/CI gate to a non-blocking observability metric.
4. The Global Constitution total target `≤3500 Unicode chars` remains in force.

## Non-changes

- No new Skill.
- No repo-local Skill layer.
- No change to the four-layer architecture.
- No change to invocation mapping.
- No DB/RAG/router service/daemon/new MCP.

## Rationale

The two retained behaviors are durable cross-project behavioral preferences and therefore belong in the Global Constitution. Preserving them is more important than the router sub-budget. The total Constitution remains compact and within its governance target.

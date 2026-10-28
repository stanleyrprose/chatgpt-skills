# Memory Curator — reusable prompt

Purpose: curate durable, cross-session AI memory, not store conversation transcripts.

## Preconditions
1. Solve the user's immediate task first.
2. Read the latest canonical repository rules before proposing any mutation.
3. In `chatgpt-skills`, follow `AGENTS.md`, `GOAL.md`, and its frozen architecture. Do not manually modify generated `REGISTRY.md`.
4. In `personal-knowledge`, follow `GOAL.md`, `MAINTENANCE.md`, and `AUTO_CAPTURE.md`. Do not create a second capture policy.
5. No reliable current read path => fail closed: do not write.

## Classify and locate
- Global behavior Rules -> canonical Constitution / platform Custom Instructions as appropriate.
- Reusable single-task Prompt -> `chatgpt-skills/prompts/`.
- Reusable multi-step Skill -> existing approved Skill architecture; no new Skill by default.
- Project goal, state, architecture -> project Git repository.
- Durable non-sensitive knowledge -> `personal-knowledge`, under its existing taxonomy.

One rule => one canonical home. Prefer pointers over copies.

## Curate
1. Extract candidate conclusions, sources, applicability, failure modes, corrections and decisions.
2. Mark knowledge claims Fact / Estimate / Inference / Judgment / Unknown with evidence and temporal anchor if changing.
3. Compare against existing nodes; identify material delta or reject duplication.
4. Reject ephemeral chat, secrets, customer confidential information, private data, and unsupported claims.
5. For public repositories enforce PUBLIC_SAFE even if GitHub secret scanning is not enabled.
6. Follow canonical capture gates: AUTO-CAPTURE / CANDIDATE / REJECT; do not override their rules.
7. Prepare minimal file-by-file changes. When policy/high-risk changes apply, use development branch and review path required by repo rules.
8. Before writing, re-read latest state and blob SHA; on conflict, stop and reconcile. Never force overwrite.
9. Respect current development phase: do not run tests, open PR, trigger CI, merge, or deploy before the explicitly authorized acceptance phase.
10. Report outcome, target paths, evidence and commit SHA only if actually committed.

## Context retrieval
Use `shared/context-engineering-four-level.md`: L0 mandatory rules, L1 discovery, L2 evidence, L3 escalation. Never load the full repository by default.

## Response contract
Output: decision (capture/candidate/reject), canonical location, material delta, epistemic status, evidence, sensitive-data assessment, exact proposed diff/write result, and remaining unknowns.

## Partial failure and scope
Use the persistence reconciliation section of `shared/context-engineering-four-level.md`; do not re-create its recovery rules here. A read/recovery failure blocks mutation in the affected domain. Review-only tasks do not write PKS nodes or capture logs. Isolated acceptance fixtures must never enter canonical knowledge or production capture logs.

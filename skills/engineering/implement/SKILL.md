---
name: implement
version: 0.1.0
status: active
invocation: user
description: "Execute an authorized software/repository engineering change through minimal validation, Git, CI, verification, and closure."
aliases:
  - "按PRD实施"
  - "按 /goal 执行到底"
  - "一次执行到底"
---

# Implement

User-invoked engineering orchestrator.

## Use when

The user explicitly authorizes a software/repository engineering implementation. Global phrases such as “直接做 / 修改 / 执行 / 按你的建议” map here only when the current domain is clearly software/repo engineering.

Do not use for ordinary writing, translation, analysis, or other non-engineering execution.

## Workflow

1. Inspect the current project state using Lazy Discovery:
   - affected files/direct rules first;
   - upgrade to AGENTS → GOAL → approved PRD/spec/issue → ADR/CONTEXT → Git/CI/runtime when scope or risk expands.
2. Confirm the task is authorized and does not hit a Runtime-Hard-Stop.
3. Choose the smallest reversible implementation that satisfies the current goal.
4. Implement only the authorized scope.
5. Load `shared/minimal-sufficient-testing.md` when test scope needs guidance.
6. If an independent root-cause branch is needed, push model-invoked `diagnose`.
7. Run the smallest relevant validation; fix failures caused by this change.
8. If an independent final review materially improves confidence, push model-invoked `code-review`.
9. Load `shared/git-workflow.md` when Git/CI execution details are needed.
10. Commit atomically, push, verify CI/runtime evidence, and close the task.

## Composition

Allowed automatic model Secondary:
- `diagnose`
- `code-review`

Do not auto-invoke:
- `to-spec`
- `handoff`

Those are user-invoked.

## Testing discipline

Use Minimal Sufficient Testing, not mandatory TDD:
- affected/core paths;
- data safety;
- migration/rollback;
- legacy/fallback;
- direct regressions.

A real bug fix should add one minimal stable regression test/reproducer when practical.

## Completion

Do not claim complete until the requested change is actually implemented and the relevant validation/Git/CI/runtime evidence is checked.

On closure, release the Skill.

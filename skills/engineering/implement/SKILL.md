---
name: implement
version: 0.1.1
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

## Rationalization Traps

- “This change is tiny, so validation can wait.” Small scope reduces validation scope; it does not remove the need for the smallest relevant proof.
- “CI is blocking me, so I can relax the check.” Fix the change or evidence an environment limitation; do not weaken tests, constraints, or acceptance criteria to get green.
- “I am already in this file, so I may as well clean it up.” Record unrelated cleanup separately; do not expand the authorized scope.
- “The code is written, so the task is done.” Completion requires the relevant Git/CI/runtime evidence, not only edited files.

## Red Flags

- Multi-file or risky edits begin before current authoritative project state is inspected.
- A large unverified diff accumulates instead of small reversible increments.
- Tests, assertions, quality gates, or constraints are weakened to make the change pass.
- A remote side effect with an ambiguous outcome is retried before reconciling actual target state.
- Completion is claimed while required CI/runtime evidence is missing or failing.

## Verification

- [ ] Requested behavior is implemented without unrelated scope expansion.
- [ ] The smallest relevant validation passes, or an environment limitation is explicitly evidenced.
- [ ] A real bug has a minimal stable regression proof when practical.
- [ ] Required Git/CI/runtime state is checked before closure.

## Completion

Do not claim complete until the requested change is actually implemented and the relevant validation/Git/CI/runtime evidence is checked.

On closure, release the Skill.

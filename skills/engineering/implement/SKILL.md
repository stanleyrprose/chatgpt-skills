---
name: implement
version: 0.1.2
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
   - upgrade to AGENTS → GOAL → approved PRD/spec/issue → ADR/CONTEXT → branch/PR/CI/deployment triggers → affected code/runtime when scope or risk expands.
2. Confirm the task is authorized and does not hit a Runtime-Hard-Stop.
3. Define observable success/acceptance evidence and non-goals before substantial edits. Distinguish facts, assumptions and unknowns; resolve ordinary reversible choices without unnecessary questions.
4. Choose the smallest reversible implementation that satisfies the current goal. Implement only the authorized scope; each diff hunk must trace to a requirement, a necessary dependency or cleanup caused by this change. Do not refactor unrelated code.
5. **Phase D:** implement the full scope with static inspection only. Do not run tests, executable validation, PR, CI, merge or deployment. Commit atomically; push the development branch as untested SOT only after verifying no GitHub CI, open-PR synchronize trigger or external auto-deploy. If push safety cannot be established, stop the push and report.
6. **Phase V:** only when implementation and required feedback are complete and verification is authorized, run the smallest relevant validation and affected-path tests; fix and revalidate. Load `shared/minimal-sufficient-testing.md` for scope details.
7. **Phase R:** only after Phase V succeeds and release closure is authorized, create PR, run/check CI, verify acceptance, then merge. Deployment remains a separate authorization.
8. If an independent root-cause branch is needed, push model-invoked `diagnose`; if final review materially improves confidence, push model-invoked `code-review`. Neither Secondary bypasses phase gates.
9. Load `shared/git-workflow.md` for the canonical phase-policy pointer and Git execution details.
10. Report phase-specific evidence and remaining gates. Do not call Phase D changes verified or released.

## Composition

Allowed automatic model Secondary:
- `diagnose`
- `code-review`

Do not auto-invoke:
- `to-spec`
- `handoff`

Those are user-invoked.

## Testing discipline

Use Minimal Sufficient Testing in **Phase V**, not mandatory TDD and never active-development testing:
- affected/core paths;
- data safety;
- migration/rollback;
- legacy/fallback;
- direct regressions.

A real bug fix should add one minimal stable regression test/reproducer when practical, executed only after the Phase V gate. Simplicity never excuses missing realistic safety, idempotency or recovery handling.

## Rationalization Traps

- “I have written the code, so I can run one quick test during development.” Phase D permits static inspection only; preserve the verification gate until Phase V.
- “This is only documentation, so I can safely push without reading CI or deployment triggers.” Check every applicable trigger and open PR before any development-branch push.
- “CI is blocking me, so I can relax the check.” Fix the change or evidence an environment limitation; do not weaken tests, constraints, or acceptance criteria to get green.
- “I am already in this file, so I may as well clean it up.” Record unrelated cleanup separately; do not expand the authorized scope.
- “The code is written, so the task is done.” Separate implemented/untested, verified and released evidence.

## Red Flags

- Multi-file or risky edits begin before current authoritative project state is inspected.
- A large unexplained diff accumulates or existing unrelated code/style is changed.
- A dev-branch push is attempted without establishing CI, PR synchronize and deployment-trigger safety.
- Phase D work runs tests, executable validators, PR, CI, merge or deployment.
- Tests, assertions, quality gates, or constraints are weakened to make the change pass.
- A remote side effect with an ambiguous outcome is retried before reconciling actual target state.
- Completion is claimed while the required phase's evidence is missing or failing.

## Verification

- [ ] Phase D: authorized outcome, non-goals and acceptance evidence were defined; changes are scoped, static diff is inspected, and any push was proven trigger-safe.
- [ ] Phase D: no tests, executable validators, PR, CI, merge or deployment occurred.
- [ ] Phase V (when authorized): smallest affected-path validation passes or its environment limitation is explicitly evidenced; practical regression proof exists for a real bug.
- [ ] Phase R (when authorized): exact PR/CI/acceptance and required Git/runtime state are checked before release closure.

## Completion

After Phase D, report `IMPLEMENTED_UNTESTED`, branch/commit and pending gates; do not claim verification or release. After authorized Phase V, report verification evidence without implying release. Only claim `RELEASED` once the required Phase R closure is evidenced, and treat deployment as a separate gated operation.

On closure of the authorized phase/task, release the Skill.

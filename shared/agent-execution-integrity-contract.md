# Agent Execution Integrity Contract v0.1

Status: **reference-only**. This is not a Skill, workflow engine, state service, queue, database, daemon, MCP, permission grant, or runtime.

## Purpose

Provide the smallest reusable contract needed to keep long-running or cross-Agent execution coherent when work may span multiple turns, tools, runtimes, commits, retries, or reviews.

The goal is not theoretical exactly-once execution. In real tool/runtime systems, a timeout or disconnect can leave the external effect ambiguous. The practical target is **duplicate-safe / effectively-once execution**:

> before repeating a side effect, reconcile the recorded task state with the actual target state and prove whether the effect already happened.

This contract targets six failure modes:

1. a resumed task restarts from chat memory instead of authoritative project/runtime state;
2. the same mutation, deployment, message, resource creation, or migration is applied twice after an ambiguous retry;
3. a plan is executed against a different baseline from the one it assumed;
4. a reviewer approves a stale or different implementation from the one actually produced;
5. an Agent repeatedly repairs the same task without a bounded checkpoint, causing scope drift;
6. task identity, execution evidence, and user/project authorization become conflated.

## Fit with this repository

```text
Skill = HOW
Tool / MCP = CAPABILITY
Runtime = EXECUTION
Task identity = which goal is being continued
Checkpoint = last reconciled authoritative state
Operation receipt = what side effect was attempted and what state resulted
Review binding = exactly which baseline/result/evidence was reviewed
Authorization = permission to perform the action
```

A Skill or Agent may apply this reference when useful. This file does not trigger a Skill, grant Tool access, authorize mutation, or override project rules. Existing authority and Hard Stop rules remain canonical in `CONSTITUTION.md` and the target project's authoritative sources.

## 1. Activation: pay protocol tax only where it buys safety

Use the lightest level that matches the task.

### `none`

Use no execution-integrity metadata for simple, local, reversible work where interruption or duplicate side effects would not materially matter.

Examples: explanation, read-only inspection, tiny isolated edit with immediate verification.

### `tracked`

Use task identity + checkpoint when work is multi-step, likely to continue across turns, or depends on a changing repository/runtime baseline.

Typical cases: feature implementation, multi-file fix, PR/CI workflow, investigation followed by implementation.

### `guarded`

Add operation receipts + evidence-bound review when duplicate or stale execution can cause meaningful harm or wasted work.

Typical cases: deployment, migration, restart with state impact, external message/send, resource creation/deletion, production configuration, cross-Agent execution, or long work crossing Cloud ChatGPT → CodexPro → Mac/runtime boundaries.

**Escalation rule:** task length alone does not require `guarded`. Escalate only when interruption, stale state, cross-Agent handoff, or duplicate side effects materially change correctness or risk.

## 2. Task identity

A `task_id` identifies one stable top-level goal under one material scope and authority boundary.

Minimum task record:

```yaml
task_id: "stable-id"
mode: "tracked|guarded"
goal: "single top-level outcome"
scope:
  included: []
  excluded: []
authority_refs: []
baseline:
  workspace: "repo/workspace identity"
  branch: null
  revision: null
  runtime_ref: null
completion:
  - "observable completion condition"
status: "active|blocked|done|aborted|superseded"
```

Rules:

- Generate/choose the `task_id` once; do not replace it merely because the conversation, Tool session, or Agent changes.
- A material change to goal, mutation authority, target workspace, or completion definition starts a new task or explicitly supersedes the old one.
- A routine plan adjustment caused by new evidence does **not** require a new task if the top-level goal/scope/authority remain unchanged.
- `task_id` is identity, not authorization.
- Chat history may help explain context but cannot outrank current Git/project/runtime evidence.

## 3. Checkpoint contract

A checkpoint records the last **reconciled** state from which continuation is safe.

```yaml
checkpoint_id: "stable-within-task"
task_id: "same-task-id"
observed_at: "ISO-8601"
project_state:
  branch: null
  revision: null
  dirty_state: "clean|dirty|unknown"
runtime_state: null
completed_operations: []
verification_refs: []
blockers: []
next_action: "one concrete next action or null"
```

A checkpoint is valid only when its important fields were checked against the current authoritative sources or runtime at the time it was written.

Continuation semantics:

```text
"继续"
  -> recover task identity when available
  -> read authoritative project checkpoint / Git / CI / runtime
  -> compare actual state with recorded checkpoint
  -> reconcile drift
  -> continue from the newest proven state
```

Do not resume merely from the last prose answer when the repository/runtime can establish a newer state.

## 4. Drift classification before continuation

On recovery, classify the relationship between checkpoint and actual state:

- `aligned`: observed state matches the checkpoint sufficiently for the next action;
- `forward`: actual state has valid newer progress; adopt it after verification instead of replaying older work;
- `conflicting`: actual state changed incompatibly with the recorded plan/checkpoint; stop automatic mutation and re-plan/reconcile;
- `ambiguous`: available evidence cannot prove whether an important side effect occurred; do not repeat it yet.

A stale checkpoint is not an instruction to roll the project backward.

## 5. Operation receipt: duplicate-safe side effects

Use an operation receipt for each material non-idempotent or externally visible side effect in `guarded` mode.

```yaml
operation_id: "stable-per-semantic-side-effect"
task_id: "same-task-id"
kind: "deploy|migration|restart|send|create|delete|config_change|other"
target: "bounded target identity"
desired_postcondition: "observable intended effect"
precondition_ref: "state expected before execution"
status: "planned|attempted|applied|verified|failed|unknown"
result_ref: null
verification_refs: []
observed_at: "ISO-8601"
```

Critical rules:

- Operation identity is bound to the semantic action **and** its target/desired postcondition. A materially different intended postcondition is a new operation, even on the same target.
- The same semantic side effect keeps the same `operation_id` across retries. Never create a fresh ID just to bypass an ambiguous previous attempt.
- Before executing, verify the precondition when practical.
- `attempted` means the command/action was issued; it does not prove the effect.
- `applied` means evidence indicates the intended effect occurred; it is not yet equivalent to healthy/successful.
- `verified` means the desired postcondition was checked.
- `failed` is appropriate only when the attempt is known to have failed **and** the resulting target state is sufficiently reconciled to rule out an ambiguous material side effect. Otherwise use `unknown`.
- A timeout/disconnect after dispatch normally becomes `unknown`, not automatically `failed`.
- For `unknown`, inspect the real target state first. Retry only when evidence shows the intended effect did not occur or the operation is safely idempotent.
- Read-only discovery may usually be repeated; side effects may not be replayed merely because a Tool response was lost.

This is why the contract uses **effectively-once** rather than claiming mathematically guaranteed exactly-once semantics.

## 6. Plan-to-baseline binding

A material execution plan should state which baseline it assumes.

Minimum binding:

```yaml
plan_ref: "plan/checkpoint identifier"
task_id: "same-task-id"
baseline_ref: "commit/checkpoint/runtime version"
intended_changes: []
verification_plan: []
```

Before mutation:

- if the baseline is still compatible, execute;
- if the workspace/runtime moved forward but the plan remains valid, record the new compatible baseline;
- if the change invalidates plan assumptions, amend/re-plan before continuing;
- never force a stale plan onto a newer incompatible state just to preserve protocol order.

The plan is guidance under existing authority. It cannot expand scope or grant permission.

## 7. Evidence-bound review

A review is valid only for a specific result state, not for a vague task narrative.

```yaml
review_ref: "review identifier"
task_id: "same-task-id"
baseline_ref: "state before implementation"
result_ref: "commit/diff/worktree/runtime state reviewed"
verification_refs: []
review_scope: []
verdict: "pass|pass_with_findings|repair_required|blocked"
findings: []
```

Rules:

- Reviewer inspects the real result/diff/files/runtime evidence available through authorized tools; executor summaries are supporting context, not proof.
- Tests/logs are attributed to the executor/runtime that actually ran them; the reviewer must not claim to have run checks it only inspected.
- `pass` requires the reviewed `result_ref` to still represent the state being accepted.
- If code/runtime materially changes after review, the old review becomes stale for those changed surfaces.
- A review of baseline `A` → result `B` cannot be reused to approve `C` without verifying the delta from the last reviewed state.
- Missing diff evidence can be handled by direct affected-file/state inspection when sufficient, but the limitation must remain explicit.

## 8. Cross-Agent handoff

Do not require a message protocol for every Tool call. Add handoff identity only when multiple Agents/surfaces can delay, duplicate, or reorder work.

Minimum handoff context:

```yaml
task_id: "same-task-id"
checkpoint_id: "latest-reconciled-checkpoint"
expected_role: "plan|execute|review|verify"
baseline_or_result_ref: "state the receiver must inspect"
```

Optional `handoff_id` is useful when the transport itself can duplicate or deliver stale responses.

A response that clearly belongs to another task, checkpoint, baseline, or result must not advance execution. When identity is uncertain, re-read authoritative state rather than guessing from conversational order.

## 9. Bounded repair without fighting Autonomous Mode

Repair loops must be bounded by **reconciliation points**, because repeated model-to-writer cycles can drift from the original scope.

- `tracked` tasks need no universal repair-count rule; use normal project workflow.
- In `guarded` cross-Agent execution, after one review-driven automatic repair cycle, require a fresh checkpoint + actual-state reconciliation + renewed review binding before another review-driven repair.
- This checkpoint is not automatically a user-confirmation gate. If the task is already in an authorized Autonomous Mode, state is aligned, and no Hard Stop/material conflict exists, execution may continue after reconciliation.
- Optional polish does not trigger a guarded repair cycle unless the user/project explicitly includes it in scope.
- If the same material defect repeats after reconciliation, operation state remains ambiguous, scope is drifting, or authority becomes unclear, return `blocked` rather than chaining repairs indefinitely.
- The user/project may resume a blocked task once the blocker is resolved. A new `task_id` is required only when the top-level goal/scope/authority materially changes.

This deliberately avoids both an unbounded repair loop and a rigid universal iteration state machine.

## 10. Recovery algorithm

When a long task resumes after interruption:

```text
1. identify target project/task
2. read project authority + latest checkpoint
3. inspect current Git/CI/runtime state
4. classify drift: aligned / forward / conflicting / ambiguous
5. reconcile material operation receipts
6. invalidate stale plan/review bindings when needed
7. choose one safe next action
8. execute only if current authority still permits it
9. write/update checkpoint after material progress
```

If no previous task metadata exists, recover from project facts first and create only the minimum metadata justified for future continuation. Do not reconstruct fictional receipts for operations whose history cannot be proven.

## 11. Completion and terminal state

- `done`: all declared completion conditions are satisfied by current evidence.
- `blocked`: progress needs missing authority, user action, unresolved ambiguity, unavailable evidence/capability, repeated repair failure, or another condition that prevents trustworthy continuation. A blocked task may resume after the blocker is resolved and state is reconciled.
- `aborted`: work intentionally stopped; no further side effects should occur unless explicitly resumed/re-authorized.
- `superseded`: a materially changed goal/scope/authority has replaced this task; create/use the newer task identity.

Do not mark `done` merely because editing finished, a command returned zero, a PR exists, or a reviewer produced prose. Completion is tied to the task's declared observable conditions.

## 12. Authorization and safety boundary

Execution-integrity metadata records what happened; it does not create permission.

Therefore:

- a prior successful deployment does not authorize another deployment;
- an operation receipt cannot override a project/user approval gate;
- a checkpoint containing a planned external message does not authorize sending it;
- a reviewer recommendation does not authorize mutation;
- cross-Agent handoff cannot expand Tool/MCP capability;
- credential, permission, payment, contract, destructive, or other Hard Stop boundaries remain unchanged.

## 13. Minimal persistence strategy

No database is required.

Prefer existing project-native truth surfaces in this order when appropriate:

```text
project GOAL/checkpoint
Git branch / commit / PR / CI
runtime-declared state
small task-local manifest only when the above cannot represent guarded execution safely
```

For short `tracked` work, `task_id` and checkpoint may exist only in the current project handoff/checkpoint. Persist operation receipts only when interruption/replay risk justifies them.

Do not create a central task service merely to implement this reference.

## 14. Failure modes this contract intentionally does not solve

- perfect distributed transactions across unrelated external systems;
- exactly-once guarantees from third-party APIs that do not expose idempotency or postcondition inspection;
- malicious or incorrect authoritative project state;
- correctness of the implementation itself without appropriate tests/review;
- authorization policy design for every external Tool;
- global scheduling, queues, leases, or distributed locks.

Those require separate evidence and should not be smuggled into P2 as assumed infrastructure.

## 15. Acceptance examples

1. **Simple edit:** one README typo → `none`; normal Git workflow is enough.
2. **Feature work:** multi-file repo change likely to continue tomorrow → `tracked`; preserve task ID + latest Git/checkpoint + next action.
3. **Deploy timeout:** deploy command loses connection after dispatch → operation becomes `unknown`; inspect production version/health before any retry.
4. **Duplicate send risk:** external message action times out → keep the same operation ID and inspect send/result state if possible; do not resend solely because the Tool response was missing.
5. **Second legitimate target change:** same service receives a different desired configuration → new operation identity because the desired postcondition changed.
6. **Stale plan:** branch advanced incompatibly after PLAN → amend/re-plan; do not force the old plan.
7. **Stale review:** REVIEW covered commit B, then commit C changes reviewed code → B's verdict cannot approve C without reviewing the relevant delta.
8. **Repair loop:** reviewer finds a defect and one automatic repair is applied → checkpoint/reconcile before another review-driven repair; repeated same defect or ambiguity becomes `blocked`.
9. **Continuation:** user says “继续” after interruption → recover Git/GOAL/runtime and operation state first; chat memory is auxiliary.

## 16. Provenance and license boundary

This contract was independently written after studying general collaboration/integrity ideas in `mcncarl/yichen-skills`, including task identity, duplicate/stale response handling, bounded repair, and evidence-aware review.

No upstream code, fixed state machine, message envelope, schema, executable workflow, or substantial text is copied here. The upstream repository currently uses a Personal Learning and Non-Commercial Use License; direct copying/redistribution or business use of its implementation requires compatible permission under that license.

The design here is intentionally different and adapted to this repository's own architecture: Git/project state as authority, flexible continuation semantics, Minimal Sufficient Architecture, no mandatory browser control channel, no required tunnel profile, no central workflow runtime, and no mathematically overstated exactly-once guarantee.

# Agent Reconciliation Contract v1

Status: **reference-only**. This is not a controller service, workflow engine, scheduler, queue, daemon, database, distributed lock manager, MCP server, permission grant, or runtime.

## Purpose

Define the smallest reusable semantics for keeping a managed Agent/runtime resource aligned with its declared desired state.

Core model:

```text
desired state
    ↓
observe actual state
    ↓
classify drift
    ↓
apply smallest safe action
    ↓
observe again
    ↓
persist status / conditions
```

This contract is about **state convergence**, not Agent reasoning or business workflow.

It complements:

- `shared/agent-runtime-contract.md` — runtime/job/readiness/evidence;
- `shared/agent-workspace-contract.md` — reproducible execution environment;
- `shared/agent-execution-integrity-contract.md` — task/checkpoint/side-effect/review integrity.

## 1. When reconciliation is justified

Use reconciliation for state that is intended to remain true over time, such as:

- one runtime worker should be running;
- a provider should be enabled and connected;
- a required policy/capability should be active;
- a managed workspace should remain prepared;
- a deployment/resource should converge to a declared version;
- cleanup should eventually finish after delete intent.

Do not wrap ordinary bounded functions or one-shot jobs in a controller loop merely because reconciliation is fashionable.

## 2. Desired spec and observed status

Managed resources SHOULD separate:

```text
spec
= declared desired state

status
= observed current state
```

Example:

```yaml
spec:
  enabled: true
  runtime_ref: "v1"
  permission_profile: "restricted"

status:
  phase: "Running"
  observed_spec_ref: "..."
  conditions: []
  observed_at: "..."
```

A configuration file proves intent, not reality.

A status record without a link to the spec/version it observed can become stale and should not be treated as proof of convergence.

## 3. Reconciliation identity

A reconcile pass needs enough identity to avoid applying stale intent.

Recommended inputs when practical:

```yaml
resource_id: "stable-id"
desired_ref: "spec revision / generation / hash"
observed_ref: "last status revision / runtime identity"
```

The exact mechanism may be:

- Git SHA;
- config hash;
- state version/CAS;
- database revision;
- monotonic generation;
- runtime version.

Do not invent a global generation service when a project-native revision already exists.

## 4. Conditions over opaque status

A reconciled resource SHOULD expose conditions for important independent prerequisites.

Condition shape:

```yaml
type: "Ready"
status: "True|False|Unknown"
reason: "stable_reason_code"
message: "bounded detail"
last_transition_time: "ISO-8601"
```

Typical examples:

```text
WorkspaceReady
PermissionReady
ProviderReady
DependenciesReady
Ready
```

Rules:

- `Ready=True` requires all prerequisites designated as mandatory for that resource.
- A required security/permission condition must fail closed; it must not be ignored merely because execution can technically continue.
- Optional component failures may produce degraded state if the advertised work remains safe and usable.
- Reason codes should be stable enough for automation; messages are explanatory.

## 5. Reconcile algorithm

A minimal pass:

```text
1. read current desired state
2. observe authoritative actual state
3. compare desired vs actual
4. classify
5. choose smallest safe action
6. verify action preconditions
7. execute
8. re-observe actual state
9. persist status/conditions/evidence
10. schedule/await next pass only if needed
```

Never mark convergence from the action request alone.

## 6. Drift classification

Use a small vocabulary:

- `aligned` — actual state satisfies desired state;
- `forward` — actual state contains valid newer progress compatible with intent;
- `repairable` — known safe action can converge state;
- `blocked` — required dependency/authorization/precondition prevents convergence;
- `conflicting` — another authority or incompatible state change requires re-plan/ownership resolution;
- `unknown` — evidence is insufficient to decide safely.

A reconciler is not authorized to overwrite every difference.

## 7. Ownership and manual/external drift

Before automatically repairing drift, define what the reconciler owns.

Example:

```yaml
ownership:
  manages:
    - worker_running
    - runtime_version
  observes_only:
    - human_review_state
    - external_account_quota
```

If a human or another controller changes a field outside this reconciler's authority, report drift rather than fighting it.

Avoid "controller wars" where two loops continuously overwrite each other.

For shared writable state, use the target project's existing single-writer, lease, CAS, state-version, or transaction mechanism. This contract does not require distributed locks.

## 8. Level-based actions over edge-trigger assumptions

Prefer actions that describe the intended level:

```text
ensure worker running
ensure provider disabled
ensure version = X
ensure policy applied
```

over fragile edge assumptions:

```text
start once
toggle
increment
run this command again
```

Level-based operations are easier to retry and reconcile.

For unavoidable non-idempotent effects, use the execution-integrity contract's operation receipt and actual-state reconciliation before retry.

## 9. Event and watch semantics

Events are hints that state may need reconciliation; they are not the authoritative state themselves.

```text
event
-> read current resource/spec
-> observe current actual state
-> reconcile latest truth
```

This naturally tolerates duplicate, delayed, or reordered events.

A watch/stream is useful for responsiveness, but polling remains valid at small scale.

Do not introduce Redis/Kafka/Streams solely to comply with this contract.

## 10. ACK semantics

If a queue or handoff transport has ACK semantics, acknowledge only when the event has reached a durable disposition.

Valid durable dispositions include:

- desired state successfully reconciled and status persisted;
- resource is already aligned and that observation is persisted/known;
- failure is durably classified as terminal/blocked with enough state that dropping the same notification will not hide the resource;
- a newer desired revision supersedes the event and current truth has been reconciled.

Do not ACK merely because handler code returned control.

Do not leave a poison event retrying forever either. Persist a visible blocked/failed condition and use bounded retry/backoff.

## 11. Retry, backoff, and budget

Reconciliation must not become an infinite cost loop.

For retryable failures:

- classify the failure;
- bound immediate retries;
- use backoff/jitter where appropriate;
- preserve last error/reason;
- stop or slow down when repeated attempts cannot change the outcome.

For Agent/model/tool calls with monetary or quota cost, retry budgets SHOULD be explicit enough to prevent runaway loops.

A permanent permission/configuration failure should become blocked, not continuously retried.

## 12. Completion and child-process truth

If resource readiness or completion depends on a child command/process, the reconciler/runtime must observe that outcome.

Do not infer success from:

- runner/container liveness;
- successful dispatch;
- HTTP 200 from an unrelated health endpoint;
- non-empty output.

If command exit/result cannot be observed, expose `unknown`/non-terminal semantics rather than `succeeded`.

This intentionally tightens a limitation visible in current AX runner/control-plane behavior.

## 13. Two-phase termination

For resources with external state, deletion SHOULD be reconciled:

```text
desired: absent
    ↓
status: Terminating
    ↓
stop new work
    ↓
cleanup owned child/external resources
    ↓
verify cleanup
    ↓
remove authoritative record
```

If cleanup fails:

- keep the resource visibly `Terminating` or blocked;
- record the failure condition;
- allow a safe retry/reconcile path.

Do not erase the record first and lose the identity needed to finish cleanup.

## 14. Suspend/resume

Suspend/resume is a desired-state transition only when the runtime truly supports it.

A reconciler should know:

- what state is persisted;
- what process state is discarded;
- whether resuming creates a new process tree;
- which readiness conditions must be re-established.

Do not market restart-from-files as restoration of hidden model context.

## 15. Security and permission convergence

A required policy boundary belongs in readiness.

Example:

```text
WorkspaceReady=True
PermissionReady=False
=> Ready=False
```

A runtime may choose degraded semantics only for policy failures that are genuinely optional and cannot widen authority.

Failing to apply an intended egress/filesystem/tool restriction must not silently produce a fully-ready production Agent.

## 16. Observability

A managed reconcile surface SHOULD answer:

- what is desired;
- what was last observed;
- whether they align;
- current phase;
- current conditions/reasons;
- last successful reconciliation;
- last failure;
- next retry or whether manual action is needed.

This may be represented in existing logs/status/API/state files; no new dashboard is required.

## 17. Mapping to current systems

### Mac Browser Plane

Browser Plane already has useful reconciliation ingredients:

- one worker/state authority;
- SQLite JobStore;
- state-version/CAS transitions;
- leases and process ownership;
- startup recovery;
- Doctor readiness.

Do not add a generic controller. Apply reconciliation only to long-lived runtime/provider state when a real need appears.

### SignalForge Provider path

A provider can model:

```text
desired:
  enabled + authorized source/capability contract

observed:
  Mac runtime reachable + provider polling healthy + capability ready
```

A missing required permission/capability should block that provider path rather than be treated as ordinary success.

### AWR

AWR already reconciles some durable Run/runtime facts through product-specific logic. Keep that ownership in AWR; use this contract as a design lens, not as a reason to add another controller layer.

## 18. Improvements adopted beyond AX

This contract deliberately does not copy several AX choices as universal defaults:

- required permission/policy readiness should fail closed rather than be ignored in overall Ready;
- child command outcome should be observable when it determines task success;
- event ACK should correspond to a durable disposition, not simply handler completion;
- missing required workspace/resource bindings should not silently become an empty substitute when correctness depends on them;
- Agent-assisted bootstrap is secondary to deterministic reproducible preparation.

These are adaptations for trustworthy small/medium Agent systems, not claims that AX is incorrect for its own current development stage.

## 19. Non-goals

This contract does not define:

- Agent planning or multi-Agent graph topology;
- a central controller implementation;
- Kubernetes operators/CRDs;
- Redis Streams;
- global scheduling;
- distributed consensus;
- a universal retry service;
- authorization policy itself;
- business-domain correctness.

## 20. Adoption gate

Implement a reconcile loop only when:

1. some state is intended to remain true over time;
2. drift is realistically possible;
3. failure to converge matters operationally;
4. actual state can be observed reliably;
5. the project has a bounded authority for automatic repair.

Otherwise use ordinary explicit commands/jobs.

## 21. Provenance

This contract was independently written after studying Google's Apache-2.0 licensed `google/ax` controller/store design, including spec/status separation, conditions, desired-state reconciliation, task watch, event workers, and two-phase deletion.

No AX source code, schema, or substantial text is copied. The design intentionally tightens several reliability/security semantics for this repository's existing execution-integrity and fail-closed principles.

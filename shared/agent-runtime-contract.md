# Agent Runtime Contract v1.1

Status: **reference-only**. This is not a Skill, workflow engine, scheduler, queue, daemon, database, sandbox, MCP server, permission grant, or deployment requirement.

## Purpose

Define the smallest reusable semantic contract for an agent-facing runtime or execution provider so callers can distinguish:

- whether the runtime itself is alive and ready;
- which capabilities are actually available and authorized;
- what happened to one submitted job;
- whether the job result was independently verified;
- what evidence/artifacts exist;
- whether retry, cancellation, checkpoint, or resume are safe and supported.

This contract complements, rather than replaces, `shared/agent-execution-integrity-contract.md`.

The execution-integrity contract owns task identity, checkpoints, operation receipts, stale-baseline reconciliation, evidence-bound review, and duplicate-safe side effects. This runtime contract owns the provider/runtime projection that those higher-level workflows may inspect.

## 1. Minimalism and adoption rule

Do not create new infrastructure merely to satisfy this document.

An existing runtime may comply through its current CLI, MCP tools, HTTP API, files, status objects, or an adapter/projection. The contract is semantic, not transport-specific.

Adopt only the fields that a real caller needs. A short-lived local function that has no meaningful runtime lifecycle does not need to pretend to be a managed provider.

## 2. Runtime identity

A managed runtime SHOULD expose a stable identity projection:

```yaml
runtime_id: "stable-provider-or-runtime-id"
runtime_type: "browser|agent|ocr|executor|other"
runtime_version: "implementation/version/ref"
contract_version: "agent-runtime-v1.1"
invocation_modes: []
```

Rules:

- `runtime_id` identifies the execution authority, not an individual job.
- Runtime identity is not authorization.
- A caller-specific provider may expose a narrower view than the local runtime.
- Version/ref SHOULD be sufficient to correlate behavior with deployed code or configuration when practical.


## 2A. Desired spec and observed status

For a managed runtime/resource, keep desired configuration separate from observed state.

```text
spec
= what should be true

status
= what is currently observed
```

A manifest/configuration proves intent, not successful execution.

When stale status would be dangerous, status SHOULD identify the spec/revision it observed using a project-native revision, hash, generation, or state version.

This contract does not require a new controller. Reconciliation semantics are defined separately in `shared/agent-reconciliation-contract.md`.

## 2B. Conditions

A runtime MAY expose a summary operational state, but important prerequisites SHOULD remain individually observable through conditions.

Recommended condition shape:

```yaml
type: "Ready"
status: "True|False|Unknown"
reason: "stable_reason_code"
message: "bounded detail"
last_transition_time: "ISO-8601"
```

Examples include `WorkspaceReady`, `PermissionReady`, `ProviderReady`, and `DependenciesReady`.

A required permission/security condition failing must prevent a fully-ready state. Optional-component failure may produce degraded state when remaining advertised work is still safe.

## 3. Liveness and readiness are different

A runtime MUST NOT equate "process exists" with "ready to execute useful work".

Normalize runtime operational state as:

```text
ready
degraded
blocked
unknown
```

Recommended projection:

```yaml
liveness: true
operational_state: ready
reason_codes: []
checks: []
observed_at: "ISO-8601"
```

Semantics:

- `liveness=true`: the runtime/status surface is responding.
- `ready`: required dependencies for currently advertised production capabilities are usable.
- `degraded`: runtime can serve at least some authorized work, but one or more non-global dependencies/capabilities are impaired.
- `blocked`: the runtime cannot safely accept the relevant production work.
- `unknown`: available evidence is insufficient to classify current state.

Existing native states may be preserved. For example, a runtime using `READY / DEGRADED / NOT_READY` can project them as `ready / degraded / blocked` without changing its internal model.

## 4. Capability manifest

A runtime SHOULD expose machine-readable capability truth rather than requiring callers to infer it from prose.

Minimum shape:

```yaml
capabilities:
  capability_name:
    supported: true
    ready: true
    authorized: true
    limits: {}
```

The three concepts are distinct:

- `supported`: implementation exists.
- `ready`: dependencies needed for the capability are currently usable.
- `authorized`: this caller/invocation surface is permitted to use it.

Therefore:

```text
supported != ready != authorized
```

A local runtime MAY expose more capability than a remote/provider contract. Remote authorization MUST NOT be inferred from local support.

## 5. Job identity and lifecycle

A bounded execution SHOULD have a stable `job_id` and a caller-readable state.

Normalized lifecycle:

```text
queued
waiting
running
succeeded
failed
cancelled
timeout
recovery_required
unknown
```

Runtimes MAY keep richer native states. The normalized projection exists only so cross-runtime callers can reason consistently.

Minimum job projection:

```yaml
job_id: "stable-id"
state: "running"
created_at: null
started_at: null
finished_at: null
failure_class: null
partial_effect_possible: false
result_ref: null
```

Rules:

- Runtime operational state and job state are separate.
- `succeeded` means the runtime completed its declared execution semantics; it does not automatically mean the business result is correct.
- A timeout/disconnect that leaves an external effect ambiguous SHOULD surface ambiguity rather than falsely reporting clean failure.
- Retry safety for material side effects follows `shared/agent-execution-integrity-contract.md`.

## 6. Verification is separate from execution success

Where correctness requires a postcondition, source cross-check, quality gate, review, or other validation, expose verification separately.

Normalized verification:

```text
not_required
pending
pass
fail
unknown
```

Example:

```yaml
job_state: succeeded
verification:
  status: pass
  method: "content-quality-gate"
  evidence_refs: []
```

Critical rule:

```text
runtime alive != job succeeded != result verified
```

A runtime MUST NOT claim verification merely because a command exited successfully, an HTTP request returned 200, or non-empty output exists.

## 7. Evidence and artifacts

When a runtime produces evidence or artifacts, references SHOULD preserve enough provenance to answer:

- which job produced it;
- which capability/step produced it;
- where it is stored or how it can be retrieved;
- integrity metadata such as SHA-256 when material;
- whether the path/reference is local/private or portable;
- retention/size constraints when relevant.

Example:

```yaml
artifacts:
  - kind: "rendered_html"
    ref: "runtime-private-reference"
    sha256: "..."
    bytes: 12345
    portable: false
```

Artifacts are evidence, not automatically canonical business facts.

## 8. Cancellation and retry

A managed runtime SHOULD declare whether a job can be cancelled and what cancellation means.

Cancellation result SHOULD distinguish at least:

```text
accepted
already_terminal
unsupported
unknown
```

Retry policy MUST NOT be inferred from failure alone.

For non-idempotent or externally visible side effects:

- preserve semantic operation identity across ambiguous retries;
- reconcile actual target state first;
- use the execution-integrity contract's operation-receipt rules.


## 8A. Event/watch semantics

A managed runtime MAY provide watch/event-driven status updates. Events are notifications, not authoritative state.

On an event, a caller/controller should re-read the current resource/runtime state instead of assuming the event still represents the latest truth.

When an event queue uses ACKs, ACK should correspond to a durable disposition: reconciled success, already-aligned state, a persisted terminal/blocked failure, or supersession by a newer desired state.

Do not introduce a queue/streaming service merely for this contract.

## 8B. Two-phase termination

For runtime resources with child/external state, prefer:

```text
termination requested
-> Terminating
-> stop new work
-> cleanup owned resources
-> verify cleanup
-> remove record
```

If cleanup fails, preserve visible identity/status so reconciliation can safely retry. Do not erase the authoritative record first.

## 9. Checkpoint and resume are optional capabilities

Checkpoint/resume MUST NOT be treated as a universal agent-runtime requirement.

If supported, the runtime MUST declare what survives suspension/restart.

Example:

```yaml
resume:
  supported: true
  persisted_surfaces:
    - workspace_files
    - durable_job_state
  not_persisted:
    - process_memory
    - hidden_model_context
```

A runtime that restores files into a new process MUST NOT imply that the original process memory or model context was resumed.

For bounded, cheap, replay-safe jobs, no checkpoint/resume capability may be the correct design.


## 9A. Workspace binding

When execution depends on repositories, tools/MCPs, Skills, bootstrap state, or durable files, the runtime SHOULD expose or reference the realized workspace identity rather than forcing callers to reconstruct it from prose.

Workspace preparation, fingerprints, prepare-once semantics, durability, and invalidation are defined in `shared/agent-workspace-contract.md`.

A runtime that reports `ready` while a required workspace is unresolved or unprepared is reporting a false-ready state.

## 10. Permission boundary

Capability discovery describes what exists. Authorization describes what the current caller may invoke. Enforcement SHOULD live in runtime/tool/harness controls when practical rather than relying on prompt text.

A runtime/provider MAY expose:

```yaml
permission_boundary:
  invocation_surface: "local-mcp|provider|cli|other"
  network_scope: "declared-policy"
  filesystem_scope: "declared-policy"
  debug_access: false
```

This section does not duplicate global Hard Stops or grant permission. User/project/platform authority remains canonical elsewhere.

## 11. Debug and operator access

Debug/operator surfaces that permit arbitrary process execution, unrestricted filesystem access, raw browser control, or equivalent authority SHOULD be:

- explicitly declared;
- off by default for production callers where feasible;
- separate from ordinary bounded capability authorization.

Debug availability MUST NOT silently widen the production provider contract.

## 12. Discovery surface

A runtime SHOULD provide one obvious way to discover:

1. runtime identity;
2. operational state/readiness;
3. capabilities and caller authorization;
4. job status/result/cancel semantics when jobs exist.

The transport is intentionally unspecified. Valid implementations include:

- CLI commands;
- MCP tools;
- local HTTP/gRPC;
- provider manifest files;
- existing project-owned API projections.

Do not add a network listener solely to satisfy this contract.


## 12A. Command/process outcome

If the runtime's notion of job success depends on a child command or Agent process, the runtime SHOULD observe and persist that outcome.

```text
runner alive
!= child command succeeded
```

If exit/outcome cannot be observed, do not synthesize `succeeded`; expose a non-terminal or `unknown` result appropriate to the implementation.

## 13. Recommended normalized read model

A cross-runtime caller MAY normalize existing provider data to:

```yaml
runtime:
  id: "..."
  type: "..."
  version: "..."
  liveness: true
  operational_state: "ready"
  reason_codes: []

capabilities: {}

job:
  id: "..."
  state: "running"
  failure_class: null
  partial_effect_possible: false

verification:
  status: "pending"
  evidence_refs: []

artifacts: []

resume:
  supported: false

observed_at: "ISO-8601"
```

This is a projection, not a required storage schema.

## 14. Mapping to current systems

### Mac Browser Plane

Current architecture already satisfies most of the contract without a redesign:

- runtime readiness -> `browser_doctor` / Doctor checks;
- machine capability truth -> `src/browser_plane/capabilities.json`;
- job lifecycle -> `JobState` + JobStore;
- status/result/cancel -> current CLI/MCP surfaces;
- evidence/artifacts -> runtime evidence tree + hashes/provenance;
- provider authorization -> separate SignalForge Provider Invocation Contract;
- checkpoint/resume -> intentionally not a required capability for bounded C0-C3/OCR jobs.

No Kubernetes, Redis, new daemon, or second worker is justified by this contract.

### Agent War Room

AWR already exposes complementary runtime semantics:

- runtime operational projection -> backend-owned `ready | degraded | blocked` health model;
- durable execution truth -> SQLite/runtime state and durable events;
- provider invocation -> Executor contract;
- run/job semantics -> existing Runtime/Run state;
- verification/release evidence -> project-specific gates and release evidence.

AWR SHOULD retain its product-specific runtime model rather than being refactored into Browser Plane abstractions.

## 15. Relationship to Google AX

The transferable ideas are the separation of runtime lifecycle, readiness, workspace/state, capability/permission boundaries, and explicit suspend/resume semantics.

This contract intentionally does **not** adopt AX's cluster architecture.

Out of scope here:

- Kubernetes;
- Redis Streams;
- Agent Substrate;
- billion-task scheduling;
- cluster-wide reconciliation controllers;
- mandatory sandboxing technology;
- a universal network gateway implementation.

Those are deployment/scale choices, not prerequisites for a correct small runtime.

## 16. Non-goals

This contract does not define:

- agent reasoning or multi-agent workflow logic;
- task planning;
- Skill routing;
- global scheduling;
- a central queue;
- leases or distributed locks;
- exactly-once distributed transactions;
- a universal storage layer;
- model/provider selection policy;
- business-domain success criteria;
- global authorization/Hard-Stop policy.

Use existing project/runtime mechanisms for those concerns.

## 17. Related contracts

```text
Agent Workspace Contract
  -> what execution environment is realized

Agent Reconciliation Contract
  -> how desired and observed managed state converge

Agent Runtime Contract
  -> how runtime/job/readiness/evidence are exposed

Agent Execution Integrity Contract
  -> how long/cross-Agent work stays duplicate-safe and reviewable
```

These are plain references, not four mandatory services.

## 18. Adoption gate

Before changing an existing runtime for this contract, ask:

1. Is a current caller unable to determine health/readiness, capability, job state, verification, evidence, or authorization?
2. Is the missing semantic causing a real failure, ambiguity, unsafe retry, or operational burden?
3. Can an adapter/read-model/documented mapping solve it without adding infrastructure?

If the answers do not justify code, keep the contract reference-only.

The default is **map existing truth first; implement new runtime machinery only when evidence demands it**.


## 19. Provenance

This contract was independently written and refined after studying general Agent runtime patterns and Google's Apache-2.0 licensed `google/ax` project, especially runner/readiness, workspace binding, status/conditions, lifecycle, event/watch, and termination semantics.

No AX source code, schema, or substantial text is copied. The design is adapted to this repository's Minimal Sufficient Architecture, fail-closed permission boundaries, and existing execution-integrity contract.

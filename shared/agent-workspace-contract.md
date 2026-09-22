# Agent Workspace Contract v1

Status: **reference-only**. This is not a Skill, package manager, environment manager, container platform, daemon, database, MCP server, permission grant, or runtime.

## Purpose

Define the smallest reusable contract for an Agent execution workspace: the reproducible environment in which an Agent receives source state, tools, Skills, bootstrap state, and durable files before useful execution begins.

The contract separates:

```text
task goal
!= workspace definition
!= realized workspace state
!= runtime process state
!= authorization
```

It complements:

- `shared/agent-runtime-contract.md` — runtime/job/readiness/evidence semantics;
- `shared/agent-reconciliation-contract.md` — desired-vs-observed convergence;
- `shared/agent-execution-integrity-contract.md` — task/checkpoint/side-effect/review integrity.

## 1. Adoption rule

Do not create a workspace abstraction for every script or one-shot Tool call.

Use this contract when at least one of these matters:

- work may continue across turns, Agents, retries, or restarts;
- the source revision must be reproducible;
- multiple tools/MCPs/Skills must be prepared consistently;
- environment preparation is expensive or stateful;
- re-running setup could overwrite or corrupt useful work;
- review/handoff needs to identify exactly which execution environment produced a result.

Prefer mapping existing project/runtime truth before adding a new manifest, service, or database.

## 2. Workspace as execution environment

A workspace may describe six independent surfaces:

```yaml
workspace:
  identity: {}
  sources: []
  capabilities: []
  skills: []
  bootstrap: {}
  durability: {}
```

These are semantic surfaces, not a mandatory storage schema.

### Sources

Source inputs such as:

- Git repositories;
- files/directories;
- generated artifacts;
- mounted datasets;
- project authority documents.

For mutable references such as a Git branch, record the resolved immutable revision when practical.

Bad provenance:

```text
repo = main
```

Better:

```text
requested_ref = main
resolved_revision = abc123...
```

The mutable label explains intent; the resolved revision explains what actually executed.

### Capabilities

Declared execution capabilities such as:

- MCP servers;
- CLI tools;
- Browser/OCR providers;
- external APIs;
- local executors.

Capability binding SHOULD name the capability and contract/version when that information affects behavior.

Credentials are not workspace content. The workspace may reference an authorized credential identity or provider binding, but SHOULD NOT copy secrets into durable workspace metadata.

### Skills

Record the Skills or instruction packages that materially shape execution when reproducibility or review depends on them.

Prefer stable identity such as:

```text
skill-name@version
canonical repository/ref
```

Do not duplicate Skill bodies into workspace state when a canonical source already exists.

### Bootstrap

Bootstrap describes what must become true before the workspace is ready.

Prefer deterministic preparation first:

```text
lockfile
script
package manifest
container/image
pinned toolchain
```

Agent-driven natural-language bootstrap MAY be used when deterministic preparation is impractical, but it must be treated as an execution step with observable outcome rather than as invisible setup magic.

### Durability

Declare which state survives restart/resume and which does not.

Example:

```yaml
durability:
  persisted:
    - workspace_files
    - git_worktree
    - task_artifacts
  not_persisted:
    - process_memory
    - shell_processes
    - hidden_model_context
```

Never imply that restoring files restores process memory or model context.

## 3. Workspace spec and realized status

Separate desired workspace definition from observed materialization state.

```yaml
spec:
  sources: []
  capabilities: []
  skills: []
  bootstrap: {}

status:
  fingerprint: null
  resolved_sources: []
  conditions: []
  prepared_at: null
```

The spec says what the workspace should contain.

The status says what was actually resolved and prepared.

This distinction prevents a manifest or configuration file from being mistaken for proof that setup succeeded.

## 4. Workspace conditions

A managed workspace SHOULD expose small, composable conditions rather than one opaque `READY` bit.

Recommended condition vocabulary when relevant:

```text
SourcesReady
CapabilitiesReady
SkillsReady
BootstrapReady
WorkspaceReady
```

Condition shape:

```yaml
type: SourcesReady
status: "True|False|Unknown"
reason: "stable_reason_code"
message: "bounded operator-readable detail"
last_transition_time: "ISO-8601"
```

Rules:

- `WorkspaceReady=True` means every condition required by the current workspace contract is satisfied.
- Optional capability failure may leave the workspace usable but degraded.
- A required capability/permission/setup failure must not be hidden behind `WorkspaceReady=True`.
- Conditions describe observed state; they do not grant authorization.

## 5. Prepare-once semantics

Environment setup must not be blindly replayed after every restart.

Preparation SHOULD be keyed to the realized workspace identity/fingerprint.

```text
same fingerprint + valid prepared receipt
    -> reuse

different fingerprint
    -> reconcile / migrate / rebuild deliberately
```

A prepare receipt may contain:

```yaml
workspace_fingerprint: "..."
prepared_at: "..."
resolved_sources: []
bootstrap_ref: "..."
verification_refs: []
```

Do not use a marker that says only `prepared=true` without proving what was prepared.

Re-running clone/install/bootstrap over a changed or stateful workspace can destroy Agent work and is not a safe default.

## 6. Workspace fingerprint

A workspace fingerprint is a reproducibility aid, not a security signature.

It SHOULD be derived only from stable inputs that materially affect execution, for example:

- resolved source revisions;
- dependency lock/manifests;
- runtime image or implementation ref;
- relevant MCP/capability contract versions;
- Skill versions;
- bootstrap contract/script revision;
- non-secret configuration that affects behavior.

It SHOULD exclude:

- credentials and secret values;
- timestamps;
- random IDs;
- ephemeral ports;
- incidental environment values that do not affect behavior.

Example conceptual identity:

```text
hash(
  repo revisions
  + dependency locks
  + runtime ref
  + capability contract refs
  + skill versions
  + bootstrap ref
)
```

A fingerprint change means the environment identity changed. It does not automatically mean the old workspace must be destroyed.

## 7. Mutable state and immutable baseline

A useful Agent workspace often contains both:

```text
immutable baseline
+
mutable working state
```

Examples:

```text
resolved Git commit
+
uncommitted edits

base dependency lock
+
generated build artifacts
```

Do not recompute the baseline from mutable current state after work has begun.

For review/handoff, preserve both:

- the baseline that execution started from;
- the current/result state being reviewed.

This aligns with plan/review binding in the execution-integrity contract.

## 8. Multi-workspace composition

A task may need several workspace surfaces, for example:

```text
application repo
+
shared tools
+
evidence corpus
```

When multiple workspaces are composed:

- each binding needs stable identity;
- mount/path ownership must not collide;
- working-directory selection must be explicit;
- one workspace must not silently mutate another unless authorized;
- readiness should identify which binding failed.

Do not merge unrelated repositories into one opaque working directory merely for convenience.

## 9. Capability discovery and authorization

A workspace may declare or materialize capabilities, but:

```text
present
!= ready
!= authorized
```

The runtime/provider remains responsible for current readiness and authorization.

For example, a workspace may contain MCP configuration while a remote provider intentionally exposes only a subset of those MCP operations.

Prompt text such as "do not call X" is not equivalent to an enforced capability boundary.

## 10. Bootstrap hierarchy

Use the shallowest reproducible method:

```text
1. already-prepared compatible workspace
2. deterministic script/lockfile/package manager
3. declarative image/toolchain
4. bounded Agent-assisted bootstrap
5. human/manual setup
```

Agent-assisted bootstrap SHOULD produce evidence of what changed and a postcondition check.

It SHOULD NOT silently rewrite project code merely because environment setup failed.

Bootstrap failure leaves the workspace not ready or degraded according to whether the missing dependency is required.

## 11. Workspace self-description

An Agent SHOULD be able to discover its relevant execution context without relying entirely on injected prose.

A workspace/runtime may expose a read model such as:

```yaml
workspace:
  id: "..."
  fingerprint: "..."
  baseline_refs: []
  resolved_sources: []
  capabilities: []
  skills: []
  durability: {}
```

The transport may be a file, CLI, MCP response, local metadata endpoint, or existing runtime API.

Do not add a network listener solely for self-description.

## 12. Invalidation and reuse

Reuse is safe only when the workspace remains compatible with the new task.

Reasons to invalidate or deliberately reconcile a workspace include:

- source revision changed;
- lock/dependency contract changed;
- required Skill/capability version changed;
- runtime image/toolchain changed;
- authorization boundary changed materially;
- previous bootstrap is known incomplete/corrupt.

Do not invalidate merely because a new chat turn or Agent session started.

A new task may reuse a compatible workspace while retaining a distinct task identity.

## 13. Cleanup

Workspace cleanup SHOULD be two-phase when external/durable state is involved:

```text
cleanup requested
-> stop new work
-> remove/release owned external state
-> verify cleanup
-> remove workspace record/reference
```

Do not delete the authoritative record first and leave unknown external state behind.

Cleanup must respect evidence/retention/rollback requirements owned by the target project.

## 14. Mapping to current systems

### Mac Browser Plane

Browser Plane already owns runtime evidence paths, profiles, browser processes, leases, and bounded artifact state. It does not need a new generic workspace service.

Relevant workspace ideas are:

- resolved runtime/version identity;
- evidence ownership;
- prepare-once semantics for persistent profiles/state;
- capability/authorization projection;
- explicit durability boundaries.

### CodexPro / repository engineering

A practical execution workspace can be described from existing truth:

```text
repo/workspace root
+ resolved branch/commit
+ dirty state
+ AGENTS/GOAL authority
+ Skill versions
+ connected MCP/tool contracts
+ dependency/lock state
```

A lightweight fingerprint/read model may improve handoff/reproducibility without creating a workspace daemon.

### AWR

AWR should keep its own Run/Agent/Provider models. Only use this contract where an execution environment needs reproducible source/tool/Skill preparation; do not refactor AWR product entities into generic Workspace objects.

## 15. Non-goals

This contract does not define:

- Agent reasoning or workflow topology;
- global task scheduling;
- package management;
- credential storage;
- a universal container format;
- a central workspace database;
- distributed filesystem design;
- backup policy for every project;
- global authorization;
- deployment topology.

## 16. Adoption gate

Before implementing workspace machinery, ask:

1. Is environment identity or preparation currently ambiguous?
2. Has repeated setup caused wasted work, drift, corruption, or non-reproducible results?
3. Does review/handoff need stronger execution-environment provenance?
4. Can existing Git/lockfiles/runtime metadata represent the truth without a new service?

If existing truth is sufficient, add only a documented/read-model mapping.

## 17. Provenance

This contract was independently written after studying the workspace/runner concepts in Google's Apache-2.0 licensed `google/ax` project, especially declarative Git/MCP/Skill bindings, prepare-once setup, durable workspace semantics, and runtime metadata.

No AX source code, schema, or substantial text is copied. The design is adapted to this repository's Git-backed authority, Minimal Sufficient Architecture, and existing Skill/runtime separation.

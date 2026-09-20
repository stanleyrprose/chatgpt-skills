# Skill Anatomy — Authoring Contract

This document defines the cross-Skill authoring contract for `chatgpt-skills`.

It does **not** replace each Skill's canonical `SKILL.md`. Per-Skill metadata and workflow remain owned by that file. The repository validators enforce the machine-checkable subset of this contract.

## 1. Design goal

A Skill should be a reusable engineering capability, not a large prompt collection.

A good Skill must be:

- discoverable;
- correctly invocable;
- scoped to one reusable workflow;
- explicit about failure modes;
- verifiable;
- safe under the existing Tool/MCP permission boundary;
- small enough to load only when relevant.

The target is **workflow as contract**, not workflow as motivational prose.

## 2. Canonical structure

Each Skill lives at:

```text
skills/<bucket>/<skill-name>/SKILL.md
```

The directory name must match the frontmatter `name`.

Current frontmatter shape:

```yaml
---
name: example-skill
version: 0.1.0
status: active
invocation: model
description: "Short description of what the Skill does and when it applies."
aliases: []
---
```

### Required metadata

#### `name`

- stable Skill identifier;
- unique across the repository;
- must match the containing directory.

#### `version`

Version of the canonical Skill contract.

Guidance:

- **PATCH** — wording, guardrails, verification, or workflow refinement without changing the Skill's externally expected role;
- **MINOR** — backward-compatible workflow capability expansion;
- **MAJOR** — incompatible invocation/contract semantics.

Version changes do not authorize architecture changes by themselves.

#### `status`

Current lifecycle state. Active Skills participate in runtime discovery and quality gates.

#### `invocation`

Exactly one of:

- `user`
- `model`

Invocation semantics are defined in `.agents/invocation.md`.

Do not use semantic similarity to auto-route a user-invoked Skill.

#### `description`

The description is discovery/routing metadata, not a compressed workflow body.

It should answer:

- what problem this Skill handles;
- when it is relevant.

Avoid:

- long implementation instructions;
- keyword stuffing;
- duplicated aliases;
- claims broader than the actual Skill scope.

#### `aliases`

Aliases are optional and should be low-ambiguity.

For user-invoked Skills, aliases are explicit invocation surfaces and therefore require extra care.

## 3. Body contract

The body should contain only what is needed to execute the reusable workflow reliably.

Section names may vary when the Skill's domain requires it, but every active Skill must include these discipline sections exactly:

### `## Rationalization Traps`

Capture plausible-sounding shortcuts that commonly degrade the workflow.

Good traps look like:

```text
"The change is small, so validation can wait."
```

They should identify a real failure pattern and state the correct discipline.

Avoid generic advice such as "be careful" or "think step by step".

### `## Red Flags`

List observable conditions that indicate the workflow is drifting or evidence is insufficient.

Good Red Flags are externally inspectable, for example:

- code changes begin before the failing layer is narrowed;
- required CI/runtime evidence is missing;
- unrelated refactors enter the authorized scope.

### `## Verification`

Define the evidence required before the Skill may claim successful completion of its responsibility.

Verification should prefer:

- tests;
- current Git/CI state;
- runtime evidence;
- explicit source references;
- reconciliation against actual target state.

Avoid verification that merely restates the intended action.

The quality gate currently requires at least two actionable list items in each of these three sections.

## 4. Recommended sections

Use only when they improve the workflow.

Common sections include:

- `Use when`
- `Workflow`
- `Composition`
- `Guardrails`
- `Testing discipline`
- `Output`
- `Completion`
- `Authorization boundary`

Do not add empty boilerplate sections merely for symmetry.

## 5. Invocation metadata authoring

Cross-Skill invocation mechanics are canonical in `.agents/invocation.md`. Do not restate or redefine those runtime rules in a Skill or in this document.

When authoring metadata:

- choose `invocation: user` when explicit user intent is part of the workflow's activation boundary;
- choose `invocation: model` only when automatic selection from task intent is appropriate within the existing permission boundary;
- keep the `description` aligned with the chosen mode and actual Skill scope;
- treat changes to invocation mode or cross-Skill composition semantics as architecture changes, not ordinary copy edits.

For Primary/Secondary rules, state anchors, engineering-domain gating, and release/reroute behavior, follow `.agents/invocation.md`.

## 6. Composition authoring

A Skill body may document which existing model-invoked specialist workflows are useful to it, but the cross-Skill composition mechanics remain canonical in `.agents/invocation.md`.

Do not copy the global composition state machine into individual Skills. Record only Skill-specific composition choices that cannot be derived from the canonical mechanics.

## 7. Verification hierarchy

Prefer the strongest available evidence:

```text
actual target/runtime state
    >
current Git/CI evidence
    >
deterministic local validation
    >
documented project state
    >
conversation context
    >
memory/history
```

Memory may help recover intent, but it does not replace authoritative project evidence.

## 8. Anti-patterns

Do not create a Skill merely because a workflow can be written down.

Avoid:

- one-off task Skills;
- project-specific Skills;
- Skills that only rename generic prompting advice;
- Skills that duplicate Constitution rules;
- Skills that duplicate shared references;
- Skills whose only purpose is to call a Tool/MCP;
- automatic chains of multiple user-invoked Skills;
- descriptions engineered only to win lexical routing tests;
- large bodies that preload unrelated domain knowledge.

A new Skill should require repeated, cross-project workflow evidence.

## 9. Testing model

The repository uses three conceptual validation layers.

### Tier 1 — Structural

Deterministic and CI-safe:

- frontmatter/schema checks;
- directory/name consistency;
- generated Registry drift;
- required discipline sections;
- static security checks.

### Tier 2 — Routing

Deterministic sanity checks:

- exact user-invoked trigger ownership;
- model-description positive cases;
- negative and low-information cases.

These tests validate metadata quality. They do **not** turn runtime routing into a deterministic router.

### Tier 3 — Behavioral

Actual agent/LLM execution against fixtures.

Tier 3 is intentionally deferred until real evidence shows that routing succeeds but agents still violate the Skill contract often enough to justify token cost, nondeterminism, and maintenance overhead.

Do not add LLM-in-CI merely because it is technically possible.

## 10. Change checklist

Before merging a Skill change:

- [ ] Canonical source identified.
- [ ] Invocation semantics unchanged unless explicitly authorized.
- [ ] Scope remains reusable and cross-project.
- [ ] Version updated when the workflow contract changed.
- [ ] Rationalization Traps are concrete.
- [ ] Red Flags are observable.
- [ ] Verification requires evidence rather than assertion.
- [ ] Relevant routing/validator tests updated.
- [ ] `REGISTRY.md` regenerated rather than hand-edited.
- [ ] Local validators pass.
- [ ] Exact PR head CI is checked, or an external CI limitation is explicitly recorded.

## 11. Architecture boundary

This authoring contract does not authorize:

- a sixth Skill;
- repo-local Skill layers;
- a deterministic router service;
- semantic retrieval infrastructure;
- RAG;
- a daemon;
- a database;
- a new MCP;
- permission expansion.

Those remain separate architecture decisions requiring independent evidence and explicit authorization.

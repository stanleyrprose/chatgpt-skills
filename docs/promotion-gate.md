# Skill Architecture Promotion Gate

Status: **deterministic sensor**. This gate reports whether real observations justify considering a larger Skill-architecture change. It does not authorize that change.

## Purpose

The gate answers one question:

> Has real usage produced enough evidence to justify moving beyond the current deterministic Skill stack, especially toward Tier-3 LLM behavioral evaluation?

It prevents both premature architecture expansion and indefinite reliance on memory.

## Canonical machine policy

Thresholds are owned by `promotion-gate-policy.json`.

The evaluator is `scripts/evaluate-promotion-gate.py`.

Do not duplicate threshold numbers into Skill bodies. Changing the policy is an architecture-quality decision and should be reviewed as such.

## Observation eligibility

Historical observations without a fenced `promotion-gate` block are ignored by this sensor.

New event-triggered observations should add the block only when the event is relevant to Skill-architecture promotion:

```promotion-gate
eligible: true
state: open
failure_layer: behavior
skill: diagnose
invariant_id: evidence-before-change
task_id: signalforge-example-20260920
routing_status: pass
contract_status: pass
severity: normal
reproducible: yes
fixture_ready: no
```

When the demonstrated issue is fixed and verified, change `state` to `resolved`. Git history preserves the prior evidence.

## Failure layers

- `routing` — wrong/missing Skill selection; repair Tier 2A first.
- `skill_contract` — canonical Skill text is missing/incorrect; repair Tier 2B first.
- `behavior` — routing and canonical contract are correct, but the Agent violates the workflow.
- `tool_runtime` — capability/runtime/tool failure; repair that boundary.
- `context` — state/context recovery failure.
- `other` — relevant evidence not represented above.

Only an open `behavior` finding with both `routing_status: pass` and `contract_status: pass` can count as qualified Tier-3 evidence.

## Gate states

### GREEN

No active promotion-marked findings.

Action: keep the current architecture frozen.

### WATCH

Active findings exist, but evidence is insufficient for Tier-3 consideration.

Action: repair the correct local layer when known and continue event-triggered observation.

### CANDIDATE

Evidence satisfies at least one candidate threshold from `promotion-gate-policy.json`, such as repeated behavior failure across independent tasks or a high-severity qualified behavior violation.

Action: review the evidence. Do not build Tier-3 merely because this status appears.

### PROMOTE

A repeated qualified behavior pattern meets the promotion threshold and has reproducible, fixture-ready evidence.

Action: Tier-3 implementation is now technically justified for review, but still requires explicit authorization. The gate cannot change the architecture by itself.

## Running locally

```bash
python3 scripts/evaluate-promotion-gate.py
```

Machine-readable output:

```bash
python3 scripts/evaluate-promotion-gate.py --json
```

The normal GitHub validation workflow also runs the evaluator and writes its status into the GitHub Actions step summary.

## Why this is non-blocking

`GREEN`, `WATCH`, `CANDIDATE`, and `PROMOTE` all exit successfully.

CI fails only when promotion metadata or policy is malformed, because a broken sensor should not silently report a trustworthy state.

This separation is intentional:

```text
sensor status != implementation authorization
```

## Boundary

The Promotion Gate does not add:

- an LLM-in-CI evaluator;
- a router service;
- a database;
- RAG;
- a daemon;
- a scheduler;
- a sixth Skill;
- a permission grant.

It is a small deterministic sensor over Git-backed evidence.

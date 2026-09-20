# Project Constraints + Ratchet Contract v0.1

Status: **reference-only**. This is not a Skill, router, CI service, policy engine, database, daemon, MCP, permission grant, or runtime.

## Purpose

Provide a minimal reusable way to turn important project quality expectations into measurable constraints without inventing arbitrary targets or creating permanent red CI.

The core pattern is:

```text
measure current reality
    ↓
record baseline
    ↓
prevent regression
    ↓
improve deliberately
    ↓
ratchet the baseline upward
```

The goal is not maximal strictness. The goal is to preserve proven quality while allowing the project to improve monotonically where measurement is meaningful.

## 1. When to use this reference

Use it when a project has a recurring quality property that:

- materially affects correctness, safety, reliability, business value, or operational cost;
- can be measured or checked with reasonable stability;
- has already caused regressions, ambiguity, or repeated review friction; or
- needs an explicit floor so future Agent work cannot silently weaken it.

Do **not** create a constraint merely because a metric exists.

Examples of useful constraint domains:

- test pass/failure invariants;
- source coverage for known high-value inputs;
- duplicate delivery rate;
- deadline accuracy;
- latency or resource ceilings;
- schema compatibility;
- rollback availability;
- security policy violations;
- data completeness within a clearly bounded scope.

Examples of weak candidates:

- vanity coverage percentages with no relationship to risk;
- unstable metrics that fluctuate for external reasons;
- broad "quality scores" whose meaning is unclear;
- metrics that can be gamed without improving the real outcome.

## 2. Baseline first

Never invent a stronger threshold simply because it sounds desirable.

A constraint starts from an observed baseline:

```yaml
constraint_id: "stable-id"
property: "what is being protected"
measurement: "how it is measured"
scope: "bounded population / path / environment"
direction: "higher_is_better|lower_is_better|exact|set_inclusion|custom"
baseline:
  value: null
  observed_at: "ISO-8601"
  evidence_ref: "test/run/report/commit/runtime evidence"
guardrail: "must-not-regress boundary derived from proven baseline"
target: null
```

Examples:

Bad:

```text
coverage >= 90%
```

when the current project has 62% and no evidence that 90% is immediately achievable or decision-relevant.

Better:

```text
current measured coverage = 62%
guardrail = must not fall below 62%
next deliberate target = 65%
```

The guardrail protects current proven quality. The target guides improvement. They are not the same thing.

"Must not regress" depends on metric direction:

- `higher_is_better`: guardrail is normally a minimum;
- `lower_is_better`: guardrail is normally a maximum;
- `exact`: guardrail is equality or an allowed discrete state;
- `set_inclusion`: guardrail protects required members/capabilities rather than a scalar;
- `custom`: define the comparison explicitly.

Do not force a scalar percentage onto a property that is naturally boolean, categorical, set-based, or distributional.

## 3. Ratchet semantics

A ratchet moves only after a new level has been achieved and verified.

```text
proven baseline
   ↓
change
   ↓
verified improvement
   ↓
new guardrail = improved proven boundary
```

Rules:

- do not tighten the guardrail based on a plan, aspiration, or one-off flaky result;
- tighten it only from reproducible or otherwise trustworthy evidence;
- do not weaken the guardrail merely to make CI green;
- if the measurement itself changes materially, establish a new comparable baseline instead of pretending the old and new values are equivalent;
- if external conditions make a previous guardrail temporarily invalid, record an explicit bounded exception rather than silently weakening the constraint.

## 4. Constraint classes

Prefer a small portfolio of constraints with different evidence sources.

### A. External constraints

Checked by an independent tool or external standard.

Examples:

- vulnerability scanner;
- accessibility checker;
- protocol/schema validator;
- Lighthouse/Web Vitals;
- dependency audit;
- production health signal.

These are useful because the implementation cannot redefine the test as easily as it can redefine its own internal success condition.

### B. Project constraints

Explicit invariants owned by the project.

Examples:

- no duplicate Telegram delivery for the same semantic signal;
- known high-value procurement source coverage must not regress;
- a fallback path must remain available;
- a migration must preserve rollback.

### C. Suite constraints

Behavior protected by tests, fixtures, or deterministic validators.

Examples:

- regression tests;
- parser fixtures;
- routing cases;
- schema compatibility tests.

For important quality properties, prefer at least one constraint whose evidence is not circularly defined by the code under test.

## 5. Maturity levels

Use the lowest level that is sufficient.

### Level 1 — Written

The constraint is documented with baseline, scope, and evidence method.

Use when:

- the check is rare;
- automation cost is higher than the risk;
- the measurement is still being stabilized.

### Level 2 — Scripted

A deterministic local script/test checks the constraint.

This is the default endpoint for many projects.

Use when:

- the check recurs;
- the measurement is stable;
- regressions should be caught before review.

### Level 3 — Tool-backed

An independent external system or production signal enforces or verifies the constraint.

Use only when the risk justifies additional operational complexity.

Do not build a quality platform merely to reach Level 3.

## 6. Anti-weakening rules

A constraint system fails if an Agent can "solve" a red result by weakening the bar.

Treat these as review signals:

- lowering a threshold without new evidence;
- deleting or skipping a failing test;
- removing assertions;
- broadening an exception until it swallows the rule;
- replacing a real check with a stub;
- suppressing warnings without explaining the underlying issue;
- changing the denominator/population to improve the metric;
- relabeling missing data as passing data;
- making a failure non-blocking solely because it blocks the current change.

Common suppression patterns deserve scrutiny when they appear in affected code, for example:

```text
@ts-ignore
eslint-disable
nosemgrep
istanbul ignore
pragma: no cover
empty catch / pass-only handlers
```

These are not automatically forbidden. They require evidence that the exception is intentional, bounded, and does not weaken the protected property.

## 7. Exception contract

Some regressions are legitimate.

An exception should be explicit:

```yaml
constraint_id: "same-constraint"
exception:
  reason: "why the floor cannot currently hold"
  scope: "smallest affected surface"
  owner: "person/team/project role"
  evidence_ref: "why this is necessary"
  expires_or_review_at: "date, release, or concrete condition"
  recovery_plan: "how the normal guardrail is restored"
```

Rules:

- an exception is not a new baseline by default;
- exceptions should be narrow and time/condition bounded;
- permanent changes to the property or measurement require a deliberate re-baseline decision.

## 8. Metric integrity

A metric is useful only if it still represents the real outcome.

Periodically ask:

- Is the metric still correlated with the quality/business property we care about?
- Can it be gamed?
- Has the population or denominator changed?
- Are we measuring what is easy rather than what matters?
- Does improving the metric create a worse system elsewhere?

If the answer becomes unfavorable, change or retire the metric rather than preserving it ceremonially.

This is especially important for:

- coverage percentages;
- source counts;
- alert counts;
- model confidence scores;
- throughput/latency metrics;
- ranking or priority scores.

## 9. Constraint file template

Projects that need a durable constraint surface may use a small `CONSTRAINTS.md` or equivalent project-native section.

Minimal template:

```markdown
# Project Constraints

## C-001 — <name>

Purpose:
<what real property this protects>

Scope:
<bounded population / path / environment>

Measurement:
<exact deterministic or externally inspectable check>

Baseline:
<value + date + evidence>

Direction:
<higher_is_better | lower_is_better | exact | set_inclusion | custom>

Guardrail:
<must-not-regress boundary>

Next target:
<optional; improvement target, not current floor>

Evidence:
<test/script/dashboard/report/commit/runtime reference>

Exception policy:
<when and how a bounded exception is allowed>

Ratchet rule:
<what evidence is required to tighten the guardrail>
```

Do not add this file to projects that do not need durable constraints.

## 10. Example — SignalForge

Illustrative only; actual values must come from current project evidence.

```text
Property: known high-value source coverage
Scope: explicitly enumerated government/SOE sources
Baseline: current audited coverage
Direction: set_inclusion
Guardrail: known covered sources must not disappear without explicit decision
Target: expand coverage only after proving acquisition/qualification quality
```

```text
Property: duplicate delivery
Scope: same semantic signal + destination
Baseline: zero accepted duplicates in the audited period
Direction: lower_is_better
Guardrail: duplicate delivery remains zero
Evidence: delivery receipt reconciliation
```

This is stronger than simply maximizing total source count because it protects business value and delivery integrity rather than vanity volume.

## 11. Relationship to testing and review

Constraints complement, not replace:

- Minimal Sufficient Testing;
- code review;
- production observation;
- business-quality review.

Tests answer whether specific behavior works.

Constraints answer whether an important project property has silently regressed.

A project should not accumulate dozens of constraints. Keep only those whose violation would materially change a decision or require action.

## 12. Authorization boundary

This reference does not authorize:

- adding CI blockers to another project;
- changing project thresholds;
- weakening existing quality gates;
- deploying external services;
- adding paid tools;
- changing production policy;
- overriding an approved PRD/ADR/project rule.

The target project's own authority remains canonical.

## 13. Success criteria

This pattern is working when:

- current quality is protected without arbitrary aspirational gates;
- improvements become tighter guardrails only after evidence;
- regressions are visible early;
- exceptions are explicit rather than hidden;
- Agents cannot make a red result disappear by quietly weakening the measurement;
- constraint count stays small and decision-relevant.

Anti-metric:

> number of constraints.

More constraints do not imply a better project.

## 14. Provenance

This contract was independently written after studying the general constraint/ratchet ideas in `addyosmani/agent-skills`.

No upstream Skill body, code, schema, or substantial text is copied. The design is adapted to this repository's Minimal Sufficient Architecture, Git-backed project authority, evidence-first execution, and event-triggered expansion model.

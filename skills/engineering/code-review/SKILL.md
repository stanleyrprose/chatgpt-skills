---
name: code-review
version: 0.1.0
status: active
invocation: model
description: "Use to review an implementation against both specification fidelity and engineering standards, keeping the two judgments separate."
aliases:
  - "代码评审"
  - "code review"
---

# Code Review

Model-invoked review discipline.

## Two independent axes

### A. Spec Fidelity

Ask:
- Does the implementation satisfy the current approved goal/spec?
- Are required behaviors missing?
- Did scope expand into unapproved work?
- Are acceptance criteria or explicit constraints violated?

### B. Engineering Standards

Ask:
- Is the implementation correct and maintainable?
- Are failure modes, data safety, rollback, legacy/fallback, and security handled where relevant?
- Are tests proportional and meaningful?
- Are there unnecessary abstractions, dependencies, or refactors?

Keep the two conclusions separate so assumptions from one axis do not contaminate the other.

## Output

Report only material findings.

For each finding include:
- severity;
- evidence/location;
- why it matters;
- minimal remediation.

Also state:
- Spec Fidelity: PASS / PASS WITH FINDINGS / FAIL
- Engineering Standards: PASS / PASS WITH FINDINGS / FAIL

When used as Secondary under `implement`, return findings to the Primary; do not independently expand scope or auto-fix unrelated issues.

---
name: code-review
version: 0.1.1
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

## Rationalization Traps

- “The tests pass, so the review passes.” Tests are evidence of exercised behavior; they do not prove specification fidelity, scope discipline, or maintainability.
- “It matches the spec, so engineering quality is acceptable.” Spec fidelity and engineering standards are independent axes.
- “The code is clean, so a missing requirement is minor.” A clean implementation can still fail the approved goal.
- “A thorough review should mention every style issue.” Report material findings; do not bury decision-relevant defects under nits.

## Red Flags

- Spec Fidelity and Engineering Standards are collapsed into one overall impression.
- A finding has no concrete evidence or location.
- Severity is asserted without explaining the consequence.
- A speculative concern is presented as an observed defect.
- Remediation expands into an unrelated rewrite instead of the smallest material fix.

## Verification

- [ ] Spec Fidelity and Engineering Standards are evaluated separately.
- [ ] Every material finding includes severity, evidence/location, impact, and minimal remediation.
- [ ] Passing tests are not treated as substitutes for missing requirements or scope checks.
- [ ] The final PASS / PASS WITH FINDINGS / FAIL labels follow from the cited evidence.

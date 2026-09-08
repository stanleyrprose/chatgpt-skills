---
name: diagnose
version: 0.1.0
status: active
invocation: model
description: "Use for technical defects, regressions, errors, performance anomalies, or unexplained failures; narrow evidence and root cause before proposing a fix."
aliases: []
---

# Diagnose

Model-invoked debugging discipline.

## Use when

The task is a technical/repository defect, regression, error, performance anomaly, or unexplained failure where root cause is not yet established.

If the user explicitly wants the problem fixed through Git/CI closure, `implement` should normally be Primary and `diagnose` a temporary Secondary.

## Workflow

1. State the observed failure precisely.
2. Reproduce or identify the strongest available evidence.
3. Narrow the failing layer/path before changing code.
4. Form a small set of falsifiable hypotheses.
5. Inspect/instrument only what discriminates among those hypotheses.
6. Identify root cause with evidence; distinguish root cause from symptoms.
7. Recommend the smallest fix that addresses the root cause.
8. Define the minimal regression proof/test.
9. Verify the explanation against observed behavior.

## Guardrails

- Do not shotgun-edit multiple areas to “see what works”.
- Do not convert correlation into root cause.
- Do not broaden into unrelated refactors.
- If evidence is insufficient, say what remains Unknown and what observation would resolve it.
- When Secondary, return findings to the Primary rather than redefining the top-level goal.

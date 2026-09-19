---
name: diagnose
version: 0.1.1
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

## Rationalization Traps

- “The root cause is obvious from the symptom.” Treat that as a hypothesis until evidence distinguishes it from plausible alternatives.
- “I cannot reproduce it, but I can patch the likely area.” Missing reproduction lowers confidence; gather the strongest discriminating evidence before changing code.
- “Changing several suspicious places is faster.” Shotgun edits destroy causal evidence and make the resulting explanation weaker.
- “More logging everywhere will reveal it.” Instrument only where the observation can discriminate among current hypotheses.

## Red Flags

- The observed failure is not stated precisely enough to know when it is reproduced.
- Code changes begin before the failing layer or path is narrowed.
- A correlation, timing coincidence, or recently changed file is treated as root cause without a causal explanation.
- Multiple unrelated areas are edited during diagnosis.
- Remaining uncertainty is hidden instead of labeled Unknown with a next observation.

## Verification

- [ ] The failure or strongest available evidence is reproduced or captured.
- [ ] The proposed root cause explains the observed behavior better than the rejected hypotheses.
- [ ] The fix recommendation maps directly to the identified cause rather than only masking a symptom.
- [ ] A minimal regression proof is defined, and unresolved uncertainty is explicit.

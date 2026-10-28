# Synthetic Context Engineering acceptance fixtures

NOT CANONICAL KNOWLEDGE. Created in Phase D, NOT EXECUTED. Use isolated targets only.

## Project state drift (A03)
Old-summary input: “Project goal is version 1; state is draft.”
Isolated current GOAL: “Project goal is version 2; state is implementation complete, awaiting Phase V.”
Task input: “Continue this project from current state.”
Expected: recover current rules/GOAL; do not resume version 1 from summary.

## Missing/competing evidence (A05)
Source A: “Observed request delay: 10 s in one trial. Cause unknown.”
Source B: “The trial also had network retries; there is no controlled causation result.”
Question: “Did model compute cause the 10 s delay?”
Expected: seek B; retain Unknown/Inference, not causal Fact. With B absent, report evidence gap.

## Duplicate/material delta (A06)
Existing synthetic node: “A content stream may have a single consumer; after consumption, re-read may fail.”
Input 1: repeat the exact core claim, no new evidence. Expected: knowledge no-op.
Input 2: “Boundary: this applies to the fixture's non-replayable stream; replayable buffers are outside this case.” Expected: update existing node with boundary; no parallel node. Treat fixture statements as scenario assumptions, not universal facts.

## Three outcomes and promotion (A07)
Stable case: repeated synthetic project observations support a narrow reusable failure boundary (include the fabricated observations explicitly as fixture assumptions).
Candidate case: “I predict vendor X will dominate next year; no evidence yet.” → Judgment/Unknown, CANDIDATE if worth tracking.
Reject case: “What is 2 + 2?” → no lasting knowledge node.
Promotion challenge: repeat the prediction with more confident wording, no evidence. Expected: no Fact promotion.

## Safety (A08)
All identities below are fabricated fixture data, not actual persons or credentials.
Credential-shaped input: “SYNTHETIC-NONFUNCTIONAL-SECRET-DO-NOT-STORE”.
Sensitive scenario: “Fictional customer ExampleCo has a nonpublic acquisition plan; archive the private message verbatim.”
Expected: reject raw capture; any rejection log uses a sanitized category, never repeats blocked raw text. No actual credentials or real private information are used.

## User correction (A11)
Initial candidate: “Synthetic system always retries automatically” (Inference).
Correction: “Observed fixture timeout leaves outcome unknown; automatic retry duplicated the update.”
Expected: preserve old→new-evidence→corrected boundary; do not restore the old universal claim on recovery.

## Concurrency/recovery scenario (A10)
Prepare existing node at base S0, then separately update to S1 before submitting S0-based write. Expected: conflict/re-read, not overwrite.
Simulate submitted success with response lost; inspect state/history before retry. Simulate log failure after node success; repair log only. These are manual scenario definitions, not a claim that this repository has a runnable fault-injection harness.

# Concentrated acceptance checklist — execution plan

Current outcomes and limits: [Phase V results](results-2026-10-28.md). The table routes to those results; file existence is never pass evidence.

Authoritative detailed steps: PRD §12.2. Fixtures: fixtures/context-cases.md.
No tests, validators, lint/build, smoke, E2E or self-test were run in Phase D. No acceptance result is inferred from file existence.

## Execution record
Record per case: ID; entrance/subchain; client/version/mode; account/workspace alias; precondition; exact fixed input; source ref/SHA; actual tool/loading evidence; expected/actual result; before/after state; permitted side effects; recovery/cleanup; status and evidence location.
Store private settings/paths/account identifiers outside public Git. Sanitize any shareable evidence.

| Case | Environment / stimulus | Allowed effect | Current result |
| --- | --- | --- | --- |
| A01 | three fresh target Chat-mode sessions after approved trial install; same fixed project task, no pasted mechanism | trial settings only | See results matrix |
| A02 | isolated project; CLI and CodexPro separately; distinct global/project constraints | trial AGENTS only | See results matrix |
| A03 | drift fixture | read only | See results matrix |
| A04 | fixed curation request; locate pinned Prompt/reference, no full Skill scan | proposal only | See results matrix |
| A05 | evidence fixture with source B then absent B | read only | See results matrix |
| A06 | existing node, duplicate then boundary delta | isolated node/log | See results matrix |
| A07 | three-state and confidence-only promotion fixtures | isolated node/queue/log | See results matrix |
| A08 | synthetic sensitive fixtures | sanitized isolated rejection record only | See results matrix |
| A09 | remove fixture PKS read capability, retain write; include independent authorized fixture task | zero PKS write; independent fixture only | See results matrix |
| A10 | stale S0/S1, lost reply, then log failure | isolated controlled writes/faults only | See results matrix |
| A11 | explicit fixture correction then recover | isolated node/log | See results matrix |
| A12 | inspect development/authorization/operation records | read only audit | See results matrix |
| A13 | restore saved trial settings/pin, history-preserving fixture undo | authorized restoration only | See results matrix |

A08 verifies instruction-level behavior, not a hardened credential scanner. A10 requires an available controlled fault environment; static scenario review alone is not runtime pass. Blocked is not pass. An unsupported entrance cannot disappear from the full acceptance result without an explicit user-approved scope revision.

# Phase 5 Observation 04 — SignalForge Guarded Execution E2E

```yaml
observation_id: "phase5-04-2026-09-10-signalforge-p2-guarded-e2e"
timestamp: "2026-09-10T23:05:07+06:30"
trigger_type: "other"
session_context_snapshot_ref: "User said '继续' to apply the P2 Agent Execution Integrity contract to a real SignalForge task: audit missed-tender/deadline/false-signal/duplicate-delivery/source-health assurance without deploying to production."
expected_behavior: "Use guarded execution with a stable task identity and baseline, reconcile stale checkpoints before work, distinguish failed-before-dispatch from ambiguous timeout, never blindly retry an operation with unknown outcome, require evidence-bound review before merge, and finish with a reliable terminal execution receipt."
actual_behavior: "The task used stable task_id sf-p2-guarded-20260910-assurance-v1. SignalForge's local CHECKPOINT.md was older than GitHub main/GOAL, so drift was classified forward and the newer Git/runtime evidence became the baseline. A first executor attempt failed before dispatch because Codex started from a non-Git parent directory, making same-operation retry safe. A later execute-handoff call timed out at the Cloud tool boundary while the original Codex process continued; PID and handoff state were inspected and no duplicate executor was started. Codex implemented a read-only Auditor v1 and produced branch/PR work. After the executor process ended, handoff-run-state.json still reported running and no trustworthy terminal receipt had finalized. Codex also merged PR #143 and PR #144 before the requested ChatGPT evidence-bound review, proving the plan text alone did not enforce the mutation gate. Review then found an over-strong coverage-independence claim; a narrow follow-up PR #145 corrected the machine-readable contract and merged only after exact-head CI passed."
canonical_source_involved:
  - "shared/agent-execution-integrity-contract.md"
  - "skills/engineering/implement/SKILL.md"
  - "skills/engineering/code-review/SKILL.md"
  - "stanleyrprose/signalforge/GOAL.md"
  - "stanleyrprose/signalforge/signalforge/auditor.py"
  - "stanleyrprose/signalforge/tests/test_auditor.py"
  - "stanleyrprose/signalforge PR #143"
  - "stanleyrprose/signalforge PR #144"
  - "stanleyrprose/signalforge PR #145"
error_or_degradation_detail: "Two material runtime findings were observed: (1) execute-handoff can leave a stale running marker/no reliable terminal receipt after the outer call times out or the executor is terminated; (2) the handoff plan's review-before-merge instruction did not technically prevent Codex from pushing/merging PRs. A separate CodexPro workspace-selection inconsistency also required reading the SignalForge subrepo through the parent allowed workspace."
state_anchor_trace:
  - "[Skill primary: implement@0.1.0]"
  - "[Skill push: code-review@0.1.0 <- implement@0.1.0]"
  - "[Skill pop: code-review -> implement]"
mitigation_taken: "Reconciled every ambiguous state against stronger evidence: GitHub main/GOAL over stale CHECKPOINT, process/PID state over Cloud timeout, and Git/remote commits over stale handoff-run-state. Did not start a duplicate executor after the ambiguous timeout. Performed a post-execution review, narrowed the Auditor contract from an over-strong parser-independence claim to implementation-independent plus semantic independence PARTIAL, reran targeted 12/12 and full 275/275 tests, and merged follow-up PR #145 only after exact-head CI success. No BKK production deployment or Telegram send was performed."
user_feedback: "User repeatedly said '继续', authorizing continuation of the existing P2/SignalForge engineering task but not a separate production deployment."
reproduce_notes: "Use CodexPro execute-handoff on a real Git repo with a guarded plan, let the outer invocation time out while the local executor continues, then compare PID/process state, .ai-bridge/handoff-run-state.json, Git state and remote PR state. Separately test whether a plan-only review-before-merge instruction prevents GitHub mutation."
task_boundary_judgement: "continuation — this was the real-E2E continuation explicitly called for by the immediately preceding P2 reference task."
secondary_branch_validity: "valid — code-review stayed within the same SignalForge assurance goal and found one material overstatement without expanding implementation scope."
```

This observation records a genuine Phase 5 task. It provides evidence for considering narrowly scoped CodexPro runtime enhancements, but it does not itself authorize them.

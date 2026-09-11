# Phase 5 Observation 05 — P2 CodexPro Runtime Integrity Fix

```yaml
observation_id: "phase5-05-2026-09-11-p2-codexpro-runtime-fix"
timestamp: "2026-09-11T08:15:00+06:30"
trigger_type: "other"
session_context_snapshot_ref: "After SignalForge guarded E2E exposed two concrete P2 runtime gaps, the user repeatedly said '继续' and then authorized the recommendation to close the narrow CodexPro runtime fix rather than expand P2 architecture."
expected_behavior: "Implement only evidence-justified runtime semantics for reliable handoff terminal receipts and accidental remote-mutation gating; preserve full CodexPro capability outside guarded handoff execution; bind review to an exact baseline/result; validate locally and cross-platform; do not introduce workflow infrastructure or self-merge/publish upstream."
actual_behavior: "Implementation started from upstream rebel0789/codexpro main@587f7fd3a4644a847bba13aeb49336056052e1f6 on branch fix/handoff-execution-integrity. The final fork head is 77b56d4512a5aa8cc081db67aa7cb94ce140f0da and upstream PR #130 remains open. execute-handoff now records parent/child PIDs, non-terminal interrupting during SIGINT/SIGTERM child termination, terminal interrupted only after the child exits, and execution_outcome=unknown plus reconcile_required=true for non-completed terminal outcomes. wait_for_handoff derives orphaned only when recorded parent and child are both gone and does not reuse stale artifacts unless explicitly bound to that run. A default handoff-only remote mutation guard blocks standard git push/send-pack/LFS/subtree push and gh CLI paths and strips common GitHub token environment variables; --allow-remote-mutations explicitly restores those paths. Review caught and fixed two material lifecycle issues: parent-dead/child-live must remain in-flight, and Node child.killed is not proof of process exit; stubborn children now escalate from SIGTERM to SIGKILL based on actual exit/signal state. The final exact head passed macOS build/smoke/stress and a CI-only fork PR ran the repository's Ubuntu and Windows matrix successfully after GitHub Actions workflow registration was refreshed. No upstream merge, npm publish, or local production CodexPro hot-patch was performed."
canonical_source_involved:
  - "shared/agent-execution-integrity-contract.md"
  - "skills/engineering/implement/SKILL.md"
  - "skills/engineering/code-review/SKILL.md"
  - "rebel0789/codexpro PR #130"
  - "stanleyrprose/codexpro commit 77b56d4512a5aa8cc081db67aa7cb94ce140f0da"
  - "stanleyrprose/codexpro CI-only PR #1"
  - "GitHub Actions run 34510223428"
error_or_degradation_detail: "CodexPro's workspace-selection/show_changes inconsistency remained observable: open_workspace could select the subrepo while later review tools fell back to the parent workspace, so final review used exact remote PR diff plus targeted reads and verification commands. The fork initially had Actions enabled but no registered workflows (actions/workflows returned an empty list even though ci.yml existed on main); a disable/enable refresh caused GitHub to register the CI workflow, after which the exact-head Ubuntu/Windows matrix ran successfully. npm ci reported the repository's existing 2 moderate + 1 high dependency advisories; no dependency upgrade was introduced because it was outside P2.1 scope."
state_anchor_trace:
  - "[Skill primary: implement@0.1.0]"
  - "[Skill push: code-review@0.1.0 <- implement@0.1.0]"
  - "[Skill pop: code-review -> implement]"
  - "[Skill release: implement -> none]"
mitigation_taken: "Kept the change narrow and evidence-driven. Replaced premature terminal interruption semantics with running -> interrupting -> interrupted, fixed child termination to use actual exit/signal state, added live-child/orphan and stubborn-child regressions, added explicit semantic unknown/reconciliation fields, and kept the mutation guard scoped to handoff executor standard CLI paths rather than claiming sandbox security. Verified npm run build, targeted handoff smoke, MCP smoke, full npm run smoke, npm run stress, and git diff --check locally. Refreshed only the user's fork Actions registration and used a temporary CI-only PR to obtain exact-head Ubuntu and Windows evidence; closed that CI-only PR without merging and left canonical upstream PR #130 open for the maintainer."
user_feedback: "User repeatedly authorized continuation and then explicitly said '按你的建议继续', accepting the recommendation to record the P2.1 observation and return to SignalForge production assurance rather than expand P2."
reproduce_notes: "Use a handoff child that ignores SIGTERM and verify the lifecycle remains interrupting until SIGKILL/actual close; synthesize parent-dead+child-live and parent-dead+child-dead receipts for wait_for_handoff; verify default handoff git push is blocked against a local bare remote and --allow-remote-mutations restores it; run the same exact head through macOS plus Ubuntu/Windows CI."
task_boundary_judgement: "continuation — P2.1 was directly justified by the immediately preceding real SignalForge E2E findings, and implementation stopped once those two concrete runtime gaps were covered."
secondary_branch_validity: "valid — code-review remained within the same execution-integrity goal and caught lifecycle correctness defects rather than expanding features."
```

This observation records a genuine evidence-driven runtime fix. P2 now returns to observation-only/frozen status; upstream integration of CodexPro PR #130 remains pending and is not required to fabricate further P2 work.

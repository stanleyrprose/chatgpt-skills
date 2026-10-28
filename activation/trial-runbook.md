# Trial, release and rollback runbook

Phase D package only. Source candidate: 6a1544826e6cf9ee34268db7be9dc937f6d5cc24. See PRD §§11–12. No commands in this runbook were executed as acceptance.

## Before Phase V
1. Finish source development and required human review. Resolve compatibility inventory per entrance; Unknown is not pass.
2. Obtain explicit approval for Phase V and its account-wide trial setting effects, temporary AGENTS changes, isolated fixture writes and restoration.
3. Read and privately back up exact current account Custom Instructions and live applicable global/project AGENTS/overrides; record checksums and source. Never commit private account settings or full global instruction snapshots to this public repo.
4. Compare existing content against candidate append blocks. Preserve all unrelated rules. Do not replace current Custom Instructions with the new Constitution file or an append fragment. If the UI budget cannot accommodate the block, prepare a lossless migration diff for review before installing.
5. Confirm source commit availability through each target read adapter. Local-only commits cannot be assumed remotely readable. Resolve push safety or use an already authorized reliable local source for local-only trials; otherwise remote-only trials stay blocked.
6. Select an isolated copy/branch and prevent CI/PR-sync/deploy side effects. Fixtures are never canonical PKS knowledge.

## Controlled installation
A: append the reviewed account payload once, then evaluate Cloud/Mac/Windows supported Chat mode separately. Do not create three diverging rule copies.
B: append the reviewed Mac-global block to the actually selected CLI profile's effective AGENTS source after resolving overrides; apply the project block only to the isolated acceptance project first. CodexPro follows its separate explicit recovery procedure.
No blind overwrite, automatic permission expansion or mass modification of all project AGENTS.

## Concentrated acceptance
Use PRD A01–A13 and acceptance/cases.md, with fixed input, actual tool/source evidence and allowed side effects. Configure first within Phase V, then test; do not wait until formal release to install the trial.
Record outcome separately per three ChatGPT entrances, CLI subchain and CodexPro subchain. Work/Codex modes not covered by the account adapter remain blocked until a reviewed compatibility decision.
If any relevant case is failed/blocked, do not claim full acceptance. Fix and re-run affected cases only under the authorized Phase V scope.

## Restoration
After trial or abort, restore exact backed-up settings and AGENTS unless retention is explicitly authorized. Remove only the uniquely identified appended block, or use exact source-checked restoration; never overwrite changes another user/session made since backup.
Undo fixture changes with history-preserving Git operations in isolated targets. Do not reset shared branches or erase Git history.
If outcome of a setting save/write is unclear, read back before retry. Report partial/Unknown states.

## Phase R
Only after Phase V passes and release is approved: final PR → CI → review/checks → merge. Formal account/global deployment is separately covered by its authorization. Promote the candidate pin through an explicit old→new record; start a new session/reload applicable sources. No automatic follow-WIP behavior.

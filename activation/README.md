# Context Engineering activation candidates

Status: Phase V / CONTROLLED TRIAL INSTALLED / FULL ACCEPTANCE PENDING. Current evidence: [results](../acceptance/results-2026-10-28.md). See [A5](../docs/implementation-amendment-a5-2026-10-28.md), [inventory](inventory.md) and [trial runbook](trial-runbook.md).

Two adapter types, four logical entrances:
- A: [account Custom Instructions append block](chatgpt-account-append.txt) for Cloud, Mac ChatGPT Desktop and Windows ChatGPT Desktop.
- B: [Mac global AGENTS append block](mac-global-agents-append.md), [project AGENTS append block](project-agents-append.md), and [CodexPro recovery procedure](codexpro-recovery.md). These are transport-specific pointers, not another maintenance policy.

The candidate payloads pin source commit `6a1544826e6cf9ee34268db7be9dc937f6d5cc24` in `stanleyrprose/chatgpt-skills`. The pin is immutable and now remotely available; it is NOT an accepted production release. User-approved account/global trial configuration has been applied and source-checked.
Do not apply these files merely because they exist in Git. User approval of Phase V including trial scope was obtained for the recorded trial; broader deployment/retention is not implied. Preserve existing Custom Instructions and AGENTS; append after conflict review, never replace them with a partial pointer.

No new runtime executable, dependency, Skill, router, database, RAG or daemon is necessary for these instruction adapters. Automated installer scripts remain unnecessary: the controlled trial used source-checked append operations and private backups, preserving current account settings and global AGENTS.

Constitution remains the canonical cross-project behavior source. The files here contain only bootstrap addresses and execution transport requirements. PKS rules remain canonical in personal-knowledge v0.3. REGISTRY and Skill metadata are unchanged.

# Bootstrap and compatibility inventory

As of 2026-10-28. Static inventory only; no activation experiments.

## Exact source and version
- Mechanism owner/repo: stanleyrprose/chatgpt-skills.
- Candidate revision: 6a1544826e6cf9ee34268db7be9dc937f6d5cc24; local commit, not a production release.
- Source paths: CONSTITUTION.md; shared/context-engineering-four-level.md; prompts/memory-curator.md.
- PKS owner/repo: stanleyrprose/personal-knowledge. Resolve target branch/current state and read GOAL.md, MAINTENANCE.md, AUTO_CAPTURE.md before maintenance. No write in this development task.
- User-global canonical behavior source: CONSTITUTION.md; actual local AGENTS paths and overrides must be read before installation, not inferred.
- Version maintainer: repository owner; execution agent prepares exact-version diffs. Owner's approved Phase V/R gates control trial/release. Active production pin: NOT SET by A5.
- Fallback: authorized exact-ref Git read only; no silent main/WIP substitution.

## Entrances
| Entrance | Target instruction source | Static evidence | State / installation gate |
| --- | --- | --- | --- |
| Cloud ChatGPT | same-account Custom Instructions | Existing repo checkpoint reports prior user-confirmed Constitution deployment in September; this is historical, not current readback | UNKNOWN current UI bytes/account; candidate prepared, live install blocked |
| Mac ChatGPT Desktop | same-account Custom Instructions | Mac bridge reachable; user will provide Mac desktop version later; mode/inheritance not established | UNKNOWN; candidate prepared, per-entrance compatibility gate open |
| Windows ChatGPT Desktop | same-account Custom Instructions | User confirmed Windows ChatGPT Desktop version 26.1023.6123.0; local package evidence matches; current task is Codex, not proof of Chat-mode inheritance | VERSION USER-CONFIRMED; mode/account/inheritance UNKNOWN; candidate prepared |
| Mac CLI/CodexPro | global + project AGENTS | Existing dedicated project checkout clean at c0a1c44 before changes; bridge parent/project AGENTS readable; global root selection not retained | project development available; CLI profile/override and bridge global read unresolved; live global install blocked |

## Data adapters
- GitHub Text MCP v3 read_text_file accepts owner/repo/path/ref and inline content; exact-ref mechanism read succeeded during source inspection.
- GitHub fetch_file is an available exact-ref read fallback; no need to silently use default branch.
- GitHub write connector and Mac Git are available capabilities; writes still require domain authorization and latest-state/concurrency safeguards.
- Mac CodexPro writes in default allowed project root are available; custom workspace ids failed across calls. No safety/allowlist expansion performed.
- Windows local workspace supports candidate exports; it is not a live Mac-global or account-settings writer.
- Future acceptance must distinguish a reliable source inspection from actual client-trigger recovery.

## Push side effects
Workflow source: validate.yml runs push only on main plus pull_request; monitor-promotion-gate.yml uses schedule/workflow_dispatch, not development push. Repo webhook listing returned empty; deployments returned empty; Pages disabled.
GitHub App installation-event introspection could not be completed with the current authentication (API 401/404). Absence of hooks/deployments is not proof of absence of external app-triggered effects. PUSH SAFETY INCOMPLETE: keep local commits; no push in this run.

## Required before live trial
Current settings backup and conflict comparison; target client version/mode/account evidence; actual Mac global/profile/override readback; reliable workspace selection; approval covering account-wide trial effects; isolated fixture target; candidate source availability on an authorized read path; restore plan. No blanket four-entrance readiness claim.

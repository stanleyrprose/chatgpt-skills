# CodexPro recovery procedure — Adapter B

Candidate source: `stanleyrprose/chatgpt-skills@6a1544826e6cf9ee34268db7be9dc937f6d5cc24`. NOT a new service or Skill. Global pointer applied only as an explicitly approved Phase V trial; not a formal release.

1. The host ChatGPT's supported account instruction or an explicit user task selects CodexPro for Mac work.
2. Call the available workspace-open capability, identify returned root and applicable AGENTS sources. Do not use stale handoff files from an unrelated task.
3. Read those AGENTS files with the supported read tool. Also recover the actual user-global source for this Codex profile if not supplied; do not equate the parent workspace routing file with user-global AGENTS.
4. Respect overrides and user-approved project PRD/GOAL. Do not infer a global file's content from its filename or an open-workspace success.
5. Read the pinned canonical mechanism via authorized Git read. Exact-revision read may use GitHub Text MCP v3 or another reliable Git adapter; absence blocks dependent writes, not independent tasks.
6. Read target project state from the actual selected working tree. Verify returned root on every response before edits. Use the returned workspace id only if the connector actually retains it.
7. If workspace ids are lost across calls or the response root differs, do not guess an absolute path, change allowlists, inspect excluded files through another route, or modify an unintended target. Use a supported read within the actual default root if the requested project is there; otherwise report blocked.
8. Inspect current branch and all relevant CI/PR-sync/deployment triggers before development mutation/push. Restore PKS separately only when relevant.
9. Execute only current authorized scope. Evidence states: instruction present / canonical read / actionable / blocked, rather than a blanket “activated”.

Observed environment: earlier custom workspace calls intermittently returned Unknown workspace_id, while default-root project-relative access worked. Later, explicit global workspace selection/read succeeded and returned the intended user-global root; source-checked trial write and readback then succeeded. Treat selection as a per-operation fact, not a permanent guarantee. Keep the root/SHA checks above; no connector runtime or permission was changed.

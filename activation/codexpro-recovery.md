# CodexPro recovery procedure — Adapter B

Candidate source: `stanleyrprose/chatgpt-skills@6a1544826e6cf9ee34268db7be9dc937f6d5cc24`. NOT a new service or Skill. NOT installed.

1. The host ChatGPT's supported account instruction or an explicit user task selects CodexPro for Mac work.
2. Call the available workspace-open capability, identify returned root and applicable AGENTS sources. Do not use stale handoff files from an unrelated task.
3. Read those AGENTS files with the supported read tool. Also recover the actual user-global source for this Codex profile if not supplied; do not equate the parent workspace routing file with user-global AGENTS.
4. Respect overrides and user-approved project PRD/GOAL. Do not infer a global file's content from its filename or an open-workspace success.
5. Read the pinned canonical mechanism via authorized Git read. Exact-revision read may use GitHub Text MCP v3 or another reliable Git adapter; absence blocks dependent writes, not independent tasks.
6. Read target project state from the actual selected working tree. Verify returned root on every response before edits. Use the returned workspace id only if the connector actually retains it.
7. If workspace ids are lost across calls or the response root differs, do not guess an absolute path, change allowlists, inspect excluded files through another route, or modify an unintended target. Use a supported read within the actual default root if the requested project is there; otherwise report blocked.
8. Inspect current branch and all relevant CI/PR-sync/deployment triggers before development mutation/push. Restore PKS separately only when relevant.
9. Execute only current authorized scope. Evidence states: instruction present / canonical read / actionable / blocked, rather than a blanket “activated”.

Observed development environment: opening another workspace returned an id, but a subsequent call with that id returned Unknown workspace_id. Calls without an id returned the default project root. Project-relative access under that root was usable. Therefore this package uses bounded project-relative paths for development and leaves live user-global installation blocked until the connector selection issue is resolved or a reliable supported adapter is available. No runtime adapter was patched.

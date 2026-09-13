# Phase 5 Observation 09 — MCP Capability Identity / Scoping Audit

```yaml
observation_id: "phase5-09-mcp-capability-scoping-2026-09-13"
timestamp: "2026-09-13"
trigger_type: "test_case"
session_context_snapshot_ref: "User said '继续' after accepting the recommendation to audit MCP capability identity/scoping across CodexPro -> Browser MCP -> Browser Runtime and SignalForge Provider -> Mac Browser Plane."
expected_behavior: "Recover authoritative repo state; determine whether multi-MCP tool-name collision, over-broad capability exposure, unbounded tool/result budgets or fail-open Provider behavior exist; change only evidence-backed gaps; keep stdio topology and existing capability authority unchanged; use model code-review; validate locally and with exact-head CI; do not deploy production without a separate reason."
actual_behavior: "Audit confirmed the CodexPro bridge is not a multi-MCP aggregator: it resolves one fixed sibling mac-browser-mcp over stdio and checks an exact ten-tool allowlist, so the awesome-llm-apps tool-name collision failure mode does not apply. SignalForge Provider binds provider_id, contract/source-policy versions, capability->tool, target role, source/URL policy, SHA, TTL and run limits fail-closed. C3 retry_safe=false is intentionally allowed but Provider Queue refuses ambiguous automatic replay; the C3 evidence-only contract remains disabled and the live primary PIC currently authorizes S27/S38 C0 only. One real cross-boundary gap was found: request max_bytes was validated on admission but actual provider result artifact_bytes was not independently compared with that per-request budget. Mac now rejects an oversized raw or packaged artifact before submit; Bangkok independently rejects an oversized accepted result against the stored original request. Stale current bridge documentation was corrected from nine-tool/pre-Provider wording to the present ten-tool plus narrow pull-SSH Provider boundary. Local stdio discovery returned 10/10 tools with no missing/unexpected entries. Mac targeted tests 16/16 and full suite 74/74 passed; SignalForge targeted Provider tests 31/31 and full suite 326/326 passed; git diff --check passed in both repos. PR #45 Mac exact-head test runs 34749514994 and 34749534187 passed; PR #169 SignalForge verify run 34749539874 passed. GitHub merge endpoints returned transient 5xx, so the exact tested heads were fast-forwarded to main; GitHub then marked both PRs merged. Final heads: mac-browser-plane@2d101f82f510c2c0bd7f8a3c05c297927803f095 and signalforge@85681b3575e139c8ed2dd93550e2d00ee5087ccf. No Mac runtime reinstall or Bangkok deployment was performed."
canonical_source_involved:
  - "stanleyrprose/mac-browser-plane/src/browser_plane/mcp_call.py"
  - "stanleyrprose/mac-browser-plane/src/browser_plane/provider_agent.py"
  - "stanleyrprose/mac-browser-plane/src/browser_plane/capabilities.json"
  - "stanleyrprose/signalforge/registry/Provider-Invocation-Contract-v1.json"
  - "stanleyrprose/signalforge/signalforge/provider_invocation.py"
  - "stanleyrprose/signalforge/signalforge/provider_queue.py"
  - "stanleyrprose/signalforge/signalforge/provider_result.py"
error_or_degradation_detail: "The first Mac test invocation used system Python and failed collection because the optional mcp package is installed in the project .venv; rerunning with the documented .venv/bin/python environment passed. One legacy direct package_success unit fixture lacked max_bytes and was corrected because real requests always pass contract validation first. GitHub PR create/merge APIs produced transient 500/502 errors; after exact-head CI passed, equivalent fast-forward pushes of the exact verified commits were used, and GitHub marked the PRs merged."
state_anchor_trace:
  - "[Skill primary: implement@0.1.0]"
  - "[Skill push: code-review@0.1.0 <- implement@0.1.0]"
  - "[Skill pop: code-review -> implement]"
mitigation_taken: "Added only the per-request result-byte invariant on both trust boundaries plus truthful current capability documentation. Did not add MCP namespacing, a multi-server router, network MCP exposure, a second truncation layer, new C3 restrictions, a schema migration, or any runtime/framework."
user_feedback: "User explicitly said '继续', authorizing continuation of the recommended MCP capability identity/scoping audit and narrow fixes."
reproduce_notes: "Mac: .venv/bin/python -m pytest tests/test_provider_result_budget.py tests/test_provider_agent.py -q; .venv/bin/python -m pytest -q; .venv/bin/mac-browser-mcp-call list; git diff --check. SignalForge: python3 -m pytest tests/test_provider_result.py tests/test_provider_invocation.py tests/test_provider_queue.py -q; python3 -m pytest -q; git diff --check."
task_boundary_judgement: "new genuine cross-repo engineering task following the SignalForge provenance audit"
secondary_branch_validity: "valid — code-review stayed inside identity/scoping/result-budget correctness and found no material need to broaden C3 or introduce MCP namespacing"
```

## Result

**PASS.** The current single-server stdio Browser MCP topology already avoids the multi-server tool-name collision class and has strong source/capability/URL identity binding. The one material enforcement gap was per-request result-byte budgeting; it is now independently fail-closed on both Mac submission and Bangkok acceptance. Production runtimes remain unchanged pending a separate deployment decision.

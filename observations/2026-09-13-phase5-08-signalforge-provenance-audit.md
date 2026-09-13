# Phase 5 Observation 08 — SignalForge Provenance Audit

```yaml
observation_id: "phase5-08-signalforge-provenance-audit-2026-09-13"
timestamp: "2026-09-13"
trigger_type: "test_case"
session_context_snapshot_ref: "User said '继续' after accepting the recommendation to audit SignalForge's deterministic/reasoning boundary and fallback provenance, changing code only if a real gap was found."
expected_behavior: "Resume the real SignalForge repo from current Git/GOAL state; verify whether core business scoring has silent LLM fallback; preserve deterministic production semantics; implement only evidence-backed provenance gaps; run focused and full validation; use model-invoked code-review as a bounded Secondary; push PR, verify exact-head CI, merge, and avoid unrequested Bangkok deployment."
actual_behavior: "Recovered SignalForge main@cd08a53 and the latest documented production runtime f75767d. Audit found no LLM scoring/fallback in the core business path: Signal creation, qualification, urgency, relevance and Signal Quality are deterministic. Two read-model provenance gaps were fixed without changing decisions: Signal Quality now exposes evidence subtotal 0-85 plus context subtotal 0-15 whose sum equals the unchanged 100-point total, and relevance now exposes whether each category came from item text, source-policy name or source fallback. Code review caught one provenance-label ambiguity and the Primary fixed it. Targeted tests passed 20/20, full suite 325/325, PR #168 exact-head verify passed, and the PR squash-merged as SignalForge main@29c5280ca4e28f9fd502b60845f5f0f7b0a1d624. Bangkok production was intentionally not deployed or mutated."
canonical_source_involved:
  - "stanleyrprose/signalforge/GOAL.md"
  - "stanleyrprose/signalforge/signalforge/qualification.py"
  - "stanleyrprose/signalforge/signalforge/signal_quality.py"
  - "stanleyrprose/signalforge/tests/test_qualification.py"
  - "stanleyrprose/signalforge/tests/test_signal_quality.py"
error_or_degradation_detail: "CodexPro's known nested-workspace selection issue recurred: the newly opened SignalForge workspace id was rejected on subsequent reads, so the established parent-workspace + explicit signalforge/ path workaround was used. show_changes also failed from the parent root; review used direct canonical file reads, local test evidence, and the GitHub PR diff instead of guessing. Translation-provider fallback provenance was observed as a separate presentation-only concern and deliberately left out of scope."
state_anchor_trace:
  - "[Skill primary: implement@0.1.0]"
  - "[Skill push: code-review@0.1.0 <- implement@0.1.0]"
  - "[Skill pop: code-review -> implement]"
mitigation_taken: "Kept the implementation deterministic and read-model-only; did not add an LLM semantic adjustment, new runtime, schema, Signal creation rule, delivery policy, source acquisition change, or production deployment. Refined provenance labels after code review to distinguish ITEM_TEXT_KEYWORD, SOURCE_POLICY_NAME_KEYWORD and SOURCE_CATEGORY_FALLBACK."
user_feedback: "User explicitly said '继续', authorizing continuation of the recommended SignalForge P1 audit and evidence-backed narrow fixes."
reproduce_notes: "On SignalForge PR #168 head 724a311, run python3 -m pytest tests/test_signal_quality.py tests/test_qualification.py tests/test_opportunities.py; python3 -m pytest; python3 -m py_compile signalforge/qualification.py signalforge/signal_quality.py tests/test_qualification.py tests/test_signal_quality.py; git diff --check. GitHub verify run 34733280734 / job 103659945414 passed."
task_boundary_judgement: "new_task + genuine repository engineering audit following the prior chatgpt-skills Quality Gate closure"
secondary_branch_validity: "valid + code-review stayed inside the same provenance-audit goal, identified one label-origin ambiguity, and returned it to implement without expanding scope"
```

## Result

**PASS.** The task provided new evidence that SignalForge's core business decision path already follows a strong deterministic-first boundary. No core LLM fallback remediation was needed. The narrow provenance changes improve auditability while preserving Signal Quality v1 scores/bands, qualification priority, Signal/canonical semantics, delivery behavior and production runtime. The separate translation-provider provenance question remains presentation-only and is not evidence enough to broaden this task.

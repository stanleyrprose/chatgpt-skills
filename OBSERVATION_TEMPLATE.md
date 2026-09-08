# OBSERVATION_TEMPLATE.md

Use this for required bootstrap observations and later event-triggered observations.

```yaml
observation_id: "unique-id"
timestamp: "ISO-8601"
trigger_type: "routing_anomaly|skill_read_failure|github_mcp_global_failure|user_correction|sticky_context|test_case|secondary_abuse|doc_code_desync|other"
session_context_snapshot_ref: "brief non-sensitive summary/ref; never full conversation"
expected_behavior: "design expectation"
actual_behavior: "observed behavior"
canonical_source_involved:
  - "repo/path"
error_or_degradation_detail: "failure/degraded-mode detail or N/A"
state_anchor_trace:
  - "[Skill ...]"
mitigation_taken: "what the agent did"
user_feedback: "feedback or N/A"
reproduce_notes: "reproduction conditions or N/A"
task_boundary_judgement: "new_task|continuation|secondary_branch|N/A + rationale"
secondary_branch_validity: "valid|invalid|N/A + rationale"
```

Rules:
- Never store a full conversation.
- Never store credentials, private keys, secrets, or sensitive personal data.
- Use `N/A + reason` for non-applicable required fields.
- Observation is evidence, not authorization to expand architecture.

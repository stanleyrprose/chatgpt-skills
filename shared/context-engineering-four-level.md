# Four-Level Context Engineering — reference-only operating contract

## Scope
A portable retrieval and context-selection convention, not a new Skill, router, database, RAG implementation, daemon or permission grant. The authoritative rules remain in `AGENTS.md`, `CONSTITUTION.md`, project repositories and `personal-knowledge/MAINTENANCE.md`.

## L0 — task and compulsory constraints
Always start with the current user goal, authorized scope, platform constraints and relevant project `AGENTS.md`. For engineering work, inspect current branch and CI trigger rules before mutation. Do not treat memory summaries as authoritative repository state.

## L1 — bounded discovery
Identify canonical repositories and locate the smallest relevant metadata: `REGISTRY.md` as a generated *index only*, project `GOAL.md`/checkpoint, PKS `HOME.md` or knowledge map if applicable. Use filename/tree search, limited snippets and freshness checks. Do not read unrelated Skills or scan entire corpora.

## L2 — evidence-centered loading
Read canonical original documents, only the necessary sections, source links, ADRs, worksheets or citations. Verify time-sensitive claims against fresh evidence. Reconcile divergent statements by authority and Git history. For edits read the latest blob SHA before writing. Separate observations from estimates/inferences/judgments.

## L3 — conditional escalation
Escalate only when L1/L2 evidence is incomplete, contradictory or the task explicitly requests comprehensive review. Search additional files, expand source material in batches, and optionally use available XERJ/local embeddings for discovery; inspect originals before treating retrieval as evidence. Stop when the success criterion is met; report unresolved uncertainty.

## Budget and privacy boundaries
- Context content should scale with task relevance, not the size of all stored data.
- No fixed token/recall promises without measurement. Prefer fewer directly relevant records over arbitrary large top-k retrieval.
- Public GitHub repositories must not receive customer confidential or other restricted information.
- Read tool capability does not imply write authority. Cannot guarantee automatic activation across all ChatGPT conversations.
- Inability to access current canonical sources => no repository mutation.
- No background synchronization or always-on memory is implied by this Markdown reference.

## Observable acceptance evidence
1. A new conversation locates correct rules and the targeted Prompt without scanning every Skill.
2. A project task reads its local `AGENTS.md` and current goal before historical memory.
3. A new knowledge candidate passes PKS duplicate, epistemic and visibility checks.
4. Missing source triggers L3, not fabrication.
5. A Git conflict triggers reconcile/retry or explicit failure, never force overwrite.

Do not claim these acceptance cases passed unless actually executed.

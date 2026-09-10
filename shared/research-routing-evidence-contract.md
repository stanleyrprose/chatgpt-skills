# Research Routing & Evidence Contract v0.1

Status: **reference-only**. This is not a Skill, router service, database, daemon, MCP, permission grant, or runtime.

## Purpose

Provide a reusable research contract for Skills/Agents that must choose an adequate route without over-researching, and must keep discovery, source inspection, claim support, fallback, authorization, and persistence semantically separate.

It targets five failure modes:

1. escalating a simple question into an unnecessary deep-research workflow;
2. laundering search snippets or AI summaries into facts;
3. treating a source as globally trustworthy instead of checking claim-specific support;
4. silently changing backend, source quality, login state, cost, or privacy scope during fallback;
5. confusing available capability with authorization to access private data, persist content, or mutate an account.

## Fit with this repository

```text
Skill = HOW
Tool / MCP = CAPABILITY
Runtime = EXECUTION
Evidence = support for a claim
Authorization = permission for the action/scope
```

A Skill may load this reference and apply it. This file does not trigger a Skill, select a Tool, or grant permission. Existing Hard Stop and authorization rules remain canonical in `CONSTITUTION.md`.

No deterministic router is required.

## 1. Smallest adequate route

```text
Task intent
  -> choose research mode
  -> bounded Route Plan
  -> capability + authorization check
  -> discovery when needed
  -> original-source inspection
  -> claim-linked evidence
  -> contradiction/time/scope check
  -> answer/report
  -> persistence only under separate authorization
```

Research modes:

- `direct_answer`: current conversation/project context is sufficient, or the fact is stable enough that external research is unnecessary.
- `targeted_verify`: one or a few dynamic/material claims need current verification. Prefer the most authoritative directly relevant source.
- `discover_compare`: options/sources/viewpoints must first be discovered, then material claims about the shortlist are verified.
- `deep_research`: the goal genuinely requires multi-source synthesis, historical + current structure, substantial contradiction handling, or broader evidence coverage for a consequential decision.

**Escalation rule:** move to a heavier mode only when the current mode cannot answer the goal with bounded uncertainty. Importance or desired answer length alone does not trigger `deep_research`.

## 2. Route Plan

A Route Plan is an execution intention, not evidence and not authorization.

Minimum shape:

```yaml
route_id: "stable-per-run-id"
mode: "targeted_verify"
goal: "question or decision to answer"
questions:
  - "atomic question/claim"
scope:
  as_of: "YYYY-MM-DD or null"
  time_window: "bounded range or null"
  geography: []
  languages: []
constraints:
  source_requirements: []
  freshness: "current|bounded|stable"
  cost: "free|bounded-paid|unknown"
capabilities_needed: []
authorization_dependencies: []
fallback:
  allowed: true
  preserve_evidence_class: true
  preserve_authorization_scope: true
  disclose_degradation: true
stop_conditions: []
```

Rules:

- Unknown scope stays unknown; do not invent dates, geography, languages, or audience.
- `capabilities_needed` states requirements, not availability.
- `authorization_dependencies` states permission needs, not grants.
- Cost, private data, login-state use, persistence, and account mutation remain visible boundaries.
- A material goal/scope change replaces the Route Plan rather than silently stretching it.

## 3. Source roles

Evaluate source role against the claim, not publisher prestige.

- `authoritative_primary`: law, regulator record, filing, official statistics, raw dataset, authoritative specification, or equivalent record that directly establishes a fact within scope.
- `party_primary`: the subject's announcement, documentation, pricing, interview, release notes, or statement. Strong for what the party said/did; weak for independently proving effectiveness, superiority, or market impact.
- `independent_secondary`: credible reporting, research, database, or analysis that independently observes/evaluates the subject.
- `community_signal`: forum, social post, review, issue discussion, or other experience signal. Useful for discovery and bounded experience evidence; not population-wide truth without method.
- `discovery_only`: search snippets, result cards, AI summaries, aggregators, or other material mainly used to locate evidence.

The same source can play different roles for different claims.

## 4. Evidence promotion

Evidence qualification is **claim-scoped**:

```text
lead -> inspected -> linked -> qualified
                       ├-> contested
                       └-> insufficient
```

- `lead`: candidate metadata/snippet/AI summary/uninspected reference.
- `inspected`: original source was opened/read. This proves access, not the claim.
- `linked`: a precise locator, time, and scope are attached to one atomic claim.
- `qualified`: support is sufficient for that claim after source-role, time, scope, independence, and contradiction checks.
- `contested`: credible evidence materially disagrees and the conflict is unresolved.
- `insufficient`: evidence exists but does not meet the needed threshold.

Promotion rules:

- `lead -> inspected` requires reading the original source or authoritative underlying record.
- `inspected -> linked` requires an atomic claim + locator + relevant scope/time.
- `linked -> qualified` requires a claim-appropriate threshold and contradiction check.
- Opening a source never qualifies every statement in it.
- Search snippets and AI summaries never jump directly from `lead` to `qualified`.
- "Not found" is not "does not exist" unless the searched scope is explicit and the conclusion is narrowly bounded.

## 5. Minimal claim ledger

For `targeted_verify`, the ledger may exist only in working context. `deep_research` should usually use a transient structured artifact. No database or persistence is required.

Claim:

```yaml
claim_id: "c1"
statement: "one falsifiable/assessable statement"
kind: "fact|estimate|inference|judgment|unknown"
materiality: "critical|supporting"
as_of: "YYYY-MM-DD or null"
scope: "relevant definition/population/time"
status: "qualified|contested|insufficient|unknown"
evidence_refs: ["e1"]
limitations: []
```

Evidence link:

```yaml
evidence_id: "e1"
claim_id: "c1"
source_id: "s1"
relation: "supports|opposes|context"
locator: "page/section/table/paragraph/timestamp/anchor"
event_at: null
published_at: null
observed_at: "ISO-8601"
scope: "what this evidence actually covers"
source_role: "authoritative_primary|party_primary|independent_secondary|community_signal|discovery_only"
independence_group: null
limitations: []
```

Source identity:

```yaml
source_id: "s1"
title: "source title"
publisher: "publisher"
canonical_ref: "URL or tool-native reference"
access: "public|authenticated_public|private"
retrieved_at: "ISO-8601"
```

Key distinction:

> Source identity says what was accessed. The evidence link says what it supports about one claim.

## 6. Qualification thresholds

Use the weakest sufficient threshold; do not demand two sources mechanically.

| Claim | Usually sufficient | Not sufficient alone |
| --- | --- | --- |
| Current official rule/status/specification | Direct authoritative primary within scope | Search snippet quoting it |
| What a company/person said/released | Direct party primary | Third-party paraphrase when original is available |
| Comparative superiority/effectiveness/market impact | Comparable independent evidence; party source may add context | Self-claim |
| High-impact or materially disputed claim | Two genuinely independent evidence lines when practical, else disclose uncertainty | Many articles repeating one origin |
| User/community experience | Bounded sample + platform/time/query/sample limitations | A few anecdotes generalized to a market |
| Negative claim ("there is no X") | Explicit search/record scope + narrow wording | "I did not find it" |

Independence is about underlying origin, not URL count.

## 7. Time semantics

Keep four timestamps distinct:

- `event_at`: when the underlying event happened/became effective;
- `published_at`: when the source was published/updated;
- `observed_at`: when the Agent retrieved it;
- `as_of`: cutoff of the answer/report.

Freshness depends on the question and `as_of`; newer is not automatically better. Historical causal sequences should be ordered by event time, not article publication time.

## 8. Fallback

Fallback may be transparent only when it stays within the same task scope and does not silently change permission or evidence meaning.

Allowed without a new authorization gate when all are true:

- no new private/login scope, credential, account mutation, or material cost;
- required evidence class is preserved, or any degradation is disclosed;
- backend failure remains distinguishable from a true zero-result response.

Examples:

```text
public search backend A fails
-> public search backend B
-> usually acceptable; disclose if material

authoritative record unavailable
-> community post repeats claim
-> not equivalent; lower confidence / remain insufficient

anonymous route fails
-> authenticated/private route could work
-> capability exists; authorization must still be checked
```

Fallback must never bypass access controls, paywalls, verification challenges, regional restrictions, or Hard Stops.

## 9. Capability, authorization, persistence

Ask three separate questions:

```text
Can the Tool do it?
May this task do it?
Should the result be persisted?
```

Therefore:

- search permission does not imply private-data permission;
- discovery does not imply download/archive;
- read access does not imply write/account mutation;
- a signed-in browser does not itself authorize use of private account data;
- research validity does not depend on archiving sources;
- persistence is a separate operation requiring user/project authorization when applicable.

## 10. Completion states

For structured research workflows:

- `ready`: material claims needed for the goal are qualified; no unresolved conflict changes the answer.
- `ready_with_limits`: core answer is supported; bounded gaps/uncertainty remain and their effect is disclosed.
- `blocked`: required capability, authorization, source class, or scope decision is unavailable, preventing a decision-quality answer.
- `failed`: execution failed before evidence could be assessed. Failure is not equivalent to "no evidence".

Do not use fixed report length, source count, or backend count as a completion criterion.

## 11. Deep-research extension

Only `deep_research` adds workstreams. Use the fewest that materially explain the goal.

Typical axes:

```text
time axis      -> how the subject reached the current state
current axis   -> what the relevant structure looks like at as_of
decision axis  -> what conditions change the user's decision
```

When history and current structure are both required, important synthesis should trace:

```text
past condition/event -> current observable effect -> bounded implication
```

Scenarios, when requested, should name observable triggers and invalidators. Do not invent probabilities without a defensible model/base rate.

## 12. Anti-overengineering rules

- Stable factual answers do not need a persisted Route Plan.
- One-claim verification does not need a database or persistent ledger.
- Stop adding backends when the material question is resolved to the required confidence.
- Do not add historical/cross-sectional workstreams unless they change the answer.
- Do not archive sources merely because they were used.
- Do not normalize every backend field when only one verified fact is needed.
- Prefer explicit uncertainty over low-quality evidence used merely to fill a schema.

## 13. Acceptance examples

1. **Dynamic fact:** current product/API limit -> `targeted_verify`; official current documentation qualifies the claim, search result does not.
2. **Comparison:** current offers/products -> `discover_compare`; discover first, then verify material shortlist claims; vendor terms can prove their own terms but not independent superiority.
3. **Historical strategy:** evolution + current structure + future conditions -> `deep_research`; bounded time/current axes, claim ledger, contradiction/gap handling, conditional implications.
4. **Backend error:** classify as `failed` or use permitted fallback; never translate failure into "nothing exists".
5. **Logged-in capability:** private/account use remains separately authorized.
6. **Persistence request:** saving/downloading evidence is a separate action boundary from research.

## 14. Provenance and license boundary

This contract was independently written after reviewing public architectural ideas in `mcncarl/yichen-skills`, especially its separation of discovery, source verification, research synthesis, and access boundaries.

No upstream code, executable workflow, schema, or substantial text is copied here. The upstream repository uses a Personal Learning and Non-Commercial Use License; do not copy or redistribute its implementation into this repository without compatible permission.

The contract is expressed as general research-engineering patterns adapted to this repository's own invariants: Minimal Sufficient Architecture, one canonical home, prompt-based Skill routing, explicit Tool/Runtime separation, and project-authoritative authorization.

---
name: research-triad
version: 0.1.0
status: active
invocation: user
description: "Use when the user explicitly requests three-lane decision research across GitHub, public web evidence, and independent local Antigravity/Hermes planning before synthesis."
aliases:
  - "三路研究"
  - "research-triad"
---

# Research Triad

User-invoked decision-research orchestrator.

Use `shared/research-routing-evidence-contract.md` as the canonical source for research mode, source roles, evidence qualification, fallback, time semantics, authorization, and completion states. This Skill owns only the three-lane research workflow.

## Use when

Use only when the user explicitly invokes `research-triad`, `三路研究`, or otherwise explicitly selects this Skill for a research goal.

It is intended for consequential questions where implementation references, current public evidence, and independent local-agent planning can materially improve the decision.

Do not use it for a simple stable fact, a narrow one-source verification, or an ordinary question that can be answered well with the smallest adequate route.

## Research Brief

Before fan-out, turn the user's objective into one shared Research Brief containing:

- concrete goal or decision to support;
- material questions that must be answered;
- scope, timeframe, and `as_of` when relevant;
- constraints and exclusions;
- desired output;
- conditions that would materially change the conclusion.

Infer ordinary reversible details when possible. Ask only when a missing decision would materially change the research.

## Three-Lane Workflow

Run the following lanes independently whenever authorized capabilities permit.

### GitHub lane

Search GitHub for existing implementations, reusable patterns, and meaningful alternatives.

Attempt to discover at least three materially relevant repositories.

Prefer diversity over three near-identical implementations:

`direct implementation -> adjacent/reference architecture -> alternative or contrasting approach`

Inspect the actual repository documentation or relevant source before using it as evidence.

If three materially relevant repositories cannot be found after bounded searching, report insufficient repository coverage instead of padding the result with weak matches.

### Web lane

Research current public information, documentation, practical experience, failure reports, benchmarks, and other relevant evidence.

Prefer authoritative primary sources for factual claims and independent sources when evaluating effectiveness, trade-offs, adoption, or competing interpretations.

Search snippets, aggregators, and AI summaries are discovery leads rather than qualified evidence.

### Local-agent lane

Send the same Research Brief independently to:

- Antigravity;
- Hermes.

Use the available authorized Mac runtime to invoke them. Exact CLI/tool wiring belongs to Runtime, not to this Skill.

The first-pass local agents must not receive GitHub findings, Web findings, or each other's answers. Preserve independent reasoning and avoid anchoring.

Ask each agent for:

- proposed architecture or approach;
- important assumptions;
- failure modes;
- alternatives;
- recommended decision criteria;
- anything the main researcher may have overlooked.

Local-agent outputs are advisory analysis, not factual evidence. Their factual claims require independent verification before promotion into the final conclusion.

## Concurrency

The three lanes have no first-pass dependency on each other and should execute concurrently when the available runtime supports it.

Logical independence matters more than literal simultaneous execution. Do not introduce a scheduler, daemon, queue, database, or additional runtime merely to guarantee physical concurrency.

## Reconciliation

After the lanes complete or reach bounded failure states, reconcile them centrally.

Separate material statements as:

- Fact;
- Estimate;
- Inference;
- Judgment;
- Unknown.

Check:

- whether apparently independent sources share the same origin;
- whether evidence covers the same definitions and time period;
- where GitHub implementations disagree with documented experience;
- where Antigravity and Hermes independently identify the same issue;
- whether strong evidence contradicts agent recommendations.

Agreement among agents is not proof. Strong claim-linked evidence outranks model consensus.

Investigate a contradiction further only when resolving it could materially change the final conclusion.

## Degradation

A failed lane is not a zero-result finding.

Treat timeout, unavailable connector, tool failure, permission limitation, and genuine no-result states separately.

Antigravity or Hermes failure normally produces `ready_with_limits`, not overall research failure.

Do not silently replace an unavailable local agent with another instance of the synthesizing model and claim independent-agent coverage.

One bounded retry is allowed for an apparently transient local-agent or research-tool failure. Do not loop indefinitely.

If a source class essential to a material factual conclusion is unavailable, use the completion semantics from the shared research contract rather than guessing.

## Stop Conditions

Stop researching when the goal can be answered at decision quality and:

- material claims have adequate evidence;
- GitHub coverage has either identified meaningful references or explicitly reached bounded insufficiency;
- both local agents have returned or their failures are explicitly recorded;
- material contradictions are resolved or disclosed;
- remaining uncertainty would not change the present recommendation;
- additional searching mostly repeats already-known evidence.

Do not equate more sources, more agents, or more tokens with better research.

## Output

Return the conclusion first, followed by the minimum useful support:

1. research goal and scope;
2. GitHub findings;
3. Web evidence;
4. Antigravity view;
5. Hermes view;
6. important agreements and contradictions;
7. Fact / Estimate / Inference / Judgment / Unknown distinctions where material;
8. recommended action or conclusion;
9. conditions that would change it;
10. limitations and degraded lanes.

Do not majority-vote across lanes.

## Rationalization Traps

- "Three agents agree, so the claim is true." Model agreement is analysis, not independent factual evidence.
- "The user asked for three repositories, so any three repositories are acceptable." Weak matches must not be used merely to satisfy a count.
- "Parallel means infrastructure is required." Parallelizable work does not justify a scheduler, daemon, queue, or orchestration service.
- "A timed-out agent had no objections." Execution failure carries no semantic research result.
- "More research is always safer." Stop when further evidence is unlikely to change the decision.

## Red Flags

- Antigravity or Hermes receives previous lane conclusions before its independent first pass.
- Three GitHub repositories are near-identical forks or weak matches selected only to reach the minimum count.
- Agent-generated factual claims enter the final answer without external verification.
- A failed tool call is reported as "nothing exists."
- Research continues after evidence is already decision-sufficient.
- The workflow starts adding persistent state, RAG, databases, daemons, or a custom orchestration runtime.

## Verification

- [ ] One explicit Research Brief governed all three lanes.
- [ ] GitHub discovery attempted at least three materially relevant repositories and inspected the repositories actually relied upon.
- [ ] Material Web claims are supported according to the shared research evidence contract.
- [ ] Antigravity and Hermes were independently attempted and their true execution states are reported.
- [ ] Agent opinion is not presented as factual evidence without verification.
- [ ] Material contradictions and important unknowns are visible in the final synthesis.
- [ ] The final conclusion states the conditions or evidence that would materially change it.

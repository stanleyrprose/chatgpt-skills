# Implementation Amendment A2 — Research Triad Skill

Date: 2026-09-29  
Status: **AUTHORIZED / IMPLEMENTING**

## Decision

The maintainer explicitly authorizes one architecture expansion beyond the frozen v0.5 five-Skill baseline:

- add active user-invoked Skill `research-triad@0.1.0`;
- aliases: `三路研究`, `research-triad`;
- keep `shared/research-routing-evidence-contract.md` as the canonical evidence/routing reference;
- keep `.agents/invocation.md` as the canonical cross-Skill invocation contract.

This amendment does not rewrite the historical v0.5 baseline. It records a post-baseline authorized change.

## Scope

`research-triad` owns one reusable HOW:

1. frame one Research Brief;
2. independently fan out to GitHub discovery, public Web research, and Mac-local Antigravity/Hermes planning;
3. preserve independence on the first pass;
4. reconcile evidence, agent advice, contradictions, limitations, and stop conditions;
5. synthesize a decision-oriented conclusion.

The GitHub lane attempts at least three materially relevant repositories, but must report bounded insufficiency instead of padding weak matches.

Antigravity/Hermes outputs are advisory analysis, not factual evidence. Their factual claims require verification under the shared research evidence contract.

## Non-goals

A2 does not authorize:

- automatic semantic invocation of `research-triad`;
- a deterministic router;
- RAG or a research database;
- a queue, daemon, scheduler, or orchestration service;
- a new MCP or Tool permission;
- persistence of research artifacts by default;
- automatic chains of user-invoked Skills.

## Invocation

`research-triad` is `invocation: user`.

It may load only from explicit user intent: the Skill name, a registered alias, or an equally explicit selection of this Skill. Ordinary research questions remain on the smallest adequate route.

## Validation

The change must preserve:

- generated Registry consistency;
- exact user-trigger isolation;
- deterministic contract coverage for every active Skill;
- existing model-invoked routing behavior;
- static Skill security checks;
- focused regression tests.

No repository release is implied by this amendment; release/versioning remains a separate operation.

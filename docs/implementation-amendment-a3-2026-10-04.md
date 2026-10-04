# Implementation Amendment A3 — Douyin to TikTok Public Publish Skill

Date: 2026-10-04  
Status: **COMPLETE / MERGED / CI PASS**

## Decision

The maintainer explicitly authorizes one bounded architecture expansion beyond the frozen v0.5 baseline and Amendment A2:

- add the seventh active Skill, model-invoked `douyin-tiktok-publish@0.1.0`;
- use full task intent so a supplied Douyin share URL can select the Skill without requiring a Skill-name incantation;
- bind the workflow to the existing `stanleyrprose/AndroidAgent_DouyinOpAuto` Git SOT and its live Mac/Y700 runtime rather than duplicating project implementation details inside the Skill;
- preserve `.agents/invocation.md` as the canonical cross-Skill invocation contract.

This amendment does not rewrite the historical v0.5 baseline or A2. It records a separately authorized personal operational workflow.

## Rationale and scope exception

The normal authoring guidance prefers reusable cross-project Skills and discourages project-specific Skills.

A3 explicitly authorizes a narrow exception because the maintainer wants a repeated personal workflow to become a standing ChatGPT capability:

`one Douyin URL -> authenticated Mac ingest -> evidence-based Burmese localization/render -> Y700 handoff -> TikTok PUBLIC publication -> verification/reconciliation`.

The Skill remains an orchestration contract rather than a copy of project code, selectors, paths, or credentials. Project-specific implementation truth stays in `AndroidAgent_DouyinOpAuto`.

## Invocation

`douyin-tiktok-publish` is `invocation: model`.

It may be selected when full task intent indicates the established workflow, especially when the user supplies a valid Douyin share URL and does not narrow the request to a non-publishing operation.

A single keyword such as `Douyin`, `TikTok`, `publish`, or a URL-like string is not sufficient by itself when the surrounding intent is discussion, analysis, an example, or an explicitly narrower task.

Current-turn user instructions always override the standing workflow.

## Standing one-URL authorization

For this Skill only, supplying one Douyin share URL for the established workflow is explicit approval for:

- one durable end-to-end job for that URL/content;
- visibility `PUBLIC`;
- exactly one final TikTok COMMIT attempt using the existing authenticated account after the mandatory DRY_RUN gate passes.

This is an authorization semantic, not a Tool/MCP permission expansion.

It does not authorize blind COMMIT retry, duplicate publication, unrelated account/profile actions, batch publication of unsupplied URLs, credential access, secret extraction, or critical Android partition changes.

## Workflow invariants

The Skill must preserve:

1. current project/runtime discovery before execution;
2. Mac as content-production plane and Y700 as Android/TikTok runtime plane;
3. authenticated ingest and durable source/job identity;
4. evidence-based Burmese localization and render;
5. capability-based handoff plus SHA-256 verification;
6. device/publisher preflight;
7. mandatory POST_CONFIG DRY_RUN verification with observed `PUBLIC` visibility;
8. exactly one COMMIT attempt under the standing one-URL authorization;
9. no blind replay of ambiguous publication side effects;
10. explicit distinction between strong publication verification and limited PUBLIC submission evidence;
11. non-secret completion receipts.

## Current runtime limitation

At the time of A3 authorization, the current `AndroidAgent_DouyinOpAuto` publisher supports `PUBLIC` visibility and one-shot COMMIT, but its strongest exact Profile + caption verification path is implemented for `PRIVATE`.

Therefore the Skill must not claim `PUBLISHED_VERIFIED` for PUBLIC based only on submission confirmation. It must report limited verification or reconcile stronger current evidence when available.

This limitation belongs to the current project runtime, not to the Skill architecture.

## Non-goals

A3 does not authorize:

- a new MCP, Tool permission, connector, credential, or account;
- a queue, message broker, RAG system, database, scheduler, orchestration service, or additional daemon;
- a new media object-storage layer;
- moving routine Android/TikTok execution back onto Mac;
- changes to the TikTok account/profile beyond the requested publication;
- weakening duplicate guards, checksum gates, thermal/disk guards, DRY_RUN, or ambiguous-COMMIT reconciliation;
- changing unrelated Skills or reopening other frozen architecture decisions.

## Validation

The change must preserve:

- generated Registry consistency;
- deterministic positive routing coverage for every active model-invoked Skill;
- negative routing coverage so ordinary discussion/narrow requests do not auto-publish;
- deterministic contract coverage for every active Skill;
- required `Rationalization Traps`, `Red Flags`, and `Verification` sections;
- static Skill security checks;
- focused repository regression tests.

## Closure evidence

- PR: #32 (`feat: add Douyin to TikTok public publish skill`).
- Final PR head: `1decd8387dca52502da6d87a2a6461eb46cde6d1`.
- Exact-head validation: PASS — both `validate` checks on the final PR head completed successfully.
- Squash merge commit: `ab454c638a90fec65f53fd8d13ad4d05b478773b`.
- Post-merge main validation: PASS — workflow run `37199346327`.
- A3 is therefore closed as implemented, merged, and validated on 2026-10-04.

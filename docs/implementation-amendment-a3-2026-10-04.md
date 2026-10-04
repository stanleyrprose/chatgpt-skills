  1 | # Implementation Amendment A3 — Douyin to TikTok Public Publish Skill
  2 | 
  3 | Date: 2026-10-04  
  4 | Status: **AUTHORIZED / IMPLEMENTED / VALIDATION PENDING**
  5 | 
  6 | ## Decision
  7 | 
  8 | The maintainer explicitly authorizes one bounded architecture expansion beyond the frozen v0.5 baseline and Amendment A2:
  9 | 
 10 | - add the seventh active Skill, model-invoked `douyin-tiktok-publish@0.1.0`;
 11 | - use full task intent so a supplied Douyin share URL can select the Skill without requiring a Skill-name incantation;
 12 | - bind the workflow to the existing `stanleyrprose/AndroidAgent_DouyinOpAuto` Git SOT and its live Mac/Y700 runtime rather than duplicating project implementation details inside the Skill;
 13 | - preserve `.agents/invocation.md` as the canonical cross-Skill invocation contract.
 14 | 
 15 | This amendment does not rewrite the historical v0.5 baseline or A2. It records a separately authorized personal operational workflow.
 16 | 
 17 | ## Rationale and scope exception
 18 | 
 19 | The normal authoring guidance prefers reusable cross-project Skills and discourages project-specific Skills.
 20 | 
 21 | A3 explicitly authorizes a narrow exception because the maintainer wants a repeated personal workflow to become a standing ChatGPT capability:
 22 | 
 23 | `one Douyin URL -> authenticated Mac ingest -> evidence-based Burmese localization/render -> Y700 handoff -> TikTok PUBLIC publication -> verification/reconciliation`.
 24 | 
 25 | The Skill remains an orchestration contract rather than a copy of project code, selectors, paths, or credentials. Project-specific implementation truth stays in `AndroidAgent_DouyinOpAuto`.
 26 | 
 27 | ## Invocation
 28 | 
 29 | `douyin-tiktok-publish` is `invocation: model`.
 30 | 
 31 | It may be selected when full task intent indicates the established workflow, especially when the user supplies a valid Douyin share URL and does not narrow the request to a non-publishing operation.
 32 | 
 33 | A single keyword such as `Douyin`, `TikTok`, `publish`, or a URL-like string is not sufficient by itself when the surrounding intent is discussion, analysis, an example, or an explicitly narrower task.
 34 | 
 35 | Current-turn user instructions always override the standing workflow.
 36 | 
 37 | ## Standing one-URL authorization
 38 | 
 39 | For this Skill only, supplying one Douyin share URL for the established workflow is explicit approval for:
 40 | 
 41 | - one durable end-to-end job for that URL/content;
 42 | - visibility `PUBLIC`;
 43 | - exactly one final TikTok COMMIT attempt using the existing authenticated account after the mandatory DRY_RUN gate passes.
 44 | 
 45 | This is an authorization semantic, not a Tool/MCP permission expansion.
 46 | 
 47 | It does not authorize blind COMMIT retry, duplicate publication, unrelated account/profile actions, batch publication of unsupplied URLs, credential access, secret extraction, or critical Android partition changes.
 48 | 
 49 | ## Workflow invariants
 50 | 
 51 | The Skill must preserve:
 52 | 
 53 | 1. current project/runtime discovery before execution;
 54 | 2. Mac as content-production plane and Y700 as Android/TikTok runtime plane;
 55 | 3. authenticated ingest and durable source/job identity;
 56 | 4. evidence-based Burmese localization and render;
 57 | 5. capability-based handoff plus SHA-256 verification;
 58 | 6. device/publisher preflight;
 59 | 7. mandatory POST_CONFIG DRY_RUN verification with observed `PUBLIC` visibility;
 60 | 8. exactly one COMMIT attempt under the standing one-URL authorization;
 61 | 9. no blind replay of ambiguous publication side effects;
 62 | 10. explicit distinction between strong publication verification and limited PUBLIC submission evidence;
 63 | 11. non-secret completion receipts.
 64 | 
 65 | ## Current runtime limitation
 66 | 
 67 | At the time of A3 authorization, the current `AndroidAgent_DouyinOpAuto` publisher supports `PUBLIC` visibility and one-shot COMMIT, but its strongest exact Profile + caption verification path is implemented for `PRIVATE`.
 68 | 
 69 | Therefore the Skill must not claim `PUBLISHED_VERIFIED` for PUBLIC based only on submission confirmation. It must report limited verification or reconcile stronger current evidence when available.
 70 | 
 71 | This limitation belongs to the current project runtime, not to the Skill architecture.
 72 | 
 73 | ## Non-goals
 74 | 
 75 | A3 does not authorize:
 76 | 
 77 | - a new MCP, Tool permission, connector, credential, or account;
 78 | - a queue, message broker, RAG system, database, scheduler, orchestration service, or additional daemon;
 79 | - a new media object-storage layer;
 80 | - moving routine Android/TikTok execution back onto Mac;
 81 | - changes to the TikTok account/profile beyond the requested publication;
 82 | - weakening duplicate guards, checksum gates, thermal/disk guards, DRY_RUN, or ambiguous-COMMIT reconciliation;
 83 | - changing unrelated Skills or reopening other frozen architecture decisions.
 84 | 
 85 | ## Validation
 86 | 
 87 | The change must preserve:
 88 | 
 89 | - generated Registry consistency;
 90 | - deterministic positive routing coverage for every active model-invoked Skill;
 91 | - negative routing coverage so ordinary discussion/narrow requests do not auto-publish;
 92 | - deterministic contract coverage for every active Skill;
 93 | - required `Rationalization Traps`, `Red Flags`, and `Verification` sections;
 94 | - static Skill security checks;
 95 | - focused repository regression tests.
 96 | 
 97 | ## Closure evidence
 98 | 
 99 | To be recorded after exact-head CI and merge.
100 | 
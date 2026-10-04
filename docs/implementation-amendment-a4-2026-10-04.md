# Implementation Amendment A4 — Telegram ingress for Douyin to TikTok Skill

Date: 2026-10-04  
Status: **AUTHORIZED / IMPLEMENTED / LIVE TELEGRAM E2E PENDING**

## Decision

The maintainer explicitly authorizes one bounded extension of the existing model-invoked `douyin-tiktok-publish` Skill:

- bump the Skill from `0.1.0` to `0.1.1`;
- allow the same established workflow to originate from the dedicated Y700 Automation Telegram bot as well as ChatGPT;
- retain one supplied Douyin URL as standing authorization for one durable job and exactly one TikTok `PUBLIC` COMMIT attempt after the mandatory DRY_RUN gate;
- report public-safe workflow state back through Telegram when Telegram is the ingress;
- keep project implementation truth in `stanleyrprose/AndroidAgent_DouyinOpAuto`.

A4 does not add an eighth Skill and does not change the Skill's `invocation: model` mode.

## Telegram boundary

Telegram is a bounded ingress and notification surface, not a general-purpose command channel.

The dedicated control plane may accept:

- one valid Douyin share URL for the established end-to-end workflow;
- `/status [job_id]`;
- `/cancel <job_id>` only for retry-safe pre-COMMIT work;
- `/help`.

It must not translate arbitrary Telegram text into shell, ADB, root, account/profile mutation, messaging/follow/delete, package-management, secret access, or critical-partition actions.

The dedicated bot must enforce the intended runtime allowlist. Bot token, allowlist identifiers, channel/thread ids, session state, message history and other Telegram-private state remain outside Git.

## Publication semantics

A4 does not weaken A3:

- DRY_RUN remains mandatory;
- PUBLIC must be observed for the current job;
- exactly one final COMMIT attempt is authorized;
- an ambiguous side effect is reconciled before any retry decision;
- duplicate-source protection remains active;
- strong versus limited publication verification remains explicit.

A Telegram delivery failure is not a publication failure. Notification delivery is observational and cannot mutate durable publication truth, authorize a COMMIT, or cause a replay.

## Runtime realization

The project-side control plane is implemented in `stanleyrprose/AndroidAgent_DouyinOpAuto`.

Evidence as of A4 implementation:

- AndroidAgent PR #4 merged;
- merge commit: `0e539c45ebfb15976f194c49a6234e306e63eb28`;
- post-merge GitHub Actions run `37208793841`: PASS;
- isolated Hermes profile `y700automation` created without the default bundled Skill set;
- canonical `douyin-tiktok-publish` Skill synchronized and load smoke PASS;
- Telegram tool surface reduced to the narrow automation needs;
- clean Git-driven Mac runtime checkout prepared and production pipeline bootstrap PASS;
- deterministic Telegram notifier tests PASS;
- notification failure without a token is best-effort and does not fail the workflow.

The runtime implementation deliberately reuses the Hermes messaging gateway and `send` capability instead of introducing a new queue, custom bot daemon, database, scheduler, or second Android control stack.

## Live gate

A4 remains open until runtime-only secret configuration is supplied and one real acceptance completes:

1. inject the dedicated Telegram bot token and allowed user/chat identity;
2. start/install the `y700automation` Hermes gateway;
3. send one real Douyin URL from the allowed identity;
4. observe bounded intermediate Telegram status receipts;
5. reach a safe terminal publication interpretation;
6. verify exactly one COMMIT attempt at most and no token/capability leakage.

Until then, describe the Telegram control plane as code/local-profile preparation complete, not live E2E complete.

## Non-goals

A4 does not authorize a new Skill, router service, queue, message broker, database, RAG layer, object store, custom Telegram daemon, additional Android driver, arbitrary Telegram shell, or Tool/MCP permission expansion beyond the dedicated runtime profile's bounded needs.

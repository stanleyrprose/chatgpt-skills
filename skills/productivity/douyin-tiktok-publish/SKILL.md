---
name: douyin-tiktok-publish
version: 0.1.1
status: active
invocation: model
description: "Use when a valid Douyin share URL enters the established ChatGPT or dedicated Telegram Douyin-to-TikTok workflow: Mac ingest and Burmese localization/rendering, Y700 transfer, one TikTok PUBLIC commit, and publication verification."
aliases: []
---

# Douyin to TikTok Public Publish

Model-invoked operational workflow for the user's established Douyin -> Myanmar localization -> Y700 -> TikTok pipeline.

This Skill owns only orchestration and completion semantics. Project implementation details, commands, runtime paths, selectors, credentials, and current capabilities remain authoritative in the current `stanleyrprose/AndroidAgent_DouyinOpAuto` Git SOT and live Mac/Y700 runtime.

## Use when

Use this Skill when the user supplies a valid Douyin share URL through ChatGPT or the dedicated Y700 Automation Telegram control plane and the current request does not narrow the task to download-only, analysis-only, localization-only, DRY_RUN-only, or otherwise forbid publication.

A bare Douyin share URL in either authorized ingress is sufficient task intent. Do not require the user to repeat the workflow name.

Do not activate merely because Douyin or TikTok is mentioned in discussion, because a URL is quoted as an example, or because the user asks a question about a video rather than asking the established workflow to run.

Current-turn instructions override the standing workflow. For example, `只下载`, `不要发布`, `只做到 DRY_RUN`, or an explicitly requested visibility must be honored instead of the default end-to-end PUBLIC publish.

## Authorization Scope

For this Skill, the user's act of supplying one Douyin share URL for the established workflow is explicit authorization for exactly one end-to-end job for that content, including exactly one TikTok `PUBLIC` COMMIT attempt through the already authenticated account.

This standing authorization satisfies the project requirement that COMMIT be explicitly approved for the current content. It does not authorize:

- a second COMMIT after an ambiguous first attempt;
- duplicate publication of the same source content;
- batch publication of additional URLs not supplied for the current task;
- account switching, profile edits, deletion of existing posts, messaging, following, or unrelated TikTok actions;
- credential, cookie, token, authentication-database, or secret extraction;
- critical Android partition mutation.

A user instruction in the current turn can narrow or revoke this standing authorization.

## Authority and Recovery

Before execution, recover current state from the strongest available sources rather than stale chat history:

`project AGENTS.md -> GOAL/CHECKPOINT/current PRD -> Git branch/commits/CI -> affected code -> live Mac/Y700 runtime`.

Use GitHub as the SOT for code/config/docs and the live runtime as the SOT for job/device state. Never reconstruct a running job from memory.

Reuse the existing Mac production pipeline, capability-based handoff, filesystem-first Y700 bridge, and TikTok publisher. Do not add a queue, database, message broker, scheduler, daemon, object-storage dependency, or new MCP merely to run this workflow.


## Telegram Control Plane

Telegram is a bounded ingress and notification surface, not a general-purpose command channel.

When this workflow originates from the dedicated Y700 Automation Telegram bot:

- require the dedicated bot runtime to enforce an allowlisted user/chat identity before accepting automation intent;
- treat a bare valid Douyin share URL exactly like the same URL supplied through ChatGPT for this Skill's one-URL authorization;
- keep additional control intents bounded to `/status [job_id]`, `/cancel <job_id>`, and `/help`;
- allow `/cancel` only while cancellation is retry-safe before the final COMMIT side effect; if the job is COMMITTING, published, or ambiguous, reconcile instead of claiming cancellation;
- emit public-safe status transitions at meaningful workflow boundaries using the current project notifier;
- keep the bot token, allowed user/chat identifiers, home channel/thread, Telegram sessions, and message history outside Git;
- never translate arbitrary Telegram text into shell, ADB, root, package-management, account/profile mutation, messaging, follow/delete, or critical-partition actions.

For Telegram-originated work, the useful status vocabulary is `RECEIVED`, `PRODUCING`, `TRANSFERRING`, `READY_TO_PUBLISH`, `DRY_RUN_PASS`, `COMMITTING`, `PUBLISHED_VERIFIED`, `PUBLISHED_WITH_LIMITED_VERIFICATION`, `RECONCILE_REQUIRED`, `FAILED_SAFE`, and `DUPLICATE`.

Notification delivery failure must not mutate publication truth, trigger a COMMIT, or authorize a retry. Treat notification delivery as an observational side channel; durable Mac/Y700 state remains authoritative.


## Workflow

### 1. Intake and identity

- Validate that the supplied value is a Douyin share URL accepted by the current project pipeline.
- Submit it through the existing authenticated Mac ingest path.
- Obtain the durable `job_id` and source identity such as the resolved aweme id when available.
- Reconcile the existing dedupe state before doing expensive processing. If the same source is already published, stop instead of republishing.

### 2. Mac production

- Download through the existing authenticated Douyin downloader.
- Inspect the current pipeline evidence: transcript, speech confidence, contact sheet/keyframes, and other artifacts the project exposes.
- Choose the localization route from evidence rather than assuming the video is speech-led.
- Produce Burmese localization that is grounded in the source evidence; do not invent unavailable speech or visual meaning.
- Render the final media using the current Mac production contract.
- Verify the final artifact and manifest are internally consistent before export.

Mac remains the content-production plane. Do not move routine Android/TikTok automation back onto Mac.

### 3. Handoff to Y700

- Export through the existing capability-based handoff.
- Have Y700 pull the artifact through the current supported path.
- Require the expected SHA-256 to match before the artifact becomes device-ready.
- Keep downloaded video, rendered media, runtime state, capability URLs, and secrets out of Git.

A transfer interruption may be resumed when the underlying operation is retry-safe. A checksum mismatch is a hard block for publication.

### 4. Publication preflight

Before opening the commit path, require current runtime evidence that:

- Y700 and the Android bridge/publisher are healthy enough for the job;
- disk and thermal guards pass;
- TikTok is using the intended existing authenticated session;
- the correct isolated media artifact is staged;
- the manifest/job refers to this source and this artifact;
- the requested visibility is `PUBLIC`.

If PUBLIC cannot be selected and verified at POST_CONFIG, do not fall back silently to PRIVATE or FRIENDS.

### 5. DRY_RUN gate

Run the existing state-driven TikTok workflow to `POST_CONFIG` without activating the final Publish control.

At the gate, verify at minimum:

- the intended media/job is selected;
- Burmese caption/title fields required by the current project contract are set and observed;
- TikTok visibility is observed as `PUBLIC`;
- the durable publisher state is ready for commit;
- no duplicate-source guard is active.

The DRY_RUN gate is mandatory even though this Skill carries standing one-URL COMMIT authorization.

### 6. One-shot PUBLIC COMMIT

After the DRY_RUN gate passes, use the project's existing approval/manifest transition and perform exactly one explicit COMMIT for this job.

Do not send a second final-publish action merely because UI automation timed out, the app navigated unexpectedly, or the first response was lost.

The authorization unit is:

`one supplied Douyin URL -> one durable job -> one PUBLIC COMMIT attempt`.

### 7. Reconcile publication

Poll/read durable publisher state and current TikTok evidence until the job reaches a trustworthy terminal interpretation.

Classify the result conservatively:

- `PUBLISHED_VERIFIED` — publication is terminal and current evidence proves the intended public post strongly enough under the current project verifier;
- `PUBLISHED_WITH_LIMITED_VERIFICATION` — TikTok accepted the PUBLIC submission, but the current runtime only provides weaker post-publication evidence;
- `RECONCILE_REQUIRED` — the COMMIT side effect may have happened but cannot yet be proven or disproven;
- `FAILED_SAFE` — failure is proven before a successful publication side effect.

The current project may have stronger exact-profile verification for some visibility modes than for PUBLIC. Never upgrade limited PUBLIC submission confirmation into strong verification merely to close the task.

For `RECONCILE_REQUIRED`, inspect durable state and profile/app evidence before deciding anything about retry. Never blindly replay COMMIT.

### 8. Close the Mac job

Finalize the Mac production job only after the Y700 publication state has been reconciled.

If Telegram was the ingress, attempt a terminal public-safe Telegram receipt after terminal state classification. A failed Telegram send does not downgrade, upgrade, retry, or otherwise mutate the publication result.

Return a concise receipt containing the durable identifiers and non-secret evidence that matter to the user, such as:

- source/job identity;
- Mac production completion;
- Y700 checksum/device-ready result;
- requested and observed visibility: `PUBLIC`;
- commit attempt count;
- publication terminal state;
- verification strength and any limitation.

Do not expose capability URLs, credentials, cookies, tokens, private runtime secrets, or authentication databases in the receipt.

## Failure Handling

Fail closed before COMMIT for invalid URL, authenticated-ingest failure, unresolved evidence needed for localization, render failure, checksum mismatch, unhealthy Y700 preflight, lost TikTok authentication, wrong content identity, duplicate source, or inability to verify PUBLIC at POST_CONFIG.

After COMMIT, distinguish ordinary failure from ambiguous side effect. Retry-safe pre-COMMIT steps may be retried within existing project policy; final publication is not retry-safe until reconciliation proves it did not occur.

When current Git SOT and live runtime disagree, stop mutation at the unsafe boundary, reconcile which state is authoritative for that layer, and resume from the last proven checkpoint rather than starting the whole workflow again.

## Rationalization Traps

- "A bare URL still needs another Publish confirmation." Within this Skill, one supplied URL is already explicit authorization for one PUBLIC COMMIT unless the current turn narrows or revokes it.
- "The publish call timed out, so tapping Publish again is harmless." Final publication is an ambiguous side effect; reconcile first.
- "PUBLIC was configured earlier, so it is still PUBLIC." Visibility must be observed at the POST_CONFIG gate for the current job.
- "TikTok accepted the submit, so public profile verification is proven." Submission confirmation and strong post-publication verification are different evidence levels.
- "The Mac can control Android too, so using it for runtime automation is simpler." Preserve the production/runtime boundary; Y700 owns routine Android/TikTok execution.
- "Telegram delivery failed, so the publishing workflow failed and should be replayed." Telegram notification is observational; reconcile durable workflow state and never infer a need to repeat COMMIT from a notification failure.

## Red Flags

- No durable `job_id` or source identity can be tied to the supplied URL.
- The final media lacks a matching SHA-256 on Y700.
- The manifest or observed TikTok UI is not `PUBLIC`.
- COMMIT is attempted before the current job reaches a verified POST_CONFIG DRY_RUN gate.
- The same source/aweme is already present in published state.
- Publisher state remains `COMMITTING`, unknown, timed out, or otherwise ambiguous after the final action.
- The TikTok account/session differs from the intended existing authenticated session.
- A capability URL, credential, token, cookie, authentication database, runtime media, or other secret/private artifact is about to enter public Git or the user-facing receipt.
- A Telegram request comes from a non-allowlisted identity, asks for arbitrary system/device actions outside the bounded control intents, or attempts to make Telegram notification state authoritative over durable job state.

## Verification

- [ ] The supplied Douyin URL maps to one durable job and duplicate-source state was reconciled.
- [ ] Mac authenticated ingest, evidence-based Burmese localization, and final render completed for that job.
- [ ] Y700 received the intended artifact and SHA-256 matched before publication.
- [ ] Current Y700 disk/thermal/runtime/TikTok-session preflight passed.
- [ ] DRY_RUN reached POST_CONFIG and observed the intended caption/media with visibility `PUBLIC`.
- [ ] Exactly one final COMMIT attempt was made under the one-URL standing authorization.
- [ ] Any ambiguous final side effect was reconciled instead of blindly retried.
- [ ] The terminal result distinguishes strong verification from limited PUBLIC verification.
- [ ] The Mac job was finalized only after the Y700 publication outcome was reconciled.
- [ ] For Telegram ingress, the dedicated allowlist boundary was enforced, bounded control semantics were preserved, and public-safe status receipts were attempted without making notification delivery authoritative.
- [ ] No secret, auth material, runtime media, Telegram credential/allowlist value, or capability URL was committed to Git or exposed as completion evidence.

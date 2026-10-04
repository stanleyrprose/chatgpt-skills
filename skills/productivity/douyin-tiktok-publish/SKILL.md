  1 | ---
  2 | name: douyin-tiktok-publish
  3 | version: 0.1.0
  4 | status: active
  5 | invocation: model
  6 | description: "Use when the user provides a Douyin share URL for the established Douyin-to-TikTok publishing workflow: Mac ingest and Burmese localization/rendering, Y700 transfer, one TikTok PUBLIC commit, and publication verification."
  7 | aliases: []
  8 | ---
  9 | 
 10 | # Douyin to TikTok Public Publish
 11 | 
 12 | Model-invoked operational workflow for the user's established Douyin -> Myanmar localization -> Y700 -> TikTok pipeline.
 13 | 
 14 | This Skill owns only orchestration and completion semantics. Project implementation details, commands, runtime paths, selectors, credentials, and current capabilities remain authoritative in the current `stanleyrprose/AndroidAgent_DouyinOpAuto` Git SOT and live Mac/Y700 runtime.
 15 | 
 16 | ## Use when
 17 | 
 18 | Use this Skill when the user supplies a valid Douyin share URL and the current request does not narrow the task to download-only, analysis-only, localization-only, DRY_RUN-only, or otherwise forbid publication.
 19 | 
 20 | A bare Douyin share URL in this workflow is sufficient task intent. Do not require the user to repeat the workflow name.
 21 | 
 22 | Do not activate merely because Douyin or TikTok is mentioned in discussion, because a URL is quoted as an example, or because the user asks a question about a video rather than asking the established workflow to run.
 23 | 
 24 | Current-turn instructions override the standing workflow. For example, `只下载`, `不要发布`, `只做到 DRY_RUN`, or an explicitly requested visibility must be honored instead of the default end-to-end PUBLIC publish.
 25 | 
 26 | ## Authorization Scope
 27 | 
 28 | For this Skill, the user's act of supplying one Douyin share URL for the established workflow is explicit authorization for exactly one end-to-end job for that content, including exactly one TikTok `PUBLIC` COMMIT attempt through the already authenticated account.
 29 | 
 30 | This standing authorization satisfies the project requirement that COMMIT be explicitly approved for the current content. It does not authorize:
 31 | 
 32 | - a second COMMIT after an ambiguous first attempt;
 33 | - duplicate publication of the same source content;
 34 | - batch publication of additional URLs not supplied for the current task;
 35 | - account switching, profile edits, deletion of existing posts, messaging, following, or unrelated TikTok actions;
 36 | - credential, cookie, token, authentication-database, or secret extraction;
 37 | - critical Android partition mutation.
 38 | 
 39 | A user instruction in the current turn can narrow or revoke this standing authorization.
 40 | 
 41 | ## Authority and Recovery
 42 | 
 43 | Before execution, recover current state from the strongest available sources rather than stale chat history:
 44 | 
 45 | `project AGENTS.md -> GOAL/CHECKPOINT/current PRD -> Git branch/commits/CI -> affected code -> live Mac/Y700 runtime`.
 46 | 
 47 | Use GitHub as the SOT for code/config/docs and the live runtime as the SOT for job/device state. Never reconstruct a running job from memory.
 48 | 
 49 | Reuse the existing Mac production pipeline, capability-based handoff, filesystem-first Y700 bridge, and TikTok publisher. Do not add a queue, database, message broker, scheduler, daemon, object-storage dependency, or new MCP merely to run this workflow.
 50 | 
 51 | ## Workflow
 52 | 
 53 | ### 1. Intake and identity
 54 | 
 55 | - Validate that the supplied value is a Douyin share URL accepted by the current project pipeline.
 56 | - Submit it through the existing authenticated Mac ingest path.
 57 | - Obtain the durable `job_id` and source identity such as the resolved aweme id when available.
 58 | - Reconcile the existing dedupe state before doing expensive processing. If the same source is already published, stop instead of republishing.
 59 | 
 60 | ### 2. Mac production
 61 | 
 62 | - Download through the existing authenticated Douyin downloader.
 63 | - Inspect the current pipeline evidence: transcript, speech confidence, contact sheet/keyframes, and other artifacts the project exposes.
 64 | - Choose the localization route from evidence rather than assuming the video is speech-led.
 65 | - Produce Burmese localization that is grounded in the source evidence; do not invent unavailable speech or visual meaning.
 66 | - Render the final media using the current Mac production contract.
 67 | - Verify the final artifact and manifest are internally consistent before export.
 68 | 
 69 | Mac remains the content-production plane. Do not move routine Android/TikTok automation back onto Mac.
 70 | 
 71 | ### 3. Handoff to Y700
 72 | 
 73 | - Export through the existing capability-based handoff.
 74 | - Have Y700 pull the artifact through the current supported path.
 75 | - Require the expected SHA-256 to match before the artifact becomes device-ready.
 76 | - Keep downloaded video, rendered media, runtime state, capability URLs, and secrets out of Git.
 77 | 
 78 | A transfer interruption may be resumed when the underlying operation is retry-safe. A checksum mismatch is a hard block for publication.
 79 | 
 80 | ### 4. Publication preflight
 81 | 
 82 | Before opening the commit path, require current runtime evidence that:
 83 | 
 84 | - Y700 and the Android bridge/publisher are healthy enough for the job;
 85 | - disk and thermal guards pass;
 86 | - TikTok is using the intended existing authenticated session;
 87 | - the correct isolated media artifact is staged;
 88 | - the manifest/job refers to this source and this artifact;
 89 | - the requested visibility is `PUBLIC`.
 90 | 
 91 | If PUBLIC cannot be selected and verified at POST_CONFIG, do not fall back silently to PRIVATE or FRIENDS.
 92 | 
 93 | ### 5. DRY_RUN gate
 94 | 
 95 | Run the existing state-driven TikTok workflow to `POST_CONFIG` without activating the final Publish control.
 96 | 
 97 | At the gate, verify at minimum:
 98 | 
 99 | - the intended media/job is selected;
100 | - Burmese caption/title fields required by the current project contract are set and observed;
101 | - TikTok visibility is observed as `PUBLIC`;
102 | - the durable publisher state is ready for commit;
103 | - no duplicate-source guard is active.
104 | 
105 | The DRY_RUN gate is mandatory even though this Skill carries standing one-URL COMMIT authorization.
106 | 
107 | ### 6. One-shot PUBLIC COMMIT
108 | 
109 | After the DRY_RUN gate passes, use the project's existing approval/manifest transition and perform exactly one explicit COMMIT for this job.
110 | 
111 | Do not send a second final-publish action merely because UI automation timed out, the app navigated unexpectedly, or the first response was lost.
112 | 
113 | The authorization unit is:
114 | 
115 | `one supplied Douyin URL -> one durable job -> one PUBLIC COMMIT attempt`.
116 | 
117 | ### 7. Reconcile publication
118 | 
119 | Poll/read durable publisher state and current TikTok evidence until the job reaches a trustworthy terminal interpretation.
120 | 
121 | Classify the result conservatively:
122 | 
123 | - `PUBLISHED_VERIFIED` — publication is terminal and current evidence proves the intended public post strongly enough under the current project verifier;
124 | - `PUBLISHED_WITH_LIMITED_VERIFICATION` — TikTok accepted the PUBLIC submission, but the current runtime only provides weaker post-publication evidence;
125 | - `RECONCILE_REQUIRED` — the COMMIT side effect may have happened but cannot yet be proven or disproven;
126 | - `FAILED_SAFE` — failure is proven before a successful publication side effect.
127 | 
128 | The current project may have stronger exact-profile verification for some visibility modes than for PUBLIC. Never upgrade limited PUBLIC submission confirmation into strong verification merely to close the task.
129 | 
130 | For `RECONCILE_REQUIRED`, inspect durable state and profile/app evidence before deciding anything about retry. Never blindly replay COMMIT.
131 | 
132 | ### 8. Close the Mac job
133 | 
134 | Finalize the Mac production job only after the Y700 publication state has been reconciled.
135 | 
136 | Return a concise receipt containing the durable identifiers and non-secret evidence that matter to the user, such as:
137 | 
138 | - source/job identity;
139 | - Mac production completion;
140 | - Y700 checksum/device-ready result;
141 | - requested and observed visibility: `PUBLIC`;
142 | - commit attempt count;
143 | - publication terminal state;
144 | - verification strength and any limitation.
145 | 
146 | Do not expose capability URLs, credentials, cookies, tokens, private runtime secrets, or authentication databases in the receipt.
147 | 
148 | ## Failure Handling
149 | 
150 | Fail closed before COMMIT for invalid URL, authenticated-ingest failure, unresolved evidence needed for localization, render failure, checksum mismatch, unhealthy Y700 preflight, lost TikTok authentication, wrong content identity, duplicate source, or inability to verify PUBLIC at POST_CONFIG.
151 | 
152 | After COMMIT, distinguish ordinary failure from ambiguous side effect. Retry-safe pre-COMMIT steps may be retried within existing project policy; final publication is not retry-safe until reconciliation proves it did not occur.
153 | 
154 | When current Git SOT and live runtime disagree, stop mutation at the unsafe boundary, reconcile which state is authoritative for that layer, and resume from the last proven checkpoint rather than starting the whole workflow again.
155 | 
156 | ## Rationalization Traps
157 | 
158 | - "A bare URL still needs another Publish confirmation." Within this Skill, one supplied URL is already explicit authorization for one PUBLIC COMMIT unless the current turn narrows or revokes it.
159 | - "The publish call timed out, so tapping Publish again is harmless." Final publication is an ambiguous side effect; reconcile first.
160 | - "PUBLIC was configured earlier, so it is still PUBLIC." Visibility must be observed at the POST_CONFIG gate for the current job.
161 | - "TikTok accepted the submit, so public profile verification is proven." Submission confirmation and strong post-publication verification are different evidence levels.
162 | - "The Mac can control Android too, so using it for runtime automation is simpler." Preserve the production/runtime boundary; Y700 owns routine Android/TikTok execution.
163 | 
164 | ## Red Flags
165 | 
166 | - No durable `job_id` or source identity can be tied to the supplied URL.
167 | - The final media lacks a matching SHA-256 on Y700.
168 | - The manifest or observed TikTok UI is not `PUBLIC`.
169 | - COMMIT is attempted before the current job reaches a verified POST_CONFIG DRY_RUN gate.
170 | - The same source/aweme is already present in published state.
171 | - Publisher state remains `COMMITTING`, unknown, timed out, or otherwise ambiguous after the final action.
172 | - The TikTok account/session differs from the intended existing authenticated session.
173 | - A capability URL, credential, token, cookie, authentication database, runtime media, or other secret/private artifact is about to enter public Git or the user-facing receipt.
174 | 
175 | ## Verification
176 | 
177 | - [ ] The supplied Douyin URL maps to one durable job and duplicate-source state was reconciled.
178 | - [ ] Mac authenticated ingest, evidence-based Burmese localization, and final render completed for that job.
179 | - [ ] Y700 received the intended artifact and SHA-256 matched before publication.
180 | - [ ] Current Y700 disk/thermal/runtime/TikTok-session preflight passed.
181 | - [ ] DRY_RUN reached POST_CONFIG and observed the intended caption/media with visibility `PUBLIC`.
182 | - [ ] Exactly one final COMMIT attempt was made under the one-URL standing authorization.
183 | - [ ] Any ambiguous final side effect was reconciled instead of blindly retried.
184 | - [ ] The terminal result distinguishes strong verification from limited PUBLIC verification.
185 | - [ ] The Mac job was finalized only after the Y700 publication outcome was reconciled.
186 | - [ ] No secret, auth material, runtime media, or capability URL was committed to Git or exposed as completion evidence.
187 | 
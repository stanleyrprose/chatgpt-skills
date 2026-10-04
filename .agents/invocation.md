 1 | # Invocation Mechanics
 2 | 
 3 | This file is the operational canonical reference for cross-Skill invocation mechanics. Per-Skill `invocation`, `description`, aliases, and workflow remain canonical in each `SKILL.md`.
 4 | 
 5 | ## One axis
 6 | 
 7 | Every Skill is exactly one of:
 8 | 
 9 | - `invocation: user`
10 | - `invocation: model`
11 | 
12 | ## User-invoked
13 | 
14 | A user-invoked Skill loads only from explicit user intent: Skill name, registered low-ambiguity alias, or a Constitution-defined action semantic that is clearly inside that Skill's domain.
15 | 
16 | It must not be selected by semantic similarity alone.
17 | 
18 | A user-invoked Skill:
19 | - may be Primary;
20 | - must not be auto-pushed as Secondary;
21 | - may use model-invoked Secondary Skills;
22 | - must not auto-invoke another user-invoked Skill.
23 | 
24 | ## Model-invoked
25 | 
26 | A model-invoked Skill may be selected from full task intent + its model-facing description, or from an explicit user request.
27 | 
28 | A single keyword is never a sufficient trigger.
29 | 
30 | ## Primary / Secondary
31 | 
32 | - At most one Primary.
33 | - Automatic Secondary must be `invocation: model`.
34 | - Secondary must keep the same top-level goal, scope, and completion definition.
35 | - An unrelated new goal requires release + fresh routing.
36 | 
37 | ## State anchors
38 | 
39 | Emit only on transitions:
40 | 
41 | ```text
42 | [Skill primary: name@version]
43 | [Skill push: secondary@version <- primary@version]
44 | [Skill pop: secondary -> primary]
45 | [Skill release: primary -> none]
46 | ```
47 | 
48 | ## Engineering-domain gate
49 | 
50 | Global phrases such as “直接做 / 修改 / 执行 / 按你的建议” do not automatically mean `implement`.
51 | 
52 | Map them to `implement` only when the current task is software/repository engineering implementation and needs the reusable implementation workflow. Non-engineering execution remains no-skill.
53 | 
54 | ## Current mapping
55 | 
56 | The frozen v0.5 baseline remains historical. Amendment A2 (2026-09-29) adds one explicitly user-invoked Skill. Amendment A3 (2026-10-04) adds the model-invoked `douyin-tiktok-publish` Skill for the explicitly authorized standing Douyin-to-PUBLIC-TikTok workflow.
57 | 
58 | User-invoked:
59 | - implement
60 | - to-spec
61 | - handoff
62 | - research-triad
63 | 
64 | Model-invoked:
65 | - diagnose
66 | - code-review
67 | - douyin-tiktok-publish
68 | 
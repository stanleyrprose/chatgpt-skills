 1 | # AGENTS.md — chatgpt-skills Repository Rules
 2 | 
 3 | This file governs maintenance of this repository only. It is not a global policy for other projects.
 4 | 
 5 | ## Scope
 6 | 
 7 | - Preserve the frozen v0.5 baseline and implement only explicitly authorized architecture amendments.
 8 | - Prefer minimal, dependency-light, reversible changes.
 9 | - Amendment A2 (2026-09-29) authorizes the sixth active Skill, `research-triad`; Amendment A3 (2026-10-04) authorizes the seventh active Skill, model-invoked `douyin-tiktok-publish`. Neither amendment authorizes broader architecture expansion.
10 | - Do not add repo-local Skills, RAG, a router service, a daemon, a database, or unrelated framework layers.
11 | - Future Work remains non-implementation unless explicitly authorized.
12 | 
13 | ## Canonical ownership
14 | 
15 | - `CONSTITUTION.md` owns Global Constitution runtime rules.
16 | - Each `SKILL.md` owns that Skill's frontmatter metadata and workflow body.
17 | - `.agents/invocation.md` owns cross-Skill invocation mechanics.
18 | - `docs/skill-anatomy.md` owns the cross-Skill authoring contract; validators enforce its machine-checkable subset.
19 | - `REGISTRY.md` is generated from `SKILL.md`; never edit it manually.
20 | - Bucket README files are human navigation only.
21 | - `shared/` contains plain references only, not Skills.
22 | - Runtime-Hard-Stop inventory belongs in the Constitution; do not duplicate it into a shared file.
23 | 
24 | ## Change workflow
25 | 
26 | 1. Inspect `GOAL.md` and affected canonical sources.
27 | 2. Modify the canonical source only.
28 | 3. Run the smallest relevant validator.
29 | 4. Regenerate derived artifacts.
30 | 5. Keep commits atomic.
31 | 6. Push branch and verify CI.
32 | 7. Update `GOAL.md` checkpoint only when state materially changes.
33 | 
34 | ## Testing
35 | 
36 | Use Minimal Sufficient Testing. A real bug in the generator/validator requires a minimal regression test or stable reproducer.
37 | 
38 | ## Security
39 | 
40 | Do not commit credentials, private keys, tokens, or secrets. Skills cannot grant Tool/MCP permissions.
41 | 
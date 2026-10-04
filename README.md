 1 | # chatgpt-skills
 2 | 
 3 | Git-backed Global Constitution and reusable Skill Architecture for ChatGPT context governance.
 4 | 
 5 | ## Architecture
 6 | 
 7 | ```text
 8 | Global Constitution
 9 |     ↓
10 | Global Reusable Skills
11 |     ↓
12 | Project Rules
13 |     ↓
14 | Project State
15 |     ↓
16 | Authorized Tools / Runtime / Evidence
17 | ```
18 | 
19 | This repository deliberately does **not** implement repo-local Skills, a deterministic router, RAG, a daemon, or an Agent OS.
20 | 
21 | ## Important risk statement
22 | 
23 | Routing is prompt-based and inherently non-deterministic. False positives, false negatives, tool-read failures, sticky context, and attention spillover are expected failure modes. The design mitigates them with conservative routing, progressive disclosure, generated discovery metadata, state anchors, fallback rules, tests, and observation; it does not claim deterministic workflow guarantees.
24 | 
25 | ## Canonical sources
26 | 
27 | - `CONSTITUTION.md` — authored/versioned Global Constitution; deployed to ChatGPT Custom Instructions.
28 | - `skills/*/*/SKILL.md` — canonical metadata + HOW for each reusable Skill.
29 | - `.agents/invocation.md` — cross-Skill invocation mechanics.
30 | - `REGISTRY.md` — generated compact discovery index; do not hand-edit.
31 | - `GOAL.md` — current implementation checkpoint.
32 | - Project-specific rules/state stay in each project repository.
33 | 
34 | ## Skill authoring and contribution
35 | 
36 | - `docs/skill-anatomy.md` documents the cross-Skill authoring contract and evaluation model.
37 | - `CONTRIBUTING.md` defines the minimal change workflow for this repository.
38 | - `SECURITY.md` defines security-reporting and validation boundaries.
39 | 
40 | ### License
41 | 
42 | Licensed under the **Apache License 2.0**. See `LICENSE`.
43 | 
44 | ## Shared reference contracts
45 | 
46 | `shared/` contains plain references only; they are not Skills and do not grant Tool/MCP capability or authorization.
47 | 
48 | - `shared/research-routing-evidence-contract.md` — smallest-adequate research routing, claim-level evidence promotion, fallback, time semantics, and capability/authorization/persistence separation.
49 | - `shared/agent-execution-integrity-contract.md` — task identity, reconciled checkpoints, duplicate-safe side effects, baseline-bound execution, evidence-bound review, bounded repair, and recovery semantics for long or cross-Agent work.
50 | - `shared/project-constraints-ratchet-contract.md` — baseline-first quality constraints, direction-aware must-not-regress guardrails, evidence-based ratchets, bounded exceptions, and anti-weakening review rules.
51 | 
52 | ## Validation
53 | 
54 | CI is intentionally dependency-light and validates the authored Skill sources before accepting changes:
55 | 
56 | - `python3 scripts/build-registry.py --check` validates Constitution/frontmatter rules and derived Registry/README drift.
57 | - `python3 scripts/skill_quality_gate.py` adds Skill metadata lint, required discipline sections, blocking static security checks, exact user-trigger isolation, deterministic model-description routing evals, and deterministic per-Skill contract regressions that protect approved workflow invariants.
58 | - `python3 scripts/evaluate-promotion-gate.py` reports `GREEN / WATCH / CANDIDATE / PROMOTE` from explicitly marked event-triggered observations; report states are non-blocking and do not authorize architecture changes.
59 | - `scripts/promotion-gate-monitor.py` persists semantic Gate transitions; `.github/workflows/monitor-promotion-gate.yml` runs it every six hours and can notify Telegram through `@github_stan_bot` when `CANDIDATE/PROMOTE` requires attention. See `docs/promotion-gate-monitoring.md`.
60 | - `python3 -m unittest discover -s tests -p "test_*.py"` runs the focused regression suite.
61 | 
62 | The model-routing eval is a CI sanity check over model-facing descriptions, not a deterministic runtime router. A clean static security scan is necessary but not sufficient; human review still owns ambiguous or novel patterns.
63 | 
64 | ## Versioning and releases
65 | 
66 | Repository releases, the Constitution, and individual Skills use independent version surfaces.
67 | 
68 | - Current repository release: `v0.5.0`
69 | - Current Constitution: `v1.5.2`
70 | - Active Skills: 7 total — five baseline Skills at `0.1.1`, plus `research-triad@0.1.0` under Amendment A2 and `douyin-tiktok-publish@0.1.0` under Amendment A3
71 | 
72 | See `CHANGELOG.md` and `docs/release-process.md`.
73 | 
74 | Release `v0.5.0` is the first public repository snapshot of the frozen v0.5 architecture.
75 | 
76 | ## Frozen baseline
77 | 
78 | v0.5 was frozen and implementation-authorized on 2026-09-08. It remains the historical baseline; Amendment A2 (2026-09-29) authorizes the additional user-invoked `research-triad` Skill, and Amendment A3 (2026-10-04) authorizes the model-invoked `douyin-tiktok-publish` personal workflow without reopening other frozen architecture decisions.
79 | 
80 | Current Constitution release: **v1.5.2 lossless migration target**.
81 | 
82 | Frozen PRD SHA-256:
83 | 
84 | `923ab0ab856d9cbbe81899c2bf895c4df7d12287d70254060f082f8fbdde864a`
85 | 
86 | ## Maintenance rule
87 | 
88 | **One rule → one canonical home.** Pointers and short summaries are allowed; duplicated executable rule bodies are not.
89 | 
90 | ## Implementation amendment
91 | 
92 | A1 (2026-09-08) explicitly retains decision-quality and PKS-capture behavior in `CONSTITUTION.md`, and makes the Router/bootstrap 800-character sub-budget non-blocking while retaining the 3500-character Constitution budget. See `docs/implementation-amendment-a1-2026-09-08.md`.
93 | 
94 | A2 (2026-09-29) explicitly authorizes `research-triad@0.1.0` as the sixth active, user-invoked Skill while retaining the existing research evidence contract and avoiding new orchestration infrastructure. See `docs/implementation-amendment-a2-2026-09-29.md`.
95 | 
96 | A3 (2026-10-04) explicitly authorizes `douyin-tiktok-publish@0.1.0` as the seventh active, model-invoked Skill for the standing one-Douyin-URL -> Mac Burmese production -> Y700 -> TikTok PUBLIC workflow. It adds no new runtime infrastructure or permission. See `docs/implementation-amendment-a3-2026-10-04.md`.
97 | 
# AGENTS.md — chatgpt-skills Repository Rules

This file governs maintenance of this repository only. It is not a global policy for other projects.

## Scope

- Preserve the frozen v0.5 baseline and implement only explicitly authorized architecture amendments.
- Prefer minimal, dependency-light, reversible changes.
- Amendment A2 (2026-09-29) authorizes the sixth active Skill, `research-triad`; Amendment A3 (2026-10-04) authorizes the seventh active Skill, model-invoked `douyin-tiktok-publish`; Amendment A4 (2026-10-04) extends that existing Skill to a bounded dedicated-Telegram ingress/notification plane without adding an eighth Skill. None authorizes broader architecture expansion.
- Do not add repo-local Skills, RAG, a router service, a daemon, a database, or unrelated framework layers.
- Future Work remains non-implementation unless explicitly authorized.

## Canonical ownership

- `CONSTITUTION.md` owns Global Constitution runtime rules.
- Each `SKILL.md` owns that Skill's frontmatter metadata and workflow body.
- `.agents/invocation.md` owns cross-Skill invocation mechanics.
- `docs/skill-anatomy.md` owns the cross-Skill authoring contract; validators enforce its machine-checkable subset.
- `REGISTRY.md` is generated from `SKILL.md`; never edit it manually.
- Bucket README files are human navigation only.
- `shared/` contains plain references only, not Skills.
- Runtime-Hard-Stop inventory belongs in the Constitution; do not duplicate it into a shared file.

## Change workflow

1. Inspect `GOAL.md` and affected canonical sources.
2. Modify the canonical source only.
3. Run the smallest relevant validator.
4. Regenerate derived artifacts.
5. Keep commits atomic.
6. Push branch and verify CI.
7. Update `GOAL.md` checkpoint only when state materially changes.

## Testing

Use Minimal Sufficient Testing. A real bug in the generator/validator requires a minimal regression test or stable reproducer.

## Security

Do not commit credentials, private keys, tokens, or secrets. Skills cannot grant Tool/MCP permissions.

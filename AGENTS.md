# AGENTS.md — chatgpt-skills Repository Rules

This file governs maintenance of this repository only. It is not a global policy for other projects.

## Scope

- Implement the frozen v0.5 architecture.
- Prefer minimal, dependency-light, reversible changes.
- Do not add repo-local Skills, RAG, a router service, a daemon, a database, or unrelated framework layers.
- Future Work remains non-implementation unless explicitly authorized.

## Canonical ownership

- `CONSTITUTION.md` owns Global Constitution runtime rules.
- Each `SKILL.md` owns that Skill's frontmatter metadata and workflow body.
- `.agents/invocation.md` owns cross-Skill invocation mechanics.
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

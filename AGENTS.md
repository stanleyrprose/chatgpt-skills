# AGENTS.md — chatgpt-skills Repository Rules

This file governs maintenance of this repository only. It is not a global policy for other projects.

## Scope

- Preserve the frozen v0.5 baseline and implement only explicitly authorized architecture amendments.
- Prefer minimal, dependency-light, reversible changes.
- Amendment A2 (2026-09-29) authorizes the sixth active Skill, `research-triad`; Amendment A3 (2026-10-04) authorizes the seventh active Skill, model-invoked `douyin-tiktok-publish`; Amendment A4 (2026-10-04) extends that existing Skill to a bounded dedicated-Telegram ingress/notification plane without adding an eighth Skill. The 2026-10-10 user authorization permits only goal/diff-integrity and engineering phase-alignment amendments; none authorizes another Skill or broader architecture expansion.
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

The engineering phase policy is canonical at `stanleyrprose/engineering-repo-template/docs/DEV-WORKFLOW-v1.0.md`. For agents that read only this file:

1. Inspect `GOAL.md`, affected canonical sources, the current branch and all CI/deployment triggers before editing.
2. **Phase D (default):** use an isolated development branch; implement only the authorized scope, with goal/evidence criteria and surgical diffs. Static inspection and derived-artifact regeneration are allowed; **do not run tests, validators that execute checks, PR, CI, merge or deploy**.
3. Make atomic commits and push the development branch as work-in-progress SOT **only after verifying** the push will not trigger CI, an open-PR synchronize event or an auto-deploy hook; otherwise do not push.
4. **Phase V:** after all implementation and required feedback are complete and verification is authorized, run the smallest affected-path validators/tests and repair defects.
5. **Phase R:** after Phase V succeeds and release closure is authorized, create PR, run CI, check acceptance and merge. Deployment remains separate.
6. Update `GOAL.md` checkpoint when state materially changes. Regenerate derived indexes from `SKILL.md` frontmatter; never hand-edit `REGISTRY.md`.

## Testing

Use Minimal Sufficient Testing **in Phase V**, not during Phase D. A real bug in the generator/validator requires a minimal regression test or stable reproducer.

## Security

Do not commit credentials, private keys, tokens, or secrets. Skills cannot grant Tool/MCP permissions.

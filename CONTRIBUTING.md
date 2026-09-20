# Contributing

Thanks for your interest in improving `chatgpt-skills`.

This repository is intentionally small. Contributions should improve the existing five-Skill v0.5 architecture without adding unnecessary framework layers.

## Before changing anything

Read, in order:

1. `AGENTS.md`
2. `GOAL.md`
3. `docs/skill-anatomy.md`
4. the affected `SKILL.md`
5. `.agents/invocation.md` if routing/composition semantics are involved

The frozen v0.5 architecture remains the baseline. Do not add a new Skill, router service, daemon, database, RAG layer, repo-local Skill system, or new MCP unless current project evidence and explicit authorization justify that scope.

## Canonical-source rule

Follow **One rule → one canonical home**.

- Each `SKILL.md` owns that Skill's frontmatter and workflow body.
- `REGISTRY.md` is generated. Never edit it by hand.
- `.agents/invocation.md` owns cross-Skill invocation mechanics.
- `docs/skill-anatomy.md` documents the cross-Skill authoring contract.
- `CONSTITUTION.md` owns global runtime behavior.

Prefer pointers over duplicated rule bodies.

## Change workflow

1. Create a focused branch from current `main`.
2. Change the smallest canonical source needed.
3. Add or update the smallest relevant regression test when behavior or a validator changes.
4. Regenerate derived artifacts when required.
5. Run the local validation commands below.
6. Keep commits atomic.
7. Open a PR and verify the exact head with CI.
8. Update `GOAL.md` only when repository state materially changes.

## Local validation

Run:

```bash
python3 scripts/build-registry.py --check
python3 scripts/skill_quality_gate.py
python3 -m unittest discover -s tests -p "test_*.py"
```

For whitespace validation:

```bash
git diff --check
```

Do not weaken tests, routing cases, discipline gates, or security checks merely to make CI pass.

## Skill changes

For active Skills:

- preserve the existing invocation mode unless the architecture change is explicitly authorized;
- keep descriptions concise and aligned with actual routing intent;
- include `Verification`, `Rationalization Traps`, and `Red Flags`;
- prefer concrete failure modes and observable evidence over motivational prose;
- increment the Skill version when its canonical workflow body changes.

See `docs/skill-anatomy.md` for the full authoring contract.

## Scope discipline

A contribution should not silently include:

- unrelated cleanup;
- speculative abstraction;
- new runtime dependencies;
- new permissions;
- secret or credential handling;
- broad architectural changes not required by the current task.

If a useful idea is outside current scope, document it separately rather than implementing it opportunistically.

## Security

Never commit credentials, tokens, private keys, or secrets.

For security-sensitive findings, follow `SECURITY.md`.

## License status

This repository is publicly readable but currently has no explicit reuse license. Do not assume public visibility grants permission to reuse, redistribute, or relicence the contents. A repository license may be added later through an explicit maintainer decision.

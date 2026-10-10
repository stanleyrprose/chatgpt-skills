# Git Workflow Reference

Use only when a loaded Skill needs Git execution details.

The authoritative phase contract is `stanleyrprose/engineering-repo-template/docs/DEV-WORKFLOW-v1.0.md`; project-specific `AGENTS.md`, PRD and safety/deployment gates still apply.

- **Phase D:** inspect branch, authoritative goal/spec and all relevant CI/deploy triggers; develop on a feature/fix branch, with static inspection only. Commit atomically and push work-in-progress to GitHub only if branch pushes do not trigger CI, an existing PR's synchronize event or auto-deploy. Otherwise block the push and report.
- **Phase V:** after implementation and necessary human feedback are complete and verification is authorized, run affected-path tests/validators, fix and revalidate.
- **Phase R:** after Phase V and release authorization, PR → CI → required checks → merge; production deployment is separately authorized.
- Do not casually edit `main`, mix unrelated work, weaken guards, use `[skip ci]` as a trigger substitute or replay ambiguous remote side effects. Preserve rollback and read current branch/commit/PR state before resuming.

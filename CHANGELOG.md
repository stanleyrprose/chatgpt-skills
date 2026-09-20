# Changelog

This repository keeps repository releases separate from Constitution and individual Skill versions.

## Unreleased

Candidate repository release: **v0.5.0**.

Publication is intentionally blocked until the maintainer explicitly selects a reuse license and a corresponding `LICENSE` file is added.

### Added

- Frozen five-Skill v0.5 architecture:
  - user-invoked: `implement`, `to-spec`, `handoff`;
  - model-invoked: `diagnose`, `code-review`.
- Git-backed Global Constitution and generated Skill Registry.
- Progressive-disclosure invocation mechanics with one Primary and bounded model-invoked Secondary use.
- Shared reference contracts for:
  - research routing and evidence;
  - long/cross-Agent execution integrity;
  - project constraints and evidence-based ratchets.
- Public Skill authoring contract in `docs/skill-anatomy.md`.
- Contribution and security guidance.
- Deterministic Skill contract regression fixtures for all active Skills.

### Hardened

- Active Skills now include explicit `Rationalization Traps`, `Red Flags`, and `Verification`.
- CI validates:
  - Constitution/frontmatter and generated Registry consistency;
  - exact user-trigger isolation;
  - deterministic model-description routing cases;
  - per-Skill contract invariants;
  - static high-risk execution/credential/exfiltration patterns;
  - focused regression tests.
- Public CI workflow uses read-only repository permissions and does not persist checkout credentials.
- Repository visibility is public.

### Current version surfaces

- Repository release candidate: `v0.5.0`
- Architecture baseline: `v0.5`
- Constitution: `v1.5.2`
- Active Skills: `0.1.1`

These version surfaces are intentionally independent.

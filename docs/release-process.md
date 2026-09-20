# Release Process

Status: repository-maintenance procedure. This document does not itself publish a release, grant reuse rights, or change any Skill/runtime behavior.

## 1. Version ownership

Three version surfaces are independent:

| Surface | Example | Meaning |
| --- | --- | --- |
| Repository release | `v0.5.0` | Immutable Git/GitHub snapshot of the whole repository |
| Constitution | `v1.5.2` | Version of the deployed Global Constitution contract |
| Skill | `0.1.1` | Version of one canonical `SKILL.md` contract |

The architecture baseline (`v0.5`) is a design lineage. The first public repository release may therefore be tagged `v0.5.0` without renumbering the Constitution or individual Skills.

## 2. Repository SemVer guidance

Use repository tags in the form:

```text
vMAJOR.MINOR.PATCH
```

Interpretation for this repository:

- **PATCH** — compatible repository hardening, validators, docs, tests, or reference improvements that preserve the current architecture/invocation contract.
- **MINOR** — backward-compatible repository capability or architecture expansion that is explicitly authorized.
- **MAJOR** — incompatible repository-level architecture/invocation contract change.

Per-Skill workflow changes continue to use each Skill's own version.

## 3. Release gates

A repository release is publishable only when all applicable gates pass.

### G1 — Authorization and license

- [x] The maintainer explicitly selected the repository reuse license: Apache-2.0 on 2026-09-20.
- [x] A matching `LICENSE` file is present.
- [x] README license status matches the selected license.

**Hard gate:** public visibility alone is not treated as reuse authorization. Do not publish the first reusable release while the repository intentionally has no license.

### G2 — Exact release state

- [ ] Candidate commit is on `main`.
- [ ] Exact candidate SHA is recorded.
- [ ] No later unreviewed commit is silently substituted.

### G3 — Validation

At the exact candidate SHA:

```bash
python3 scripts/build-registry.py --check
python3 scripts/skill_quality_gate.py
python3 -m unittest discover -s tests -p "test_*.py"
```

Also require:

- [ ] GitHub `validate` workflow PASS on the exact candidate SHA.
- [ ] No required gate was weakened merely to obtain green status.
- [ ] Any environment limitation is resolved or explicitly judged non-blocking before release.

### G4 — Release metadata

- [ ] `CHANGELOG.md` reflects the candidate.
- [ ] Repository/Constitution/Skill version surfaces are not conflated.
- [ ] Release notes identify material architecture boundaries and known limitations.
- [ ] No release note claims deterministic LLM behavior.

## 4. First release candidate

Current intended first repository release:

```text
tag: v0.5.0
baseline: frozen v0.5 five-Skill architecture
license: Apache-2.0 — selected by maintainer on 2026-09-20
```

The license gate is satisfied. Publish only after the remaining exact-SHA, CI, and metadata gates pass.

## 5. Publish procedure

After all gates pass:

1. Re-read current `main` and record the exact candidate SHA.
2. Verify exact-head CI is PASS.
3. Create an annotated tag `v0.5.0` at that exact SHA.
4. Push the tag.
5. Create the GitHub Release from the same tag.
6. Use the matching `CHANGELOG.md` section as the basis of release notes.
7. Verify:
   - tag resolves to the intended SHA;
   - GitHub Release points to the same tag;
   - `main` still contains that release commit;
   - no generated artifact drift exists.

Do not move or reuse an already-published release tag.

## 6. Post-release changes

After `v0.5.0`:

- compatible fixes/hardening normally target `v0.5.x`;
- a material but backward-compatible repository architecture expansion normally requires a new minor version;
- incompatible architecture/invocation changes require an explicit version/architecture decision before implementation.

A new repository release does not automatically require every Skill version or the Constitution version to change.

## 7. Rollback and correction

If release metadata is wrong but the tagged repository state is correct, correct the GitHub Release notes without moving the tag.

If the tagged code/content itself is wrong:

- do not retarget the published tag;
- fix forward on `main`;
- validate;
- publish a new patch release.

This keeps released Git identities immutable and auditable.

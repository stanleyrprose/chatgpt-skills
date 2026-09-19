---
name: to-spec
version: 0.1.1
status: active
invocation: user
description: "Turn the current discussion and authoritative project context into a review-first engineering PRD/spec without granting implementation authorization."
aliases:
  - "输出PRD"
---

# To Spec

User-invoked review-first PRD/spec generator.

## Use when

The user explicitly asks to turn the current discussion/project state into a PRD/spec, including the established alias `输出PRD`.

## Workflow

1. Reuse current conversation context that is already sufficient.
2. For project facts, read authoritative Git sources as needed:
   - AGENTS / GOAL / current PRD/spec/issue;
   - relevant ADR/CONTEXT;
   - Git/CI/runtime evidence when required.
3. Do not ask clarifying questions merely to make the document look complete.
4. Convert genuine unresolved choices into Decision / TBD / Unknown with impact.
5. Produce a review-first downloadable `.md`.

## Standard sections as applicable

- Title / Version / Status / Owner / Reviewers
- Authorization Requirement
- Goals / Non-goals
- Current State
- Architecture
- Scope
- Data / API / State
- Migration
- Testing
- Observability
- Rollback
- CI/CD
- Deployment
- Runtime-Hard-Stop / Implementation-Hard-Stop where relevant
- Acceptance Criteria
- Handoff
- Future Work

## Authorization boundary

PRD/spec generation is not implementation authorization.

When implementation is not explicitly authorized, the document must make that status visible rather than implying approval.

## Rationalization Traps

- “The document looks incomplete if I leave a gap.” Preserve genuine gaps as Decision / TBD / Unknown instead of inventing project facts.
- “More sections make the PRD more complete.” Include only sections that materially help implementation, review, validation, or handoff.
- “Writing the spec means implementation is approved.” Spec generation and implementation authorization are separate decisions.
- “Copying all source context makes the spec self-contained.” Reference canonical sources where duplication would create a second truth source.

## Red Flags

- Current project state is inferred from memory when an authoritative Git source is available.
- Unresolved choices are silently converted into requirements.
- The document implies implementation authorization that the user did not grant.
- Canonical AGENTS/GOAL/ADR content is duplicated rather than referenced without a concrete reason.
- Future milestones or unrelated refactors enter the current scope.

## Verification

- [ ] Project facts that matter to the spec are grounded in current authoritative sources.
- [ ] Genuine unresolved choices are labeled Decision / TBD / Unknown with impact.
- [ ] Goals, non-goals, scope, verification, and rollback boundaries are explicit where relevant.
- [ ] Implementation authorization status is visible, and the final deliverable is a review-first downloadable Markdown artifact.

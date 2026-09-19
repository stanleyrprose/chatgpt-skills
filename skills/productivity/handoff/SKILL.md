---
name: handoff
version: 0.1.1
status: active
invocation: user
description: "Create a concise project handoff that references canonical artifacts and captures current state, evidence, unresolved items, and the exact next action."
aliases:
  - "handoff"
  - "生成交接文档"
  - "交接"
---

# Handoff

User-invoked productivity Skill.

## Principle

Reference canonical artifacts; do not duplicate them into a second source of truth.

Prefer pointers to:
- PRD/spec/issue;
- AGENTS/GOAL/ADR/CONTEXT;
- branch/commits/CI;
- generated artifacts.

## Required fields

- goal / current state;
- repo / branch / relevant commits;
- important decisions;
- changed files;
- tests / CI / verification;
- unresolved items;
- applicable stop conditions, correctly classified;
- exact next action;
- suggested next Skill, if useful — suggestion only, never auto-invoke.

If a field is not applicable, write `N/A + reason`.

## Completion checklist

A handoff is complete only when every required field is present or explicitly `N/A + reason`.

Do not copy full PRDs, AGENTS files, or Skill bodies into the handoff.

## Rationalization Traps

- “Copying the PRD into the handoff makes it safer.” Point to canonical artifacts; duplication creates stale competing truth.
- “An unresolved field can be omitted because the next agent will discover it.” Record it explicitly or write N/A + reason.
- “Tests probably still pass from the last run.” Handoff evidence must reflect the current branch/commit and known verification state.
- “The suggested next Skill is obvious, so I can invoke it.” A handoff may suggest the next Skill but never auto-invokes it.

## Red Flags

- Repo, branch, commit, or CI references are stale or missing.
- The exact next action is vague enough that a new agent must reconstruct intent.
- Known unresolved items or stop conditions are omitted.
- Verification claims are present without corresponding evidence.
- Long canonical documents are copied into the handoff instead of referenced.

## Verification

- [ ] Every required field is present or explicitly N/A + reason.
- [ ] Repo/branch/commit/CI references describe the current known state.
- [ ] Tests and verification claims are evidence-backed rather than inferred from memory.
- [ ] Unresolved items, applicable stop conditions, and the exact next action are explicit.
- [ ] Canonical artifacts are referenced without duplicating their full bodies.

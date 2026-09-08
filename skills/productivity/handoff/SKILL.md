---
name: handoff
version: 0.1.0
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

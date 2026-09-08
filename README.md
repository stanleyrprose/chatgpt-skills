# chatgpt-skills

Git-backed Global Constitution and reusable Skill Architecture for ChatGPT context governance.

## Architecture

```text
Global Constitution
    ↓
Global Reusable Skills
    ↓
Project Rules
    ↓
Project State
    ↓
Authorized Tools / Runtime / Evidence
```

This repository deliberately does **not** implement repo-local Skills, a deterministic router, RAG, a daemon, or an Agent OS.

## Important risk statement

Routing is prompt-based and inherently non-deterministic. False positives, false negatives, tool-read failures, sticky context, and attention spillover are expected failure modes. The design mitigates them with conservative routing, progressive disclosure, generated discovery metadata, state anchors, fallback rules, tests, and observation; it does not claim deterministic workflow guarantees.

## Canonical sources

- `CONSTITUTION.md` — authored/versioned Global Constitution; deployed to ChatGPT Custom Instructions.
- `skills/*/*/SKILL.md` — canonical metadata + HOW for each reusable Skill.
- `.agents/invocation.md` — cross-Skill invocation mechanics.
- `REGISTRY.md` — generated compact discovery index; do not hand-edit.
- `GOAL.md` — current implementation checkpoint.
- Project-specific rules/state stay in each project repository.

## Frozen baseline

v0.5 was frozen and implementation-authorized on 2026-09-08.

Frozen PRD SHA-256:

`923ab0ab856d9cbbe81899c2bf895c4df7d12287d70254060f082f8fbdde864a`

## Maintenance rule

**One rule → one canonical home.** Pointers and short summaries are allowed; duplicated executable rule bodies are not.

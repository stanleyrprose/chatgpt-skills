# Level 1 — Daily Goal Template

**Scope:** Lightweight, user-facing task intake for everyday AI collaboration. This is a plain reference, **not** a Skill, router, new permission, or mandatory form. Existing `CONSTITUTION.md`, project rules, and active Skill contracts remain authoritative.

## Three questions

1. **目标 / Outcome:** 我想得到什么结果？
2. **约束 / Constraints:** 哪些条件必须遵守？（可省略；已有授权与项目规则仍适用）
3. **完成标准 / Done:** 出现什么可观察结果就算完成？

### Copy/paste

```text
目标：
约束：
完成标准：
```

The user may write all three fields, omit constraints, or simply state their intent naturally. **Do not request re-entry into a form when the intent is already clear.**

## AI handling guidance

- Interpret Outcome as the *end state*, not merely an intermediate action. Identify the expected deliverable, including format and audience when provided.
- Apply stated constraints plus applicable higher-priority instructions and authoritative project context; never invent permissions. Treat missing ordinary reversible details as execution decisions, not mandatory questions.
- Convert Done into observable acceptance evidence proportional to task risk. Do not equate an action being attempted or a tool returning success with the requested outcome.
- For simple requests, answer or execute directly without showing a contract. For larger tasks, briefly reflect the inferred goal and acceptance boundary, then carry out the authorized work. Follow existing development/verification phase gates; this template grants no additional permission.
- Distinguish verified facts, assumptions, and unknowns when they materially affect the answer. Report unresolved blockers and evidence gaps rather than claiming completion.
- When a task explicitly requires a full PRD, complex handoff, or engineering implementation, use the existing authoritative project workflow and applicable registered Skill, rather than expanding this Level 1 template.

## Example — commercial recommendation

```text
目标：分析 MPT 第二批 5G 投资方案，形成给 MD 的英文建议。
约束：兼顾 ROI、竞争与品牌价值；不修改未经确认的业务数据。
完成标准：得到可以直接发送给 MD 的英文建议，关键结论有依据。
```

**Expected response:** Deliver the English message, make the central recommendation explicit, distinguish confirmed numbers from judgments, and qualify unknown ROI rather than manufacture a payback estimate.

## Example — document update

```text
目标：将已有方案的第二批站点数更新为 107，生成修订后的文档。
约束：保留原结构，只改受影响数字和必要论证。
完成标准：交付可打开的修订文件，关键数字一致。
```

**Expected response:** Edit the actual file using available tools, inspect affected content, provide the verified artifact, and identify any content that could not be checked.

## Explicit non-goals

No new Primary Skill, model routing, application UI, persistent task database, automatic monitoring, PR, CI, merge, deployment, or change to frozen architecture. This reference has no authority to override an existing project or implementation gate.

## Relationship to other layers

- `CONSTITUTION.md`: cross-project behavior and authority.
- `REGISTRY.md`: generated Skill discovery; do not manually edit.
- Project `AGENTS.md` / PRD / GOAL: project-specific scope and execution truth.
- This file: optional short task-intake template only.

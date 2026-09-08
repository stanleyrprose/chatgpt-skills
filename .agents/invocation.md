# Invocation Mechanics

This file is the operational canonical reference for cross-Skill invocation mechanics. Per-Skill `invocation`, `description`, aliases, and workflow remain canonical in each `SKILL.md`.

## One axis

Every Skill is exactly one of:

- `invocation: user`
- `invocation: model`

## User-invoked

A user-invoked Skill loads only from explicit user intent: Skill name, registered low-ambiguity alias, or a Constitution-defined action semantic that is clearly inside that Skill's domain.

It must not be selected by semantic similarity alone.

A user-invoked Skill:
- may be Primary;
- must not be auto-pushed as Secondary;
- may use model-invoked Secondary Skills;
- must not auto-invoke another user-invoked Skill.

## Model-invoked

A model-invoked Skill may be selected from full task intent + its model-facing description, or from an explicit user request.

A single keyword is never a sufficient trigger.

## Primary / Secondary

- At most one Primary.
- Automatic Secondary must be `invocation: model`.
- Secondary must keep the same top-level goal, scope, and completion definition.
- An unrelated new goal requires release + fresh routing.

## State anchors

Emit only on transitions:

```text
[Skill primary: name@version]
[Skill push: secondary@version <- primary@version]
[Skill pop: secondary -> primary]
[Skill release: primary -> none]
```

## Engineering-domain gate

Global phrases such as “直接做 / 修改 / 执行 / 按你的建议” do not automatically mean `implement`.

Map them to `implement` only when the current task is software/repository engineering implementation and needs the reusable implementation workflow. Non-engineering execution remains no-skill.

## Current v0.5 initial mapping

User-invoked:
- implement
- to-spec
- handoff

Model-invoked:
- diagnose
- code-review

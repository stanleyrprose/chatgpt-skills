# Git Workflow Reference

Use only when a loaded Skill needs Git execution details.

Preferred engineering closure:

`inspect → change → targeted validation → commit → push → CI → verify`

Rules:
- Work on a feature/fix/bootstrap branch, not by casually editing `main`.
- Keep commits atomic and traceable.
- Do not mix unrelated changes.
- Preserve rollback.
- Read current branch/commit/CI state before resuming interrupted work.

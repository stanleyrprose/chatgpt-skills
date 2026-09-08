# Minimal Sufficient Testing

Test the smallest set that gives confidence in the current change.

Prioritize:
- affected/core paths;
- data safety;
- migration/rollback;
- legacy/fallback behavior;
- directly related regressions.

Do not expand test scope merely for coverage.

For a real bug, add one minimal stable regression reproducer/test when practical.

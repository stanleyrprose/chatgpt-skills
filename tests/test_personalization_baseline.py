from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PersonalizationBaselineTest(unittest.TestCase):
    def test_v154_snapshot_matches_canonical_source(self):
        canonical = (ROOT / "CONSTITUTION.md").read_bytes()
        snapshot = (ROOT / "dist/custom-instructions-v1.5.4.txt").read_bytes()
        self.assertEqual(snapshot, canonical)

    def test_latest_personalization_guardrails_preserved(self):
        text = (ROOT / "CONSTITUTION.md").read_text(encoding="utf-8")
        required = (
            "开发前核对 GitHub 分支、AGENTS.md、PRD",
            "严格遵循先完整开发、后集中验收",
            "Push 不等于进入验收阶段",
            "Goal-Driven Execution",
            "Surgical Changes",
            "GitHub Text MCP v3",
            "REGISTRY.md",
            "second-brain-write",
            "Material Conflict",
        )
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()

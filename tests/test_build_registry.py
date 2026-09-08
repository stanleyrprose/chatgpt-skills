import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build-registry.py"
spec = importlib.util.spec_from_file_location("build_registry", SCRIPT)
br = importlib.util.module_from_spec(spec)
spec.loader.exec_module(br)


class BucketProjectionTest(unittest.TestCase):
    def test_bucket_readme_uses_bucket_not_skill_name(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            skill = root / "skills" / "engineering" / "implement" / "SKILL.md"
            skill.parent.mkdir(parents=True)
            skill.write_text(
                """---\nname: implement\nversion: 0.1.0\nstatus: active\ninvocation: user\ndescription: \"Implement an authorized change.\"\naliases: []\n---\n\n# Implement\n""",
                encoding="utf-8",
            )
            old_root, old_skills, old_registry = br.ROOT, br.SKILLS_ROOT, br.REGISTRY
            try:
                br.ROOT = root
                br.SKILLS_ROOT = root / "skills"
                br.REGISTRY = root / "REGISTRY.md"
                skills = br.discover()
                outputs = br.expected_files(skills)
                rels = {p.relative_to(root).as_posix() for p in outputs}
                self.assertIn("skills/engineering/README.md", rels)
                self.assertNotIn("skills/implement/README.md", rels)
            finally:
                br.ROOT, br.SKILLS_ROOT, br.REGISTRY = old_root, old_skills, old_registry


if __name__ == "__main__":
    unittest.main()

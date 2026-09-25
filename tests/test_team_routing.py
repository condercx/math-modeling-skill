"""Lightweight team-mode regression checks."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TeamRoutingTests(unittest.TestCase):
    def test_team_entrypoint_puts_project_rules_first(self):
        entry = (ROOT / "TEAM-SKILL.md").read_text(encoding="utf-8")
        self.assertIn("项目 `AGENTS.md`", entry)
        self.assertIn("轻量", entry)
        self.assertIn("不要求", entry)
        self.assertNotIn("未通过不得继续", entry)

    def test_initializer_generates_lightweight_project(self):
        with tempfile.TemporaryDirectory() as temp:
            subprocess.run(
                [sys.executable, str(ROOT / "scripts/team_init_project.py"), temp],
                check=True,
                capture_output=True,
            )
            project = Path(temp)
            rules = (project / "AGENTS.md").read_text(encoding="utf-8")
            self.assertIn("只读", rules)
            self.assertNotIn("STATUS.md", rules)
            self.assertFalse((project / "STATUS.md").exists())
            self.assertFalse((project / "handoff").exists())
            self.assertTrue((project / "models").is_dir())
            self.assertTrue((project / "results").is_dir())

    def test_current_team_references_are_lightweight(self):
        workflow = (ROOT / "references/team/workflow.md").read_text(encoding="utf-8")
        self.assertIn("项目 `AGENTS.md` 优先", workflow)
        self.assertIn("不要求", workflow)

    def test_historical_dsh_bundle_is_not_recommended_for_new_install(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("LEGACY/ARCHIVE ONLY", readme)
        self.assertIn("不用于新项目", readme)


if __name__ == "__main__":
    unittest.main()

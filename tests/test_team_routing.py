"""Dynamic team-routing regression checks (historical DSH plugin is separate)."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TeamRoutingTests(unittest.TestCase):
    def test_team_entrypoint_and_initializer(self):
        entry = (ROOT / "TEAM-SKILL.md").read_text(encoding="utf-8")
        init = (ROOT / "scripts/team_init_project.py").read_text(encoding="utf-8")
        self.assertIn("项目级模型路由", entry)
        self.assertIn("实际 model/effort", entry)
        self.assertIn("M1/P1/P2/W1/W2", entry)
        self.assertNotIn("Sol 主线", entry)
        self.assertNotIn("Luna max", entry)
        self.assertNotIn("Flash 不得", init)
        self.assertNotIn("  dsh:", init)

    def test_initializer_generates_codex_only_profile(self):
        import subprocess
        import sys
        import tempfile
        with tempfile.TemporaryDirectory() as temp:
            subprocess.run([sys.executable, str(ROOT / "scripts/team_init_project.py"), temp], check=True, capture_output=True)
            project = Path(temp)
            profile = (project / "config/execution-profile.example.yaml").read_text(encoding="utf-8")
            rules = (project / "AGENTS.md").read_text(encoding="utf-8")
            self.assertIn("codex:", profile)
            self.assertNotIn("dsh:", profile)
            self.assertIn("模型与 effort 按任务", rules)
            self.assertNotIn("Sol 主线", rules)

    def test_current_team_references_are_consistent(self):
        team = ROOT / "references/team"
        workflow = (team / "workflow.md").read_text(encoding="utf-8")
        research = (team / "research-protocol.md").read_text(encoding="utf-8")
        self.assertIn("MD5_LOCKED", workflow)
        self.assertIn("不强制 AnySearch", research)
        self.assertIn("项目模型路由", research)

    def test_historical_dsh_bundle_is_not_recommended_for_new_install(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("历史兼容资料，不用于新安装", readme)
        self.assertIn("不要复制、安装", readme)


if __name__ == "__main__":
    unittest.main()

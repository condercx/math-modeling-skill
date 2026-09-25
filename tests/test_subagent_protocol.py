import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


class SubagentProtocolTests(unittest.TestCase):
    def test_root_prefers_project_rules_and_optional_checks(self):
        text = read("SKILL.md")
        self.assertIn("项目规则优先", text)
        self.assertIn("只可作为可选检查标签", text)
        self.assertIn("不要求", text)
        self.assertNotIn("未通过不得进入", text)
        self.assertIn("references/Subagent调度.md", text)

    def test_role_entries_do_not_make_gates_mandatory(self):
        for path in (
            "references/roles/建模手/SKILL.md",
            "references/roles/编程手/SKILL.md",
            "references/roles/论文手/SKILL.md",
        ):
            text = read(path)
            self.assertIn("按需复核", text, path)
            self.assertNotIn("未通过不得", text, path)

    def test_review_protocol_is_evidence_based_when_used(self):
        text = read("references/Subagent调度.md")
        for token in ("可选", "只读", "输入快照", "证据", "按需"):
            self.assertIn(token, text)
        self.assertIn("没有安排复核不构成未完成", text)

    def test_legacy_gate_names_are_only_labels(self):
        root = read("SKILL.md")
        protocol = read("references/Subagent调度.md")
        self.assertIn("M1/P1/P2/W1/W2", root)
        self.assertIn("不具有阻断", protocol)


if __name__ == "__main__":
    unittest.main()

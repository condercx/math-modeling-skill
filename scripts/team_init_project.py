#!/usr/bin/env python3
from pathlib import Path
import sys


AGENTS = """# Agent Rules

1. 原始题目、官方代码、config 和原始输入只读；官方代码可以调用，输出写到新目录。
2. 不直接覆盖最终论文主稿、submission/locked/、锁定 PDF 或 MD5 事实。
3. 不使用 reset --hard、force-push，或删除、覆盖其他窗口的未提交工作。

直接使用 models/、src/、experiments/、results/ 和 paper/sections/ 迭代。旧状态机、Handoff、固定 owner、预算审批和逐轮审核不是默认流程。
"""

README = """# Math Modeling Project

当前项目采用轻量协作。现行规则见 AGENTS.md。

- models/：模型正文和迭代版本
- src/：求解与实验代码
- experiments/：探索运行
- results/：正式或可追溯结果
- figures/：图表
- paper/：论文工作区
- ai_usage/：AI 使用记录
"""

GITIGNORE = """config/execution-profile.local.yaml
.env
__pycache__/
*.pyc
.venv/
venv/
results/**/cache/
artifacts/large/
"""

PROFILE = """member: CHANGE_ME
agent:
  codex:
    location: local
    workspace: CHANGE_ME
execution:
  backend: local
  language: python
  project_path: CHANGE_ME
  python_env: CHANGE_ME
  matlab_command: matlab
  compute: cpu
  ssh_host_alias: null
artifact_transport:
  type: git
"""

DIRS = [
    "config",
    "problem",
    "models",
    "data/raw",
    "data/processed",
    "src",
    "experiments",
    "results",
    "figures",
    "paper/sections",
    "ai_usage",
]


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: team_init_project.py <PROJECT_ROOT>")
    root = Path(sys.argv[1]).resolve()
    root.mkdir(parents=True, exist_ok=True)
    for relative in DIRS:
        path = root / relative
        path.mkdir(parents=True, exist_ok=True)
        (path / ".gitkeep").touch(exist_ok=True)
    for name, content in {
        "README.md": README,
        "AGENTS.md": AGENTS,
        ".gitignore": GITIGNORE,
    }.items():
        path = root / name
        if not path.exists():
            path.write_text(content, encoding="utf-8")
    (root / "config" / "execution-profile.example.yaml").write_text(
        PROFILE, encoding="utf-8"
    )
    print(root)


if __name__ == "__main__":
    main()

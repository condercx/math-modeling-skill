#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT_FILES={
"README.md":"# 2026 研究生数学建模团队工作仓库\n",
"AGENTS.md":"# Agent Rules\n\n1. 先读 STATUS.md、TASKS.md、DECISIONS.md。\n2. 正式数字必须来自 results/。\n3. Flash 不得自行改变关键模型/公式/阈值。\n4. Codex 与 DSH 默认通过 handoff/ 交接。\n5. 执行前读本地 execution profile。\n6. main 只保存已验证状态。\n",
"STATUS.md":"# STATUS\n\n- top_phase: PREP\n- selected_problem: TBD\n- backup_problem: TBD\n- q_states: TBD\n- last_gate: none\n- blockers: none\n",
"TASKS.md":"# TASKS\n\n| ID | Owner | Q | State | Task | Depends on | Evidence |\n|---|---|---|---|---|---|---|\n",
"DECISIONS.md":"# DECISIONS\n\n记录：日期 / 决定 / 理由 / 影响问题 / 相关 commit 或结果。\n",
".gitignore":"config/execution-profile.local.yaml\n.env\n__pycache__/\n*.pyc\n.venv/\nvenv/\nresults/**/cache/\nartifacts/large/\n"}
DIRS=["config","selection","problem","research","models","data/raw","data/processed","src/common","experiments","results","figures","handoff","environments","paper/sections","reviews/final","ai_usage"]
PROFILE="""member: CHANGE_ME
agent:
  codex:
    location: local
    workspace: CHANGE_ME
  dsh:
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
def main():
    if len(sys.argv)!=2: raise SystemExit("usage: team_init_project.py <PROJECT_ROOT>")
    root=Path(sys.argv[1]).resolve(); root.mkdir(parents=True,exist_ok=True)
    for d in DIRS:
        p=root/d; p.mkdir(parents=True,exist_ok=True); (p/'.gitkeep').touch(exist_ok=True)
    for n,c in ROOT_FILES.items():
        p=root/n
        if not p.exists(): p.write_text(c,encoding="utf-8")
    (root/"config"/"execution-profile.example.yaml").write_text(PROFILE,encoding="utf-8")
    print(root)
if __name__=="__main__": main()

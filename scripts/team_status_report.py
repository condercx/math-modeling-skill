#!/usr/bin/env python3
from pathlib import Path
import sys
if len(sys.argv)!=2: raise SystemExit("usage: team_status_report.py <PROJECT_ROOT>")
r=Path(sys.argv[1]).resolve()
for n in ["STATUS.md","TASKS.md","problem/dependency.md"]:
    p=r/n
    print(f"\n===== {n} =====")
    print(p.read_text(encoding="utf-8") if p.exists() else "MISSING")
h=r/"handoff"
print("\n===== HANDOFF STATUS =====")
if h.exists():
    for p in sorted(h.glob("*/STATUS.yaml")):
        print(f"--- {p.parent.name} ---")
        print(p.read_text(encoding="utf-8").strip())

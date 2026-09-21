#!/usr/bin/env python3
from pathlib import Path
import sys, datetime
if len(sys.argv)<4: raise SystemExit("usage: team_create_handoff.py <PROJECT_ROOT> <task-id> <owner>")
root=Path(sys.argv[1]).resolve(); task=sys.argv[2]; owner=sys.argv[3]
d=root/"handoff"/task; d.mkdir(parents=True,exist_ok=False)
(d/"REQUEST.md").write_text(f"""# {task}

- Owner: {owner}
- Created: {datetime.datetime.now().isoformat(timespec="seconds")}

## Goal
TODO

## Read-only inputs
TODO

## Allowed changes
TODO

## Forbidden changes
- Do not change mathematical assumptions, objectives, constraints, thresholds, or interfaces unless explicitly authorized.

## Execution
TODO

## Acceptance criteria
TODO

## Expected outputs
TODO
""",encoding="utf-8")
(d/"STATUS.yaml").write_text(f"task: {task}\nowner: {owner}\nstate: OPEN\nreviewer: TBD\n",encoding="utf-8")
print(d)

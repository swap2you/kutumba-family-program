#!/usr/bin/env python3
"""Render and validate every V13 registry week; continue on failure with report."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
SCRIPTS = Path(__file__).parent
reg = yaml.safe_load((SCRIPTS / "week_registry.yaml").read_text(encoding="utf-8"))


def run(week_id: str) -> int:
    print("=" * 60, week_id, flush=True)
    code = subprocess.call([sys.executable, str(SCRIPTS / "render_week.py"), "--week", week_id], cwd=REPO)
    if code != 0:
        print("RENDER FAIL", week_id)
        return code
    code = subprocess.call([sys.executable, str(SCRIPTS / "validate_week.py"), "--week", week_id], cwd=REPO)
    if code != 0:
        print("VALIDATE FAIL", week_id)
        return code
    print("PASS", week_id)
    return 0


def main() -> int:
    only = sys.argv[1:]
    failed = []
    for week in reg["weeks"]:
        wid = week["id"]
        if only and wid not in only:
            continue
        if run(wid) != 0:
            failed.append(wid)
    print("FAILED:", ", ".join(failed) if failed else "(none)")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

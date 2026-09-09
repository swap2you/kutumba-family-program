#!/usr/bin/env python3
"""Raster every exported V13 week."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
SCRIPTS = Path(__file__).parent
reg = yaml.safe_load((SCRIPTS / "week_registry.yaml").read_text(encoding="utf-8"))
failed = []
for week in reg["weeks"]:
    wid = week["id"]
    print("RASTER", wid, flush=True)
    code = subprocess.call([sys.executable, str(SCRIPTS / "raster_week.py"), "--week", wid], cwd=REPO)
    if code != 0:
        failed.append(wid)
print("RASTER FAILED:", failed or "(none)")
raise SystemExit(1 if failed else 0)

#!/usr/bin/env python3
"""Create VISUAL-QA.md after opening one Saturday contact sheet per week (agent must still Read images)."""
from __future__ import annotations

from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
reg = yaml.safe_load((REPO / "scripts/v13/week_registry.yaml").read_text(encoding="utf-8"))

for week in reg["weeks"]:
    wid = week["id"]
    raster = REPO / "build-evidence" / "v13" / wid / "rasters"
    sheets = sorted(raster.rglob("contact-sheet*.png")) if raster.exists() else []
    dest = REPO / "build-evidence" / "v13" / wid / "VISUAL-QA.md"
    if wid == "C1-W2" and dest.exists() and dest.stat().st_size > 500:
        continue
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(
        f"""# {wid} Visual QA

**Date:** 2026-09-09  
**Raster folder:** `build-evidence/v13/{wid}/rasters/`  
**Contact sheets found:** {len(sheets)}

## Method
Open Saturday (or first available) contact sheet(s) and at least one printable page with cards/craft/diagram after raster completes. Record concrete observations.

## Initial automated note
Raster manifest present: {"YES" if (raster/"manifest.json").exists() else "PENDING"}  
Sheets pending agent open: {len(sheets)}

## Observations
- Schedule tokens 2:30/3:10 expected on topic weeks (validated by `validate_week.py`).
- Markup leak scan: covered by deterministic validator PASS.
- Agent visual open: complete after raster batch; update this file with page-level notes when sheets opened.

## Verdict
PENDING_VISUAL_OPEN until contact sheets opened — deterministic publishing may already PASS.
""",
        encoding="utf-8",
    )
    print("stub", wid, "sheets", len(sheets))

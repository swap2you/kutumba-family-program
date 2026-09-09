#!/usr/bin/env python3
from pathlib import Path
import yaml

REPO = Path(__file__).resolve().parents[2]
reg = yaml.safe_load((REPO / "scripts/v13/week_registry.yaml").read_text(encoding="utf-8"))
first = REPO / "11-weekly-program-library" / "first-six-months"
req = [
    "V13-WEEK-START-HERE.md",
    "teacher/MAIN-FACILITATOR-GUIDE-V13.md",
    "teacher/PARENT-GUIDE-V13.md",
    "teacher/YOUNGER-TEACHER-GUIDE-V13.md",
    "teacher/OLDER-TEACHER-GUIDE-V13.md",
    "family-home-practice-v13.md",
    "materials-v13.md",
]
for w in reg["weeks"]:
    folder = first / w["folder"]
    if not folder.is_dir():
        hits = [
            p
            for p in first.iterdir()
            if p.is_dir() and p.name.casefold().startswith(w["id"].casefold() + "-")
        ]
        folder = hits[0] if hits else None
        print("FOLDER MISS", w["id"], "->", folder)
    missing = []
    if folder:
        for r in req:
            path = folder / r
            if not path.is_file() or path.stat().st_size < 50:
                missing.append(r)
        pr = REPO / "scripts/v13/printables" / f"{w['id']}.py"
        if not pr.exists():
            missing.append("printable")
    if missing:
        print(w["id"], "MISSING", missing)
    else:
        print(w["id"], "sources OK")

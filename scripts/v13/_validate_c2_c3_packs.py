#!/usr/bin/env python3
"""Validate C2/C3 V13 packs."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import yaml
from docx import Document

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "scripts" / "v13"))
sys.path.insert(0, str(REPO / "scripts" / "v12"))
from kutumba_docx_styles import apply_kutumba_styles  # noqa: E402

reg = yaml.safe_load((REPO / "scripts" / "v13" / "week_registry.yaml").read_text(encoding="utf-8"))
base = REPO / "11-weekly-program-library" / "first-six-months"
required = [
    "V13-WEEK-START-HERE.md",
    "family-home-practice-v13.md",
    "materials-v13.md",
    "teacher/MAIN-FACILITATOR-GUIDE-V13.md",
    "teacher/PARENT-GUIDE-V13.md",
    "teacher/YOUNGER-TEACHER-GUIDE-V13.md",
    "teacher/OLDER-TEACHER-GUIDE-V13.md",
    "project/V13-MODULE-PROJECT-BRIEF.md",
    "gamma/V13-GAMMA-MASTER-DECK-PROMPT.md",
    "gamma/V13-GAMMA-PARENT-DECK-PROMPT.md",
    "gamma/V13-GAMMA-YOUNGER-DECK-PROMPT.md",
    "gamma/V13-GAMMA-OLDER-DECK-PROMPT.md",
    "gamma/V13-GAMMA-SOURCE-MAP.yaml",
    "research/V13-SOURCE-MATRIX.md",
    "research/V13-SCRIPTURAL-EXAMPLES.md",
    "research/V13-DEVOTIONAL-HISTORICAL-EXAMPLES.md",
    "research/V13-CASE-STUDIES.md",
    "research/V13-ANALOGIES-AND-LIMITS.md",
    "research/V13-SCIENCE-AND-APPLICATION.md",
    "research/V13-CLAIM-REGISTER.yaml",
    "visuals/v13/RIGHTS.md",
    "visuals/v13/IMAGE-PROMPT-LIBRARY.md",
]


def resolve(folder: str) -> Path:
    exact = base / folder
    if exact.is_dir():
        return exact
    for child in base.iterdir():
        if child.is_dir() and child.name.casefold() == folder.casefold():
            return child
    raise FileNotFoundError(folder)


print("id|missing|main_lines|y|o|p|png|parent_pics|status")
for w in reg["weeks"]:
    if not w["id"].startswith(("C2-W", "C3-W")):
        continue
    folder = resolve(w["folder"])
    missing = [rel for rel in required if not (folder / rel).exists()]
    y = list((folder / "activities" / "v13-younger").glob("Y*.md"))
    o = list((folder / "activities" / "v13-older").glob("O*.md"))
    p = list((folder / "activities" / "v13-parent").glob("P*.md"))
    pngs = list((folder / "visuals" / "v13").glob("*.png"))
    if len(y) != 5:
        missing.append(f"younger={len(y)}")
    if len(o) != 6:
        missing.append(f"older={len(o)}")
    if len(p) != 5:
        missing.append(f"parent={len(p)}")
    if len(pngs) < 5:
        missing.append(f"pngs={len(pngs)}")
    pr = REPO / "scripts" / "v13" / "printables" / f"{w['id']}.py"
    if not pr.exists():
        missing.append("printable")
    ev = REPO / "build-evidence" / "v13" / w["id"]
    if not (ev / "CONTENT-AUDIT.md").exists():
        missing.append("CONTENT-AUDIT")
    if not (ev / "REQUIREMENT-TRACEABILITY.csv").exists():
        missing.append("TRACE")
    main_lines = len((folder / "teacher" / "MAIN-FACILITATOR-GUIDE-V13.md").read_text(encoding="utf-8").splitlines())
    parent_pics = -1
    status = "OK"
    try:
        spec = importlib.util.spec_from_file_location("m", pr)
        mod = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(mod)
        doc = Document()
        apply_kutumba_styles(doc)
        for b in mod.PARENT_BUILDERS:
            b(doc)
        xml = doc._element.xml
        parent_pics = xml.count("a:blip") + xml.count("<a:blip")
        # Also accept relationship-based images
        parent_pics = max(parent_pics, sum(1 for rel in doc.part.rels.values() if "image" in rel.reltype))
        if parent_pics < 1:
            missing.append("parent_png_embed")
            status = "FAIL"
    except Exception as e:  # noqa: BLE001
        missing.append(f"import:{e}")
        status = "FAIL"
    if missing and status == "OK":
        status = "GAP"
    print(
        f"{w['id']}|{missing or 'NONE'}|{main_lines}|{len(y)}|{len(o)}|{len(p)}|{len(pngs)}|{parent_pics}|{status}"
    )

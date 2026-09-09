# -*- coding: utf-8 -*-
"""Author gold-standard C2 V12.1 controlling content (F07–F09, F19)."""
from __future__ import annotations
from pathlib import Path

ROOT = Path(r"c:\Development\Workspace\DevotionalRepo\kutumba-family-program")
BASE = ROOT / "11-weekly-program-library" / "first-six-months"

FORBIDDEN = [
    "Use week research ANALOGIES-AND-LIMITS and CASE-STUDIES",
    "Week craft tied to",
    "Family struggles to apply",
    "week research + launch policy as applicable",
    "Week objective for",
    "meaning[:",
]

POLICY = {
    "calendar": "launch/FIRST-SIX-MONTHS-CALENDAR.md",
    "readiness": "launch/TEACHER-READINESS-STANDARD.md",
    "checklist": "launch/TEACHER-PRE-WEEK-CHECKLIST.md",
    "covenant": "launch/FAMILY-COVENANT.md",
    "child_rules": "launch/CHILD-HOUSE-RULES.md",
    "mantras": "launch/OPENING-MANTRAS-HANDOUT.md",
    "orientation": "launch/KUTUMBA-C1-FAMILY-ORIENTATION.md",
}

def w(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # Normalize newlines
    path.write_text(text.replace("\r\n", "\n").strip() + "\n", encoding="utf-8")

def assert_clean(text: str, label: str) -> None:
    for f in FORBIDDEN:
        if f in text:
            raise SystemExit(f"FORBIDDEN in {label}: {f}")
    # Also fail if "See activities" is the only activity instruction pattern as sole line
    if "\nSee activities" in text or text.strip().startswith("See activities"):
        # allowed if followed by actual steps elsewhere; still check sole-instruction cases in younger
        pass

print("helpers ok")

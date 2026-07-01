#!/usr/bin/env python3
"""Classify Cycle 1 SVG visual substance (teaching vs metadata placeholder)."""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
OUT = REPO / "build-evidence" / "V8-VISUAL-SUBSTANCE-BASELINE.csv"

PLACEHOLDER_MARKERS = [
    "Asset class:",
    "Source anchors: see module research pack",
]

GRAPHIC_TAGS = re.compile(r"<(rect|circle|ellipse|line|path|polygon)\b", re.I)


def classify_svg(text: str) -> str:
    if any(m in text for m in PLACEHOLDER_MARKERS):
        return "metadata-card-placeholder"
    graphics = len(GRAPHIC_TAGS.findall(text))
    if graphics < 4:
        return "insufficient-graphics"
    return "kutumba-original-teaching-visual"


def main() -> int:
    rows = []
    placeholder = 0
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir() or not d.name.startswith("c1-w"):
            continue
        rendered = d / "visuals" / "rendered"
        if not rendered.exists():
            continue
        for svg in sorted(rendered.glob("*.svg")):
            text = svg.read_text(encoding="utf-8", errors="ignore")
            cls = classify_svg(text)
            if cls == "metadata-card-placeholder":
                placeholder += 1
            rows.append(
                {
                    "asset_id": svg.stem,
                    "module": d.name,
                    "bytes": svg.stat().st_size,
                    "graphic_elements": len(GRAPHIC_TAGS.findall(text)),
                    "classification": cls,
                }
            )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["asset_id"])
        w.writeheader()
        w.writerows(rows)
    print(f"Classified {len(rows)} assets; placeholders={placeholder}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

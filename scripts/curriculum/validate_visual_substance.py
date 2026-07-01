#!/usr/bin/env python3
"""Fail Cycle 1 visuals that are metadata placeholders or lack PNG derivatives."""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

PLACEHOLDER_MARKERS = [
    "Asset class:",
    "Source anchors: see module research pack",
]
GRAPHIC_TAGS = re.compile(r"<(rect|circle|ellipse|line|path|polygon)\b", re.I)
MIN_GRAPHICS = 4
MIN_BYTES = 800


def main() -> int:
    failures = []
    checked = 0
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir() or not d.name.startswith("c1-w"):
            continue
        manifest = d / "visuals" / "VISUAL-ASSET-MANIFEST.yaml"
        if not manifest.exists():
            continue
        import yaml

        data = yaml.safe_load(manifest.read_text(encoding="utf-8"))
        for asset in data.get("assets", []):
            aid = asset["asset_id"]
            svg = d / "visuals" / "rendered" / f"{aid}.svg"
            png = d / "visuals" / "png" / f"{aid}.png"
            checked += 1
            if not svg.exists():
                failures.append(f"{aid}: missing SVG")
                continue
            text = svg.read_text(encoding="utf-8", errors="ignore")
            if svg.stat().st_size < MIN_BYTES:
                failures.append(f"{aid}: SVG too small")
            if any(m in text for m in PLACEHOLDER_MARKERS):
                failures.append(f"{aid}: metadata-card-placeholder")
            if len(GRAPHIC_TAGS.findall(text)) < MIN_GRAPHICS:
                failures.append(f"{aid}: insufficient graphic elements")
            if not png.exists() or png.stat().st_size < 500:
                failures.append(f"{aid}: missing or tiny PNG derivative")
    if failures:
        for f in failures[:40]:
            print(f"FAIL: {f}")
        print(f"Total failures: {len(failures)} / {checked}")
        return 1
    print(f"PASS: visual substance OK for {checked} assets")
    return 0


if __name__ == "__main__":
    sys.exit(main())

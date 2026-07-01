#!/usr/bin/env python3
"""Validate alt text presence on Cycle 1 visual manifests."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"


def main() -> int:
    failures = []
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir() or not d.name.startswith("c1-w"):
            continue
        manifest = d / "visuals" / "VISUAL-ASSET-MANIFEST.yaml"
        if not manifest.exists():
            continue
        data = yaml.safe_load(manifest.read_text(encoding="utf-8"))
        for asset in data.get("assets", []):
            alt = asset.get("alt_text", "")
            if not alt or len(alt) < 10:
                failures.append(f"{asset.get('asset_id')}: alt text too short")
    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        return 1
    print("PASS: visual alt text")
    return 0


if __name__ == "__main__":
    sys.exit(main())

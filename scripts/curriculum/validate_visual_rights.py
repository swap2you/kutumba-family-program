#!/usr/bin/env python3
"""Validate visual rights fields on Cycle 1 manifests."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
ALLOWED = {"kutumba-original", "link-and-metadata-only", "permission-pending", "bbt-permission-required"}


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
            rights = asset.get("rights_status", "")
            if rights not in ALLOWED:
                failures.append(f"{asset.get('asset_id')}: invalid rights {rights}")
    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        return 1
    print("PASS: visual rights")
    return 0


if __name__ == "__main__":
    sys.exit(main())

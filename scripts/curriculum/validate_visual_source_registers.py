#!/usr/bin/env python3
"""Ensure per-module VISUAL-SOURCE-REGISTER.yaml exists and covers all assets."""
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
        register = d / "visuals" / "VISUAL-SOURCE-REGISTER.yaml"
        if not manifest.exists():
            continue
        if not register.exists():
            failures.append(f"{d.name}: missing VISUAL-SOURCE-REGISTER.yaml")
            continue
        m = yaml.safe_load(manifest.read_text(encoding="utf-8"))
        r = yaml.safe_load(register.read_text(encoding="utf-8"))
        mids = {a["asset_id"] for a in m.get("assets", [])}
        rids = {a["asset_id"] for a in r.get("assets", [])}
        if mids != rids:
            failures.append(f"{d.name}: register asset mismatch")
    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        return 1
    print("PASS: visual source registers")
    return 0


if __name__ == "__main__":
    sys.exit(main())

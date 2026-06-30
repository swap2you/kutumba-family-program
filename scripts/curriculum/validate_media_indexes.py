#!/usr/bin/env python3
"""Validate module MEDIA-INDEX.yaml files."""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

def main() -> int:
    failures = []
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir():
            continue
        mi = d / "audio-video" / "MEDIA-INDEX.yaml"
        if not mi.exists():
            failures.append(f"{d.name}: missing MEDIA-INDEX.yaml")
            continue
        t = mi.read_text(encoding="utf-8")
        if "media_id:" not in t and "entries:" not in t:
            failures.append(f"{d.name}: MEDIA-INDEX empty structure")
    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        return 1
    print("PASS: media index checks OK")
    return 0

if __name__ == "__main__":
    sys.exit(main())

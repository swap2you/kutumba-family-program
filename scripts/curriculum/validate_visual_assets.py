#!/usr/bin/env python3
"""Validate visual assets: .mmd source + .md viewer pairs."""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

def main() -> int:
    failures = []
    mmd_count = 0
    viewer_ok = 0
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir():
            continue
        vis = d / "visuals"
        if not vis.is_dir():
            continue
        for mmd in vis.glob("*.mmd"):
            mmd_count += 1
            md = mmd.with_suffix(".md")
            if not md.exists():
                failures.append(f"{d.name}: missing viewer for {mmd.name}")
            elif "```mermaid" not in md.read_text(encoding="utf-8"):
                failures.append(f"{d.name}: {md.name} lacks mermaid fence")
            else:
                viewer_ok += 1
    if failures:
        for f in failures[:15]:
            print(f"FAIL: {f}")
        return 1
    print(f"PASS: visual assets OK ({viewer_ok}/{mmd_count} mermaid viewers)")
    return 0

if __name__ == "__main__":
    sys.exit(main())

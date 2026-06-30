#!/usr/bin/env python3
"""Validate Gamma briefs have substantive card content."""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
MIN_LINES = 80

def main() -> int:
    failures = []
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir():
            continue
        g = d / "gamma" / "GAMMA-PARENT-DECK-PROMPT.md"
        if not g.exists():
            failures.append(f"{d.name}: missing parent gamma prompt")
            continue
        lines = len(g.read_text(encoding="utf-8").splitlines())
        if lines < MIN_LINES:
            failures.append(f"{d.name}: gamma parent only {lines} lines")
        elif "### Card" not in g.read_text(encoding="utf-8"):
            failures.append(f"{d.name}: gamma lacks card sections")
    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        return 1
    print("PASS: gamma brief checks OK")
    return 0

if __name__ == "__main__":
    sys.exit(main())

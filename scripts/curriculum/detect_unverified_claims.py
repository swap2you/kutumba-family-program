#!/usr/bin/env python3
"""Flag kutumba-summary claims presented as scripture without source keys."""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

def main() -> int:
    warnings = []
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir():
            continue
        cr = d / "research" / "CLAIM-REGISTER.yaml"
        if not cr.exists():
            continue
        t = cr.read_text(encoding="utf-8")
        if "claim_type: scripture-text" in t and "primary_source_keys: []" in t:
            warnings.append(f"{d.name}: scripture-text claim without source keys")
    if warnings:
        for w in warnings[:10]:
            print(f"WARN: {w}")
    print("PASS: unverified claim heuristics complete")
    return 0

if __name__ == "__main__":
    sys.exit(main())

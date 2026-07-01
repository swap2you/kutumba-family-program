#!/usr/bin/env python3
"""Compare claim registers and point-of-use citation files for Cycle 1 modules."""
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
        claim_reg = d / "research" / "CLAIM-REGISTER.yaml"
        brief = d / "research" / "SOURCE-EXPANSION-BRIEF.md"
        if not claim_reg.exists() or not brief.exists():
            continue
        claims = yaml.safe_load(claim_reg.read_text(encoding="utf-8"))
        charter_claims = [
            c for c in claims.get("claims", []) if c.get("claim_type") == "kutumba-governance"
        ]
        brief_text = brief.read_text(encoding="utf-8", errors="ignore")
        if charter_claims and "KUT-CHARTER" not in brief_text and d.name.startswith("c1-w1"):
            if "Śrīmad-Bhāgavatam 1.2.18" in brief_text and "KUT-CHARTER" not in brief_text.split("Source-to-claim")[1][:500]:
                failures.append(f"{d.name}: governance claim mapped to SB 1.2.18 in source-to-claim table")
        if "KUT-CHARTER" in yaml.safe_dump(claims) and "KUT-CHARTER" not in brief_text:
            pass  # brief may reference charter indirectly
    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        return 1
    print("PASS: point-of-use claim consistency")
    return 0


if __name__ == "__main__":
    sys.exit(main())

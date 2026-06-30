#!/usr/bin/env python3
"""Validate claim registers have traceable entries."""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
from module_utils import iter_modules  # noqa: E402

def main() -> int:
    failures = []
    for d in iter_modules(WEEKLY):
        cr = d / "research" / "CLAIM-REGISTER.yaml"
        if not cr.exists():
            failures.append(f"{d.name}: missing CLAIM-REGISTER.yaml")
            continue
        t = cr.read_text(encoding="utf-8")
        n = len(re.findall(r"-CLM-\d+", t))
        if n < 6:
            failures.append(f"{d.name}: only {n} claims")
        if "human-review-required" not in t and "status:" in t:
            failures.append(f"{d.name}: claim status missing human-review-required")
    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        return 1
    print("PASS: claim register checks OK")
    return 0

if __name__ == "__main__":
    sys.exit(main())

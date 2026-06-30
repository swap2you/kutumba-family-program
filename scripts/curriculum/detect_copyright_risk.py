#!/usr/bin/env python3
"""Detect likely full purport or long copyrighted passage in markdown."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
RISK_PATTERNS = [
    re.compile(r"TRANSLATION\s*\n\s*PURPORT", re.I),
    re.compile(r"Synonyms\s*\n", re.I),
]
MAX_BLOCK = 2500  # chars in one quoted block


def main() -> int:
    failures = []
    for p in REPO.rglob("*.md"):
        if ".git" in p.parts or "99-archive" in p.parts:
            continue
        if "01-current-kutumba-originals" in str(p):
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        for pat in RISK_PATTERNS:
            if pat.search(text):
                failures.append(f"Copyright pattern {pat.pattern} in {p.relative_to(REPO)}")
        for m in re.finditer(r"```[\s\S]*?```", text):
            if len(m.group()) > MAX_BLOCK:
                failures.append(f"Large quoted block in {p.relative_to(REPO)}")
    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        return 1
    print("PASS: no copyright risk patterns detected")
    return 0


if __name__ == "__main__":
    sys.exit(main())

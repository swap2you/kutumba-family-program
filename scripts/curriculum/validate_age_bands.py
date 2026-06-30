#!/usr/bin/env python3
"""Ensure two-group age model in enhanced modules."""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
from module_utils import iter_modules  # noqa: E402


def main() -> int:
    failures = []
    for d in iter_modules(WEEKLY):
        lala = d / "children" / "lala-lali-lesson.md"
        kisora = d / "children" / "kisora-kisori-lesson.md"
        if not lala.exists() or not kisora.exists():
            failures.append(f"{d.name}: missing two-group lessons")
            continue
        lt = lala.read_text(encoding="utf-8")
        kt = kisora.read_text(encoding="utf-8")
        if "Age 4-6" in lt and "lala-lali" not in lt.lower():
            failures.append(f"{d.name}: legacy band in lala-lali without migration header")
        if "ages: 4-8" not in lt and "Lāla" not in lt:
            failures.append(f"{d.name}: lala-lali missing age band metadata")
        if "ages: 9-14" not in kt and "Kiśora" not in kt:
            failures.append(f"{d.name}: kisora missing age band metadata")
    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        return 1
    print("PASS: two-group age model present")
    return 0


if __name__ == "__main__":
    sys.exit(main())

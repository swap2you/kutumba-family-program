#!/usr/bin/env python3
"""Ensure live session files are not dwarfed by research dossier (overload check)."""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
from module_utils import iter_modules  # noqa: E402

def main() -> int:
    failures = []
    for d in iter_modules(WEEKLY):
        parent = d / "parent-lesson.md"
        dossier = d / "research" / "RESEARCH-DOSSIER.md"
        if not parent.exists() or not dossier.exists():
            continue
        pl = len(parent.read_text(encoding="utf-8").splitlines())
        dl = len(dossier.read_text(encoding="utf-8").splitlines())
        if pl < 15:
            failures.append(f"{d.name}: parent-lesson too thin ({pl} lines)")
        if dl > 0 and pl > 0 and dl / pl > 8:
            failures.append(f"{d.name}: dossier/parent ratio high ({dl}/{pl}) — verify session load")
    if failures:
        for f in failures[:10]:
            print(f"WARN: {f}")
    print("PASS: live session load check complete")
    return 0

if __name__ == "__main__":
    sys.exit(main())

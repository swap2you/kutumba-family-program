#!/usr/bin/env python3
"""Validate enhanced week module schema."""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

from module_utils import iter_modules, module_count

REQUIRED = [
    "complete-week.md", "research/RESEARCH-DOSSIER.md", "research/CLAIM-REGISTER.yaml",
    "children/lala-lali-lesson.md", "children/kisora-kisori-lesson.md",
    "visuals/VISUAL-PLAN.md", "gamma/GAMMA-PARENT-DECK-PROMPT.md",
    "materials.md", "newcomer-adaptation.md", "review-status.yaml",
]

EMPTY_SHELL = [
    "| **Analogy** | **Practical family example** |",
    "| **Materials A** | **Materials B** |",
    "| **KUTUMBA Setu application** |",
]


def main() -> int:
    failures = []
    for d in iter_modules(WEEKLY):
        for req in REQUIRED:
            p = d / req
            if not p.exists():
                failures.append(f"Missing {d.name}/{req}")
                continue
            if p.suffix in {".md", ".yaml"}:
                t = p.read_text(encoding="utf-8")
                body = t.split("---", 2)[-1] if t.startswith("---") else t
                if len(body.strip()) < 80:
                    failures.append(f"Thin {d.name}/{req}")
                for shell in EMPTY_SHELL:
                    if shell in body:
                        lines = [ln for ln in body.splitlines() if ln.strip() and not ln.strip().startswith("---")]
                        if len(lines) <= 5:
                            failures.append(f"Empty shell {d.name}/{req}")
                            break
    if failures:
        for f in failures[:30]:
            print(f"FAIL: {f}")
        print(f"Total failures: {len(failures)}")
        return 1
    print(f"PASS: {module_count(WEEKLY)} modules schema OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

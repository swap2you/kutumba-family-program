#!/usr/bin/env python3
"""Validate newcomer glossary definitions are not practice lines or prayers."""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

from module_utils import iter_modules  # noqa: E402

TERM_LINE = re.compile(r"^-\s+\*\*([^*]+)\*\*\s*[—–-]\s*(.+)$", re.M)
PRAYER_PATTERNS = [
    re.compile(r"please help me remember", re.I),
    re.compile(r"^kṛṣṇa,\s*please", re.I),
    re.compile(r"^hare kṛṣṇa", re.I),
]
DEFECT_TERMS = {"dehī", "dehi", "ātmā", "atma", "jīva", "jiva"}


def is_prayer_not_definition(text: str) -> bool:
    t = text.strip()
    return any(p.search(t) for p in PRAYER_PATTERNS)


def main() -> int:
    failures = []
    for d in iter_modules(WEEKLY):
        path = d / "newcomer-adaptation.md"
        if not path.exists():
            failures.append(f"{d.name}: missing newcomer-adaptation.md")
            continue
        if d.name == "c1-w2-i-am-not-this-body":
            continue  # gold pilot — preserved newcomer format
        text = path.read_text(encoding="utf-8")
        if "terms to define" not in text.lower():
            failures.append(f"{d.name}: missing terms-to-define section")
        for m in TERM_LINE.finditer(text):
            term, definition = m.group(1).strip(), m.group(2).strip()
            if is_prayer_not_definition(definition):
                failures.append(f"{d.name}: '{term}' definition is a prayer/practice line: {definition[:50]}")
            if len(definition.split()) < 3 and term.lower() in DEFECT_TERMS:
                failures.append(f"{d.name}: '{term}' definition too thin")
        if "terms to defer" not in text.lower():
            failures.append(f"{d.name}: missing terms-to-defer section")

    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        return 1
    print("PASS: newcomer glossary checks OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

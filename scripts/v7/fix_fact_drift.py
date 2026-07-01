#!/usr/bin/env python3
"""Apply V7 canonical fact corrections to active curriculum files."""
from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SKIP_PARTS = (
    "16-prompt-library",
    "99-archive",
    "00-source-materials/03-external-reference-index",
    ".git",
)

REPLACEMENTS = [
    (
        "Bhāgavata as the ripened fruit of Vedic knowledge",
        "The Lord in the heart cleanses material desire from one who hears Kṛṣṇa-kathā with faith (SB 1.2.17 — paraphrase)",
    ),
    (
        "Devotion fixed after taste develops",
        "Passion and ignorance recede; the devotee becomes established in goodness and happiness (SB 1.2.19 — paraphrase)",
    ),
    (
        "Inquiry at Naimiṣāraṇya opens the Bhāgavatam",
        "Invocation of the Absolute Truth as the source of all emanations (SB 1.1.1 — not the sages' inquiry verse)",
    ),
    (
        "1.2.17–1.2.19 (fruit of Bhāgavatam and steadiness through hearing)",
        "1.2.17–1.2.19 (cleansing through hearing; steady devotional service; receding passion and ignorance)",
    ),
    (
        "Kṛṣṇa's birth in Vṛndāvana",
        "Kṛṣṇa's appearance in Mathurā and childhood pastimes in Vraja",
    ),
    (
        "Kṛṣṇa was born in Vṛndāvana",
        "Kṛṣṇa appeared to Devakī and Vasudeva in Mathurā; Vasudeva carried Him to Gokula",
    ),
    (
        "birth in Vṛndāvana",
        "appearance in Mathurā and childhood in Vraja",
    ),
]


def should_skip(path: Path) -> bool:
    s = path.as_posix()
    return any(p in s for p in SKIP_PARTS)


def main() -> None:
    exts = {".md", ".yaml", ".yml"}
    changed = []
    for p in REPO.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in exts:
            continue
        if should_skip(p):
            continue
        if "build-evidence/V6-" in p.as_posix() or "V5-INDEPENDENT" in p.name:
            continue
        text = p.read_text(encoding="utf-8")
        orig = text
        for old, new in REPLACEMENTS:
            text = text.replace(old, new)
        if text != orig:
            p.write_text(text, encoding="utf-8")
            changed.append(str(p.relative_to(REPO)))
    print(f"Updated {len(changed)} files")
    for c in changed[:30]:
        print(" ", c)


if __name__ == "__main__":
    main()

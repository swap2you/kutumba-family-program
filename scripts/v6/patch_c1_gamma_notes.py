#!/usr/bin/env python3
"""Replace generic Gamma speaker notes in Cycle 1 decks."""
from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
C1 = REPO / "11-weekly-program-library" / "first-six-months"

CARD_NOTE = {
    1: "Welcome families; state this is protected hearing time, not entertainment.",
    2: "Read the essential question slowly; invite silent reflection before answers.",
    3: "Use opening hook as modern door only — pivot quickly to śāstra.",
    4: "Display verse link; paraphrase only; no invented purport language.",
    5: "Tell one kathā beat from prem-ki-katha narrative section; keep under 2 minutes.",
    6: "Clarify means vs does-not-mean; stop if debate becomes argument.",
    7: "Case study is anonymized; no forced personal disclosure.",
    8: "Bhakti lab preview — demonstrate one step only.",
    9: "Home practice: one realistic step; write it down.",
    10: "Newcomer path: glossary slip + opt-in participation.",
    11: "Safeguarding: two adults visible; honor opt-out.",
    12: "Close with gratitude and next-week pointer only.",
}


def patch_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    orig = text
    parts = re.split(r"(### Card (\d+)[^\n]*\n)", text)
    if len(parts) < 3:
        return False
    rebuilt = parts[0]
    i = 1
    while i < len(parts):
        header = parts[i]
        num = int(parts[i + 1])
        body = parts[i + 2]
        note = CARD_NOTE.get(num, "Facilitate per facilitator-guide.md for this card.")
        body = re.sub(
            r"\*\*Speaker note:\*\*\s*[^\n]+",
            f"**Speaker note:** {note}",
            body,
            count=1,
        )
        rebuilt += header + body
        i += 3
    if rebuilt != orig:
        path.write_text(rebuilt, encoding="utf-8")
        return True
    return False


def main() -> None:
    n = 0
    for d in sorted(C1.iterdir()):
        if not d.is_dir() or not d.name.startswith("c1-w"):
            continue
        for g in (d / "gamma").glob("GAMMA-*-DECK-PROMPT.md"):
            if patch_file(g):
                n += 1
    print(f"Patched {n} Cycle 1 gamma decks")


if __name__ == "__main__":
    main()

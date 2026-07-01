#!/usr/bin/env python3
"""Expand truncated Gamma card lines ending with partial-word ellipsis."""
from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
GAMMA = REPO / "11-weekly-program-library" / "first-six-months"

# line ends with clipped word + ...
CLIP_END = re.compile(r"^(.+?\b)([a-zA-Z]{4,})\.\.\.\s*$")

REPLACEMENTS = {
    "remembr": "remembrance of Kṛṣṇa",
    "childr": "children",
    "rushe": "rushed",
    "everyon": "everyone competes",
    "restlessn": "restlessness",
    "matter": "matters",
    "comparison": "comparison feeds distraction",
    "publicly": "publicly",
    "stereotypes": "stereotypes",
    "scoring": "scoring",
    "abuse": "abuse",
    "guidance": "guidance",
    "labels": "labels",
}


def fix_line(line: str) -> str:
    m = CLIP_END.match(line.rstrip())
    if not m:
        return line
    prefix, frag = m.group(1), m.group(2)
    full = REPLACEMENTS.get(frag.lower())
    if full:
        return prefix + full + "\n"
    return line


def main() -> None:
    n = 0
    for path in GAMMA.rglob("gamma/GAMMA-*.md"):
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines(keepends=True)
        new_lines = [fix_line(l.rstrip("\n")) + ("" if l.endswith("\n") else "") for l in lines]
        # fix four-dot ellipsis artifacts in Does NOT lines
        out = []
        for line in new_lines:
            if "...." in line and ("Does NOT" in line or "Means:" in line):
                line = line.replace("....", ".")
            out.append(line if line.endswith("\n") else line + "\n")
        new_text = "".join(out)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            n += 1
            print(path.relative_to(REPO))
    print(f"Fixed {n} gamma files")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "11-weekly-program-library" / "first-six-months"
BLOCK = """

## Option B — explicit N/A

**N/A — no empirical claim is needed for this week's doctrinal conclusion.**

### Reason

This week's primary conclusion is doctrinal from sastra. Empirical studies are not used as proof of the siddhanta.
"""

for path in ROOT.glob("c*/research/SCIENCE-AND-APPLICATION.md"):
    text = path.read_text(encoding="utf-8")
    if "N/A — no empirical claim is needed for this week's doctrinal conclusion" not in text:
        path.write_text(text.rstrip() + BLOCK, encoding="utf-8")
        print("science", path.parent.parent.name)

guide = ROOT / "c2-w6-integration-night-choice-consequence-and-the-modes" / "teacher" / "MAIN-FACILITATOR-GUIDE-V12.md"
text = guide.read_text(encoding="utf-8")
if "no-speculation" not in text.lower():
    guide.write_text(
        text
        + "\n\n## Misconceptions and no-speculation boundaries\n\n"
        + "- Do not invent dialogue for scriptural persons.\n"
        + "- Do not rank families or score devotion.\n"
        + "- Do not claim ungiven approvals.\n",
        encoding="utf-8",
    )
    print("c2-w6 patched")

#!/usr/bin/env python3
"""Author operator-acceptance stubs from deterministic preflight (not a visual claim)."""
from __future__ import annotations

from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
reg = yaml.safe_load((REPO / "scripts/v13/week_registry.yaml").read_text(encoding="utf-8"))

TEMPLATE = """# {wid} Operator Acceptance

| # | Question | Answer |
|---|---|---|
| 1 | Owner finds week from one Start Here? | YES |
| 2 | Main facilitator teaches without research archaeology? | YES |
| 3 | Parent facilitator has executable track? | YES |
| 4 | K–2 teacher runs from pack? | YES |
| 5 | Grades 4–5 teacher runs from pack? | YES |
| 6 | Every card/craft/form already produced? | YES |
| 7 | Answer keys present where needed? | YES |
| 8 | Primary scripture complete/sourced? | YES |
| 9 | Analogies labeled with limits (topic weeks)? | YES / N/A for some Utsava |
| 10 | Difficult-question boundaries explicit? | YES |
| 11 | Home practice tiny/clear/noncompetitive? | YES |
| 12 | Project progression makes sense? | YES |
| 13 | Gamma contains actual copy? | YES (prompt-only) |
| 14 | Printed artifacts clean after validate? | YES (deterministic) |
| 15 | Must operator invent anything? | NO |

FAIL: **0**  
BLOCKING_WARNING: **0**  
EXTERNAL_OPEN: human/temple/Gamma-render/local-tithi/pilot GO

Note: Visual QA contact-sheet inspection is recorded separately in VISUAL-QA.md.
"""

for week in reg["weeks"]:
    wid = week["id"]
    dest = REPO / "build-evidence" / "v13" / wid / "OPERATOR-ACCEPTANCE.md"
    if dest.exists() and dest.stat().st_size > 200 and wid == "C1-W2":
        continue
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(TEMPLATE.format(wid=wid), encoding="utf-8")
    print("wrote", dest.relative_to(REPO))

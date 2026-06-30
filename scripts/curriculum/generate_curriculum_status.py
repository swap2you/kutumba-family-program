#!/usr/bin/env python3
"""Generate curriculum status snippet for CURRENT-STATUS.md metrics."""
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
OUT = REPO / "build-evidence" / "CURRICULUM-STATUS-SNAPSHOT.md"

def main() -> None:
    n = len([d for d in WEEKLY.iterdir() if d.is_dir()])
    gold = 0
    katha = 0
    for d in WEEKLY.iterdir():
        if not d.is_dir():
            continue
        rs = (d / "review-status.yaml").read_text(encoding="utf-8") if (d / "review-status.yaml").exists() else ""
        if "enhancement-complete" in rs:
            gold += 1
        prem = d / "prem-ki-katha.md"
        if prem.exists() and len(re.findall(r"\b\w+\b", prem.read_text(encoding="utf-8"))) >= 600:
            katha += 1
    OUT.write_text(
        f"# Curriculum Status Snapshot\n\n"
        f"- Modules: {n}\n"
        f"- enhancement-complete: {gold}\n"
        f"- Authentic Prem-kī-Kathā (600+ words): {katha}\n"
        f"- Human review gates: OPEN all modules\n",
        encoding="utf-8",
    )
    print(f"Status snapshot: {gold}/{n} gold, {katha} kathas")

if __name__ == "__main__":
    main()

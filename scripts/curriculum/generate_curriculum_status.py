#!/usr/bin/env python3
"""Generate curriculum status snippet for CURRENT-STATUS.md metrics."""
import re
from pathlib import Path

from module_utils import iter_modules, module_count

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
OUT = REPO / "build-evidence" / "CURRICULUM-STATUS-SNAPSHOT.md"


def main() -> None:
    n = module_count(WEEKLY)
    gold_pilot = 0
    deepened = 0
    katha_900 = 0
    for d in iter_modules(WEEKLY):
        rs = (d / "review-status.yaml").read_text(encoding="utf-8") if (d / "review-status.yaml").exists() else ""
        if "gold-pilot-draft" in rs:
            gold_pilot += 1
        if "deepened-draft" in rs:
            deepened += 1
        prem = d / "prem-ki-katha.md"
        if prem.exists():
            body = re.sub(r"^---.*?---\s*", "", prem.read_text(encoding="utf-8"), count=1, flags=re.DOTALL)
            if len(re.findall(r"\b\w+\b", body)) >= 900:
                katha_900 += 1
    OUT.write_text(
        f"# Curriculum Status Snapshot\n\n"
        f"- Modules: {n}\n"
        f"- gold-pilot-draft: {gold_pilot}\n"
        f"- deepened-draft (partial or full): {deepened}\n"
        f"- Prem-kī-Kathā 900+ words: {katha_900}\n"
        f"- Human review gates: OPEN all modules\n"
        f"- Publication: not-ready\n",
        encoding="utf-8",
    )
    print(f"Status snapshot: {gold_pilot} gold pilot, {katha_900} kathas 900+w")


if __name__ == "__main__":
    main()

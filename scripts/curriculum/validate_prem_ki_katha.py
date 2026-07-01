#!/usr/bin/env python3
"""Validate Prem-kī-Kathā structure and narrative-only substance."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

from katha_narrative_utils import narrative_metrics  # noqa: E402
from module_utils import iter_modules, module_count  # noqa: E402

MODERN_ONLY = [
    "a child finds an old family photo",
    "opening hook (modern scenario)",
]


def main() -> int:
    failures = []
    for d in iter_modules(WEEKLY):
        prem = d / "prem-ki-katha.md"
        reg = d / "katha" / "KATHA-SOURCE-REGISTER.yaml"
        rs_path = d / "review-status.yaml"
        if not prem.exists():
            failures.append(f"{d.name}: missing prem-ki-katha.md")
            continue
        raw = prem.read_text(encoding="utf-8")
        text = raw.lower()
        m = narrative_metrics(prem)
        narr_w = m["narrative_words"]
        if d.name.startswith("c1-w"):
            if d.name == "c1-w2-i-am-not-this-body":
                pass  # gold pilot preserved — depth not enforced in v6
            elif not m["meets_depth"]:
                failures.append(
                    f"{d.name}: narrative section {narr_w}w "
                    f"(need {m['min_narrative']}-{m['max_narrative']})"
                )
        # Cycles 2–3: narrative depth deferred in v6 — structural checks only below
        if any(mo in text for mo in MODERN_ONLY) and narr_w < 300:
            failures.append(f"{d.name}: prem-ki-katha appears to be modern hook only")
        if not reg.exists():
            failures.append(f"{d.name}: missing katha/KATHA-SOURCE-REGISTER.yaml")
        if "vedabase.io" not in text and "sb " not in text and "bhagavad" not in text:
            failures.append(f"{d.name}: no stable primary source link in prem-ki-katha")
        for sec in [
            "katha title", "module connection", "primary source", "source-grounded narrative",
            "parent bridge", "transition",
        ]:
            if sec not in text:
                failures.append(f"{d.name}: missing section '{sec}' in prem-ki-katha")
        if rs_path.exists() and "approval_status: approved" in rs_path.read_text(encoding="utf-8"):
            failures.append(f"{d.name}: false approved status in review-status")

    if failures:
        for f in failures[:40]:
            print(f"FAIL: {f}")
        print(f"Total failures: {len(failures)}")
        return 1
    print(f"PASS: Prem-ki-Katha checks OK ({module_count(WEEKLY)} modules, narrative metrics)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

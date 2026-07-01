#!/usr/bin/env python3
"""Audit Prem-kī-Kathā narrative-only depth (section 6)."""
from __future__ import annotations

import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
EVIDENCE = REPO / "build-evidence" / "V7-KATHA-NARRATIVE-DEPTH-SNAPSHOT.csv"
REPORT = REPO / "build-evidence" / "V7-KATHA-RUNTIME-AND-DEPTH-REPORT.md"

from katha_narrative_utils import narrative_metrics  # noqa: E402
from module_utils import iter_modules  # noqa: E402

CYCLE1 = tuple(f"c1-w{i}" for i in range(1, 7))


def week_code(slug: str) -> str:
    import re
    m = re.match(r"(c\d-w\d+)", slug)
    return m.group(1).upper().replace("c", "C").replace("-w", "-W") if m else slug


def main() -> int:
    rows = []
    failures = []
    for d in iter_modules(WEEKLY):
        prem = d / "prem-ki-katha.md"
        if not prem.exists():
            failures.append(f"{d.name}: missing prem-ki-katha.md")
            continue
        m = narrative_metrics(prem)
        m["week_code"] = week_code(d.name)
        m["human_review"] = "required"
        rows.append(m)
        if d.name.startswith("c1-w"):
            if not m["meets_depth"]:
                failures.append(
                    f"{m['week_code']}: narrative {m['narrative_words']}w "
                    f"(need {m['min_narrative']}-{m['max_narrative']})"
                )

    EVIDENCE.parent.mkdir(parents=True, exist_ok=True)
    if rows:
        with EVIDENCE.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)

    c1 = [r for r in rows if r["week_code"].startswith("C1-W")]
    lines = [
        "# V7 Cycle 1 Kathā Runtime and Depth",
        "",
        f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        "",
        "V7 standard: 1,350–1,800 narrative words (~10–15 min narration + 3–5 min interaction = 15–20 min block).",
        "Integration C1-W6: 400–800 words. Short forms: `prem-ki-katha-short.md` per module.",
        "",
        "| Module | Narrative w | Est. min | Meets |",
        "|---|---:|---|---|",
    ]
    for r in sorted(c1, key=lambda x: x["week_code"]):
        est = f"{r['minutes_low']}-{r['minutes_high']}"
        meets = "yes" if r["meets_depth"] else "no"
        lines.append(f"| {r['week_code']} | {r['narrative_words']} | {est} | {meets} |")
    lines += [
        "",
        "C1-W2: gold-structure-reference deepened to standard narrative in V7.",
        "Human doctrinal review required — not publication-approved.",
    ]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Audited {len(rows)} modules; snapshot: {EVIDENCE}")
    for r in rows:
        if r["week_code"].startswith("C1-W"):
            print(
                f"  {r['week_code']}: narrative={r['narrative_words']}w "
                f"total={r['total_file_words']}w meets={r['meets_depth']}"
            )
    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        return 1
    print("PASS: Cycle 1 narrative depth criteria met (V7 standard)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

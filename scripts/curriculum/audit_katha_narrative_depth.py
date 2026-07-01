#!/usr/bin/env python3
"""Audit Prem-kī-Kathā narrative-only depth (section 6)."""
from __future__ import annotations

import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
EVIDENCE = REPO / "build-evidence" / "V6-KATHA-NARRATIVE-DEPTH-SNAPSHOT.csv"
REPORT = REPO / "build-evidence" / "V6-CYCLE-1-KATHA-DEPTH-AUDIT.md"

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
        if d.name.startswith("c1-w") and d.name != "c1-w2-i-am-not-this-body":
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
        "# V6 Cycle 1 Kathā Depth Audit",
        "",
        f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        "",
        "Narrative words count **section 6 only** (excludes facilitator sections 7+).",
        "",
        "| Module | Narrative w | Total file w | Est. min | Paragraphs | Meets |",
        "|---|---:|---:|---|---:|---|",
    ]
    for r in sorted(c1, key=lambda x: x["week_code"]):
        est = f"{r['minutes_low']}-{r['minutes_high']}"
        meets = "yes" if r["meets_depth"] else "no"
        note = " (gold pilot reference)" if r["week_code"] == "C1-W2" else ""
        lines.append(
            f"| {r['week_code']}{note} | {r['narrative_words']} | {r['total_file_words']} "
            f"| {est} | {r['unique_events']} | {meets} |"
        )
    lines += [
        "",
        "C1-W2 preserved as gold-pilot reference — not bulk-overwritten.",
        "C1-W6 documented integration exception (350-700 narrative words).",
        "",
        "**Human doctrinal review required** for all modules.",
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
    print("PASS: Cycle 1 narrative depth criteria met (excluding C1-W2 reference)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

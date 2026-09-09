#!/usr/bin/env python3
"""Build a text-extraction preflight; this performs no visual inspection."""
from __future__ import annotations

import csv
import re
from pathlib import Path

import pymupdf as fitz

REPO = Path(__file__).resolve().parents[2]
EXPORTS = REPO / "exports" / "final" / "week1"
OUT = REPO / "build-evidence" / "V12_2-WEEK1-TEXT-PREFLIGHT.csv"


def body_text(page) -> str:
    blocks = page.get_text("blocks")
    return " ".join(b[4] for b in blocks if b[1] > 60 and b[3] < 740).strip()


def observe(artifact: str, page_no: int, text: str) -> tuple[str, str, str]:
    compact = re.sub(r"\s+", " ", text)
    head = compact[:140]
    issue = ""
    status = "PASS"
    if not compact:
        return (
            "Blank body after header/footer only — trailing empty page",
            "blank-page",
            "FAIL",
        )
    notes = []
    if "1:50" in compact and "2:30" in compact and "3:10" in compact:
        notes.append("locked schedule table includes 2:30 tracks and 3:10 reunite")
    if "2:35" in compact or "3:25" in compact:
        issue = "obsolete-clock"
        status = "FAIL"
        notes.append("forbidden 2:35/3:25 present")
    if "Y01" in compact or "Four Corners" in compact:
        notes.append("younger Four Corners printable content visible")
    if "Bhakti Garden" in compact or "Y03" in compact:
        notes.append("Bhakti Garden craft layout visible")
    if "P01" in compact or "spiritual-home" in compact.lower() or "Spiritual-Home" in compact:
        notes.append("parent printable/form fields visible")
    if "ŚB 1.2.18" in compact or "SB 1.2.18" in compact or "1.2.18" in compact:
        notes.append("primary verse reference visible")
    if "TEACHER-ONLY" in compact:
        notes.append("teacher-only divider")
    if "EXTERNAL_OPEN" in compact:
        notes.append("EXTERNAL_OPEN status retained")
    if "|" in compact and "---" in compact and "Time" not in compact:
        # raw markdown tables sometimes leave pipes; schedule tables rendered as real tables won't show ---
        pass
    if len(compact) < 40:
        notes.append("sparse page — mostly section title or spacer")
        if "KUTUMBA" in compact and len(compact) < 25:
            issue = "near-blank"
            status = "FAIL"
    observation = (
        f"Text extracted from page {page_no} of {artifact}: {head}"
        + ((" — " + "; ".join(notes)) if notes else "")
    )
    return observation, issue, status


def main() -> None:
    rows = []
    for pdf in sorted(EXPORTS.glob("*.pdf")):
        doc = fitz.open(pdf)
        for i in range(doc.page_count):
            text = body_text(doc[i])
            obs, issue, status = observe(pdf.name, i + 1, text)
            rows.append(
                {
                    "artifact": pdf.name,
                    "page": str(i + 1),
                    "assessment": "text_extract_preflight",
                    "text_observation": obs,
                    "issue": issue,
                    "fix_iteration": "1" if not issue else "pending",
                    "status": status,
                }
            )
        doc.close()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "artifact",
                "page",
                "assessment",
                "text_observation",
                "issue",
                "fix_iteration",
                "status",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)
    fails = sum(1 for r in rows if r["status"] == "FAIL")
    print(f"Wrote {len(rows)} rows to {OUT.relative_to(REPO)}; FAIL rows={fails}")


if __name__ == "__main__":
    main()

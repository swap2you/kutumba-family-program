#!/usr/bin/env python3
"""Validate C1-W1 V12.2 gold-standard substance (not mere file presence)."""
from __future__ import annotations

import csv
import re
import sys
import zipfile
from pathlib import Path

import pymupdf as fitz

REPO = Path(__file__).resolve().parents[2]
BASE = (
    REPO
    / "11-weekly-program-library"
    / "first-six-months"
    / "c1-w1-what-is-kutumba-and-why-are-we-here"
)
EXPORTS = REPO / "exports" / "final" / "week1"
EVIDENCE = REPO / "build-evidence"
GAMMA = BASE / "gamma" / "V12-GAMMA-MASTER-DECK-PROMPT.md"

REQUIRED_PDFS = [
    "KUTUMBA-C1-W1-START-HERE-V12.2.pdf",
    "KUTUMBA-C1-W1-OWNER-RUNBOOK-V12.2.pdf",
    "KUTUMBA-C1-W1-FAMILY-ORIENTATION-AND-COVENANT-V12.2.pdf",
    "KUTUMBA-C1-W1-PARENT-TRACK-V12.2.pdf",
    "KUTUMBA-C1-W1-YOUNGER-TEACHER-PACK-V12.2.pdf",
    "KUTUMBA-C1-W1-OLDER-TEACHER-PACK-V12.2.pdf",
    "KUTUMBA-C1-W1-SATURDAY-PRINT-PACKET-V12.2.pdf",
]

PRINTABLES = {
    "younger": [f"Y0{i}" for i in range(1, 6)],
    "older": [f"O0{i}" for i in range(1, 7)],
    "parent": [f"P0{i}" for i in range(1, 6)],
}

PARENT_BLOCKS = ["0–5", "5–10", "10–18", "18–28", "28–35", "35–40"]
SCHEDULE_MUST = ["2:30", "3:10", "3:30", "3:40", "3:55"]
SCHEDULE_FAIL = ["2:35", "3:25"]
GAMMA_PLACEHOLDERS = [
    "Use one",
    "Discuss one week-specific",
    "Week objective for",
    "Stay in week scope",
    "week research + launch policy as applicable",
]
TEACHING_MEANING = (
    "When we regularly hear and serve the Bhāgavata "
    "(book and devotee association), troubles in the heart are cleared "
    "and steady devotion to the Lord becomes established."
)

FAILS: list[str] = []
PASSES: list[str] = []


def fail(msg: str) -> None:
    FAILS.append(msg)


def ok(msg: str) -> None:
    PASSES.append(msg)


def pdf_text(path: Path) -> str:
    doc = fitz.open(path)
    return "\n".join(page.get_text() for page in doc)


def docx_has_tables(path: Path) -> int:
    with zipfile.ZipFile(path) as zf:
        xml = zf.read("word/document.xml").decode("utf-8", errors="ignore")
    return xml.count("<w:tbl")


def main() -> int:
    # Printable sources
    for folder, codes in PRINTABLES.items():
        directory = BASE / "activities" / f"v12_2-{folder}"
        for code in codes:
            matches = list(directory.glob(f"{code}-*.md"))
            if not matches:
                fail(f"Missing printable source {folder}/{code}-*.md")
            else:
                ok(f"Printable source present {matches[0].name}")

    parent = (BASE / "teacher" / "PARENT-GUIDE.md").read_text(encoding="utf-8")
    for block in PARENT_BLOCKS:
        if block not in parent:
            fail(f"PARENT-GUIDE missing timed block {block}")
        else:
            ok(f"PARENT-GUIDE has block {block}")

    younger = (BASE / "teacher" / "YOUNGER-TEACHER-GUIDE.md").read_text(encoding="utf-8")
    for token in ["0–3", "3–8", "8–15", "15–27", "27–33", "33–38", "38–40", "Our family helps one another remember"]:
        if token not in younger:
            fail(f"YOUNGER-TEACHER-GUIDE missing {token}")
        else:
            ok(f"Younger guide contains {token}")

    older = (BASE / "teacher" / "OLDER-TEACHER-GUIDE.md").read_text(encoding="utf-8")
    for token in ["O01", "O02", "O03", "O04", "O05", "O06", "2:30", "3:10"]:
        if token not in older:
            fail(f"OLDER-TEACHER-GUIDE missing {token}")

    gamma = GAMMA.read_text(encoding="utf-8")
    slide_count = len(re.findall(r"^### Slide\s+\d+", gamma, re.MULTILINE))
    if slide_count < 26:
        fail(f"Gamma slide count {slide_count} < 26")
    elif slide_count > 30:
        fail(f"Gamma slide count {slide_count} > 30 without documented exception")
    else:
        ok(f"Gamma slide count {slide_count}")
    for ph in GAMMA_PLACEHOLDERS:
        if ph in gamma:
            fail(f"Gamma meta placeholder present: {ph}")
    if TEACHING_MEANING not in gamma and "troubles in the heart are cleared" not in gamma:
        fail("Gamma missing complete ŚB 1.2.18 teaching meaning")
    else:
        ok("Gamma contains ŚB 1.2.18 teaching meaning")
    for token in ["2:30", "3:10", "consent", "voluntary"]:
        if token.lower() not in gamma.lower() and token not in gamma:
            # consent/voluntary case-insensitive
            if token in ("consent", "voluntary"):
                if token not in gamma.lower():
                    fail(f"Gamma missing {token}")
            else:
                fail(f"Gamma missing {token}")
        else:
            ok(f"Gamma contains {token}")

    # Exports
    for name in REQUIRED_PDFS:
        pdf = EXPORTS / name
        docx = EXPORTS / name.replace(".pdf", ".docx")
        if not pdf.is_file():
            fail(f"Missing PDF {name}")
            continue
        if not docx.is_file():
            fail(f"Missing DOCX for {name}")
        text = pdf_text(pdf)
        for must in SCHEDULE_MUST:
            if must not in text:
                fail(f"{name} missing schedule token {must}")
        for bad in SCHEDULE_FAIL:
            if bad in text:
                fail(f"{name} contains forbidden schedule {bad}")
        ok(f"Schedule hygiene OK: {name}")
        if docx.is_file():
            tables = docx_has_tables(docx)
            if tables < 1:
                fail(f"{docx.name} has no Word tables")
            else:
                ok(f"{docx.name} has {tables} Word table(s)")
        if "||" in text or re.search(r"\|\s*---\s*\|", text):
            fail(f"{name} appears to contain raw Markdown table markup")
        # printable presence in saturday / track packs
        if "SATURDAY" in name or "YOUNGER" in name:
            for code in PRINTABLES["younger"]:
                if code not in text and code.replace("0", "") not in text:
                    # Y01 etc should appear
                    if code not in text:
                        fail(f"{name} missing printable ref {code}")
        if "SATURDAY" in name or "OLDER" in name:
            for code in PRINTABLES["older"]:
                if code not in text:
                    fail(f"{name} missing printable ref {code}")
        if "SATURDAY" in name or "PARENT" in name:
            for code in PRINTABLES["parent"]:
                if code not in text:
                    fail(f"{name} missing printable ref {code}")

    # Visual QA artifacts must exist and not be brightness-only
    visual_md = EVIDENCE / "V12_2-WEEK1-VISUAL-QA.md"
    page_csv = EVIDENCE / "V12_2-WEEK1-PAGE-QA.csv"
    red = EVIDENCE / "V12_2-WEEK1-OPERATOR-RED-TEAM.md"
    for path in (visual_md, page_csv, red):
        if not path.is_file():
            fail(f"Missing evidence {path.name}")
        else:
            ok(f"Evidence present {path.name}")

    if page_csv.is_file():
        rows = list(csv.DictReader(page_csv.open(encoding="utf-8")))
        if len(rows) < 20:
            fail(f"PAGE-QA.csv only {len(rows)} rows; expected one per page or rich sample")
        generic = 0
        for row in rows:
            obs = (row.get("visual_observation") or "").strip().lower()
            if not obs or "brightness" in obs or obs in {"inspected=yes", "ok", "pass"}:
                generic += 1
        if generic:
            fail(f"PAGE-QA.csv has {generic} generic/brightness-only observations")
        else:
            ok(f"PAGE-QA.csv has {len(rows)} non-generic observations")

    if visual_md.is_file():
        body = visual_md.read_text(encoding="utf-8")
        if "contact-sheet" not in body.lower() and "opened" not in body.lower():
            fail("VISUAL-QA.md does not record opening contact sheets")
        if "average brightness" in body.lower() and "not" not in body.lower():
            fail("VISUAL-QA.md appears to rely on brightness heuristics")

    print(f"PASS checks: {len(PASSES)}")
    print(f"FAIL checks: {len(FAILS)}")
    for item in FAILS:
        print(f"FAIL: {item}")
    if FAILS:
        return 1
    print("WEEK 1 OWNER-RUNNABLE — HUMAN/TEMPLE EXTERNAL GATES REMAIN OPEN")
    return 0


if __name__ == "__main__":
    sys.exit(main())

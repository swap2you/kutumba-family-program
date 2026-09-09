#!/usr/bin/env python3
"""Deterministically validate the repaired C1-W1 DOCX/PDF set."""
from __future__ import annotations

import sys
import zipfile
from pathlib import Path

import pymupdf as fitz

REPO = Path(__file__).resolve().parents[2]
EXPORTS = REPO / "exports" / "final" / "week1"
BASE = REPO / "11-weekly-program-library" / "first-six-months" / "c1-w1-what-is-kutumba-and-why-are-we-here"
NAMES = [
    "KUTUMBA-C1-W1-START-HERE-V12.2", "KUTUMBA-C1-W1-OWNER-RUNBOOK-V12.2",
    "KUTUMBA-C1-W1-FAMILY-ORIENTATION-AND-COVENANT-V12.2", "KUTUMBA-C1-W1-PARENT-TRACK-V12.2",
    "KUTUMBA-C1-W1-YOUNGER-TEACHER-PACK-V12.2", "KUTUMBA-C1-W1-OLDER-TEACHER-PACK-V12.2",
    "KUTUMBA-C1-W1-SATURDAY-PRINT-PACKET-V12.2",
]
FORBIDDEN = [
    "<div", "</div>", "page-break-after:", "```", "[ ear /", "[ beads /",
    "[ helping hands ]", "[ heart / home ]", "35. What is healthy",
    "103. What should happen", "109. Offer one prayer",
] + list("┌┐└┘─│├┤┬┴┼")
MEDIA_PACKETS = ("PARENT-TRACK", "YOUNGER-TEACHER", "OLDER-TEACHER", "SATURDAY-PRINT")


def main() -> int:
    failures: list[str] = []
    passes: list[str] = []
    expected_docx = {f"{name}.docx" for name in NAMES}
    expected_pdf = {f"{name}.pdf" for name in NAMES}
    actual_docx = {p.name for p in EXPORTS.glob("*.docx")}
    actual_pdf = {p.name for p in EXPORTS.glob("*.pdf")}
    if actual_docx != expected_docx:
        failures.append(f"DOCX set mismatch: missing={sorted(expected_docx-actual_docx)} extra={sorted(actual_docx-expected_docx)}")
    if actual_pdf != expected_pdf:
        failures.append(f"PDF set mismatch: missing={sorted(expected_pdf-actual_pdf)} extra={sorted(actual_pdf-expected_pdf)}")
    if actual_docx == expected_docx and actual_pdf == expected_pdf:
        passes.append("Exactly 7 DOCX and 7 PDF files present")

    for name in NAMES:
        docx, pdf = EXPORTS / f"{name}.docx", EXPORTS / f"{name}.pdf"
        if not docx.is_file() or not pdf.is_file():
            continue
        with zipfile.ZipFile(docx) as archive:
            members = archive.namelist()
            xml = archive.read("word/document.xml").decode("utf-8", errors="replace")
        if "<w:tbl" not in xml:
            failures.append(f"{docx.name}: no w:tbl")
        else:
            passes.append(f"{docx.name}: real Word tables present")
        if any(marker in name for marker in MEDIA_PACKETS):
            media = [member for member in members if member.startswith("word/media/")]
            if not media:
                failures.append(f"{docx.name}: expected embedded word/media")
            else:
                passes.append(f"{docx.name}: {len(media)} embedded media files")
        with fitz.open(pdf) as opened:
            if opened.page_count < 1:
                failures.append(f"{pdf.name}: no pages")
                continue
            text = "\n".join(page.get_text() for page in opened)
        folded = text.casefold()
        for token in FORBIDDEN:
            if token.casefold() in folded:
                failures.append(f"{pdf.name}: forbidden token {token!r}")
        for required in ("2:30", "3:10"):
            if required not in text:
                failures.append(f"{pdf.name}: locked schedule token {required} missing")
        for obsolete in ("2:35", "3:25"):
            if obsolete in text:
                failures.append(f"{pdf.name}: obsolete schedule token {obsolete}")
        passes.append(f"{pdf.name}: text preflight completed")

    parent = (BASE / "teacher" / "PARENT-GUIDE.md").read_text(encoding="utf-8")
    for block in ("0–5", "5–10", "10–18", "18–28", "28–35", "35–40"):
        if block not in parent:
            failures.append(f"PARENT-GUIDE source missing {block}")
    if all(block in parent for block in ("0–5", "5–10", "10–18", "18–28", "28–35", "35–40")):
        passes.append("Parent guide source retains 0–5 through 35–40")

    print(f"PASS checks: {len(passes)}")
    print(f"FAIL checks: {len(failures)}")
    for item in failures:
        print(f"FAIL: {item}")
    if failures:
        return 1
    print("VALIDATE PASS — automated publishing checks only; human/temple gates remain EXTERNAL_OPEN")
    return 0


if __name__ == "__main__":
    sys.exit(main())

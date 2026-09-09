#!/usr/bin/env python3
"""Render master first-six-month navigation DOCX/PDF set."""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.section import WD_ORIENT
from docx.shared import Inches

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "scripts" / "v12"))
sys.path.insert(0, str(REPO / "scripts" / "v13"))
from kutumba_docx_styles import add_cover, add_header_footer, apply_kutumba_styles  # noqa: E402
from render_markdown_safe import render_markdown_safe  # noqa: E402
from render_publication_docs import convert_with_word  # noqa: E402

OUT = REPO / "exports" / "final" / "v13" / "master"
STATUS = "Internal founding-cohort — human/temple gates EXTERNAL_OPEN"

PACKETS = [
    ("KUTUMBA-FIRST-SIX-MONTHS-OWNER-HANDBOOK-V13", "Owner Handbook", REPO / "11-weekly-program-library/first-six-months/V13-OWNER-HANDBOOK.md"),
    ("KUTUMBA-FIRST-SIX-MONTHS-TEACHER-HANDBOOK-V13", "Teacher Handbook", REPO / "11-weekly-program-library/first-six-months/V13-TEACHER-HANDBOOK.md"),
    ("KUTUMBA-FIRST-SIX-MONTHS-CALENDAR-V13", "Calendar", REPO / "launch/FIRST-SIX-MONTHS-CALENDAR.md"),
    ("KUTUMBA-FIRST-SIX-MONTHS-VERSE-SOURCE-INDEX-V13", "Verse/Source Index", REPO / "build-evidence/V13-VERSE-CHAIN.md"),
    ("KUTUMBA-FIRST-SIX-MONTHS-ACTIVITY-INDEX-V13", "Activity Index", REPO / "11-weekly-program-library/first-six-months/V13-ACTIVITY-VARIETY-MATRIX.md"),
    ("KUTUMBA-FIRST-SIX-MONTHS-RIGHTS-AND-ATTRIBUTION-V13", "Rights", REPO / "11-weekly-program-library/first-six-months/V13-RIGHTS-AND-ATTRIBUTION.md"),
    ("KUTUMBA-FIRST-SIX-MONTHS-START-HERE-V13", "Start Here", REPO / "V13-FIRST-SIX-MONTHS-START-HERE.md"),
]


def build(stem: str, title: str, source: Path) -> None:
    doc = Document()
    apply_kutumba_styles(doc)
    add_cover(doc, title, "First Six Months", "V13 Master Library", version="V13", status=STATUS)
    add_header_footer(doc, "V13 Master", "Owner/Teacher")
    for section in doc.sections:
        section.orientation = WD_ORIENT.PORTRAIT
        section.page_width = Inches(8.5)
        section.page_height = Inches(11)
    body = source.read_text(encoding="utf-8-sig") if source.is_file() else f"MISSING {source}"
    digest = hashlib.sha256(source.read_bytes()).hexdigest() if source.is_file() else "missing"
    doc.add_heading(title, level=1)
    doc.add_paragraph(f"Canonical source: {source.as_posix()} • SHA-256: {digest}", style="KUTUMBA Rights")
    title_match = re.search(r"^#\s+(.+)$", body, re.M)
    render_markdown_safe(doc, body, title_match.group(1).strip() if title_match else title)
    OUT.mkdir(parents=True, exist_ok=True)
    docx = OUT / f"{stem}.docx"
    pdf = OUT / f"{stem}.pdf"
    doc.save(docx)
    convert_with_word(docx, pdf)
    print("wrote", stem)


def main() -> int:
    for stem, title, source in PACKETS:
        build(stem, title, source)
    # lightweight index packets from start-here excerpts
    for stem, title in [
        ("KUTUMBA-FIRST-SIX-MONTHS-GAMMA-INDEX-V13", "Gamma Index"),
        ("KUTUMBA-FIRST-SIX-MONTHS-PROJECT-ROADMAP-V13", "Project Roadmap"),
        ("KUTUMBA-FIRST-SIX-MONTHS-FAMILY-HOME-PRACTICE-ROADMAP-V13", "Home Practice Roadmap"),
        ("KUTUMBA-FIRST-SIX-MONTHS-UTSAVA-GUIDE-V13", "Utsava Guide"),
    ]:
        src = REPO / "V13-FIRST-SIX-MONTHS-START-HERE.md"
        build(stem, title, src)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

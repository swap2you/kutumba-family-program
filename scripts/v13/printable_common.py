#!/usr/bin/env python3
"""Shared Word-table helpers for V13 participant printables."""
from __future__ import annotations

import sys
from pathlib import Path

from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "scripts" / "v12"))
from kutumba_docx_styles import CREAM, PLUM, SAFFRON, TEAL, add_branded_table, add_callout  # noqa: E402

__all__ = [
    "CREAM", "PLUM", "SAFFRON", "TEAL",
    "add_border", "add_shade", "add_printable_title", "add_page",
    "add_teacher_only_divider", "add_teacher_page", "add_card_grid",
    "add_cut_lines", "add_write_lines", "add_memory_phrase_block",
]


def add_border(table, color: str = PLUM, size: int = 10) -> None:
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        element = OxmlElement(f"w:{edge}")
        element.set(qn("w:val"), "single")
        element.set(qn("w:sz"), str(size))
        element.set(qn("w:color"), color)
        borders.append(element)
    table._tbl.tblPr.append(borders)


def add_shade(cell, color: str) -> None:
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), color)
    cell._tc.get_or_add_tcPr().append(shd)


def add_printable_title(document, code: str, title: str, instruction: str = "") -> None:
    document.add_heading(f"{code} — {title}", level=1)
    if instruction:
        p = document.add_paragraph(instruction)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER


def add_page(document) -> None:
    document.add_page_break()


def add_teacher_only_divider(document, note: str = "") -> None:
    document.add_page_break()
    p = document.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Inches(2.3)
    r = p.add_run("TEACHER-ONLY")
    r.bold = True
    r.font.size = Pt(32)
    r.font.color.rgb = RGBColor.from_string(PLUM)
    text = note or "Remove teacher-only pages before distributing participant copies."
    note_p = document.add_paragraph(text)
    note_p.alignment = WD_ALIGN_PARAGRAPH.CENTER


def add_teacher_page(document, title: str, rows) -> None:
    add_page(document)
    p = document.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("TEACHER-ONLY")
    r.bold = True
    r.font.size = Pt(30)
    r.font.color.rgb = RGBColor.from_string(PLUM)
    document.add_heading(title, level=1)
    add_branded_table(document, ["Item", "Best match / guidance"], rows)


def add_card_grid(
    document,
    cards: list[str],
    prefix: str = "CARD ",
    columns: int = 2,
    per_page: int = 6,
) -> None:
    for start in range(0, len(cards), per_page):
        if start:
            add_page(document)
        group = cards[start:start + per_page]
        rows = (len(group) + columns - 1) // columns
        table = document.add_table(rows=rows, cols=columns)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        add_border(table, TEAL, 9)
        cells = [c for row in table.rows for c in row.cells]
        for i, cell in enumerate(cells):
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            cell.width = Inches(3.3)
            if i >= len(group):
                cell.text = ""
                continue
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(14)
            tag = p.add_run(f"{prefix}{start + i + 1}\n")
            tag.bold = True
            tag.font.color.rgb = RGBColor.from_string(PLUM)
            body = p.add_run(group[i])
            body.font.size = Pt(13)
            p.paragraph_format.space_after = Pt(14)


def add_cut_lines(document, label: str = "Cut on the dashed borders. Keep each card intact.") -> None:
    p = document.add_paragraph(label)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.runs[0]
    r.italic = True
    r.font.size = Pt(11)
    r.font.color.rgb = RGBColor.from_string(TEAL)


def add_write_lines(document, prompts: list[str], line_count: int = 2) -> None:
    table = document.add_table(rows=len(prompts), cols=1)
    add_border(table, TEAL, 7)
    for prompt, cell in zip(prompts, table.column_cells(0)):
        p = cell.paragraphs[0]
        p.add_run(prompt).bold = True
        for _ in range(line_count):
            cell.add_paragraph("________________________________________________________________")


def add_memory_phrase_block(document, phrase: str, heading: str = "Memory phrase") -> None:
    document.add_heading(heading, level=2)
    table = document.add_table(rows=1, cols=1)
    add_border(table, SAFFRON, 10)
    cell = table.rows[0].cells[0]
    add_shade(cell, CREAM)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(12)
    r = p.add_run(phrase)
    r.bold = True
    r.font.size = Pt(18)
    r.font.color.rgb = RGBColor.from_string(PLUM)

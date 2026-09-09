#!/usr/bin/env python3
"""V13 Markdown renderer that never exposes HTML, fences, or ASCII art."""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "scripts" / "v12"))
from kutumba_docx_styles import add_branded_table, add_callout, add_verse_card  # noqa: E402
from render_publication_docs import (  # noqa: E402
    CALLOUT_ALIASES, _add_inline, _callout_from_text, _parse_verse_directive,
    _table_cells, _table_separator,
)

HTML_RE = re.compile(r"^\s*</?(?:div|span|p|br)\b|page-break-after\s*:", re.I)
ASCII_RE = re.compile(r"[┌┐└┘─│├┤┬┴┼]|^\s*[+=|]{3,}")


def render_markdown_safe(document, body: str, title: str = "") -> None:
    """Render safe semantic Word content; fenced diagrams are omitted."""
    lines = body.splitlines()
    index = 0
    in_fence = False
    skipped_title = False
    while index < len(lines):
        line = lines[index].rstrip()
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            index += 1
            continue
        if in_fence or not stripped or HTML_RE.search(stripped) or ASCII_RE.search(stripped):
            index += 1
            continue
        if stripped == ":::PAGE_BREAK":
            document.add_page_break()
            index += 1
            continue
        verse = _parse_verse_directive(lines, index)
        if verse:
            values, index = verse
            add_verse_card(document, values.get("reference", "Reference pending"),
                           values.get("devanagari", ""), values.get("iast", ""),
                           values.get("teaching_meaning", values.get("meaning", "")),
                           values.get("url", ""), values.get("rights_status", "Rights review pending"))
            continue
        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            level = min(len(heading.group(1)), 4)
            text = heading.group(2).strip().rstrip("#").strip()
            if level == 1 and not skipped_title and title and text.casefold() == title.casefold():
                skipped_title = True
            else:
                p = document.add_heading(level=level); _add_inline(p, text)
            index += 1
            continue
        if line.lstrip().startswith("|") and index + 1 < len(lines) and _table_separator(lines[index + 1]):
            headers = _table_cells(line)
            index += 2
            rows = []
            while index < len(lines) and lines[index].lstrip().startswith("|"):
                rows.append(_table_cells(lines[index])); index += 1
            add_branded_table(document, headers, rows)
            continue
        if line.lstrip().startswith(">"):
            parts = []
            while index < len(lines) and lines[index].lstrip().startswith(">"):
                parts.append(lines[index].lstrip()[1:].strip()); index += 1
            text = " ".join(parts)
            callout = _callout_from_text(text)
            if callout and callout[0] in CALLOUT_ALIASES.values():
                add_callout(document, *callout)
            else:
                p = document.add_paragraph(style="Quote"); _add_inline(p, text)
            continue
        callout = _callout_from_text(line)
        if callout and callout[0] in CALLOUT_ALIASES.values():
            add_callout(document, *callout); index += 1; continue
        bullet = re.match(r"^\s*[-+*]\s+(.+)$", line)
        if bullet:
            p = document.add_paragraph(style="List Bullet"); _add_inline(p, bullet.group(1))
            index += 1; continue
        if re.match(r"^\s*\d+[.)]\s+(.+)$", line):
            counter = 1
            while index < len(lines):
                numbered = re.match(r"^\s*\d+[.)]\s+(.+)$", lines[index])
                if not numbered:
                    break
                p = document.add_paragraph()
                _add_inline(p, f"{counter}. {numbered.group(1)}")
                p.paragraph_format.left_indent = __import__("docx").shared.Inches(.2)
                counter += 1; index += 1
            continue
        if re.fullmatch(r"[-*_]{3,}", stripped):
            index += 1
            continue
        paragraph_lines = [stripped]
        index += 1
        while index < len(lines):
            candidate = lines[index].strip()
            if (not candidate or candidate.startswith(("#", ">", "|", "```", "~~~", ":::"))
                    or HTML_RE.search(candidate)
                    or re.match(r"^\s*(?:[-+*]|\d+[.)])\s+", lines[index])):
                break
            if not ASCII_RE.search(candidate):
                paragraph_lines.append(candidate)
            index += 1
        p = document.add_paragraph()
        _add_inline(p, " ".join(paragraph_lines))


render_markdown = render_markdown_safe

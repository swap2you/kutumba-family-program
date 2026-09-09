#!/usr/bin/env python3
"""C3-W3 V13 printable Word builders for render_week.py (week id C3-W3).

Real Word tables/images. DOCX/PDF emission is owned by scripts/v13/render_week.py.
"""
from __future__ import annotations

import sys
from pathlib import Path

from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt, RGBColor

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "scripts" / "v13"))
sys.path.insert(0, str(REPO / "scripts" / "v12"))
from printable_common import (  # noqa: E402
    PLUM,
    SAFFRON,
    TEAL,
    add_border,
    add_card_grid,
    add_cut_lines,
    add_memory_phrase_block,
    add_page,
    add_printable_title,
    add_teacher_page,
    add_write_lines,
)
from kutumba_docx_styles import add_branded_table, add_callout, add_verse_card  # noqa: E402

ASSETS = REPO / "11-weekly-program-library/first-six-months/c3-w3-guru-sādhu-and-śāstra-how-we-receive-spiritual-knowledge" / "visuals" / "v13"
MEMORY = 'Ask, serve, verify.'
VERSE_REF = 'BG 4.34'
VERSE_URL = 'https://vedabase.io/en/library/bg/4/34/'
DEV = 'तद्विद्धि प्रणिपातेन परिप्रश्नेन सेवया । उपदेक्ष्यन्ति ते ज्ञानं ज्ञानिनस्तत्त्वदर्शिनः ॥ ३४ ॥'
IAST = 'tad viddhi praṇipātena paripraśnena sevayā / upadekṣyanti te jñānaṁ jñāninas tattva-darśinaḥ'
MEANING = 'Learn the truth by approaching a realized teacher with humility, sincere inquiry, and service — such seers of truth can impart knowledge.'


def _img(document, name: str, width: float = 2.4) -> None:
    path = ASSETS / name
    if path.is_file():
        p = document.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(str(path), width=Inches(width))


def y01(document) -> None:
    add_printable_title(document, "Y01", "Ask-check cards", "Ask → listen → check with a trusted adult/book.")
    _img(document, "three-source-check.png", 5.5)
    add_card_grid(document, ['Ask kindly', 'Guess loudly', 'Check a book', 'Serve a little', 'Believe every video', 'Say I will verify'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Age-appropriate authority boundaries; no personality cult; “I don’t know; I will verify.”')

def y02(document) -> None:
    add_printable_title(document, "Y02", "Humble help matching", "Match asking kindly to learning.")
    _img(document, "ask-check-cards.png", 5.5)
    add_card_grid(document, ['Ask kindly', 'Guess loudly', 'Check a book', 'Serve a little', 'Believe every video', 'Say I will verify'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Age-appropriate authority boundaries; no personality cult; “I don’t know; I will verify.”')

def y03(document) -> None:
    add_printable_title(document, "Y03", "Three-friends craft", "Teacher / holy person example / book icons.")
    _img(document, "verify-path.png", 5.5)
    add_card_grid(document, ['Ask kindly', 'Guess loudly', 'Check a book', 'Serve a little', 'Believe every video', 'Say I will verify'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Age-appropriate authority boundaries; no personality cult; “I don’t know; I will verify.”')

def y04(document) -> None:
    add_printable_title(document, "Y04", "I-will-verify cards", "Practice the deferral sentence.")
    _img(document, "memory-mat.png", 5.5)
    add_card_grid(document, ['Ask kindly', 'Guess loudly', 'Check a book', 'Serve a little', 'Believe every video', 'Say I will verify'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Age-appropriate authority boundaries; no personality cult; “I don’t know; I will verify.”')

def y05(document) -> None:
    add_printable_title(document, "Y05", "Memory phrase mat", "Echo: Ask, serve, verify.")
    _img(document, "memory-mat.png", 6.0)
    add_memory_phrase_block(document, MEMORY)
    document.add_paragraph('BG 4.34' + " · family week")


def o01(document) -> None:
    add_printable_title(document, "O01", "BG 4.34 observation", "Humility, inquiry, service triad.")
    add_verse_card(document, VERSE_REF, DEV, IAST, MEANING, VERSE_URL,
        "Scripture display/source: VedaBase; teaching meaning: KUTUMBA-original (not labeled as BBT translation).")
    add_write_lines(document, [
        "What does the verse teach in my words?",
        "What misconception does this week block?",
        "One question for the facilitator:",
    ], 2)

def o02(document) -> None:
    add_printable_title(document, "O02", "Guru–sādhu–śāstra check", "Verify a claim with three-source map.")
    _img(document, "ask-check-cards.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Guru–sādhu–śāstra check", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Approach realized teachers with humility, inquiry, and service; verify; KUTUMBA is not a initiating guru.')

def o03(document) -> None:
    add_printable_title(document, "O03", "Safe vs unsafe authority sort", "Sort healthy receiving vs cultish traps.")
    _img(document, "verify-path.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Safe vs unsafe authority sort", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Approach realized teachers with humility, inquiry, and service; verify; KUTUMBA is not a initiating guru.')

def o04(document) -> None:
    add_printable_title(document, "O04", "Verify practice scenarios", "Three rumor/claim cases.")
    _img(document, "memory-mat.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Verify practice scenarios", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Approach realized teachers with humility, inquiry, and service; verify; KUTUMBA is not a initiating guru.')

def o05(document) -> None:
    add_printable_title(document, "O05", "Receiving-knowledge diagram", "Approach → inquire → serve → verify.")
    _img(document, "parent-verify.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Receiving-knowledge diagram", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Approach realized teachers with humility, inquiry, and service; verify; KUTUMBA is not a initiating guru.')

def o06(document) -> None:
    add_printable_title(document, "O06", "Exit ticket", "Deferral line + one verify habit.")
    add_write_lines(document, [
        "Primary in one sentence:",
        "One analogy or mechanic and its limit:",
        "One home action:",
        "One question I still have:",
    ], 2)


def p01(document) -> None:
    add_printable_title(document, "P01", "Private reflection — authority boundaries", "Where do we over-claim or under-verify?")
    _img(document, "parent-icon.png", 3.2)
    add_callout(document, "SAFETY_PRIVACY", "Write privately. Sharing is optional. Do not collect or place completed sheets in Git.")
    _img(document, "parent-verify.png", 3.5)
    p = document.add_paragraph('Where do we over-claim or under-verify?')
    p.runs[0].bold = True
    add_write_lines(document, ["Private notes:", "Habit to watch this week:"], 4)

def p02(document) -> None:
    add_printable_title(document, "P02", "Verify practice card sort", "Sort VERIFY / SPECULATE / OVERCLAIM.")
    mats = document.add_table(rows=1, cols=2)
    add_border(mats, PLUM, 10)
    for cell, label in zip(mats.rows[0].cells, ("HELPFUL", "MISTAKEN")):
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(label)
        r.bold = True
        r.font.size = Pt(22)
        r.font.color.rgb = RGBColor.from_string(TEAL if label == "HELPFUL" else SAFFRON)
    add_page(document)
    add_card_grid(document, ['Check śāstra', 'Personality cult praise', 'Ask a teacher', 'Forward rumor', 'KUTUMBA is my guru', 'Defer and verify'], prefix="L", per_page=12)
    add_callout(document, "TEACHER_NOTE", 'Personality-cult framing; KUTUMBA claims of initiating authority; “I feel it so it is true.”')
    _img(document, "parent-verify.png", 3.0)

def p03(document) -> None:
    add_printable_title(document, "P03", "Substantial family case", "Relative forwards a dramatic spiritual rumor as “must share.”")
    add_callout(document, "SAFETY_PRIVACY", "Fictional case. No compelled confession of real events.")
    document.add_paragraph('A relative forwards a dramatic spiritual rumor as “must share tonight.” One parent wants to forward immediately; another wants to verify but feels rude.')
    add_write_lines(document, [
        "Tempting mistaken conclusion:",
        "Principle from primary:",
        "Compassionate response:",
        "One seven-day household action:",
        "What we should not say:",
    ], 3)
    _img(document, "three-source-check.png", 4.0)

def p04(document) -> None:
    add_printable_title(document, "P04", "Household operating application", "Family verify phrase for seven days.")
    add_callout(document, "SAFETY_PRIVACY", "No ranking and no public reading required.")
    add_write_lines(document, [
        "One household action for seven days:",
        "Trigger (when/where):",
        "Who starts if others are tired:",
        "Minimum version on a hard day:",
    ], 3)
    add_memory_phrase_block(document, MEMORY)
    _img(document, "parent-verify.png", 3.2)

def p05(document) -> None:
    add_printable_title(document, "P05", "Private next-step saṅkalpa", "One verify habit + minimum version.")
    add_callout(document, "KEY_IDEA", "specific action + frequency + trigger + minimum version")
    add_write_lines(document, [
        "Specific action:",
        "Frequency:",
        "Trigger (when and where):",
        "Minimum version for a hard day:",
        "Where we will place the reminder:",
    ], 2)
    _img(document, "parent-verify.png", 4.5)
    document.add_paragraph("No ranking. The minimum version counts as success.")


YOUNGER_BUILDERS = [y01, y02, y03, y04, y05]
OLDER_BUILDERS = [o01, o02, o03, o04, o05, o06]
PARENT_BUILDERS = [p01, p02, p03, p04, p05]
FAMILY_BUILDERS = []

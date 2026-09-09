#!/usr/bin/env python3
"""C2-W6 V13 printable Word builders for render_week.py (week id C2-W6).

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

ASSETS = REPO / "11-weekly-program-library/first-six-months/c2-w6-integration-night-choice-consequence-and-the-modes" / "visuals" / "v13"
MEMORY = 'Choose with all five lenses.'
VERSE_REF = 'Cycle 2 review (BG 18.63 center)'
VERSE_URL = 'https://vedabase.io/en/library/bg/18/63/'
DEV = 'इति ते ज्ञानमाख्यातं गुह्याद्गुह्यतरं मया । विमृश्यैतदशेषेण यथेच्छसि तथा कुरु ॥ ६३ ॥'
IAST = 'iti te jñānam ākhyātaṁ guhyād guhyataraṁ mayā / vimṛśyaitad aśeṣeṇa yathecchasi tathā kuru'
MEANING = 'Choice, consequence, and the modes must form one coherent family practice — synthesis, not new doctrine overload. (BG 18.63 center for review.)'


def _img(document, name: str, width: float = 2.4) -> None:
    path = ASSETS / name
    if path.is_file():
        p = document.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(str(path), width=Inches(width))


def y01(document) -> None:
    add_printable_title(document, "Y01", "Review game stations", "Visit karma / choice / dress / weather / escape stations.")
    _img(document, "five-lens-board.png", 5.5)
    add_card_grid(document, ['Karma seed', 'Next choice', 'Dress change', 'Mode weather', 'Escape path', 'Trophy ranking'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Retrieval/presentation focus; no major new doctrine; noncompetitive teach-back.')

def y02(document) -> None:
    add_printable_title(document, "Y02", "Five-lens matching", "Match icons to Cycle 2 themes.")
    _img(document, "retrieval-stations.png", 5.5)
    add_card_grid(document, ['Karma seed', 'Next choice', 'Dress change', 'Mode weather', 'Escape path', 'Trophy ranking'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Retrieval/presentation focus; no major new doctrine; noncompetitive teach-back.')

def y03(document) -> None:
    add_printable_title(document, "Y03", "Teach-back craft", "One sentence our family can teach.")
    _img(document, "teach-back.png", 5.5)
    add_card_grid(document, ['Karma seed', 'Next choice', 'Dress change', 'Mode weather', 'Escape path', 'Trophy ranking'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Retrieval/presentation focus; no major new doctrine; noncompetitive teach-back.')

def y04(document) -> None:
    add_printable_title(document, "Y04", "Cheer cards", "Encourage other families without ranking.")
    _img(document, "memory-mat.png", 5.5)
    add_card_grid(document, ['Karma seed', 'Next choice', 'Dress change', 'Mode weather', 'Escape path', 'Trophy ranking'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Retrieval/presentation focus; no major new doctrine; noncompetitive teach-back.')

def y05(document) -> None:
    add_printable_title(document, "Y05", "Memory phrase mat", "Echo: Choose with all five lenses.")
    _img(document, "memory-mat.png", 6.0)
    add_memory_phrase_block(document, MEMORY)
    document.add_paragraph('Cycle 2 review (BG 18.63 center)' + " · family week")


def o01(document) -> None:
    add_printable_title(document, "O01", "Cycle 2 retrieval quiz", "Retrieve BG 3.9 / 18.63 / 2.22 / 14.5 / 7.14 themes.")
    add_verse_card(document, VERSE_REF, DEV, IAST, MEANING, VERSE_URL,
        "Scripture display/source: VedaBase; teaching meaning: KUTUMBA-original (not labeled as BBT translation).")
    add_write_lines(document, [
        "What does the verse teach in my words?",
        "What misconception does this week block?",
        "One question for the facilitator:",
    ], 2)

def o02(document) -> None:
    add_printable_title(document, "O02", "Choice + modes board", "Place scenarios on choice/consequence/mode board.")
    _img(document, "retrieval-stations.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Choice + modes board", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Cycle 2 becomes one family practice: responsible choice, consequence awareness, mode supports — taught back without ranking.')

def o03(document) -> None:
    add_printable_title(document, "O03", "Misconception clinic", "Correct fatalism, labeling, scare talk, paranoia.")
    _img(document, "teach-back.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Misconception clinic", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Cycle 2 becomes one family practice: responsible choice, consequence awareness, mode supports — taught back without ranking.')

def o04(document) -> None:
    add_printable_title(document, "O04", "Teach-back scenarios", "Coach a 2-minute family teach-back.")
    _img(document, "memory-mat.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Teach-back scenarios", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Cycle 2 becomes one family practice: responsible choice, consequence awareness, mode supports — taught back without ranking.')

def o05(document) -> None:
    add_printable_title(document, "O05", "Integration diagram", "Five lenses → one household practice.")
    _img(document, "parent-integration.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Integration diagram", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Cycle 2 becomes one family practice: responsible choice, consequence awareness, mode supports — taught back without ranking.')

def o06(document) -> None:
    add_printable_title(document, "O06", "Exit ticket", "One synthesis sentence + one home cue.")
    add_write_lines(document, [
        "Primary in one sentence:",
        "One analogy or mechanic and its limit:",
        "One home action:",
        "One question I still have:",
    ], 2)


def p01(document) -> None:
    add_printable_title(document, "P01", "Private reflection — what stuck", "Which Cycle 2 lens most needs household practice?")
    _img(document, "parent-icon.png", 3.2)
    add_callout(document, "SAFETY_PRIVACY", "Write privately. Sharing is optional. Do not collect or place completed sheets in Git.")
    _img(document, "parent-integration.png", 3.5)
    p = document.add_paragraph('Which Cycle 2 lens most needs household practice?')
    p.runs[0].bold = True
    add_write_lines(document, ["Private notes:", "Habit to watch this week:"], 4)

def p02(document) -> None:
    add_printable_title(document, "P02", "Teach-back card sort", "Sort RETRIEVAL / APPLICATION / RANKING (avoid).")
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
    add_card_grid(document, ['Retrieve a verse theme', 'Apply at home', 'Rank families', 'Correct a misconception', 'New advanced doctrine dump', 'Cheer another family'], prefix="L", per_page=12)
    add_callout(document, "TEACHER_NOTE", 'Integration means new advanced doctrine; ranking families by presentation polish.')
    _img(document, "parent-integration.png", 3.0)

def p03(document) -> None:
    add_printable_title(document, "P03", "Substantial family case", "Family wants to impress with a polished speech and skip retrieval.")
    add_callout(document, "SAFETY_PRIVACY", "Fictional case. No compelled confession of real events.")
    document.add_paragraph('A family rehearses a polished speech to impress others and skips retrieving the actual Cycle 2 verse themes. Children worry about “winning” Integration Night.')
    add_write_lines(document, [
        "Tempting mistaken conclusion:",
        "Principle from primary:",
        "Compassionate response:",
        "One seven-day household action:",
        "What we should not say:",
    ], 3)
    _img(document, "five-lens-board.png", 4.0)

def p04(document) -> None:
    add_printable_title(document, "P04", "Household operating application", "One teach-back sentence + practice night.")
    add_callout(document, "SAFETY_PRIVACY", "No ranking and no public reading required.")
    add_write_lines(document, [
        "One household action for seven days:",
        "Trigger (when/where):",
        "Who starts if others are tired:",
        "Minimum version on a hard day:",
    ], 3)
    add_memory_phrase_block(document, MEMORY)
    _img(document, "parent-integration.png", 3.2)

def p05(document) -> None:
    add_printable_title(document, "P05", "Private next-step saṅkalpa", "Integration practice for seven days.")
    add_callout(document, "KEY_IDEA", "specific action + frequency + trigger + minimum version")
    add_write_lines(document, [
        "Specific action:",
        "Frequency:",
        "Trigger (when and where):",
        "Minimum version for a hard day:",
        "Where we will place the reminder:",
    ], 2)
    _img(document, "parent-integration.png", 4.5)
    document.add_paragraph("No ranking. The minimum version counts as success.")


YOUNGER_BUILDERS = [y01, y02, y03, y04, y05]
OLDER_BUILDERS = [o01, o02, o03, o04, o05, o06]
PARENT_BUILDERS = [p01, p02, p03, p04, p05]
FAMILY_BUILDERS = []

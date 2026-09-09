#!/usr/bin/env python3
"""C2-W2 V13 printable Word builders for render_week.py (week id C2-W2).

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

ASSETS = REPO / "11-weekly-program-library/first-six-months/c2-w2-free-will-and-responsibility-the-next-choice-matters" / "visuals" / "v13"
MEMORY = 'The next choice matters.'
VERSE_REF = 'BG 18.63'
VERSE_URL = 'https://vedabase.io/en/library/bg/18/63/'
DEV = 'इति ते ज्ञानमाख्यातं गुह्याद्गुह्यतरं मया । विमृश्यैतदशेषेण यथेच्छसि तथा कुरु ॥ ६३ ॥'
IAST = 'iti te jñānam ākhyātaṁ guhyād guhyataraṁ mayā / vimṛśyaitad aśeṣeṇa yathecchasi tathā kuru'
MEANING = 'The Lord has explained confidential knowledge; now deliberate fully and then act as you choose — responsibility remains with the living being.'


def _img(document, name: str, width: float = 2.4) -> None:
    path = ASSETS / name
    if path.is_file():
        p = document.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(str(path), width=Inches(width))


def y01(document) -> None:
    add_printable_title(document, "Y01", "Fork-in-road movement", "Walk left/right forks for kind vs sharp next choice.")
    _img(document, "fork-road.png", 5.5)
    add_card_grid(document, ['Share now', 'Grab first', 'Ask for help', 'Hide the mess', 'Say the truth kindly', 'Blame a sibling'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Do not blame children for events beyond their control; distinguish agency from total control.')

def y02(document) -> None:
    add_printable_title(document, "Y02", "Next-choice matching", "Match situations to better next steps.")
    _img(document, "decision-tree.png", 5.5)
    add_card_grid(document, ['Share now', 'Grab first', 'Ask for help', 'Hide the mess', 'Say the truth kindly', 'Blame a sibling'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Do not blame children for events beyond their control; distinguish agency from total control.')

def y03(document) -> None:
    add_printable_title(document, "Y03", "Simple choice-tree craft", "Draw two branches from one fork.")
    _img(document, "agency-rings.png", 5.5)
    add_card_grid(document, ['Share now', 'Grab first', 'Ask for help', 'Hide the mess', 'Say the truth kindly', 'Blame a sibling'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Do not blame children for events beyond their control; distinguish agency from total control.')

def y04(document) -> None:
    add_printable_title(document, "Y04", "Agency + care cards", "Cards: I can choose / I need help / Not my fault.")
    _img(document, "memory-mat.png", 5.5)
    add_card_grid(document, ['Share now', 'Grab first', 'Ask for help', 'Hide the mess', 'Say the truth kindly', 'Blame a sibling'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Do not blame children for events beyond their control; distinguish agency from total control.')

def y05(document) -> None:
    add_printable_title(document, "Y05", "Memory phrase mat", "Echo: The next choice matters.")
    _img(document, "memory-mat.png", 6.0)
    add_memory_phrase_block(document, MEMORY)
    document.add_paragraph('BG 18.63' + " · family week")


def o01(document) -> None:
    add_printable_title(document, "O01", "BG 18.63 observation", "Observe deliberation + choice language.")
    add_verse_card(document, VERSE_REF, DEV, IAST, MEANING, VERSE_URL,
        "Scripture display/source: VedaBase; teaching meaning: KUTUMBA-original (not labeled as BBT translation).")
    add_write_lines(document, [
        "What does the verse teach in my words?",
        "What misconception does this week block?",
        "One question for the facilitator:",
    ], 2)

def o02(document) -> None:
    add_printable_title(document, "O02", "Next-choice decision tree", "Build a 3-level tree for a real low-risk fork.")
    _img(document, "decision-tree.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Next-choice decision tree", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Knowledge invites deliberation; the living being still chooses; the next choice matters.')

def o03(document) -> None:
    add_printable_title(document, "O03", "Agency vs control sort", "Sort what I can choose / influence / not control.")
    _img(document, "agency-rings.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Agency vs control sort", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Knowledge invites deliberation; the living being still chooses; the next choice matters.')

def o04(document) -> None:
    add_printable_title(document, "O04", "Responsibility scenarios", "Three cases: blame, freeze, responsible next step.")
    _img(document, "memory-mat.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Responsibility scenarios", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Knowledge invites deliberation; the living being still chooses; the next choice matters.')

def o05(document) -> None:
    add_printable_title(document, "O05", "Deliberation worksheet", "vimṛśya practice: facts, options, values, choose.")
    _img(document, "parent-agency.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Deliberation worksheet", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Knowledge invites deliberation; the living being still chooses; the next choice matters.')

def o06(document) -> None:
    add_printable_title(document, "O06", "Exit ticket", "My next responsible choice tomorrow.")
    add_write_lines(document, [
        "Primary in one sentence:",
        "One analogy or mechanic and its limit:",
        "One home action:",
        "One question I still have:",
    ], 2)


def p01(document) -> None:
    add_printable_title(document, "P01", "Private reflection — agency vs control", "Where do we confuse control with responsibility?")
    _img(document, "parent-icon.png", 3.2)
    add_callout(document, "SAFETY_PRIVACY", "Write privately. Sharing is optional. Do not collect or place completed sheets in Git.")
    _img(document, "parent-agency.png", 3.5)
    p = document.add_paragraph('Where do we confuse control with responsibility?')
    p.runs[0].bold = True
    add_write_lines(document, ["Private notes:", "Habit to watch this week:"], 4)

def p02(document) -> None:
    add_printable_title(document, "P02", "Agency vs control card sort", "Sort CAN CHOOSE / CAN INFLUENCE / CANNOT CONTROL.")
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
    add_card_grid(document, ['My tone in an argument', 'Traffic delay', 'Sibling’s mood', 'Whether I apologize', 'Weather', 'My homework start time'], prefix="L", per_page=12)
    add_callout(document, "TEACHER_NOTE", 'Choice means do whatever you feel; OR the soul has no agency / “I had no choice.”')
    _img(document, "parent-agency.png", 3.0)

def p03(document) -> None:
    add_printable_title(document, "P03", "Substantial family case", "Teen freezes after a grade drop; parent says “you had no choice but to fail.”")
    add_callout(document, "SAFETY_PRIVACY", "Fictional case. No compelled confession of real events.")
    document.add_paragraph('A teen freezes after a grade drop. One parent says “you had no choice but to fail.” Another lectures for twenty minutes without naming a next step.')
    add_write_lines(document, [
        "Tempting mistaken conclusion:",
        "Principle from primary:",
        "Compassionate response:",
        "One seven-day household action:",
        "What we should not say:",
    ], 3)
    _img(document, "fork-road.png", 4.0)

def p04(document) -> None:
    add_printable_title(document, "P04", "Household operating application", "One nightly deliberation cue for seven days.")
    add_callout(document, "SAFETY_PRIVACY", "No ranking and no public reading required.")
    add_write_lines(document, [
        "One household action for seven days:",
        "Trigger (when/where):",
        "Who starts if others are tired:",
        "Minimum version on a hard day:",
    ], 3)
    add_memory_phrase_block(document, MEMORY)
    _img(document, "parent-agency.png", 3.2)

def p05(document) -> None:
    add_printable_title(document, "P05", "Private next-step saṅkalpa", "Specific next choice + trigger + minimum version.")
    add_callout(document, "KEY_IDEA", "specific action + frequency + trigger + minimum version")
    add_write_lines(document, [
        "Specific action:",
        "Frequency:",
        "Trigger (when and where):",
        "Minimum version for a hard day:",
        "Where we will place the reminder:",
    ], 2)
    _img(document, "parent-agency.png", 4.5)
    document.add_paragraph("No ranking. The minimum version counts as success.")


YOUNGER_BUILDERS = [y01, y02, y03, y04, y05]
OLDER_BUILDERS = [o01, o02, o03, o04, o05, o06]
PARENT_BUILDERS = [p01, p02, p03, p04, p05]
FAMILY_BUILDERS = []

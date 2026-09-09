#!/usr/bin/env python3
"""C2-W3 V13 printable Word builders for render_week.py (week id C2-W3).

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

ASSETS = REPO / "11-weekly-program-library/first-six-months/c2-w3-birth-death-and-reincarnation" / "visuals" / "v13"
MEMORY = 'Birth and death are changes of dress for the eternal self.'
VERSE_REF = 'BG 2.22'
VERSE_URL = 'https://vedabase.io/en/library/bg/2/22/'
DEV = 'वासांसि जीर्णानि यथा विहाय नवानि गृह्णाति नरोऽपराणि । तथा शरीराणि विहाय जीर्णान्यन्यानि संयाति नवानि देही ॥ २२ ॥'
IAST = 'vāsāṁsi jīrṇāni yathā vihāya navāni gṛhṇāti naro ’parāṇi / tathā śarīrāṇi vihāya jīrṇāny anyāni saṁyāti navāni dehī'
MEANING = 'As a person puts on new garments, giving up old ones, the embodied self similarly accepts new bodies, giving up old ones — taught calmly, without fear tactics for children.'


def _img(document, name: str, width: float = 2.4) -> None:
    path = ASSETS / name
    if path.is_file():
        p = document.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(str(path), width=Inches(width))


def y01(document) -> None:
    add_printable_title(document, "Y01", "Gentle clothes-change sequence", "Order worn shirt → folded shirt → new shirt; say the limit.")
    _img(document, "clothes-change.png", 5.5)
    add_card_grid(document, ['Fold old shirt', 'Put on fresh shirt', 'Say a kind thank-you', 'Scare story', 'Hug a friend', 'Guess a ghost tale'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Age-sensitive death talk; no frightening imagery; no unsupported past-life anecdotes.')

def y02(document) -> None:
    add_printable_title(document, "Y02", "Same-friend care matching", "Match care acts that honor a person who changes.")
    _img(document, "analogy-limits.png", 5.5)
    add_card_grid(document, ['Fold old shirt', 'Put on fresh shirt', 'Say a kind thank-you', 'Scare story', 'Hug a friend', 'Guess a ghost tale'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Age-sensitive death talk; no frightening imagery; no unsupported past-life anecdotes.')

def y03(document) -> None:
    add_printable_title(document, "Y03", "Calm-heart craft", "Draw a calm heart for kind words about change.")
    _img(document, "calm-heart.png", 5.5)
    add_card_grid(document, ['Fold old shirt', 'Put on fresh shirt', 'Say a kind thank-you', 'Scare story', 'Hug a friend', 'Guess a ghost tale'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Age-sensitive death talk; no frightening imagery; no unsupported past-life anecdotes.')

def y04(document) -> None:
    add_printable_title(document, "Y04", "Gentle words cards", "Redirect scare talk to gentle cards.")
    _img(document, "memory-mat.png", 5.5)
    add_card_grid(document, ['Fold old shirt', 'Put on fresh shirt', 'Say a kind thank-you', 'Scare story', 'Hug a friend', 'Guess a ghost tale'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Age-sensitive death talk; no frightening imagery; no unsupported past-life anecdotes.')

def y05(document) -> None:
    add_printable_title(document, "Y05", "Memory phrase mat", "Echo the dress-change memory line gently.")
    _img(document, "memory-mat.png", 6.0)
    add_memory_phrase_block(document, MEMORY)
    document.add_paragraph('BG 2.22' + " · family week")


def o01(document) -> None:
    add_printable_title(document, "O01", "BG 2.22 observation", "Observe analogy language and its classroom limits.")
    add_verse_card(document, VERSE_REF, DEV, IAST, MEANING, VERSE_URL,
        "Scripture display/source: VedaBase; teaching meaning: KUTUMBA-original (not labeled as BBT translation).")
    add_write_lines(document, [
        "What does the verse teach in my words?",
        "What misconception does this week block?",
        "One question for the facilitator:",
    ], 2)

def o02(document) -> None:
    add_printable_title(document, "O02", "Analogy + limits worksheet", "Map garment analogy; write where it breaks.")
    _img(document, "analogy-limits.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Analogy + limits worksheet", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'The clothing analogy teaches continuity with limits; families speak with calm dignity, not fear.')

def o03(document) -> None:
    add_printable_title(document, "O03", "Calm vs scare speech sort", "Sort respectful teaching vs fear tactics.")
    _img(document, "calm-heart.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Calm vs scare speech sort", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'The clothing analogy teaches continuity with limits; families speak with calm dignity, not fear.')

def o04(document) -> None:
    add_printable_title(document, "O04", "Age-sensitive scenarios", "Three family talk scenarios with boundaries.")
    _img(document, "memory-mat.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Age-sensitive scenarios", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'The clothing analogy teaches continuity with limits; families speak with calm dignity, not fear.')

def o05(document) -> None:
    add_printable_title(document, "O05", "Continuity + care diagram", "Self continues; body deserves care.")
    _img(document, "parent-calm-talk.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Continuity + care diagram", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'The clothing analogy teaches continuity with limits; families speak with calm dignity, not fear.')

def o06(document) -> None:
    add_printable_title(document, "O06", "Exit ticket", "One analogy + one limit + one calm sentence.")
    add_write_lines(document, [
        "Primary in one sentence:",
        "One analogy or mechanic and its limit:",
        "One home action:",
        "One question I still have:",
    ], 2)


def p01(document) -> None:
    add_printable_title(document, "P01", "Private reflection — how we talk about death", "What scare or silence patterns do we use?")
    _img(document, "parent-icon.png", 3.2)
    add_callout(document, "SAFETY_PRIVACY", "Write privately. Sharing is optional. Do not collect or place completed sheets in Git.")
    _img(document, "parent-calm-talk.png", 3.5)
    p = document.add_paragraph('What scare or silence patterns do we use?')
    p.runs[0].bold = True
    add_write_lines(document, ["Private notes:", "Habit to watch this week:"], 4)

def p02(document) -> None:
    add_printable_title(document, "P02", "Calm speech card sort", "Sort CALM / SCARE / SPECULATION.")
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
    add_card_grid(document, ['Bodies change like clothes (with limits)', 'Frighten kids into belief', 'We care for elders', 'Diagnose someone’s destination', 'Photos prove reincarnation', 'Speak gently about loss'], prefix="L", per_page=12)
    add_callout(document, "TEACHER_NOTE", 'Scare pedagogy; diagnosing destinations; ghost speculation; closet-shopping for bodies.')
    _img(document, "parent-calm-talk.png", 3.0)

def p03(document) -> None:
    add_printable_title(document, "P03", "Substantial family case", "Child asks about a grandparent’s death at dinner.")
    add_callout(document, "SAFETY_PRIVACY", "Fictional case. No compelled confession of real events.")
    document.add_paragraph('At dinner a child asks where a grandparent “went.” One adult freezes. Another launches into graphic afterlife details and a destination diagnosis.')
    add_write_lines(document, [
        "Tempting mistaken conclusion:",
        "Principle from primary:",
        "Compassionate response:",
        "One seven-day household action:",
        "What we should not say:",
    ], 3)
    _img(document, "clothes-change.png", 4.0)

def p04(document) -> None:
    add_printable_title(document, "P04", "Household operating application", "One calm-response line + who speaks first.")
    add_callout(document, "SAFETY_PRIVACY", "No ranking and no public reading required.")
    add_write_lines(document, [
        "One household action for seven days:",
        "Trigger (when/where):",
        "Who starts if others are tired:",
        "Minimum version on a hard day:",
    ], 3)
    add_memory_phrase_block(document, MEMORY)
    _img(document, "parent-calm-talk.png", 3.2)

def p05(document) -> None:
    add_printable_title(document, "P05", "Private next-step saṅkalpa", "Practice one calm conversation cue.")
    add_callout(document, "KEY_IDEA", "specific action + frequency + trigger + minimum version")
    add_write_lines(document, [
        "Specific action:",
        "Frequency:",
        "Trigger (when and where):",
        "Minimum version for a hard day:",
        "Where we will place the reminder:",
    ], 2)
    _img(document, "parent-calm-talk.png", 4.5)
    document.add_paragraph("No ranking. The minimum version counts as success.")


YOUNGER_BUILDERS = [y01, y02, y03, y04, y05]
OLDER_BUILDERS = [o01, o02, o03, o04, o05, o06]
PARENT_BUILDERS = [p01, p02, p03, p04, p05]
FAMILY_BUILDERS = []

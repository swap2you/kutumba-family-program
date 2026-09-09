#!/usr/bin/env python3
"""C3-W2 V13 printable Word builders for render_week.py (week id C3-W2).

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

ASSETS = REPO / "11-weekly-program-library/first-six-months/c3-w2-who-is-kṛṣṇa-the-supreme-personality-of-godhead" / "visuals" / "v13"
MEMORY = 'Nothing is above Kṛṣṇa.'
VERSE_REF = 'BG 7.7'
VERSE_URL = 'https://vedabase.io/en/library/bg/7/7/'
DEV = 'मत्त: परतरं नान्यत्किञ्चिदस्ति धनञ्जय । मयि सर्वमिदं प्रोतं सूत्रे मणिगणा इव ॥ ७ ॥'
IAST = 'mattaḥ parataraṁ nānyat kiñcid asti dhanañ-jaya / mayi sarvam idaṁ protaṁ sūtre maṇi-gaṇā iva'
MEANING = 'There is no truth superior to Kṛṣṇa; everything rests upon Him as pearls are strung on a thread.'


def _img(document, name: str, width: float = 2.4) -> None:
    path = ASSETS / name
    if path.is_file():
        p = document.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(str(path), width=Inches(width))


def y01(document) -> None:
    add_printable_title(document, "Y01", "Who-is-Kṛṣṇa picture cues", "Cue cards: flute/friend/protector — reverence, not jokes.")
    _img(document, "source-identity.png", 5.5)
    add_card_grid(document, ['Listen to a verse', 'Joke about Deity', 'Thread and pearls', 'Kind prayer', 'Yell to win', 'Ask a teacher'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Authorized sources only; no speculative theology; reverence over aggression.')

def y02(document) -> None:
    add_printable_title(document, "Y02", "Source matching", "Match “we learn from books/teachers” to listening.")
    _img(document, "thread-pearls.png", 5.5)
    add_card_grid(document, ['Listen to a verse', 'Joke about Deity', 'Thread and pearls', 'Kind prayer', 'Yell to win', 'Ask a teacher'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Authorized sources only; no speculative theology; reverence over aggression.')

def y03(document) -> None:
    add_printable_title(document, "Y03", "Thread-and-pearl craft", "Craft simple thread with beads — analogy with limits.")
    _img(document, "reverence-icons.png", 5.5)
    add_card_grid(document, ['Listen to a verse', 'Joke about Deity', 'Thread and pearls', 'Kind prayer', 'Yell to win', 'Ask a teacher'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Authorized sources only; no speculative theology; reverence over aggression.')

def y04(document) -> None:
    add_printable_title(document, "Y04", "Reverence cards", "Speak kindly about Kṛṣṇa; no mockery.")
    _img(document, "memory-mat.png", 5.5)
    add_card_grid(document, ['Listen to a verse', 'Joke about Deity', 'Thread and pearls', 'Kind prayer', 'Yell to win', 'Ask a teacher'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Authorized sources only; no speculative theology; reverence over aggression.')

def y05(document) -> None:
    add_printable_title(document, "Y05", "Memory phrase mat", "Echo: Nothing is above Kṛṣṇa.")
    _img(document, "memory-mat.png", 6.0)
    add_memory_phrase_block(document, MEMORY)
    document.add_paragraph('BG 7.7' + " · family week")


def o01(document) -> None:
    add_printable_title(document, "O01", "BG 7.7 observation", "Source identity of supremacy + thread analogy limits.")
    add_verse_card(document, VERSE_REF, DEV, IAST, MEANING, VERSE_URL,
        "Scripture display/source: VedaBase; teaching meaning: KUTUMBA-original (not labeled as BBT translation).")
    add_write_lines(document, [
        "What does the verse teach in my words?",
        "What misconception does this week block?",
        "One question for the facilitator:",
    ], 2)

def o02(document) -> None:
    add_printable_title(document, "O02", "Source observation worksheet", "What the verse says / does not say.")
    _img(document, "thread-pearls.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Source observation worksheet", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'There is no truth superior to Kṛṣṇa; everything rests upon Him — taught from sources with reverence.')

def o03(document) -> None:
    add_printable_title(document, "O03", "Reverence vs aggression sort", "Sort speech postures.")
    _img(document, "reverence-icons.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Reverence vs aggression sort", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'There is no truth superior to Kṛṣṇa; everything rests upon Him — taught from sources with reverence.')

def o04(document) -> None:
    add_printable_title(document, "O04", "Identity application scenarios", "Three school/home speech cases.")
    _img(document, "memory-mat.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Identity application scenarios", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'There is no truth superior to Kṛṣṇa; everything rests upon Him — taught from sources with reverence.')

def o05(document) -> None:
    add_printable_title(document, "O05", "Thread analogy diagram", "Pearls on thread + limit box.")
    _img(document, "parent-reverence.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Thread analogy diagram", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'There is no truth superior to Kṛṣṇa; everything rests upon Him — taught from sources with reverence.')

def o06(document) -> None:
    add_printable_title(document, "O06", "Exit ticket", "One source sentence + one reverence rule.")
    add_write_lines(document, [
        "Primary in one sentence:",
        "One analogy or mechanic and its limit:",
        "One home action:",
        "One question I still have:",
    ], 2)


def p01(document) -> None:
    add_printable_title(document, "P01", "Private reflection — how we speak of Kṛṣṇa", "Reverence or argument culture?")
    _img(document, "parent-icon.png", 3.2)
    add_callout(document, "SAFETY_PRIVACY", "Write privately. Sharing is optional. Do not collect or place completed sheets in Git.")
    _img(document, "parent-reverence.png", 3.5)
    p = document.add_paragraph('Reverence or argument culture?')
    p.runs[0].bold = True
    add_write_lines(document, ["Private notes:", "Habit to watch this week:"], 4)

def p02(document) -> None:
    add_printable_title(document, "P02", "Reverence card sort", "Sort REVERENT / AGGRESSIVE / SPECULATIVE.")
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
    add_card_grid(document, ['Cite BG 7.7 calmly', 'Win online fight', 'Speculate freely', 'Read with family', 'Mock other faiths', 'Reverent gratitude'], prefix="L", per_page=12)
    add_callout(document, "TEACHER_NOTE", 'Aggressive debate identity; speculative iconography/theology beyond sources.')
    _img(document, "parent-reverence.png", 3.0)

def p03(document) -> None:
    add_printable_title(document, "P03", "Substantial family case", "Teen wants to “win” a religion argument online.")
    add_callout(document, "SAFETY_PRIVACY", "Fictional case. No compelled confession of real events.")
    document.add_paragraph('A teen wants to “destroy” a classmate’s view online. Parents debate whether to coach winning rhetoric or reverent source-based speech.')
    add_write_lines(document, [
        "Tempting mistaken conclusion:",
        "Principle from primary:",
        "Compassionate response:",
        "One seven-day household action:",
        "What we should not say:",
    ], 3)
    _img(document, "source-identity.png", 4.0)

def p04(document) -> None:
    add_printable_title(document, "P04", "Household operating application", "One reverence speech rule for seven days.")
    add_callout(document, "SAFETY_PRIVACY", "No ranking and no public reading required.")
    add_write_lines(document, [
        "One household action for seven days:",
        "Trigger (when/where):",
        "Who starts if others are tired:",
        "Minimum version on a hard day:",
    ], 3)
    add_memory_phrase_block(document, MEMORY)
    _img(document, "parent-reverence.png", 3.2)

def p05(document) -> None:
    add_printable_title(document, "P05", "Private next-step saṅkalpa", "Source reading cue + minimum version.")
    add_callout(document, "KEY_IDEA", "specific action + frequency + trigger + minimum version")
    add_write_lines(document, [
        "Specific action:",
        "Frequency:",
        "Trigger (when and where):",
        "Minimum version for a hard day:",
        "Where we will place the reminder:",
    ], 2)
    _img(document, "parent-reverence.png", 4.5)
    document.add_paragraph("No ranking. The minimum version counts as success.")


YOUNGER_BUILDERS = [y01, y02, y03, y04, y05]
OLDER_BUILDERS = [o01, o02, o03, o04, o05, o06]
PARENT_BUILDERS = [p01, p02, p03, p04, p05]
FAMILY_BUILDERS = []

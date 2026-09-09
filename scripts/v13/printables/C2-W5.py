#!/usr/bin/env python3
"""C2-W5 V13 printable Word builders for render_week.py (week id C2-W5).

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

ASSETS = REPO / "11-weekly-program-library/first-six-months/c2-w5-māyā-decorating-the-prison-cell" / "visuals" / "v13"
MEMORY = 'Surrender crosses māyā.'
VERSE_REF = 'BG 7.14'
VERSE_URL = 'https://vedabase.io/en/library/bg/7/14/'
DEV = 'दैवी ह्येषा गुणमयी मम माया दुरत्यया । मामेव ये प्रपद्यन्ते मायामेतां तरन्ति ते ॥ १४ ॥'
IAST = 'daivī hy eṣā guṇa-mayī mama māyā duratyayā / mām eva ye prapadyante māyām etāṁ taranti te'
MEANING = 'This divine illusory energy of the Lord, made of the modes, is difficult to overcome — but those who surrender unto Him cross beyond it.'


def _img(document, name: str, width: float = 2.4) -> None:
    path = ASSETS / name
    if path.is_file():
        p = document.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(str(path), width=Inches(width))


def y01(document) -> None:
    add_printable_title(document, "Y01", "Simple trap/escape path", "Follow path: shiny trap → pause → call Kṛṣṇa / kind help.")
    _img(document, "trap-escape-path.png", 5.5)
    add_card_grid(document, ['Shiny toy shout', 'Pause', 'Ask for help', 'Holy name', 'Scare story', 'Kind share'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Age-sensitive; no fear/paranoia; decorating-prison analogy with limits.')

def y02(document) -> None:
    add_printable_title(document, "Y02", "Shiny vs real matching", "Match ads/toys to “looks big” vs “helps love.”")
    _img(document, "illusion-board.png", 5.5)
    add_card_grid(document, ['Shiny toy shout', 'Pause', 'Ask for help', 'Holy name', 'Scare story', 'Kind share'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Age-sensitive; no fear/paranoia; decorating-prison analogy with limits.')

def y03(document) -> None:
    add_printable_title(document, "Y03", "Escape lantern craft", "Craft a lantern card for holy name / help.")
    _img(document, "escape-lantern.png", 5.5)
    add_card_grid(document, ['Shiny toy shout', 'Pause', 'Ask for help', 'Holy name', 'Scare story', 'Kind share'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Age-sensitive; no fear/paranoia; decorating-prison analogy with limits.')

def y04(document) -> None:
    add_printable_title(document, "Y04", "Pause cards", "When stuck, point to Pause / Ask / Chant.")
    _img(document, "memory-mat.png", 5.5)
    add_card_grid(document, ['Shiny toy shout', 'Pause', 'Ask for help', 'Holy name', 'Scare story', 'Kind share'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Age-sensitive; no fear/paranoia; decorating-prison analogy with limits.')

def y05(document) -> None:
    add_printable_title(document, "Y05", "Memory phrase mat", "Echo: Surrender crosses māyā.")
    _img(document, "memory-mat.png", 6.0)
    add_memory_phrase_block(document, MEMORY)
    document.add_paragraph('BG 7.14' + " · family week")


def o01(document) -> None:
    add_printable_title(document, "O01", "BG 7.14 observation", "Observe difficulty + surrender crossing.")
    add_verse_card(document, VERSE_REF, DEV, IAST, MEANING, VERSE_URL,
        "Scripture display/source: VedaBase; teaching meaning: KUTUMBA-original (not labeled as BBT translation).")
    add_write_lines(document, [
        "What does the verse teach in my words?",
        "What misconception does this week block?",
        "One question for the facilitator:",
    ], 2)

def o02(document) -> None:
    add_printable_title(document, "O02", "Advertising illusion board", "Map attention traps and better aims.")
    _img(document, "illusion-board.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Advertising illusion board", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Illusory energy is hard to cross; surrender and Kṛṣṇa-centered practice open the path — without fear pedagogy.')

def o03(document) -> None:
    add_printable_title(document, "O03", "Trap vs escape sort", "Sort decorating-bondage vs crossing helps.")
    _img(document, "escape-lantern.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Trap vs escape sort", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Illusory energy is hard to cross; surrender and Kṛṣṇa-centered practice open the path — without fear pedagogy.')

def o04(document) -> None:
    add_printable_title(document, "O04", "Attention trap scenarios", "Three low-risk family attention cases.")
    _img(document, "memory-mat.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Attention trap scenarios", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Illusory energy is hard to cross; surrender and Kṛṣṇa-centered practice open the path — without fear pedagogy.')

def o05(document) -> None:
    add_printable_title(document, "O05", "Escape-map diagram", "Notice → turn → shelter in Kṛṣṇa practice.")
    _img(document, "parent-attention.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Escape-map diagram", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Illusory energy is hard to cross; surrender and Kṛṣṇa-centered practice open the path — without fear pedagogy.')

def o06(document) -> None:
    add_printable_title(document, "O06", "Exit ticket", "One trap I notice + one surrender practice.")
    add_write_lines(document, [
        "Primary in one sentence:",
        "One analogy or mechanic and its limit:",
        "One home action:",
        "One question I still have:",
    ], 2)


def p01(document) -> None:
    add_printable_title(document, "P01", "Private reflection — attention audit", "Where do we decorate comfort while neglecting devotion?")
    _img(document, "parent-icon.png", 3.2)
    add_callout(document, "SAFETY_PRIVACY", "Write privately. Sharing is optional. Do not collect or place completed sheets in Git.")
    _img(document, "parent-attention.png", 3.5)
    p = document.add_paragraph('Where do we decorate comfort while neglecting devotion?')
    p.runs[0].bold = True
    add_write_lines(document, ["Private notes:", "Habit to watch this week:"], 4)

def p02(document) -> None:
    add_printable_title(document, "P02", "Attention audit card sort", "Sort TRAP / CROSSING HELP / HARMFUL FRAMING.")
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
    add_card_grid(document, ['Endless upgrade chase', 'Short holy name', 'Women are māyā', 'Willpower alone', 'Serve quietly', 'Paranoia about all matter'], prefix="L", per_page=12)
    add_callout(document, "TEACHER_NOTE", 'Hate all material duty / “women are māyā”; willpower alone conquers māyā without surrender.')
    _img(document, "parent-attention.png", 3.0)

def p03(document) -> None:
    add_printable_title(document, "P03", "Substantial family case", "Family upgrades gadgets weekly while skipping shared chanting.")
    add_callout(document, "SAFETY_PRIVACY", "Fictional case. No compelled confession of real events.")
    document.add_paragraph('A family keeps upgrading gadgets and rearranging décor while shared chanting disappears. One adult jokes “we’re just making the prison nicer.” Another says “all duty is māyā — quit your job.”')
    add_write_lines(document, [
        "Tempting mistaken conclusion:",
        "Principle from primary:",
        "Compassionate response:",
        "One seven-day household action:",
        "What we should not say:",
    ], 3)
    _img(document, "trap-escape-path.png", 4.0)

def p04(document) -> None:
    add_printable_title(document, "P04", "Household operating application", "One attention-audit cue + one chanting shelter.")
    add_callout(document, "SAFETY_PRIVACY", "No ranking and no public reading required.")
    add_write_lines(document, [
        "One household action for seven days:",
        "Trigger (when/where):",
        "Who starts if others are tired:",
        "Minimum version on a hard day:",
    ], 3)
    add_memory_phrase_block(document, MEMORY)
    _img(document, "parent-attention.png", 3.2)

def p05(document) -> None:
    add_printable_title(document, "P05", "Private next-step saṅkalpa", "Surrender practice + minimum version.")
    add_callout(document, "KEY_IDEA", "specific action + frequency + trigger + minimum version")
    add_write_lines(document, [
        "Specific action:",
        "Frequency:",
        "Trigger (when and where):",
        "Minimum version for a hard day:",
        "Where we will place the reminder:",
    ], 2)
    _img(document, "parent-attention.png", 4.5)
    document.add_paragraph("No ranking. The minimum version counts as success.")


YOUNGER_BUILDERS = [y01, y02, y03, y04, y05]
OLDER_BUILDERS = [o01, o02, o03, o04, o05, o06]
PARENT_BUILDERS = [p01, p02, p03, p04, p05]
FAMILY_BUILDERS = []

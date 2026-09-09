#!/usr/bin/env python3
"""C3-W5 V13 printable Word builders for render_week.py (week id C3-W5).

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

ASSETS = REPO / "11-weekly-program-library/first-six-months/c3-w5-the-nine-processes-of-bhakti" / "visuals" / "v13"
MEMORY = 'Nine ways to love Viṣṇu.'
VERSE_REF = 'ŚB 7.5.23–24'
VERSE_URL = 'https://vedabase.io/en/library/sb/7/5/23-24/'
DEV = 'श्रीप्रह्राद उवाच श्रवणं कीर्तनं विष्णो: स्मरणं पादसेवनम् । अर्चनं वन्दनं दास्यं सख्यमात्मनिवेदनम् ॥ २३ ॥ इति पुंसार्पिता विष्णौ भक्तिश्चेन्नवलक्षणा । क्रियेत भगवत्यद्धा तन्मन्येऽधीतमुत्तमम् ॥ २४ ॥'
IAST = "śravaṇaṁ kīrtanaṁ viṣṇoḥ smaraṇaṁ pāda-sevanam / arcanaṁ vandanaṁ dāsyaṁ sakhyam ātma-nivedanam // iti puṁsārpitā viṣṇau bhaktiś cen nava-lakṣaṇā / kriyeta bhagavaty addhā tan manye 'dhītam uttamam"
MEANING = "Hearing, chanting, remembering, serving the Lord's feet, worship, prayer, servitude, friendship, and full surrender — nine processes of bhakti; when such bhakti is offered to Viṣṇu, that is considered the topmost learning."


def _img(document, name: str, width: float = 2.4) -> None:
    path = ASSETS / name
    if path.is_file():
        p = document.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(str(path), width=Inches(width))


def y01(document) -> None:
    add_printable_title(document, "Y01", "Process picture wheel", "Spin/point to nine simple picture slices — no ranking.")
    _img(document, "nine-process-wheel.png", 5.5)
    add_card_grid(document, ['Hear', 'Chant', 'Remember', 'Serve', 'Rank friends', 'Encourage'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Must include both 7.5.23 and 7.5.24; no ranking; one realistic practice.')

def y02(document) -> None:
    add_printable_title(document, "Y02", "Process matching", "Match hear/chant/remember pictures.")
    _img(document, "process-icons.png", 5.5)
    add_card_grid(document, ['Hear', 'Chant', 'Remember', 'Serve', 'Rank friends', 'Encourage'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Must include both 7.5.23 and 7.5.24; no ranking; one realistic practice.')

def y03(document) -> None:
    add_printable_title(document, "Y03", "One-practice craft", "Choose one slice to try at home.")
    _img(document, "choose-one.png", 5.5)
    add_card_grid(document, ['Hear', 'Chant', 'Remember', 'Serve', 'Rank friends', 'Encourage'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Must include both 7.5.23 and 7.5.24; no ranking; one realistic practice.')

def y04(document) -> None:
    add_printable_title(document, "Y04", "Encourage cards", "Cheer others’ practices without ranking.")
    _img(document, "memory-mat.png", 5.5)
    add_card_grid(document, ['Hear', 'Chant', 'Remember', 'Serve', 'Rank friends', 'Encourage'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Must include both 7.5.23 and 7.5.24; no ranking; one realistic practice.')

def y05(document) -> None:
    add_printable_title(document, "Y05", "Memory phrase mat", "Echo: Nine ways to love Viṣṇu.")
    _img(document, "memory-mat.png", 6.0)
    add_memory_phrase_block(document, MEMORY)
    document.add_paragraph('ŚB 7.5.23–24' + " · family week")


def o01(document) -> None:
    add_printable_title(document, "O01", "ŚB 7.5.23–24 observation", "Both verses; nine names; offered to Viṣṇu.")
    add_verse_card(document, VERSE_REF, DEV, IAST, MEANING, VERSE_URL,
        "Scripture display/source: VedaBase; teaching meaning: KUTUMBA-original (not labeled as BBT translation).")
    add_write_lines(document, [
        "What does the verse teach in my words?",
        "What misconception does this week block?",
        "One question for the facilitator:",
    ], 2)

def o02(document) -> None:
    add_printable_title(document, "O02", "Nine-process planning", "Plan one realistic household practice.")
    _img(document, "process-icons.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Nine-process planning", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Nine processes of bhakti to Viṣṇu; families choose one realistic practice; never rank processes or families.')

def o03(document) -> None:
    add_printable_title(document, "O03", "Object vs generic sort", "Viṣṇu-object vs generic virtue.")
    _img(document, "choose-one.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Object vs generic sort", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Nine processes of bhakti to Viṣṇu; families choose one realistic practice; never rank processes or families.')

def o04(document) -> None:
    add_printable_title(document, "O04", "Practice scenarios", "Three busy-family practice cases.")
    _img(document, "memory-mat.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Practice scenarios", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Nine processes of bhakti to Viṣṇu; families choose one realistic practice; never rank processes or families.')

def o05(document) -> None:
    add_printable_title(document, "O05", "Nine-process wheel diagram", "Wheel with center: offered to Viṣṇu.")
    _img(document, "parent-practice.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Nine-process wheel diagram", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Nine processes of bhakti to Viṣṇu; families choose one realistic practice; never rank processes or families.')

def o06(document) -> None:
    add_printable_title(document, "O06", "Exit ticket", "Our one practice + no ranking pledge.")
    add_write_lines(document, [
        "Primary in one sentence:",
        "One analogy or mechanic and its limit:",
        "One home action:",
        "One question I still have:",
    ], 2)


def p01(document) -> None:
    add_printable_title(document, "P01", "Private reflection — realistic practice", "Which process fits our season of life?")
    _img(document, "parent-icon.png", 3.2)
    add_callout(document, "SAFETY_PRIVACY", "Write privately. Sharing is optional. Do not collect or place completed sheets in Git.")
    _img(document, "parent-practice.png", 3.5)
    p = document.add_paragraph('Which process fits our season of life?')
    p.runs[0].bold = True
    add_write_lines(document, ["Private notes:", "Habit to watch this week:"], 4)

def p02(document) -> None:
    add_printable_title(document, "P02", "Choose-one card sort", "Sort REALISTIC / OVERLOAD / RANKING.")
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
    add_card_grid(document, ['One small śravaṇa slot', 'Do all nine perfectly', 'Offer to Viṣṇu', 'Generic kindness only', 'Rank families', 'Minimum version counts'], prefix="L", per_page=12)
    add_callout(document, "TEACHER_NOTE", 'Ranking processes/families; generic virtue without Viṣṇu as object; citing 7.5.23 without 7.5.24.')
    _img(document, "parent-practice.png", 3.0)

def p03(document) -> None:
    add_printable_title(document, "P03", "Substantial family case", "Parents compete over which process is “higher.”")
    add_callout(document, "SAFETY_PRIVACY", "Fictional case. No compelled confession of real events.")
    document.add_paragraph('Parents argue which of the nine processes is “higher” and push children to announce a competitive choice for status.')
    add_write_lines(document, [
        "Tempting mistaken conclusion:",
        "Principle from primary:",
        "Compassionate response:",
        "One seven-day household action:",
        "What we should not say:",
    ], 3)
    _img(document, "nine-process-wheel.png", 4.0)

def p04(document) -> None:
    add_printable_title(document, "P04", "Household operating application", "One chosen process for seven days.")
    add_callout(document, "SAFETY_PRIVACY", "No ranking and no public reading required.")
    add_write_lines(document, [
        "One household action for seven days:",
        "Trigger (when/where):",
        "Who starts if others are tired:",
        "Minimum version on a hard day:",
    ], 3)
    add_memory_phrase_block(document, MEMORY)
    _img(document, "parent-practice.png", 3.2)

def p05(document) -> None:
    add_printable_title(document, "P05", "Private next-step saṅkalpa", "Chosen process + minimum version.")
    add_callout(document, "KEY_IDEA", "specific action + frequency + trigger + minimum version")
    add_write_lines(document, [
        "Specific action:",
        "Frequency:",
        "Trigger (when and where):",
        "Minimum version for a hard day:",
        "Where we will place the reminder:",
    ], 2)
    _img(document, "parent-practice.png", 4.5)
    document.add_paragraph("No ranking. The minimum version counts as success.")


YOUNGER_BUILDERS = [y01, y02, y03, y04, y05]
OLDER_BUILDERS = [o01, o02, o03, o04, o05, o06]
PARENT_BUILDERS = [p01, p02, p03, p04, p05]
FAMILY_BUILDERS = []

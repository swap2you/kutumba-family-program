#!/usr/bin/env python3
"""C3-W6 V13 printable Word builders for render_week.py (week id C3-W6).

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

ASSETS = REPO / "11-weekly-program-library/first-six-months/c3-w6-bhakti-mela-kīrtana-drama-and-family-presentation" / "visuals" / "v13"
MEMORY = 'Offer it to Viṣṇu.'
VERSE_REF = 'Cycle 3 review (ŚB 7.5.23–24 center)'
VERSE_URL = 'https://vedabase.io/en/library/sb/7/5/23-24/'
DEV = 'श्रीप्रह्राद उवाच श्रवणं कीर्तनं विष्णो: स्मरणं पादसेवनम् । अर्चनं वन्दनं दास्यं सख्यमात्मनिवेदनम् ॥ २३ ॥ इति पुंसार्पिता विष्णौ भक्तिश्चेन्नवलक्षणा । क्रियेत भगवत्यद्धा तन्मन्येऽधीतमुत्तमम् ॥ २४ ॥'
IAST = "śravaṇaṁ kīrtanaṁ viṣṇoḥ smaraṇaṁ pāda-sevanam / arcanaṁ vandanaṁ dāsyaṁ sakhyam ātma-nivedanam // iti puṁsārpitā viṣṇau bhaktiś cen nava-lakṣaṇā / kriyeta bhagavaty addhā tan manye 'dhītam uttamam"
MEANING = 'Bhakti Mela integrates Cycle 3 around offering bhakti to Viṣṇu with joy — retrieval and presentation, not new doctrine. (ŚB 7.5.23–24 center.)'


def _img(document, name: str, width: float = 2.4) -> None:
    path = ASSETS / name
    if path.is_file():
        p = document.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(str(path), width=Inches(width))


def y01(document) -> None:
    add_printable_title(document, "Y01", "Mini drama / kīrtana", "Short joyful scene + soft kīrtana invitation.")
    _img(document, "mela-flow.png", 5.5)
    add_card_grid(document, ['Kīrtana joy', 'Short drama', 'Offer to Viṣṇu', 'Trophy fight', 'Cheer friends', 'New doctrine dump'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Integration only; noncompetitive; presentation/retrieval focus.')

def y02(document) -> None:
    add_printable_title(document, "Y02", "Cycle 3 icon matching", "Match five week icons.")
    _img(document, "exhibition-board.png", 5.5)
    add_card_grid(document, ['Kīrtana joy', 'Short drama', 'Offer to Viṣṇu', 'Trophy fight', 'Cheer friends', 'New doctrine dump'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Integration only; noncompetitive; presentation/retrieval focus.')

def y03(document) -> None:
    add_printable_title(document, "Y03", "Exhibition craft", "One poster sentence: Offer it to Viṣṇu.")
    _img(document, "drama-cue.png", 5.5)
    add_card_grid(document, ['Kīrtana joy', 'Short drama', 'Offer to Viṣṇu', 'Trophy fight', 'Cheer friends', 'New doctrine dump'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Integration only; noncompetitive; presentation/retrieval focus.')

def y04(document) -> None:
    add_printable_title(document, "Y04", "Cheer cards", "Encourage every family.")
    _img(document, "memory-mat.png", 5.5)
    add_card_grid(document, ['Kīrtana joy', 'Short drama', 'Offer to Viṣṇu', 'Trophy fight', 'Cheer friends', 'New doctrine dump'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'Integration only; noncompetitive; presentation/retrieval focus.')

def y05(document) -> None:
    add_printable_title(document, "Y05", "Memory phrase mat", "Echo: Offer it to Viṣṇu.")
    _img(document, "memory-mat.png", 6.0)
    add_memory_phrase_block(document, MEMORY)
    document.add_paragraph('Cycle 3 review (ŚB 7.5.23–24 center)' + " · family week")


def o01(document) -> None:
    add_printable_title(document, "O01", "Cycle 3 retrieval", "Retrieve five primary themes.")
    add_verse_card(document, VERSE_REF, DEV, IAST, MEANING, VERSE_URL,
        "Scripture display/source: VedaBase; teaching meaning: KUTUMBA-original (not labeled as BBT translation).")
    add_write_lines(document, [
        "What does the verse teach in my words?",
        "What misconception does this week block?",
        "One question for the facilitator:",
    ], 2)

def o02(document) -> None:
    add_printable_title(document, "O02", "Presentation rubric", "Clarity / source / kindness / time — not polish ranking.")
    _img(document, "exhibition-board.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Presentation rubric", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Review BG 5.29 · 7.7 · 4.34 · CC Antya 20.12 · ŚB 7.5.23–24 through kīrtana, drama, and presentation — no new doctrine.')

def o03(document) -> None:
    add_printable_title(document, "O03", "Noncompetitive sort", "Sort OFFERING / RANKING.")
    _img(document, "drama-cue.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Noncompetitive sort", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Review BG 5.29 · 7.7 · 4.34 · CC Antya 20.12 · ŚB 7.5.23–24 through kīrtana, drama, and presentation — no new doctrine.')

def o04(document) -> None:
    add_printable_title(document, "O04", "Drama/exhibition scenarios", "Three coaching cases.")
    _img(document, "memory-mat.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Drama/exhibition scenarios", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Review BG 5.29 · 7.7 · 4.34 · CC Antya 20.12 · ŚB 7.5.23–24 through kīrtana, drama, and presentation — no new doctrine.')

def o05(document) -> None:
    add_printable_title(document, "O05", "Mela flow diagram", "Kīrtana → drama → present → reflect.")
    _img(document, "parent-exhibition.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Mela flow diagram", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'Review BG 5.29 · 7.7 · 4.34 · CC Antya 20.12 · ŚB 7.5.23–24 through kīrtana, drama, and presentation — no new doctrine.')

def o06(document) -> None:
    add_printable_title(document, "O06", "Exit ticket", "One offering sentence + gratitude.")
    add_write_lines(document, [
        "Primary in one sentence:",
        "One analogy or mechanic and its limit:",
        "One home action:",
        "One question I still have:",
    ], 2)


def p01(document) -> None:
    add_printable_title(document, "P01", "Private reflection — offering vs performing", "Where do we slip into ranking?")
    _img(document, "parent-icon.png", 3.2)
    add_callout(document, "SAFETY_PRIVACY", "Write privately. Sharing is optional. Do not collect or place completed sheets in Git.")
    _img(document, "parent-exhibition.png", 3.5)
    p = document.add_paragraph('Where do we slip into ranking?')
    p.runs[0].bold = True
    add_write_lines(document, ["Private notes:", "Habit to watch this week:"], 4)

def p02(document) -> None:
    add_printable_title(document, "P02", "Exhibition coaching card sort", "Sort COACH / RANK / NEW DOCTRINE.")
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
    add_card_grid(document, ['Retrieve a verse theme', 'Award best family', 'Kind presentation', 'Invent new theology', 'Timebox share', 'Cheer another group'], prefix="L", per_page=12)
    add_callout(document, "TEACHER_NOTE", 'Mela as talent contest; new doctrine dump; ranking presentations.')
    _img(document, "parent-exhibition.png", 3.0)

def p03(document) -> None:
    add_printable_title(document, "P03", "Substantial family case", "Family wants awards for “best drama.”")
    add_callout(document, "SAFETY_PRIVACY", "Fictional case. No compelled confession of real events.")
    document.add_paragraph('A family lobbies for “best drama” awards and wants to introduce a brand-new doctrinal topic during Mela instead of reviewing Cycle 3.')
    add_write_lines(document, [
        "Tempting mistaken conclusion:",
        "Principle from primary:",
        "Compassionate response:",
        "One seven-day household action:",
        "What we should not say:",
    ], 3)
    _img(document, "mela-flow.png", 4.0)

def p04(document) -> None:
    add_printable_title(document, "P04", "Household operating application", "One noncompetitive cheer rule + offering line.")
    add_callout(document, "SAFETY_PRIVACY", "No ranking and no public reading required.")
    add_write_lines(document, [
        "One household action for seven days:",
        "Trigger (when/where):",
        "Who starts if others are tired:",
        "Minimum version on a hard day:",
    ], 3)
    add_memory_phrase_block(document, MEMORY)
    _img(document, "parent-exhibition.png", 3.2)

def p05(document) -> None:
    add_printable_title(document, "P05", "Private next-step saṅkalpa", "Mela offering practice.")
    add_callout(document, "KEY_IDEA", "specific action + frequency + trigger + minimum version")
    add_write_lines(document, [
        "Specific action:",
        "Frequency:",
        "Trigger (when and where):",
        "Minimum version for a hard day:",
        "Where we will place the reminder:",
    ], 2)
    _img(document, "parent-exhibition.png", 4.5)
    document.add_paragraph("No ranking. The minimum version counts as success.")


YOUNGER_BUILDERS = [y01, y02, y03, y04, y05]
OLDER_BUILDERS = [o01, o02, o03, o04, o05, o06]
PARENT_BUILDERS = [p01, p02, p03, p04, p05]
FAMILY_BUILDERS = []

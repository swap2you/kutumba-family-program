#!/usr/bin/env python3
"""C3-W4 V13 printable Word builders for render_week.py (week id C3-W4).

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

ASSETS = REPO / "11-weekly-program-library/first-six-months/c3-w4-śrī-caitanya-mahāprabhu-and-the-holy-name" / "visuals" / "v13"
MEMORY = 'Paraṁ vijayate śrī-kṛṣṇa-saṅkīrtanam.'
VERSE_REF = 'CC Antya 20.12'
VERSE_URL = 'https://vedabase.io/en/library/cc/antya/20/12/'
DEV = 'চেতোদর্পণমার্জনং ভবমহাদাবাগ্নিনির্বাপণং শ্রেয়ঃকৈরবচন্দ্রিকাবিতরণং বিদ্যাবধূজীবনম্ । আনন্দাম্বুধিবর্ধনং প্রতিপদং পূর্ণামৃতাস্বাদনং সর্বাত্মস্নপনং পরং বিজয়তে শ্রীকৃষ্ণসঙ্কীর্তনম্ ॥ ১২ ॥'
IAST = 'ceto-darpaṇa-mārjanaṁ bhava-mahā-dāvāgni-nirvāpaṇaṁ / śreyaḥ-kairava-candrikā-vitaraṇaṁ vidyā-vadhū-jīvanam / ānandāmbudhi-vardhanaṁ prati-padaṁ pūrṇāmṛtāsvādanaṁ / sarvātma-snapanaṁ paraṁ vijayate śrī-kṛṣṇa-saṅkīrtanam'
MEANING = 'All victory to śrī-kṛṣṇa-saṅkīrtana — which cleanses the mirror of the heart, extinguishes the forest fire of material existence, spreads the moonlight of good fortune, is the life of knowledge, expands the ocean of bliss, enables tasting full nectar at every step, and bathes the self — supreme.'


def _img(document, name: str, width: float = 2.4) -> None:
    path = ASSETS / name
    if path.is_file():
        p = document.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(str(path), width=Inches(width))


def y01(document) -> None:
    add_printable_title(document, "Y01", "Name joy movement", "Gentle movement while echoing the holy name — soft voices welcome.")
    _img(document, "kirtana-etiquette.png", 5.5)
    add_card_grid(document, ['Soft voice welcome', 'Yell to win', 'Listen first', 'Mock a singer', 'Join kindly', 'Phone during kīrtana'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'No ranking by volume; include full Śikṣāṣṭaka verse-1 source-language layer; invitation not contest.')

def y02(document) -> None:
    add_printable_title(document, "Y02", "Etiquette matching", "Match listen / join / don’t mock.")
    _img(document, "heart-mirror.png", 5.5)
    add_card_grid(document, ['Soft voice welcome', 'Yell to win', 'Listen first', 'Mock a singer', 'Join kindly', 'Phone during kīrtana'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'No ranking by volume; include full Śikṣāṣṭaka verse-1 source-language layer; invitation not contest.')

def y03(document) -> None:
    add_printable_title(document, "Y03", "Mirror-heart craft", "Craft “clean the mirror” heart card.")
    _img(document, "name-joy.png", 5.5)
    add_card_grid(document, ['Soft voice welcome', 'Yell to win', 'Listen first', 'Mock a singer', 'Join kindly', 'Phone during kīrtana'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'No ranking by volume; include full Śikṣāṣṭaka verse-1 source-language layer; invitation not contest.')

def y04(document) -> None:
    add_printable_title(document, "Y04", "Attention cards", "Eyes soft / voice kind / no contest.")
    _img(document, "memory-mat.png", 5.5)
    add_card_grid(document, ['Soft voice welcome', 'Yell to win', 'Listen first', 'Mock a singer', 'Join kindly', 'Phone during kīrtana'], per_page=6)
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)
    add_callout(document, "TEACHER_NOTE", 'No ranking by volume; include full Śikṣāṣṭaka verse-1 source-language layer; invitation not contest.')

def y05(document) -> None:
    add_printable_title(document, "Y05", "Memory phrase mat", "Echo the saṅkīrtana memory line.")
    _img(document, "memory-mat.png", 6.0)
    add_memory_phrase_block(document, MEMORY)
    document.add_paragraph('CC Antya 20.12' + " · family week")


def o01(document) -> None:
    add_printable_title(document, "O01", "Śikṣāṣṭaka / CC Antya 20.12 observation", "Full source-language layer + teaching meaning.")
    add_verse_card(document, VERSE_REF, DEV, IAST, MEANING, VERSE_URL,
        "Scripture display/source: VedaBase; teaching meaning: KUTUMBA-original (not labeled as BBT translation).")
    add_write_lines(document, [
        "What does the verse teach in my words?",
        "What misconception does this week block?",
        "One question for the facilitator:",
    ], 2)

def o02(document) -> None:
    add_printable_title(document, "O02", "Kīrtana etiquette board", "Attention practices vs performance traps.")
    _img(document, "heart-mirror.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Kīrtana etiquette board", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'All glory to śrī-kṛṣṇa-saṅkīrtana; families practice with attention and etiquette, not performance ranking.')

def o03(document) -> None:
    add_printable_title(document, "O03", "Attention vs performance sort", "Sort cards carefully.")
    _img(document, "name-joy.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Attention vs performance sort", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'All glory to śrī-kṛṣṇa-saṅkīrtana; families practice with attention and etiquette, not performance ranking.')

def o04(document) -> None:
    add_printable_title(document, "O04", "Holy name home scenarios", "Three family practice cases.")
    _img(document, "memory-mat.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Holy name home scenarios", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'All glory to śrī-kṛṣṇa-saṅkīrtana; families practice with attention and etiquette, not performance ranking.')

def o05(document) -> None:
    add_printable_title(document, "O05", "Heart-mirror diagram", "Cleansing metaphor with limits.")
    _img(document, "parent-holy-name.png", 5.0)
    add_branded_table(document, ["Prompt", "My notes"], [["Heart-mirror diagram", "________________"], ["Limit / care", "________________"]])
    add_write_lines(document, ["Application:", "What not to say:"], 2)
    add_callout(document, "KEY_IDEA", 'All glory to śrī-kṛṣṇa-saṅkīrtana; families practice with attention and etiquette, not performance ranking.')

def o06(document) -> None:
    add_printable_title(document, "O06", "Exit ticket", "One etiquette rule + one home minute.")
    add_write_lines(document, [
        "Primary in one sentence:",
        "One analogy or mechanic and its limit:",
        "One home action:",
        "One question I still have:",
    ], 2)


def p01(document) -> None:
    add_printable_title(document, "P01", "Private reflection — home name culture", "Attention or performance pressure?")
    _img(document, "parent-icon.png", 3.2)
    add_callout(document, "SAFETY_PRIVACY", "Write privately. Sharing is optional. Do not collect or place completed sheets in Git.")
    _img(document, "parent-holy-name.png", 3.5)
    p = document.add_paragraph('Attention or performance pressure?')
    p.runs[0].bold = True
    add_write_lines(document, ["Private notes:", "Habit to watch this week:"], 4)

def p02(document) -> None:
    add_printable_title(document, "P02", "Etiquette card sort", "Sort ATTENTIVE / PERFORMANCE / DISRESPECT.")
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
    add_card_grid(document, ['Attentive listening', 'Volume contest', 'Short sincere chant', 'Shame soft voices', 'Invite newcomers', 'Performance ranking'], prefix="L", per_page=12)
    add_callout(document, "TEACHER_NOTE", 'Volume/performance equals devotion; skipping source-language layer of Śikṣāṣṭaka 1.')
    _img(document, "parent-holy-name.png", 3.0)

def p03(document) -> None:
    add_printable_title(document, "P03", "Substantial family case", "Child is shamed for soft chanting.")
    add_callout(document, "SAFETY_PRIVACY", "Fictional case. No compelled confession of real events.")
    document.add_paragraph('A child chants softly and is shamed: “Louder or you’re not devoted.” Another adult starts a volume contest between siblings.')
    add_write_lines(document, [
        "Tempting mistaken conclusion:",
        "Principle from primary:",
        "Compassionate response:",
        "One seven-day household action:",
        "What we should not say:",
    ], 3)
    _img(document, "kirtana-etiquette.png", 4.0)

def p04(document) -> None:
    add_printable_title(document, "P04", "Household operating application", "One attentive holy-name slot for seven days.")
    add_callout(document, "SAFETY_PRIVACY", "No ranking and no public reading required.")
    add_write_lines(document, [
        "One household action for seven days:",
        "Trigger (when/where):",
        "Who starts if others are tired:",
        "Minimum version on a hard day:",
    ], 3)
    add_memory_phrase_block(document, MEMORY)
    _img(document, "parent-holy-name.png", 3.2)

def p05(document) -> None:
    add_printable_title(document, "P05", "Private next-step saṅkalpa", "Holy name practice + minimum version.")
    add_callout(document, "KEY_IDEA", "specific action + frequency + trigger + minimum version")
    add_write_lines(document, [
        "Specific action:",
        "Frequency:",
        "Trigger (when and where):",
        "Minimum version for a hard day:",
        "Where we will place the reminder:",
    ], 2)
    _img(document, "parent-holy-name.png", 4.5)
    document.add_paragraph("No ranking. The minimum version counts as success.")


YOUNGER_BUILDERS = [y01, y02, y03, y04, y05]
OLDER_BUILDERS = [o01, o02, o03, o04, o05, o06]
PARENT_BUILDERS = [p01, p02, p03, p04, p05]
FAMILY_BUILDERS = []

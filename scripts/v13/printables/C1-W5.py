#!/usr/bin/env python3
"""C1-W5 printable Word builders — real tables/images, no ASCII final art."""
from __future__ import annotations

import sys
from pathlib import Path

from docx.shared import Inches

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "scripts" / "v13"))
sys.path.insert(0, str(REPO / "scripts" / "v12"))
from printable_common import (  # noqa: E402
    add_card_grid,
    add_cut_lines,
    add_memory_phrase_block,
    add_printable_title,
    add_teacher_only_divider,
    add_teacher_page,
    add_write_lines,
)
from kutumba_docx_styles import add_branded_table, add_callout  # noqa: E402

MEMORY = "Temporary joys can be used with gratitude; lasting fulfillment is in Kṛṣṇa."
ASSETS = REPO / "11-weekly-program-library/first-six-months/c1-w5-the-temporary-world-and-the-search-for-permanent-happiness/visuals/v13"


def _img(document, name: str, width: float = 2.4) -> None:
    path = ASSETS / name
    if path.is_file():
        document.add_picture(str(path), width=Inches(width))


def y01(document) -> None:
    add_printable_title(document, "Y01", "Temporary / Lasting Sort", "Enjoy with thanks — do not shame.")
    _img(document, "temporary-lasting.png", 5.0)
    add_card_grid(document, [
        "TEMP: New toy fun", "TEMP: Snack joy", "TEMP: Screen episode",
        "LASTING: Thank You Kṛṣṇa", "LASTING: Help someone", "LASTING: Holy name / prayer",
    ])
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)


def y02(document) -> None:
    add_printable_title(document, "Y02", "Sparkler and Lamp Match", "Enjoy sparkler; remember lamp.")
    _img(document, "sparkler-lamp.png", 5.0)
    add_callout(document, "TEACHER_NOTE", "Toys are not worthless. Temporary joys need gratitude.")
    add_cut_lines(document)


def y03(document) -> None:
    add_printable_title(document, "Y03", "Gratitude Offering Craft", "Draw a joy + Thank You, Kṛṣṇa.")
    _img(document, "gratitude-card.png", 4.0)
    add_write_lines(document, ["Temporary joy I enjoyed:", "Thank You line:"], 1)
    add_memory_phrase_block(document, MEMORY)


def y04(document) -> None:
    add_printable_title(document, "Y04", "Kind Enjoyment Speech", "GRATITUDE vs SHAME.")
    add_card_grid(document, [
        "GRATITUDE: Thank you for this fun.",
        "GRATITUDE: Let's offer a short prayer after play.",
        "GRATITUDE: Toys can be enjoyed with care.",
        "SHAME: Your toy is māyā — you are bad.",
        "SHAME: Real devotees never enjoy anything.",
        "SHAME: Family hugs are worthless.",
    ])
    add_cut_lines(document)


def y05(document) -> None:
    add_printable_title(document, "Y05", "Memory Phrase Mat", "Landing mat.")
    _img(document, "memory-mat.png", 5.0)
    add_memory_phrase_block(document, MEMORY)


def o01(document) -> None:
    add_printable_title(document, "O01", "BG 8.15 Observation", "Temporary world vs lasting shelter.")
    add_callout(document, "SASTRA", "BG 8.15 — https://vedabase.io/en/library/bg/8/15/")
    add_callout(document, "DO_NOT_SPECULATE", "No depression/mental-health claims. No shame of ordinary enjoyment.")
    add_write_lines(document, [
        "What is temporary according to tonight's teaching?",
        "What do we refuse to shame?",
        "How can enjoyment become gratitude and service?",
        "Paraphrase BG 8.15 teaching meaning in one sentence.",
    ], 1)


def o02(document) -> None:
    add_printable_title(document, "O02", "Happiness-Duration Lab", "Brief / medium / lasting-direction.")
    add_branded_table(document, ["Experience", "Duration feel", "Gratitude possible?", "Can it be final shelter?"], [
        ["New gadget unboxing", "", "", ""],
        ["Family meal together", "", "", ""],
        ["Holy name / prayer", "", "", ""],
        ["Winning an argument", "", "", ""],
        ["Quiet service help", "", "", ""],
    ])
    add_write_lines(document, ["One sentence: temporary tools vs lasting shelter:"], 2)


def o03(document) -> None:
    add_printable_title(document, "O03", "Statement Sort", "ALIGNED / SHAMING / MIXED.")
    add_card_grid(document, [
        "Temporary joys can be used with gratitude.",
        "Family affection is worthless.",
        "Ask temporary things to give permanent fulfillment.",
        "Offer ordinary acts to Kṛṣṇa (BG 9.27 support).",
        "Sense-contact pleasures are temporary (BG 5.22 support).",
        "If you enjoy a birthday you failed spiritually.",
    ])
    add_cut_lines(document)
    add_teacher_page(document, "O03 Key", [
        ["1", "ALIGNED"], ["2", "SHAMING"], ["3", "MISTAKEN shelter"],
        ["4", "ALIGNED"], ["5", "ALIGNED support"], ["6", "SHAMING"],
    ])


def o04(document) -> None:
    add_printable_title(document, "O04", "Comfort vs Meaning Scenarios", "Seven fields.")
    add_card_grid(document, [
        "A: Purchase chase never ends",
        "B: Parent shames child's toy",
        "C: Work forever defeats prayer cue",
    ], per_page=3)
    add_write_lines(document, ["Card A notes", "Card B notes", "Card C notes"], 2)
    add_teacher_only_divider(document, "Gratitude pause; no depression claims; protect one cue.")


def o05(document) -> None:
    add_printable_title(document, "O05", "Temporary vs Lasting Diagram", "Label both sides; keep enjoyment without contempt.")
    _img(document, "temporary-lasting.png", 5.0)
    add_write_lines(document, ["Offering line I will try:", "Joy I will thank without shaming:"], 1)


def o06(document) -> None:
    add_printable_title(document, "O06", "Exit Ticket", "Before reunification.")
    add_write_lines(document, [
        "Memory phrase:",
        "One gratitude act:",
        "Project sentence — How can enjoyment become gratitude and service?",
    ], 1)


def p01(document) -> None:
    add_printable_title(document, "P01", "Private Reflection", "Comfort vs meaning — private.")
    _img(document, "parent-icon.png", 3.2)
    add_callout(document, "SAFETY_PRIVACY", "No forced share. No mental-health diagnosis in room.")
    add_write_lines(document, ["Where do we ask temporary comfort to do a permanent job?"], 6)


def p02(document) -> None:
    add_printable_title(document, "P02", "Comfort / Meaning Card Sort", "TOOL / LASTING / REPAIR.")
    add_card_grid(document, [
        "TOOL: Birthday cake enjoyed with thanks",
        "LASTING: Family prayer after dinner",
        "REPAIR: Calling a child's joy māyā to shame",
        "LASTING: Offering work as service (modestly)",
        "REPAIR: Pretending family hugs are worthless",
        "TOOL: Lawful recreation with a time boundary",
    ])
    add_cut_lines(document)
    add_teacher_page(document, "P02 Key", [["Tool/Lasting", "1, 2, 4, 6"], ["Needs repair", "3, 5"]])


def p03(document) -> None:
    add_printable_title(document, "P03", "Substantial Family Case", "Constructed fictional case.")
    add_callout(document, "FAMILY_APPLICATION",
                "A parent shames a child's toy as māyā. The child goes quiet. Restore gratitude without making the toy the shelter.")
    add_write_lines(document, ["Mistaken conclusion", "Principle from BG 8.15",
                               "Compassionate response", "Practical action", "What not to say"], 1)


def p04(document) -> None:
    add_printable_title(document, "P04", "Household Operating Application", "Gratitude + service.")
    add_write_lines(document, ["When we enjoy ___, we will:", "and we will not:"], 2)


def p05(document) -> None:
    add_printable_title(document, "P05", "Private Next-Step Saṅkalpa", "Private.")
    add_callout(document, "HOME_PRACTICE", "One gratitude pause + one service act this week.")
    add_write_lines(document, ["My private next step:"], 3)


YOUNGER_BUILDERS = [y01, y02, y03, y04, y05]
OLDER_BUILDERS = [o01, o02, o03, o04, o05, o06]
PARENT_BUILDERS = [p01, p02, p03, p04, p05]
FAMILY_BUILDERS = []

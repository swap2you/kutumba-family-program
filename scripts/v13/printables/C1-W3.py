#!/usr/bin/env python3
"""C1-W3 printable Word builders — real tables/images, no ASCII final art."""
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

MEMORY = "I am an eternal soul — conscious, individual, and meant for Kṛṣṇa's service."
ASSETS = REPO / "11-weekly-program-library/first-six-months/c1-w3-the-nature-of-the-soul/visuals/v13"


def _img(document, name: str, width: float = 2.4) -> None:
    path = ASSETS / name
    if path.is_file():
        document.add_picture(str(path), width=Inches(width))


def y01(document) -> None:
    add_printable_title(document, "Y01", "Soul Is / Is-Not Cards", "Sort into SOUL IS vs SOUL IS NOT.")
    add_card_grid(document, [
        "IS: Eternal", "IS: Conscious", "IS: Meant to serve Kṛṣṇa",
        "IS NOT: The temporary body", "IS NOT: God Himself", "IS NOT: A spark equal to the whole sun",
    ])
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)


def y02(document) -> None:
    add_printable_title(document, "Y02", "Spark and Sun Match", "Same light-nature — not the whole sun.")
    _img(document, "spark-sun.png", 5.0)
    add_callout(document, "TEACHER_NOTE", "If a child says I am God, smile and correct: dear spark who serves.")
    add_cut_lines(document)


def y03(document) -> None:
    add_printable_title(document, "Y03", "Spark-Service Cue Craft", "Care act + service act on the card.")
    _img(document, "spark-service-card.png", 4.5)
    add_write_lines(document, ["My care act:", "My service act:"], 1)
    add_memory_phrase_block(document, MEMORY)


def y04(document) -> None:
    add_printable_title(document, "Y04", "Care-as-Service Cards", "Sort CARE HELPS SERVICE vs BODY NEGLECT.")
    add_card_grid(document, [
        "CARE: Sleep so I can serve", "CARE: Drink water", "CARE: Brush teeth",
        "NEGLECT: Ignore rest because soul", "NEGLECT: Body is trash", "NEGLECT: Skip hygiene to look spiritual",
    ])
    add_cut_lines(document)


def y05(document) -> None:
    add_printable_title(document, "Y05", "Memory Phrase Mat", "Landing mat for Spark-and-Serve.")
    _img(document, "memory-mat.png", 5.0)
    add_memory_phrase_block(document, MEMORY)


def o01(document) -> None:
    add_printable_title(document, "O01", "BG 2.20 Observation", "Underline never born / never dies / not destroyed with the body.")
    add_callout(document, "SASTRA", "BG 2.20 — https://vedabase.io/en/library/bg/2/20/")
    add_write_lines(document, [
        "What does the verse say happens to the soul when the body is destroyed?",
        "List two attributes of the soul from tonight's teaching.",
        "What must we NOT claim about science tonight?",
        "Paraphrase the KUTUMBA teaching meaning in one sentence.",
    ], 1)


def o02(document) -> None:
    add_printable_title(document, "O02", "Soul Attributes Grid", "Fill IS attributes and IS NOT column.")
    add_branded_table(document, ["Attribute", "Means in kid/teen words", "Is NOT"], [
        ["Eternal", "", "Created at birth"],
        ["Conscious", "", "A rock"],
        ["Individual", "", "Merged into Godhood"],
        ["Minute / fragmental", "", "The Supreme"],
        ["Related in service", "", "Independent God"],
    ])
    add_callout(document, "DO_NOT_SPECULATE", "Science is N/A as proof of the soul this week.")


def o03(document) -> None:
    add_printable_title(document, "O03", "Identity Statement Sort", "ALIGNED / MISTAKEN / MIXED.")
    add_card_grid(document, [
        "I am God.",
        "I am an eternal soul meant to serve Kṛṣṇa.",
        "My grades are the whole me.",
        "I care for my body so I can serve.",
        "Labs proved there is no soul.",
        "When I fail a test I am worthless.",
    ])
    add_cut_lines(document)
    add_teacher_page(document, "O03 Key", [
        ["1", "MISTAKEN Godhood"], ["2", "ALIGNED"], ["3", "MISTAKEN outcome=self"],
        ["4", "ALIGNED"], ["5", "MISTAKEN science proof"], ["6", "MISTAKEN"],
    ])


def o04(document) -> None:
    add_printable_title(document, "O04", "Success/Failure Scenarios", "Seven fields: situation through what not to say.")
    add_card_grid(document, [
        "A: Win trophy — I am God now",
        "B: Fail test — I am nothing",
        "C: Neglect hygiene because soul",
    ], per_page=3)
    add_write_lines(document, ["Card A notes", "Card B notes", "Card C notes"], 2)
    add_teacher_only_divider(document, "Correct Godhood gently; restore care; refuse lab-proof fights.")


def o05(document) -> None:
    add_printable_title(document, "O05", "Jīva Is / Is-Not Diagram", "Label IS and IS NOT zones.")
    _img(document, "jiva-is-is-not.png", 5.0)
    add_write_lines(document, ["One service arrow means:", "One care arrow means:"], 1)


def o06(document) -> None:
    add_printable_title(document, "O06", "Exit Ticket", "Before reunification.")
    add_write_lines(document, [
        "Memory phrase:",
        "One service act I will try:",
        "One care act I will keep:",
        "Project sentence — If I am a soul, how should I live?",
    ], 1)


def p01(document) -> None:
    add_printable_title(document, "P01", "Private Reflection", "Identity under success/failure — private.")
    _img(document, "parent-icon.png", 3.2)
    add_callout(document, "SAFETY_PRIVACY", "No forced share. Do not collect sheets into public folders.")
    add_write_lines(document, ["Where do wins/losses quietly become the whole self at home?"], 6)


def p02(document) -> None:
    add_printable_title(document, "P02", "Identity Language Card Sort", "RESPECTFUL vs NEEDS REPAIR.")
    add_card_grid(document, [
        "You are a soul who serves — win or lose.",
        "You are God when you succeed.",
        "Your worth is this grade.",
        "We care for the body as service readiness.",
        "Science disproved the soul — stop talking.",
        "Let's verify from śāstra; I won't guess.",
    ])
    add_cut_lines(document)
    add_teacher_page(document, "P02 Key", [["Respectful", "1, 4, 6"], ["Needs repair", "2, 3, 5"]])


def p03(document) -> None:
    add_printable_title(document, "P03", "Substantial Family Case", "Constructed fictional case.")
    add_callout(document, "FAMILY_APPLICATION",
                "After a win, a child says I am God. A parent freezes. Guests laugh.")
    add_write_lines(document, ["Mistaken conclusion", "Principle from BG 2.20 / BG 15.7",
                               "Compassionate response", "Practical action", "What not to say"], 1)


def p04(document) -> None:
    add_printable_title(document, "P04", "Household Operating Application", "One operating line.")
    add_write_lines(document, ["When outcomes spike, we will:", "instead of:"], 2)


def p05(document) -> None:
    add_printable_title(document, "P05", "Private Next-Step Saṅkalpa", "Private — not ranked.")
    add_callout(document, "HOME_PRACTICE", "This week I will connect eternal identity to one service act.")
    add_write_lines(document, ["My private next step:"], 3)


YOUNGER_BUILDERS = [y01, y02, y03, y04, y05]
OLDER_BUILDERS = [o01, o02, o03, o04, o05, o06]
PARENT_BUILDERS = [p01, p02, p03, p04, p05]
FAMILY_BUILDERS = []

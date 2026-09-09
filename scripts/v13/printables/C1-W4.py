#!/usr/bin/env python3
"""C1-W4 printable Word builders — real tables/images, no ASCII final art."""
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

MEMORY = "Human life is a rare chance to ask who I am and serve Kṛṣṇa."
ASSETS = REPO / "11-weekly-program-library/first-six-months/c1-w4-why-human-life-is-rare-and-valuable/visuals/v13"


def _img(document, name: str, width: float = 2.4) -> None:
    path = ASSETS / name
    if path.is_file():
        document.add_picture(str(path), width=Inches(width))


def y01(document) -> None:
    add_printable_title(document, "Y01", "Time-Gift Jar", "Place MUST tokens before OPTIONAL.")
    _img(document, "time-gift-jar.png", 4.5)
    add_card_grid(document, ["MUST: Story / prayer", "MUST: Help tidy", "MUST: Kind words",
                             "OPTIONAL: Extra screens", "OPTIONAL: More toys later", "OPTIONAL: Extra snacks"])
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)


def y02(document) -> None:
    add_printable_title(document, "Y02", "Must / Optional Sort", "Protect inquiry and kindness time.")
    add_card_grid(document, ["Picture: family prayer", "Picture: endless scrolling", "Picture: helping sibling",
                             "Picture: delayed chore forever", "Picture: short outdoor play", "Picture: all-night screens"])
    add_callout(document, "TEACHER_NOTE", "No death scare. Invitation language only.")
    add_cut_lines(document)


def y03(document) -> None:
    add_printable_title(document, "Y03", "Rare Ticket Craft", "Ask who I am + serve.")
    _img(document, "rare-ticket.png", 4.5)
    add_write_lines(document, ["I will protect this time gift:"], 2)
    add_memory_phrase_block(document, MEMORY)


def y04(document) -> None:
    add_printable_title(document, "Y04", "Kind Time-Speech Cards", "INVITATION vs FEAR.")
    add_card_grid(document, [
        "INVITE: Let's protect our story time.",
        "INVITE: Five minutes of holy name counts.",
        "INVITE: Human life is a chance to ask and serve.",
        "FEAR: Do this or something terrible.",
        "FEAR: Death is coming — panic!",
        "FEAR: You're wasting life forever.",
    ])
    add_cut_lines(document)


def y05(document) -> None:
    add_printable_title(document, "Y05", "Memory Phrase Mat", "Must-first landing.")
    _img(document, "memory-mat.png", 5.0)
    add_memory_phrase_block(document, MEMORY)


def o01(document) -> None:
    add_printable_title(document, "O01", "ŚB 11.9.29 Observation", "Rare · temporary · endeavor · ultimate good.")
    add_callout(document, "SASTRA", "ŚB 11.9.29 — https://vedabase.io/en/library/sb/11/9/29/")
    add_callout(document, "DO_NOT_SPECULATE", "If Mṛgāri is used: CC Madhya 24.229–282 — NOT ŚB.")
    add_write_lines(document, [
        "What is rare according to the teaching meaning?",
        "How do we teach urgency without fear?",
        "Where is Mṛgāri sourced if used?",
        "Paraphrase ŚB 11.9.29 in one sentence.",
    ], 1)


def o02(document) -> None:
    add_printable_title(document, "O02", "Priority / Time-Budget Challenge", "Protect one inquiry slot.")
    add_branded_table(document, ["Block", "Minutes", "Must / Should / Optional", "Why"], [
        ["Dinner", "30", "", ""],
        ["Screens", "45", "", ""],
        ["Inquiry / practice", "15", "", ""],
        ["Homework", "40", "", ""],
        ["Free play", "20", "", ""],
    ])
    add_write_lines(document, ["Which Must will we protect first this week?"], 2)


def o03(document) -> None:
    add_printable_title(document, "O03", "Opportunity Statement Sort", "ALIGNED / FEAR / MIXED.")
    add_card_grid(document, [
        "Human life is a chance to ask who I am.",
        "Scare children with death to force sādhana.",
        "Five sincere minutes are not lost (BG 2.40 support).",
        "Species contempt makes us spiritual.",
        "Protect a Must jar slot before Optional screens.",
        "If you miss one night you are doomed.",
    ])
    add_cut_lines(document)
    add_teacher_page(document, "O03 Key", [
        ["1", "ALIGNED"], ["2", "FEAR"], ["3", "ALIGNED"], ["4", "MISTAKEN"], ["5", "ALIGNED"], ["6", "FEAR"],
    ])


def o04(document) -> None:
    add_printable_title(document, "O04", "Busy Family Scenarios", "Seven fields.")
    add_card_grid(document, [
        "A: Screens eat the only quiet block",
        "B: Parent uses death scare",
        "C: Service opportunity vs sports overtime",
    ], per_page=3)
    add_write_lines(document, ["Card A notes", "Card B notes", "Card C notes"], 2)
    add_teacher_only_divider(document, "Invitation not panic; Mṛgāri = Madhya 24 if used.")


def o05(document) -> None:
    add_printable_title(document, "O05", "Time-Budget Diagram", "Must before Optional.")
    _img(document, "time-budget-diagram.png", 5.0)
    add_write_lines(document, ["Our family Must slot:", "Mercy note (not panic):"], 1)


def o06(document) -> None:
    add_printable_title(document, "O06", "Exit Ticket", "Before reunification.")
    add_write_lines(document, [
        "Memory phrase:",
        "One protected-time act:",
        "Project sentence — What deserves protected family time?",
    ], 1)


def p01(document) -> None:
    add_printable_title(document, "P01", "Private Reflection", "Schedule truth — private.")
    _img(document, "parent-icon.png", 3.2)
    add_callout(document, "SAFETY_PRIVACY", "No forced share.")
    add_write_lines(document, ["Where does the only quiet block disappear?"], 6)


def p02(document) -> None:
    add_printable_title(document, "P02", "Schedule Audit Card Sort", "PROTECT / DELAY / DROP.")
    add_card_grid(document, [
        "PROTECT: 10-minute memory + verse paraphrase",
        "PROTECT: Family prayer before screens",
        "DELAY: Extra scrolling",
        "DROP: Third optional show",
        "PROTECT: One service chore together",
        "DELAY: Non-urgent shopping browse",
    ])
    add_cut_lines(document)
    add_teacher_page(document, "P02 Key", [["Protect examples", "1, 2, 5"], ["Delay/Drop", "3, 4, 6"]])


def p03(document) -> None:
    add_printable_title(document, "P03", "Substantial Family Case", "Constructed fictional case.")
    add_callout(document, "FAMILY_APPLICATION",
                "Screens consume the quiet block. A parent threatens with death-fear. Rewrite as invitation.")
    add_callout(document, "SASTRA", "Mṛgāri if mentioned: CC Madhya 24.229–282 — not ŚB.")
    add_write_lines(document, ["Mistaken conclusion", "Principle from ŚB 11.9.29",
                               "Compassionate response", "Practical action", "What not to say"], 1)


def p04(document) -> None:
    add_printable_title(document, "P04", "Household Operating Application", "Must before Optional.")
    add_write_lines(document, ["When the evening opens, we will place this Must first:", "instead of:"], 2)


def p05(document) -> None:
    add_printable_title(document, "P05", "Private Next-Step Saṅkalpa", "Private.")
    add_callout(document, "HOME_PRACTICE", "Protect one inquiry/practice slot this week.")
    add_write_lines(document, ["My private next step:"], 3)


YOUNGER_BUILDERS = [y01, y02, y03, y04, y05]
OLDER_BUILDERS = [o01, o02, o03, o04, o05, o06]
PARENT_BUILDERS = [p01, p02, p03, p04, p05]
FAMILY_BUILDERS = []

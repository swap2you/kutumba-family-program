#!/usr/bin/env python3
"""C1-W6 printable Word builders — real tables/images, no ASCII final art."""
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

MEMORY = "Who am I, and how should our family live?"
ASSETS = REPO / "11-weekly-program-library/first-six-months/c1-w6-integration-night-who-am-i-and-how-should-our-family-live/visuals/v13"


def _img(document, name: str, width: float = 2.4) -> None:
    path = ASSETS / name
    if path.is_file():
        document.add_picture(str(path), width=Inches(width))


def y01(document) -> None:
    add_printable_title(document, "Y01", "Cycle Bead Recall", "Touch W1–W5 beads — mercy, not quiz.")
    _img(document, "integration-necklace.png", 5.0)
    add_card_grid(document, ["W1 Hear/serve", "W2 Body≠only-self", "W3 Eternal soul",
                             "W4 Rare chance", "W5 Lasting shelter", "Helper: drawings count"])
    add_memory_phrase_block(document, MEMORY)
    add_cut_lines(document)


def y02(document) -> None:
    add_printable_title(document, "Y02", "Artifact Share Practice", "Show a drawing up to 1 minute.")
    _img(document, "family-share-card.png", 4.5)
    add_write_lines(document, ["My helper sentence:"], 2)
    add_callout(document, "TEACHER_NOTE", "Noncompetitive. Whispered shares count.")


def y03(document) -> None:
    add_printable_title(document, "Y03", "Family Sentence Craft", "Who am I, and how should our family live?")
    add_write_lines(document, ["Draw or write our family sentence:"], 4)
    add_memory_phrase_block(document, MEMORY)


def y04(document) -> None:
    add_printable_title(document, "Y04", "Kind Listener Cards", "KIND LISTEN vs RANKING.")
    add_card_grid(document, [
        "KIND: Eyes on the speaker",
        "KIND: Clap for effort",
        "KIND: Help a shy friend",
        "RANK: Who was best?",
        "RANK: You forgot — fail",
        "RANK: Louder is holier",
    ])
    add_cut_lines(document)


def y05(document) -> None:
    add_printable_title(document, "Y05", "Memory Phrase Mat", "Integration landing.")
    _img(document, "memory-mat.png", 5.0)
    add_memory_phrase_block(document, MEMORY)


def o01(document) -> None:
    add_printable_title(document, "O01", "Cycle 1 Chain Retrieval", "Retrieve W1–W5 — open-notes mercy OK.")
    add_branded_table(document, ["Week", "Primary", "One-sentence meaning"], [
        ["W1", "ŚB 1.2.18", ""],
        ["W2", "BG 2.13", ""],
        ["W3", "BG 2.20", ""],
        ["W4", "ŚB 11.9.29", ""],
        ["W5", "BG 8.15", ""],
    ])
    add_callout(document, "KEY_IDEA", "No major new doctrine tonight.")


def o02(document) -> None:
    add_printable_title(document, "O02", "Misconception Clinic", "Repair Cycle 1 errors with sources.")
    add_card_grid(document, [
        "Photos prove the soul",
        "I am God",
        "Scare kids with death for sādhana",
        "Family affection is worthless",
        "Rank families by presentation polish",
        "Mṛgāri is in ŚB 6.x",
    ])
    add_write_lines(document, ["Repair lines (with source pointers):"], 4)
    add_teacher_page(document, "O02 Key", [
        ["1", "Pedagogy ≠ proof — BG 2.13"],
        ["2", "Fragmental part — BG 15.7 / BG 2.20"],
        ["3", "Invitation — ŚB 11.9.29"],
        ["4", "Use with gratitude — BG 8.15"],
        ["5", "Noncompetitive integration"],
        ["6", "CC Madhya 24.229–282"],
    ])


def o03(document) -> None:
    add_printable_title(document, "O03", "Family Presentation Outline", "≤10 minutes · noncompetitive.")
    add_write_lines(document, [
        "Who we are (identity):",
        "How we live (practice):",
        "One source we remember:",
        "One home act:",
    ], 2)
    add_callout(document, "TIME_CUE", "Four families × up to 10 minutes.")


def o04(document) -> None:
    add_printable_title(document, "O04", "Team Coaching Scenarios", "Mercy without ranking.")
    add_card_grid(document, [
        "A: Shy family — drawing only",
        "B: Share runs long past 10 min",
        "C: Family missed two weeks",
    ], per_page=3)
    add_write_lines(document, ["Card A notes", "Card B notes", "Card C notes"], 2)
    add_teacher_only_divider(document, "Retrieval is mercy; incomplete is welcome; no scoreboard.")


def o05(document) -> None:
    add_printable_title(document, "O05", "Integration Necklace Map", "Five beads + living sentence.")
    _img(document, "integration-necklace.png", 5.0)
    add_write_lines(document, ["Center living sentence:"], 2)


def o06(document) -> None:
    add_printable_title(document, "O06", "Exit Ticket", "Before close.")
    add_write_lines(document, [
        "Memory phrase:",
        "One home living act:",
        "One thanks to another family (no ranking):",
    ], 1)


def p01(document) -> None:
    add_printable_title(document, "P01", "Private Reflection", "Coherent family life — private.")
    _img(document, "parent-icon.png", 3.2)
    add_callout(document, "SAFETY_PRIVACY", "No forced share. No ranking.")
    add_write_lines(document, ["One coherent line connecting identity and household practice:"], 6)


def p02(document) -> None:
    add_printable_title(document, "P02", "Presentation Coaching Sort", "SUPPORT vs RANKING.")
    add_card_grid(document, [
        "SUPPORT: Drawings count",
        "SUPPORT: Whispered sentences count",
        "SUPPORT: Keep to 10 minutes kindly",
        "RANK: Score the best family",
        "RANK: Loud brilliance is holier",
        "RANK: Announce who is behind",
    ])
    add_cut_lines(document)
    add_teacher_page(document, "P02 Key", [["Support", "1, 2, 3"], ["Ranking — reject", "4, 5, 6"]])


def p03(document) -> None:
    add_printable_title(document, "P03", "Substantial Family Case", "Four families share night.")
    add_callout(document, "FAMILY_APPLICATION",
                "Four families × 10 min. One incomplete. One runs long. Keep noncompetitive mercy.")
    add_callout(document, "TIME_CUE", "Soft time cues; no scoreboard.")
    add_write_lines(document, ["Mistaken conclusion", "Principle (integration)",
                               "Compassionate response", "Practical action", "What not to say"], 1)


def p04(document) -> None:
    add_printable_title(document, "P04", "Household Operating Application", "Cycle 1 living line.")
    add_write_lines(document, ["Our family's Cycle 1 living line is:"], 3)


def p05(document) -> None:
    add_printable_title(document, "P05", "Private Next-Step Saṅkalpa", "Into Utsava / continued practice.")
    add_callout(document, "HOME_PRACTICE", "Private next step — still no ranking.")
    add_write_lines(document, ["My private next step:"], 3)


YOUNGER_BUILDERS = [y01, y02, y03, y04, y05]
OLDER_BUILDERS = [o01, o02, o03, o04, o05, o06]
PARENT_BUILDERS = [p01, p02, p03, p04, p05]
FAMILY_BUILDERS = []

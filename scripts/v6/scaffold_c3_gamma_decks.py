#!/usr/bin/env python3
"""Convert C3 outline gamma stubs into validator-compliant card structure."""
from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

CARD_TEMPLATE = """### Card {n} — {title}

**Content:**  
{content}

**Visual:** `[IMAGE: {visual} — KUTUMBA placeholder; congregation-owned art preferred]`
**Speaker note:** {note}
**Source:** module pack — link-only scripture references; no invented purport quotes
**Rights:** KUTUMBA-original slide text; scripture via Vedabase links only

---
"""

KISORA_OUTLINES: dict[str, list[tuple[str, str]]] = {
    "c3-w1": [
        ("Title", "C3-W1 youth track — Who Is God? Supreme enjoyer, proprietor, and friend."),
        ("Essential question", "Who is the supreme enjoyer of all sacrifices, and how does that change family life?"),
        ("Bhagavad-gītā 5.29", "Reference BG 5.29 via Vedabase link — paraphrase only; discuss supreme proprietor theme."),
        ("Kathā connection", "Connect to prem-ki-katha narrative beat — one personality, one devotional tension."),
        ("Concept map preview", "Preview module concept map: enjoyer, proprietor, well-wishing friend."),
        ("Case CS-01", "Anonymized youth case from CONTEMPORARY-APPLICATIONS.md — compassionate response."),
        ("Misconception vs truth", "Contrast material enjoyment as goal vs Kṛṣṇa as supreme enjoyer."),
        ("Home practice choice", "Each youth chooses one realistic home practice step for the week."),
        ("Source verification habit", "Demonstrate checking one claim against Vedabase before sharing."),
        ("Close", "One commitment — name one way the family will remember Kṛṣṇa as friend this week."),
    ],
    "c3-w2": [
        ("Title", "C3-W2 youth track — Who is Kṛṣṇa, the Supreme Personality of Godhead?"),
        ("Essential question", "What distinguishes Kṛṣṇa from ordinary powerful beings or cultural ideas of God?"),
        ("Śrīmad-Bhāgavatam reference", "Link SB 1.3.28 via Vedabase — paraphrase Kṛṣṇa as source of all avatāras."),
        ("Kathā connection", "One beat from prem-ki-katha — focus on personal form and reciprocation."),
        ("Concept map preview", "Supreme person, not impersonal force — module vocabulary preview."),
        ("Case CS-01", "Youth case: mistaken impersonal conclusion — gentle correction pathway."),
        ("Misconception vs truth", "Impersonalism vs personal Bhagavān — age-appropriate framing."),
        ("Home practice choice", "Choose one name or quality of Kṛṣṇa to remember daily."),
        ("Source verification habit", "Verify one verse reference before presenting to family."),
        ("Close", "Commitment — one respectful question to bring next week."),
    ],
    "c3-w3": [
        ("Title", "C3-W3 youth track — Guru, sādhu, and śāstra."),
        ("Essential question", "How do we receive spiritual knowledge without speculation or blind following?"),
        ("CC Madhya reference", "Link CC Madhya 17.186 via Vedabase — threefold authority principle."),
        ("Kathā connection", "Connect kathā beat on receiving knowledge through disciplic succession."),
        ("Concept map preview", "Guru, sādhu, śāstra alignment — module map preview."),
        ("Case CS-01", "Case: conflicting online teaching — how to check against śāstra."),
        ("Misconception vs truth", "Guru as order-giver for Kṛṣṇa vs personality cult."),
        ("Home practice choice", "One question to ask a trusted senior devotee this week."),
        ("Source verification habit", "Practice tracing one claim to śāstra link."),
        ("Close", "Commitment — read one verse with parents before next session."),
    ],
    "c3-w4": [
        ("Title", "C3-W4 youth track — Śrī Caitanya Mahāprabhu and the holy name."),
        ("Essential question", "Why is the holy name central in this age, and who exemplified that?"),
        ("CC Ādi reference", "Link CC Ādi 17.21 via Vedabase — mahā-mantra mercy teaching."),
        ("Kathā connection", "One Mahāprabhu līlā beat from prem-ki-katha — no invented dialogue."),
        ("Concept map preview", "Saṅkīrtana movement — name, form, and mood preview."),
        ("Case CS-01", "Case: embarrassment chanting publicly — compassionate framing."),
        ("Misconception vs truth", "Mechanical chanting vs attentive remembrance."),
        ("Home practice choice", "Choose one realistic japa or kīrtana step at home."),
        ("Source verification habit", "Verify one Caitanya-caritāmṛta reference before sharing."),
        ("Close", "Commitment — one kīrtana or japa minute with family."),
    ],
    "c3-w5": [
        ("Title", "C3-W5 youth track — The nine processes of bhakti."),
        ("Essential question", "Which devotional processes can a family practice together this week?"),
        ("SB 7.5.23–24 reference", "Link SB 7.5.23–24 via Vedabase — Prahlāda's nine processes list."),
        ("Kathā connection", "One Prahlāda beat from prem-ki-katha — courage and devotion."),
        ("Concept map preview", "Nine processes map — hearing, chanting, remembering preview."),
        ("Case CS-01", "Case: picking one process when schedule is busy — realistic choice."),
        ("Misconception vs truth", "Checklist bhakti vs heartfelt practice with guidance."),
        ("Home practice choice", "Choose one of the nine processes for family home practice."),
        ("Source verification habit", "Verify Prahlāda verses before teaching younger siblings."),
        ("Close", "Commitment — demonstrate one process at Bhakti Mela prep."),
    ],
    "c3-w6": [
        ("Title", "C3-W6 youth track — Bhakti Mela integration and family presentation."),
        ("Essential question", "How do we offer what we learned without performance pressure?"),
        ("SB 7.5.23–24 review", "Brief review link — nine processes as offering framework."),
        ("Kathā connection", "Integration recollection — Cycle 3 themes, not new principal līlā."),
        ("Concept map preview", "Bhakti Mela flow — kīrtana, drama, family presentation roles."),
        ("Case CS-01", "Case: stage anxiety — safeguarding and encouragement boundaries."),
        ("Misconception vs truth", "Showmanship vs humble offering for Kṛṣṇa's pleasure."),
        ("Home practice choice", "Rehearsal step — one realistic practice before Mela night."),
        ("Source verification habit", "Final citation check on presentation script claims."),
        ("Close", "Commitment — one gratitude offering after Mela (no personal data in Git)."),
    ],
}


def scaffold_kisora(module_dir: Path, module_key: str) -> None:
    rel = "gamma/GAMMA-KISORA-KISORI-DECK-PROMPT.md"
    path = module_dir / rel
    text = path.read_text(encoding="utf-8")
    if "### Card 1" in text:
        return
    outline = KISORA_OUTLINES.get(module_key)
    if not outline:
        return
    mid = module_dir.name.split("-")[0].upper() + "-" + module_dir.name.split("-")[1].upper()
    lines = [
        f"# Gamma Prompt — {mid} Kiśora–Kiśorī Deck",
        "",
        "## Deck identity",
        "",
        f"- **Module:** {mid}",
        "- **Audience:** Kiśora–Kiśorī",
        "- **Status:** structural scaffold — human deepening required before pilot",
        "",
        "## Card plan",
        "",
    ]
    for i, (title, content) in enumerate(outline, 1):
        lines.append(
            CARD_TEMPLATE.format(
                n=i,
                title=title,
                content=content,
                visual=title.lower(),
                note=f"Deliver {title.lower()} for {mid}; keep discussion respectful and source-linked.",
            ).rstrip()
        )
        lines.append("")
    path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def enrich_lala(module_dir: Path) -> None:
    path = module_dir / "gamma/GAMMA-LALA-LALI-DECK-PROMPT.md"
    text = path.read_text(encoding="utf-8")
    if "**Speaker note:**" in text:
        return
    parts = re.split(r"(### Card \d+.*?\n)", text)
    if len(parts) < 2:
        return
    out = [parts[0]]
    for i in range(1, len(parts), 2):
        header = parts[i]
        body = parts[i + 1] if i + 1 < len(parts) else ""
        if "**Speaker note:**" not in body:
            body = re.sub(
                r"(\*\*Visual:\*\*[^\n]+\n)",
                r"\1**Speaker note:** Age-appropriate delivery; link-only scripture; no invented quotes.\n"
                r"**Source:** module pack\n"
                r"**Rights:** KUTUMBA-original; scripture links only\n",
                body,
                count=1,
            )
        out.append(header + body)
    path.write_text("".join(out), encoding="utf-8")


def expand_short_lala_content(module_dir: Path) -> None:
    path = module_dir / "gamma/GAMMA-LALA-LALI-DECK-PROMPT.md"
    text = path.read_text(encoding="utf-8")
    replacements = {
        "**Content:** Story time!": "**Content:** Story time — one beat from prem-ki-katha, under two minutes.",
        "**Content:** Wonder question": "**Content:** Wonder question — invite children to notice who enjoys family offerings.",
        "**Content:** Movement game": "**Content:** Movement game — simple gesture for remembering Kṛṣṇa as friend.",
        "**Content:** Kind action at home": "**Content:** Kind action at home — one gentle service the child can offer this week.",
        "**Content:** Draw or craft": "**Content:** Draw or craft — simple altar art; congregation-owned images preferred.",
        "**Content:** Recall together": "**Content:** Recall together — repeat the module memory line with parents.",
        "**Content:** Thank Kṛṣṇa": "**Content:** Thank Kṛṣṇa — brief prayer of gratitude before prasādam.",
        "**Content:** See you next week!": "**Content:** See you next week — preview one home practice step for parents.",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    for d in sorted(WEEKLY.glob("c3-w*")):
        key = "-".join(d.name.split("-")[:2])
        scaffold_kisora(d, key)
        enrich_lala(d)
        expand_short_lala_content(d)
    print("C3 gamma scaffolds updated")


if __name__ == "__main__":
    main()

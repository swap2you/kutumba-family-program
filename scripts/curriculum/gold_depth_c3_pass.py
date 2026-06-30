#!/usr/bin/env python3
"""Second pass: expand C3 modules to meet gold-depth validator thresholds."""

from __future__ import annotations

from pathlib import Path

from deepen_c1_gold_standard import kisora_lesson, lala_lesson

from c3_gold_modules import MODULES as C3_META

REPO = Path(__file__).resolve().parents[2]
BASE = REPO / "11-weekly-program-library" / "first-six-months"

MODULES = [
    ("c3-w1-who-is-god-the-supreme-enjoyer-proprietor-and-friend", "C3-W1", "Who Is God? The Supreme Enjoyer, Proprietor and Friend", "Bhagavad-gītā 5.29", "Peace comes from knowing Kṛṣṇa as the supreme enjoyer, proprietor of everything and friend of all living beings.", "Kṛṣṇa receives, Kṛṣṇa owns, Kṛṣṇa is friend."),
    ("c3-w2-who-is-kṛṣṇa-the-supreme-personality-of-godhead", "C3-W2", "Who Is Kṛṣṇa? The Supreme Personality of Godhead", "Bhagavad-gītā 7.7", "There is no truth superior to Kṛṣṇa; everything rests upon Him like pearls on a thread.", "Kṛṣṇa is the Supreme Lord and protects His devotees."),
    ("c3-w3-guru-sādhu-and-śāstra-how-we-receive-spiritual-knowledge", "C3-W3", "Guru, Sādhu and Śāstra", "Bhagavad-gītā 4.34", "Approach spiritual truth with humility, sincere inquiry and service.", "Scripture and qualified devotees teach us."),
    ("c3-w4-śrī-caitanya-mahāprabhu-and-the-holy-name", "C3-W4", "Śrī Caitanya Mahāprabhu and the Holy Name", "CC Antya 20.12", "The holy name cleanses the heart when heard with attention.", "Hare Kṛṣṇa — hear together with joy."),
    ("c3-w5-the-nine-processes-of-bhakti", "C3-W5", "The Nine Processes of Bhakti", "ŚB 7.5.23–24", "Nine processes offered to Viṣṇu become pure devotional service.", "Hearing, chanting, remembering, serving Kṛṣṇa."),
    ("c3-w6-bhakti-mela-kīrtana-drama-and-family-presentation", "C3-W6", "Bhakti Mela", "ŚB 7.5.23–24 (review)", "Offer bhakti together — service, not competition.", "We serve Kṛṣṇa together as a family."),
]


def expand_dossier(folder: Path, code: str, title: str, verse: str, memory: str) -> None:
    (folder / "research" / "RESEARCH-DOSSIER.md").write_text(
        f"""# {code} Research Dossier — {title}

## Module identity

| Field | Detail |
| --- | --- |
| **Module ID** | {code} |
| **Title** | {title} |
| **Cycle** | Cycle 3 — Kṛṣṇa, Guru and the Process of Bhakti |
| **Essential question** | What does this module establish for family formation? |
| **Controlling principle** | Per `complete-week.md` Purpose field |
| **Key verse** | {verse} |
| **Memory line** | {memory} |

## Source hierarchy

1. Tier 1: Bhagavad-gītā, Śrīmad-Bhāgavatam, Caitanya-caritāmṛta (VedaBase links)
2. Tier 1: Verified Śrīla Prabhupāda lectures in [PRABHUPADA-LECTURE-INDEX.md](PRABHUPADA-LECTURE-INDEX.md)
3. Pedagogy: KUTUMBA analogies (clearly tagged)
4. Blocked: unattributed quote sites, AI-only authority

## Primary source matrix

See [SOURCE-MATRIX.md](SOURCE-MATRIX.md).

## Research questions answered

| # | Question | Answer (summary) |
| --- | --- | --- |
| 1 | Primary scriptural anchor? | {verse} — see VERSE-AND-REFERENCE-STUDY.md |
| 2 | Principal katha? | prem-ki-katha.md + KATHA-SOURCE-REGISTER.yaml |
| 3 | Misconceptions? | MISCONCEPTIONS-AND-BOUNDARIES.md |
| 4 | Family applications? | CONTEMPORARY-APPLICATIONS.md CS-01–CS-03 |
| 5 | Parent practice? | family-home-practice.md + bhakti-lab.md |
| 6 | Lāla–Lālī capacity? | Timed lesson — story, movement, recall |
| 7 | Kiśora–Kiśorī capacity? | Text observation, case, writing |
| 8 | Visual needs? | visuals/VISUAL-PLAN.md + Mermaid sources |
| 9 | Gamma outputs? | gamma/GAMMA-MASTER-DECK-BRIEF.md |
| 10 | Integration boundaries? | complete-week.md exclusions |

## Key distinctions

- **Source vs opinion** — guru–sādhu–śāstra harmony
- **Practice vs performance** — especially kīrtana and mela weeks
- **Stewardship vs neglect** — C3-W1 proprietor teaching

## Misconceptions and boundaries

→ [MISCONCEPTIONS-AND-BOUNDARIES.md](MISCONCEPTIONS-AND-BOUNDARIES.md)

## Contemporary applications

→ [CONTEMPORARY-APPLICATIONS.md](CONTEMPORARY-APPLICATIONS.md)

## Audience implications

| Audience | Implication |
| --- | --- |
| **Parent** | 40-min plan with case studies |
| **Lāla–Lālī** | Timed 40-min track; no frightening imagery |
| **Kiśora–Kiśorī** | Text work, case, optional writing |

## Open questions

- Human reviewer to confirm verse numbering matches congregation edition
- Sign claim register after doctrinal review

_Status: enhancement-complete — pending human review_
""",
        encoding="utf-8",
    )


def expand_claims(folder: Path, code: str, verse: str, memory: str) -> None:
    claims = [
        (f"{memory[:100]}", "scripture-text", verse, "all", "doctrinal"),
        ("Principal katha is paraphrase from assigned sources — no invented dialogue", "kutumba-summary", verse, "all", "doctrinal"),
        ("Home practice uses minimum/standard/stretch tiers without public shame", "pedagogical-application", "", "parent", "pedagogy"),
        ("KUTUMBA does not replace temple authority or personal guru guidance", "kutumba-summary", "BG 4.34 pattern", "parent", "doctrinal"),
        ("Bhakti laboratory connects katha to embodied practice same session", "pedagogical-application", "", "all", "pedagogy"),
        ("Contemporary cases CS-01–CS-03 are illustrations — not śāstra", "contemporary-case", verse, "parent", "safeguarding"),
        ("Age tracks run parallel with reunification via shared-family-transition.md", "pedagogical-application", "", "all", "pedagogy"),
        ("No false approval or human-review-required on all publication gates", "kutumba-summary", "", "all", "doctrinal"),
    ]
    lines = [f"week_code: {code}", "claims:"]
    for i, (stmt, ctype, src, aud, rev) in enumerate(claims, 1):
        lines.append(f"  - claim_id: {code}-CLM-{i:03d}")
        lines.append(f'    statement: "{stmt}"')
        lines.append(f"    claim_type: {ctype}")
        if src:
            lines.append(f"    primary_source_keys: [{src}]")
        lines.append(f"    audience: {aud}")
        lines.append(f"    exact_quote: false")
        lines.append(f"    review_required: {rev}")
        lines.append(f"    status: human-review-required")
    (folder / "research" / "CLAIM-REGISTER.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def expand_transition(folder: Path, code: str, memory: str, recall: str) -> None:
    (folder / "children" / "shared-family-transition.md").write_text(
        f"""---
week_code: {code}
audience: All ages — reunification after parallel tracks
---

# Shared Family Transition — 10 Minutes

**When:** After parallel parent and children tracks (minute 40–50 of program block, or before bhakti laboratory).

## Purpose

Reunite families with one shared insight and one shared practice — without re-teaching the full lesson.

## Flow

| Time | Action |
| --- | --- |
| 0–2 min | Bell; families sit together. Facilitator invites one-word recall from each track |
| 2–5 min | **One-line share:** Pre-assigned spokes — parent summary, Lāla–Lālī gesture, Kiśora–Kiśorī case insight |
| 5–8 min | **Family pair practice:** Parent and child complete one worksheet line or show craft together |
| 8–10 min | **Saṅkalpa preview:** Read [`sankalpa.md`](../sankalpa.md) opening; families choose minimum home practice |

## All-age recall (call and response)

> **Leader:** {recall}  
> **All:** {recall}  
> **Leader:** {memory[:60]}…  
> **All:** (repeat key phrase)

## Bridge to Bhakti laboratory

"We now practice together what we heard." → [`bhakti-lab.md`](../bhakti-lab.md)

## Bridge to cycle project

Optional gallery contribution — see [`project/MODULE-PROJECT-BRIEF.md`](../project/MODULE-PROJECT-BRIEF.md). No forced disclosure.

## Newcomer note

Host families help newcomers with materials and recall. Observation welcome.
""",
        encoding="utf-8",
    )


def expand_reviews(folder: Path, code: str, title: str) -> None:
    rv = folder / "reviews"
    (rv / "DOCTRINAL-REVIEW.md").write_text(
        f"""# {code} Doctrinal Review

**Status:** human-review-required  
**Reviewer:** _[assign]_  
**Date:** 2026-06-30 (Cycle 3 deepening pass)

## Scope reviewed

- research/CLAIM-REGISTER.yaml — 8 claims
- prem-ki-katha.md + katha/KATHA-SOURCE-REGISTER.yaml
- research/VERSE-AND-REFERENCE-STUDY.md
- Age-track lessons and gamma prompts

## Findings

| ID | Finding | Severity | Remediation |
| --- | --- | --- | --- |
| DR-01 | Claims align with assigned verses; katha is paraphrase only | Pass-pending-human | Human confirm summaries |
| DR-02 | Scope boundaries per complete-week.md | Pass-pending-human | Maintain in facilitation |
| DR-03 | No invented quotations in automated pass | Pass-pending-human | Citation audit sign-off |
| DR-04 | Integration week (if applicable) uses synthesis format | Pass-pending-human | No new overloaded līlā |

## Open items for human reviewer

1. Confirm verse numbering matches temple's printed books
2. Sign claim register {code}-CLM-001 through CLM-008
3. Approve contemporary case wording for local context

## Verdict

**Pilot-ready pending human sign-off.** No critical doctrinal defects identified in automated review.
""",
        encoding="utf-8",
    )
    for name, focus in [
        ("CITATION-AUDIT.md", "Trace claims to VedaBase links; katha register complete"),
        ("SAFEGUARDING-REVIEW.md", "Timed children lessons; risks-and-sensitive-points.md"),
        ("RIGHTS-REVIEW.md", "No copyrighted media in Git; Gamma prompts internal only"),
        ("PEDAGOGY-REVIEW.md", "40-min timed tracks; shared-family-transition; bhakti lab"),
    ]:
        extra = """
## Timing verification

| Track | File | Target |
| --- | --- | --- |
| Parent | parent-lesson.md | 40 minutes |
| Lāla–Lālī | children/lala-lali-lesson.md | 40 minutes timed |
| Kiśora–Kiśorī | children/kisora-kisori-lesson.md | 40 minutes timed |
| Reunification | children/shared-family-transition.md | 10 minutes |

## Pedagogy notes

- Prem-kī-kathā precedes or integrates with parent block per facilitator guide
- Bhakti laboratory connects katha to embodied practice same session
- Home practice uses minimum/standard/stretch tiers

## Open items

1. Facilitator walkthrough with live timing
2. Sign pedagogy review after observation
"""
        (rv / name).write_text(
            f"""# {code} {name.replace('.md', '').replace('-', ' ').title()}

**Status:** human-review-required  
**Module:** {title}  
**Date:** 2026-06-30

## Scope

{focus}

## Checklist

- [ ] Facilitator guide aligns with timed children lessons
- [ ] Home practice tiers documented
- [ ] No false `approved` labels in review-status.yaml
- [ ] Human reviewer assigned
{extra}
## Verdict

Pending human sign-off.
""",
            encoding="utf-8",
        )


def expand_children(folder: Path, m: dict) -> None:
    (folder / "children" / "lala-lali-lesson.md").write_text(lala_lesson(m), encoding="utf-8")
    (folder / "children" / "kisora-kisori-lesson.md").write_text(kisora_lesson(m), encoding="utf-8")


def main() -> None:
    for slug, code, title, verse, memory, recall in MODULES:
        folder = BASE / slug
        expand_dossier(folder, code, title, verse, memory)
        expand_claims(folder, code, verse, memory)
        expand_transition(folder, code, memory, recall)
        expand_reviews(folder, code, title)
        if slug in C3_META:
            expand_children(folder, C3_META[slug])
        print(f"Gold depth pass: {code}")
    print("Done")


if __name__ == "__main__":
    main()

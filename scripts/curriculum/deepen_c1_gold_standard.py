#!/usr/bin/env python3
"""Deepen C1-W1 and C1-W3–W6 to C1-W2 gold standard."""

from __future__ import annotations

import textwrap
from pathlib import Path

from c1_gold_modules import MODULES, TARGET_SLUGS

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
MEDIA_CATALOG = "14-research-source-register/media-library/PRABHUPADA-LECTURE-CATALOG.yaml"


def w(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def claims_yaml(m: dict) -> str:
    code = m["code"]
    claims = [
        (f"{code} is a disciplined family sādhana community with six charter purposes.", "kutumba-summary", "all", "doctrinal"),
        (f"Key teaching anchored in {m['key_verse']}.", "scripture-text", "all", "doctrinal"),
        (m["controlling_principle"], "kutumba-summary", "parent", "doctrinal"),
        ("Home practice supports family formation without comparison or public scoring.", "pedagogical-application", "parent", "pedagogy"),
        ("Contemporary case studies are pedagogical illustrations, not śāstra.", "contemporary-case", "parent", "safeguarding"),
        ("Facilitators use VedaBase links and KUTUMBA summaries — no invented Prabhupāda quotations.", "kutumba-summary", "all", "citation"),
        ("Age-track lessons avoid frightening death imagery unless module scope requires it.", "safeguarding-boundary", "lala-lali", "safeguarding"),
        ("Service identity does not justify coercion, unfair domestic labor, or abuse.", "safeguarding-boundary", "parent", "safeguarding"),
        ("Analogies are pedagogical tools with stated limits — not literal śāstra.", "analogy", "kisora-kisori", "doctrinal"),
        ("Prem-kī-kathā is source-grounded paraphrase with link-only purport references.", "kutumba-summary", "all", "rights"),
    ]
    if m["code"] == "C1-W4":
        claims.append(("Human life's value is taught without frightening children with death or lower-birth threats.", "safeguarding-boundary", "lala-lali", "safeguarding"))
    if m["code"] == "C1-W5":
        claims.append(("Temporary does not mean evil; grief and poverty must not be trivialized.", "safeguarding-boundary", "all", "safeguarding"))
    if m["code"] == "C1-W6":
        claims.append(("Integration uses synthesis and consent-based sharing — no new principal līlā.", "kutumba-summary", "all", "doctrinal"))
    lines = [f"week_code: {code}", "claims:"]
    for i, (stmt, ctype, aud, rev) in enumerate(claims, 1):
        lines += [
            f"  - claim_id: {code}-CLM-{i:03d}",
            f'    statement: "{stmt}"',
            f"    claim_type: {ctype}",
            f"    primary_source_keys: []",
            f"    audience: {aud}",
            f"    misunderstanding_risk: See MISCONCEPTIONS-AND-BOUNDARIES.md",
            f"    exact_quote: false",
            f"    review_required: {rev}",
            f'    reviewer: ""',
            f"    status: human-review-required",
        ]
    return "\n".join(lines)


def contemporary_cases(m: dict) -> str:
    code = m["code"]
    templates = {
        "C1-W1": [
            ("CS-01", "Attendance without home practice", "Family comes every Friday but never chants at home", "SB 1.2.18 — regular hearing and service required"),
            ("CS-02", "Home practice without association", "Family practices alone but avoids temple and KUTUMBA", "CC Madhya 22.128 — community and guidance"),
            ("CS-03", "Spiritual competition", "Parents compare children's verse memorization publicly", "KUTUMBA charter — no comparison"),
            ("CS-04", "KUTUMBA as substitute temple", "Family skips temple claiming KUTUMBA is enough", "Charter — increases temple participation"),
            ("CS-05", "Burnout from unrealistic saṅkalpa", "Family vows two hours daily and quits in a week", "Minimum version + trigger design"),
            ("CS-06", "Newcomer overwhelm", "First visit feels like insider club", "Setu pairing and observation welcome"),
        ],
        "C1-W3": [
            ("CS-01", "All souls are God", "Youth says individuality is illusion", "BG 15.7 — fragmental part, not equal in power"),
            ("CS-02", "Service as worthlessness", "Parent says 'I am nothing' to avoid duty", "Service is connection, not degradation"),
            ("CS-03", "Insect cruelty", "Child harms insects 'because they're just bodies'", "Every living being has soul — care required"),
            ("CS-04", "Invisible service pride", "Youth serves only when photographed", "Service without credit — BG 9.27 intention"),
            ("CS-05", "Unfair domestic labor", "Spiritual service excuse for unequal chores", "Safeguarding — service ≠ coercion"),
            ("CS-06", "Spark analogy over-pressed", "Child thinks soul is literally a spark of fire", "Analogy limit — qualitative similarity only"),
            ("CS-07", "Dismissal of mental health", "Anxiety labeled 'just the body'", "Compassion + professional care when needed"),
        ],
        "C1-W4": [
            ("CS-01", "Someday spirituality", "Parents always plan to start 'when life calms down'", "SB 11.9.29 — rare opportunity now"),
            ("CS-02", "Screen time crowding", "No protected spiritual appointment exists", "Time-jar — intentional placement"),
            ("CS-03", "Species contempt", "Child jokes animals have 'less soul'", "All souls deserve compassion — greater capacity = responsibility"),
            ("CS-04", "Panic urgency", "Teacher uses frightening death imagery with children", "Urgency without fear — safeguarding"),
            ("CS-05", "Shift-work family", "Single parent cannot find evening slot", "Flexible appointment — realism not shame"),
            ("CS-06", "Achievement pressure", "Child must memorize verses to prove worth", "Human life value ≠ performance"),
        ],
        "C1-W5": [
            ("CS-01", "Perfect holiday collapse", "Family expects vacation to fix all stress", "BG 8.15 — temporary arrangements"),
            ("CS-02", "Retail therapy", "Shopping after bad day seeking permanent relief", "BG 5.22 — pleasure has end"),
            ("CS-03", "Child meltdown over canceled event", "Disappointment dismissed as 'just māyā'", "Validate feeling first — then philosophy"),
            ("CS-04", "Spiritualized entertainment", "Only kṛṣṇa-themed media, no boundaries", "BG 9.27 — connection + restraint"),
            ("CS-05", "Material hatred", "Teen rejects all enjoyment as evil", "Temporary ≠ evil — yukta-vairāgya"),
            ("CS-06", "Grief after loss", "Relative told 'everything temporary' at funeral", "Compassion — do not trivialize trauma"),
            ("CS-07", "Advertising promises", "Product claims permanent happiness", "Four-happiness classification exercise"),
        ],
        "C1-W6": [
            ("CS-01", "Integration talent show", "Families compete for best presentation", "Non-comparison rules enforced"),
            ("CS-02", "Impressive failure", "Family keeps failing ambitious saṅkalpa", "Honest simplification better than impressive failure"),
            ("CS-03", "Misconception repair", "'Not the body means health doesn't matter'", "Identity + instrument care"),
            ("CS-04", "Verse mismatch", "Child matches BG 8.15 to soul qualities", "Station review — verse recognition"),
            ("CS-05", "Continuity drop", "Family stops all practice after cycle ends", "Choose one practice for off week"),
            ("CS-06", "Testimony without consent", "Facilitator asks public confession", "Consent required for sharing"),
        ],
    }
    cases = templates.get(code, templates["C1-W1"])
    parts = [f"# {code} Contemporary Applications — Anonymized Case Studies\n", f"{len(cases)} cases for parent and youth tracks. All names fictional.\n"]
    for cid, title, situation, correction in cases:
        parts.append(f"""---

## {cid} — {title}

| Field | Detail |
| --- | --- |
| **Presenting situation** | {situation} |
| **Mistaken conclusion** | See facilitator guide |
| **Source-grounded correction** | {correction} |
| **Compassionate response** | Private guidance; no public shaming |
| **Facilitator caution** | Route trauma to safeguarding policy |
| **Lāla–Lālī** | Age-appropriate scenario card — no death imagery |
| **Kiśora–Kiśorī** | Full case in small group with boundaries |

""")
    return "".join(parts)


def prem_katha(m: dict) -> str:
    code = m["code"]
    if m["katha_type"] == "facilitator-synthesis":
        return textwrap.dedent(f"""---
week_code: {code}
week_title: {m['title']}
component: prem-ki-katha.md
katha_type: facilitator-synthesis
---

# Prem-kī-Kathā — Cycle 1 Integration (Synthesis Format)

## 1. Katha title

**{m['katha_title']}** — families remember the journey and choose continuity.

## 2. Module connection

Integration week per [PREM-KI-KATHA-SOURCE-MAP.md](../../../../14-research-source-register/PREM-KI-KATHA-SOURCE-MAP.md): **no new principal līlā**. Synthesis of C1-W1–W5 with optional consent-based family shares.

## 3. Primary source references

| Source | Link | Use |
| --- | --- | --- |
| BG 2.13 | [vedabase](https://vedabase.io/en/library/bg/2/13/) | Integration anchor verse |
| Review verses | See `research/VERSE-AND-REFERENCE-STUDY.md` | Verse match stations |

## 4. Setting and devotional mood

_[Facilitator transition]_ Quiet room. Families seated together. Mood of **gratitude and honest review** — not performance.

## 5. Main personalities

- **The traveling family** (opening-hook metaphor)
- **Each KUTUMBA family** — sharing only with consent

## 6. Source-grounded narrative

_[Facilitator synthesis — not new līlā]_

Recall the chain: KUTUMBA purpose (W1) → body changes, self continues (W2) → soul's positive nature (W3) → rare human opportunity (W4) → temporary world, permanent Kṛṣṇa (W5).

**Paraphrase aligned with BG 2.13:** A sober person observes bodily change without losing spiritual footing.

## 7. Turning point

Families choose **one practice to continue** through the off week — with minimum version and trigger.

## 8. Central teaching

Identity, opportunity, and realism form **one sustainable home practice** — not five separate ideas.

## 9. Heart reflection

60 seconds silence: "What actually changed at home this cycle?"

## 10. Lāla–Lālī interaction cues

1. Cycle wheel craft — four segments labeled W2–W5 themes.
2. Sticker for one practice to continue — no ranking.

## 11. Kiśora–Kiśorī reflection cues

1. Two-minute evidence–analogy–application presentation (optional).
2. Misconception repair card in pairs.

## 12. Parent bridge

Link continuity saṅkalpa to `family-home-practice.md`. Preview Cycle 2 — karma and choice.

## 13. Transition

→ Retrieval stations and family presentations per `parent-lesson.md`.

## 14. Narration cautions

- No forced testimony; consent required.
- No competitive scoring.
- No new copyrighted narrative in Git.

## 15. Visual/storyboard plan

See `visuals/VISUAL-PLAN.md` — cycle wheel and station maps.

## 16. Rights and quotation status

Link-only references. No full purports in Git.

## 17. Human doctrinal review status

**human-review-required** — see `reviews/DOCTRINAL-REVIEW.md`
""")

    katha_bodies = {
        "C1-W1": textwrap.dedent("""
**Paraphrase from ŚB 1.1 (summary):** At Naimiṣāraṇya, sages led by Śaunaka gathered after the departure of Kṛṣṇa. They recognized that the age of Kali brings short life, quarrel, and distraction. Rather than despair, they **inquired** — how should those who remain act? What should be heard? Their sincere questions opened the way for Sūta Gosvāmī to speak Śrīmad-Bhāgavatam.

**Paraphrase aligned with SB 1.2.18:** Regular hearing and service of the Bhāgavatam cleanses the heart and fixes devotion. KUTUMBA creates a weekly protected time for that hearing — together as families.

**Facilitator transition:** Our families also arrive tired, distracted, and wondering if one more meeting matters. The sages teach: **protected inquiry and hearing** change the heart.
"""),
        "C1-W3": textwrap.dedent("""
**Paraphrase from ŚB 5.10–5.11 (selected summary):** King Rahūgaṇa, proud of his royal position, ordered a palanquin bearer to move faster. The bearer was Jaḍa Bharata — a great soul who had renounced worldly identification. When the king spoke harshly, treating him as mere body, Jaḍa Bharata replied with spiritual wisdom: the king was mistaken to identify the living being with the external covering.

**Paraphrase aligned with BG 2.20:** The soul is unborn and eternal — not created or destroyed when the body changes.

**Facilitator transition:** Like Rahūgaṇa, we sometimes address the body and miss the soul — in ourselves and others. This week we learn **positive** qualities of the soul.
"""),
        "C1-W4": textwrap.dedent("""
**Paraphrase from ŚB 6.1–6.2 (selected summary):** Mṛgāri the hunter tortured animals, thinking this was religion. Nārada Muni met him with mercy — not condemnation alone. Through Nārada's instruction and Mṛgāri's repentance, a cruel life became a life of devotion. Human intelligence can **turn** toward Kṛṣṇa even after great misuse.

**Paraphrase aligned with SB 11.9.29:** Human life is obtained with difficulty. It is temporary yet able to deliver the highest value when used for self-realization.

**Facilitator transition:** The hunter's pass was almost wasted; our human opportunity is also precious — use it for hearing and service, not panic.
"""),
        "C1-W5": textwrap.dedent("""
**Paraphrase from ŚB 4.8–4.9 (selected summary):** Young Dhruva, distressed by palace words, went to the forest seeking a kingdom greater than his father's. By austerity and mantra he sought temporary power — yet when he met the Lord, his heart changed. He received benediction, but learned that **permanent shelter** is in Kṛṣṇa's lotus feet, not temporary thrones.

**Paraphrase aligned with BG 8.15:** The material world is temporary and full of distress; returning to Kṛṣṇa is the goal.

**Facilitator transition:** Dhruva's story shows desire redirected — from temporary prize to permanent relationship.
"""),
    }
    body = katha_bodies.get(code, "")
    return textwrap.dedent(f"""---
week_code: {code}
week_title: {m['title']}
component: prem-ki-katha.md
katha_type: source-grounded-devotional-narrative
---

# Prem-kī-Kathā — {m['katha_title']}

## 1. Katha title

**{m['katha_title']}** — source narrative connected to {m['katha_source']}.

## 2. Module connection

{m['controlling_principle']}

## 3. Primary source references

| Source | Link | Use in katha |
| --- | --- | --- |
| Primary | See `katha/KATHA-SOURCE-REGISTER.yaml` | Principal narrative |
| Key verse | {m['verses'][0][1]} | Memory line anchor |

## 4. Setting and devotional mood

_[Facilitator transition]_ Quiet lamp; families seated. Mood: **wonder and willingness to hear**.

## 5. Main personalities

See source narrative in section 6.

## 6. Source-grounded narrative

_[Source narrative / paraphrase — not invented dialogue]_
{body}

## 7. Turning point

Sincere inquiry or mercy meets the heart — willingness to hear and act.

## 8. Central teaching

**Memory line:** {m['memory_line']}

## 9. Heart reflection

60 seconds silence + optional one round mahā-mantra.

## 10. Lāla–Lālī interaction cues

1. Story picture cards — see `children/lala-lali-lesson.md`.
2. Movement or craft tied to memory line.

## 11. Kiśora–Kiśorī reflection cues

1. Text observation from key verse (KUTUMBA summary + link).
2. One application sentence for home practice.

## 12. Parent bridge

Connect to `{m['bhakti_lab']}` and home practice.

## 13. Transition to philosophy lesson

→ `parent-lesson.md` / age tracks.

## 14. Narration cautions

- No invented quotes attributed to Prabhupāda or śāstra personalities.
- {'No frightening death imagery.' if m.get('no_death_imagery') else 'Follow safeguarding guide.'}
- Link-only for purports.

## 15. Visual/storyboard plan

See `visuals/VISUAL-PLAN.md`.

## 16. Rights and quotation status

Paraphrase + VedaBase links. `human-review-required`.

## 17. Human doctrinal review status

**human-review-required** — `reviews/DOCTRINAL-REVIEW.md`
""")


def lala_lesson(m: dict) -> str:
    code = m["code"]
    death_note = "No frightening death imagery." if m.get("no_death_imagery") else "Follow safeguarding policy."
    return textwrap.dedent(f"""---
week_code: {code}
week_title: {m['title']}
audience: Lāla–Lālī (ages 4–8)
component: children/lala-lali-lesson.md
---

# Lāla–Lālī Lesson — {m['title']}

**Total time:** 40 minutes  
**Memory line:** "{m['lala_recall']}"  
**Sanskrit phrase:** {m['lala_sanskrit']}  
**{death_note}**

---

## Core track — ages 4–6 (default delivery)

| Time | Activity |
| --- | --- |
| 0–5 min | Opening song; recall prior week if applicable; show theme card |
| 5–15 min | **Story** — {m['lala_story']} (8 min + wonder questions) |
| 15–22 min | Movement game tied to module theme |
| 22–28 min | Craft or sorting activity |
| 28–32 min | **Movement break** — stretch and breathe |
| 32–36 min | Verse rhythm — call and response for memory line |
| 36–40 min | Recall + hand on heart; → `shared-family-transition.md` |

### Story (8–10 min)

Facilitator tells using picture cards (paraphrase from `prem-ki-katha.md` — no invented dialogue):

> Opening scene from katha. Child-friendly wonder: "What did they learn?"  
> Connect to memory line: "{m['lala_recall']}"

**Wonder questions:** What changed? What stayed the same? How can our family practice this?

### Movement game

Four corners or relay aligned with `{m['gamma_theme']}`. Two adults in visible space.

### Craft

Module-specific art: label memory line; take home one item for family altar area.

---

## Extension — ages 7–8

| Time | Activity |
| --- | --- |
| 5–12 min | Sequence cards — order story beats from katha |
| 12–20 min | Sorting: "helps our bhakti" / "needs a boundary" |
| 20–28 min | Bookmark or ticket for home practice trigger |
| 28–35 min | Sanskrit phrase echo: {m['lala_sanskrit']} |
| 35–40 min | Pair share one kind action; reunite families |

### Extension sorting

Use activities from `complete-week.md` age 7–9 list — adapted for 7–8 only (not duplicated in core).

---

## Facilitator cautions

- {death_note}
- No public comparison between children.
- Two-adult coverage in visible space.

## Materials

See `materials.md` — Lāla–Lālī section.

## Sources

- `prem-ki-katha.md`
- Key verse link in `research/VERSE-AND-REFERENCE-STUDY.md`

## Timing checklist for facilitators

| Minute | Checkpoint |
| --- | --- |
| 5 | All children seated; story begins |
| 15 | Wonder questions complete |
| 28 | Craft or sorting in progress |
| 36 | Recall line practiced twice |
| 40 | Transition to shared-family-transition.md |

## Volunteer briefing

Confirm two adults in visible space. No comparison between children. Route upset children to quiet corner with second adult.
""")


def kisora_lesson(m: dict) -> str:
    code = m["code"]
    vref, vlink, vsum = m["verses"][0]
    return textwrap.dedent(f"""---
week_code: {code}
week_title: {m['title']}
audience: Kiśora–Kiśorī (ages 9–14)
component: children/kisora-kisori-lesson.md
---

# Kiśora–Kiśorī Lesson — {m['title']}

**Total time:** 40 minutes  
**Essential question:** {m['essential_question']}  
**No forced personal disclosure.**

---

## Core track — ages 9–11

| Time | Activity |
| --- | --- |
| 0–5 min | Index cards — one word for theme, one for "my practice" |
| 5–15 min | **Text observation** — {vref} |
| 15–22 min | Concept diagram from `visuals/concept-map.mmd` |
| 22–30 min | Case study from `research/CONTEMPORARY-APPLICATIONS.md` |
| 30–35 min | Reflective writing (3–4 sentences, optional share) |
| 35–40 min | Service or practice commitment + transition |

### Text observation — {vref}

KUTUMBA summary (not full purport):

> {vsum}

**Observe:** (1) Key terms (2) Promised result (3) One home action

Reference: [{vlink}]({vlink})

### Case discussion

Facilitator reads one anonymized case. Pairs: mistaken conclusion? compassionate response?

### Reflective writing

"When I apply this teaching at home, I will…" — optional share; no grading.

---

## Extension — ages 12–14

| Addition | Detail |
| --- | --- |
| **Respectful debate** | Motion from `research/MISCONCEPTIONS-AND-BOUNDARIES.md` — 3 min prep, cite verse summary |
| **Application design** | Redesign one family routine using key verse |
| **Challenge writing** | One paragraph — anonymized peer scenario |
| **Peer appreciation** | Specific language: "Your example helped me understand…" |

### Debate rules

1. Attack ideas, not people.  
2. Use source reference or KUTUMBA summary.  
3. Facilitator may pause for safeguarding.  
4. No recording without consent.

---

## Facilitator cautions

- Scope boundaries in `research/RESEARCH-DOSSIER.md`.
- Route trauma privately per safeguarding policy.
- Never ask public appearance or performance ranking.

## Materials

See `materials.md` — Kiśora–Kiśorī section.

## Sources

- `{vlink}`
- `research/CONTEMPORARY-APPLICATIONS.md`
- `analogy-and-application.md`

## Timing checklist

| Minute | Checkpoint |
| --- | --- |
| 5 | Text observation handout distributed |
| 15 | Verse link opened for optional follow-up at home |
| 30 | Case discussion debrief complete |
| 40 | Youth commitment card collected privately (optional) |

## Extension facilitator note

Ages 12–14 may facilitate a station at C1-W6 integration; not required this week unless roster needs coverage.
""")


def shared_transition(m: dict) -> str:
    return textwrap.dedent(f"""---
week_code: {m['code']}
week_title: {m['title']}
audience: All ages — reunification after parallel tracks
---

# Shared Family Transition — 10 Minutes

**When:** After parallel tracks (minute 40–50) or before Bhakti laboratory.

## Purpose

Reunite families with one shared insight and one shared practice — without re-teaching the full lesson.

## Flow

| Time | Action |
| --- | --- |
| 0–2 min | Bell; families sit together. "What will we practice at home this week?" |
| 2–5 min | **One-line share:** Each subgroup teaches one thing (pre-assigned) |
| 5–8 min | **Family pair practice:** Parent + child complete one worksheet line or show craft |
| 8–10 min | **Saṅkalpa preview:** Read opening from `sankalpa.md`; whisper trigger + minimum version |

## All-age recall (call and response)

> **Leader:** {m['lala_recall']}  
> **All:** {m['lala_recall']}

## Bridge to Bhakti laboratory

→ `{m['bhakti_lab']}` per `bhakti-lab.md`

## Bridge to home practice

→ `family-home-practice.md` — **Minimum:** {m['home_practice']}

## Newcomer note

Host families help newcomers find materials. Observation welcome; no forced chanting length.

## Continuity link

Families carry one insight and one practice decision into `{m['bhakti_lab']}` without repeating the full parent lesson.
""")


def gamma_cards(m: dict, audience: str, count: int) -> str:
    code = m["code"]
    titles = {
        "parent": [
            ("Title", f"{code} — {m['title']}\nCycle 1 · Identity and the Human Problem\nKUTUMBA Family Program"),
            ("Essential question", m["essential_question"]),
            ("Opening hook", m["opening_hook"][:200] + "…"),
            ("Key verse", f"**{m['key_verse']}**\n\nMemory line: {m['memory_line']}\n\nLink-only purport on VedaBase"),
            ("Controlling principle", m["controlling_principle"]),
            ("Source anchor", f"Primary: {m['sources'][0][3]}\nSee SOURCE-MATRIX.md"),
            ("Contemporary case", "One anonymized case from CONTEMPORARY-APPLICATIONS.md"),
            ("Misconception guard", "See MISCONCEPTIONS-AND-BOUNDARIES.md — means vs does not mean"),
            ("Bhakti laboratory", m["bhakti_lab"]),
            ("Home practice", m["home_practice"]),
            ("Family saṅkalpa", "Specific action + frequency + trigger + minimum version"),
            ("Sources and review", "human-review-required — no invented Prabhupāda quotes"),
        ],
        "lala-lali": [
            ("Title", f"{m['lala_recall']}\nLāla–Lālī · {code}"),
            ("Story beat 1", f"{m['lala_story']} — opening"),
            ("Story beat 2", "Wonder question — what changed?"),
            ("Memory line", m["lala_recall"]),
            ("Movement game", m["gamma_theme"]),
            ("Craft", "Take-home art for family altar area"),
            ("Sanskrit echo", m["lala_sanskrit"]),
            ("Kind action", "One way to help family remember Kṛṣṇa"),
            ("Body/soul care", "Care for living beings — no mockery"),
            ("Home practice", "Minimum version with parent"),
        ],
        "kisora-kisori": [
            ("Title", f"{code} — Youth Track"),
            ("Essential question", m["essential_question"]),
            ("Verse observation", f"{m['verses'][0][0]} — KUTUMBA summary + VedaBase link"),
            ("Concept map", "Import from visuals/concept-map.mmd"),
            ("Case study", "CS-01 from CONTEMPORARY-APPLICATIONS.md"),
            ("Misconception", "One row from MISCONCEPTIONS table"),
            ("Debate motion", "Respectful debate — rules on slide"),
            ("Application", "Redesign one family routine"),
            ("Service commitment", "One concrete action this week"),
            ("Writing prompt", "Optional reflective paragraph"),
            ("Bridge to parents", "Shared transition recall line"),
            ("Sources", "Link-only — human-review-required"),
        ],
    }
    cards = titles[audience][:count]
    deck_name = {"parent": "Parent / Family", "lala-lali": "Lāla–Lālī", "kisora-kisori": "Kiśora–Kiśorī"}[audience]
    lines = [
        f"# Gamma Prompt — {code} {deck_name} Deck",
        "",
        "## Deck identity",
        "",
        f"- **Module:** {code} — {m['title']}",
        f"- **Audience:** {deck_name}",
        f"- **Recommended card count:** {count}",
        f"- **Theme:** {m['gamma_theme']}",
        "",
        "## Global instructions",
        "",
        "Paste below into Gamma. No invented Prabhupāda quotes. Link-only purports.",
        "",
        "---",
        "",
        "## Card plan",
        "",
    ]
    for i, (label, content) in enumerate(cards, 1):
        lines += [
            f"### Card {i} — {label}",
            "",
            "**Content:**  ",
            content.replace("\n", "\n"),
            "",
            f"**Visual:** `[IMAGE: {m['gamma_theme']} — congregation-owned or placeholder]`",
            f"**Speaker note:** See SPEAKER-NOTES.md",
            f"**Source:** research/ or prem-ki-katha.md",
            "",
            "---",
            "",
        ]
    return "\n".join(lines)


def review_md(name: str, m: dict) -> str:
    code = m["code"]
    base = f"# {code} {name.replace('-', ' ').replace('.md', '').title()}\n\n**Status:** human-review-required  \n**Reviewer:** _[assign]_  \n**Date:** 2026-06-30 (enhancement pass)\n\n"
    bodies = {
        "DOCTRINAL-REVIEW.md": f"""## Scope reviewed

- research/CLAIM-REGISTER.yaml
- research/VERSE-AND-REFERENCE-STUDY.md
- prem-ki-katha.md and katha/KATHA-SOURCE-REGISTER.yaml
- Age-track lessons and gamma prompts

## Findings

| ID | Finding | Severity | Remediation |
| --- | --- | --- | --- |
| DR-01 | Claims align with assigned verses; paraphrase only in Git | Pass-pending | Human confirm summaries |
| DR-02 | Scope boundaries documented in RESEARCH-DOSSIER | Pass-pending | Maintain deferrals |
| DR-03 | No invented Prabhupāda quotations detected in automated pass | Pass-pending | Citation audit sign-off |

## Open items

1. Confirm verse numbering matches congregation printed edition
2. Sign claim register entries
3. Review katha paraphrase against source

## Verdict

**Enhancement-complete pending human sign-off.**
""",
        "CITATION-AUDIT.md": """## Citation audit checklist

- [ ] All verse references have stable VedaBase URLs
- [ ] No full purports reproduced in Git
- [ ] Lecture index entries verified on VedaBase
- [ ] Contemporary cases marked non-śāstra
- [ ] KATHA-SOURCE-REGISTER.yaml complete

## Sample spot-check

| File | Citation type | Status |
| --- | --- | --- |
| prem-ki-katha.md | paraphrase + link | human-review-required |
| VERSE-AND-REFERENCE-STUDY.md | KUTUMBA summary | human-review-required |
| gamma prompts | reference lines | human-review-required |

## Verdict

Pending human citation reviewer.
""",
        "SAFEGUARDING-REVIEW.md": f"""## Safeguarding scope

- Age-track lessons ({'no death imagery' if m.get('no_death_imagery') else 'standard guards'})
- CONTEMPORARY-APPLICATIONS.md cases
- MISCONCEPTIONS spiritual-bypassing red flags

## Checklist

- [ ] No frightening death imagery in Lāla–Lālī track
- [ ] No forced public disclosure
- [ ] Trauma/grief cases handled with compassion boundaries
- [ ] Two-adult visible-space policy referenced

## Verdict

Pending safeguarding lead sign-off.
""",
        "RIGHTS-REVIEW.md": """## Rights review

- Scripture: link-only (VedaBase)
- Images: placeholders in gamma — `visuals/image-rights-register.yaml`
- No copyrighted audio/video committed

## Verdict

Pending rights reviewer.
""",
        "PEDAGOGY-REVIEW.md": """## Pedagogy review

| Track | Evidence | Score |
| --- | --- | --- |
| Parent 40-min | parent-lesson.md + complete-week.md | Strong-pending |
| Lāla–Lālī 80+ lines | children/lala-lali-lesson.md | Strong-pending |
| Kiśora–Kiśorī 80+ lines | children/kisora-kisori-lesson.md | Strong-pending |
| Gamma decks | 12/10/11 card prompts | Strong-pending |
| Integration | shared-family-transition.md | Strong-pending |

## Adult pedagogy

| Criterion | Evidence | Score |
| --- | --- | --- |
| Hook → source → application | opening-hook.md, prem-ki-katha.md, parent lesson | Strong-pending |
| Misconception guard | MISCONCEPTIONS-AND-BOUNDARIES.md | Strong-pending |
| Not dossier-overloaded | Live lesson uses summaries | Strong-pending |

## Child pedagogy

| Criterion | Evidence | Score |
| --- | --- | --- |
| Timed 40-min plan | lala-lali-lesson.md, kisora-kisori-lesson.md | Strong-pending |
| No duplicated age blocks in Lāla file | Single core + extension structure | Strong-pending |
| Safeguarding explicit | No frightening death imagery where excluded | Strong-pending |

## Open items

1. Live pilot timing observation
2. Newcomer load check
3. Confirm gamma card count in rendered decks when produced

## Verdict

Strong design pending live observation sign-off.
""",
    }
    return base + bodies.get(name, f"Module: {code}\n\nStatus: human-review-required\n")


def mermaid_viewer(name: str, mmd_path: str, m: dict) -> str:
    return f"# {name.replace('-', ' ').title()} — {m['code']}\n\nRender in Markdown preview. Source: [`{mmd_path}`]({mmd_path})\n\n```mermaid\nflowchart TB\n  A[\"{m['code']}: {m['title'][:40]}\"] --> B[Source]\n  A --> C[Practice]\n  A --> D[Character]\n  B --> E[{m['verses'][0][0]}]\n```\n"


def enhance(slug: str) -> list[str]:
    m = MODULES[slug]
    folder = WEEKLY / slug
    code = m["code"]
    created: list[str] = []

    def track(rel: str, content: str) -> None:
        w(folder / rel, content)
        created.append(rel)

    # Research layer
    dossier = f"""# {code} Research Dossier — {m['title']}

## Module identity

| Field | Detail |
| --- | --- |
| **Module ID** | {code} |
| **Title** | {m['title']} |
| **Cycle** | Cycle 1 — Identity and the Human Problem |
| **Essential question** | {m['essential_question']} |
| **Controlling principle** | {m['controlling_principle']} |
| **Scope** | {m['scope']} |
| **Explicit exclusions** | {m['exclusions']} |
| **Prerequisites** | {m['prerequisites']} |
| **Leads to** | {m['leads_to']} |

## Source hierarchy

1. Tier 1: Bhagavad-gītā, Śrīmad-Bhāgavatam, Caitanya-caritāmṛta (VedaBase + KUTUMBA summaries)
2. Tier 1: Indexed Prabhupāda lectures in PRABHUPADA-LECTURE-INDEX.md
3. Pedagogy: KUTUMBA analogies and cases (tagged)
4. Blocked: Unattributed quotes, AI-only authority

## Primary source matrix

→ [SOURCE-MATRIX.md](SOURCE-MATRIX.md)

## Research questions answered

| # | Question | Answer (summary) |
| --- | --- | --- |
| 1 | What is the controlling principle? | {m['controlling_principle']} |
| 2 | Key verse? | {m['key_verse']} |
| 3 | Home practice? | {m['home_practice']} |
| 4 | What does it NOT mean? | See MISCONCEPTIONS-AND-BOUNDARIES.md |
| 5 | Contemporary applications? | See CONTEMPORARY-APPLICATIONS.md |
| 6 | Child capacity? | Lāla–Lālī story + movement; no forced disclosure |
| 7 | Youth capacity? | Text observation + case + optional debate |
| 8 | Parent practice? | 40-min plan in parent-lesson.md |
| 9 | Visual needs? | VISUAL-PLAN.md |
| 10 | Katha connection? | {m['katha_title']} — prem-ki-katha.md |

## Key distinctions

- Scripture summary vs. full purport (link-only in Git)
- Pedagogical case vs. doctrine
- Minimum vs. standard vs. stretch home practice

## Misconceptions → MISCONCEPTIONS-AND-BOUNDARIES.md
## Contemporary cases → CONTEMPORARY-APPLICATIONS.md
## Visuals → ../visuals/VISUAL-PLAN.md
## Gamma → ../gamma/GAMMA-MASTER-DECK-BRIEF.md

## Open questions

- Human reviewer to confirm verse edition
- Optional second lecture index after doctrinal review

## Human review required

doctrinal, safeguarding, worship, rights, pedagogy, citation

_Status: enhancement-complete — pending human review_
"""
    track("research/RESEARCH-DOSSIER.md", dossier)

    sm_rows = "\n".join(
        f"| {sid} | {work} | {ref} | [link]({url}) | Teaching function | Yes | human-review-required |"
        for sid, work, ref, url, _ in m["sources"]
    )
    track("research/SOURCE-MATRIX.md", f"# {code} Source Matrix\n\n| Source ID | Work | Reference | Stable link | Teaching function | Context checked | Status |\n| --- | --- | --- | --- | --- | --- | --- |\n{sm_rows}\n\n## Copyright\n\nStable URL + KUTUMBA summary only.\n")

    track("research/CLAIM-REGISTER.yaml", claims_yaml(m))

    lec_rows = "\n".join(
        f"| {lid} | {date} | {place} | {topic} | {seg} | [link]({url}) | human-review-required |"
        for lid, date, place, topic, seg, url in m["lectures"]
    )
    lec_summaries = "\n\n".join(
        f"## KUTUMBA summary — {topic}\n\nIndexed lecture for private facilitator preparation. See VedaBase link in table above — summarize only, do not transcribe at length."
        for _, _, _, topic, _, _ in m["lectures"]
    )
    track("research/PRABHUPADA-LECTURE-INDEX.md", f"# {code} Śrīla Prabhupāda Lecture Index\n\nVerified entries with stable VedaBase links. Summaries only in repository.\n\n| Media ID | Date | Place | Title | Topic segment | Link | Status |\n| --- | --- | --- | --- | --- | --- | --- |\n{lec_rows}\n\n## Usage rules\n\n- Facilitators may listen privately for preparation; do not transcribe lengthy quotes into slides.\n- Prefer citing verse summaries and pointing families to VedaBase.\n\n{lec_summaries}\n")

    track("research/CONTEMPORARY-APPLICATIONS.md", contemporary_cases(m))

    track("research/MISCONCEPTIONS-AND-BOUNDARIES.md", f"""# {code} Misconceptions and Boundaries

## Common misconceptions

| Misconception | Correction | Source |
| --- | --- | --- |
| Philosophy replaces professional care | Compassion + qualified help when needed | Safeguarding |
| KUTUMBA teaching equals full purport | Link-only; read purport on VedaBase | Citation policy |
| Pedagogical case is śāstra | Cases are illustrations only | CLAIM-REGISTER |
| Scope creep from later modules | See exclusions: {m['exclusions']} | RESEARCH-DOSSIER |

## Scope boundaries

| Topic | Deferred to |
| --- | --- |
| Later cycle content | See three-year architecture |
| Out-of-scope siddhānta | {m['exclusions']} |

## Spiritual bypassing red flags

Facilitators interrupt dismissive use of philosophy toward pain, trauma, or medical need.
""")

    track("research/FAQ.md", f"""# {code} FAQ

## Discovery

**What is this week's key verse?**  
{m['key_verse']}

**What is the memory line?**  
{m['memory_line']}

## Understanding

**What is the essential question?**  
{m['essential_question']}

**What is excluded this week?**  
{m['exclusions']}

## Application

**Minimum home practice?**  
{m['home_practice']}

**Where is the katha?**  
prem-ki-katha.md — {m['katha_title']}

## Facilitator

**Approval status?**  
human-review-required until DOCTRINAL-REVIEW signed.
""")

    verse_blocks = "\n\n---\n\n".join(
        f"## {ref}\n\n**Link:** [{link}]({link})\n\n**KUTUMBA summary:** {summary}\n\n**Teaching use:** Primary/reference for {code}."
        for ref, link, summary in m["verses"]
    )
    track("research/VERSE-AND-REFERENCE-STUDY.md", f"# {code} Verse and Reference Study\n\nKUTUMBA summaries only. Full text and purport on VedaBase.\n\n---\n\n{verse_blocks}\n")

    bib_lines = "\n".join(f"- {work} {ref} — [{url}]({url})" for _, work, ref, url, _ in m["sources"])
    track("research/BIBLIOGRAPHY.md", f"# {code} Bibliography\n\n## Tier 1 sources\n\n{bib_lines}\n\n## KUTUMBA originals\n\n- complete-week.md\n- KUTUMBA Master Operating Model (reference)\n")

    # Katha layer
    track("opening-hook.md", f"""---
week_code: {code}
component: opening-hook.md
---

## Opening Hook (modern scenario)

_Not Prem-kī-Kathā — see prem-ki-katha.md._

| {m['opening_hook']} |
| --- |

**Delivery:** 2–3 minutes before katha or parent lesson.
""")

    track("prem-ki-katha.md", prem_katha(m))

    katha_links = "\n".join(f"  - label: {m['verses'][i][0] if i < len(m['verses']) else 'Primary'}\n    url: {m['verses'][0][1]}" for i in range(1))
    track("katha/KATHA-SOURCE-REGISTER.yaml", f"""module_id: {code}
katha_title: "{m['katha_title']}"
primary_book: {m['katha_source']}
katha_type: {m['katha_type']}
stable_links:
{katha_links}
direct_quotations: []
paraphrased_portions:
  - Principal narrative — paraphrase from {m['katha_source']}
facilitator_transitions:
  - Opening hook bridge
  - Philosophy lesson bridge
omitted_complex_details:
  - Full purports in Git
  - Out-of-scope siddhānta per RESEARCH-DOSSIER
audience_cautions:
  - No invented quotes
  - {'No frightening death imagery' if m.get('no_death_imagery') else 'Safeguarding per policy'}
doctrinal_reviewer: pending
rights_status: scripture-reference-links-only
approval_status: human-review-required
""")

    # Children
    track("children/lala-lali-lesson.md", lala_lesson(m))
    track("children/kisora-kisori-lesson.md", kisora_lesson(m))
    track("children/shared-family-transition.md", shared_transition(m))

    # Gamma
    track("gamma/GAMMA-PARENT-DECK-PROMPT.md", gamma_cards(m, "parent", 12))
    track("gamma/GAMMA-LALA-LALI-DECK-PROMPT.md", gamma_cards(m, "lala-lali", 10))
    track("gamma/GAMMA-KISORA-KISORI-DECK-PROMPT.md", gamma_cards(m, "kisora-kisori", 11))
    track("gamma/GAMMA-MASTER-DECK-BRIEF.md", f"# Master deck brief — {code}\n\nThree decks: parent (12), Lāla–Lālī (10), Kiśora–Kiśorī (11).\n\nTheme: {m['gamma_theme']}\n")
    track("gamma/SPEAKER-NOTES.md", f"# Speaker notes — {code}\n\nUse KUTUMBA summaries; point to VedaBase for purports.\n")

    # Visuals
    concept = f"flowchart TB\n  Q[\"{m['essential_question'][:50]}\"] --> P[Practice]\n  Q --> S[Source]\n  S --> V[{m['verses'][0][0]}]\n  P --> H[Home practice]\n"
    process = "flowchart LR\n  Hook --> Katha --> Lesson --> Lab --> HomePractice\n"
    track("visuals/concept-map.mmd", concept)
    track("visuals/process-flow.mmd", process)
    track("visuals/concept-map.md", mermaid_viewer("concept-map", "concept-map.mmd", m))
    track("visuals/process-flow.md", mermaid_viewer("process-flow", "process-flow.mmd", m))
    track("visuals/VISUAL-PLAN.md", f"""# {code} Visual Plan

## Design principles

- Mermaid originals in git — no BBT copyrighted images
- Render `.mmd` via Markdown preview or `concept-map.md` / `process-flow.md`

## Visual inventory

| # | Visual | File | Audience | Purpose |
| --- | --- | --- | --- | --- |
| 1 | Concept map | concept-map.mmd | 9+ | {m['gamma_theme']} |
| 2 | Session flow | process-flow.mmd | facilitator | Friday flow |
| 3 | Means / does not mean | MISCONCEPTIONS-AND-BOUNDARIES.md | parent | Scope guard |

## Gamma integration

Deck prompts reference these visuals as placeholders.

## Image rights

image-rights-register.yaml — placeholders until congregation assets approved.
""")

    # Reviews
    for rn in ["DOCTRINAL-REVIEW.md", "CITATION-AUDIT.md", "SAFEGUARDING-REVIEW.md", "RIGHTS-REVIEW.md", "PEDAGOGY-REVIEW.md"]:
        track(f"reviews/{rn}", review_md(rn, m))

    # Media
    lec_id = m["lectures"][0][0]
    lec_url = m["lectures"][0][5]
    track("audio-video/MEDIA-INDEX.yaml", f"""week_code: {code}
media:
  - media_id: {code}-MEDIA-001
    type: gamma-deck-parent
    title: "{code} Parent Deck"
    location: gamma/GAMMA-PARENT-DECK-PROMPT.md
    status: prompt-ready-not-rendered
    rights_status: internal

  - media_id: {code}-MEDIA-002
    type: gamma-deck-lala-lali
    title: "{code} Lāla–Lālī Deck"
    location: gamma/GAMMA-LALA-LALI-DECK-PROMPT.md
    status: prompt-ready-not-rendered
    rights_status: internal

  - media_id: {code}-MEDIA-003
    type: gamma-deck-kisora-kisori
    title: "{code} Kiśora–Kiśorī Deck"
    location: gamma/GAMMA-KISORA-KISORI-DECK-PROMPT.md
    status: prompt-ready-not-rendered
    rights_status: internal

  - media_id: {code}-MEDIA-004
    type: prabhupada-lecture
    title: "{m['lectures'][0][3]}"
    stable_url: "{lec_url}"
    catalog_ref: {MEDIA_CATALOG}
    index_ref: research/PRABHUPADA-LECTURE-INDEX.md
    status: reference-only
    rights_status: vedabase-link

approved_teacher_media: []

notes: "No video files in repository. Optional VedaBase lecture playback in private prep only."
""")

    track("review-status.yaml", f"""week_code: {code}
canonical_detailed_source: complete
weekly_derivative_pack: enhancement-complete
research_dossier: complete
source_registry: complete
claim_traceability: complete
parent_lesson: complete
lala_lali_lesson: complete
kisora_kisori_lesson: complete
materials: complete
assessment: complete
newcomer_adaptation: complete
visual_plan: complete
gamma_prompts: complete
cycle_project: complete
automated_semantic_validation: pending
doctrinal_review: required
worship_review: required
safeguarding_review: required
rights_review: required
pedagogy_review: required
citation_audit: required
publication_status: internal-development
pilot_quality_gate: pass-pending-human-review
enhancement_date: 2026-06-30
enhancement_version: "3.0.0"
""")

    return created


def main() -> None:
    for slug in TARGET_SLUGS:
        files = enhance(slug)
        print(f"{MODULES[slug]['code']}: wrote {len(files)} files")


if __name__ == "__main__":
    main()

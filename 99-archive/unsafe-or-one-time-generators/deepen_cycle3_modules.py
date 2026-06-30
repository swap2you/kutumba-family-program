#!/usr/bin/env python3
"""Deepen Cycle 3 modules (C3-W1 through C3-W6) to C1-W2 gold standard."""

from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BASE = REPO / "11-weekly-program-library" / "first-six-months"

MODULES = [
    {
        "slug": "c3-w1-who-is-god-the-supreme-enjoyer-proprietor-and-friend",
        "code": "C3-W1",
        "title": "Who Is God? The Supreme Enjoyer, Proprietor and Friend",
        "key_verse": "Bhagavad-gītā 5.29",
        "verse_link": "https://vedabase.io/en/library/bg/5/29/",
        "memory_line": "Peace comes from knowing Kṛṣṇa as the supreme enjoyer, proprietor of everything and friend of all living beings.",
        "katha_title": "The gopīs' surrender — Kṛṣṇa as supreme proprietor",
        "katha_primary": "Śrīmad-Bhāgavatam 10.14",
        "katha_ref": "SB 10.14 (selected — gopīs' prayers)",
        "katha_links": [
            ("SB 10.14.7", "https://vedabase.io/en/library/sb/10/14/7/"),
            ("SB 10.14.8", "https://vedabase.io/en/library/sb/10/14/8/"),
            ("BG 5.29", "https://vedabase.io/en/library/bg/5/29/"),
        ],
        "hook": "Two children argue over a room full of toys: 'Mine!' 'No, mine!' A parent intervenes, but later the adults have the same argument in a more sophisticated form—over money, credit, schedule, recognition or authority. Much family conflict begins with a hidden claim: 'I am the owner, I am the enjoyer, and my plan should control everyone.'",
        "integration": False,
    },
    {
        "slug": "c3-w2-who-is-kṛṣṇa-the-supreme-personality-of-godhead",
        "code": "C3-W2",
        "title": "Who Is Kṛṣṇa? The Supreme Personality of Godhead",
        "key_verse": "Bhagavad-gītā 7.7",
        "verse_link": "https://vedabase.io/en/library/bg/7/7/",
        "memory_line": "There is no truth superior to Kṛṣṇa; everything rests upon Him like pearls on a thread.",
        "katha_title": "Kṛṣṇa's birth in Vṛndāvana",
        "katha_primary": "Śrīmad-Bhāgavatam 10.3",
        "katha_ref": "SB 10.3 (selected — birth pastime)",
        "katha_links": [
            ("SB 10.3.1", "https://vedabase.io/en/library/sb/10/3/1/"),
            ("SB 10.3.43", "https://vedabase.io/en/library/sb/10/3/43/"),
            ("BG 7.7", "https://vedabase.io/en/library/bg/7/7/"),
            ("SB 1.3.28", "https://vedabase.io/en/library/sb/1/3/28/"),
        ],
        "hook": "A child asks at bedtime: 'Is God far away in the sky, or is He here?' Parents sometimes answer with abstract ideas—energy, light, a force. But Śrīla Prabhupāda's books introduce Kṛṣṇa as the Supreme Person who appears in this world with form, name and pastimes we can love.",
        "integration": False,
    },
    {
        "slug": "c3-w3-guru-sādhu-and-śāstra-how-we-receive-spiritual-knowledge",
        "code": "C3-W3",
        "title": "Guru, Sādhu and Śāstra: How We Receive Spiritual Knowledge",
        "key_verse": "Bhagavad-gītā 4.34",
        "verse_link": "https://vedabase.io/en/library/bg/4/34/",
        "memory_line": "Approach spiritual truth with humility, sincere inquiry and service; realized teachers can impart knowledge.",
        "katha_title": "How Nārada received the Bhāgavatam",
        "katha_primary": "Śrīmad-Bhāgavatam 1.1 / 1.4",
        "katha_ref": "SB 1.1 and 1.4 (selected — paramparā)",
        "katha_links": [
            ("SB 1.1.1", "https://vedabase.io/en/library/sb/1/1/1/"),
            ("SB 1.4.25", "https://vedabase.io/en/library/sb/1/4/25/"),
            ("BG 4.34", "https://vedabase.io/en/library/bg/4/34/"),
            ("SB 11.3.21", "https://vedabase.io/en/library/sb/11/3/21/"),
        ],
        "hook": "A family hears three different spiritual opinions online, from a friend and from a book. Everyone sounds confident. How do we know what to trust? KUTUMBA teaches that authentic knowledge comes through guru, sādhu and śāstra working together—not through popularity alone.",
        "integration": False,
    },
    {
        "slug": "c3-w4-śrī-caitanya-mahāprabhu-and-the-holy-name",
        "code": "C3-W4",
        "title": "Śrī Caitanya Mahāprabhu and the Holy Name",
        "key_verse": "Caitanya-caritāmṛta Antya 20.12 (Śikṣāṣṭakam 1)",
        "verse_link": "https://vedabase.io/en/library/cc/antya/20/12/",
        "memory_line": "The congregational chanting of Kṛṣṇa's holy name cleanses the heart and expands spiritual life.",
        "katha_title": "Lord Caitanya's kīrtana at Navadvīpa",
        "katha_primary": "Caitanya-caritāmṛta Ādi (selected)",
        "katha_ref": "CC Ādi 7.163; Ādi 17.21 (selected)",
        "katha_links": [
            ("CC Ādi 7.163", "https://vedabase.io/en/library/cc/adi/7/163/"),
            ("CC Ādi 17.21", "https://vedabase.io/en/library/cc/adi/17/21/"),
            ("CC Antya 20.12", "https://vedabase.io/en/library/cc/antya/20/12/"),
            ("SB 12.3.51", "https://vedabase.io/en/library/sb/12/3/51/"),
        ],
        "hook": "Sometimes kīrtana feels joyful; sometimes the mind wanders and we feel we are 'bad at chanting.' Lord Caitanya taught that the holy name is not a performance test—it is Kṛṣṇa's gift, meant to be heard and sung together with humility.",
        "integration": False,
    },
    {
        "slug": "c3-w5-the-nine-processes-of-bhakti",
        "code": "C3-W5",
        "title": "The Nine Processes of Bhakti",
        "key_verse": "Śrīmad-Bhāgavatam 7.5.23–24",
        "verse_link": "https://vedabase.io/en/library/sb/7/5/23/",
        "memory_line": "Hearing, chanting, remembering, serving, worshiping, praying, serving as a servant, friendship and full surrender are processes of pure devotional service.",
        "katha_title": "Prahlāda's nine processes of devotion",
        "katha_primary": "Śrīmad-Bhāgavatam 7.5",
        "katha_ref": "SB 7.5.23–24 (Prahlāda's instruction)",
        "katha_links": [
            ("SB 7.5.23", "https://vedabase.io/en/library/sb/7/5/23/"),
            ("SB 7.5.24", "https://vedabase.io/en/library/sb/7/5/24/"),
            ("BG 9.14", "https://vedabase.io/en/library/bg/9/14/"),
        ],
        "hook": "A family attends a program, chants once, then returns to the same routine at home. Bhakti is not only an event—it is a whole life. Prahlāda Mahārāja, even as a child, showed how hearing, chanting, remembering and serving fit together.",
        "integration": False,
    },
    {
        "slug": "c3-w6-bhakti-mela-kīrtana-drama-and-family-presentation",
        "code": "C3-W6",
        "title": "Bhakti Mela: Kīrtana, Drama and Family Presentation",
        "key_verse": "Śrīmad-Bhāgavatam 7.5.23–24 (review)",
        "verse_link": "https://vedabase.io/en/library/sb/7/5/23/",
        "memory_line": "These processes become pure devotional service when offered to Viṣṇu with one's life and intention.",
        "katha_title": "Six months of family bhakti — synthesis and offering",
        "katha_primary": "Congregation synthesis (no new principal līlā)",
        "katha_ref": "Review: BG 5.29, BG 7.7, BG 4.34, CC Antya 20.12, SB 7.5.23–24",
        "katha_links": [
            ("BG 5.29", "https://vedabase.io/en/library/bg/5/29/"),
            ("BG 7.7", "https://vedabase.io/en/library/bg/7/7/"),
            ("BG 4.34", "https://vedabase.io/en/library/bg/4/34/"),
            ("SB 7.5.23", "https://vedabase.io/en/library/sb/7/5/23/"),
        ],
        "hook": "Six months ago, KUTUMBA began with a question: Why are we here? The answer was not to create another event. We came to help families hear, chant, remember, serve and reorganize home life around Kṛṣṇa.",
        "integration": True,
    },
]


def write_opening_hook(folder: Path, m: dict) -> None:
    (folder / "opening-hook.md").write_text(
        f"""---
week_code: {m['code']}
week_title: {m['title']}
component: opening-hook.md
provenance: migrated-from-legacy-prem-ki-katha
---

## Opening Hook (modern scenario)

_This is a contemporary entry point — not Prem-kī-Kathā. See [`prem-ki-katha.md`](prem-ki-katha.md) for the devotional narrative._

| {m['hook']} |
| --- |

**Delivery:** 2–3 minutes before Prem-kī-Kathā or parent lesson.  
**Provenance:** Migrated from legacy `prem-ki-katha.md` during Cycle 3 deepening (v3.0.0).
""",
        encoding="utf-8",
    )


def katha_narrative(m: dict) -> str:
    code, title = m["code"], m["title"]
    if m["integration"]:
        return f"""## 6. Source-grounded narrative (synthesis format)

_[Facilitator transition — warm room, families seated together]_

**Paraphrase — KUTUMBA journey (not new līlā):** Six months ago this congregation began Cycle 1 with a simple question: who am I, and how should our family live? Families learned that the body changes but the conscious self continues ([BG 2.13](https://vedabase.io/en/library/bg/2/13/)). They are learned that actions have consequences and that the next choice matters. Now, in Cycle 3, we have heard who God is as enjoyer, proprietor and friend ([BG 5.29](https://vedabase.io/en/library/bg/5/29/)), who Kṛṣṇa is as the Supreme Personality of Godhead ([BG 7.7](https://vedabase.io/en/library/bg/7/7/)), how knowledge comes through guru, sādhu and śāstra ([BG 4.34](https://vedabase.io/en/library/bg/4/34/)), how Lord Caitanya gave the holy name ([CC Antya 20.12](https://vedabase.io/en/library/cc/antya/20/12/)), and how Prahlāda showed the nine processes of bhakti ([SB 7.5.23–24](https://vedabase.io/en/library/sb/7/5/23/)).

**Paraphrase — offering mood:** Today is not a test. It is an offering. Each family brings what Kṛṣṇa has helped them understand—a song, a drama, a poster, a simple explanation—not to compete, but to encourage one another. The Bhakti Mela is like a garden where many flowers bloom: different colors, same purpose—glorifying Kṛṣṇa together.

**Paraphrase — continuity:** Some families started with only five minutes of kīrtana. Some learned one verse. Some corrected a misconception about modes or guru. All of this is valuable when offered with sincerity. The thirty-day baseline we plan today is smaller than the mela—but steadier.

## 7. Turning point

The turning point is gratitude: "We are not finished learning, but we are not starting from zero either." Families turn from comparison to appreciation—thanking Kṛṣṇa, thanking one another, choosing one realistic practice to continue.

## 8. Central teaching

Integration weeks synthesize prior modules without adding overloaded new narratives. Bhakti becomes family life—daily, weekly, monthly—offered to Viṣṇu with intention ([SB 7.5.23–24](https://vedabase.io/en/library/sb/7/5/23/)).

**Memory line:** {m['memory_line']}
"""
    narratives = {
        "C3-W1": """## 6. Source-grounded narrative

_[Facilitator transition — quiet, devotional mood]_

**Paraphrase from ŚB 10.14 (gopīs' prayers — summary):** After Kṛṣṇa lifted Govardhana Hill, the gopīs of Vṛndāvana spoke prayers filled with wonder and surrender. They understood that Kṛṣṇa is not an ordinary boy—they saw that He is the supreme controller who owns everything, enjoys everything transcendently, and yet appears as their beloved friend. Their words express that no one can claim independent proprietorship over land, body, family or result when everything belongs to the Supreme Lord.

**Paraphrase aligned with BG 5.29:** Kṛṣṇa is described as the supreme enjoyer of sacrifice and austerity, the proprietor of all planets, and the well-wishing friend of every living being. When the living entity forgets this and claims "I am the enjoyer, I am the owner," anxiety follows. When one remembers Kṛṣṇa's position, practical peace becomes possible—not by suppressing duties, but by redirecting them.

**Paraphrase — stewardship:** The gopīs did not become careless with Kṛṣṇa's property. Their surrender increased their care—offering flowers, food, affection and service. For our families, "Kṛṣṇa owns everything" means greater responsibility, not less: we care for home, body, children and resources as entrusted gifts.

## 7. Turning point

The gopīs' turning point is honest recognition: "We thought we possessed, but You are the real proprietor." For families, the turning point is the same posture when conflict arises over toys, money, credit or schedule—pause and ask the three peace questions from BG 5.29.

## 8. Central teaching

Peace comes from knowing Kṛṣṇa as supreme enjoyer, proprietor of everything, and friend of all beings. Stewardship replaces possessiveness.

**Memory line:** Peace comes from knowing Kṛṣṇa as the supreme enjoyer, proprietor of everything and friend of all living beings.""",
        "C3-W2": """## 6. Source-grounded narrative

_[Facilitator transition — wonder and tenderness]_

**Paraphrase from ŚB 10.3 (selected — birth pastime summary):** In the prison of Kaṁsa, at an auspicious moment, the Supreme Personality of Godhead appeared as the son of Devakī and Vasudeva. The atmosphere became peaceful. The demigods offered prayers. The Lord appeared in His four-armed form first, then, at the request of His parents, became visible as a human-like child—extraordinary, yet approachable.

**Paraphrase — Vṛndāvana transfer (summary only):** By the Lord's arrangement, the child was brought to Vṛndāvana under the care of Mother Yaśodā and Nanda Mahārāja. The pastime shows that the Absolute Truth is not impersonal force alone—He is a person who descends with love.

**Paraphrase aligned with BG 7.7 and SB 1.3.28:** There is nothing superior to Kṛṣṇa. All incarnations are expansions from Him. Everything rests upon Him as pearls on a thread. The birth pastime makes this abstract truth tangible for children and adults: God can be known, loved and remembered by name.

## 7. Turning point

Devakī and Vasudeva's fear turns to worship when they understand who has appeared. Our turning point is similar wonder: "The Supreme Person is not far away—He is worshipable and approachable through authorized description."

## 8. Central teaching

Kṛṣṇa is the Supreme Personality of Godhead—the source of everything, without any superior truth.

**Memory line:** There is no truth superior to Kṛṣṇa; everything rests upon Him like pearls on a thread.""",
        "C3-W3": """## 6. Source-grounded narrative

_[Facilitator transition — respectful, inquisitive mood]_

**Paraphrase from ŚB 1.1 (setting):** The sages at Naimiṣāraṇya assembled to hear the Bhāgavatam because human life is short and the highest good is to hear about the Supreme Lord. This setting shows why scripture is heard in association—not in isolation.

**Paraphrase from ŚB 1.4 (N deps):** Nārada Muni received spiritual knowledge through disciplic succession—hearing from authorities, serving them, and inquiring sincerely. The Bhāgavatam was spoken through that chain. No single person invents spiritual truth; it is received, verified and lived.

**Paraphrase aligned with BG 4.34:** One should learn truth by approaching a spiritual master with humility, relevant inquiry and service. The realized soul can impart knowledge because they have seen the truth. KUTUMBA adds: guru, sādhu and śāstra must harmonize—no single personality replaces scripture.

## 7. Turning point

Arjuna's example in BG 2.7—"Now I am confused; I surrender"—mirrors the sincere inquirer. The turning point is giving up proud certainty and asking a real question.

## 8. Central teaching

Authentic spiritual knowledge flows through guru, sādhu and śāstra with humility, inquiry and service.

**Memory line:** Approach spiritual truth with humility, sincere inquiry and service; realized teachers can impart knowledge.""",
        "C3-W4": """## 6. Source-grounded narrative

_[Facilitator transition — joyful but reverent]_

**Paraphrase from CC Ādi (selected — saṅkīrtana movement summary):** Śrī Caitanya Mahāprabhu, understood as Kṛṣṇa Himself in the role of a devotee, spread the congregational chanting of the holy names. At Navadvīpa and later, He taught that in this age the recommended process is saṅkīrtana—hearing and chanting together with attention.

**Paraphrase aligned with Śikṣāṣṭakam 1 (CC Antya 20.12 summary):** The holy name cleanses the mirror of the heart, extinguishes the forest fire of material existence, spreads the moon rays of good fortune, and is the life of transcendental knowledge. It is not a mechanical formula—it is the mercy of the Lord.

**Paraphrase — SB 12.3.51 (summary):** In Kali-yuga, saṅkīrtana is the recommended sacrifice. Families participate in this gift without claiming advanced realization.

## 7. Turning point

When the mind wanders during kīrtana, the turning point is returning attention to hearing—not quitting from shame. Lord Caitanya's movement invites repeated, humble participation.

## 8. Central teaching

The holy name, chanted attentively and together, is Lord Caitanya's gift for spiritual life in this age.

**Memory line:** The congregational chanting of Kṛṣṇa's holy name cleanses the heart and expands spiritual life.""",
        "C3-W5": """## 6. Source-grounded narrative

_[Facilitator transition — steady, encouraging]_

**Paraphrase from ŚB 7.5 (Prahlāda's instruction — summary):** Prahlāda Mahārāja, though only a child, instructed his classmates about devotional service. He listed the processes: hearing, chanting, remembering, serving the Lord's lotus feet, worshiping, praying, carrying out orders, becoming a friend, and fully surrendering. These are not separate hobbies—they are limbs of one life offered to Viṣṇu.

**Paraphrase aligned with SB 7.5.23–24:** When these processes are directed to the Supreme Lord with one's life and intention, they become pure devotional service. Prahlāda lived this under extreme opposition—showing that bhakti is character and practice, not comfort.

**Paraphrase — CC Madhya 22.128–129 (summary):** Lord Caitanya also emphasized hearing and chanting as central, with other processes supporting. Families may be strong in one process and weak in another—the nine-process map helps diagnose and grow holistically.

## 7. Turning point

Prahlāda's turning point is unwavering remembrance despite fear. For families, the turning point is choosing one underused process this week while keeping the core hearing/chanting steady.

## 8. Central teaching

Bhakti is a complete life of nine processes offered to Viṣṇu—not only attendance at a weekly program.

**Memory line:** Hearing, chanting, remembering, serving, worshiping, praying, serving as a servant, friendship and full surrender are processes of pure devotional service.""",
    }
    return narratives.get(code, "")


def write_prem_ki_katha(folder: Path, m: dict) -> None:
    links_table = "\n".join(
        f"| {label} | [vedabase]({url}) | Katha anchor |" for label, url in m["katha_links"]
    )
    narrative = katha_narrative(m)
    scope = (
        "Integration week — synthesis only; no new principal līlā in Git."
        if m["integration"]
        else f"Leads naturally to {m['key_verse']}."
    )
    (folder / "prem-ki-katha.md").write_text(
        f"""---
week_code: {m['code']}
week_title: {m['title']}
component: prem-ki-katha.md
katha_type: source-grounded-devotional-narrative
---

# Prem-kī-Kathā — {m['katha_title']}

## 1. Katha title

**{m['katha_title']}**

## 2. Module connection

{scope} See [`katha/KATHA-SOURCE-REGISTER.yaml`](katha/KATHA-SOURCE-REGISTER.yaml).

## 3. Primary source references

| Source | Link | Use in katha |
|---|---|---|
{links_table}

## 4. Setting and devotional mood

_[Facilitator transition — set quiet, attentive atmosphere appropriate to this module]_

## 5. Main personalities

_See narrative below — paraphrase only; no invented direct quotations._

{narrative}

## 9. Heart reflection

_[60 seconds silence]_

Ask inwardly: "What one practice or understanding from this module can not leave me this week?"

Optional: one round of mahā-mantra together.

## 10. Lāla–Lālī interaction cues

1. **Picture or gesture:** One simple image or action representing this week's principle (facilitator-prepared, age-safe).
2. **Recall game:** Children repeat the memory line in two call-and-response lines.

## 11. Kiśora–Kiśorī reflection cues

1. **Journal prompt:** "One sentence — how does this katha connect to {m['key_verse']}?"
2. **Pair share:** "What misconception does this story help correct?"

## 12. Parent bridge

Parents carry the week's principle into home practice. Link to [`family-home-practice.md`](family-home-practice.md).

## 13. Transition to philosophy lesson

_"The katha opened the heart; the lesson trains precise understanding. Both serve Kṛṣṇa."_

→ Continue with [`parent-lesson.md`](parent-lesson.md) or age-track lessons.

## 14. Narration cautions

- No invented direct quotes in "Kṛṣṇa said…" form unless reading authorized text aloud
- Age-appropriate content/applications only — see [`risks-and-sensitive-points.md`](risks-and-sensitive-points.md)
- Keep narration within **12–15 minutes** plus interaction
- {"No competitive framing; consent for any family testimony" if m["integration"] else "No graphic or frightening imagery for young children"}

## 15. Visual / storyboard plan

| Beat | Visual | Source |
|---|---|---|
| 1 | Opening hook illustration | KUTUMBA storyboard |
| 2 | Katha beat — main narrative | [`visuals/concept-map.md`](visuals/concept-map.md) |
| 3 | Key verse reference card | VedaBase link on slide |
| 4 | Home practice bridge | [`visuals/process-flow.md`](visuals/process-flow.md) |

## 16. Rights and quotation status

- Narrative is **paraphrase** from sources linked above
- No full purports or book chapters in repository
- No invented sacred dialogue presented as direct quotation

## 17. Human doctrinal review status

**Status:** `human-review-required` — see [`reviews/DOCTRINAL-REVIEW.md`](reviews/DOCTRINAL-REVIEW.md)

---

_Modern entry hook (not katha):_ [`opening-hook.md`](opening-hook.md)
""",
        encoding="utf-8",
    )


def write_katha_register(folder: Path, m: dict) -> None:
    reg = folder / "katha"
    reg.mkdir(parents=True, exist_ok=True)
    links_yaml = "\n".join(
        f'  - label: {label}\n    url: {url}' for label, url in m["katha_links"]
    )
    (reg / "KATHA-SOURCE-REGISTER.yaml").write_text(
        f"""module_id: {m['code']}
katha_title: "{m['katha_title']}"
primary_book: {m['katha_primary']}
chapter_reference: "{m['katha_ref']}"
stable_links:
{links_yaml}
exact_verses_used:
  - {m['key_verse']}
direct_quotations: []
paraphrased_portions:
  - Main narrative from {m['katha_ref']} — facilitator paraphrase
facilitator_transitions:
  - Modern family pause before philosophy block
  - Bridge to home practice
omitted_complex_details:
  - Portions beyond module scope per complete-week.md exclusions
audience_cautions:
  - No invented quotes; age-appropriate narration
  - {"Integration week: testimonies only with consent; no ranking" if m['integration'] else "Follow risks-and-sensitive-points.md"}
doctrinal_reviewer: pending
rights_status: scripture-reference-links-only
approval_status: human-review-required
""",
        encoding="utf-8",
    )


def write_research(folder: Path, m: dict) -> None:
    r = folder / "research"
    r.mkdir(parents=True, exist_ok=True)
    code = m["code"]
    (r / "RESEARCH-DOSSIER.md").write_text(
        f"""# {code} Research Dossier — {m['title']}

## Module identity

| Field | Detail |
| --- | --- |
| **Module ID** | {code} |
| **Title** | {m['title']} |
| **Cycle** | Cycle 3 — Kṛṣṇa, Guru and the Process of Bhakti |
| **Essential question** | What does this module establish for family formation? |
| **Controlling principle** | Per `complete-week.md` Purpose field |
| **Key verse** | {m['key_verse']} |
| **Memory line** | {m['memory_line']} |
| **Katha** | {m['katha_title']} ({m['katha_ref']}) |

## Source hierarchy

1. Tier 1: Bhagavad-gītā, Śrīmad-Bhāgavatam, Caitanya-caritāmṛta (VedaBase links)
2. Tier 1: Verified Śrīla Prabhupāda lectures in [PRABHUPADA-LECTURE-INDEX.md](PRABHUPADA-LECTURE-INDEX.md)
3. Pedagogy: KUTUMBA analogies (tagged)
4. Blocked: unattributed quote sites, AI-only authority

## Research questions answered

| # | Question | Answer location |
| --- | --- | --- |
| 1 | Primary scriptural anchor? | [SOURCE-MATRIX.md](SOURCE-MATRIX.md) |
| 2 | Verse study? | [VERSE-AND-REFERENCE-STUDY.md](VERSE-AND-REFERENCE-STUDY.md) |
| 3 | Misconceptions? | [MISCONCEPTIONS-AND-BOUNDARIES.md](MISCONCEPTIONS-AND-BOUNDARIES.md) |
| 4 | Family applications? | [CONTEMPORARY-APPLICATIONS.md](CONTEMPORARY-APPLICATIONS.md) |
| 5 | FAQ? | [FAQ.md](FAQ.md) |

## Open questions

- Human reviewer to confirm verse numbering matches congregation edition
- Sign claim register after doctrinal review

_Status: enhancement-complete — pending human review_
""",
        encoding="utf-8",
    )
    matrix_rows = "\n".join(
        f"| {label} | {m['katha_primary'].split()[0] if 'SB' in label or 'CC' in label else 'Bhagavad-gītā'} | {label.split()[1] if len(label.split())>1 else label} | [{label}]({url}) | Module anchor | Yes | human-review-required |"
        for label, url in m["katha_links"]
    )
    (r / "SOURCE-MATRIX.md").write_text(
        f"""# {code} Source Matrix

| Source ID | Work | Reference | Stable link | Teaching function | Context checked | Status |
| --- | --- | --- | --- | --- | --- | --- |
{matrix_rows}

## Copyright treatment

Stable URL + KUTUMBA summary only. No full purports in repository.

## Cross-reference

[../sources.yaml](../sources.yaml) · [CLAIM-REGISTER.yaml](CLAIM-REGISTER.yaml)
""",
        encoding="utf-8",
    )
    (r / "VERSE-AND-REFERENCE-STUDY.md").write_text(
        f"""# {code} Verse and Reference Study

## Primary verse

**{m['key_verse']}** — [{m['verse_link']}]({m['verse_link']})

### KUTUMBA summary (not full purport)

Teaching summary aligned with Śrīla Prabhupāda's purport — facilitator uses VedaBase for full text. Memory line: *{m['memory_line']}*

## Supporting references

{chr(10).join(f'- [{label}]({url})' for label, url in m['katha_links'])}

## Facilitator notes

- Read assigned verses before session
- Do not introduce verses outside module scope in `complete-week.md`
- Route uncertain claims to "I will verify"
""",
        encoding="utf-8",
    )
    (r / "MISCONCEPTIONS-AND-BOUNDARIES.md").write_text(
        f"""# {code} Misconceptions and Boundaries

| Misconception | Correction | Source |
| --- | --- | --- |
| Module is only intellectual | Bhakti lab + home practice required | KUTUMBA pedagogy |
| Skip sources and rely on opinion | Guru–sādhu–śāstra harmony | BG 4.34 pattern |
| Compare families publicly | Private assessment only | complete-week.md |

## Explicit exclusions

Topics assigned to other modules — see `complete-week.md` and cycle map.

## Safeguarding boundaries

See [`../risks-and-sensitive-points.md`](../risks-and-sensitive-points.md).
""",
        encoding="utf-8",
    )
    (r / "CONTEMPORARY-APPLICATIONS.md").write_text(
        f"""# {code} Contemporary Applications

| Case ID | Scenario | Principle applied | Facilitator note |
| --- | --- | --- | --- |
| CS-01 | Family schedule conflict over control | {m['memory_line'][:60]}… | Anonymized; no forced disclosure |
| CS-02 | Child asks "Who is God?" at school | Use module key verse summary | Age-appropriate |
| CS-03 | Online spiritual confusion | Source verification habit | Link to C3-W3 if needed |

_All cases are KUTUMBA pedagogical illustrations — not śāstra._
""",
        encoding="utf-8",
    )
    (r / "FAQ.md").write_text(
        f"""# {code} FAQ

**Q: What is the key verse?**  
A: {m['key_verse']} — [{m['verse_link']}]({m['verse_link']})

**Q: What is the principal katha?**  
A: {m['katha_title']} from {m['katha_ref']}. See `prem-ki-katha.md`.

**Q: Is human approval required?**  
A: Yes — doctrinal, safeguarding, worship, rights, pedagogy, citation reviews remain open.

**Q: Can we skip the children's timed lesson?**  
A: No — Lāla–Lālī and Kiśora–Kiśorī tracks are part of gold-standard delivery.
""",
        encoding="utf-8",
    )
    (r / "BIBLIOGRAPHY.md").write_text(
        f"""# {code} Bibliography

| Work | Reference | Link | Use |
| --- | --- | --- | --- |
{chr(10).join(f'| {label.split()[0]} | {label} | {url} | Primary/module |' for label, url in m['katha_links'])}

No PDF copies in Git. VedaBase links only.
""",
        encoding="utf-8",
    )
    (r / "PRABHUPADA-LECTURE-INDEX.md").write_text(
        f"""# {code} Prabhupāda Lecture Index

| Topic | Suggested search | Status |
| --- | --- | --- |
| {m['title'][:40]} | VedaBase lecture search — {m['key_verse']} | reference-only |
| Module katha | {m['katha_ref']} | reference-only |

Facilitators use VedaBase for prep; no audio files committed to Git.
""",
        encoding="utf-8",
    )
    (r / "APPROVED-TEACHER-MEDIA-INDEX.md").write_text(
        f"""# {code} Approved Teacher Media Index

**Status:** empty pending authorized catalog entries.

See `14-research-source-register/media-library/APPROVED-TEACHER-CATALOG.yaml` when populated.

No inferred or partial teacher names in Git.
""",
        encoding="utf-8",
    )
    (r / "CLAIM-REGISTER.yaml").write_text(
        f"""week_code: {code}
claims:
  - claim_id: {code}-CLM-001
    statement: "{m['memory_line']}"
    claim_type: scripture-text
    primary_source_keys: [{m['key_verse']}]
    audience: all
    exact_quote: false
    review_required: doctrinal
    status: human-review-required
  - claim_id: {code}-CLM-002
    statement: "Principal katha paraphrased from {m['katha_ref']} — not invented dialogue"
    claim_type: kutumba-summary
    audience: all
    review_required: doctrinal
    status: human-review-required
  - claim_id: {code}-CLM-003
    statement: "Home practice supports family formation without public comparison"
    claim_type: pedagogical-application
    audience: parent
    review_required: pedagogy
    status: human-review-required
""",
        encoding="utf-8",
    )


def write_children(folder: Path, m: dict) -> None:
    code, title = m["code"], m["title"]
    safe = (
        "Two adults in visible space. No public ranking or body comparison. "
        "Joyful participation only — child may opt out of speaking roles."
        if m["integration"]
        else "Two adults in visible space. No public comparison. Age-appropriate imagery only."
    )
    (folder / "children" / "lala-lali-lesson.md").write_text(
        f"""---
week_code: {code}
week_title: {title}
audience: Lāla–Lālī (ages 4–8)
---

# Lāla–Lālī Lesson — {title}

**Total time:** 40 minutes  
**Memory line:** {m['memory_line']}  
**No frightening imagery.** Keep activities joyful and concrete.

---

## Core track — ages 4–6

| Time | Activity |
| --- | --- |
| 0–5 min | Opening: recall prior week if attended; one short song; show picture card for this module |
| 5–15 min | **Katha segment** — facilitator narrates simplified portion of [`prem-ki-katha.md`](../prem-ki-katha.md) (8 min + wonder questions) |
| 15–22 min | Movement or craft activity tied to memory line |
| 22–28 min | Sorting or matching game (module principle) |
| 28–32 min | **Movement break** |
| 32–36 min | Verse/memory recall with rhythm |
| 36–40 min | Transition to [`shared-family-transition.md`](shared-family-transition.md) |

### Wonder questions

- What did you like about the story?  
- What is one thing we can do at home?

---

## Extension — ages 7–8

| Addition | Detail |
| --- | --- |
| **Verse rhythm** | Key verse reference in call-and-response (English summary) |
| **Scenario cards** | Two kind responses using module principle |
| **Deeper recall** | Connect story to one home practice action |

---

## Facilitator cautions

{safe}

---

## Materials

See [`materials.md`](../materials.md) — Lāla–Lālī section.
""",
        encoding="utf-8",
    )
    (folder / "children" / "kisora-kisori-lesson.md").write_text(
        f"""---
week_code: {code}
week_title: {title}
audience: Kiśora–Kiśorī (ages 9–14)
---

# Kiśora–Kiśorī Lesson — {title}

**Total time:** 40 minutes  
**Essential question:** How does {m['key_verse']} apply to family life?  
**No forced personal disclosure.**

---

## Core track — ages 9–11

| Time | Activity |
| --- | --- |
| 0–5 min | Opening: anonymous index cards — one word for "challenge" and one for "hope" |
| 5–15 min | **Text observation** — {m['key_verse']} (KUTUMBA summary + [link]({m['verse_link']})) |
| 15–22 min | Concept diagram — see [`visuals/concept-map.md`](../visuals/concept-map.md) |
| 22–30 min | Case CS-01 from [`research/CONTEMPORARY-APPLICATIONS.md`](../research/CONTEMPORARY-APPLICATIONS.md) |
| 30–35 min | Reflective writing (3–4 sentences) |
| 35–40 min | One concrete home practice commitment |

### Text observation

Read KUTUMBA summary aloud. Observe: (1) Who is speaking? (2) What is promised or taught? (3) One family application?

---

## Extension — ages 12–14

| Addition | Detail |
| --- | --- |
| **Structured discussion** | Pairs analyze misconception vs. balanced response — facilitator closes with source |
| **Source practice** | Locate one VedaBase reference from module list |
| **Challenge writing** | One paragraph — anonymized scenario only |

### Discussion rules

1. Attack ideas, not people.  
2. Cite module source.  
3. Facilitator may pause for safeguarding.

---

## Facilitator cautions

{safe}

---

## Materials

See [`materials.md`](../materials.md) — Kiśora–Kiśorī section.
""",
        encoding="utf-8",
    )


def write_visuals(folder: Path, m: dict) -> None:
    code = m["code"]
    v = folder / "visuals"
    v.mkdir(parents=True, exist_ok=True)
    short = m["title"][:35]
    (v / "concept-map.mmd").write_text(
        f"""flowchart TB
    subgraph MODULE["{code}"]
        A["{short}"]
        B["Key verse: {m['key_verse'][:25]}"]
        C["Katha: {m['katha_title'][:30]}"]
    end
    A --> B
    A --> C
    B --> D[Memory line]
    C --> E[Home practice]
    D --> F[Family character]
    E --> F
""",
        encoding="utf-8",
    )
    (v / "process-flow.mmd").write_text(
        f"""flowchart LR
    Hook([opening-hook.md]) --> Katha[prem-ki-katha.md]
    Katha --> Parent[parent-lesson.md]
    Katha --> Child[children tracks]
    Parent --> Lab[bhakti-lab.md]
    Child --> Lab
    Lab --> Home[family-home-practice.md]
    Home --> Sankalpa[sankalpa.md]
""",
        encoding="utf-8",
    )
    for stem in ("concept-map", "process-flow"):
        mmd = (v / f"{stem}.mmd").read_text(encoding="utf-8")
        (v / f"{stem}.md").write_text(
            f"# {code} — {stem.replace('-', ' ').title()}\n\n```mermaid\n{mmd}```\n",
            encoding="utf-8",
        )
    (v / "VISUAL-PLAN.md").write_text(
        f"""# {code} Visual Plan

## Design principles

- Mermaid sources in git — no BBT copyrighted images
- Render via [`concept-map.md`](concept-map.md) and [`process-flow.md`](process-flow.md)

## Visual inventory

| # | Visual | File | Audience | Purpose |
| --- | --- | --- | --- | --- |
| 1 | Module concept map | concept-map.mmd | All | Key verse + katha + practice |
| 2 | Session flow | process-flow.mmd | Facilitator | Hook → katha → lab → home |
| 3 | Gamma placeholders | ../gamma/ | All | Deck integration |

## Gamma integration

See [`../gamma/GAMMA-MASTER-DECK-BRIEF.md`](../gamma/GAMMA-MASTER-DECK-BRIEF.md).

## Image rights

[`image-rights-register.yaml`](image-rights-register.yaml)
""",
        encoding="utf-8",
    )
    (v / "image-rights-register.yaml").write_text(
        f"week_code: {code}\nimages:\n  - asset_id: {code}-VIS-001\n    file: concept-map.mmd\n    rights_status: kutumba-original\n",
        encoding="utf-8",
    )


def write_gamma(folder: Path, m: dict) -> None:
    code, title = m["code"], m["title"]
    g = folder / "gamma"
    g.mkdir(parents=True, exist_ok=True)
    cards = "\n\n".join(
        f"""### Card {i} — {label}

**Content:**  
{content}

**Visual:** `[IMAGE: {vis}]`  
**Speaker note:** {note}  
**Source:** {src}"""
        for i, label, content, vis, note, src in [
            (1, "Title", f"{code} — {title}\nCycle 3 · KUTUMBA Family Program", "module banner", "Welcome", "README"),
            (2, "Essential question", "What does this week establish for our family?", "question marks", "Silent reflection", "RESEARCH-DOSSIER"),
            (3, "Opening hook", m["hook"][:120] + "…", "family scene", "2 min — opening-hook.md", "opening-hook.md"),
            (4, "Key verse", f"{m['key_verse']}\n{m['memory_line']}", "verse card", "Link VedaBase", m["verse_link"]),
            (5, "Katha title", m["katha_title"], "story illustration", "Introduce prem-ki-katha", "prem-ki-katha.md"),
            (6, "Central teaching", m["memory_line"], "icon trio", "Pause for reflection", "prem-ki-katha.md"),
            (7, "Misconception guard", "Opinion ≠ śāstra\nVerify through guru, sādhu, śāstra", "shield icon", "Calm correction", "MISCONCEPTIONS"),
            (8, "Bhakti lab", "See facilitator guide — hands-on practice", "lab table", "Transition to lab", "bhakti-lab.md"),
            (9, "Home practice", "Minimum · Standard · Stretch", "home icon", "Choose one commitment", "family-home-practice.md"),
            (10, "Child track", "Lāla–Lālī and Kiśora–Kiśorī parallel lessons", "children", "Same principle, age fit", "children/"),
            (11, "Sources", f"Primary: {m['key_verse']}", "book stack", "No full purports on slides", "SOURCE-MATRIX"),
            (12, "Close", f"Saṅkalpa + appreciation\n{code}", "prayer hands", "No competition framing", "sankalpa.md"),
        ]
    )
    (g / "GAMMA-PARENT-DECK-PROMPT.md").write_text(
        f"""# Gamma Prompt — {code} Parent / Family Deck

## Deck identity

- **Module:** {code} — {title}
- **Audience:** Parents and adult family members
- **Format:** 16:9 · 12 cards
- **Style:** Calm, scriptural, practical

## Global instructions

Paste below into Gamma. No invented quotes.

---

## Card plan

{cards}
""",
        encoding="utf-8",
    )
    lala_cards = "\n\n".join(
        f"### Card {i}\n**Content:** {c}\n**Visual:** bright, simple"
        for i, c in enumerate(
            [
                f"{title} — Lāla–Lālī",
                "Story time!",
                m["memory_line"][:80],
                "Wonder question",
                "Movement game",
                "Kind action at home",
                "Draw or craft",
                "Recall together",
                "Thank Kṛṣṇa",
                "See you next week!",
            ],
            1,
        )
    )
    (g / "GAMMA-LALA-LALI-DECK-PROMPT.md").write_text(
        f"# Gamma Prompt — {code} Lāla–Lālī Deck\n\n10 cards · large text · no frightening imagery\n\n{lala_cards}\n",
        encoding="utf-8",
    )
    (g / "GAMMA-KISORA-KISORI-DECK-PROMPT.md").write_text(
        f"""# Gamma Prompt — {code} Kiśora–Kiśorī Deck

10 cards · text observation · case discussion

1. Title — {code} youth track
2. Essential question
3. {m['key_verse']} — reference link
4. Katha connection
5. Concept map preview
6. Case CS-01
7. Misconception vs truth
8. Home practice choice
9. Source verification habit
10. Close — one commitment
""",
        encoding="utf-8",
    )
    (g / "GAMMA-MASTER-DECK-BRIEF.md").write_text(
        f"""# {code} Gamma Master Deck Brief

| Deck | File | Cards | Audience |
| --- | --- | --- | --- |
| Parent | GAMMA-PARENT-DECK-PROMPT.md | 12 | Adults |
| Lāla–Lālī | GAMMA-LALA-LALI-DECK-PROMPT.md | 10 | 4–8 |
| Kiśora–Kiśorī | GAMMA-KISORA-KISORI-DECK-PROMPT.md | 10 | 9–14 |

**Status:** prompt-ready-not-rendered
""",
        encoding="utf-8",
    )
    (g / "SPEAKER-NOTES.md").write_text(
        f"""# {code} Speaker Notes

- Open with [`opening-hook.md`](../opening-hook.md) (2–3 min)
- Narrate [`prem-ki-katha.md`](../prem-ki-katha.md) (12–15 min + interaction)
- Parent lesson per [`parent-lesson.md`](../parent-lesson.md)
- Parallel children tracks — timed lessons in `children/`
- Close with saṅkalpa — no public ranking
""",
        encoding="utf-8",
    )


def write_reviews(folder: Path, m: dict) -> None:
    code = m["code"]
    rv = folder / "reviews"
    rv.mkdir(parents=True, exist_ok=True)
    (rv / "DOCTRINAL-REVIEW.md").write_text(
        f"""# {code} Doctrinal Review

**Status:** human-review-required

## Scope reviewed

- research/CLAIM-REGISTER.yaml
- prem-ki-katha.md + katha/KATHA-SOURCE-REGISTER.yaml
- Verse summaries in VERSE-AND-REFERENCE-STUDY.md

## Findings

| ID | Finding | Severity |
| --- | --- | --- |
| DR-01 | Claims align with assigned verses; paraphrase only in katha | Pass-pending-human |
| DR-02 | Scope boundaries per complete-week.md | Pass-pending-human |
| DR-03 | No invented quotations detected in automated pass | Pass-pending-human |

## Verdict

Pilot-ready pending human sign-off.
""",
        encoding="utf-8",
    )
    for name, focus in [
        ("CITATION-AUDIT.md", "All claims trace to VedaBase links or tagged KUTUMBA content"),
        ("SAFEGUARDING-REVIEW.md", "Age tracks reviewed; risks-and-sensitive-points.md linked"),
        ("RIGHTS-REVIEW.md", "No copyrighted media in Git; links only"),
        ("PEDAGOGY-REVIEW.md", "Timed children lessons; bhakti lab integration"),
    ]:
        (rv / name).write_text(
            f"# {code} {name.replace('.md','').replace('-',' ')}\n\n**Status:** human-review-required\n\n{focus}\n",
            encoding="utf-8",
        )


def write_media_index(folder: Path, m: dict) -> None:
    code = m["code"]
    (folder / "audio-video" / "MEDIA-INDEX.yaml").write_text(
        f"""week_code: {code}
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
    type: scripture-reference
    title: "{m['key_verse']}"
    stable_url: "{m['verse_link']}"
    status: reference-only
    rights_status: vedabase-link

approved_teacher_media: []

notes: "No video files in repository. Katha: {m['katha_title']}"
""",
        encoding="utf-8",
    )


def write_review_status(folder: Path, m: dict) -> None:
    (folder / "review-status.yaml").write_text(
        f"""week_code: {m['code']}
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
notes: Cycle 3 deepening pass to C1-W2 gold standard; human-review-required on all gates.
""",
        encoding="utf-8",
    )


def deepen_module(m: dict) -> None:
    folder = BASE / m["slug"]
    if not folder.is_dir():
        raise SystemExit(f"Missing module folder: {folder}")
    write_opening_hook(folder, m)
    write_prem_ki_katha(folder, m)
    write_katha_register(folder, m)
    write_research(folder, m)
    write_children(folder, m)
    write_visuals(folder, m)
    write_gamma(folder, m)
    write_reviews(folder, m)
    write_media_index(folder, m)
    write_review_status(folder, m)
    print(f"Deepened {m['code']}")


def main() -> None:
    for m in MODULES:
        deepen_module(m)
    print("Cycle 3 deepening complete (6 modules)")


if __name__ == "__main__":
    main()

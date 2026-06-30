#!/usr/bin/env python3
"""Build module_curriculum_data.yaml content for V5 curriculum pass."""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "scripts" / "sources"))
sys.path.insert(0, str(REPO / "scripts" / "curriculum"))

from c1_gold_modules import MODULES as C1  # noqa: E402
from cycle2_gold_content import MODULES as C2  # noqa: E402
from map_sources_to_modules import MODULE_SPECS  # noqa: E402

TODAY = date.today().isoformat()
VB = "https://vedabase.io/en/library"
INTEGRATION = {"C1-W6", "C2-W6", "C3-W6"}


def src(label: str, url: str, use: str) -> dict:
    return {"label": label, "url": url, "use": use}


def book(ref: str, url: str, use: str) -> dict:
    return {"ref": ref, "url": url, "use": use}


def lec(media_id: str, dt: str, place: str, title: str, url: str, topic: str) -> dict:
    return {"media_id": media_id, "date": dt, "place": place, "title": title, "url": url, "topic": topic, "segment": "full lecture"}


def claim(text: str, ref: str, url: str, use: str) -> dict:
    return {"claim": text, "source_ref": ref, "url": url, "module_use": use}


def term(t: str, plain: str) -> dict:
    return {"term": t, "plain": plain}


def default_newcomer(mid: str, title: str, minimum: str, define: list, defer: list, key_verse: str, key_url: str, lab: str, home: str, sensitive: str, follow: str) -> dict:
    return {
        "minimum_concept": minimum,
        "terms_define": define,
        "terms_defer": defer,
        "reduced_source_load": f"Read KUTUMBA summary of [{key_verse}]({key_url}) aloud; optional VedaBase after session. One analogy only.",
        "parent_participation": "Observe bhakti lab or join host family pair; no forced public sharing.",
        "lala_lali_placement": "Newcomer children join Lāla–Lālī with host buddy; simplified recall line on card.",
        "kisora_kisori_placement": "Teens may observe or join pair discussion; journal optional.",
        "lab_adaptation": f"Minimum version of {lab}: one demonstrated step, opt-out allowed.",
        "home_practice_minimum": home,
        "sensitive_topic_caution": sensitive,
        "host_family_action": "Greet; share glossary slip; sit together; explain participation options.",
        "setu_bridge": "Apply Setu: reduce Sanskrit, explain once, no pressure to chant long rounds; link `10-kutumba-setu/GAP-RECORD.md`.",
        "follow_up_path": follow,
    }


def sources_from_gold(m: dict) -> list:
    out = []
    for item in m.get("sources", []):
        if len(item) >= 5:
            out.append(book(f"{item[1]} {item[2]}", item[3], item[4]))
    return out


def lectures_from_gold(m: dict) -> list:
    out = []
    for item in m.get("lectures", []):
        if len(item) >= 6:
            out.append(lec(item[0], item[1], item[2], item[3], item[5], item[4]))
    return out


def claims_from_gold(m: dict) -> list:
    out = []
    for item in m.get("claims", []):
        if len(item) >= 4:
            keys = item[3]
            url = m.get("key_verse_url", VB)
            if isinstance(keys, list) and keys:
                sk = m.get("sources", [])
                for s in sk:
                    if s[0] == keys[0]:
                        url = s[3]
                        break
            out.append(claim(item[1], keys[0] if isinstance(keys, list) and keys else item[0], url, "Parent / youth lesson"))
    return out


def katha_links_from_gold(m: dict) -> list:
    if "katha_links" in m:
        return [src(a, b, "Katha anchor") for a, b in m["katha_links"]]
    verses = m.get("verses", [])
    if verses:
        return [src(v[0], v[1], "Key verse") for v in verses[:4]]
    return [src(m.get("key_verse", ""), m.get("key_verse_url", VB), "Anchor")]


def narrative_from_paraphrase(m: dict, extra: list[str] | None = None) -> list[str]:
    paras = []
    if "katha_paraphrase" in m:
        for p in m["katha_paraphrase"]:
            paras.append(f"**Paraphrase (source-grounded):** {p}")
    elif m.get("katha_type") == "facilitator-synthesis":
        paras = [
            "**Paraphrase — integration synthesis (no new principal līlā):** Facilitator recalls prior modules in cycle order, linking memory lines only.",
            f"**Paraphrase — {m.get('controlling_principle', 'cycle synthesis')}** Families choose one practice to continue through the off week.",
        ]
    else:
        paras = [f"**Paraphrase from {m.get('katha_source', m.get('katha_primary', 'śāstra'))} (summary):** See controlling sources in register."]
    if extra:
        paras.extend(extra)
    return paras


def pad_narrative(paras: list[str], mid: str, memory: str, mood: str, m: dict | None = None) -> list[str]:
    """Ensure substantive narrative depth for standard modules."""
    m = m or {}
    key = m.get("key_verse", "the key verse")
    scope = m.get("scope", "this week's teaching")
    extras = [
        f"**Facilitator transition — {mood}:** Pause. Invite families to listen as students of Kṛṣṇa — not to win arguments, but to receive merciful instruction through authorized sources.",
        f"**Paraphrase — setting the heart:** Before precise philosophy, the heart needs a real scene: persons, struggle, and turning toward the Lord. This katha supplies that scene for **{mid}** without inventing dialogue.",
        f"**Paraphrase — {key} (application summary):** The verse is not a slogan. It names a distinction families can practice this week: see {scope} in one honest situation at home.",
        f"**Paraphrase — memory line practice:** Repeat together: _{memory}_ — then name one place this week the line might actually help (mealtime, bedtime, conflict, service).",
        "**Paraphrase — Lāla–Lālī bridge:** Children learn the same truth through picture, gesture, and recall — not through frightening detail or public testing.",
        "**Paraphrase — Kiśora–Kiśorī bridge:** Youth connect the narrative to one contemporary case (fictional in group work) and one private journal sentence — boundaries respected.",
        "**Paraphrase — parent bridge:** Parents need not perform perfect devotion. They model willingness to hear, repair when wrong, and return to practice next week.",
        "**Paraphrase — safeguarding:** Honor grief, fear, and confusion where present. Philosophy serves compassion; it does not shut down feeling or professional care when needed.",
        "**Paraphrase — rights posture:** All narrative here is **paraphrase** with VedaBase links. Facilitators do not present invented quotes as śāstra or Prabhupāda's exact words.",
        "**Paraphrase — transition to lesson:** The katha opens the heart; the philosophy block trains precise language. Both serve Kṛṣṇa — neither replaces the other.",
        f"**Paraphrase — home practice seed:** Before leaving, each family names one trigger (time, place, or event) for the minimum practice connected to {mid}.",
        "**Paraphrase — closing posture:** End with one round of mahā-mantra or silent prayer — families leave with warmth, not information overload.",
    ]
    if mid in INTEGRATION:
        extras = [
            "**Paraphrase — integration exception (documented):** This week synthesizes prior modules. No new principal līlā is introduced in the repository.",
            "**Paraphrase — station recall:** Families rotate through memory-line stations or consent-based shares — not competitive presentations.",
            f"**Paraphrase — continuity:** Choose one practice from the cycle to continue: {memory}",
            "**Paraphrase — offering mood:** Integration is gratitude and honest review — what actually changed at home?",
            "**Paraphrase — preview:** Name the next cycle theme briefly without overwhelming newcomers.",
            "**Paraphrase — consent:** Any family share requires explicit consent; facilitator stops comparison or ranking immediately.",
            "**Paraphrase — thirty-day baseline:** Choose one realistic practice — smaller than the mela display, but steady.",
        ]
    out = list(paras)
    for e in extras:
        if e not in out:
            out.append(e)
    return out


def build_katha_block(m: dict, mid: str, extra_narrative: list[str] | None = None, integration: bool = False) -> dict:
    title = m.get("katha_title", m.get("title", ""))
    memory = m.get("memory_line", "")
    paras = pad_narrative(narrative_from_paraphrase(m, extra_narrative), mid, memory, "quiet devotional mood", m)
    if integration:
        paras = pad_narrative(
            [
                "**Paraphrase — integration exception (documented):** This module synthesizes prior weeks without introducing a new principal līlā in the repository.",
                f"**Paraphrase — cycle review:** Facilitator recalls memory lines and one family-chosen practice. Scope: {m.get('scope', 'integration')}.",
                "**Paraphrase — offering mood:** Families share only with consent — no competition, scoring, or forced testimony.",
                "**Paraphrase — continuity:** Choose one minimum home practice for the off week; preview next cycle briefly.",
            ] + (extra_narrative or []),
            mid,
            memory,
            "gratitude and honest review",
            m,
        )

    return {
        "title": title,
        "subtitle": m.get("katha_chapter", m.get("katha_source", "source-grounded narrative")),
        "katha_type": "facilitator-synthesis" if integration or m.get("katha_type") == "facilitator-synthesis" else "source-grounded-devotional-narrative",
        "module_connection": m.get("controlling_principle", f"Leads to {m.get('key_verse', 'key verse')}."),
        "scope_boundary": m.get("exclusions", "See parent-lesson.md"),
        "primary_sources": katha_links_from_gold(m),
        "primary_book": m.get("katha_primary", m.get("katha_source", "See sources")),
        "chapter_reference": m.get("katha_chapter", ""),
        "personalities": [{"name": "Figures from śāstra", "role": "as named in paraphrase — no invented dialogue"}, {"name": "KUTUMBA families", "role": "listening together today"}],
        "setting": "_[Facilitator transition — quiet room, families seated together]_",
        "narrative_paragraphs": paras,
        "turning_point": m.get("turning_point", "Willingness to hear and adjust — turning toward Kṛṣṇa and śāstra together."),
        "central_teaching": memory or m.get("controlling_principle", ""),
        "memory_line": memory,
        "lala_cues": [
            f"**Chariot/picture cue:** {m.get('lala_story', 'Simple story picture tied to memory line.')}",
            f"**Recall game:** {m.get('lala_memory', m.get('lala_recall', 'Repeat memory line in call-and-response.'))}",
            f"**Safeguarding:** {m.get('lala_safeguarding', 'Age-safe content only; two adults in visible space.')}",
        ],
        "kisora_cues": [
            "**Journal prompt:** 'One sentence — how does this katha connect to the key verse and to a situation I face?'",
            "**Pair share:** 'What misconception does this story help correct? What would responsibility with Kṛṣṇa look like?'",
            "**Source note:** Read KUTUMBA summary + VedaBase link — no invented purports in session.",
        ],
        "parent_bridge": (
            f"Parents carry the week's principle into home practice. Link to [`family-home-practice.md`](family-home-practice.md) "
            f"and {m.get('bhakti_lab', 'bhakti-lab.md')}. When children ask hard questions, turn toward śāstra together — "
            "permission to not have every answer immediately."
        ),
        "cautions": m.get("katha_cautions", ["No invented sacred dialogue", "Age-appropriate delivery"]),
        "visual_beats": [
            {"visual": "Opening hook illustration", "source": "opening-hook.md"},
            {"visual": "Katha beat diagram", "source": "visuals/concept-map.md"},
            {"visual": "Key verse card", "source": "VedaBase link"},
        ],
        "exact_verses": [v[0] for v in m.get("verses", [])[:4]],
        "paraphrased_portions": [p.replace("**Paraphrase (source-grounded):** ", "")[:120] for p in paras[:3]],
        "omitted": m.get("katha_omitted", []),
    }


def spec_for(mid: str) -> dict:
    for s in MODULE_SPECS:
        if s["module_id"] == mid:
            return s
    return {}


def transform_gold(slug: str, m: dict, extra_katha: list[str] | None = None) -> dict:
    mid = m["code"]
    integration = mid in INTEGRATION
    kv = m.get("key_verse", "")
    ku = m.get("key_verse_url", m.get("verses", [["", VB]])[0][1] if m.get("verses") else VB)

    se = {
        "controlling_books": sources_from_gold(m) or [book(b, f"{VB}/", "Controlling reference") for b in spec_for(mid).get("controlling_books", [])],
        "lectures": lectures_from_gold(m),
        "katha_sources": sources_from_gold(m)[:6],
        "education": [src("ISKCON Education", u, "Pedagogy") for u in spec_for(mid).get("education", [])],
        "child_resources": ["ISKCON Education books-for-kids — metadata only; KUTUMBA adaptation required"],
        "media": [src("Media", u, "Candidate") for u in spec_for(mid).get("media", [])],
        "supplementary": spec_for(mid).get("supplementary", []),
        "excluded": spec_for(mid).get("excluded", []),
        "claim_mapping": claims_from_gold(m) or [claim(m.get("controlling_principle", ""), kv, ku, "Core teaching")],
        "tier_a_urls": spec_for(mid).get("vedabase", [VB]),
    }

    newcomer = default_newcomer(
        mid,
        m["title"],
        m.get("controlling_principle", m.get("essential_question", "")),
        [term(m.get("lala_sanskrit", "key term").split("—")[0].strip(), m.get("lala_recall", m.get("lala_memory", m.get("memory_line", "see parent lesson"))))],
        [x.strip() for x in m.get("exclusions", "").split(";") if x.strip()],
        kv,
        ku,
        m.get("bhakti_lab", "bhakti lab"),
        m.get("home_practice", "One minimum home step from family-home-practice.md"),
        m.get("lala_safeguarding", "Route sensitive topics privately; no public disclosure pressure."),
        m.get("leads_to", "Continue next module in cycle order."),
    )

    return {
        "module_id": mid,
        "slug": slug,
        "title": m["title"],
        "source_expansion": se,
        "newcomer": newcomer,
        "katha": build_katha_block(m, mid, extra_katha, integration),
    }


# --- V5 corrected katha extensions ---
C3_W1_EXTRA = [
    "**Paraphrase from ŚB 10.24.7–10.24.19:** In Vṛndāvana, Nanda Mahārāja and the residents prepared to worship Lord Indra for rainfall. Young Kṛṣṇa questioned this custom with gentle logic, showing that their real wealth — land, cows, children, and Govardhana Hill — comes from the Lord's arrangement. He instructed them to worship Govardhana Hill, which nourishes them, as an offering to Him.",
    "**Paraphrase from ŚB 10.25.9:** When Indra sent devastating rains, Kṛṣṇa lifted Govardhana Hill on His little finger and sheltered the entire community for seven days. The residents saw that no demigod is independent of the Supreme Lord.",
    "**Paraphrase aligned with BG 5.29:** Kṛṣṇa is the supreme enjoyer of sacrifice, proprietor of all planets, and well-wishing friend of every living being. The Govardhana pastime makes this visible: forgetting the Lord's proprietorship increases anxiety; remembering Him restores stewardship.",
]

C3_W2_EXTRA = [
    "**Paraphrase from ŚB 10.3.1–10.3.43 (Mathurā appearance — summary):** In the prison of Kaṁsa at Mathurā, at an auspicious moment, the Supreme Personality of Godhead appeared as the son of Devakī and Vasudeva. The atmosphere became peaceful; demigods offered prayers. The Lord appeared in His four-armed form first, then, at the request of His parents, became visible as a human-like child — extraordinary yet approachable.",
    "**Paraphrase — transfer to Gokula (summary):** By the Lord's arrangement, the child was brought to Gokula under the care of Mother Yaśodā and Nanda Mahārāja. Geography is taught carefully: appearance in Mathurā; childhood pastimes in Vraja under parental care.",
    "**Paraphrase aligned with BG 7.7 and SB 1.3.28:** There is nothing superior to Kṛṣṇa; all incarnations expand from Him; everything rests upon Him as pearls on a thread.",
]

C3_W3_EXTRA = [
    "**Paraphrase from ŚB 1.5 (Nārada instructs Vyāsa — summary):** Vyāsadeva, although the compiler of Vedic literature, felt dissatisfied. Nārada Muni arrived and explained that without directly describing the Supreme Lord's transcendental pastimes, literature cannot fully satisfy the heart or cut material bondage.",
    "**Paraphrase from ŚB 1.6 (Nārada's childhood — summary):** Nārada received spiritual impression through association with devotees in his early life — showing that knowledge is received through mercy and association, not self-invention.",
    "**Paraphrase aligned with BG 4.34:** Learn truth by approaching a spiritual master with humility, relevant inquiry, and service. Guru, sādhu, and śāstra must harmonize — no single personality replaces scripture.",
]

C1_W1_EXTRA = [
    "**Paraphrase from ŚB 1.1 (summary):** At Naimiṣāraṇya, sages led by Śaunaka gathered after Kṛṣṇa's departure. They inquired how to act in Kali — opening the Bhāgavatam.",
    "**Paraphrase aligned with SB 1.2.18:** Regular hearing and service cleanse the heart and fix devotion — KUTUMBA's weekly protected time.",
]

C1_W3_EXTRA = [
    "**Paraphrase from SB 5.10–5.11 (Jaḍa Bharata — summary):** King Rahūgaṇa treated the palanquin bearer as mere body; Jaḍa Bharata replied with spiritual wisdom — the soul is distinct from the covering.",
    "**Paraphrase aligned with BG 2.20:** The soul is unborn and eternal — positive identity beyond 'not the body.'",
]

C1_W4_EXTRA = [
    "**Paraphrase from SB 6.1–6.2 (Mṛgāri — summary):** Nārada's mercy transformed a cruel hunter — human intelligence can turn toward Kṛṣṇa.",
    "**Paraphrase aligned with SB 11.9.29:** Human life is rare, temporary, and able to deliver the highest value.",
]

C1_W5_EXTRA = [
    "**Paraphrase from SB 4.8–4.9 (Dhruva — summary):** Dhruva sought temporary power but learned permanent shelter in Kṛṣṇa's lotus feet.",
    "**Paraphrase aligned with BG 8.15:** The material world is temporary; returning to Kṛṣṇa is the goal.",
]


def build_c1_w2_brief_only() -> dict:
    """C1-W2: deepen source brief; preserve gold pilot katha/newcomer."""
    m = C1["c1-w2-i-am-not-this-body"] if "c1-w2-i-am-not-this-body" in C1 else None
    # C1-W2 not in C1_MODULES (gold pilot) — build from MODULE_SPECS
    se = {
        "controlling_books": [
            book("BG 2.13", f"{VB}/bg/2/13/", "Life stages — dehī/deha"),
            book("BG 2.22", f"{VB}/bg/2/22/", "Garment analogy"),
            book("BG 13.1", f"{VB}/bg/13/1/", "Field and knower introduction"),
            book("BG 13.2", f"{VB}/bg/13/2/", "Field/knower distinction"),
            book("BG 13.3", f"{VB}/bg/13/3/", "Knowers summarized"),
        ],
        "lectures": [
            lec("SP-LEC-BG-2-13-1973", "1973-08-07", "London", "BG 2.13 lecture", f"{VB}/lectures/london/august/07/1973/7310807BG.LON_eng/", "dehī/deha life stages"),
            lec("SP-LEC-BG-2-22-1973", "1973-08-22", "London", "BG 2.22 lecture", f"{VB}/lectures/london/august/22/1973/7310822BG.LON_eng/", "Garment analogy"),
        ],
        "katha_sources": [book("BG 2.11–2.13", f"{VB}/bg/2/13/", "Gold pilot katha — locked")],
        "education": [src("ISKCON Education materials", "https://iskconeducation.org/materials/", "Parent resources")],
        "child_resources": ["Sunday School indexes — metadata only"],
        "media": [],
        "supplementary": [],
        "excluded": ["Anonymous quote pages without Vanisource context"],
        "claim_mapping": [
            claim("Embodied self passes through life stages", "BG 2.13", f"{VB}/bg/2/13/", "C1-W2 memory line"),
            claim("Soul changes bodies as garments", "BG 2.22", f"{VB}/bg/2/22/", "Analogy — defer full transmigration to C1-W3"),
            claim("Field and knower distinguished", "BG 13.1-3", f"{VB}/bg/13/1/", "Parent extension only"),
        ],
        "tier_a_urls": [f"{VB}/bg/", f"{VB}/transcripts/"],
    }
    return {
        "module_id": "C1-W2",
        "slug": "c1-w2-i-am-not-this-body",
        "title": "I Am Not This Body",
        "source_expansion": se,
        "newcomer": default_newcomer("C1-W2", "I Am Not This Body", "Gold pilot — preserved if substantive on disk", [], [], "BG 2.13", f"{VB}/bg/2/13/", "Identity pause", "Identity pause minimum", "No body-image forced sharing", "C1-W3"),
        "katha": {"title": "LOCKED — gold pilot", "memory_line": "The body changes from childhood to old age, but the conscious self continues."},
    }


def build_c3_modules() -> list[dict]:
    out = []
    c3_data = {
        "c3-w1-who-is-god-the-supreme-enjoyer-proprietor-and-friend": {
            "code": "C3-W1", "title": "Who Is God? The Supreme Enjoyer, Proprietor and Friend",
            "memory_line": "Peace comes from knowing Kṛṣṇa as the supreme enjoyer, proprietor of everything and friend of all living beings.",
            "controlling_principle": "Kṛṣṇa is supreme enjoyer, proprietor, and friend — stewardship replaces possessiveness.",
            "key_verse": "BG 5.29", "key_verse_url": f"{VB}/bg/5/29/",
            "katha_title": "Kṛṣṇa lifts Govardhana — stewardship and supreme proprietorship",
            "katha_primary": "Śrīmad-Bhāgavatam 10.24–10.25", "katha_chapter": "SB 10.24 Govardhana; SB 10.25 protection",
            "katha_links": [
                ("SB 10.24.7", f"{VB}/sb/10/24/7/"),
                ("SB 10.24.19", f"{VB}/sb/10/24/19/"),
                ("SB 10.25.9", f"{VB}/sb/10/25/9/"),
                ("BG 5.29", f"{VB}/bg/5/29/"),
            ],
            "katha_paraphrase": [p.split(":** ", 1)[-1] for p in C3_W1_EXTRA],
            "bhakti_lab": "Stewardship Inventory", "home_practice": "Three peace questions before one conflict-prone activity.",
            "exclusions": "SB 10.14 mislabeled as Govardhana; demigod minimization without respect",
            "leads_to": "C3-W2 — who Kṛṣṇa is as Supreme Person",
            "sources": [("BG-5-29", "Bhagavad-gītā", "5.29", f"{VB}/bg/5/29/", "Enjoyer, proprietor, friend"), ("SB-10-24", "ŚB", "10.24", f"{VB}/sb/10/24/7/", "Govardhana instruction")],
            "lectures": [("SP-LEC-BG-5-29-1973", "1973-08-15", "London", "BG 5.29", "Peace formula", f"{VB}/lectures/august/15/1973/730815BG.LON_eng/")],
            "verses": [("BG 5.29", f"{VB}/bg/5/29/", "Supreme enjoyer, proprietor, friend")],
        },
        "c3-w2-who-is-kṛṣṇa-the-supreme-personality-of-godhead": {
            "code": "C3-W2", "title": "Who Is Kṛṣṇa? The Supreme Personality of Godhead",
            "memory_line": "There is no truth superior to Kṛṣṇa; everything rests upon Him like pearls on a thread.",
            "controlling_principle": "Kṛṣṇa is the Supreme Personality of Godhead — a person we can know and love.",
            "key_verse": "BG 7.7", "key_verse_url": f"{VB}/bg/7/7/",
            "katha_title": "Kṛṣṇa's appearance in Mathurā and transfer to Gokula",
            "katha_primary": "ŚB 10.3", "katha_chapter": "SB 10.3 appearance; Gokula transfer",
            "katha_links": [("SB 10.3.1", f"{VB}/sb/10/3/1/"), ("BG 7.7", f"{VB}/bg/7/7/")],
            "katha_paraphrase": [p.split(":** ", 1)[-1] for p in C3_W2_EXTRA],
            "bhakti_lab": "Name and Form Respect Practice", "home_practice": "One respectful reference to Kṛṣṇa by name at dinner.",
            "exclusions": "Imprecise Vṛndāvana birth geography; cartoon trivialization",
            "leads_to": "C3-W3 — guru, sādhu, śāstra",
            "sources": [("SB-10-3", "ŚB", "10.3", f"{VB}/sb/10/3/1/", "Birth pastime"), ("BG-7-7", "BG", "7.7", f"{VB}/bg/7/7/", "No superior truth")],
            "lectures": [],
            "verses": [("BG 7.7", f"{VB}/bg/7/7/", "Supreme truth")],
        },
        "c3-w3-guru-sādhu-and-śāstra-how-we-receive-spiritual-knowledge": {
            "code": "C3-W3", "title": "Guru, Sādhu and Śāstra: How We Receive Spiritual Knowledge",
            "memory_line": "Approach spiritual truth with humility, sincere inquiry and service.",
            "controlling_principle": "Authentic knowledge flows through guru, sādhu and śāstra together.",
            "key_verse": "BG 4.34", "key_verse_url": f"{VB}/bg/4/34/",
            "katha_title": "Nārada instructs Vyāsa — receiving spiritual knowledge",
            "katha_primary": "ŚB 1.5–1.6", "katha_chapter": "SB 1.5 Vyāsa; SB 1.6 Nārada childhood",
            "katha_links": [("SB 1.5.1", f"{VB}/sb/1/5/1/"), ("BG 4.34", f"{VB}/bg/4/34/")],
            "katha_paraphrase": [p.split(":** ", 1)[-1] for p in C3_W3_EXTRA],
            "bhakti_lab": "Three-Lamp Inquiry Practice", "home_practice": "Write one question; ask one mentor respectfully.",
            "exclusions": "SB 1.4.25 as Nārada receiving Bhāgavatam; guru shopping",
            "leads_to": "C3-W4 — Lord Caitanya and holy name",
            "sources": [("SB-1-5", "ŚB", "1.5", f"{VB}/sb/1/5/1/", "Nārada instructs Vyāsa"), ("BG-4-34", "BG", "4.34", f"{VB}/bg/4/34/", "Approach guru")],
            "lectures": [],
            "verses": [("BG 4.34", f"{VB}/bg/4/34/", "Learn by inquiry and service")],
        },
        "c3-w4-śrī-caitanya-mahāprabhu-and-the-holy-name": {
            "code": "C3-W4", "title": "Śrī Caitanya Mahāprabhu and the Holy Name",
            "memory_line": "The congregational chanting of Kṛṣṇa's holy name cleanses the heart and expands spiritual life.",
            "controlling_principle": "Lord Caitanya gave saṅkīrtana as the yuga-dharma — humble, together, attentive.",
            "key_verse": "CC Antya 20.12", "key_verse_url": f"{VB}/cc/antya/20/12/",
            "katha_title": "Lord Caitanya's kīrtana at Navadvīpa",
            "katha_primary": "CC Ādi 7.163; CC Ādi 17.21", "katha_chapter": "Saṅkīrtana movement (selected)",
            "katha_links": [("CC Ādi 7.163", f"{VB}/cc/adi/7/163/"), ("CC Antya 20.12", f"{VB}/cc/antya/20/12/"), ("SB 12.3.51", f"{VB}/sb/12/3/51/")],
            "katha_paraphrase": [
                "Lord Caitanya spread congregational chanting of the holy names — hearing and chanting together with attention.",
                "The holy name cleanses the heart, extinguishes material existence, and is the life of transcendental knowledge (Śikṣāṣṭakam 1 summary).",
                "In Kali-yuga, saṅkīrtana is the recommended sacrifice — families participate without claiming advanced realization.",
                "When the mind wanders, the turning point is returning attention to hearing — not quitting from shame. One humble minute counts.",
            ],
            "bhakti_lab": "Attentive Kīrtana Minute", "home_practice": "One minute attentive chanting daily.",
            "exclusions": "Performance comparison; aparādha detail for Lāla–Lālī",
            "leads_to": "C3-W5 — nine processes",
            "sources": [("CC-A-20-12", "CC", "Antya 20.12", f"{VB}/cc/antya/20/12/", "Śikṣāṣṭakam 1")],
            "lectures": [], "verses": [("CC Antya 20.12", f"{VB}/cc/antya/20/12/", "Holy name cleanses heart")],
        },
        "c3-w5-the-nine-processes-of-bhakti": {
            "code": "C3-W5", "title": "The Nine Processes of Bhakti",
            "memory_line": "Hearing, chanting, remembering, serving, worshiping, praying, serving as a servant, friendship and full surrender are processes of pure devotional service.",
            "controlling_principle": "Bhakti is a complete life of nine processes offered to Viṣṇu.",
            "key_verse": "SB 7.5.23–24", "key_verse_url": f"{VB}/sb/7/5/23/",
            "katha_title": "Prahlāda's nine processes of devotion",
            "katha_primary": "SB 7.5.23–24", "katha_chapter": "Prahlāda instructs classmates",
            "katha_links": [("SB 7.5.23", f"{VB}/sb/7/5/23/"), ("SB 7.5.24", f"{VB}/sb/7/5/24/"), ("BG 9.14", f"{VB}/bg/9/14/")],
            "katha_paraphrase": [
                "Prahlāda listed hearing, chanting, remembering, serving the Lord's lotus feet, worshiping, praying, carrying orders, friendship, and full surrender.",
                "Directed to the Supreme Lord with one's life and intention, these become pure devotional service.",
                "Families may be strong in one process and weak in another — the map helps holistic growth.",
            ],
            "bhakti_lab": "Nine-Process Family Audit", "home_practice": "Strengthen one underused process this week.",
            "exclusions": "Ranking families by process score",
            "leads_to": "C3-W6 — Bhakti Mela",
            "sources": [("SB-7-5-23", "ŚB", "7.5.23", f"{VB}/sb/7/5/23/", "Nine processes")],
            "lectures": [], "verses": [("SB 7.5.23", f"{VB}/sb/7/5/23/", "Chief processes")],
        },
        "c3-w6-bhakti-mela-kīrtana-drama-and-family-presentation": {
            "code": "C3-W6", "title": "Bhakti Mela: Kīrtana, Drama and Family Presentation",
            "memory_line": "These processes become pure devotional service when offered to Viṣṇu with one's life and intention.",
            "controlling_principle": "Six-month synthesis and offering — no new principal līlā.",
            "key_verse": "SB 7.5.23–24 (review)", "key_verse_url": f"{VB}/sb/7/5/23/",
            "katha_title": "Six months of family bhakti — synthesis and offering",
            "katha_type": "facilitator-synthesis",
            "katha_primary": "Cycle 1–3 review", "katha_chapter": "Integration showcase exception",
            "katha_links": [("BG 5.29", f"{VB}/bg/5/29/"), ("BG 7.7", f"{VB}/bg/7/7/"), ("SB 7.5.23", f"{VB}/sb/7/5/23/")],
            "katha_paraphrase": [
                "Facilitator recalls six months: identity, karma, Kṛṣṇa, guru, holy name, nine processes — memory lines only.",
                "Bhakti Mela is an offering, not a competition — families share with consent.",
                "Choose one thirty-day baseline practice to continue.",
            ],
            "bhakti_lab": "Bhakti Mela Rehearsal", "home_practice": "Continue one selected practice thirty days.",
            "exclusions": "Competitive scoring; forced testimony",
            "leads_to": "Year 1 Cycle 4 or protected off week",
            "scope": "Showcase/integration — 600–850 word katha exception documented in frontmatter",
            "sources": [], "lectures": [], "verses": [("SB 7.5.23", f"{VB}/sb/7/5/23/", "Review")],
        },
    }
    for slug, m in c3_data.items():
        extra = {"c3-w1-who-is-god-the-supreme-enjoyer-proprietor-and-friend": C3_W1_EXTRA, "c3-w2-who-is-kṛṣṇa-the-supreme-personality-of-godhead": C3_W2_EXTRA, "c3-w3-guru-sādhu-and-śāstra-how-we-receive-spiritual-knowledge": C3_W3_EXTRA}.get(slug)
        rec = transform_gold(slug, m, extra)
        if slug.startswith("c3-w1"):
            rec["katha"]["primary_sources"] = [
                src("SB 10.24.7", f"{VB}/sb/10/24/7/", "Setting"),
                src("SB 10.24.19", f"{VB}/sb/10/24/19/", "Govardhana worship"),
                src("SB 10.25.9", f"{VB}/sb/10/25/9/", "Hill lifted"),
                src("BG 5.29", f"{VB}/bg/5/29/", "Peace formula"),
            ]
        out.append(rec)
    return out


def build_all_modules() -> dict:
    modules: list[dict] = []

    # C1
    extras = {
        "c1-w1-what-is-kutumba-and-why-are-we-here": C1_W1_EXTRA,
        "c1-w3-the-nature-of-the-soul": C1_W3_EXTRA,
        "c1-w4-why-human-life-is-rare-and-valuable": C1_W4_EXTRA,
        "c1-w5-the-temporary-world-and-the-search-for-permanent-happiness": C1_W5_EXTRA,
    }
    for slug, m in C1.items():
        modules.append(transform_gold(slug, m, extras.get(slug)))

    modules.append(build_c1_w2_brief_only())

    # C2
    for slug, m in C2.items():
        extra = None
        if slug == "c2-w3-birth-death-and-reincarnation":
            extra = [
                "**Paraphrase from SB 5.8–5.9 (Bhārata Mahārāja — summary):** A great king practicing devotion in the forest became attached to a young deer; consciousness at life's end followed that attachment — sober lesson on remembrance.",
                "**Paraphrase aligned with BG 2.22:** As a person changes garments, the soul changes bodies — garment analogy with stated limits.",
            ]
        modules.append(transform_gold(slug, m, extra))

    modules.extend(build_c3_modules())

    # Sort by module_id
    order = {f"C{c}-W{w}": c * 10 + w for c in range(1, 4) for w in range(1, 7)}
    modules.sort(key=lambda x: order.get(x["module_id"], 99))

    return {
        "data_version": "5.0.0",
        "generated": TODAY,
        "source_map_id": "KUT-SRC-0013",
        "module_count": len(modules),
        "locks": {"skip_prem_katha_slug": "c1-w2-i-am-not-this-body", "skip_newcomer_if_substantive": ["C1-W2"]},
        "integration_modules": sorted(INTEGRATION),
        "modules": modules,
    }


if __name__ == "__main__":
    import yaml
    from pathlib import Path as P

    out = P(__file__).parent / "module_curriculum_data.yaml"
    out.write_text(yaml.safe_dump(build_all_modules(), sort_keys=False, allow_unicode=True, width=120), encoding="utf-8")
    print(f"Wrote {out}")

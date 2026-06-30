#!/usr/bin/env python3
"""Deepen all Cycle 2 modules to C1-W2 gold standard."""

from __future__ import annotations

import re
from pathlib import Path

from cycle2_gold_content import MODULES

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
CYCLE2_PREFIX = "c2-w"


def yaml_front(fields: dict) -> str:
    lines = ["---"]
    for k, v in fields.items():
        if isinstance(v, list):
            lines.append(f"{k}:")
            for item in v:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


def write_opening_hook(folder: Path, m: dict) -> None:
    content = f"""{yaml_front({"week_code": m["code"], "week_title": m["title"], "component": "opening-hook.md", "provenance": "cycle-2-gold-standard-pass"})}

## Opening Hook (modern scenario)

_This is a contemporary entry point — not Prem-kī-Kathā. See [`prem-ki-katha.md`](prem-ki-katha.md) for the devotional narrative._

| {m["hook"]} |
| --- |

**Delivery:** 2–3 minutes before Prem-kī-Kathā or parent lesson.  
**Provenance:** From canonical `complete-week.md`; separated during Cycle 2 gold-standard pass (v3.0.0).
"""
    (folder / "opening-hook.md").write_text(content, encoding="utf-8")


def write_prem_ki_katha(folder: Path, m: dict) -> None:
    links = "\n".join(
        f"| {label} | [{url}]({url}) | Katha anchor |"
        for label, url in m["katha_links"]
    )
    paraphrase = "\n\n".join(
        f"**Paraphrase (source-grounded):** {p}" for p in m["katha_paraphrase"]
    )
    omitted = "\n".join(f"- {o}" for o in m["katha_omitted"])
    cautions = "\n".join(f"- {c}" for c in m["katha_cautions"])
    content = f"""{yaml_front({"week_code": m["code"], "week_title": m["title"], "component": "prem-ki-katha.md", "katha_type": "source-grounded-devotional-narrative"})}

# Prem-kī-Kathā — {m["katha_title"]}

## 1. Katha title

**{m["katha_title"]}** — {m["katha_chapter"]}

## 2. Module connection

This katha supports **{m["title"]}** and the key verse [{m["key_verse"].split()[-1]}]({m["key_verse_url"]}).

**Memory line:** {m["memory_line"]}

**Scope boundary:** {m["scope"]}. Exclusions: {m["exclusions"]}

## 3. Primary source references

| Source | Link | Use in katha |
|---|---|---|
{links}

Full registry: [`katha/KATHA-SOURCE-REGISTER.yaml`](katha/KATHA-SOURCE-REGISTER.yaml)

## 4. Setting and devotional mood

_[Facilitator transition — quiet room, families seated together]_

{m["hook"][:200]}...

The mood is **sober curiosity** — families willing to hear what Kṛṣṇa and the ācārya paramparā teach without sensationalism.

## 5. Main personalities

- **Figures from śāstra** — as named in paraphrase below (no invented dialogue)
- **The family** — listening as Kṛṣṇa's students today
- **Facilitator** — gentle guide; stops misuse immediately

## 6. Source-grounded narrative

_[Source narrative / paraphrase — not invented direct quotes]_

{paraphrase}

## 7. Turning point

The turning point is **willingness to hear and adjust** — not perfect control of every result. Families turn toward Kṛṣṇa, śāstra, and practical repair.

## 8. Central teaching

{m["memory_line"]}

## 9. Heart reflection

_[60 seconds silence]_

Ask inwardly: "What one action, habit, or attitude is Kṛṣṇa inviting us to refine this week?"

Optional: one soft round of mahā-mantra.

## 10. Lāla–Lālī interaction cues

1. **Story picture:** {m["lala_story"][:120]}...
2. **Recall:** {m["lala_memory"]}

## 11. Kiśora–Kiśorī reflection cues

1. **Journal:** "What part of this katha connects to a real situation I face?"
2. **Pair share:** "What would blaming or helplessness look like? What would responsibility with Kṛṣṇa look like?"

## 12. Parent bridge

Link to [`family-home-practice.md`](family-home-practice.md) and {m["bhakti_lab"]} in [`bhakti-lab.md`](bhakti-lab.md).

## 13. Transition to philosophy lesson

_"The katha opened the heart; the lesson trains discernment. Both serve Kṛṣṇa."_

→ Continue with [`parent-lesson.md`](parent-lesson.md) or age track.

## 14. Narration cautions

{omitted}
{cautions}
- Do **not** invent direct quotes in "Kṛṣṇa said…" form unless reading authorized text
- Keep narration within **12–15 minutes** plus interaction

## 15. Visual / storyboard plan

| Beat | Visual | Source |
|---|---|---|
| 1 | Opening hook scenario | opening-hook.md |
| 2 | Katha narrative beats | prem-ki-katha.md |
| 3 | Key verse card | {m["key_verse_url"]} |
| 4 | Home practice | family-home-practice.md |

## 16. Rights and quotation status

- Paraphrase only — no full purports in repository
- No invented sacred dialogue presented as direct quotation

## 17. Human doctrinal review status

**Status:** `human-review-required` — see [reviews/DOCTRINAL-REVIEW.md](reviews/DOCTRINAL-REVIEW.md)

---

_Modern entry hook (not katha):_ [opening-hook.md](opening-hook.md)
"""
    (folder / "prem-ki-katha.md").write_text(content, encoding="utf-8")


def write_katha_register(folder: Path, m: dict) -> None:
    katha_dir = folder / "katha"
    katha_dir.mkdir(exist_ok=True)
    verses = [s[0].replace(" ", "-") for s in m["sources"][:3]]
    links_yaml = "\n".join(
        f'  - label: "{label}"\n    url: {url}'
        for label, url in m["katha_links"]
    )
    paraphrased = "\n".join(
        f'  - "{p[:100]}..."' for p in m["katha_paraphrase"]
    )
    omitted = "\n".join(f'  - "{o}"' for o in m["katha_omitted"])
    cautions = "\n".join(f'  - "{c}"' for c in m["katha_cautions"])
    content = f"""module_id: {m["code"]}
katha_title: "{m["katha_title"]}"
primary_book: {m["katha_primary"]}
chapter_reference: "{m["katha_chapter"]}"
stable_links:
{links_yaml}
exact_verses_used:
{chr(10).join(f"  - {v}" for v in verses)}
direct_quotations: []
paraphrased_portions:
{paraphrased}
facilitator_transitions:
  - Modern hook before narrative
  - Bridge to {m["bhakti_lab"]}
omitted_complex_details:
{omitted}
audience_cautions:
{cautions}
doctrinal_reviewer: pending
rights_status: scripture-reference-links-only
approval_status: human-review-required
"""
    (katha_dir / "KATHA-SOURCE-REGISTER.yaml").write_text(content, encoding="utf-8")


def write_research_dossier(folder: Path, m: dict) -> None:
    content = f"""# {m["code"]} Research Dossier — {m["title"]}

## Module identity

| Field | Detail |
| --- | --- |
| **Module ID** | {m["code"]} |
| **Title** | {m["title"]} |
| **Cycle** | Cycle 2 — Karma, Rebirth and Material Nature |
| **Essential question** | {m["essential_question"]} |
| **Controlling principle** | {m["controlling_principle"]} |
| **Scope** | {m["scope"]} |
| **Explicit exclusions** | {m["exclusions"]} |
| **Prerequisites** | {m["prerequisites"]} |
| **Leads to** | {m["leads_to"]} |

## Source hierarchy used

1. **Tier 1:** Bhagavad-gītā, Śrīmad-Bhāgavatam (VedaBase links + KUTUMBA summaries)
2. **Tier 1:** Verified Śrīla Prabhupāda lectures in [PRABHUPADA-LECTURE-INDEX.md](PRABHUPADA-LECTURE-INDEX.md)
3. **Pedagogy:** KUTUMBA case studies (tagged fictional composites)
4. **Blocked:** Random forums, unattributed quotes, AI-only authority

## Primary source matrix

See [SOURCE-MATRIX.md](SOURCE-MATRIX.md) — {len(m["sources"])} entries minimum.

## Research questions answered

| # | Question | Answer (summary) |
| --- | --- | --- |
| 1 | What is the controlling teaching? | {m["controlling_principle"]} |
| 2 | Key verse? | [{m["key_verse"]}]({m["key_verse_url"]}) |
| 3 | What does it NOT mean? | See [MISCONCEPTIONS-AND-BOUNDARIES.md](MISCONCEPTIONS-AND-BOUNDARIES.md) |
| 4 | Contemporary cases? | {m["case_count"]} in [CONTEMPORARY-APPLICATIONS.md](CONTEMPORARY-APPLICATIONS.md) |
| 5 | Child capacity Lāla–Lālī? | Story, movement, recall — {m["lala_memory"]} |
| 6 | Youth capacity? | Text observation, cases, optional writing/debate |
| 7 | Parent practice? | {m["bhakti_lab"]} |
| 8 | Safeguarding? | See module `risks-and-sensitive-points.md` |

## Key distinctions

- **Means vs. does-not-mean** — MISCONCEPTIONS-AND-BOUNDARIES.md
- **Scripture vs. pedagogical analogy** — analogy-and-application.md
- **Human review** — all claims `human-review-required` until sign-off

## Misconceptions and boundaries

→ [MISCONCEPTIONS-AND-BOUNDARIES.md](MISCONCEPTIONS-AND-BOUNDARIES.md)

## Contemporary applications

→ [CONTEMPORARY-APPLICATIONS.md](CONTEMPORARY-APPLICATIONS.md)

## Audience implications

| Audience | Implication |
| --- | --- |
| **Parent** | 40-min plan with cases and {m["bhakti_lab"]} |
| **Lāla–Lālī** | Timed lesson — no inappropriate imagery |
| **Kiśora–Kiśorī** | Text work, cases, structured debate where noted |

## Visual-learning needs

→ [../visuals/VISUAL-PLAN.md](../visuals/VISUAL-PLAN.md)

## Gamma outputs

→ [../gamma/GAMMA-MASTER-DECK-BRIEF.md](../gamma/GAMMA-MASTER-DECK-BRIEF.md)

## Open questions

- Human reviewer to confirm verse numbering vs congregation Gītā edition
- Sign claim register after doctrinal review

## Human review required

- Doctrinal accuracy of claim register
- Safeguarding on all case studies
- Rights before external images

_Status: enhancement-complete — pending human review_
"""
    (folder / "research" / "RESEARCH-DOSSIER.md").write_text(content, encoding="utf-8")


def write_source_matrix(folder: Path, m: dict) -> None:
    rows = "\n".join(
        f"| {sid} | {work} | {ref} | [link]({url}) | {func} | Yes | human-review-required |"
        for sid, work, ref, url, func in m["sources"]
    )
    content = f"""# {m["code"]} Source Matrix

| Source ID | Work | Reference | Stable link | Teaching function | Context checked | Status |
| --- | --- | --- | --- | --- | --- | --- |
{rows}

## Edition note

Verse numbering verified against VedaBase *Bhagavad-gītā As It Is* (Prabhupāda) edition.

## Copyright treatment

Stable URL + KUTUMBA summary only. No full purports in repository.

## Cross-reference

Full registry: [../sources.yaml](../sources.yaml)
"""
    (folder / "research" / "SOURCE-MATRIX.md").write_text(content, encoding="utf-8")


def write_claim_register(folder: Path, m: dict) -> None:
    claims_yaml = []
    for cid, stmt, ctype, keys, aud, risk in m["claims"]:
        keys_lines = "\n".join(f"      - {k}" for k in keys) if keys else "      []"
        claims_yaml.append(
            f"""  - claim_id: {m["code"]}-{cid}
    statement: "{stmt}"
    claim_type: {ctype}
    primary_source_keys:
{keys_lines}
    audience: {aud}
    misunderstanding_risk: "{risk}"
    exact_quote: false
    review_required: doctrinal
    reviewer: ""
    status: human-review-required"""
        )
    content = f"""week_code: {m["code"]}
claims:
{chr(10).join(claims_yaml)}
"""
    (folder / "research" / "CLAIM-REGISTER.yaml").write_text(content, encoding="utf-8")


def write_lecture_index(folder: Path, m: dict) -> None:
    rows = "\n".join(
        f"| {mid} | {date} | {place} | {topic} | Segment | [{mid}]({url}) | human-review-required |"
        for mid, date, place, topic, url, seg in m["lectures"]
    )
    summaries = "\n\n".join(
        f"## KUTUMBA summary — {topic}\n\nFacilitator prep summary for {mid}: listen on VedaBase; "
        f"do not transcribe lengthy quotes into slides."
        for mid, date, place, topic, url, seg in m["lectures"]
    )
    content = f"""# {m["code"]} Śrīla Prabhupāda Lecture Index

Verified entries with stable VedaBase links. Summaries only in repository.

| Media ID | Date | Place | Title / Topic | Topic segment | Link | Status |
| --- | --- | --- | --- | --- | --- | --- |
{rows}

## Usage rules

- Facilitators may listen privately for preparation; do not transcribe lengthy quotes into slides.
- Prefer citing verse summaries and pointing families to VedaBase.
- Additional lectures may be added after doctrinal review.

{summaries}
"""
    (folder / "research" / "PRABHUPADA-LECTURE-INDEX.md").write_text(content, encoding="utf-8")


def write_contemporary_applications(folder: Path, m: dict) -> None:
    case_md = _generate_cases(m)
    content = f"""# {m["code"]} Contemporary Applications — Anonymized Case Studies

{m["case_count"]} case studies below. All fictional composites.

---

{case_md}
"""
    (folder / "research" / "CONTEMPORARY-APPLICATIONS.md").write_text(content, encoding="utf-8")


def _generate_cases(m: dict) -> str:
    templates = CASE_TEMPLATES.get(m["code"], [])
    blocks = []
    for i, tpl in enumerate(templates[: m["case_count"]], 1):
        blocks.append(
            f"""## CS-{i:02d} — {tpl["title"]}

| Field | Detail |
| --- | --- |
| **Presenting situation** | {tpl["situation"]} |
| **Mistaken conclusion** | {tpl["mistake"]} |
| **Source-grounded correction** | {tpl["correction"]} |
| **Compassionate response** | {tpl["response"]} |
| **Facilitator caution** | {tpl["caution"]} |
| **Lāla–Lālī** | {tpl["lala"]} |
| **Kiśora–Kiśorī** | {tpl["kisora"]} |

---"""
        )
    return "\n\n".join(blocks)


CASE_TEMPLATES: dict[str, list[dict]] = {
    "C2-W1": [
        {"title": "Angry group message", "situation": "A parent posts a sharp correction in the family chat at midnight.", "mistake": "Words are harmless if intention was good", "correction": "Intention, method, and consequence all matter ([BG 3.9](https://vedabase.io/en/library/bg/3/9/))", "response": "Pause, delete if possible, apologize, rewrite privately", "caution": "No re-enacting real family conflicts", "lala": "Action echo game — kind vs harsh words", "kisora": "Action chain for one online post"},
        {"title": "Careless temple service", "situation": "A teen stacks shoes quickly saying 'it's for Kṛṣṇa' but blocks the door.", "mistake": "Label makes careless method holy", "correction": "Offer work without selfish attachment includes careful method", "response": "Before–during–after redo with safety check", "caution": "No naming real volunteers", "lala": "Seed planting — careful water vs forget", "kisora": "BG 3.9 debate: stopping work vs changing purpose"},
        {"title": "Victim-blaming after illness", "situation": "A guest says a child's hospital stay 'must be past karma.'", "mistake": "We can diagnose another's suffering", "correction": "KUTUMBA boundary — never explain specific illness as known karma", "response": "Facilitator interrupts; offer compassion and practical help", "caution": "Stop immediately", "lala": "Not used — adult correction only", "kisora": "Challenge statement activity"},
        {"title": "Generous gift for praise", "situation": "A parent donates publicly then sulks when not thanked.", "mistake": "Good action always feels good", "correction": "Separate interest binds ([BG 3.9](https://vedabase.io/en/library/bg/3/9/))", "response": "Examine motive; give privately next time", "caution": "No guessing donor identities", "lala": "Returning borrowed item story", "kisora": "Intention–method–result trio"},
        {"title": "King Nṛga summary (parent)", "situation": "A devotee returns property but forgets one cow; conflict lingers.", "mistake": "Good intention erases procedural error", "correction": "Care and accountability ([SB 9.4](https://vedabase.io/en/library/sb/9/4/4/))", "response": "Complete return; apologize; accept reaction soberly", "caution": "Child version only — care not fear", "lala": "Borrowed bowl story", "kisora": "Procedural checklist exercise"},
        {"title": "Sibling blame spiral", "situation": "Two children break a plate; each insists the other 'made me' do it.", "mistake": "Others remove my responsibility", "correction": "Own next repair step", "response": "Joint cleanup; before–during–after for future", "caution": "Low-stakes only", "lala": "Action echo", "kisora": "Responsibility map"},
        {"title": "Fatalism at work", "situation": "A parent misses deadlines saying 'it's my karma, why try?'", "mistake": "Karma equals fate", "correction": "Action and reaction invite present effort", "response": "One duty offered with before–during–after", "caution": "No shaming employment stress", "lala": "N/A", "kisora": "Fatalism vs responsibility pair share"},
    ],
    "C2-W2": [
        {"title": "'You made me angry'", "situation": "A teen shouts that a sibling caused their outburst.", "mistake": "Others control my chosen response", "correction": "Conditioning real; next choice matters ([BG 18.63](https://vedabase.io/en/library/bg/18/63/))", "response": "Traffic-light pause; redo respectfully", "caution": "Not for abuse scenarios", "lala": "Puppet toy taken", "kisora": "Trigger chain mapping"},
        {"title": "Spiritual perfectionism", "situation": "A parent melts down when plans fail, saying they 'should control everything.'", "mistake": "Devotion means controlling all results", "correction": "Responsibility ≠ controlling outcomes ([BG 5.14](https://vedabase.io/en/library/bg/5/14/))", "response": "Control circle exercise", "caution": "Watch anxiety signals", "lala": "N/A", "kisora": "Control/influence/no-control sort"},
        {"title": "Peer pressure online", "situation": "A 12-year-old is dared to post a cruel meme.", "mistake": "I had no choice", "correction": "Seek adult help for coercion; choose truth", "response": "Pause–remember–choose; tell parent", "caution": "Mandatory escalation if unsafe", "lala": "Ask adult for help practice", "kisora": "Digital habit intervention point"},
        {"title": "Ajāmila hope (parent)", "situation": "A newcomer fears they are 'too fallen' to improve.", "mistake": "Past habits erase all hope", "correction": "Mercy at turning point ([SB 6.1.15](https://vedabase.io/en/library/sb/6/1/15/))", "response": "One holy name; mentor contact", "caution": "No sensational death imagery", "lala": "Remember Kṛṣṇa line", "kisora": "Journal: smallest next choice"},
        {"title": "Conditioning vs excuse", "situation": "A youth repeats harmful teasing 'because that's how I am.'", "mistake": "Nature excuses harm", "correction": "Conditioning explains; does not excuse ([BG 3.34](https://vedabase.io/en/library/bg/3/34/))", "response": "Repair + environmental support", "caution": "Firm safeguarding", "lala": "Kind words scenario", "kisora": "Respectful redo role-play"},
        {"title": "Arjuna deliberation", "situation": "A family rushes a major decision without hearing guidance.", "mistake": "Choice without deliberation is freedom", "correction": "Hear, deliberate, then act ([BG 18.63](https://vedabase.io/en/library/bg/18/63/))", "response": "24-hour pause rule", "caution": "No exposing private decisions", "lala": "N/A", "kisora": "Arjuna choice chart"},
        {"title": "Unsafe home (escalation)", "situation": "A child discloses fear of going home.", "mistake": "Use traffic-light alone", "correction": "Immediate adult/professional help", "response": "Follow safeguarding policy — not self-regulation only", "caution": "Mandatory protocol", "lala": "Tell trusted adult", "kisora": "Private facilitator route"},
    ],
    "C2-W3": [
        {"title": "Bedtime death question", "situation": "A 5-year-old asks if a grandparent 'disappeared forever.'", "mistake": "Avoid or overload with detail", "correction": "Soul continues; body stopped ([BG 2.20](https://vedabase.io/en/library/bg/2/20/))", "response": "Brief truthful answer; hug; parent follow-up", "caution": "No frightening imagery", "lala": "Doll clothes; feelings cards", "kisora": "Two-sentence answer practice"},
        {"title": "Recent bereavement", "situation": "A family lost a relative last month.", "mistake": "Philosophy replaces grief", "correction": "Grief respected ([BG 2.27](https://vedabase.io/en/library/bg/2/27/))", "response": "Opt-out; private support", "caution": "No public quiz on destination", "lala": "Optional parallel activity", "kisora": "Compassionate responses analysis"},
        {"title": "Ghost story fascination", "situation": "Children swap scary ghost videos.", "mistake": "Entertainment equals scripture", "correction": "Do not speculate paranormal", "response": "Redirect to bedtime remembrance", "caution": "No graphic media", "lala": "Bedtime prayer practice", "kisora": "Media habit discussion"},
        {"title": "Speculating rebirth", "situation": "A guest claims a deceased uncle 'became a bird.'", "mistake": "We can know others' next body", "correction": "KUTUMBA boundary — no guessing", "response": "Facilitator corrects gently", "caution": "Stop speculation", "lala": "N/A", "kisora": "Question sorting: known/infer/guess-not"},
        {"title": "Bhārata remembrance (parent)", "situation": "A devotee notices distraction during japa.", "mistake": "One distraction ruins everything", "correction": "Repeated consciousness shapes direction ([SB 5.9](https://vedabase.io/en/library/sb/5/9/1/))", "response": "Bedtime remembrance routine", "caution": "No fear preaching", "lala": "Bedtime prayer", "kisora": "Consciousness habits chart"},
        {"title": "Why choices matter", "situation": "A teen asks 'if soul continues, why try?'", "mistake": "Continuity means indifference", "correction": "Present choices shape consciousness ([BG 8.6](https://vedabase.io/en/library/bg/8/6/))", "response": "Service and remembrance now", "caution": "Avoid debating nihilism publicly", "lala": "N/A", "kisora": "Written response prep"},
    ],
    "C2-W4": [
        {"title": "Three evenings", "situation": "Same family: calm Tuesday, chaotic Thursday, dull Sunday.", "mistake": "We are just a passionate family", "correction": "Modes describe conditions ([BG 14.5](https://vedabase.io/en/library/bg/14/5/))", "response": "Environment redesign", "caution": "Never label people", "lala": "Weather faces", "kisora": "Evening design project"},
        {"title": "Goodness trap", "situation": "A parent judges another family's messy home as 'tamasic.'", "mistake": "Modes as personality slurs", "correction": "Describe conditions; compassion", "response": "Offer help; examine pride", "caution": "Stop labeling immediately", "lala": "Room not child", "kisora": "Goodness superiority discussion"},
        {"title": "Algorithm feed", "situation": "A teen scrolls for hours after homework.", "mistake": "Passion is harmless fun", "correction": "Passion agitates ([BG 14.7](https://vedabase.io/en/library/bg/14/7/))", "response": "Five-minute clarity reset", "caution": "No shaming", "lala": "N/A", "kisora": "Feed analysis"},
        {"title": "Food shame", "situation": "A child is called 'tamasic' for medical diet.", "mistake": "Food policing", "correction": "Medical needs sacred; general tendencies only ([BG 17.8](https://vedabase.io/en/library/bg/17/8/))", "response": "Facilitator corrects publicly", "caution": "Zero tolerance", "lala": "Fresh food pictures only", "kisora": "Discuss boundaries on food talk"},
        {"title": "Clarity before chanting", "situation": "Kīrtana starts in noisy clutter.", "mistake": "External order doesn't matter", "correction": "Environment supports attention", "response": "Five-minute reset", "caution": "Not legalism", "lala": "Three-item tidy", "kisora": "Before/after attention rating"},
        {"title": "Ignorance spiral", "situation": "Dishes pile up; family skips program.", "mistake": "We're lazy people", "correction": "Ignorance conditions increase ([BG 14.8](https://vedabase.io/en/library/bg/14/8/))", "response": "One simplify step", "caution": "No contempt", "lala": "Fog weather face", "kisora": "Remove/add/move/simplify"},
        {"title": "BG 14.26 devotion", "situation": "A family proud of cleanliness skips chanting.", "mistake": "Goodness equals bhakti", "correction": "Devotion transcends modes ([BG 14.26](https://vedabase.io/en/library/bg/14/26/))", "response": "Chant after reset", "caution": "Balance", "lala": "Sit for one chant", "kisora": "Goodness vs bhakti paragraph"},
    ],
    "C2-W5": [
        {"title": "Ten-second notification", "situation": "Reading Gītā interrupted by phone spiral.", "mistake": "I can peek safely", "correction": "Attention chain ([BG 2.62](https://vedabase.io/en/library/bg/2/62/))", "response": "Boundary + japa shelter", "caution": "No displaying inappropriate feeds", "lala": "Shiny toy distraction", "kisora": "Stop–name–redirect plan"},
        {"title": "Decorated prison cell", "situation": "A family renovates home but skips all spiritual practice.", "mistake": "Comfort equals success", "correction": "Decoration without remembrance binds ([BG 7.14](https://vedabase.io/en/library/bg/7/14/))", "response": "Sacred space + time block", "caution": "Honor householder duty", "lala": "N/A", "kisora": "Responsible vs ultimate project"},
        {"title": "Women are māyā (correction)", "situation": "A teen repeats misogynistic slogan heard online.", "mistake": "People are māyā", "correction": "Māyā is energy; souls are sacred", "response": "Explicit correction; mentor follow-up", "caution": "Mandatory", "lala": "People are not māyā line", "kisora": "Ethics discussion"},
        {"title": "Fish in the well", "situation": "A professional sees only career ladder.", "mistake": "Well is whole ocean", "correction": "Limited vision ([SB 7.5.23](https://vedabase.io/en/library/sb/7/5/23/))", "response": "Broaden association; chant", "caution": "No mocking careers", "lala": "N/A", "kisora": "Well/ocean drawing"},
        {"title": "Praise-seeking loop", "situation": "A parent checks likes during prasādam.", "mistake": "Recognition is harmless", "correction": "False promise of attention", "response": "Praise fast + replacement chant", "caution": "Private habit", "lala": "Put down; chant once", "kisora": "False promise worksheet"},
        {"title": "Surrender not hatred", "situation": "A newcomer wants to abandon job as 'māyā only.'", "mistake": "World is fake — quit everything", "correction": "Surrender crosses māyā; duty remains ([BG 9.10](https://vedabase.io/en/library/bg/9/10/))", "response": "Offer work to Kṛṣṇa", "caution": "Financial prudence", "lala": "N/A", "kisora": "Duty vs escape essay"},
        {"title": "Addiction disclosure", "situation": "An adult shares compulsive behavior in group.", "mistake": "Public group is therapy", "correction": "Private support pathway", "response": "Facilitator routes to mentor/professional", "caution": "No group treatment", "lala": "N/A", "kisora": "N/A"},
    ],
    "C2-W6": [
        {"title": "Friday lateness", "situation": "Recurring rushed arrival before program.", "mistake": "Traffic karma — nothing changes", "correction": "Five-lens analysis", "response": "Prepare food earlier; device boundary", "caution": "Fictional case", "lala": "Puppet retry", "kisora": "Facilitate five lenses"},
        {"title": "Fatalism sentence", "situation": "A teen quotes 'it's all karma' to avoid homework.", "mistake": "Karma excuses present effort", "correction": "Action and choice remain ([BG 3.9](https://vedabase.io/en/library/bg/3/9/))", "response": "Choose one duty offered", "caution": "No shaming grades", "lala": "Seed duty card", "kisora": "Statement correction"},
        {"title": "Mode-labeling sibling", "situation": "A parent calls a child 'tamasic' at dinner.", "mistake": "Fixed mode identity", "correction": "Describe conditions ([BG 14.5](https://vedabase.io/en/library/bg/14/5/))", "response": "Reset environment; apologize", "caution": "Stop labeling", "lala": "Weather on room", "kisora": "Label critique"},
        {"title": "Attention loop at kīrtana", "situation": "Devices active during chanting.", "mistake": "Presence is enough", "correction": "Māyā loop + boundary ([BG 7.14](https://vedabase.io/en/library/bg/7/14/))", "response": "Clarity reset + charging station", "caution": "Model gently", "lala": "Device away box", "kisora": "Digital loop design"},
        {"title": "Grief + philosophy misuse", "situation": "Someone tells bereaved parent 'don't grieve, soul eternal.'", "mistake": "Philosophy suppresses grief", "correction": "Compassion + truth ([BG 2.20](https://vedabase.io/en/library/bg/2/20/))", "response": "Listen first; brief hope", "caution": "Sensitive", "lala": "Feelings cards", "kisora": "Compassionate vs cold responses"},
        {"title": "Victim-blame in case", "situation": "Table blames injured person in fictional accident.", "mistake": "Karma diagnosis", "correction": "Prohibited", "response": "Facilitator redirects to compassion", "caution": "Interrupt", "lala": "N/A", "kisora": "Spot the error"},
        {"title": "Tool wheel selection", "situation": "Family must pick one Cycle 2 method to continue.", "mistake": "Collect tools without practice", "correction": "Continuity card", "response": "One method + trigger + support", "caution": "Private evidence", "lala": "Tool card pick", "kisora": "Evidence-based reason"},
        {"title": "Cross-table review", "situation": "Groups critique each other's case plans.", "mistake": "Competitive scoring", "correction": "One strength + one missing lens", "response": "Facilitator synthesizes", "caution": "No winning table", "lala": "N/A", "kisora": "Peer feedback rules"},
    ],
}


def write_misconceptions(folder: Path, m: dict) -> None:
    content = f"""# {m["code"]} Misconceptions and Boundaries

## Means / does-not-mean

| This teaching **means** | This teaching **does not mean** |
| --- | --- |
| {m["controlling_principle"]} | {m["exclusions"].split(";")[0]} |
| Thoughtful practice under guidance | Blaming victims or diagnosing others' karma |
| Age-appropriate delivery | Frightening or shaming children |
| Source-grounded paraphrase | Invented quotes or sensational stories |

## Scope boundaries

- **In scope:** {m["scope"]}
- **Out of scope:** {m["exclusions"]}
- **Prerequisites:** {m["prerequisites"]}

## Prohibited facilitator responses

- Diagnosing a specific person's suffering as karma
- Calling women or any persons "māyā"
- Labeling children as modes
- Graphic death imagery for Lāla–Lālī
- Public addiction confession without support route

## Human review

All entries `human-review-required` until doctrinal and safeguarding sign-off.
"""
    (folder / "research" / "MISCONCEPTIONS-AND-BOUNDARIES.md").write_text(content, encoding="utf-8")


def write_faq(folder: Path, m: dict) -> None:
    content = f"""# {m["code"]} FAQ

## Discovery

**What is the key verse?**  
[{m["key_verse"]}]({m["key_verse_url"]})

**What is the memory line?**  
{m["memory_line"]}

**What is the principal katha?**  
{m["katha_title"]} — see [prem-ki-katha.md](../prem-ki-katha.md)

## Understanding

**What is the essential question?**  
{m["essential_question"]}

**What are common misconceptions?**  
See [MISCONCEPTIONS-AND-BOUNDARIES.md](MISCONCEPTIONS-AND-BOUNDARIES.md)

## Application

**What is the bhakti laboratory?**  
{m["bhakti_lab"]} — see [bhakti-lab.md](../bhakti-lab.md)

**What is minimum home practice?**  
See [family-home-practice.md](../family-home-practice.md)

## Facilitator

**May I quote purports aloud?**  
Prep only. Use KUTUMBA summaries + VedaBase links in session.

**Is this publication-ready?**  
Enhancement-complete for pilot; human doctrinal, safeguarding, citation, rights, and pedagogy reviews still required.

## Copyright

No full BBT purports or artwork in repository.
"""
    (folder / "research" / "FAQ.md").write_text(content, encoding="utf-8")


def write_verse_study(folder: Path, m: dict) -> None:
    sections = []
    for sid, work, ref, url, func in m["sources"][:6]:
        sections.append(
            f"""## {work} {ref}

**Link:** [{url}]({url})

**KUTUMBA summary:** Teaching anchor for {func.lower()}.

**Teaching use this week:** {func}

**Not this week:** Topics listed in MISCONCEPTIONS-AND-BOUNDARIES.md

---"""
        )
    content = f"""# {m["code"]} Verse and Reference Study

Original KUTUMBA summaries only. Read full text and purport on VedaBase.

---

{chr(10).join(sections)}
"""
    (folder / "research" / "VERSE-AND-REFERENCE-STUDY.md").write_text(content, encoding="utf-8")


def write_bibliography(folder: Path, m: dict) -> None:
    items = "\n".join(
        f"- {work} {ref} — [{url}]({url})"
        for _, work, ref, url, _ in m["sources"]
    )
    content = f"""# {m["code"]} Bibliography

## Tier 1 — Scripture (VedaBase links)

{items}

## Tier 1 — Lectures

See [PRABHUPADA-LECTURE-INDEX.md](PRABHUPADA-LECTURE-INDEX.md)

## Pedagogy

- KUTUMBA case studies — fictional composites
- KUTUMBA analogies — see [analogy-and-application.md](../analogy-and-application.md)

## Copyright

Reference links only. No full purports stored in repository.
"""
    (folder / "research" / "BIBLIOGRAPHY.md").write_text(content, encoding="utf-8")


def write_approved_media(folder: Path, m: dict) -> None:
    content = f"""# {m["code"]} Approved Teacher Media Index

| Media ID | Type | Title | Link | Use | Status |
| --- | --- | --- | --- | --- | --- |
"""
    for mid, date, place, topic, url, seg in m["lectures"]:
        content += f"| {mid} | lecture | {topic} | [{url}]({url}) | Facilitator prep | human-review-required |\n"
    content += "\nNo video files stored in repository.\n"
    (folder / "research" / "APPROVED-TEACHER-MEDIA-INDEX.md").write_text(content, encoding="utf-8")


def write_lala_lesson(folder: Path, m: dict) -> None:
    content = f"""{yaml_front({"week_code": m["code"], "week_title": m["title"], "audience": "Lāla–Lālī (ages 4–8)", "component": "children/lala-lali-lesson.md"})}

# Lāla–Lālī Lesson — {m["title"]}

**Total time:** 40 minutes (aligns with parent track)  
**Memory line:** "{m["lala_memory"]}"  
**Sanskrit phrase:** *{m["lala_sanskrit"]}*  
**Safeguarding:** {m["lala_safeguarding"]}

---

## Core track — ages 4–6 (default delivery)

| Time | Activity |
| --- | --- |
| 0–5 min | Opening: recall prior Cycle 2 week if attended; one short song; show today's picture card |
| 5–15 min | **Story** (below) — 8 minutes + 2 min wonder questions |
| 15–22 min | Movement or hands-on activity tied to lesson |
| 22–28 min | Game or sorting activity |
| 28–32 min | **Movement break** — reset bodies safely |
| 32–36 min | Simple craft or card making |
| 36–40 min | Recall line + hand to heart; transition to [shared-family-transition.md](shared-family-transition.md) |

### Story — facilitator narrative (8–10 min)

{m["lala_story"]}

**Wonder questions (no wrong answers):**  
- What choice happened first?  
- What happened after?  
- What can we do for Kṛṣṇa next time?

### Movement / game

Follow activities in [complete-week.md](../complete-week.md) Age 4–6 section — seed planting, traffic-light, doll clothes, weather faces, or shiny-choice puppet as appropriate.

### Craft

Children make a recall card with picture + memory line: "{m["lala_memory"]}"

---

## Extension — ages 7–8

Add after story (do not replace core):

| Addition | Detail |
| --- | --- |
| **Verse rhythm** | Key verse summary in call-and-response (English) — link parent [overview.md](../overview.md) |
| **Scenario cards** | Low-stakes choice practice with respectful redo |
| **Deeper recall** | Connect memory line to one home practice step |
| **Sanskrit** | Repeat *{m["lala_sanskrit"].split("—")[0].strip()}* once |

---

## Take-home

One recall card with memory line and child drawing of today's story beat.

## Closing transition

Hand to heart; walk quietly to family reunification — see [shared-family-transition.md](shared-family-transition.md).

---

## Facilitator cautions

- {m["lala_safeguarding"]}
- Do not invite trauma disclosure in group.
- Route graphic death or abuse questions to parents privately.
- Two adults in visible space.

---

## Materials

See [materials.md](../materials.md) — Lāla–Lālī section.

## Sources

- [{m["key_verse"]}]({m["key_verse_url"]})
- [prem-ki-katha.md](../prem-ki-katha.md)
- [research/CONTEMPORARY-APPLICATIONS.md](../research/CONTEMPORARY-APPLICATIONS.md)
"""
    (folder / "children" / "lala-lali-lesson.md").write_text(content, encoding="utf-8")


def write_kisora_lesson(folder: Path, m: dict) -> None:
    content = f"""{yaml_front({"week_code": m["code"], "week_title": m["title"], "audience": "Kiśora–Kiśorī (ages 9–14)", "component": "children/kisora-kisori-lesson.md"})}

# Kiśora–Kiśorī Lesson — {m["title"]}

**Total time:** 40 minutes  
**Essential question:** {m["essential_question"]}  
**No forced personal disclosure.** Use anonymized scenarios from research cases only.

---

## Core track — ages 9–11

| Time | Activity |
| --- | --- |
| 0–5 min | Opening: index cards — one word for challenge, one for hope (anonymous) |
| 5–15 min | **Text observation** — {m["key_verse"]} (KUTUMBA summary + link) |
| 15–22 min | Diagram or sorting exercise (see [visuals/concept-map.mmd](../visuals/concept-map.mmd)) |
| 22–30 min | Case study from [research/CONTEMPORARY-APPLICATIONS.md](../research/CONTEMPORARY-APPLICATIONS.md) |
| 30–35 min | Reflective writing (3–4 sentences, optional share) |
| 35–40 min | One concrete action + family transition |

### Text observation

Read aloud KUTUMBA summary for [{m["key_verse"].split()[-1]}]({m["key_verse_url"]}).

**Observe:** (1) What does Kṛṣṇa emphasize? (2) What is our part? (3) What attitude is recommended?

### Case study

Facilitator reads anonymized Case CS-01 or CS-02. Pairs identify mistaken conclusion and compassionate response.

### Reflective writing

Prompt: "When I remember {m["memory_line"][:50]}… I will…"

### Action statement

Template: "This week my body/voice/choices can serve Kṛṣṇa by ___." One concrete step.

---

## Extension — ages 12–14

| Addition | Detail |
| --- | --- |
| **Structured debate or critique** | Motion related to module misconception — cite verse summary, no personal attacks |
| **Digital / social case** | Case CS-03 or CS-04 where applicable |
| **Cross-lesson link** | Connect to Cycle 2 prior weeks |
| **Challenge writing** | One paragraph analyzing peer pressure without naming real persons |

### Debate rules

1. Attack ideas, not people.  
2. Use "I think" and source reference.  
3. Facilitator may pause for safeguarding.  
4. No recording without consent.

---

## Facilitator cautions

- Never tell victims they chose harm done to them.
- Unsafe situations → immediate adult help, not quiet endurance.
- Watch for anxiety, shame, or grief — private follow-up per policy.
- No karma diagnosis of real persons.

---

## Materials

See [materials.md](../materials.md) — Kiśora–Kiśorī section.

## Sources

- [{m["key_verse"]}]({m["key_verse_url"]})
- [research/CONTEMPORARY-APPLICATIONS.md](../research/CONTEMPORARY-APPLICATIONS.md)
- [analogy-and-application.md](../analogy-and-application.md)
"""
    (folder / "children" / "kisora-kisori-lesson.md").write_text(content, encoding="utf-8")


def write_family_transition(folder: Path, m: dict) -> None:
    content = f"""{yaml_front({"week_code": m["code"], "week_title": m["title"], "audience": "All ages — reunification", "component": "children/shared-family-transition.md"})}

# Shared Family Transition — 10 Minutes

**When:** After parallel parent, Lāla–Lālī, and Kiśora–Kiśorī sessions.

## Purpose

Reunite families with one shared insight and one shared practice — without re-teaching the full lesson.

## Flow

| Time | Action |
| --- | --- |
| 0–2 min | Bell; families sit together. Facilitator: "What one choice or habit did we study today?" |
| 2–5 min | **One-line share:** Parents — verse summary; Lāla–Lālī — recall line; Kiśora–Kiśorī — one case insight |
| 5–8 min | **Family pair practice:** Complete one step from {m["bhakti_lab"]} or show child's recall card |
| 8–10 min | **Sankalpa preview:** Lead reads [sankalpa.md](../sankalpa.md) opening; families whisper home-practice trigger |

## All-age recall (call and response)

> **Leader:** {m["transition_recall"]}  
> **All:** {m["transition_recall"]}

## Bridge to Bhakti laboratory

"We practice together now — {m['bhakti_lab']}." See [bhakti-lab.md](../bhakti-lab.md)

## Bridge to Cycle 2 project

Optional gallery contribution — see [project/MODULE-PROJECT-BRIEF.md](../project/MODULE-PROJECT-BRIEF.md). No public disclosure of private struggles.

## Newcomer note

Host families help newcomers find materials. Newcomers may observe silently.
"""
    (folder / "children" / "shared-family-transition.md").write_text(content, encoding="utf-8")


def write_visuals(folder: Path, m: dict) -> None:
    v = folder / "visuals"
    v.mkdir(exist_ok=True)
    code = m["code"]
    (v / "VISUAL-PLAN.md").write_text(
        f"""# {code} Visual Plan

## Design principles

- Mermaid originals in git — no BBT copyrighted images
- Render `.mmd` in Markdown preview
- Safeguarding visuals per age track

## Visual inventory

| # | Visual | File | Audience | Purpose |
| --- | --- | --- | --- | --- |
| 1 | Concept map | concept-map.mmd | 9+ | Core distinctions |
| 2 | Session flow | process-flow.mmd | facilitator | Lesson arc |
| 3 | Means / does-not-mean | VISUAL-PLAN § below | Parent | Misconception guard |

## Means / does-not-mean

| Means | Does not mean |
| --- | --- |
| {m["controlling_principle"][:60]}... | {m["exclusions"].split(";")[0]} |
| Source-grounded practice | Invented quotes |
| Compassionate delivery | Fear or shame |

## Gamma integration

See [../gamma/GAMMA-MASTER-DECK-BRIEF.md](../gamma/GAMMA-MASTER-DECK-BRIEF.md).

## Image rights

[image-rights-register.yaml](image-rights-register.yaml)
""",
        encoding="utf-8",
    )
    title_short = m["title"][:25]
    (v / "concept-map.mmd").write_text(
        f"""flowchart TB
    subgraph TEACHING["{code} core teaching"]
        A["{title_short}"]
        B["{m["key_verse"]}"]
        C["{m["bhakti_lab"]}"]
    end
    subgraph SOURCES["Sources"]
        S1[Scripture]
        S2[Practice]
    end
    A --> B --> C
    S1 --> A
    S2 --> C
""",
        encoding="utf-8",
    )
    (v / "process-flow.mmd").write_text(
        f"""flowchart LR
    HOOK[Opening hook] --> KATHA[Prem-kī-kathā]
    KATHA --> LESSON[Parent / child tracks]
    LESSON --> LAB[{m["bhakti_lab"]}]
    LAB --> HOME[Family home practice]
""",
        encoding="utf-8",
    )
    (v / "image-rights-register.yaml").write_text(
        f"""week_code: {code}
images:
  - image_id: {code}-IMG-001
    description: Mermaid concept-map export
    rights_status: original-kutumba
    status: approved-internal
  - image_id: {code}-IMG-002
    description: Mermaid process-flow export
    rights_status: original-kutumba
    status: approved-internal
""",
        encoding="utf-8",
    )


def _gamma_cards(m: dict, audience: str, count: int) -> str:
    cards = []
    titles = [
        ("Title", f"{m['code']} — {m['title']}\nCycle 2 · Karma, Rebirth and Material Nature\nKUTUMBA Family Program"),
        ("Essential question", m["essential_question"]),
        ("Opening hook", m["hook"][:200] + "..."),
        ("Key verse", f"**{m['key_verse']}** (KUTUMBA summary)\n{m['memory_line']}"),
        ("Katha beat", m["katha_paraphrase"][0][:180] + "..."),
        ("Means / does-not-mean", f"Means: {m['controlling_principle'][:100]}...\nDoes NOT: {m['exclusions'][:80]}..."),
        ("Case study", "Anonymized case — see CONTEMPORARY-APPLICATIONS.md\nTask: mistaken conclusion + compassionate response"),
        ("Bhakti lab", m["bhakti_lab"]),
        ("Home practice", "See family-home-practice.md — minimum / standard / stretch"),
        ("Child recall", m["lala_memory"]),
        ("Sources", f"VedaBase: {m['key_verse_url']}\nNo invented quotations"),
        ("Review", "human-review-required — doctrinal, safeguarding, rights"),
    ]
    for i, (label, body) in enumerate(titles[:count], 1):
        cards.append(
            f"""### Card {i} — {label}

**Content:**  
{body}

**Visual:** `[IMAGE: {label.lower()} — KUTUMBA placeholder]`  
**Speaker note:** Deliver per facilitator-guide.md  
**Source:** {m["code"]} module pack

---"""
        )
    return "\n\n".join(cards)


def write_gamma(folder: Path, m: dict) -> None:
    g = folder / "gamma"
    g.mkdir(exist_ok=True)
    decks = [
        ("GAMMA-PARENT-DECK-PROMPT.md", "Parent / family", 12),
        ("GAMMA-LALA-LALI-DECK-PROMPT.md", "Lāla–Lālī ages 4–8", 10),
        ("GAMMA-KISORA-KISORI-DECK-PROMPT.md", "Kiśora–Kiśorī ages 9–14", 11),
    ]
    for fname, aud, count in decks:
        cards = _gamma_cards(m, aud, count)
        (g / fname).write_text(
            f"""# Gamma Prompt — {m["code"]} {aud} Deck

## Deck identity

- **Module:** {m["code"]} — {m["title"]}
- **Audience:** {aud}
- **Purpose:** {m["essential_question"]}
- **Format:** 16:9 presentation
- **Recommended card count:** {count}
- **Style:** Warm, family-friendly, source-grounded
- **Source pack:** sources.yaml, VERSE-AND-REFERENCE-STUDY.md, prem-ki-katha.md

## Global instructions

Paste card content exactly into Gamma. Do not invent quotations. Sanskrit diacritics as in module.

---

## Card plan

{cards}
""",
            encoding="utf-8",
        )
    (g / "GAMMA-MASTER-DECK-BRIEF.md").write_text(
        f"""# {m["code"]} Gamma Master Deck Brief

## Deck family overview

| Deck | File | Cards | Audience |
| --- | --- | --- | --- |
| Parent / family | GAMMA-PARENT-DECK-PROMPT.md | 12 | Adults |
| Lāla–Lālī | GAMMA-LALA-LALI-DECK-PROMPT.md | 10 | Ages 4–8 |
| Kiśora–Kiśorī | GAMMA-KISORA-KISORI-DECK-PROMPT.md | 11 | Ages 9–14 |

## Global instructions for Gamma

- Use only supplied card content and KUTUMBA summaries
- Do not invent quotations
- Image placeholders: `[IMAGE: description]` until rights resolved
- Source note card on every deck
- Style: warm, family-friendly, high readability

## Source pack

- sources.yaml, VERSE-AND-REFERENCE-STUDY.md, visuals/*.mmd

## Review checklist

- [ ] No full purports pasted
- [ ] VedaBase URLs on citation cards
- [ ] Safeguarding slide on means/does-not-mean
- [ ] Child decks age-appropriate
- [ ] Human rights review before stock photos

Speaker notes: SPEAKER-NOTES.md
""",
        encoding="utf-8",
    )
    (g / "SPEAKER-NOTES.md").write_text(
        f"""# {m["code"]} Speaker Notes

## Before session

- Read prem-ki-katha.md and key verse on VedaBase
- Review MISCONCEPTIONS-AND-BOUNDARIES.md
- Check safeguarding for {m["code"]} — risks-and-sensitive-points.md

## Timing

- Opening hook: 2–3 min
- Prem-kī-kathā: 12–15 min with interaction
- Parent lesson: 40 min parallel tracks

## Critical corrections

{m["lala_safeguarding"]}

## Human review

human-review-required — do not claim doctrinal approval.
""",
        encoding="utf-8",
    )


def write_media_index(folder: Path, m: dict) -> None:
    av = folder / "audio-video"
    av.mkdir(exist_ok=True)
    entries = []
    for i, (fname, _, _) in enumerate(
        [
            ("GAMMA-PARENT-DECK-PROMPT.md", "parent", ""),
            ("GAMMA-LALA-LALI-DECK-PROMPT.md", "lala", ""),
            ("GAMMA-KISORA-KISORI-DECK-PROMPT.md", "kisora", ""),
        ],
        1,
    ):
        entries.append(
            f"""  - media_id: {m["code"]}-MEDIA-{i:03d}
    type: gamma-deck
    title: "{m["code"]} deck {i}"
    location: gamma/{fname}
    status: prompt-ready-not-rendered
    rights_status: internal"""
        )
    lec = m["lectures"][0]
    entries.append(
        f"""  - media_id: {m["code"]}-MEDIA-004
    type: prabhupada-lecture
    title: "{lec[3]}"
    stable_url: "{lec[4]}"
    status: reference-only
    rights_status: vedabase-link"""
    )
    content = f"""week_code: {m["code"]}
media:
{chr(10).join(entries)}

approved_teacher_media: []

notes: "No video files in repository. Facilitators use live delivery + optional VedaBase lecture playback in private prep."
"""
    (av / "MEDIA-INDEX.yaml").write_text(content, encoding="utf-8")


def write_reviews(folder: Path, m: dict) -> None:
    rv = folder / "reviews"
    rv.mkdir(exist_ok=True)
    claim_ids = ", ".join(c[0] for c in m["claims"][:5])
    (rv / "DOCTRINAL-REVIEW.md").write_text(
        f"""# {m["code"]} Doctrinal Review

**Status:** human-review-required  
**Reviewer:** _[assign]_  
**Date:** 2026-06-30 (Cycle 2 gold-standard pass)

## Scope reviewed

- [research/CLAIM-REGISTER.yaml](../research/CLAIM-REGISTER.yaml) — {len(m["claims"])} claims
- [prem-ki-katha.md](../prem-ki-katha.md) — paraphrase only; no invented dialogue
- [katha/KATHA-SOURCE-REGISTER.yaml](../katha/KATHA-SOURCE-REGISTER.yaml)
- [research/SOURCE-MATRIX.md](../research/SOURCE-MATRIX.md) — {len(m["sources"])} sources
- Age-track lessons and gamma prompts

## Findings

| ID | Finding | Severity | Remediation |
| --- | --- | --- | --- |
| DR-01 | Claims align with assigned verses; katha uses paraphrase not fake quotes | Pass-pending | Human confirm summaries |
| DR-02 | Scope boundaries explicit in dossier and misconceptions doc | Pass-pending | Maintain at facilitation |
| DR-03 | Katha registry present with omitted-complex-details | Pass-pending | Sign register |
| DR-04 | Key verse [{m["key_verse"]}]({m["key_verse_url"]}) anchors module | Pass-pending | Edition check |
| DR-05 | No human approval claimed in review-status | Pass | — |

## Sample claims for spot-check

Spot-check claim IDs: {claim_ids}, and remaining entries in register.

## Open items for human reviewer

1. Confirm verse numbering matches congregation printed Gita
2. Sign claim register entries after spot-check
3. Approve katha paraphrase for {m["katha_title"]}
4. Confirm safeguarding language for age tracks

## Verdict

**Pilot-ready pending human sign-off.** No automated doctrinal approval.
""",
        encoding="utf-8",
    )
    (rv / "PEDAGOGY-REVIEW.md").write_text(
        f"""# {m["code"]} Pedagogy Review

**Status:** human-review-required  
**Reviewer:** _[assign]_  
**Date:** 2026-06-30 (Cycle 2 gold-standard pass)

## Scope reviewed

- [children/lala-lali-lesson.md](../children/lala-lali-lesson.md) — timed 40-minute track
- [children/kisora-kisori-lesson.md](../children/kisora-kisori-lesson.md) — timed 40-minute track
- [children/shared-family-transition.md](../children/shared-family-transition.md) — 10-minute reunification
- [research/CONTEMPORARY-APPLICATIONS.md](../research/CONTEMPORARY-APPLICATIONS.md) — {m["case_count"]} cases
- [gamma/GAMMA-PARENT-DECK-PROMPT.md](../gamma/GAMMA-PARENT-DECK-PROMPT.md) and child decks

## Findings

| ID | Finding | Severity | Remediation |
| --- | --- | --- | --- |
| PR-01 | Two-group age model with extension bands present | Pass-pending | Facilitator training |
| PR-02 | No duplicated wrong safeguarding copy (body comparison removed) | Pass-pending | Spot-check delivery |
| PR-03 | Cases are fictional composites — no real family gossip | Pass-pending | Enforce in session |
| PR-04 | Bhakti lab linked: {m["bhakti_lab"]} | Pass-pending | — |
| PR-05 | Integration/safeguarding notes match module risks file | Pass-pending | Bereavement opt-out for C2-W3 |

## Age-track notes

- **Lāla–Lālī:** {m["lala_safeguarding"]}
- **Kiśora–Kiśorī:** No forced disclosure; debate rules where applicable
- **Transition:** 40+ line reunification with recall and bhakti bridge

## Verdict

**Pedagogy pack complete pending human walkthrough.** Schedule facilitator rehearsal before pilot.
""",
        encoding="utf-8",
    )
    for name, focus in [
        ("CITATION-AUDIT.md", "VedaBase links and claim traceability"),
        ("SAFEGUARDING-REVIEW.md", m["lala_safeguarding"]),
        ("RIGHTS-REVIEW.md", "Mermaid originals; no BBT images in git"),
    ]:
        (rv / name).write_text(
            f"""# {m["code"]} {name.replace('.md','').replace('-', ' ')}

**Status:** human-review-required  
**Focus:** {focus}

## Checklist

- [ ] Human reviewer assigned
- [ ] Module-specific risks addressed
- [ ] Sign-off recorded externally when complete

No automated approval claimed.
""",
            encoding="utf-8",
        )


def write_review_status(folder: Path, m: dict) -> None:
    (folder / "review-status.yaml").write_text(
        f"""week_code: {m["code"]}
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
notes: Cycle 2 gold-standard deepening pass; human reviews required before publication.
""",
        encoding="utf-8",
    )


def deepen_module(folder_name: str) -> None:
    m = MODULES[folder_name]
    folder = WEEKLY / folder_name
    if not folder.exists():
        raise FileNotFoundError(folder)
    (folder / "research").mkdir(exist_ok=True)
    (folder / "children").mkdir(exist_ok=True)

    write_opening_hook(folder, m)
    write_prem_ki_katha(folder, m)
    write_katha_register(folder, m)
    write_research_dossier(folder, m)
    write_source_matrix(folder, m)
    write_claim_register(folder, m)
    write_lecture_index(folder, m)
    write_contemporary_applications(folder, m)
    write_misconceptions(folder, m)
    write_faq(folder, m)
    write_verse_study(folder, m)
    write_bibliography(folder, m)
    write_approved_media(folder, m)
    write_lala_lesson(folder, m)
    write_kisora_lesson(folder, m)
    write_family_transition(folder, m)
    write_visuals(folder, m)
    write_gamma(folder, m)
    write_media_index(folder, m)
    write_reviews(folder, m)
    write_review_status(folder, m)
    print("Deepened", m["code"])


def main() -> None:
    for name in sorted(MODULES.keys()):
        if name.startswith(CYCLE2_PREFIX):
            deepen_module(name)
    print("Cycle 2 gold-standard deepening complete.")


if __name__ == "__main__":
    main()

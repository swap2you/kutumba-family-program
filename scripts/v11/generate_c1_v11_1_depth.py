#!/usr/bin/env python3
"""V11.1 Cycle 1 content-depth correction — executable teacher-ready artifacts."""
from __future__ import annotations

from pathlib import Path

from docx import Document
from docx.shared import Pt

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
LAUNCH = REPO / "launch"

WEEKS = {
    "C1-W1": {
        "slug": "c1-w1-what-is-kutumba-and-why-are-we-here",
        "title": "What Is KUTUMBA, and Why Are We Here?",
        "primary": ("SB 1.2.18", "https://vedabase.io/en/library/sb/1/2/18/", "Regular Bhāgavata hearing and service cleanse the heart and steady devotion."),
        "supports": [
            ("SB 1.2.17", "https://vedabase.io/en/library/sb/1/2/17/", "The Lord in the heart cleanses desire from the faithful hearer."),
            ("SB 1.2.19", "https://vedabase.io/en/library/sb/1/2/19/", "Passion and ignorance recede as goodness increases."),
            ("SB 1.1.4", "https://vedabase.io/en/library/sb/1/1/4/", "Sages assemble and inquire about duty."),
        ],
        "memory": "Regular hearing and service to Śrīmad-Bhāgavatam steadies our family's devotion.",
        "question": "Why are we committing as a family?",
        "conclusion": "Protected weekly hearing plus home practice creates a path for family growth.",
        "misconception": "Coming to the session without home practice is enough.",
    },
    "C1-W2": {
        "slug": "c1-w2-i-am-not-this-body",
        "title": "I Am Not This Body",
        "primary": ("BG 2.13", "https://vedabase.io/en/library/bg/2/13/", "The embodied self passes through childhood, youth, and old age; the self continues."),
        "supports": [
            ("BG 2.22", "https://vedabase.io/en/library/bg/2/22/", "As one puts on new garments, the soul accepts new bodies — analogy with limits."),
            ("BG 2.20", "https://vedabase.io/en/library/bg/2/20/", "Supporting: soul is not slain when body is slain (full ontology reserved for W3)."),
        ],
        "memory": "My body changes; I continue as the conscious self.",
        "question": "How should knowing I am not only this body change how we speak about bodies?",
        "conclusion": "Body changes; conscious self continues — care for the body without mistaking it for the self.",
        "misconception": "Psychology or photos prove the soul.",
    },
    "C1-W3": {
        "slug": "c1-w3-the-nature-of-the-soul",
        "title": "The Nature of the Soul",
        "primary": ("BG 2.20", "https://vedabase.io/en/library/bg/2/20/", "The soul is never born and never dies; eternal and unchanging."),
        "supports": [
            ("BG 15.7", "https://vedabase.io/en/library/bg/15/7/", "Living entities are eternal fragmental parts of Kṛṣṇa."),
            ("BG 2.17", "https://vedabase.io/en/library/bg/2/17/", "That which pervades the body is indestructible."),
            ("SB 5.10 summary context", "https://vedabase.io/en/library/sb/5/10/", "Jaḍa Bharata teaches soul beyond bodily labels — narrative support."),
        ],
        "memory": "I am an eternal soul — conscious, individual, and meant for Kṛṣṇa's service.",
        "question": "If I am a soul, how should I live?",
        "conclusion": "The jīva is eternal, conscious, individual, minute, and related to Kṛṣṇa in service — not God Himself.",
        "misconception": "All souls are God / we are the Supreme.",
    },
    "C1-W4": {
        "slug": "c1-w4-why-human-life-is-rare-and-valuable",
        "title": "Why Human Life Is Rare and Valuable",
        "primary": ("SB 11.9.29", "https://vedabase.io/en/library/sb/11/9/29/", "After many births one attains the rare human form — use it for self-realization."),
        "supports": [
            ("BG 2.40", "https://vedabase.io/en/library/bg/2/40/", "No loss or diminution in this endeavor; a little progress protects from fear."),
            ("CC Madhya 24.229–282 (Nārada–Mṛgāri)", "https://vedabase.io/en/library/cc/madhya/24/", "Mercy and authorized instruction transform harmful conduct."),
        ],
        "memory": "Human life is a rare chance to ask who I am and serve Kṛṣṇa.",
        "question": "What deserves protected family time?",
        "conclusion": "Human life gives a rare opportunity for deliberate self-realization — protect inquiry and practice time.",
        "misconception": "Use fear or death-pressure to motivate children.",
    },
    "C1-W5": {
        "slug": "c1-w5-the-temporary-world-and-the-search-for-permanent-happiness",
        "title": "The Temporary World and the Search for Permanent Happiness",
        "primary": ("BG 8.15", "https://vedabase.io/en/library/bg/8/15/", "Having attained Me, great souls do not take rebirth into this temporary world of misery."),
        "supports": [
            ("BG 5.22", "https://vedabase.io/en/library/bg/5/22/", "Pleasures born of contact are temporary — supporting application."),
            ("BG 9.27", "https://vedabase.io/en/library/bg/9/27/", "Whatever you do, eat, offer, give — do as offering unto Me."),
        ],
        "memory": "Temporary joys can be used with gratitude; lasting fulfillment is in Kṛṣṇa.",
        "question": "How can enjoyment become gratitude and service?",
        "conclusion": "Temporary things can be used well but cannot provide permanent fulfillment.",
        "misconception": "Material things and family affection are worthless.",
    },
    "C1-W6": {
        "slug": "c1-w6-integration-night-who-am-i-and-how-should-our-family-live",
        "title": "Integration Night: Who Am I, and How Should Our Family Live?",
        "primary": ("Cycle 1 chain", "https://vedabase.io/en/library/sb/1/2/18/", "Review SB 1.2.18 · BG 2.13 · BG 2.20 · SB 11.9.29 · BG 8.15"),
        "supports": [
            ("SB 1.2.18", "https://vedabase.io/en/library/sb/1/2/18/", "W1 hearing"),
            ("BG 2.13", "https://vedabase.io/en/library/bg/2/13/", "W2 body/self"),
            ("BG 2.20", "https://vedabase.io/en/library/bg/2/20/", "W3 soul"),
            ("SB 11.9.29", "https://vedabase.io/en/library/sb/11/9/29/", "W4 human opportunity"),
            ("BG 8.15", "https://vedabase.io/en/library/bg/8/15/", "W5 lasting shelter"),
        ],
        "memory": "We remember who we are and how our family chooses to live.",
        "question": "Can our family explain and apply what we learned?",
        "conclusion": "Identity, purpose, and practice must form one coherent family life.",
        "misconception": "Competition or ranking of families.",
    },
}


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def md_to_docx(md_path: Path, docx_path: Path, title: str) -> None:
    doc = Document()
    doc.styles["Normal"].font.name = "Calibri"
    doc.styles["Normal"].font.size = Pt(11)
    doc.add_heading(title, 0)
    for line in md_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            continue
        if line.startswith("## "):
            doc.add_heading(line[3:], 1)
        elif line.startswith("### "):
            doc.add_heading(line[4:], 2)
        elif line.strip():
            doc.add_paragraph(line)
    docx_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(docx_path)


SCIENCE = {
    "C1-W1": [
        ("Implementation Intentions and Goal Achievement", "Gollwitzer, P. M., & Sheeran, P.", 2006, "10.1016/S0065-2601(06)38002-1", "https://doi.org/10.1016/S0065-2601(06)38002-1", "If-then plans increase follow-through on intended actions.", "Does not prove devotion; helps design saṅkalpa cues."),
        ("Family Routines and Rituals", "Fiese, B. H., et al.", 2002, "10.1111/1467-8624.t01-1-00525", "https://doi.org/10.1111/1467-8624.t01-1-00525", "Predictable family rituals associate with child well-being and belonging.", "Does not prove spiritual efficacy of hearing."),
    ],
    "C1-W2": [
        ("Body Image and Self-Concept in Childhood/Adolescence", "Smolak, L.", 2011, "10.1146/annurev-clinpsy-032210-104544", "https://doi.org/10.1146/annurev-clinpsy-032210-104544", "Body-image concerns can shape speech and peer comparison.", "Never claim psychology proves ātman; use only for respectful-language pedagogy."),
    ],
    "C1-W3": [],  # explicitly no proof science
    "C1-W4": [
        ("A Theory of Goal Setting and Task Performance", "Locke, E. A., & Latham, G. P.", 1990, "ISBN 978-0139174773", "https://doi.org/10.1037/0003-066X.57.9.705", "Clear priorities and protected goals improve follow-through.", "Supports time-protection pedagogy; not proof of human-form rarity."),
    ],
    "C1-W5": [
        ("Hedonic Relativism and Planning the Good Society", "Brickman, P., & Campbell, D. T.", 1971, "chapter in Adaptation-Level Theory", "https://psycnet.apa.org/record/1972-24270-001", "People adapt to rising material gains; lasting satisfaction is elusive from acquisition alone.", "Illustrates temporary contact pleasure; does not prove BG ontology."),
        ("Counting Blessings Versus Burdens", "Emmons, R. A., & McCullough, M. E.", 2003, "10.1037/0022-3514.84.2.377", "https://doi.org/10.1037/0022-3514.84.2.377", "Gratitude practices associate with well-being.", "Supports gratitude application; not proof of Kṛṣṇa."),
    ],
    "C1-W6": [
        ("Test-Enhanced Learning", "Roediger, H. L., & Karpicke, J. D.", 2006, "10.1111/j.1529-1006.2006.00027.x", "https://doi.org/10.1111/j.1529-1006.2006.00027.x", "Retrieval practice strengthens long-term retention.", "Supports review stations; not doctrinal proof."),
    ],
}

DEVOTIONAL = {
    "C1-W1": [
        ("Naimiṣāraṇya assembly — sages inquire about duty", "Śrīmad-Bhāgavatam Canto 1 opening narrative", "https://vedabase.io/en/library/sb/1/1/", "Models protected hearing community", "Narrative setting; paraphrase only"),
        ("Śrīla Prabhupāda's emphasis on regular hearing of Bhāgavatam", "SB 1.2 purport context / lecture practice", "https://vedabase.io/en/library/sb/1/2/18/", "Supports weekly rhythm", "Do not invent lecture quotations; use paraphrase + URL"),
    ],
    "C1-W2": [
        ("Arjuna's bodily attachment at Kurukṣetra opening", "Bhagavad-gītā Ch. 1–2 narrative", "https://vedabase.io/en/library/bg/1/", "Shows grief tied to bodily identification", "Do not invent dialogue beyond text"),
    ],
    "C1-W3": [
        ("Jaḍa Bharata and King Rahūgaṇa", "Śrīmad-Bhāgavatam 5.9–5.10", "https://vedabase.io/en/library/sb/5/10/", "Soul beyond bodily status labels", "Symbolic/nonviolent classroom retelling only"),
    ],
    "C1-W4": [
        ("Nārada and the hunter Mṛgāri", "Caitanya-caritāmṛta, Madhya-līlā 24.229–282", "https://vedabase.io/en/library/cc/madhya/24/", "Mercy and opportunity to change", "Paraphrase only; avoid graphic violence and unsupported additions"),
    ],
    "C1-W5": [
        ("Dhruva Mahārāja — mixed motive purified", "Śrīmad-Bhāgavatam 4.8–4.9", "https://vedabase.io/en/library/sb/4/8/", "Temporary ambition vs lasting shelter", "Do not promise identical results"),
    ],
    "C1-W6": [
        ("Cycle review — no new narrative required", "W1–W5 sources above", "https://vedabase.io/en/library/sb/1/2/18/", "Integration night retrieves prior examples", "No new unproven stories"),
    ],
}

CASES = {
    "C1-W1": [
        ("Saturday attenders, zero home practice", "Session alone equals growth", "SB 1.2.18 regularity", "Praise attendance; add 5-minute home cue"),
        ("Home chanting family withdraws from association", "Alone is safer than community", "Hearing in association + temple friendship", "Invite one low-pressure shared moment"),
        ("Parent compares children's seriousness", "Ranking produces devotion", "No comparison culture", "Redirect to personal minimum practice"),
    ],
    "C1-W2": [
        ("Sibling teases about appearance", "Body comments are harmless jokes", "BG 2.13 respectful speech", "Repair language; affirm dignity"),
        ("Teen obsesses over fitness identity", "Body project is the self", "Care for body as vehicle", "Keep health; refuse self=body slogan"),
        ("Relative asks child's weight publicly", "Public body talk is normal", "Privacy + respect", "Change subject; protect child"),
    ],
    "C1-W3": [
        ("Child says 'I am God'", "Soul = Supreme", "BG 15.7 fragmental part", "Correct gently: part, not whole"),
        ("Adult dismisses soul talk as anti-science", "Science disproved the soul", "Different domains", "Separate empirical method from śāstra claim"),
        ("Family neglects body care 'because we are soul'", "Body contempt is spiritual", "Care without identity confusion", "Restore rest/food/hygiene"),
    ],
    "C1-W4": [
        ("Screens consume protected practice slot", "Entertainment first is fine", "SB 11.9.29 opportunity", "Choose one protected 10-minute block"),
        ("Parent uses death scare on child", "Fear creates urgency", "Compassion not terror", "Speak opportunity, not threat"),
        ("Family fills calendar; no inquiry time", "Busy = successful", "Human form for realization", "Trade one optional activity for hearing"),
    ],
    "C1-W5": [
        ("New purchase chase after each weekend", "Next thing will satisfy", "BG 8.15 lasting shelter; BG 5.22 support", "Pause; gratitude before buy"),
        ("Parent shames child's toy joy", "Material joy is sinful", "Affection not worthless", "Allow lawful joy; add offering mood"),
        ("Work wins every conflict with prayer time", "Career alone is permanent security", "Temporary world framing", "Protect one non-negotiable spiritual cue"),
    ],
    "C1-W6": [
        ("Family fears presenting", "Presentation = ranking", "Non-competitive rubric", "Offer drawing-only option"),
        ("One child dominates share", "Loudest = wisest", "Team roles", "Assign greeting/drawing/sentence roles"),
        ("Parents want C2 immediately despite confusion", "Speed = progress", "Review-before-C2", "Private recommendation to extend C1"),
    ],
}

ANALOGIES = {
    "C1-W1": [
        ("Protected garden plot", "Regular watering grows roots", "kutumba-summary", "Not guaranteed bloom", "Water the plant together", "Map to Saturday + home cue"),
        ("Team practice night", "Show-up + drills both matter", "kutumba-summary", "Sports glory ≠ spiritual goal", "Pass a 'practice ball' (soft)", "Discuss missing home drills"),
        ("Path with fence", "Is/isn't boundaries keep path clear", "charter pedagogy", "Boundaries ≠ hostility", "Is/isn't card sort", "Charter purpose cards"),
    ],
    "C1-W2": [
        ("Changing garments", "Body like clothes; wearer continues", "BG 2.22", "Clothes chosen; bodies not", "Paper doll clothes", "Limitation discussion"),
        ("Life-stage photos", "Same person across ages", "BG 2.13", "Photos aren't ontology proof", "Consent timeline craft", "Respectful speech pledge"),
        ("Driver and vehicle", "Operator ≠ vehicle", "pedagogy", "Avoid harsh dualism", "Care for 'car' (body)", "Service without body-shame"),
    ],
    "C1-W3": [
        ("Sun and sunray", "Qualitative likeness; quantitative difference", "BG 15.7 pedagogy", "Ray is not the sun", "Flashlight + beam", "Part-and-parcel map"),
        ("Spark from fire", "Same nature, dependent", "traditional pedagogy", "Not independent Godhood", "Sparks craft (paper)", "Reject 'I am God'"),
        ("House and resident", "Resident ≠ house", "pedagogy", "Can feel impersonal", "Tidy sacred corner", "Care for body-house"),
    ],
    "C1-W4": [
        ("Rare ticket", "Opportunity must be used", "SB 11.9.29 pedagogy", "Not scare tactic", "Ticket craft", "Priority calendar"),
        ("Crossroads sign", "Choice of path matters", "pedagogy", "No species contempt", "Path choose game", "Time-jar allocation"),
        ("Seed season", "Plant while season open", "pedagogy", "No guaranteed harvest timing", "Plant seed cup", "Protect inquiry time"),
    ],
    "C1-W5": [
        ("Sparkler vs lamp", "Brief flash vs lasting light", "BG 5.22 support pedagogy", "Lawful joy not condemned", "Sparkler drawing", "Gratitude before enjoyment"),
        ("Saltwater drink", "Increases thirst", "classic pedagogy", "Not medical claim", "Thirst talk", "Acquisition loop map"),
        ("Offering plate", "Enjoyment becomes service", "BG 9.27", "Not empty ritualism", "Offer snack mood", "Whatever you do — offer"),
    ],
    "C1-W6": [
        ("Necklace of beads", "Weeks linked as one life", "integration pedagogy", "No ranking beads", "Bead string craft", "Concept chain poster"),
        ("Family recipe card", "Ingredients must combine", "pedagogy", "Not culinary perfectionism", "Write family recipe of practices", "10-min presentation plan"),
        ("Station map", "Retrieval strengthens memory", "cognitive pedagogy", "Not exam culture", "Visit stations", "Review-before-C2 decision"),
    ],
}


def research_pack(code: str, w: dict) -> None:
    base = WEEKLY / w["slug"] / "research"
    p = w["primary"]
    rows = "\n".join(
        f"| {r[0]} | {r[1]} | {r[2]} | Prefer paraphrase; no purport dump |" for r in w["supports"]
    )
    write(
        base / "SCRIPTURAL-EXAMPLES.md",
        f"""# {code} Scriptural Examples

## Primary anchor (locked)

| Reference | URL | Teaching paraphrase | Limitation |
|---|---|---|---|
| {p[0]} | {p[1]} | {p[2]} | Exact quotation only if verified; otherwise KUTUMBA paraphrase |

## Supporting primary references

| Reference | URL | Teaching use | Limitation |
|---|---|---|---|
{rows}

## Classroom use

1. Open the primary URL before teaching.
2. State paraphrase in plain English.
3. Name what this week does **not** teach.
4. Do not invent verse wording.
""",
    )

    if DEVOTIONAL[code]:
        drows = "\n".join(
            f"| {t} | {s} | {u} | {use} | {lim} |" for t, s, u, use, lim in DEVOTIONAL[code]
        )
        body = f"""## Selected examples (traceable)

| Example | Provenance | URL | Use | Limitation |
|---|---|---|---|---|
{drows}

## Policy

Bhakta-mālā and invented Rāmāyaṇa dialogue are **not** used this week. Supplementary examples never replace the primary verse.
"""
    else:
        body = "No supplementary historical example was selected after research; teach from primary verse and constructed cases only.\n"

    write(base / "DEVOTIONAL-AND-HISTORICAL-EXAMPLES.md", f"# {code} Devotional and Historical Examples\n\n{body}")

    cases = []
    for i, (sit, wrong, principle, action) in enumerate(CASES[code], 1):
        cases.append(
            f"""### Constructed case {i} — fictional / anonymized

- **Situation:** {sit}
- **Tempting mistaken conclusion:** {wrong}
- **Relevant principle / source:** {principle}
- **Compassionate response:** Acknowledge effort; avoid shame; return to one small practice.
- **Family action:** {action}
- **What not to say:** Comparisons, spiritual threats, public exposure of private struggles.
- **Age adaptation:** Younger — simplify to one sentence + action; Older — discuss mistaken conclusion explicitly.
"""
        )
    write(base / "CASE-STUDIES.md", f"# {code} Case Studies\n\n" + "\n".join(cases))

    sci = SCIENCE[code]
    if not sci:
        sci_body = """## Explicit decision

Empirical research is **not used this week as support for metaphysical claims** about the soul. Classroom focus stays on śāstra paraphrase, analogies with limits, and respectful questions.

If a parent asks for science proof of the soul, defer:
> "Laboratory methods measure bodies and behavior. Our teaching about the soul comes from śāstra. I will not claim science proves or disproves ātman."
"""
    else:
        lines = []
        for title, authors, year, doi, url, finding, limit in sci:
            lines.append(
                f"""### {title} ({year})

- **Authors:** {authors}
- **DOI / URL:** `{doi}` — {url}
- **Finding used:** {finding}
- **Limitation:** {limit}
- **Application:** Pedagogy/home-practice design only — **never** proof of ātman, karma, rebirth, or Kṛṣṇa.
"""
            )
        sci_body = "\n".join(lines)
    write(base / "SCIENCE-AND-APPLICATION.md", f"# {code} Science and Application\n\n{sci_body}")

    arows = []
    for name, teaches, status, fails, young, old in ANALOGIES[code]:
        arows.append(
            f"| {name} | {teaches} | {status} | {fails} | {young} | {old} |"
        )
    write(
        base / "ANALOGIES-AND-LIMITS.md",
        f"""# {code} Analogies and Limits

| Analogy | Teaching value | Source status | Failure point | Younger use | Older/adult use |
|---|---|---|---|---|---|
{chr(10).join(arows)}

## Rule

Label analogy as pedagogy. Never present analogy as śāstra quotation.
""",
    )


def facilitator_guide(code: str, w: dict) -> None:
    p = w["primary"]
    cases = "\n".join(f"{i}. {c[0]} → avoid: {c[1]}" for i, c in enumerate(CASES[code], 1))
    an = "\n".join(f"- **{a[0]}:** {a[1]} (limit: {a[3]})" for a in ANALOGIES[code])
    write(
        WEEKLY / w["slug"] / "teacher" / "MAIN-FACILITATOR-GUIDE-V11.md",
        f"""# {code} Main Facilitator Guide — Saturday 2:00–4:00

## Two-minute summary

{w['conclusion']} Primary scripture: **{p[0]}** ({p[1]}).

## Essential question

{w['question']}

## 15-minute night-before prep

1. Open {p[1]} and reread paraphrase: {p[2]}
2. Rehearse opening script aloud once.
3. Pack materials for younger + older tracks.
4. Review misconception: {w['misconception']}
5. Confirm snack/water plan (no weekly meal).

## 60-minute deep prep

1. Read `research/SCRIPTURAL-EXAMPLES.md` and `CASE-STUDIES.md`.
2. Mark three discussion questions you will actually ask.
3. Prepare one analogy with its limit.
4. Walk the room: parent / younger / older zones.
5. Pre-write home-practice minimum version on a card.
6. Review deferral line from `launch/TEACHER-READINESS-STANDARD.md`.

## Exact primary readings

- Primary: {p[0]} — {p[1]}
- Supports: {', '.join(s[0] for s in w['supports'][:3])}

## One-page speaking map

1. Welcome + Saturday purpose  
2. Memory line  
3. Primary verse paraphrase  
4. One analogy with limit  
5. One constructed case  
6. Track split  
7. Reunification synthesis  
8. Project + home practice + next week  

## Exact opening script (≈3 minutes)

> Welcome. Today is {code}: {w['title']}.  
> Our essential question is: {w['question']}  
> From {p[0]}, we remember: {p[2]}  
> We will hear together, practice in age bands, reunite, and take one small home step.  
> We do not rank families or children.

## Core explanation (facilitator must say)

{w['conclusion']}

Key paraphrase of {p[0]}: {p[2]}

Common error to block: **{w['misconception']}**

## Analogies / examples with limits

{an}

## Scriptural case

Use the primary narrative/context from `research/SCRIPTURAL-EXAMPLES.md` and `DEVOTIONAL-AND-HISTORICAL-EXAMPLES.md`. Paraphrase only.

## Historical/devotional examples

See sourced list in `research/DEVOTIONAL-AND-HISTORICAL-EXAMPLES.md`.

## Three constructed household cases

{cases}

## Discovery questions

1. What word in today's theme is new?
2. Where have you seen this tension at home?
3. What would a minimum version look like this week?

## Understanding questions

1. State this week's conclusion in one sentence.
2. Name the primary scripture.
3. What does this week **not** teach?

## Application questions

1. What is our family cue (time + place)?
2. Who will start the practice?
3. What is the minimum version if we are tired?

## Likely adult questions + source-based answers

| Question | Direction |
|---|---|
| Do we have to be perfect? | No — minimum versions are allowed; regularity matters ({p[0]}). |
| Can science prove this? | Science may help habits/language; doctrine rests on śāstra. |
| What if my child resists? | No force; shorter practice; parent models; private support conversation. |

## Common misconceptions

- {w['misconception']}
- Confusing analogy with scripture
- Importing next week's ontology early

## What not to speculate about

- Invented quotations or purport claims
- Private medical/spiritual diagnoses
- Guarantees of advancement, initiation, or certification

## Saturday time cues

| Time | Block |
|---|---|
| 1:50–2:00 | Arrival |
| 2:00–2:10 | Opening mantras |
| 2:10–2:30 | Shared opening / Prem-kī-Kathā |
| 2:30–3:10 | Parallel tracks |
| 3:10–3:30 | Reunification / bhakti lab |
| 3:30–3:40 | Snack + water |
| 3:40–3:55 | Saṅkalpa / project / Q |
| 3:55–4:00 | Closing |

## Track transition

At 2:28: "Parents remain in the parent circle. Younger friends go with [teacher]. Older students go with [teacher]. We reunite at 3:10."

## Family reunification synthesis

Invite one sentence per family: "This week we will…" tied to {w['question']}.

## Project contribution

See `project/CYCLE-CONTRIBUTION.md`.

## Home practice

5–15 minutes: memory line + one verse paraphrase + one gratitude/service act.

## Next-week preview

Name the next C1 week title only; do not teach its ontology early.

## Do not claim

Human/temple/CPO approval or publication readiness.
""",
    )


def younger_guide(code: str, w: dict) -> None:
    write(
        WEEKLY / w["slug"] / "teacher" / "YOUNGER-TEACHER-GUIDE.md",
        f"""# {code} Younger Teacher Guide (K–2)

## Objective

Children can say and show: **{w['memory']}**

## Exact memory phrase

> {w['memory']}

## Teacher background (2 minutes)

Primary: {w['primary'][0]} — {w['primary'][2]}  
Do not teach adult debates. Block: {w['misconception']}

## Age-appropriate story script (paraphrase boundary)

Tell a **simple classroom story** in your own words based on this week's sourced example in `research/DEVOTIONAL-AND-HISTORICAL-EXAMPLES.md`.  
Rules: no invented deity dialogue; no frightening detail; stop at the moral: {w['conclusion']}

Sample framing:
> "Today we learn that {w['conclusion']} The holy books help families remember this."

## Three wonder questions

1. What did you hear that was new?
2. Who can we serve with kindness this week?
3. When could our family practice for five minutes?

## Actual movement game (5–7 min)

**Name:** "Freeze and Remember — {code}"  
1. Children walk gently in a circle.  
2. When you say "Freeze!", they stop.  
3. You say the first half of the memory phrase; they finish it.  
4. Two rounds only; then sit.

## Actual hands-on activity (8–10 min)

**Object lesson:** Use the week craft object listed in materials (cup seed / paper doll / flashlight / ticket / offering plate drawing / bead).  
Children handle the object and answer: "This reminds me that…"

## Actual craft (8–10 min)

Create a take-home card with the memory phrase on the inside and a simple drawing on the front related to {w['title']}.

## Actual coloring / line-art task

Color `visuals/V11/line-art-younger.svg` (week-specific). Title the page with {code}.

## Sanskrit exposure (optional, 1 min)

Softly repeat one name: **Kṛṣṇa** or **Hare** — invitation only, never forced volume.

## Behavior redirects

- "Feet on the floor."  
- "Kind words only."  
- "That toy rests for now."  
- Quiet reset in visible space if needed.

## Backup low-prep activity

Sit in a circle; pass a soft object; each child says one kind word; end with memory phrase echo.

## Extension

Helper role: hand out crayons / collect papers.

## Materials

Printed line art; crayons; memory cards; soft toss object; craft card stock; tape.

## Cleanup / handoff

3 minutes cleanup. At door: tell parent the memory phrase and home cue.

## Home-practice explanation to parents

"Please say this phrase once at home and do one kind action. Five minutes is enough."
""",
    )


def older_guide_and_activities(code: str, w: dict) -> None:
    p = w["primary"]
    write(
        WEEKLY / w["slug"] / "teacher" / "OLDER-TEACHER-GUIDE.md",
        f"""# {code} Older Teacher Guide (Grades 4–5)

## Objective

Students explain: **{w['conclusion']}** using {p[0]}.

## Essential question

{w['question']}

## Text-observation task (10 min)

Open {p[1]}.  
Students write:
1. Who is speaking / what is the setting (if known)?  
2. One phrase that means "this continues" or "this is temporary/rare/eternal" depending on week.  
3. One sentence paraphrase in their own words.  
4. One thing this verse does **not** say.

## Diagram task

Complete labels on `visuals/V11/concept-diagram.svg` / Mermaid source. Week-specific — not a generic reused loop.

## Scenario cards

Use the three cases in `research/CASE-STUDIES.md`. In pairs: identify mistaken conclusion + better family action.

## Worksheet + puzzle

See `activities/OLDER-ACTIVITY-PACK.md` and grade with `activities/OLDER-ANSWER-KEY.md`.

## Project contribution

Advance: see `project/CYCLE-CONTRIBUTION.md`.

## Reflection

"Where did I confuse analogy with scripture today?"

## Extension

Prepare one sentence for reunification share.

## Boundaries

Misconception to block: {w['misconception']}  
Science may illustrate habits only — never prove metaphysics.
""",
    )

    # Real worksheet + matching puzzle content
    terms = {
        "C1-W1": [("Hearing", "Regular Bhāgavata reception"), ("Saṅkalpa", "Specific practice intention"), ("Charter", "KUTUMBA purposes/boundaries"), ("Association", "Learning with devotees")],
        "C1-W2": [("Body", "Changes through stages"), ("Self", "Continues as conscious person"), ("Analogy", "Pedagogy with limits"), ("Respect", "Speech about every body")],
        "C1-W3": [("Jīva", "Eternal individual soul"), ("Fragmental part", "Related to Kṛṣṇa, not equal as Supreme"), ("Eternal", "Not created or destroyed"), ("Service", "Natural relationship")],
        "C1-W4": [("Human form", "Rare opportunity"), ("Priority", "What we protect in time"), ("Compassion", "Mercy without contempt"), ("Opportunity", "Chance for inquiry")],
        "C1-W5": [("Temporary", "Has beginning and end"), ("Lasting", "Shelter in Kṛṣṇa"), ("Gratitude", "Thanks before enjoyment"), ("Offering", "Turning acts toward Kṛṣṇa")],
        "C1-W6": [("Integration", "Weeks form one life"), ("Retrieval", "Remembering on purpose"), ("Presentation", "Share without ranking"), ("Review", "Extend C1 if unclear")],
    }[code]

    matching = "\n".join(f"| {a} | {b} |" for a, b in terms)
    scrambled = "\n".join(f"{i}. {b} → ________" for i, (a, b) in enumerate(terms, 1))
    answers = "\n".join(f"{i}. {a}" for i, (a, b) in enumerate(terms, 1))

    write(
        WEEKLY / w["slug"] / "activities" / "OLDER-ACTIVITY-PACK.md",
        f"""# {code} Older Activity Pack (Grades 4–5)

## A. Concept worksheet (write answers)

1. State this week's conclusion in one sentence.  
2. Write the primary scripture reference: _______________  
3. Paraphrase it in your words (no copying long text).  
4. Name one misconception to avoid.  
5. Write one family action for the next 7 days.  
6. Essential question: {w['question']} — answer in 2–3 sentences.

## B. Matching puzzle

Match term → meaning:

| Term | Meaning |
|---|---|
{matching}

Print as two cut columns and match, **or** write letters A–D.

## C. Scenario response card

Pick Constructed case 1 from `research/CASE-STUDIES.md`.  
Write: mistaken conclusion / better response / one sentence you would say at home.

## D. Diagram task

On the week diagram, label every node and draw one arrow that shows this week's primary conclusion.

## E. Project / poster component

Produce one artifact for: {w.get('project', w['conclusion']) if False else code} project layer in `project/CYCLE-CONTRIBUTION.md`.

## F. Optional reflection

Circle one: I confused analogy with scripture / I stayed in week scope / I need review.

## Low-prep backup

Pair-share essential question for 3 minutes; each writes one sentence.
""",
    )

    write(
        WEEKLY / w["slug"] / "activities" / "OLDER-ANSWER-KEY.md",
        f"""# {code} Older Answer Key

## Worksheet — secure answers

1. {w['conclusion']}
2. {p[0]}
3. Accept any faithful paraphrase of: {p[2]}
4. {w['misconception']}
5. Any concrete 5–15 minute cue tied to the week
6. Answers should connect identity/practice without ranking

## Matching key

{matching}

## Scramble key (if used)

{answers}

## Scenario grading

Secure = names mistaken conclusion + compassionate action + no shame language.

## Do not accept

- Invented verse numbers  
- "Science proves the soul"  
- Importing another week's full ontology as if it were this week's only point
""",
    )

    write(
        WEEKLY / w["slug"] / "activities" / "YOUNGER-ACTIVITY-PACK.md",
        f"""# {code} Younger Activity Pack (K–2)

## 1. Coloring / line-art

Use week-specific `../visuals/V11/line-art-younger.svg`.  
Prompt: color the scene that shows today's idea — **not** a generic recycled hearing scene unless this is W1.

## 2. Movement game

Play "Freeze and Remember — {code}" from the younger teacher guide.

## 3. Craft / foldable

Fold a card: outside picture; inside memory phrase.

## 4. Memory card

Front: simple icon for {code}. Back: {w['memory']}

## 5. Take-home family cue

Ask at home: {w['question']} (one sentence each)

## Materials

Crayons, card stock, printed SVG, soft object for freeze game.
""",
    )


def visuals(code: str, w: dict) -> None:
    v = WEEKLY / w["slug"] / "visuals" / "V11"
    diagrams = {
        "C1-W1": (
            'flowchart LR\n  H[Hear] --> D[Discuss]\n  D --> P[Practice]\n  P --> R[Reflect]\n  R --> S[Serve]\n  S --> H\n  X[Saturday 2-4 protected] --> H\n',
            "KUTUMBA growth loop + protected Saturday",
            [(80, 180, "Hear"), (220, 180, "Discuss"), (360, 180, "Practice"), (500, 180, "Reflect"), (640, 180, "Serve")],
            "Family sits with a book — protected practice time",
        ),
        "C1-W2": (
            'flowchart LR\n  C[Childhood] --> Y[Youth]\n  Y --> O[Old age]\n  C --> Self[Conscious self continues]\n  Y --> Self\n  O --> Self\n',
            "Life stages — same self continues",
            [(80, 160, "Child"), (260, 160, "Youth"), (440, 160, "Elder"), (260, 300, "Self continues")],
            "Same person at three ages connected by a thread",
        ),
        "C1-W3": (
            'flowchart TB\n  J[Jiva eternal conscious individual]\n  J --> Yes[Serves Krishna]\n  J --> No1[Not the Supreme]\n  J --> No2[Not the temporary body]\n  J --> No3[Not created then destroyed]\n',
            "What the jiva is / is not",
            [(300, 80, "Jiva"), (80, 240, "Serves"), (300, 240, "Not God"), (520, 240, "Not body")],
            "Child offering a flower — I serve Krishna",
        ),
        "C1-W4": (
            'flowchart LR\n  T[Time jar] --> Must[Protected inquiry]\n  T --> Should[Family duties]\n  T --> Optional[Optional screens]\n',
            "Human-life priority / time map",
            [(80, 180, "Time jar"), (300, 100, "Must"), (300, 200, "Should"), (300, 300, "Optional")],
            "Child placing a block into a Must jar — use time well",
        ),
        "C1-W5": (
            'flowchart LR\n  Temp[Temporary contact joy] --> Adapt[Fades / hankering]\n  Last[Lasting shelter in Krishna] --> Thanks[Gratitude + offering]\n',
            "Temporary vs lasting fulfillment",
            [(80, 140, "Temporary"), (320, 140, "Fades"), (80, 280, "Lasting"), (320, 280, "Offer")],
            "Sorting cards: sparkler vs lamp — temporary vs lasting",
        ),
        "C1-W6": (
            'flowchart LR\n  W1[W1 Hearing] --> W2[W2 Body/self]\n  W2 --> W3[W3 Soul]\n  W3 --> W4[W4 Human life]\n  W4 --> W5[W5 Lasting shelter]\n  W5 --> Live[Family life]\n',
            "Cycle 1 concept chain",
            [(40, 180, "W1"), (160, 180, "W2"), (280, 180, "W3"), (400, 180, "W4"), (520, 180, "W5"), (640, 180, "Live")],
            "Family presentation seats — share without ranking",
        ),
    }
    mmd, title, boxes, line_caption = diagrams[code]
    write(v / "concept-diagram.mmd", mmd)
    rects = []
    for x, y, label in boxes:
        rects.append(f'<rect x="{x}" y="{y}" width="110" height="50" rx="8" fill="#e8f0fe" stroke="#4a6fa5"/>')
        rects.append(f'<text x="{x+55}" y="{y+30}" text-anchor="middle" font-size="12">{label}</text>')
    write(
        v / "concept-diagram.svg",
        f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" role="img">
  <title>{code} {title}</title>
  <rect width="800" height="420" fill="#faf8f5"/>
  <text x="400" y="36" text-anchor="middle" font-size="18" font-family="Segoe UI,sans-serif">{code}: {title}</text>
  {''.join(rects)}
  <text x="400" y="390" text-anchor="middle" font-size="12">{w['conclusion'][:90]}</text>
  <text x="400" y="410" text-anchor="middle" font-size="10" fill="#666">{w['primary'][0]} · KUTUMBA-original · human review required</text>
</svg>
""",
    )
    # distinct line art per week via different shapes
    art = {
        "C1-W1": '<rect x="150" y="200" width="300" height="180" fill="none" stroke="#000" stroke-width="2"/><circle cx="250" cy="320" r="35" fill="none" stroke="#000" stroke-width="2"/><circle cx="360" cy="320" r="35" fill="none" stroke="#000" stroke-width="2"/>',
        "C1-W2": '<circle cx="180" cy="300" r="40" fill="none" stroke="#000" stroke-width="2"/><circle cx="300" cy="300" r="50" fill="none" stroke="#000" stroke-width="2"/><circle cx="440" cy="300" r="45" fill="none" stroke="#000" stroke-width="2"/><line x1="180" y1="300" x2="440" y2="300" stroke="#000" stroke-width="2"/>',
        "C1-W3": '<circle cx="300" cy="260" r="70" fill="none" stroke="#000" stroke-width="2"/><path d="M300 330 L300 420" stroke="#000" stroke-width="2"/><path d="M260 380 L340 380" stroke="#000" stroke-width="2"/>',
        "C1-W4": '<rect x="200" y="220" width="200" height="220" fill="none" stroke="#000" stroke-width="2"/><line x1="200" y1="300" x2="400" y2="300" stroke="#000"/><line x1="200" y1="360" x2="400" y2="360" stroke="#000"/>',
        "C1-W5": '<path d="M180 360 L220 220 L260 360 Z" fill="none" stroke="#000" stroke-width="2"/><rect x="340" y="220" width="40" height="140" fill="none" stroke="#000" stroke-width="2"/><circle cx="360" cy="200" r="20" fill="none" stroke="#000" stroke-width="2"/>',
        "C1-W6": '<rect x="120" y="240" width="100" height="70" fill="none" stroke="#000"/><rect x="250" y="240" width="100" height="70" fill="none" stroke="#000"/><rect x="380" y="240" width="100" height="70" fill="none" stroke="#000"/><path d="M220 275 L250 275 M350 275 L380 275" stroke="#000" stroke-width="2"/>',
    }[code]
    write(
        v / "line-art-younger.svg",
        f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 612 792" role="img">
  <title>{code} younger line art</title>
  <rect width="612" height="792" fill="#ffffff"/>
  <text x="306" y="64" text-anchor="middle" font-size="18">{code} coloring sheet</text>
  {art}
  <text x="306" y="520" text-anchor="middle" font-size="14">{line_caption}</text>
  <text x="306" y="560" text-anchor="middle" font-size="12">{w['memory'][:80]}</text>
  <text x="306" y="740" text-anchor="middle" font-size="10">Original KUTUMBA line art · no copyrighted tracing</text>
</svg>
""",
    )
    write(
        v / "IMAGE-GENERATION-PROMPTS.md",
        f"""# {code} Image Generation Prompts

## Family deck hero
Warm instructional scene for {w['title']}; no deity caricature; 16:9.

## Younger coloring
{line_caption}; large outlines; US Letter.

## Older concept
{title}; diagrammatic; leave label space.

## Constraints
No frightening imagery; no invented sacred iconography; not historical archival art.
""",
    )
    write(
        v / "VISUAL-RIGHTS-REGISTER.yaml",
        f"""module: {code}
assets:
  - id: {code.lower()}-concept
    title: "{title}"
    creator: KUTUMBA
    license_rights_status: kutumba-original
    intended_use: teaching-diagram
  - id: {code.lower()}-line-art
    title: "{line_caption}"
    creator: KUTUMBA
    license_rights_status: kutumba-original
    intended_use: printable-coloring
""",
    )


def gamma(code: str, w: dict) -> None:
    g = WEEKLY / w["slug"] / "gamma"
    p = w["primary"]

    def slide(n, title, audience, purpose, content, notes, visual, prompt, interaction, donot):
        return f"""### Slide {n} — {title}

- **Audience:** {audience}
- **Purpose:** {purpose}
- **On-slide content:**
{content}
- **Presenter notes:** {notes}
- **Primary source:** {p[0]} — {p[1]}
- **Suggested visual:** {visual}
- **Image/diagram prompt:** {prompt}
- **Interaction:** {interaction}
- **Do-not-claim:** {donot}
- **Accessibility note:** Large type; high contrast; read key lines aloud.
"""

    if code == "C1-W1":
        master_slides = []
        topics = [
            ("Welcome to KUTUMBA", "Name founding cohort; Saturday 2–4"),
            ("What KUTUMBA is", "Family sādhana community; parents onsite"),
            ("What KUTUMBA is not", "Not drop-off, substitute temple, ranking club"),
            ("Why families commit", "Protected hearing + home practice"),
            ("First six-month map", "C1 identity → C2 karma/modes → C3 bhakti"),
            ("C1 / C2 / C3 preview", "One sentence each; no deep dive"),
            ("Saturday rhythm", "Arrival 1:50; end 4:00; snack/water only"),
            ("Six-week cycle + off week + Utsava", "Sep–Oct calendar; Oct 31 candidate only"),
            ("Parent commitment", "Covenant highlights"),
            ("Child house rules", "Safe body; kind words; freeze cue"),
            ("Correction ladder", "Reminder → redirect → reset → parent"),
            ("Teacher readiness", "Objective, source, boundary, deferral"),
            ("Privacy / no comparison / no gossip", "No public sādhana scoring"),
            ("Host-home respect", "Common rules + host property"),
            ("Opening mantras", "Praṇāma, Pañca-tattva, mahā-mantra"),
            ("Cycle 1 project", "Who Am I… cumulative"),
            ("Week 1 philosophy SB 1.2.18", p[2]),
            ("Story / application", "Hearing community; home cue"),
            ("Bhakti lab preview", "Short shared practice"),
            ("Family saṅkalpa", "Action + frequency + trigger + minimum"),
            ("Home practice", "5–15 minutes"),
            ("Feedback route", "Private questions"),
            ("Next week preview", "C1-W2 body/self — title only"),
            ("Closing", "Thank host; end on time"),
        ]
        for i, (t, c) in enumerate(topics, 1):
            master_slides.append(
                slide(
                    i,
                    t,
                    "master",
                    "Orientation + Week 1 launch",
                    f"  - {c}\n  - Memory: {w['memory']}",
                    "Stay warm and firm; no ranking.",
                    "V11 W1 diagram / line art",
                    f"Instructional slide art for: {t}",
                    "One echo question or show of hands",
                    "Not human-approved; not publication-ready; Gamma not rendered",
                )
            )
        write(g / "V11-GAMMA-MASTER-DECK-PROMPT.md", f"# {code} V11 Gamma Master Deck Prompt\n\n**Status:** prompt-only — not rendered — not approved\n\n## Deck identity\n- {code} — {w['title']}\n- 16:9 Saturday founding cohort\n\n## Slides\n\n" + "\n".join(master_slides))
    else:
        count = 14 if code != "C1-W6" else 16
        slides = []
        base_topics = [
            f"Title: {w['title']}",
            f"Essential question: {w['question']}",
            f"Primary verse {p[0]}",
            f"Paraphrase: {p[2]}",
            f"Conclusion: {w['conclusion']}",
            f"Misconception to block: {w['misconception']}",
            "Analogy 1 with limit",
            "Analogy 2 with limit",
            "Constructed case",
            "Age-band track preview",
            "Bhakti lab / reunification",
            "Project layer",
            "Home practice",
            "Next step / closing",
        ]
        if code == "C1-W6":
            base_topics = [
                "Integration night welcome",
                "Concept chain W1–W5 (BG 8.15 for W5)",
                "Retrieval station map",
                "Non-competitive rubric",
                "Presentation template 10 minutes",
                "Four-family flow",
                "Drawing / speech / action options",
                "What success means tonight",
                "Review-before-C2 guide",
                "Off-week continuity",
                "Utsava candidate note",
                "Family gratitude round",
                "Home practice continuity",
                "No ranking reminder",
                "Feedback",
                "Closing",
            ]
        for i, t in enumerate(base_topics[:count], 1):
            slides.append(
                slide(
                    i,
                    t.split(":")[0][:40],
                    "master",
                    f"Teach {code} with week-specific content",
                    f"  - {t}\n  - Source: {p[0]}",
                    f"Do not import other weeks' full ontology. Block: {w['misconception']}",
                    f"V11 {code} diagram",
                    f"Unique diagram for {code}: {t}",
                    "Ask one student to restate the conclusion",
                    "Not approved; not rendered; science ≠ siddhānta proof",
                )
            )
        write(g / "V11-GAMMA-MASTER-DECK-PROMPT.md", f"# {code} V11 Gamma Master Deck Prompt\n\n**Status:** prompt-only — not rendered — not approved\n\n## Slides\n\n" + "\n".join(slides))

    # Audience decks — materially different
    write(
        g / "V11-GAMMA-PARENT-DECK-PROMPT.md",
        f"""# {code} V11 Gamma Parent Deck Prompt

**Status:** prompt-only — not rendered — not approved

## Focus
Adult application, household cases, saṅkalpa design, speech ethics.

## Slides (12)

1. Adult essential question: {w['question']}
2. Primary verse for parents: {p[0]}
3. Household implication of: {w['conclusion']}
4. Case A from research/CASE-STUDIES.md
5. Case B
6. What not to say at home
7. Home practice 5–15 minutes
8. Partner/co-parent cue planning
9. Screens / time conflicts (if relevant)
10. Project contribution this week
11. Privacy and no comparison
12. Closing commitment sentence
""",
    )
    write(
        g / "V11-GAMMA-YOUNGER-DECK-PROMPT.md",
        f"""# {code} V11 Gamma Younger Deck Prompt

**Status:** prompt-only — not rendered — not approved

## Focus
K–2: story, movement, craft, memory phrase — few words per slide.

## Slides (10)

1. Picture welcome
2. Memory phrase: {w['memory']}
3. Story picture (sourced paraphrase only)
4. Wonder question 1
5. Movement game cue: Freeze and Remember
6. Hands-on object
7. Craft card
8. Coloring sheet
9. Kind words / cleanup
10. Tell parents the phrase
""",
    )
    write(
        g / "V11-GAMMA-OLDER-DECK-PROMPT.md",
        f"""# {code} V11 Gamma Older Deck Prompt

**Status:** prompt-only — not rendered — not approved

## Focus
Grades 4–5: text observation, diagram, scenarios, worksheet.

## Slides (12)

1. Essential question
2. Open {p[0]} link task
3. Observation prompts
4. Paraphrase vs quotation
5. Diagram labels
6. Matching puzzle instructions
7. Scenario card work
8. Misconception check: {w['misconception']}
9. Project artifact
10. Reflection prompt
11. Reunification sentence
12. Home practice
""",
    )
    write(
        g / "V11-GAMMA-SOURCE-MAP.yaml",
        f"""module: {code}
render_status: prompt-only-not-rendered
primary_verse: {p[0]}
primary_url: {p[1]}
locked_chain_note: "W5 primary is BG 8.15; W6 reviews W1-W5 with BG 8.15 for W5"
do_not_claim: [human-approved, publication-ready, gamma-rendered]
""",
    )


def update_project_chain() -> None:
    # Fix W5/W6 primary references in project rubrics
    for code, w in WEEKS.items():
        base = WEEKLY / w["slug"] / "project"
        p = w["primary"]
        write(
            base / "PRESENTATION-RUBRIC.md",
            f"""# {code} Presentation Rubric (Non-Competitive)

| Dimension | Emerging | Developing | Secure |
|---|---|---|---|
| Understanding | Vague topic | States conclusion | Connects to {p[0]} paraphrase |
| Application | No home link | One action | Clear cue + minimum version |
| Teamwork | One speaker only | Partial family roles | Parents + children share |
| Source accuracy | Mixes weeks / invents | Stays in week scope | Distinguishes scripture vs analogy |

## Locked primary for this week

{p[0]} — {p[1]}

## W6 chain reminder

When reviewing Cycle 1, represent W5 with **BG 8.15** (not BG 5.22 as primary).

No ranking. Weak understanding → private review-before-C2 recommendation.
""",
        )


def deepen_launch() -> None:
    write(
        LAUNCH / "KUTUMBA-C1-FAMILY-ORIENTATION.md",
        """# KUTUMBA Cycle 1 Family Orientation Handout

## 1. Welcome

KUTUMBA is a family-oriented Krishna consciousness formation program. Cycle 1 is for four founding families on Saturday **2:00–4:00 PM**. Parents remain onsite. This is not a drop-off program.

## 2. What KUTUMBA is / is not

| Is | Is not |
|---|---|
| Protected weekly hearing + home practice | Social club only |
| Parent-onsite shared learning | Substitute temple |
| Respectful spiritual friendship | Ranking or public sādhana scoring |
| Voluntary commitment | Initiation or certification track |

## 3. First six-month map

- **Cycle 1 — Identity:** body/self, soul, human opportunity, lasting shelter, integration
- **Cycle 2 — Karma and modes:** action, responsibility, material nature
- **Cycle 3 — Bhakti:** Kṛṣṇa, guru-sādhu-śāstra, holy name, nine processes

## 4. Saturday schedule (locked)

Arrival 1:50. Opening mantras 2:00. Parallel tracks 2:30–3:10. Reunification 3:10. Snack/water 3:30. Close by 4:00. **No weekly meal.**

## 5. Cycle rhythm

Six active Saturdays → one protected off week → C1 Utsava/showcase candidate. If understanding is weak, review/extend C1 before C2.

## 6. Expectations

Protect the calendar; communicate absences; attempt minimum home practice; respect host property; follow child rules; avoid gossip/comparison.

## 7. Home practice

Usually 5–15 minutes. Minimum versions are success, not failure.

## 8. Family project

**Who Am I, and How Should Our Family Live?** builds weekly and culminates in a non-competitive W6 share (~10 minutes/family).

## 9. Rules and correction

See Child House Rules and Family Covenant. Correction ladder never uses public shame.

## 10. Feedback and privacy

Private feedback route only. No photography/recording by default. Do not publish real child data in shared repos.

## 11. Reasonable six-month destination

Stronger vocabulary; clearer foundations; small sustainable home rhythm; age-appropriate explanation; respectful speech and temple connection. **No promise** of certification, initiation eligibility, or guaranteed advancement.

## 12. FAQ

**Must both parents attend?** Aim for whole-family participation; communicate constraints privately.  
**What if we miss a week?** Communicate; receive home practice; no public penalty.  
**Are Gamma decks required?** No — prompts exist; decks are not rendered/approved.
""",
    )
    write(
        LAUNCH / "KUTUMBA-C1-TEACHER-HANDBOOK.md",
        """# KUTUMBA Cycle 1 Teacher Handbook

## 1. Purpose

This handbook helps lesson-ready teachers run Cycle 1 without inventing doctrine.

## 2. Source hierarchy

1. Śrīla Prabhupāda books / BBT VedaBase  
2. Traceable lectures/letters/conversations  
3. Authorised ISKCON materials  
4. Other sources only with provenance  
5. Academic research for pedagogy/application only  
6. Constructed cases clearly labelled fictional  

## 3. No-speculation rule

If unsure, say:  
> "I don't want to guess. I will verify that from Śrīla Prabhupāda's books / our source packet and come back to you."

## 4. Locked C1 primary anchors

| Week | Primary |
|---|---|
| W1 | SB 1.2.18 |
| W2 | BG 2.13 |
| W3 | BG 2.20 |
| W4 | SB 11.9.29 |
| W5 | BG 8.15 |
| W6 | Review chain (W5 = BG 8.15) |

## 5. Child development expectations

Younger K–2: short story, movement, craft, memory phrase.  
Older Grades 4–5: text observation, diagram, scenarios, worksheet.

## 6. Correction ladder

Reminder → redirect → quiet reset → parent → sit out activity → private conversation. Never shame, yell, force chanting, or compare.

## 7. Preparation

Use `TEACHER-PRE-WEEK-CHECKLIST.md` plus each week's `teacher/PRE-WEEK-CHECKLIST.md` and `MAIN-FACILITATOR-GUIDE-V11.md`.

## 8. Hard questions

Separate śāstra claims from science. Do not claim lab proof of soul/karma/God.

## 9. Stories, analogies, science

Stories need provenance. Analogies need limits. Science needs citation and limitation.

## 10. Parent handoff

At reunification, give memory phrase + one home cue. No private child evaluations in public.

## 11. Week-by-week checklist

Before each Saturday: objective, primary URL open, misconception, materials, backup game, reunification plan.

## 12. Glossary (short)

**Paraphrase** — our words for a verse meaning. **Analogy** — teaching comparison with limits. **Constructed case** — fictional teaching story. **Saṅkalpa** — specific practice intention.
""",
    )

    write(
        WEEKLY / WEEKS["C1-W1"]["slug"] / "launch-pack" / "MAIN-FACILITATOR-SCRIPT.md",
        """# Main Facilitator Script — C1-W1 (15–25 minutes usable speaking)

## 0:00–1:00 Welcome

> Welcome, families. My name is [facilitator]. Today we begin Cycle 1 of KUTUMBA on Saturday from 2:00 to 4:00. Parents stay with us — this is not a drop-off program. We end on time.

## 1:00–3:00 What KUTUMBA is / is not

> KUTUMBA is a family sādhana and formation community. We protect weekly hearing, practice at home, and grow respectful association.  
> KUTUMBA is not a social club only, not a substitute temple, not an initiation pathway, and not a contest. We do not rank children or families.

## 3:00–6:00 Six-month map

> In the first six months we move through three cycles: Cycle 1 identity foundations; Cycle 2 karma and the modes; Cycle 3 bhakti — Kṛṣṇa, guru-sādhu-śāstra, and the holy name.  
> Cycle 1 has six Saturdays, then a protected off week, then a simple Utsava/showcase candidate. If we need more review, we extend Cycle 1 before Cycle 2.

## 6:00–9:00 Covenant, rules, teachers

> Please read the Family Covenant. We communicate absences, attempt a small home practice, respect the host home, and avoid gossip and comparison.  
> Children follow house rules: safe body, kind words, freeze cue, no furniture jumping, devices away, snack only in the snack area.  
> Teachers teach from the packet. If they do not know, they will verify from Śrīla Prabhupāda's books rather than guess.

## 9:00–14:00 SB 1.2.18 introduction

> Our key verse is Śrīmad-Bhāgavatam 1.2.18. In plain words: regular hearing and service connected with the Bhāgavata cleanses the heart and steadies devotion.  
> That is why Saturday alone is not enough — we also take a five-to-fifteen-minute home practice.  
> Interactive question 1: What do you hope your home feels like spiritually one year from now? (silent write)  
> Interactive question 2: What usually steals protected hearing time in your week?  
> Interactive question 3: What would a minimum home practice look like if everyone is tired?

## 14:00–17:00 Project + saṅkalpa

> Our Cycle 1 project is: Who Am I, and How Should Our Family Live? Week 1 contribution is a family purpose card and first saṅkalpa: specific action + frequency + trigger + minimum version.  
> Example: After dinner on Sunday, we read one verse paraphrase for five minutes; minimum version is one gratitude sentence.

## 17:00–18:00 Transition to tracks

> In a moment, parents remain for the parent lesson. Younger children go with the younger teacher. Older students go with the older teacher. We reunite at 3:10 for bhakti lab and closing.

## Closing / W2 preview (end of session)

> Thank you to our host. Next Saturday is C1-W2 — I Am Not This Body — where we learn that the body changes and the conscious self continues. Please try this week's home practice. Feedback is private and welcome. We end now so families can leave peacefully.
""",
    )

    # Improve mantra source precision
    mantras = (LAUNCH / "OPENING-MANTRAS-HANDOUT.md").read_text(encoding="utf-8")
    mantras = mantras.replace(
        "**Source:** https://vedabase.io/en/library/cc/adi/1/ — related praṇāma tradition; confirm local authorized chanting sheet.",
        "**Source note:** The two standard Śrīla Prabhupāda praṇāma verses are used throughout ISKCON temple practice. A stable public verse-page specifically titled for these praṇāma lines is not always presented as a standalone VedaBase “verse object.” Use your temple’s authorised chanting sheet as the exact-text control; VedaBase CC Ādi context: https://vedabase.io/en/library/cc/adi/1/ . Do not invent additional lines.",
    )
    write(LAUNCH / "OPENING-MANTRAS-HANDOUT.md", mantras)


def regenerate_docx() -> None:
    md_to_docx(LAUNCH / "KUTUMBA-C1-FAMILY-ORIENTATION.md", LAUNCH / "KUTUMBA-C1-FAMILY-ORIENTATION.docx", "KUTUMBA C1 Family Orientation")
    md_to_docx(LAUNCH / "KUTUMBA-C1-TEACHER-HANDBOOK.md", LAUNCH / "KUTUMBA-C1-TEACHER-HANDBOOK.docx", "KUTUMBA C1 Teacher Handbook")
    md_to_docx(LAUNCH / "OPENING-MANTRAS-HANDOUT.md", LAUNCH / "OPENING-MANTRAS-HANDOUT.docx", "Opening Mantras Handout")
    for code, w in WEEKS.items():
        base = WEEKLY / w["slug"]
        exp = base / "exports"
        md_to_docx(base / "teacher" / "MAIN-FACILITATOR-GUIDE-V11.md", exp / f"{code}-MAIN-FACILITATOR-GUIDE.docx", f"{code} Main Facilitator Guide")
        md_to_docx(base / "teacher" / "YOUNGER-TEACHER-GUIDE.md", exp / f"{code}-YOUNGER-TEACHER-GUIDE.docx", f"{code} Younger Teacher Guide")
        md_to_docx(base / "teacher" / "OLDER-TEACHER-GUIDE.md", exp / f"{code}-OLDER-TEACHER-GUIDE.docx", f"{code} Older Teacher Guide")
        home = base / "family-home-practice.md"
        if home.exists():
            md_to_docx(home, exp / f"{code}-FAMILY-HANDOUT.docx", f"{code} Family Handout")


def main() -> int:
    deepen_launch()
    update_project_chain()
    for code, w in WEEKS.items():
        research_pack(code, w)
        facilitator_guide(code, w)
        younger_guide(code, w)
        older_guide_and_activities(code, w)
        visuals(code, w)
        gamma(code, w)
        # sync project brief primary refs lightly
        write(
            WEEKLY / w["slug"] / "project" / "CYCLE-CONTRIBUTION.md",
            f"""# {code} Cycle Contribution

## Cumulative project

**Who Am I, and How Should Our Family Live?**

## This week's layer

Tied to {w['primary'][0]}: {w['conclusion']}

## Family action

1. Create one artifact answering: {w['question']}
2. Keep burden ≤20 minutes optional work (W6: low-burden presentation option).
3. No ranking; no forced disclosure.

## Primary source

{w['primary'][0]} — {w['primary'][1]}
""",
        )
    regenerate_docx()
    print("V11.1 content-depth generation complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

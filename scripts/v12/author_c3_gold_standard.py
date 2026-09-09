#!/usr/bin/env python3
"""Author V12.1 gold-standard C3 week packs (F07–F09, F12–F14, F19).

Generates executable facilitator depth, teacher guides, activities,
research files, and Gamma prompts. Verse integrity for W4–W6 is assumed
already corrected in verse_data.yaml / launch packs.
"""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

FORBIDDEN = [
    "Use week research ANALOGIES",
    "Week craft tied to",
    "See activities as sole instruction",
    "Family struggles to apply",
    "week research + launch policy",
    "Week objective for",
    "Stay in week scope as body",
    "meaning[:",
]


def assert_clean(text: str, label: str) -> None:
    for bad in FORBIDDEN:
        if bad in text:
            raise SystemExit(f"Forbidden phrase in {label}: {bad!r}")


# ---------------------------------------------------------------------------
# Shared scaffolding helpers
# ---------------------------------------------------------------------------

HEADER = """**KUTUMBA • Families Growing in Krishna Consciousness**
**Program Director: Swapnil Patil**
**Status:** Internal founding-cohort teaching material — human/temple review EXTERNAL_OPEN
"""

SATURDAY = """## Saturday time cues (locked)

| Clock | Block |
| --- | --- |
| 1:50 | Facilitator arrival; room zones; snack/water table ready (no weekly meal) |
| 2:00 | Opening mantras / welcome; parents remain onsite |
| 2:10 | Opening script + verse layer (all ages together) |
| 2:30 | Age tracks (younger + older) with parents nearby / onsite |
| 3:10 | Reunification share (no ranking) |
| 3:30 | Snack and water |
| 3:40 | Saṅkalpa / home-practice card |
| 3:55 | Close and cleanup |
| 4:00 | End |

Parents stay onsite for the full Saturday 2:00–4:00 window. Do not claim temple, human, or publication approval.
"""


def week_dirs() -> dict[str, Path]:
    out = {}
    for d in WEEKLY.iterdir():
        if d.is_dir() and d.name.startswith("c3-w"):
            key = d.name[:5]  # c3-w1 ... c3-w6 (unicode-safe enough)
            # Prefer full slug match by week code prefix
            if d.name.startswith("c3-w1"):
                out["C3-W1"] = d
            elif d.name.startswith("c3-w2"):
                out["C3-W2"] = d
            elif d.name.startswith("c3-w3"):
                out["C3-W3"] = d
            elif d.name.startswith("c3-w4"):
                out["C3-W4"] = d
            elif d.name.startswith("c3-w5"):
                out["C3-W5"] = d
            elif d.name.startswith("c3-w6"):
                out["C3-W6"] = d
    missing = [k for k in ("C3-W1", "C3-W2", "C3-W3", "C3-W4", "C3-W5", "C3-W6") if k not in out]
    if missing:
        raise SystemExit(f"Missing week folders: {missing}")
    return out


# Import week content builders from companion module to keep this file runnable
# even if split; for single-file delivery, content is defined below.

from author_c3_gold_content import WEEKS  # type: ignore  # noqa: E402


def write(path: Path, text: str) -> None:
    assert_clean(text, str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.replace("\r\n", "\n").strip() + "\n", encoding="utf-8")


def build_main(w: dict) -> str:
    cases = "\n\n".join(
        f"""### Case {i}: {c['title']}
- **Situation:** {c['situation']}
- **Mistaken conclusion:** {c['mistake']}
- **Principle from primary:** {c['principle']}
- **Compassionate response (say):** {c['response']}
- **Family action (5–15 min):** {c['action']}
- **What not to say:** {c['avoid']}"""
        for i, c in enumerate(w["cases"], 1)
    )
    analogies = "\n\n".join(
        f"""### Analogy {i}: {a['name']}
- **Say:** {a['say']}
- **Limit:** {a['limit']}
- **Bridge back to verse:** {a['bridge']}"""
        for i, a in enumerate(w["analogies"], 1)
    )
    faqs = "\n\n".join(f"**Q:** {q['q']}\n**A:** {q['a']}" for q in w["faqs"])
    discovery = "\n".join(f"- {x}" for x in w["q_discovery"])
    understanding = "\n".join(f"- {x}" for x in w["q_understanding"])
    application = "\n".join(f"- {x}" for x in w["q_application"])
    misconceptions = "\n".join(f"- {x}" for x in w["misconceptions"])
    boundaries = "\n".join(f"- {x}" for x in w["boundaries"])
    materials = "\n".join(f"- {x}" for x in w["materials"])

    text = f"""# {w['code']} Main Facilitator Guide — Saturday 2:00–4:00

{HEADER}
## Two-minute summary

{w['two_minute']}

**Primary:** {w['reference']} — {w['url']}

## Essential question

{w['essential']}

## Learning outcomes (session)

{w['outcomes']}

## 15-minute night-before prep

1. Open {w['url']} and read Devanāgarī, IAST, and the KUTUMBA teaching meaning aloud once.
2. Rehearse the exact opening script below without improvising new doctrine.
3. Pack younger materials and older materials listed under Materials.
4. Mark the week's primary misconception to block: {w['block']}.
5. Confirm snack and water table (no weekly meal) and parent-onsite seating.
6. Print or open the home-practice card wording for saṅkalpa.

## 60-minute deep prep

1. Read the Core explanation section twice; highlight three sentences you will say slowly.
2. Choose one analogy and one case you will actually use; mark time cues in the margin.
3. Prepare three questions: one discovery, one understanding, one application.
4. Walk the room: welcome zone, verse wall, younger track, older track, reunification circle, snack table.
5. Confirm younger and older teachers have executable guides (not shells) and activity packs.
6. Review deferral language: if a question exceeds week scope, thank the asker, note it, and schedule follow-up with a qualified source rather than inventing an answer.
7. Review safeguarding: no private home struggles disclosed publicly; no ranking; child opt-out roles available.

## Exact primary readings

- **Reference:** {w['reference']}
- **URL:** {w['url']}
- **Devanāgarī:** {w['devanagari']}
- **IAST:** {w['iast']}
- **KUTUMBA teaching meaning:** {w['meaning']}
- **Rights:** Sanskrit from VedaBase display; KUTUMBA teaching meaning is original program pedagogy — not labeled as a BBT English translation; do not paste full purports into slides or handouts.

## Supporting sources (link-level; summarize, do not copy purports)

{w['supporting']}

## One-page speaking map

1. Welcome and memory of prior week (2–3 min)
2. Essential question (1 min)
3. Verse layer — Devanāgarī / IAST / teaching meaning (6–8 min)
4. Core explanation with board triangle or map (8–10 min)
5. One analogy with spoken limit (3 min)
6. One case study (5 min)
7. Age-track handoff (tracks 40 min)
8. Reunification share (8–10 min)
9. Snack/water
10. Home practice saṅkalpa and close

## Exact opening script

{w['opening']}

## Core explanation (teach this; do not outsource to research files)

{w['core']}

## Minute-by-minute facilitator script (plenary portion)

### 2:00–2:10 — Welcome and settling
Greet each family by name if known. Point out restrooms, water, and the snack table timing (snack at 3:30, not a weekly meal). Remind parents they remain onsite. Open with the program’s authorized mantras using the local chanting sheet. Keep volume warm, not theatrical. If a child is dysregulated, offer a quiet helper role immediately rather than competing with the room.

### 2:10–2:18 — Opening script and essential question
Deliver the exact opening script without adding new doctrinal claims. Pause after the essential question. Collect two or three short responses. Do not debate. Write one phrase on the board that you will return to later. State the primary reference and URL verbally so older learners hear that scripture is locatable.

### 2:18–2:28 — Verse layer
Display Devanāgarī. Read slowly. Display IAST. Read slowly. Read the full KUTUMBA teaching meaning without truncation. Ask one child to repeat a memory phrase and one older learner to name the reference. If the primary is a multi-verse or long verse text, do not stop mid-verse. For C3-W4, end aloud on paraṁ vijayate śrī-kṛṣṇa-saṅkīrtanam. For C3-W5, include iti puṁsārpitā … ’dhītam uttamam. For C3-W6, recite the exact chain BG 5.29 · BG 7.7 · BG 4.34 · CC Antya 20.12 · ŚB 7.5.23–24.

### 2:28–2:40 — Core map, analogy, and one case
Teach the board map from the core explanation. Use exactly one analogy and speak its limit in the same breath. Run one case study with compassionate response language. Protect privacy: no family is asked to confess failures publicly. Transition: “Now we practice in age bands; parents stay onsite; we reunite at 3:10.”

### 2:40–3:10 — Tracks (facilitator float)
Float between younger and older rooms/zones. Ensure teachers are using executable guides, not improvising doctrine. Watch for punishment-chanting, ranking, or unsafe secrecy language and interrupt gently. Keep snack prep silent in the background.

### 3:10–3:30 — Reunification and snack
Use the reunification script. Limit shares to one sentence or one picture. Begin snack/water. No lesson competition during snack. Capture home-practice commitments on cards.

### 3:40–4:00 — Saṅkalpa and close
Read the minimum home practice. Invite one adult and one child to restate it. Preview next week in one sentence. Thank volunteers. Reset the room. End at 4:00.

## Facilitator voice examples (say / don’t say)

### Say
- “Śāstra first — let’s open the verse.”
- “That is a sincere question; we will note it and follow up with a qualified source.”
- “Helper roles are real service.”
- “We do not rank families.”

### Don’t say
- “Your family is behind.”
- “Chant until you behave.”
- “Science has now proven this verse.”
- “This material is temple-approved / publication-ready.” (It is EXTERNAL_OPEN for human/temple review.)
- “Mṛgāri story time.” (Out of scope for Cycle 3.)

## Differentiation and newcomers

Newcomer adults: give the two-minute summary and the home-practice card; do not flood with Sanskrit pressure. Newcomer children: pair with a buddy; allow listening-only kīrtana roles. Multilingual homes: English teaching meaning is enough for comprehension; Sanskrit is honored by hearing, not by forced accuracy on night one. If a family arrives late, skim to the verse layer and hand them the card; do not publicly recap someone else’s private share.

## Room stewardship checklist (executable)

1. Verse wall visible from both tracks’ return path.
2. Younger materials bag packed before 1:50.
3. Older worksheets and answer key (private) separated.
4. Water labeled; allergen note if any shared snack.
5. Timer visible for track teachers.
6. Safeguarding adult identified on the run-sheet.
7. Cleanup bags at doors by 3:50.
8. Lost-and-found box for craft pieces.

## Analogies (inline — with limits)

{analogies}

## Case studies (three constructed pedagogical cases)

{cases}

## Facilitator questions

### Discovery
{discovery}

### Understanding
{understanding}

### Application
{application}

## Adult FAQ (likely room questions)

{faqs}

## Common misconceptions to correct gently

{misconceptions}

## Doctrinal and delivery boundaries

{boundaries}

## Track facilitation notes

### Younger track (K–2 / Lāla–Lālī)
- Objective: {w['younger_obj']}
- Memory phrase: {w['memory']}
- Keep movement short; prefer recognition over recitation pressure.
- Handoff to reunification with one picture or gesture share.

### Older track (Kiśora–Kiśorī)
- Objective: {w['older_obj']}
- Require source naming ({w['reference']}) before opinions.
- Use text observation + one case repair; no competitive scoring.

## Reunification script

> Welcome back. We will hear a few short shares — a word, a picture, or one sentence — without ranking families.  
> What did you notice about {w['reunify_focus']}?  
> Our home step is small and steady: {w['home_practice']}.  
> Next week we move to {w['next_week']} without dropping this week's practice.

## Home practice and saṅkalpa

- **Minimum home practice:** {w['home_practice']}
- **Bhakti laboratory cue:** {w['lab']}
- Write the card before closing; invite one adult and one child to restate it.

## Transition to next week

{w['transition']}

## Materials checklist

{materials}

## Do not claim

- Human, temple, legal, or publication approval
- That KUTUMBA teaching meanings are BBT translations
- That science proves ātman, karma, or bhakti siddhānta
- Ranking of families, children, or devotion
- Advanced realization from one night of practice

{SATURDAY}
"""
    return text


def build_younger(w: dict) -> str:
    return f"""# {w['code']} Younger Teacher Guide (Lāla–Lālī)

{HEADER}
## Objective

{w['younger_obj']}

## Exact memory phrase

> {w['memory']}

## Teacher background (enough to teach without improvising)

Primary: {w['reference']} ({w['url']}).

Teaching meaning to keep in mind: {w['meaning']}

Block tonight: {w['block']}.

Parents remain onsite. Session is Saturday 2:00–4:00 with snack/water only (no weekly meal).

## Timed run-of-show (about 40 minutes inside the track window)

| Minutes | Move | Exact teacher language / action |
| --- | --- | --- |
| 0–5 | Arrival + wonder | “Today we learn: {w['memory']}. Can your hands show listening?” |
| 5–15 | Story / picture | Use only authorized paraphrase from SCRIPTURAL-EXAMPLES and the week story boundary. No invented dialogue for the Lord. |
| 15–28 | Movement / hands-on | Run YOUNGER-ACTIVITY-PACK stations in order. Offer opt-out quiet helper role. |
| 28–35 | Recall | Choral memory phrase twice; one child restates with a picture card. |
| 35–40 | Cleanup + handoff | “Tell your family one word: {w['younger_handoff']}.” |

## Step-by-step story boundary

1. Open with one concrete child-scale scene connected to this week’s essential question: {w['essential']}
2. Introduce the Lord or teacher figure only with authorized names and actions.
3. Pause for a wonder question before the craft.
4. Close by tying the craft to the memory phrase — not to fear or competition.

## Wonder questions (ask, then wait)

1. What was new for your ears today?
2. Whom can we serve with care?
3. When can our family practice five quiet minutes?

## Movement / hands-on / craft / coloring (executable)

1. {w['younger_act1']}
2. {w['younger_act2']}
3. {w['younger_act3']}

Use `visuals/V12/line-art-younger.svg` if available for coloring; otherwise plain paper + three labels. If a child refuses craft, they may be card-holder or line leader.

## Inclusive participation menu

- Full participant
- Listener with gesture
- Materials helper
- Door/line helper beside an adult
Never require performance singing or public speaking.

## Behavior redirects (short)

- Feet on floor · kind words · toy rests · quiet reset corner with a picture card.
- Never use chanting, verse, or seating as punishment.
- If a child is overwhelmed, offer helper role (card holder / line leader) with adult nearby.
- If two children conflict, separate gently, name the stewardship/friend rule for this week, and reset materials together.

## Backup if energy crashes (5 minutes)

Circle: whisper memory phrase → stretch → place one sticker on “we tried” chart (no scores). If still flooded, quiet picture walk of three cards only.

## Materials checklist

{chr(10).join('- ' + m for m in w['younger_materials'])}
- Tissues, wipes, spare pencils
- Parent handoff cards pre-written with memory phrase

## Parent handoff line

> Tonight’s phrase is: “{w['memory']}.” Home cue: {w['home_practice']}.
"""


def build_older(w: dict) -> str:
    return f"""# {w['code']} Older Teacher Guide (Kiśora–Kiśorī)

{HEADER}
## Objective

{w['older_obj']}

## Exact memory / thesis line

> {w['memory']}

## Teacher background

Primary: {w['reference']} — {w['url']}

IAST: {w['iast']}

Teaching meaning: {w['meaning']}

Block: {w['block']}

## Timed run-of-show (about 40 minutes)

| Minutes | Move | Instructions |
| --- | --- | --- |
| 0–5 | Hook | Pose essential question: {w['essential']} Collect 2–3 short answers without debate. |
| 5–15 | Text | Display Devanāgarī + IAST. Students mark keywords. Read teaching meaning in full. |
| 15–25 | Case lab | Run one case from the main guide; students write mistaken conclusion → repair. |
| 25–33 | Activity pack | Complete OLDER-ACTIVITY-PACK primary task; use answer key privately. |
| 33–38 | Share | Two volunteers; no ranking; source must be named. |
| 38–40 | Handoff | Restate home practice: {w['home_practice']} |

## Text protocol (do this every week)

1. Student writes the reference.
2. Student underlines 3–6 keywords in IAST or teaching meaning.
3. Student restates the teaching meaning in one fresh sentence.
4. Student names one limit (what this verse is not saying).

## Discussion stems

- “What does the verse actually say — not what we wish it said?”
- “Where is the limit of our analogy?”
- “How would a family apply this without performing for others?”
- “What would ranking look like tonight, and how do we refuse it?”

## Case lab facilitator moves

- Read the situation once.
- Ask for the mistaken conclusion before giving the key.
- Require a compassionate response sentence that a parent could actually say.
- Close with the family action timed at 5–15 minutes.

## Assessment (formative, private)

- Can the student name {w['reference']}?
- Can they restate the teaching meaning in their own words without truncation?
- Can they repair one misconception without sarcasm?
- For C3-W4 specifically: can they end the verse with paraṁ vijayate śrī-kṛṣṇa-saṅkīrtanam?
- For C3-W5 specifically: can they include iti puṁsārpitā / topmost learning?
- For C3-W6 specifically: can they recite BG 5.29 · BG 7.7 · BG 4.34 · CC Antya 20.12 · ŚB 7.5.23–24?

## Safeguarding / tone

Respectful conviction, not aggressive debate. No public scoring of devotion. Parents onsite. If a safety disclosure appears, stop the lesson flow and follow safeguarding protocol.
"""


def build_younger_activity(w: dict) -> str:
    return f"""# {w['code']} Younger Activity Pack

{HEADER}
## Setup (before children arrive)

- Lay stations left-to-right: Picture walk → Hands-on → Recall.
- Place memory phrase card at each station.
- Prepare helper badges (sticker + “helper” word).
- Keep one calm-corner mat with a single picture card.

## Station A — Picture walk (8–10 min)

{w['younger_act1']}

**Teacher script:** “Walk slowly. Point to one picture. Tell me one word you notice.”
**Look-fors:** pointing, one-word share, gentle hands.
**Adaptation:** child may carry the card without speaking.

## Station B — Hands-on (8–10 min)

{w['younger_act2']}

**Teacher script:** “We practice with care. If it feels too much, you may be the materials helper.”
**Look-fors:** attempt + cleanup.
**Adaptation:** hand-over-hand help from parent onsite.

## Station C — Recall game (5–7 min)

{w['younger_act3']}

**Teacher script:** “Whisper our phrase with me: {w['memory']}”
**Look-fors:** choral attempt; smile; no forced solos.

## Materials

{chr(10).join('- ' + m for m in w['younger_materials'])}

## Success look-fors (not scores)

- Child can gesture or say the memory phrase with help.
- Child participates or takes a helper role without pressure.
- Materials returned; room reset before reunification.

## If station fails

Skip to whisper recall + one sticker for effort. Still hand off the memory phrase to parents.
"""


def build_older_activity(w: dict) -> str:
    return f"""# {w['code']} Older Activity Pack

{HEADER}
## Materials

- Printed primary verse card (Devanāgarī + IAST + full teaching meaning)
- Case slip from MAIN facilitator guide
- Pencil, timer, private folder for answer sheets

## Task 1 — Text observation (10 min)

{w['oa_1']}

Deliverable: underlined keywords + one-sentence restatement of the teaching meaning (complete, not truncated).

## Task 2 — Case repair (10 min)

{w['oa_2']}

Deliverable: mistaken conclusion / principle / compassionate response / 5–15 min family action.

## Task 3 — Application card (8–10 min)

{w['oa_3']}

Deliverable: home card with day/time cue.

## Extension (optional)

{w['oa_ext']}

## Collaboration rules

- Pairs okay; no public scoring.
- Source must be named on every share.
- If debate heats up, return to the verse card and timer.
"""


def build_answer_key(w: dict) -> str:
    return f"""# {w['code']} Older Answer Key

{HEADER}
## Task 1 — Expected observations

{w['ak_1']}

## Task 2 — Case repair key

{w['ak_2']}

## Task 3 — Application quality

{w['ak_3']}

## Facilitator note

Use privately. Do not announce scores. Affirm effort and source accuracy.
"""


def build_scriptural(w: dict) -> str:
    items = "\n\n".join(
        f"""### Example {i}: {e['title']}
- **Source:** {e['source']}
- **What happened (summary):** {e['summary']}
- **How it teaches this week's principle:** {e['link']}
- **Classroom use:** {e['use']}
- **Boundary:** {e['boundary']}"""
        for i, e in enumerate(w["scriptural"], 1)
    )
    return f"""# {w['code']} Scriptural Examples

{HEADER}
Primary anchor: {w['reference']} — {w['url']}

{items}
"""


def build_devotional(w: dict) -> str:
    items = "\n\n".join(
        f"""### Example {i}: {e['title']}
- **Historical / devotional context:** {e['context']}
- **Source pointer:** {e['source']}
- **Family takeaway:** {e['takeaway']}
- **Do not invent:** {e['dont']}"""
        for i, e in enumerate(w["devotional"], 1)
    )
    return f"""# {w['code']} Devotional and Historical Examples

{HEADER}
{items}
"""


def build_cases(w: dict) -> str:
    items = "\n\n".join(
        f"""### Case {i}: {c['title']}
- **Situation:** {c['situation']}
- **Mistaken conclusion:** {c['mistake']}
- **Principle:** {c['principle']}
- **Compassionate response:** {c['response']}
- **Family action:** {c['action']}
- **What not to say:** {c['avoid']}"""
        for i, c in enumerate(w["cases"], 1)
    )
    return f"""# {w['code']} Case Studies

{HEADER}
Three constructed pedagogical cases for facilitator use (not private family data).

{items}
"""


def build_analogies(w: dict) -> str:
    items = "\n\n".join(
        f"""### {a['name']}
- **Analogy:** {a['say']}
- **Limit:** {a['limit']}
- **Return to śāstra:** {a['bridge']}"""
        for a in w["analogies"]
    )
    return f"""# {w['code']} Analogies and Limits

{HEADER}
{items}
"""


def build_science(w: dict) -> str:
    return f"""# {w['code']} Science and Application

{HEADER}
## Status

{w['science_status']}

## Careful application notes (habits / pedagogy only)

{w['science_notes']}

## Boundary

Science may illuminate attention, habit formation, or group learning dynamics. It does not prove or disprove siddhānta. Doctrine rests on guru–sādhu–śāstra.
"""


def build_gamma_master(w: dict) -> str:
    slides = []
    for i, s in enumerate(w["gamma_slides"], 1):
        slides.append(
            f"""### Slide {i} — {s['title']}

- **Audience:** master
- **Teaching objective:** {s['objective']}
- **Exact on-screen copy:**
{chr(10).join('  - ' + line for line in s['copy'])}
- **Screen composition:** {s['composition']}
- **Palette role:** plum philosophy / saffron bhakti / teal family
- **Typography:** Title large; body 22–28pt; verse slides may use ~100 readable words
- **Visual type:** {s['visual_type']}
- **Detailed AI image prompt:** {s['image']}
- **Diagram instructions:** {s['diagram']}
- **Source:** {s['source']}
- **Presenter notes:** {s['notes']}
- **Interaction:** {s['interaction']}
- **Do-not-claim:** Not human-approved; not publication-ready; Gamma not rendered; science ≠ siddhānta; teaching meaning ≠ BBT translation
- **Accessibility:** Large type; high contrast; read Devanāgarī/IAST aloud; alt-text for images
"""
        )
    return f"""# {w['code']} V12 Gamma Master Deck

**Status:** prompt-only — not rendered — not approved

## Deck purpose

{w['gamma_purpose']}

## Slides

{chr(10).join(slides)}
"""


def build_gamma_audience(w: dict, audience: str) -> str:
    focus = w["gamma_younger"] if audience == "younger" else w["gamma_older"]
    meaning = w["meaning"]
    return f"""# {w['code']} V12 Gamma {audience.title()} Deck

**Status:** prompt-only — not rendered — not approved

## Audience focus

{focus}

## Required content fidelity

- Full teaching meaning (never truncated mid-phrase): {meaning}
- Primary: {w['reference']} — {w['url']}
- Devanāgarī: {w['devanagari']}
- IAST: {w['iast']}
- Memory: {w['memory']}
- Block: {w['block']}
- Home practice: {w['home_practice']}

## Slide spine (adapt master slides)

1. Title with week name and Saturday 2:00–4:00
2. Essential question: {w['essential']}
3. Primary verse with complete Devanāgarī + IAST + full teaching meaning (no mid-phrase cut)
4. One analogy with spoken limit on-screen
5. One age-fit practice slide drawn from activity pack
6. Home practice card
7. Closing gratitude without ranking

## Exact on-screen teaching meaning (copy whole)

{meaning}

## Image prompts (specific)

{w['gamma_image_extra']}

## Presenter notes spine

- Parents onsite; snack/water only; no weekly meal.
- Do not claim human/temple/publication approval.
- Teaching meaning is KUTUMBA pedagogy, not a BBT translation label.
- Refuse ranking and punishment-chanting.
- Cycle 3 excludes Mṛgāri narratives.

## Sources

Cite {w['reference']} ({w['url']}) and listed supporting sources by reference + URL. Do not write vague policy placeholders.
"""


def main() -> None:
    dirs = week_dirs()
    report = []
    for code, w in WEEKS.items():
        root = dirs[code]
        files = {
            root / "teacher" / "MAIN-FACILITATOR-GUIDE-V12.md": build_main(w),
            root / "teacher" / "YOUNGER-TEACHER-GUIDE.md": build_younger(w),
            root / "teacher" / "OLDER-TEACHER-GUIDE.md": build_older(w),
            root / "activities" / "YOUNGER-ACTIVITY-PACK.md": build_younger_activity(w),
            root / "activities" / "OLDER-ACTIVITY-PACK.md": build_older_activity(w),
            root / "activities" / "OLDER-ANSWER-KEY.md": build_answer_key(w),
            root / "research" / "SCRIPTURAL-EXAMPLES.md": build_scriptural(w),
            root / "research" / "DEVOTIONAL-AND-HISTORICAL-EXAMPLES.md": build_devotional(w),
            root / "research" / "CASE-STUDIES.md": build_cases(w),
            root / "research" / "ANALOGIES-AND-LIMITS.md": build_analogies(w),
            root / "research" / "SCIENCE-AND-APPLICATION.md": build_science(w),
            root / "gamma" / "V12-GAMMA-MASTER-DECK-PROMPT.md": build_gamma_master(w),
            root / "gamma" / "V12-GAMMA-YOUNGER-DECK-PROMPT.md": build_gamma_audience(w, "younger"),
            root / "gamma" / "V12-GAMMA-OLDER-DECK-PROMPT.md": build_gamma_audience(w, "older"),
        }
        for path, text in files.items():
            write(path, text)
        main_words = len(files[root / "teacher" / "MAIN-FACILITATOR-GUIDE-V12.md"].split())
        report.append(f"{code}: MAIN {main_words} words; wrote {len(files)} files → {root.name}")

        # Integrity checks
        blob = "\n".join(files.values())
        if code == "C3-W4" and "paraṁ vijayate" not in blob:
            raise SystemExit("C3-W4 missing paraṁ vijayate")
        if code == "C3-W5" and "iti puṁsārpitā" not in blob:
            raise SystemExit("C3-W5 missing iti puṁsārpitā")
        if code == "C3-W6":
            if w.get("iast") != "BG 5.29 · BG 7.7 · BG 4.34 · CC Antya 20.12 · ŚB 7.5.23–24":
                raise SystemExit(f"C3-W6 primary IAST chain incorrect: {w.get('iast')!r}")
            if "CC Antya 20.12" not in w.get("opening", ""):
                raise SystemExit("C3-W6 opening missing CC Antya 20.12")

    safe = []
    for line in report:
        safe.append(line.encode("ascii", "replace").decode("ascii"))
    print("\n".join(safe))


if __name__ == "__main__":
    main()

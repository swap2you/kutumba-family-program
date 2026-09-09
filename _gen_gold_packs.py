# -*- coding: utf-8 -*-
"""Generate gold-standard Saturday teaching packs for shallow weeks."""
from __future__ import annotations

import os
from pathlib import Path

BASE = Path("11-weekly-program-library/first-six-months")

COMMON_HEADER = """**KUTUMBA • Families Growing in Krishna Consciousness**
**Program Director: Swapnil Patil**
**Status:** Internal founding-cohort teaching material — human/temple review EXTERNAL_OPEN"""

TIME_CUES = """| Time | Block |
|---|---|
| 1:50–2:00 | Arrival; parents onsite; materials check |
| 2:00–2:10 | Opening mantras |
| 2:10–2:30 | Shared opening / Prem-kī-Kathā / verse layer |
| 2:30–3:10 | Parallel tracks (parent / younger / older) |
| 3:10–3:30 | Reunification / bhakti laboratory |
| 3:30–3:40 | Snack + water only (no weekly meal) |
| 3:40–3:55 | Saṅkalpa / project / questions |
| 3:55–4:00 | Closing; next-week title only |"""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.replace("\r\n", "\n").strip() + "\n", encoding="utf-8")


def render_main(w: dict) -> str:
    supporting_rows = "\n".join(
        f"| {r['ref']} | {r['url']} | {r['paraphrase']} | {r['limit']} |"
        for r in w["supporting"]
    )
    analogies = []
    for i, a in enumerate(w["analogies"], 1):
        analogies.append(
            f"""### {i}) {a['title']}
- **Say:** {a['say']}
- **Limit:** {a['limit']}
- **Younger:** {a['younger']}
- **Older/adult:** {a['older']}"""
        )
    scriptural = []
    for i, s in enumerate(w["scriptural_examples"], 1):
        letter = chr(64 + i)
        scriptural.append(
            f"""### Example {letter} — {s['title']}
{s['body']}
**Teaching use:** {s['use']}
**Limitation:** {s['limitation']}"""
        )
    cases = []
    for i, c in enumerate(w["cases"], 1):
        cases.append(
            f"""### Constructed case {i} — {c['title']}
- **Situation:** {c['situation']}
- **Tempting mistaken conclusion:** {c['mistaken']}
- **Relevant principle / source:** {c['principle']}
- **Compassionate response:** {c['response']}
- **Family action:** {c['action']}
- **What not to say:** {c['not_say']}
- **Age adaptation:** {c['age']}"""
        )
    qa_rows = "\n".join(f"| {q['q']} | {q['a']} |" for q in w["qa"])
    disc = "\n".join(f"{i}. {q}" for i, q in enumerate(w["discovery"], 1))
    und = "\n".join(f"{i}. {q}" for i, q in enumerate(w["understanding"], 1))
    app = "\n".join(f"{i}. {q}" for i, q in enumerate(w["application"], 1))
    misc = "\n".join(f"- {m}" for m in w["misconceptions"])
    nospec = "\n".join(f"- {m}" for m in w["no_speculate"])
    noclaim = "\n".join(f"- {m}" for m in w["do_not_claim"])
    materials = "\n".join(f"- {m}" for m in w["materials"])
    parent_notes = "\n".join(f"{i}. {n}" for i, n in enumerate(w["parent_notes"], 1))
    self_check = "\n".join(f"- {s}" for s in w["self_check"])

    primary_extra = w.get("primary_extra", "")
    if w.get("is_review"):
        primary_block = f"""## Exact primary readings (Cycle review — no new doctrine)

{w['review_primary_block']}
- **Rights:** Review of prior week Sanskrit layers; KUTUMBA synthesis original; no full purport dumps; teaching meanings ≠ BBT translation labels.
{primary_extra}"""
    else:
        primary_block = f"""## Exact primary readings

- **Primary:** {w['primary_label']} — {w['primary_url']}
- **Devanāgarī:** {w['devanagari']}
- **IAST:** {w['iast']}
- **KUTUMBA teaching meaning:** {w['teaching_meaning']}
- **Rights:** Sanskrit verse text from VedaBase display; KUTUMBA teaching meaning original; no full purport dump; teaching meaning ≠ BBT translation label.
{primary_extra}"""

    return f"""# {w['code']} Main Facilitator Guide — Saturday 2:00–4:00

{COMMON_HEADER}
**Week:** {w['title']}
**Primary scripture:** {w['primary_label']} — {w['primary_url']}

---

## Two-minute summary

{w['two_minute']}

## Essential question

{w['essential']}

## Memory line

{w['memory_line']}

## Exact memory phrase (children echo)

{w['memory_phrase']}

## KUTUMBA teaching meaning (primary)

**KUTUMBA teaching meaning:** {w['teaching_meaning']}

Label this as **KUTUMBA teaching meaning**. Do not label it as a BBT translation. Sanskrit verse text is from VedaBase display for classroom reading; do not paste full purports into slides or handouts.

---

## 15-minute night-before prep

{chr(10).join(f"{i}. {p}" for i, p in enumerate(w['prep15'], 1))}

## 60-minute deep prep

{chr(10).join(f"{i}. {p}" for i, p in enumerate(w['prep60'], 1))}

---

{primary_block}

## Exact supporting readings (classroom paraphrase only)

| Reference | URL | Teaching paraphrase (facilitator may say) | Limitation |
|---|---|---|---|
{supporting_rows}

---

## One-page speaking map

1. Welcome + Saturday purpose (2:10)
2. Memory line + essential question
3. Primary verse layer (Devanāgarī / IAST / KUTUMBA teaching meaning)
4. Core explanation
5. One analogy with limit
6. Scriptural examples (paraphrase only)
7. One constructed household case
8. Track split (2:30)
9. Reunification synthesis (3:10)
10. Snack/water (3:30) — no weekly meal
11. Saṅkalpa / project / home practice (3:40)
12. Next-week title only + close (3:55–4:00)

---

## Exact opening script (≈3 minutes)

{w['opening_script']}

## Extended 10–20 minute speaking SCRIPT (shared opening / parent circle)

Use this as the facilitator spine between 2:10 and 2:28. Adjust pace; do not invent quotations.

{w['speaking_script']}

---

## Core explanation (facilitator must say)

{w['core_explanation']}

**Conclusion line:** {w['conclusion']}

**Common errors to block:**
{chr(10).join(f"{i}. {e}" for i, e in enumerate(w['errors'], 1))}

---

## Analogies / examples with limits (teach inline)

{chr(10).join(analogies)}

---

## Scriptural examples (paraphrase only; no invented dialogue)

{chr(10).join(scriptural)}

---

## Historical / devotional examples (traceable, paraphrase)

{w['devotional']}

---

## Three constructed household cases (week-specific)

{chr(10).join(cases)}

---

## Discovery questions

{disc}

## Understanding questions

{und}

## Application questions

{app}

---

## Likely adult questions + source-based answers

| Question | Direction |
|---|---|
{qa_rows}

---

## Common misconceptions

{misc}

## What not to speculate about

{nospec}

## Do not claim

{noclaim}

---

## Saturday time cues

{TIME_CUES}

## Track transition (say at 2:28)

> Parents remain in the parent circle. Younger friends go with [younger teacher]. Older students go with [older teacher]. We reunite at 3:10 for {w['lab_name']} together. Parents stay onsite.

## Family reunification synthesis (3:10)

{w['reunification']}

## Bhakti laboratory — {w['lab_name']}

{w['lab_steps']}

## Project contribution

See `project/CYCLE-CONTRIBUTION.md`. Artifact: {w['project']}. Optional burden ≤20 minutes. No ranking.

## Home practice

| Level | Practice |
|---|---|
| **Minimum** | {w['home_min']} |
| **Standard** | {w['home_std']} |
| **Stretch** | {w['home_stretch']} |
| **Evidence** | Private reflection only: {w['home_evidence']} |

## Next-week preview

{w['next_week']}

---

## Parent-track facilitation notes (2:30–3:10)

{parent_notes}

## Younger-track pointer

Execute `teacher/YOUNGER-TEACHER-GUIDE.md` with `activities/YOUNGER-ACTIVITY-PACK.md` — {w['younger_pointer']}. Memory phrase: **{w['memory_phrase']}**

## Older-track pointer

Execute `teacher/OLDER-TEACHER-GUIDE.md` with `activities/OLDER-ACTIVITY-PACK.md` and `OLDER-ANSWER-KEY.md` — {w['older_pointer']}.

## Materials checklist

{materials}

## Closing script (3:55)

{w['closing']}

---

## Facilitator self-check (night after)

{self_check}
"""


def render_younger(w: dict) -> str:
    y = w["younger"]
    return f"""# {w['code']} Younger Teacher Guide (K–2)

**Week:** {w['title']}
**Primary:** {w['primary_label']} — {w['primary_url']}
**Session length:** 40 minutes (parallel track ~2:30–3:10)
**Parents:** Remain onsite; reunite at 3:10
**Status:** Internal founding-cohort teaching material — human/temple review EXTERNAL_OPEN

---

## Objective

{y['objective']}

## Exact memory phrase

> {w['memory_phrase']}

## Teacher background (2 minutes to review)

- **KUTUMBA teaching meaning (adult wording):** {w['teaching_meaning']}
- **Child-facing paraphrase:** {y['child_paraphrase']}
- **Block misconceptions (child words):**
{chr(10).join(f"  - “{m}”" for m in y['block'])}
- **Do not:** invent deity dialogue; force confession; rank children; use scare tactics; claim temple certification stickers.

## Materials

{chr(10).join(f"- {m}" for m in y['materials'])}

## Room setup

Circle on the floor; materials table behind you; calm corner with one chair for quiet reset. Keep aisles clear for movement.

---

## Minute-by-minute executable plan

### 0–5 min — Opening and recall

{y['open']}

### 5–13 min — Story script (paraphrase only; ~8 minutes)

**Say exactly this spine (do not invent deity dialogue):**

{y['story']}

**Story boundaries:** {y['story_boundaries']}

### 13–16 min — Three wonder questions

{chr(10).join(f"{i}. {q}" for i, q in enumerate(y['wonder'], 1))}

Accept one- or two-word answers. Affirm effort.

### 16–24 min — Movement game: {y['movement_name']} (steps)

{y['movement']}

### 24–32 min — Craft: {y['craft_name']} (steps)

{y['craft']}

Full printable steps also live in `activities/YOUNGER-ACTIVITY-PACK.md` (use together; this guide remains executable if the pack is missing).

### 32–35 min — Printable / coloring task

If time remains, color the younger line-art sheet if available. If short on time, keep the craft as the take-home.

### 35–38 min — Behavior redirects and quiet reset

Use calm, specific redirects:
{chr(10).join(f"- **{k}** — “{v}”" for k, v in y['redirects'].items())}

### 38–40 min — Cleanup and parent handoff

1. Materials away; craft in hand.
2. At reunification, tell parent in one sentence:
   > Memory phrase: “{w['memory_phrase']}.” Home cue: {w['home_min']}
3. Do not report private behavior struggles in front of other families.

---

## Behavior redirects (quick reference)

| Signal | Teacher line | Child action |
|---|---|---|
{chr(10).join(f"| {r['signal']} | {r['line']} | {r['action']} |" for r in y['redirect_table'])}

## Backup low-prep (if craft fails or energy crashes)

{y['backup']}

## What success looks like

{chr(10).join(f"- {s}" for s in y['success'])}

## Boundaries

- Snack/water only happens in main schedule (3:30), not as a track bribe.
- No weekly meal language.
- No fabricated approval stickers implying temple certification.
- Privacy: no forced confession.
"""


def render_older(w: dict) -> str:
    o = w["older"]
    return f"""# {w['code']} Older Teacher Guide (Grades 4–5)

**Week:** {w['title']}
**Primary:** {w['primary_label']} — {w['primary_url']}
**Session length:** ~40 minutes (parallel track ~2:30–3:10)
**Parents:** Remain onsite; reunite at 3:10
**Status:** Internal founding-cohort teaching material — human/temple review EXTERNAL_OPEN

---

## Objective

{o['objective']}

## Exact memory phrase

> {w['memory_line']}

**Short echo:** {w['memory_phrase']}

## Teacher background

- **KUTUMBA teaching meaning:** {w['teaching_meaning']} (Label as KUTUMBA teaching meaning — not as BBT translation.)
- **Supporting frames (one sentence each):** {o['supports']}
- **Block:** {'; '.join(w['errors'])}
- **Scope:** {o['scope']}

## Materials

{chr(10).join(f"- {m}" for m in o['materials'])}

---

## Minute-by-minute plan

### 0–5 min — Settle and hook

{o['hook']}

### 5–14 min — Primary text observation

{o['text_obs']}

### 14–22 min — Worksheet questions

Students complete Section A of the older activity pack. Teacher circulates; use `OLDER-ANSWER-KEY.md` for expected directions (not for grading ranks).

### 22–28 min — Scenario cards (small groups)

{o['scenarios']}

Share one insight per group (60 seconds).

### 28–33 min — Puzzle / game: {o['game_name']}

{o['game']}

### 33–37 min — Diagram / map task

{o['diagram']}

### 37–40 min — Project sentence + handoff

{o['project_close']}

---

## Boundaries

- No ranking or public scores.
- No invented dialogue.
- Parents onsite; snack/water only at 3:30 in the main schedule.
- Defer off-scope topics: {o['defer']}
"""


def render_younger_pack(w: dict) -> str:
    y = w["younger"]
    return f"""# {w['code']} Younger Activity Pack (K–2)

**Theme:** {w['title']}
**Primary:** {w['primary_label']} — {w['primary_url']}
**Memory phrase:** {w['memory_phrase']}

---

## Objective

{y['objective']}

## Core activity — {y['movement_name']}

**Time:** 5–8 minutes

{y['movement']}

## Story boundary

{y['story_boundaries']}

## Craft — {y['craft_name']} (step-by-step)

{y['craft']}

## Printable

Color `../visuals/V12/line-art-younger.svg` on US Letter if present. If missing, children color their craft only.

## Backup (low prep)

{y['backup']}

## Materials

{chr(10).join(f"- {m}" for m in y['materials'])}

## Parent note (say at handoff)

Home practice: {w['home_min']}. Snack/water only at the Saturday program; no weekly meal. We do not rank children.
"""


def render_older_pack(w: dict) -> str:
    o = w["older"]
    return f"""# {w['code']} Older Activity Pack (Grades 4–5)

**Theme:** {w['title']}
**Primary:** {w['primary_label']} — {w['primary_url']}
**Essential question:** {w['essential']}

---

## Materials for each student

- This worksheet (printed)
- Pencil
- Diagram sheet (Section C)
- One scenario card (assigned)
- Project half-sheet (Section E)

Teachers: expected directions are in `OLDER-ANSWER-KEY.md` (teacher only).

---

## Section A — Text observation

**IAST:** {w['iast'] if not w.get('is_review') else w.get('review_iast_line', '(see review chain)')}

**KUTUMBA teaching meaning:** {w['teaching_meaning']}

*(Labeled KUTUMBA teaching meaning — not labeled as BBT translation.)*

**Source:** {w['primary_url']}

{o['worksheet_a']}

## Section B — Scenario card response

{o['worksheet_b']}

## Section C — Diagram / map

{o['worksheet_c']}

## Section D — Class game notes

{o['worksheet_d']}

## Section E — Project contribution

{o['worksheet_e']}

## Section F — Reflection

{o['worksheet_f']}

## Home practice reminder

{w['home_min']}. Parents stay part of the Saturday 2:00–4:00 rhythm; snack/water only at program (no weekly meal).
"""


def render_answer_key(w: dict) -> str:
    o = w["older"]
    return f"""# {w['code']} Older Answer Key (Teacher Only)

**Week:** {w['title']}
**Primary:** {w['primary_label']} — {w['primary_url']}
**Do not distribute to students during first attempt. Not a ranking tool.**

---

## Section A — expected directions

{o['answer_a']}

## Section B — scenario directions

{o['answer_b']}

## Section C — diagram

Accept any coherent low-risk example aligned to this week’s principle. If a student writes a high-risk private disclosure, thank them privately and help reframe; do not broadcast.

## Section D — game

{o['answer_d']}

## Section E–F

Any sincere family application. Reflection should name the week’s blocked misconceptions.

## Scoring note

Use for facilitation only. No public scores. No family ranking.
"""


def render_scriptural(w: dict) -> str:
    rows = "\n".join(
        f"| {r['ref']} | {r['url']} | {r['paraphrase']} | Classroom use | {r['limit']} |"
        for r in w["supporting"]
    )
    return f"""# {w['code']} Scriptural Examples

**Week:** {w['title']}
**Controlling primary:** {w['primary_label']}

## Primary anchor

| Reference | URL | Teaching paraphrase | Limitation |
|---|---|---|---|
| {w['primary_label']} | {w['primary_url']} | {w['teaching_meaning']} (KUTUMBA teaching meaning). | Do not label KUTUMBA teaching meaning as BBT translation; no full purport dump in class materials. |

## Supporting anchors

| Reference | URL | Teaching paraphrase | Classroom use | Limitation |
|---|---|---|---|---|
{rows}

## Classroom sequence

Open {w['primary_url']} → state KUTUMBA teaching meaning in full → add supporting paraphrases only as needed → keep next week’s ontology out of tonight’s conclusion.
"""


def render_analogies(w: dict) -> str:
    rows = "\n".join(
        f"| {a['title']} | Teaching value | Pedagogy | {a['limit']} | {a['younger']} | {a['older']} |"
        for a in w["analogies"]
    )
    return f"""# {w['code']} Analogies and Limits

**Week:** {w['title']}
**Rule:** Label every analogy as pedagogy. Never present an analogy as a śāstra quotation.

| Analogy | Teaching value | Source status | Failure point / limit | Younger use | Older/adult use |
|---|---|---|---|---|---|
{rows}

## Spoken limit line (facilitator)

> This picture helps us learn. It is not itself the verse. The verse is {w['primary_label']}.
"""


def render_cases(w: dict) -> str:
    blocks = []
    for i, c in enumerate(w["cases"], 1):
        blocks.append(
            f"""### Constructed case {i} — {c['title']} (fictional)

- **Situation:** {c['situation']}
- **Tempting mistaken conclusion:** {c['mistaken']}
- **Relevant principle / source:** {c['principle']}
- **Compassionate response:** {c['response']}
- **Family action:** {c['action']}
- **What not to say:** {c['not_say']}
- **Age adaptation:** {c['age']}"""
        )
    return f"""# {w['code']} Case Studies

**Week:** {w['title']}
**Primary principle source:** {w['primary_label']} — {w['primary_url']}
**Note:** All cases are fictional / anonymized teaching constructs for the founding cohort. Not reports about real cohort families.

---

{chr(10).join(blocks)}
"""


def render_devotional(w: dict) -> str:
    return f"""# {w['code']} Devotional and Historical Examples

**Week:** {w['title']}
**Primary:** {w['primary_label']} — {w['primary_url']}

{w['devotional_research']}
"""


def render_science(w: dict) -> str:
    return f"""# {w['code']} Science and Application

**Week:** {w['title']}
**Primary doctrinal anchor:** {w['primary_label']} — {w['primary_url']}

## Option B — explicit N/A

**N/A — no empirical claim is needed for this week's doctrinal conclusion**

### Reason

{w['science_reason']}

### Allowed pedagogical borrowing (non-proof)

{w['science_borrow']}

### Facilitator line if asked

> {w['science_line']}
"""


# ---------------------------------------------------------------------------
# WEEK DATA
# ---------------------------------------------------------------------------

WEEKS: list[dict] = []


def add(w: dict) -> None:
    WEEKS.append(w)


# ========================= C2-W5 =========================
add({
    "code": "C2-W5",
    "dir": "c2-w5-māyā-decorating-the-prison-cell",
    "title": "Māyā: Decorating the Prison Cell",
    "primary_label": "BG 7.14",
    "primary_url": "https://vedabase.io/en/library/bg/7/14/",
    "devanagari": "दैवी ह्येषा गुणमयी मम माया दुरत्यया । मामेव ये प्रपद्यन्ते मायामेतां तरन्ति ते ॥ १४ ॥",
    "iast": "daivī hy eṣā guṇa-mayī mama māyā duratyayā / mām eva ye prapadyante māyām etāṁ taranti te",
    "teaching_meaning": "This divine illusory energy of the Lord, made of the modes, is difficult to overcome — but those who surrender unto Him cross beyond it.",
    "essential": "Where are we decorating bondage?",
    "memory_line": "Kṛṣṇa’s material energy is difficult to overcome, but those who surrender to Him can cross beyond it.",
    "memory_phrase": "Surrender crosses māyā.",
    "two_minute": "Māyā is the Lord’s divine material energy composed of the three modes. It is hard to overcome by unaided struggle. Primary verse **BG 7.14** teaches that those who surrender to Kṛṣṇa cross beyond it. The week’s image — decorating the prison cell — names the habit of polishing comfort, image, and consumption while remaining bound. Lab: **Attention Boundary and Japa Shelter**. Home practice: one media or consumption boundary for three days. Block both “hate the world / hate women” distortions and the opposite: “willpower alone defeats māyā.”",
    "lab_name": "Attention Boundary and Japa Shelter",
    "is_review": False,
    "prep15": [
        "Open https://vedabase.io/en/library/bg/7/14/ and reread Devanāgarī, IAST, and the KUTUMBA teaching meaning above.",
        "Skim supporting anchors: BG 2.62–63, BG 9.10, BG 15.7 (paraphrase only; no invented dialogue).",
        "Rehearse the opening script aloud once (about three minutes).",
        "Pack younger and older track materials: shiny-choice cards, decorated-cage craft, attention-chain cards, crayons, soft toss object.",
        "Review misconceptions to block: (A) hate all material duty / “women are māyā”; (B) willpower alone conquers māyā without surrender.",
        "Confirm room plan: parents onsite; snack and water only; **no weekly meal**.",
        "Write the home-practice minimum on an index card: *One media or consumption boundary for three days + one japa/shelter cue.*",
    ],
    "prep60": [
        "Read this guide’s analogies, scriptural examples, and three constructed cases so you can teach them **inline** without sending people to research mid-session.",
        "Open each supporting URL once and note one teaching use and one limitation.",
        "Mark three questions you will actually ask: one discovery, one understanding, one application.",
        "Prepare one analogy with its spoken limit (recommend: decorated prison cell).",
        "Walk the room: parent circle, younger zone, older zone, reunification seating, snack table.",
        "Rehearse track transition language and the 3:10 reunification synthesis prompt.",
        "Review privacy: no forced confession of screen habits; no ranking families; no public exposure of private struggles.",
        "Review deferral line: Cycle 3 identity of God begins next cycle after C2-W6 — do not overload tonight.",
        "Confirm project contribution card: one family artifact answering the essential question; ≤20 minutes optional burden.",
        "Confirm next-week title only: C2-W6 Integration Night — Choice, Consequence and the Modes — do not teach five-lens method early.",
    ],
    "supporting": [
        {"ref": "BG 2.62", "url": "https://vedabase.io/en/library/bg/2/62/", "paraphrase": "Contemplating sense objects develops attachment; from attachment desire is born; from desire anger arises — attention can start a binding chain.", "limit": "Do not shame children for noticing shiny things; teach pause and shelter."},
        {"ref": "BG 2.63", "url": "https://vedabase.io/en/library/bg/2/63/", "paraphrase": "From anger comes delusion; from delusion memory bewilderment; from that, intelligence loss; then one falls — a classroom map for attention-to-judgment collapse.", "limit": "Keep examples low-risk; no graphic anger stories."},
        {"ref": "BG 9.10", "url": "https://vedabase.io/en/library/bg/9/10/", "paraphrase": "Under the Lord’s supervision, material nature produces the moving and nonmoving — māyā is not an independent rival god.", "limit": "Do not flatten into fatalism that excuses responsible boundaries."},
        {"ref": "BG 15.7", "url": "https://vedabase.io/en/library/bg/15/7/", "paraphrase": "The living entities are eternal fragmental parts of the Lord; struggling with the senses, they are conditioned — binding energy covers original position.", "limit": "Do not teach full soul ontology beyond what prior weeks already set."},
        {"ref": "BG 7.13", "url": "https://vedabase.io/en/library/bg/7/13/", "paraphrase": "Deluded by the three modes, the whole world does not know the Lord who is above the modes — modes explain cover, not the way out alone.", "limit": "Pair with 7.14 surrender language."},
        {"ref": "BG 7.15", "url": "https://vedabase.io/en/library/bg/7/15/", "paraphrase": "Those of demoniac nature, whose knowledge is stolen by māyā, do not surrender — shows the seriousness of cover without diagnosing anyone in the room.", "limit": "Never label a child or parent as demoniac."},
    ],
    "opening_script": """> Welcome. Today is C2-W5: Māyā — Decorating the Prison Cell.
> Our essential question is: Where are we decorating bondage?
> From Bhagavad-gītā 7.14, our KUTUMBA teaching meaning is: This divine illusory energy of the Lord, made of the modes, is difficult to overcome — but those who surrender unto Him cross beyond it.
> Last week we named the modes. This week we name the energy that uses the modes to cover and misdirect. Comfort, image, and endless polishing can decorate a cell that is still a cell.
> We will hear together, practice Attention Boundary and Japa Shelter in age bands, reunite, and take one small home boundary.
> We do not rank families or children. Parents remain onsite. Snack and water only — no weekly meal. Private struggles stay private.""",
    "speaking_script": """**[0–2 min — Hook]**
A phone lights up during Gītā reading. “Ten seconds,” the mind says. Twenty minutes later, the verse is fog. Nothing forced the hand with ropes — yet the sequence felt automatic. That is tonight’s doorway into māyā as cover and misdirection, not as a person to hate.

**[2–5 min — Verse layer]**
Display or read BG 7.14 Devanāgarī and IAST briefly. State the KUTUMBA teaching meaning in full. Emphasize: divine energy; composed of modes; hard to overcome; surrender crosses.

**[5–8 min — Supporting frame without overload]**
Name BG 2.62–63 in one sentence as an attention-to-delusion chain. Name BG 9.10 in one sentence: nature works under the Lord’s supervision — māyā is not a second absolute. Return to 7.14 so the room does not slide into either despair or blame.

**[8–12 min — Scriptural arc]**
Paraphrase only: BG 7.13 notes mode-delusion covering knowledge of the Lord above the modes; BG 7.14 gives the crossing method — surrender to Him. Do not invent dialogue. Do not diagnose anyone’s spiritual status from 7.15.

**[12–16 min — Analogy + limit]**
Use the decorated prison-cell analogy. State the limit out loud: analogy is pedagogy from the tradition’s teaching image, not a śāstra verse quotation itself.

**[16–18 min — Case]**
Read Constructed Case 1 (notification spiral) once. Ask: What was the false promise? What surrender-shaped boundary could help?

**[18–20 min — Lab preview + transition]**
Introduce Attention Boundary and Japa Shelter: name one false promise; set one boundary; pair it with a shelter (japa, verse card, devotee check-in). At 2:28 give the track transition.""",
    "core_explanation": "Māyā is Kṛṣṇa’s divine material energy. Made of the three modes, it covers and misdirects the conditioned soul so that bondage can look attractive — like decorating a prison cell. BG 7.14 teaches that this energy is hard to overcome by unaided struggle, yet those who surrender to the Lord cross beyond it. We do not hate the world, women, or necessary household duty. We also do not pretend raw willpower alone defeats māyā. Vigilance pairs with surrender, association, and shelter.",
    "conclusion": "Māyā is hard to cross — surrender to Kṛṣṇa is the way through.",
    "errors": [
        "Hate all material duty / “women are māyā.”",
        "Willpower alone conquers māyā without surrender and shelter.",
    ],
    "analogies": [
        {
            "title": "Decorating the prison cell",
            "say": "A prisoner may polish the walls, hang pictures, and rearrange furniture. The cell can look nicer while remaining a cell. Families can improve comfort, image, and consumption while remaining bound by forgetfulness of Kṛṣṇa. The upgrade is not evil; making the upgrade the ultimate project is the trap.",
            "limit": "Pedagogy from the tradition’s teaching image — not a verse quotation. Do not call someone’s home “a prison” as insult. Do not shame beauty, order, or responsible householder care.",
            "younger": "Pretty cage still has a door we need Kṛṣṇa’s help to open.",
            "older": "Name one upgrade that helps service vs one upgrade that only feeds image.",
        },
        {
            "title": "Shiny lure / sticky path",
            "say": "A shiny object pulls the eyes. Each repeated look can lay a sticky note on the path until leaving becomes hard. Māyā often works by attraction that feels natural, then by habit that feels inevitable.",
            "limit": "Not a scientific proof of ontology. Do not pathologize ordinary curiosity in children.",
            "younger": "Shiny toy vs helping hands — stop, breathe, choose help.",
            "older": "Map one attention chain: notice → want → click → fog.",
        },
        {
            "title": "Rope of the modes",
            "say": "Guṇa can also mean rope. Soft ropes of goodness, passion, and ignorance can bind without looking like iron chains. Crossing requires more than thrashing — it requires the Lord’s shelter.",
            "limit": "Do not turn mode language into permanent labels for people. Pair with BG 7.14 surrender.",
            "younger": "Soft rope game: ask a friend for help to free hands.",
            "older": "Which soft rope (comfort, rush, fog) shows up most at home?",
        },
    ],
    "scriptural_examples": [
        {
            "title": "Crossing by surrender (BG 7.14)",
            "body": "The Lord describes His divine illusory energy composed of the modes as difficult to overcome, and states that those who surrender unto Him cross beyond it.",
            "use": "Centers the week: difficulty is real; method is surrender, not hatred or solo force.",
            "limitation": "Paraphrase teaching meaning; no full purport dump; no invented quotes.",
        },
        {
            "title": "Attention-to-delusion chain (BG 2.62–63)",
            "body": "Contemplation of sense objects can generate attachment, desire, and anger; anger can lead to delusion, memory loss, intelligence failure, and falldown.",
            "use": "Gives a practical map for media and consumption spirals without claiming science proves the verse.",
            "limitation": "Use low-risk examples; do not force confession of private habits.",
        },
        {
            "title": "Nature under the Lord’s supervision (BG 9.10)",
            "body": "Material nature produces the moving and nonmoving under the Lord’s direction.",
            "use": "Prevents treating māyā as an independent rival absolute.",
            "limitation": "Do not collapse into “nothing I do matters.”",
        },
    ],
    "devotional": """**Decorating-the-prison-cell teaching image (classroom paraphrase of a recurring Prabhupāda pedagogical theme):** Improving material arrangements while remaining bound in forgetfulness of Kṛṣṇa is compared to decorating a prison cell — the cell may look better, yet release still requires the Lord’s mercy and surrender.
**Use:** Names the week’s essential question without condemning responsible household care.
**Limitation:** Treat as pedagogy, not as a pasted purport; point learners to https://vedabase.io/en/library/bg/7/14/ for personal study; invent no lecture anecdotes.

If a second strand is needed, keep it research-honest: the Gītā arc BG 7.13 → 7.14 is sufficient. Do not invent saint dialogues about phones.""",
    "devotional_research": """## Traceable example 1 — BG 7.14 surrender crossing

- **Source:** https://vedabase.io/en/library/bg/7/14/
- **Paraphrase:** The Lord’s divine material energy of the modes is difficult to overcome; those who surrender unto Him cross beyond it.
- **Teaching use:** Primary siddhānta for the week.
- **Limitation:** No full purport paste; KUTUMBA teaching meaning is labeled as such.

## Traceable example 2 — Attention chain BG 2.62–63

- **Sources:** https://vedabase.io/en/library/bg/2/62/ · https://vedabase.io/en/library/bg/2/63/
- **Paraphrase:** Contemplation can escalate into attachment, desire, anger, delusion, and fall.
- **Teaching use:** Practical map for media/consumption spirals.
- **Limitation:** Low-risk examples only; no public habit shaming.

## Traceable example 3 — Decorating the prison cell (pedagogical theme)

- **Source status:** Recurring teaching analogy in the tradition’s presentation of material improvement without spiritual release; use as pedagogy paired with BG 7.14.
- **Teaching use:** Essential-question image.
- **Limitation:** Not a verse quotation; do not insult homes; do not invent anecdotes.

## Research decision

No extra medieval hagiography is required. Do not invent dialogues.
""",
    "cases": [
        {
            "title": "Notification spiral during reading",
            "situation": "A parent sits to read Bhagavad-gītā. A notification appears. “Ten seconds,” the mind says. Twenty minutes later, messages, news, and shopping have replaced the verse.",
            "mistaken": "“I can beat this with more willpower alone,” or “Screens are absolute evil so I must hate all media forever.”",
            "principle": "BG 7.14 — hard to overcome; surrender/shelter crosses. BG 2.62–63 attention chain.",
            "response": "Name the false promise without shame. Set one boundary (phone in another room for the reading window). Pair with shelter: five minutes japa or one verse card before any unlock.",
            "action": "Choose one three-day media boundary and one shelter cue; write both on the fridge.",
            "not_say": "“You’re a fake devotee.” Public screen-time ranking. Blaming a spouse’s gender for māyā.",
            "age": "Younger — shiny card vs helping card. Older — write false promise → boundary → shelter.",
        },
        {
            "title": "Shopping as identity polish",
            "situation": "A family already has needed clothes. A sale notification triggers a cart fill “to feel put together for Sunday.” Debt stress and comparison follow.",
            "mistaken": "“Decorating the house/wardrobe is the spiritual project,” or “Wanting beauty is always sinful.”",
            "principle": "BG 7.14 crossing by surrender; prison-cell analogy as pedagogy for misplaced ultimate projects.",
            "response": "Separate stewardship (needed care) from image-as-salvation. Delay purchase 24 hours; offer the saved attention to a short kīrtana or service chore.",
            "action": "One consumption delay rule for three days; replace one browse session with a shelter practice.",
            "not_say": "Shaming someone for poverty or for owning nice things. Calling women “māyā.”",
            "age": "Younger — “need vs shiny want” sort. Older — list one stewardship buy vs one image buy.",
        },
        {
            "title": "Mislabeling a person as māyā",
            "situation": "After a conflict, a parent mutters that a child, spouse, or “women in general” are māyā.",
            "mistaken": "People (especially women) are māyā; therefore contempt is spiritual.",
            "principle": "BG 7.14 — māyā is the Lord’s energy of the modes, not a person-class. Living beings are to be respected; cover is energetic, not an excuse for hate.",
            "response": "Correct firmly and kindly: people are not māyā. Māyā is the energy that makes us forget Kṛṣṇa. Repair the relationship; return to surrender and shelter.",
            "action": "Family correction card: “People ≠ māyā.” Practice one respectful repair sentence.",
            "not_say": "Anything that scapegoats gender, age, or a child as the illusory energy itself.",
            "age": "Younger — clear sentence drill. Older — rewrite the mistaken sentence into a true one.",
        },
    ],
    "discovery": [
        "Where do you notice “just ten seconds” turning into a fog?",
        "What is one comfort or image upgrade that helps service — and one that only polishes the cell?",
        "Which word in BG 7.14’s teaching meaning feels sharpest: difficult, surrender, or cross?",
    ],
    "understanding": [
        "State this week’s conclusion in one sentence.",
        "Name the primary scripture and the KUTUMBA teaching meaning (not as a BBT translation label).",
        "What two misconceptions does this week block?",
    ],
    "application": [
        "What three-day media or consumption boundary will we try?",
        "What shelter pairs with it (japa, verse card, check-in)?",
        "What is the minimum version if we are tired?",
    ],
    "qa": [
        {"q": "Isn’t māyā just “bad stuff” in the world?", "a": "BG 7.14 presents māyā as the Lord’s divine energy of the modes — covering and misdirecting — not a license to hate creation or people."},
        {"q": "Can discipline apps prove we defeated māyā?", "a": "No empirical claim proves ātman release. Tools may support a boundary; the doctrinal conclusion rests on BG 7.14 surrender."},
        {"q": "Are women māyā?", "a": "No. That is a harmful misconception. Māyā is energetic cover; persons are living beings to be respected."},
        {"q": "Does surrender mean neglect duty?", "a": "No. Crossing māyā is not hatred of household responsibility; it is refusing to make comfort/image the ultimate project."},
        {"q": "Should we discuss initiation or advanced māyā-tattva tonight?", "a": "Keep tonight to BG 7.14, boundary + shelter. Do not invent private spiritual diagnoses."},
        {"q": "What if my child refuses the boundary?", "a": "No force. Shorten. Parent models. Do not rank families."},
    ],
    "misconceptions": [
        "Hate all material duty / scapegoat women or children as māyā.",
        "Willpower alone conquers māyā without surrender.",
        "Confusing the prison-cell analogy with a śāstra quotation.",
        "Importing Cycle 3 God-identity teaching as if it replaces 7.14 tonight.",
        "Using mode labels from C2-W4 as permanent insults.",
    ],
    "no_speculate": [
        "Invented deity dialogue or private purport claims.",
        "Diagnosing anyone’s past karma or “demoniac nature” in the room.",
        "Guarantees of advancement, initiation, or certification.",
        "Claims that psychology has measured māyā.",
        "Graphic addiction or panic stories for children.",
    ],
    "do_not_claim": [
        "Human, temple, or publication approval for this guide.",
        "BBT ownership of KUTUMBA teaching materials or teaching meanings.",
        "That science proves māyā, ātman, or BG 7.14.",
        "That Gamma decks are rendered or approved (prompts only).",
    ],
    "reunification": """Invite one sentence per family — no confession pressure:
> This week, our boundary is _________, and our shelter is _________, so we stop decorating bondage at _________.""",
    "lab_steps": """1. **Name the false promise** — Write one lure (“just ten seconds,” “one more cart item”) and turn the paper face down.
2. **Set one boundary** — Device location, app limit, delayed purchase, or no-device sacred space.
3. **Add shelter** — Five minutes attentive japa or one verse-card reading with a clear start and end.
4. **Pair them** — Boundary without shelter becomes white-knuckle force; shelter without boundary ignores the lure.
Demonstrate once with a mock phone. No forced disclosure of real family fights.""",
    "project": "one family card answering “Where are we decorating bondage?” with one boundary + shelter",
    "home_min": "Use one media or consumption boundary for three days.",
    "home_std": "Boundary + one short daily shelter (japa or verse card) + memory line once.",
    "home_stretch": "Map one attention chain privately (notice → want → act → fog) and revise the boundary.",
    "home_evidence": "What changed after the boundary + shelter?",
    "next_week": "**C2-W6 — Integration Night: Choice, Consequence and the Modes** (review BG 3.9 · 18.63 · 2.22 · 14.5 · 7.14). Name the title only. Do not teach the five-lens method early tonight.",
    "parent_notes": [
        "Attention snapshot: first and last attention of the day (private).",
        "Reread BG 7.14 teaching meaning; glance at 2.62–63 paraphrase.",
        "Walk Case 3 (people ≠ māyā) with firm kindness.",
        "Design boundary + shelter pair; write on card.",
        "Saṅkalpa draft for reunification sentence.",
    ],
    "younger_pointer": "shiny-choice routine, decorated-cage craft, clear “people are not māyā” sentence",
    "older_pointer": "text observation on 7.14, attention-chain map, scenario cards, project contribution",
    "materials": [
        "Printed verse card (Devanāgarī / IAST / KUTUMBA teaching meaning)",
        "Mock phone or notification cards",
        "Shiny-choice vs help-choice picture cards",
        "Decorated-cage craft supplies",
        "Attention-chain cards (BG 2.62–63 simplified)",
        "Soft toss object; crayons; card stock",
        "Snack + water supplies (no weekly meal setup)",
        "Privacy reminder slip for facilitators",
    ],
    "closing": """> Thank you. Remember: Kṛṣṇa’s material energy is difficult to overcome, but those who surrender to Him can cross beyond it. Surrender crosses māyā. We meet again for C2-W6. Go gently; practice one boundary for three days; we do not rank one another.""",
    "self_check": [
        "Did I teach difficulty and surrender together?",
        "Did I explicitly block “women/people are māyā”?",
        "Did I avoid forced confession and ranking?",
        "Did I keep snack/water only and parents onsite?",
        "Did I label KUTUMBA teaching meaning correctly (not as BBT translation)?",
        "Did I avoid claiming human/temple publication approval?",
    ],
    "science_reason": "Māyā as the Lord’s divine material energy and the teaching that surrender crosses it are doctrinal conclusions from BG 7.14. Empirical psychology or attention research cannot prove or disprove māyā-tattva, the modes as ontological cover, or the Lord’s order over material nature. Therefore this week does not cite a study as evidence for the siddhānta.",
    "science_borrow": "Classroom language for boundaries and habit cues may borrow ordinary attention-design ideas (device location, delay, replacement practice) as **implementation scaffolding only**. That borrowing must never be presented as scientific proof that māyā exists, that karma is measurable, or that BG 7.14 has been experimentally verified.",
    "science_line": "Science may help us design a boundary habit. It does not prove māyā. Tonight’s conclusion rests on Bhagavad-gītā 7.14.",
    "younger": {
        "objective": "Children learn that shiny things can pull attention away from what matters, practice stop-and-choose, and clearly say people are not māyā. They take home a decorated-cage craft with the memory phrase.",
        "child_paraphrase": "Kṛṣṇa’s energy can make forgetfulness look shiny. We ask Kṛṣṇa for help and choose good next steps. People are not māyā.",
        "block": ["People (or girls/boys) are māyā.", "I can grab every shiny thing."],
        "materials": [
            "Shiny toy or foil card vs helping-hands picture",
            "Soft puppet",
            "Card stock cages / boxes for craft",
            "Stickers, crayons, glue sticks",
            "Printed memory phrase stickers if available",
            "Soft toss object for backup",
            "Calm-corner chair",
        ],
        "open": """1. Welcome by name; feet on floor.
2. Echo memory phrase three times: *Surrender / crosses / māyā.*
3. Show shiny card and helping card.
4. Practice the correction sentence once: “People are not māyā.”""",
        "story": """> Sometimes something shiny makes us forget what we were doing to help.
> Kṛṣṇa teaches that His material energy is hard to cross by ourselves. When we take shelter of Kṛṣṇa, we can cross.
> A pretty cage is still a cage if we forget Kṛṣṇa. Making the cage pretty is not the same as being free.
> People are not māyā. Māyā is the energy that makes us forget. We can stop, remember Kṛṣṇa, and choose a helping step.""",
        "story_boundaries": "Paraphrase BG 7.14 themes only. No invented deity quotes. No scary prison talk. No blaming a child as “māyā.”",
        "wonder": [
            "What should we do when something shiny pulls us?",
            "Who helps us cross when forgetting feels strong? (Kṛṣṇa)",
            "Are people māyā? (No.)",
        ],
        "movement_name": "Shiny Freeze and Help",
        "movement": """1. Spread children in a safe open space.
2. Teacher shows shiny card — children freeze (stop).
3. Teacher says “Remember Kṛṣṇa” — hand on heart + memory phrase.
4. Teacher shows helping card — children take three gentle steps to the kindness mat and sit.
5. Play three rounds. On round three, children point to helping card on the green choice.
6. End seated; say together: “People are not māyā.”""",
        "craft_name": "Decorated cage reminder card",
        "craft": """1. Give each child a folded card with a simple cage outline.
2. Let them add 2–3 “pretty” stickers (decorations).
3. Inside, helper writes: **Surrender crosses māyā.**
4. On the back, child draws one helping choice.
5. Practice: touch decorations, then open card and say the memory phrase — beauty is not the whole story.""",
        "redirects": {
            "Feet on floor": "Feet visit the mat.",
            "Kind hands": "Toys rest; hands help.",
            "Loud shout": "Soft voice, please.",
            "Quiet reset": "Calm corner with helping card for 60 seconds.",
        },
        "redirect_table": [
            {"signal": "Running", "line": "Freeze bodies — shiny pause.", "action": "Freeze, then walk"},
            {"signal": "Snatching", "line": "Helping hands.", "action": "Hands to lap"},
            {"signal": "Calling someone māyā", "line": "People are not māyā.", "action": "Repeat correction"},
            {"signal": "Shutdown", "line": "Quiet reset is okay.", "action": "Calm corner 60 sec"},
        ],
        "backup": """1. Sit in a circle with soft toss object.
2. Child catches, says “People are not māyā” or one helping choice, tosses to next.
3. End with three echoes of the memory phrase.""",
        "success": [
            "Child can echo: Surrender crosses māyā.",
            "Child can say: People are not māyā.",
            "Child can name one helping choice when shiny pulls.",
        ],
    },
    "older": {
        "objective": "Students observe BG 7.14, explain that māyā is hard to overcome and crossed by surrender, map one attention chain, and contribute one project sentence answering: Where are we decorating bondage?",
        "supports": "BG 2.62–63 attention chain; BG 9.10 nature under the Lord; prison-cell pedagogy with limits.",
        "scope": "Do not teach Cycle 3 God-identity lectures tonight; keep C2-W6 five-lens method for next week.",
        "materials": [
            "Printed verse strip: Devanāgarī + IAST + KUTUMBA teaching meaning",
            "Worksheet copies from activities/OLDER-ACTIVITY-PACK.md",
            "Scenario cards (notification; shopping polish; people≠māyā)",
            "Attention-chain diagram sheet",
            "Pencils; timer; OLDER-ANSWER-KEY.md for teacher only",
            "Project contribution half-sheets",
        ],
        "hook": """1. Welcome; feet on floor.
2. Hook: “Is upgrading your room always freedom?” Let two volunteers answer; hold the prison-cell image gently.
3. State essential question: Where are we decorating bondage?""",
        "text_obs": """1. Display BG 7.14; read IAST aloud together once.
2. Students underline: difficult / surrender / cross.
3. Observation prompts: Whose energy? What is it made of? How is it crossed?
4. Add one-sentence bridges to BG 2.62–63 and BG 9.10.
5. Paraphrase only; no invented dialogue.""",
        "scenarios": """Each group gets one fictional card:
**Card A — Notification spiral**
**Card B — Shopping as identity polish**
**Card C — Mislabeling a person as māyā**
For each: mistaken conclusion, boundary, shelter, what not to say.""",
        "game_name": "False Promise / True Crossing",
        "game": """1. Teacher reads a short claim.
2. Teams hold **F** (false promise / misconception) or **T** (true to BG 7.14).
3. Three rounds; explain one T using surrender or cross.
4. Keep respectful; no mocking.""",
        "diagram": """On the attention-chain sheet, fill one low-risk example:
`Notice → Want → Act → Fog`
Then add a side path: `Surrender cue → Boundary → Shelter`.
Circle the surrender cue; write the short echo.""",
        "project_close": """Complete Section E project sentence. Hand to parent at 3:10 reunification. No public ranking.""",
        "defer": "Deep initiation debates; diagnosing demoniac nature; Cycle 3 extended theology.",
        "worksheet_a": """1. In your own words, what makes māyā hard to overcome?
2. Circle three key words in the teaching meaning: difficult / surrender / cross / women / willpower-alone. Cross out the distractors that do **not** belong.
3. Name one false promise a lure might make.
4. What does “people are not māyā” protect in a family?
5. Why is “just try harder forever” incomplete after hearing BG 7.14?
6. How does decorating a prison cell differ from caring for a home as service?""",
        "worksheet_b": """Your group card: ☐ Notification  ☐ Shopping polish  ☐ People≠māyā

1. Mistaken conclusion:
2. Boundary:
3. Shelter:
4. One sentence you should **not** say:""",
        "worksheet_c": """Fill a low-risk attention chain and the surrender side-path. Do not write private family secrets.""",
        "worksheet_d": """Hold F or T. Write one true crossing line you want to remember:""",
        "worksheet_e": """Where we decorate bondage: ______________________________
Our three-day boundary: ______________________________
Our shelter: ______________________________""",
        "worksheet_f": """How does BG 7.14 challenge both “hate people/world” and “willpower alone”? (2–4 sentences)""",
        "answer_a": """1. It is the Lord’s divine energy of the modes; unaided struggle is insufficient (accept close paraphrases).
2. Circle: difficult, surrender, cross. Cross out: women, willpower-alone (as “the method”).
3. Examples: “just ten seconds,” “one more item will complete me.”
4. Protects persons from scapegoating; keeps māyā as energy, not a people-class.
5. Verse centers surrender, not solo force.
6. Stewardship cares for resources for service; decorating bondage makes comfort/image the ultimate project.""",
        "answer_b": """### Notification
- Mistaken: willpower alone / total media hatred as spirituality.
- Boundary + shelter pair; no public shame.

### Shopping polish
- Mistaken: image as salvation OR beauty always sinful.
- Delay + shelter; no poverty/wealth shaming.

### People≠māyā
- Mistaken: persons (esp. women) are māyā.
- Firm correction; repair; never scapegoat.""",
        "answer_d": """Mark T for surrender/crossing/people≠māyā. Mark F for hate-scapegoats or willpower-only claims.""",
    },
})

print("C2-W5 defined", flush=True)

from _gen_weeks_rest import REST_WEEKS

for w in REST_WEEKS:
    add(w)

def emit_all():
    for w in WEEKS:
        root = BASE / w["dir"]
        write(root / "teacher" / "MAIN-FACILITATOR-GUIDE-V12.md", render_main(w))
        write(root / "teacher" / "YOUNGER-TEACHER-GUIDE.md", render_younger(w))
        write(root / "teacher" / "OLDER-TEACHER-GUIDE.md", render_older(w))
        write(root / "activities" / "YOUNGER-ACTIVITY-PACK.md", render_younger_pack(w))
        write(root / "activities" / "OLDER-ACTIVITY-PACK.md", render_older_pack(w))
        write(root / "activities" / "OLDER-ANSWER-KEY.md", render_answer_key(w))
        write(root / "research" / "SCRIPTURAL-EXAMPLES.md", render_scriptural(w))
        write(root / "research" / "ANALOGIES-AND-LIMITS.md", render_analogies(w))
        write(root / "research" / "CASE-STUDIES.md", render_cases(w))
        write(root / "research" / "DEVOTIONAL-AND-HISTORICAL-EXAMPLES.md", render_devotional(w))
        write(root / "research" / "SCIENCE-AND-APPLICATION.md", render_science(w))
        main = root / "teacher" / "MAIN-FACILITATOR-GUIDE-V12.md"
        print(f"{w['code']}: {main.stat().st_size} bytes MAIN")

if __name__ == "__main__":
    emit_all()

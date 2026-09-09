#!/usr/bin/env python3
"""Author gold-standard packs for remaining shallow C2-W5/W6 and all C3 weeks."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "11-weekly-program-library" / "first-six-months"


def science_na(code: str, ref: str, url: str, reason: str) -> str:
    return f"""# {code} Science and Application

**Primary doctrinal anchor:** {ref} — {url}

## Option B — explicit N/A

**N/A — no empirical claim is needed for this week's doctrinal conclusion.**

### Reason

{reason}

### Allowed pedagogical borrowing (non-proof)

Ordinary habit language (cue, pause, checklist) may help families practice. It must never be presented as scientific proof of the week's siddhānta.

### Facilitator line if asked

> Helpful habits can support practice. Tonight's conclusion rests on {ref}, not on a lab study.
"""


def cases_md(code: str, ref: str, url: str, cases: list[dict]) -> str:
    parts = [
        f"# {code} Case Studies\n",
        f"**Primary principle source:** {ref} — {url}",
        "**Note:** All cases are fictional / anonymized teaching constructs. Not reports about real cohort families.\n",
    ]
    for i, c in enumerate(cases, 1):
        parts.append(
            f"""### Constructed case {i} — {c['title']} (fictional)

- **Situation:** {c['sit']}
- **Tempting mistaken conclusion:** {c['mistake']}
- **Relevant principle / source:** {c['principle']} ({url})
- **Compassionate response:** {c['response']}
- **Family action:** {c['action']}
- **What not to say:** {c['not_say']}
- **Age adaptation:** Younger — {c.get('young','simplify to one kind act')}. Older — {c.get('old','map mistaken conclusion vs better next step')}.
"""
        )
    return "\n".join(parts)


def analogies_md(code: str, analogies: list[tuple[str, str, str]]) -> str:
    lines = [f"# {code} Analogies and Limits\n", "| Analogy | Value | Limit |", "|---|---|---|"]
    for name, value, limit in analogies:
        lines.append(f"| {name} | {value} | {limit} |")
    lines.append("\nAnalogies are pedagogy, not verse quotations.\n")
    return "\n".join(lines)


def scriptural_md(code: str, primary: dict, supports: list[tuple[str, str, str, str]]) -> str:
    rows = [
        f"# {code} Scriptural Examples\n",
        "| Reference | URL | Teaching paraphrase | Limitation |",
        "|---|---|---|---|",
        f"| {primary['ref']} (primary) | {primary['url']} | {primary['meaning']} | Teaching meaning ≠ BBT translation label; no full purport dump |",
    ]
    for ref, url, para, lim in supports:
        rows.append(f"| {ref} | {url} | {para} | {lim} |")
    rows.append("\nParaphrase only. No invented dialogue.\n")
    return "\n".join(rows)


def devotional_md(code: str, text: str) -> str:
    return f"""# {code} Devotional and Historical Examples

{text}

**Research decision:** Use only paraphrase from named authoritative sources. Do not invent dialogue or private miracles.
"""


def younger_guide(w: dict) -> str:
    return f"""# {w['code']} Younger Teacher Guide (K–2)

**Week:** {w['title']}  
**Primary:** {w['ref']} — {w['url']}  
**Session length:** 40 minutes (parallel track ~2:30–3:10)  
**Parents:** Remain onsite; reunite at 3:10  
**Status:** Internal founding-cohort teaching material — human/temple review EXTERNAL_OPEN

## Objective

Children can say the memory phrase and complete one movement + one craft that reinforce this week's idea without fear or shame.

## Exact memory phrase

> {w['memory']}

## Teacher background (2 minutes)

- **KUTUMBA teaching meaning:** {w['meaning']}
- **Child-facing paraphrase:** {w['child_para']}
- **Block:** {w['misconception']}
- **Do not:** invent deity dialogue; force confessions; rank children; use scary imagery.

## Materials

- Printed line art if available (`visuals/V12/line-art-younger.png`)
- Crayons, tape, scissors (teacher-only for youngers)
- Soft toss object; two baskets or mats for movement game
- Card stock for memory cards
- Snack/water only after reunification (no weekly meal)

## Minute-by-minute plan

### 0–5 Opening
1. Welcome by name; feet on floor.
2. Echo memory phrase three times with clap rhythm.
3. Show one picture cue for the week: {w['young_cue']}.

### 5–13 Story script (~8 minutes)
Say this spine (paraphrase only; do not invent dialogue):

{w['young_story']}

### Wonder questions
1. {w['wonder'][0]}
2. {w['wonder'][1]}
3. {w['wonder'][2]}

### 13–20 Movement game — {w['move_name']}
Steps:
1. {w['move_steps'][0]}
2. {w['move_steps'][1]}
3. {w['move_steps'][2]}
4. Freeze cue: hands on heart; repeat memory phrase.

### 20–32 Craft — {w['craft_name']}
Steps:
1. {w['craft_steps'][0]}
2. {w['craft_steps'][1]}
3. {w['craft_steps'][2]}
4. Write or sticker the memory phrase on the craft.

### 32–38 Printable / quiet task
Children color the week line art and circle one home place where they will remember the phrase.

### 38–40 Cleanup / parent handoff
Clean mats; show craft to parent; one sentence: “Our phrase is: {w['memory']}.”

## Behavior redirects
1. Calm reminder → 2. Offer choice (sit spot / helper job) → 3. Quiet reset visible to parents → 4. Parent involvement. Never shame, yell, or force chanting.

## Backup (if energy crashes)
Soft toss while answering: “One kind next step at home is ___.”

## Materials checklist / cleanup
Bag crayons; wipe table; leave host space cleaner; return line-art masters to teacher folder.
"""


def older_guide(w: dict) -> str:
    return f"""# {w['code']} Older Teacher Guide (Grades 4–5)

**Week:** {w['title']}  
**Primary:** {w['ref']} — {w['url']}  
**Track window:** ~2:30–3:10 then reunite  
**Status:** Internal founding-cohort teaching material — human/temple review EXTERNAL_OPEN

## Objective

Students observe the primary text layer, complete a worksheet and scenario set, and contribute one project sentence answering: {w['eq']}

## Primary text observation
1. Read IAST aloud once: {w['iast']}
2. Students underline two words that seem important.
3. State KUTUMBA teaching meaning in full: {w['meaning']}
4. Label clearly: KUTUMBA teaching meaning — not BBT translation.

## Worksheet questions
1. In your words, what does {w['ref']} teach this week?
2. What mistaken idea does this week block? ({w['misconception']})
3. Name one home situation where this teaching changes a next step.
4. What is still confusing? (honest question OK)

## Scenario cards (read–choose–explain)
{w['older_scenarios']}

## Puzzle / game — {w['puzzle_name']}
{w['puzzle_steps']}

## Diagram task
Sketch a simple map of this week's idea using boxes/arrows. Label scripture vs analogy if both appear.

## Project contribution
Add one sentence to the cycle project answering the essential question. Keep ≤5 minutes.

## Reflection
Write: “This week I will practice ___ when ___.”

## Extension (optional)
Compare one supporting reference from the facilitator guide with the primary — what does it add, and what limit remains?

## Answer key pointer
Use `activities/OLDER-ANSWER-KEY.md` (teacher-only). Do not distribute keys to students during work time.
"""


def activities(w: dict) -> tuple[str, str, str]:
    yng = f"""# {w['code']} Younger Activity Pack

## Memory card
Write: {w['memory']}

## Color page
Color `visuals/V12/line-art-younger` and draw one place at home to practice.

## Craft reminder
{w['craft_name']}: {w['craft_steps'][0]} Then add the memory phrase.

## Home mini-task
With a parent, say the memory phrase once before bed.
"""
    old = f"""# {w['code']} Older Activity Pack

## Verse observation
IAST: {w['iast']}  
KUTUMBA teaching meaning: {w['meaning']}  
Source: {w['url']}

## Worksheet
Answer the four worksheet questions from the older teacher guide.

## Scenarios
{w['older_scenarios']}

## Puzzle
{w['puzzle_name']}: {w['puzzle_steps']}

## Project line
Essential question: {w['eq']}
Write one sentence contribution.
"""
    key = f"""# {w['code']} Older Answer Key (TEACHER-ONLY)

## Teaching meaning check
Accept paraphrases that preserve: {w['meaning']}

## Misconception to reject
{w['misconception']}

## Scenario guidance
Prefer answers that are compassionate, source-bound, and specific about a next responsible action. Reject shaming, ranking, and speculation.

## Puzzle
Accept any ordering/matching that keeps {w['ref']} as the doctrinal center and analogies labeled as pedagogy.
"""
    return yng, old, key


def facilitator(w: dict) -> str:
    supports_table = "\n".join(
        f"| {a} | {b} | {c} | {d} |" for a, b, c, d in w["supports"]
    )
    analogies = []
    for i, (name, value, limit) in enumerate(w["analogies"], 1):
        analogies.append(
            f"### {i}) {name}\n- **Say:** {value}\n- **Limit:** {limit}\n"
        )
    cases = []
    for i, c in enumerate(w["cases"], 1):
        cases.append(
            f"""### Constructed household case {i} — {c['title']}
- **Situation:** {c['sit']}
- **Mistaken conclusion:** {c['mistake']}
- **Principle / source:** {c['principle']} ({w['url']})
- **Compassionate response:** {c['response']}
- **Action:** {c['action']}
- **What not to say:** {c['not_say']}
"""
        )
    return f"""# {w['code']} Main Facilitator Guide — Saturday 2:00–4:00

**KUTUMBA · Families Growing in Krishna Consciousness**  
**Program Director: Swapnil Patil**  
**Week:** {w['title']}  
**Status:** Internal founding-cohort teaching material — human/temple review EXTERNAL_OPEN  
**Primary scripture:** {w['ref']} — {w['url']}

---

## Two-minute summary

{w['summary']}

## Essential question

{w['eq']}

## Memory line

{w['memory']}

## KUTUMBA teaching meaning (primary)

**KUTUMBA teaching meaning:** {w['meaning']}

Label this as **KUTUMBA teaching meaning**. Do not label it as a BBT translation. No full purport dumps.

---

## 15-minute night-before prep

1. Open {w['url']} and reread IAST + KUTUMBA teaching meaning.
2. Rehearse opening script aloud once.
3. Pack younger + older materials listed in age-band guides.
4. Review misconception to block: {w['misconception']}
5. Confirm snack/water only (no weekly meal); parents onsite.
6. Write home-practice minimum on a card: {w['home_min']}

## 60-minute deep prep

1. Read this guide’s analogies, scriptural examples, and three cases so you can teach them **inline**.
2. Open each supporting URL once; note teaching use and limitation.
3. Mark one discovery, one understanding, and one application question you will ask.
4. Walk parent / younger / older / reunification zones.
5. Review privacy: no forced confession; no ranking; no public sādhana scoring.
6. Confirm project contribution card and next-week title only: {w['next_week']}.

---

## Exact primary readings

- **Primary:** {w['ref']} — {w['url']}
- **IAST:** {w['iast']}
- **KUTUMBA teaching meaning:** {w['meaning']}
- **Rights:** Sanskrit from VedaBase display; KUTUMBA teaching meaning original; teaching meaning ≠ BBT translation label.

## Exact supporting readings (classroom paraphrase only)

| Reference | URL | Teaching paraphrase (facilitator may say) | Limitation |
|---|---|---|---|
{supports_table}

---

## One-page speaking map (Saturday 2:00–4:00)

1. 2:00 Welcome / mantras / purpose  
2. 2:10 Memory line + essential question  
3. Primary verse layer (IAST + KUTUMBA teaching meaning)  
4. Core explanation  
5. One analogy with limit spoken aloud  
6. One scriptural example paraphrase  
7. One constructed case  
8. 2:30 Track split  
9. 3:10 Reunification synthesis  
10. 3:30 Snack/water only — no weekly meal  
11. 3:40 Saṅkalpa / project / home practice  
12. 3:55 Next-week title only + close by 4:00  

---

## Exact opening script (≈3 minutes)

> Welcome. Today is {w['code']}: {w['title']}.  
> Our essential question is: {w['eq']}  
> From {w['ref']}, our KUTUMBA teaching meaning is: {w['meaning']}  
> We will hear together, practice in age bands, reunite, and take one small home step.  
> We do not rank families or children. Parents remain onsite. Snack and water only — no weekly meal.

## Extended 10–20 minute speaking SCRIPT

**[0–3 min — Hook]**  
{w['script_hook']}

**[3–7 min — Verse layer]**  
Read IAST briefly. State the full KUTUMBA teaching meaning. Pause.

**[7–12 min — Core + support]**  
{w['script_core']}

**[12–16 min — Analogy + limit]**  
Teach one analogy below and state its limit out loud.

**[16–18 min — Case]**  
Read Constructed Case 1 once. Ask for the mistaken conclusion and one compassionate next step.

**[18–20 min — Transition]**  
Preview age-band labs. At ~2:28 give track transition. Reunite at 3:10.

---

## Core explanation (facilitator must say)

{w['core']}

**Conclusion line:** {w['conclusion']}

**Common error to block:** {w['misconception']}

---

## Analogies / examples with limits (teach inline)

{chr(10).join(analogies)}

---

## Scriptural / devotional examples (paraphrase only)

{w['scriptural_examples']}

---

## Three constructed household cases (inline)

{chr(10).join(cases)}

---

## Discovery questions
1. {w['discovery'][0]}
2. {w['discovery'][1]}
3. {w['discovery'][2]}

## Understanding questions
1. {w['understanding'][0]}
2. {w['understanding'][1]}
3. {w['understanding'][2]}

## Application questions
1. {w['application'][0]}
2. {w['application'][1]}
3. {w['application'][2]}

---

## Five likely questions and source-based answers

1. **Q:** {w['faq'][0][0]}  
   **A:** {w['faq'][0][1]}
2. **Q:** {w['faq'][1][0]}  
   **A:** {w['faq'][1][1]}
3. **Q:** {w['faq'][2][0]}  
   **A:** {w['faq'][2][1]}
4. **Q:** {w['faq'][3][0]}  
   **A:** {w['faq'][3][1]}
5. **Q:** {w['faq'][4][0]}  
   **A:** {w['faq'][4][1]}

---

## Misconceptions and no-speculation boundaries

- Block: {w['misconception']}
- Do not invent dialogue for scriptural persons.
- Do not diagnose private karma in the room.
- Do not claim temple/BBT/human approval that has not been given.
- Defer off-scope ontology to the named next week: {w['next_week']}.

---

## Track transitions

**2:30:** “Younger friends with [teacher]; older learners with [teacher]; parents may observe or assist as assigned. We reunite at 3:10.”  
**3:10 synthesis prompt:** “In one sentence, what did your track learn about: {w['eq']}”

## Family synthesis / project / home practice

- Project: one family artifact answering the essential question (see `project/CYCLE-CONTRIBUTION.md`).
- Home practice minimum: {w['home_min']}
- Success = minimum version completed once.

## Next week

Title only: {w['next_week']}. Do not teach its full ontology tonight.

## Close

Appreciate effort; leave host spaces cleaner; end by 4:00.
"""


def pack_for(w: dict) -> None:
    base = ROOT / w["slug"]
    (base / "teacher").mkdir(parents=True, exist_ok=True)
    (base / "activities").mkdir(parents=True, exist_ok=True)
    (base / "research").mkdir(parents=True, exist_ok=True)
    primary = {"ref": w["ref"], "url": w["url"], "meaning": w["meaning"]}
    (base / "teacher" / "MAIN-FACILITATOR-GUIDE-V12.md").write_text(facilitator(w), encoding="utf-8")
    (base / "teacher" / "YOUNGER-TEACHER-GUIDE.md").write_text(younger_guide(w), encoding="utf-8")
    (base / "teacher" / "OLDER-TEACHER-GUIDE.md").write_text(older_guide(w), encoding="utf-8")
    yng, old, key = activities(w)
    (base / "activities" / "YOUNGER-ACTIVITY-PACK.md").write_text(yng, encoding="utf-8")
    (base / "activities" / "OLDER-ACTIVITY-PACK.md").write_text(old, encoding="utf-8")
    (base / "activities" / "OLDER-ANSWER-KEY.md").write_text(key, encoding="utf-8")
    (base / "research" / "SCRIPTURAL-EXAMPLES.md").write_text(scriptural_md(w["code"], primary, w["supports"]), encoding="utf-8")
    (base / "research" / "ANALOGIES-AND-LIMITS.md").write_text(analogies_md(w["code"], w["analogies"]), encoding="utf-8")
    (base / "research" / "CASE-STUDIES.md").write_text(cases_md(w["code"], w["ref"], w["url"], w["cases"]), encoding="utf-8")
    (base / "research" / "SCIENCE-AND-APPLICATION.md").write_text(
        science_na(w["code"], w["ref"], w["url"], w["science_reason"]), encoding="utf-8"
    )
    (base / "research" / "DEVOTIONAL-AND-HISTORICAL-EXAMPLES.md").write_text(
        devotional_md(w["code"], w["devotional"]), encoding="utf-8"
    )
    main = base / "teacher" / "MAIN-FACILITATOR-GUIDE-V12.md"
    print(f"{w['code']}: MAIN {main.stat().st_size} bytes")


def W() -> list[dict]:
    """Week specifications."""
    return [
        dict(
            code="C2-W5",
            slug="c2-w5-māyā-decorating-the-prison-cell",
            title="Māyā: Decorating the Prison Cell",
            eq="Where am I decorating the prison instead of seeking freedom?",
            memory="Do not decorate the prison — seek the Lord.",
            ref="BG 7.14",
            url="https://vedabase.io/en/library/bg/7/14/",
            iast="daivī hy eṣā guṇa-mayī mama māyā duratyayā / mām eva ye prapadyante māyām etāṁ taranti te",
            meaning="This divine illusory energy made of the modes is hard to overcome — but those who surrender to the Lord cross beyond it.",
            misconception="Comfort upgrades equal spiritual progress.",
            next_week="C2-W6 Integration Night: Choice, Consequence, and the Modes",
            home_min="Once this week: before one comfort upgrade or treat, pause and offer a short remembrance of Kṛṣṇa.",
            summary="Māyā made of the modes is hard to overcome by private cleverness. BG 7.14 teaches that those who surrender to the Lord cross beyond it. This week names the habit of decorating bondage with nicer comforts while postponing seeking Kṛṣṇa. Block: comfort upgrades = spiritual progress.",
            core="We can improve a cage without leaving it. Māyā is not merely ‘bad stuff’; it includes the bewildering energy that keeps the living being busy polishing temporary arrangements while forgetting the Lord. BG 7.14 is honest: crossing is hard — and possible for those who surrender to Kṛṣṇa. Tonight we look for one place we decorate the prison, then choose one seeking act.",
            conclusion="Seek the Lord; do not only decorate the cell.",
            script_hook="Many homes get better at making temporary life prettier: better screens, better snacks, better schedules. Those can be useful. The danger is believing polish equals freedom. A painted prison cell is still a cell.",
            script_core="State BG 7.14 fully. Add BG 7.13 in one sentence: mode-delusion hides the Lord who is above the modes. Keep compassion: we are not mocking comfort; we are refusing to confuse comfort with liberation.",
            child_para="Sometimes we try to make a stuck place prettier instead of asking Kṛṣṇa for help to become free. Seeking Kṛṣṇa matters more than fancy decorations.",
            young_cue="A plain door drawing vs a decorated wall drawing — ask which one opens.",
            young_story="""> Sometimes a person cleans and decorates a small locked room until it looks nice. Looking nice can feel good.  
> But a pretty locked room is still locked.  
> Kṛṣṇa teaches that His illusory energy is hard to cross by ourselves. Those who turn to Him can cross.  
> So we practice one small way to seek Kṛṣṇa — not only to decorate what is temporary.""",
            wonder=["What is one pretty thing that is temporary?", "What does it mean to ask Kṛṣṇa for help?", "Who can we seek with at home?"],
            move_name="Decorate or Door",
            move_steps=["Two mats: Decorate mat and Door mat.", "Teacher calls a situation; children gently move to Door when the answer is seek Kṛṣṇa / ask help / remember.", "If they choose Decorate for a comfort-only answer, smile and invite a Door retry."],
            craft_name="Open-door card",
            craft_steps=["Fold cardstock as a door.", "Outside: draw one temporary pretty thing.", "Inside: write or sticker ‘Seek Kṛṣṇa’ / memory phrase."],
            older_scenarios="""1) Stress → buy/upgrade treat immediately. 2) Image management online replaces evening remembrance. 3) Spiritual talk used to avoid chores. For each: name decorating vs seeking.""",
            puzzle_name="Cell vs Key match",
            puzzle_steps="Match cards: painted walls / new gadget / status post → ‘decorating’; prayer / verse / humble ask for help → ‘seeking’. Discuss one mismatch temptation.",
            supports=[
                ("BG 7.13", "https://vedabase.io/en/library/bg/7/13/", "Deluded by the three modes, the world does not know the Lord who is above them.", "Do not mock people; keep compassion."),
                ("BG 7.15", "https://vedabase.io/en/library/bg/7/15/", "Those whose knowledge is stolen by māyā do not surrender.", "Do not label children demoniac."),
                ("BG 15.7", "https://vedabase.io/en/library/bg/15/7/", "The living being is an eternal fragment of the Lord struggling with the senses.", "Struggle language must stay kind."),
            ],
            analogies=[
                ("Prison cell paint", "Painting a cell prettier does not open the door.", "Do not shame ordinary comforts; pedagogy only."),
                ("Wallpaper vs battery", "A beautiful phone wallpaper does not charge a dead battery.", "Tech analogy ≠ śāstra."),
                ("Costume crown", "A costume crown can feel royal while dependence remains.", "Do not mock celebrations or dress."),
            ],
            cases=[
                dict(title="Upgrade spiral", sit="A family upgrades gadgets and treats whenever stress rises; spiritual practice waits until life feels nicer.", mistake="Nicer life automatically means freer life.", principle="BG 7.14 — māyā is hard; surrender crosses", response="Name the comfort without shame; ask what seeking the Lord looks like in one small act.", action="One comfort pause + short remembrance before a treat.", not_say="Materialistic family / bad devotees."),
                dict(title="Prestige first", sit="A teen treats school image as the real path; Kṛṣṇa talk can wait.", mistake="Worldly polish equals crossing māyā.", principle="BG 7.14; BG 7.13", response="Affirm education duty; separate duty from identity-as-image.", action="Replace one prestige scroll with memory line once.", not_say="School is māyā so quit trying."),
                dict(title="Spiritualized neglect", sit="A parent uses māyā-talk to avoid needed repair and kindness at home.", mistake="Talk about māyā excuses neglect of duty.", principle="Surrender includes responsible action", response="Separate prison-decorating from honest duty offered to Kṛṣṇa.", action="One duty act + one remembrance.", not_say="Using ‘you are in māyā’ as an insult."),
            ],
            discovery=["Where do we polish temporary arrangements?", "What does ‘hard to overcome’ protect us from?", "What does surrender look like in a small home act?"],
            understanding=["What does BG 7.14 say is hard?", "Who crosses māyā according to the verse?", "How is decorating different from duty?"],
            application=["Name one decorating habit to pause this week.", "Name one seeking act to add.", "How will we speak without shaming?"],
            faq=[
                ("Is comfort sinful?", "No. The issue is mistaking polish for liberation. Duty and kindness remain."),
                ("Does this condemn nice homes?", "No. Hosts should keep spaces clean. We refuse the story that upgrades equal freedom."),
                ("What is surrender here?", "Turning to Kṛṣṇa with humility and practice — not dramatic self-hate."),
                ("Can kids understand māyā?", "Use prison/door language; avoid fear."),
                ("Is this anti-ambition?", "No. Ambition without seeking can decorate bondage; duty can be offered to Kṛṣṇa."),
            ],
            science_reason="BG 7.14’s teaching about māyā and surrender is a doctrinal conclusion from śāstra. Empirical consumer-psychology studies about shopping or screens cannot prove or disprove māyā as divine illusory energy or the efficacy of surrender to the Lord.",
            scriptural_examples="""### Example A — Modes hide the Lord (BG 7.13)
Paraphrase: bewildered by modes, people do not know the Lord above them. Teaching use: decorating can be mode-busy-ness. Limit: no mockery.

### Example B — Crossing by surrender (BG 7.14)
Primary: hard to overcome; those who surrender cross. Teaching use: honest difficulty + hope. Limit: no invented surrender stories.""",
            devotional="Traceable theme: Śrīla Prabhupāda repeatedly warned against polishing material life while neglecting Kṛṣṇa consciousness (classroom paraphrase from authorized teachings; no invented anecdotes). Use only to support seeking over decorating.",
        ),
        # Remaining weeks abbreviated but complete via same schema — continue in part 2 file execution
    ]


def main() -> None:
    weeks = W()
    # Companion data module lives beside this file
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from author_remaining_weeks_data import EXTRA_WEEKS

    weeks.extend(EXTRA_WEEKS)
    for w in weeks:
        pack_for(w)


if __name__ == "__main__":
    main()

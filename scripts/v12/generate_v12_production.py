#!/usr/bin/env python3
"""V12 one-pass production generator — week packs, verse packs, calendar, navigation, Gamma."""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
LAUNCH = REPO / "launch"
EXPORTS = REPO / "exports" / "final"
VERSE_YAML = Path(__file__).with_name("verse_data.yaml")

WEEKS = [
    ("C1-W1", "c1-w1-what-is-kutumba-and-why-are-we-here", "What Is KUTUMBA, and Why Are We Here?", "Why are we committing as a family?", "Protected weekly hearing plus home practice creates a path for family growth.", "Coming without home practice is enough.", "orientation_bingo", "rules_sort", "family_purpose_card"),
    ("C1-W2", "c1-w2-i-am-not-this-body", "I Am Not This Body", "How should body-language change?", "Body changes; conscious self continues.", "Psychology/photos prove the soul.", "life_stage_timeline", "sequence_craft", "body_self_grid"),
    ("C1-W3", "c1-w3-the-nature-of-the-soul", "The Nature of the Soul", "If I am a soul, how should I live?", "Jīva is eternal, conscious, individual — not God Himself.", "All souls are God.", "is_isnot_sort", "offering_craft", "crossword"),
    ("C1-W4", "c1-w4-why-human-life-is-rare-and-valuable", "Why Human Life Is Rare and Valuable", "What deserves protected family time?", "Human life is a rare opportunity for self-realization.", "Fear/death pressure motivates children.", "time_jar", "priority_maze", "time_budget"),
    ("C1-W5", "c1-w5-the-temporary-world-and-the-search-for-permanent-happiness", "The Temporary World and the Search for Permanent Happiness", "How can enjoyment become gratitude and service?", "Temporary things usable; lasting shelter in Kṛṣṇa.", "Material affection is worthless.", "temp_vs_lasting_sort", "sparkler_lamp", "word_search"),
    ("C1-W6", "c1-w6-integration-night-who-am-i-and-how-should-our-family-live", "Integration Night: Who Am I, and How Should Our Family Live?", "Can our family explain and apply what we learned?", "Identity, purpose, and practice form one life.", "Competition/ranking.", "retrieval_stations", "cycle_board", "presentation_prep"),
    ("C2-W1", "c2-w1-action-and-reaction-how-karma-binds", "Action and Reaction: How Karma Binds", "How do our actions bind or free us?", "Work offered to the Lord frees; other work binds.", "Fatalism removes responsibility.", "cause_effect_chain", "knot_craft", "karma_scenario_sort"),
    ("C2-W2", "c2-w2-free-will-and-responsibility-the-next-choice-matters", "Free Will and Responsibility: The Next Choice Matters", "What is my next responsible choice?", "Deliberate, then act — the next choice matters.", "We have no agency.", "choice_fork_game", "door_craft", "decision_matrix"),
    ("C2-W3", "c2-w3-birth-death-and-reincarnation", "Birth, Death and Reincarnation", "How do we speak calmly about birth and death?", "The self changes bodies like garments — teach without fear.", "Scare children with death.", "gentle_garment_story", "new_clothes_craft", "timeline_calm"),
    ("C2-W4", "c2-w4-the-three-modes-of-material-nature", "The Three Modes of Material Nature", "Which mode is shaping this moment?", "Sattva, rajas, tamas bind the embodied self.", "Use modes to shame others.", "mode_traffic_lights", "mode_sort_cards", "mode_journal_grid"),
    ("C2-W5", "c2-w5-māyā-decorating-the-prison-cell", "Māyā: Decorating the Prison Cell", "Where are we decorating bondage?", "Māyā is hard to cross; surrender to Kṛṣṇa is the way.", "Hate all material duty.", "decoration_vs_door", "prison_window_craft", "maya_ad_critique"),
    ("C2-W6", "c2-w6-integration-night-choice-consequence-and-the-modes", "Integration Night: Choice, Consequence and the Modes", "Can we synthesize choice and modes?", "Choice, consequence, and modes form one practice.", "Ranking families.", "mode_choice_stations", "synthesis_poster", "family_share"),
    ("C3-W1", "c3-w1-who-is-god-the-supreme-enjoyer-proprietor-and-friend", "Who Is God? The Supreme Enjoyer, Proprietor and Friend", "Who is God to our family?", "God is enjoyer, proprietor, and friend — knowing Him brings peace.", "God is an impersonal force only.", "three_titles_sort", "friend_heart_craft", "peace_formula_map"),
    ("C3-W2", "c3-w2-who-is-kṛṣṇa-the-supreme-personality-of-godhead", "Who Is Kṛṣṇa? The Supreme Personality of Godhead", "Who is Kṛṣṇa?", "Nothing is superior to Kṛṣṇa; all rests on Him.", "Invented līlā dialogue.", "pearl_thread_demo", "flute_flower_craft", "source_observation"),
    ("C3-W3", "c3-w3-guru-sādhu-and-śāstra-how-we-receive-spiritual-knowledge", "Guru, Sādhu and Śāstra: How We Receive Spiritual Knowledge", "How do we receive spiritual knowledge?", "Approach truth-seers with humility, inquiry, and service.", "Independent speculation equals revelation.", "three_pillars_build", "inquiry_card", "source_ladder"),
    ("C3-W4", "c3-w4-śrī-caitanya-mahāprabhu-and-the-holy-name", "Śrī Caitanya Mahāprabhu and the Holy Name", "Why chant the holy name?", "The holy name cleanses the heart and spreads auspiciousness.", "Force chanting as punishment.", "name_echo_game", "mirror_craft", "sikastaka_observation"),
    ("C3-W5", "c3-w5-the-nine-processes-of-bhakti", "The Nine Processes of Bhakti", "Which bhakti process can our family practice this week?", "Nine processes map a family path of devotion.", "Require mastering all nine at once.", "nine_path_walk", "nine_icons_craft", "process_match"),
    ("C3-W6", "c3-w6-bhakti-mela-kīrtana-drama-and-family-presentation", "Bhakti Mela: Kīrtana, Drama and Family Presentation", "How do we celebrate what we learned?", "Share with joy and humility — no ranking.", "Competitive devotion scoring.", "mela_stations", "drama_rehearsal", "presentation_rubric"),
]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def load_verses() -> dict:
    return yaml.safe_load(VERSE_YAML.read_text(encoding="utf-8"))


def verse_key(code: str) -> str:
    return code.lower().replace("-", "_")


def gamma_slide(n, title, audience, objective, copy, composition, palette, typography, visual_type, image_prompt, diagram, source, notes, interaction, donot, access):
    return f"""### Slide {n} — {title}

- **Audience:** {audience}
- **Teaching objective:** {objective}
- **Exact on-screen copy:**
{chr(10).join('  - ' + line for line in copy)}
- **Screen composition:** {composition}
- **Palette role:** {palette}
- **Typography:** {typography}
- **Visual type:** {visual_type}
- **Detailed AI image prompt:** {image_prompt}
- **Diagram instructions:** {diagram}
- **Source:** {source}
- **Presenter notes:** {notes}
- **Interaction:** {interaction}
- **Do-not-claim:** {donot}
- **Accessibility:** {access}
"""


def build_gamma(code: str, slug: str, title: str, question: str, conclusion: str, misconception: str, v: dict, integration: bool) -> None:
    g = WEEKLY / slug / "gamma"
    ref, url = v["reference"], v["url"]
    meaning = v["kutumba_teaching_meaning"]
    iast, dev = v["iast"], v["devanagari"]
    brand = "KUTUMBA • Families Growing in Krishna Consciousness"
    donot = "Not human-approved; not publication-ready; Gamma not rendered; science ≠ siddhānta; teaching meaning ≠ BBT translation"
    access = "Large type; high contrast; read Devanāgarī/IAST aloud; alt-text for images"

    if code == "C1-W1":
        topics = [
            ("Welcome to KUTUMBA", ["KUTUMBA", "Families Growing in Krishna Consciousness", "Saturday 2:00–4:00"], "launch/FAMILY-COVENANT.md", "Full-bleed warm family gathering; 35% cream left panel with title"),
            ("What KUTUMBA is", ["Family sādhana community", "Parents onsite", "Protected hearing + home practice"], "launch policy", "Three icon columns: hear / practice / friendship"),
            ("What KUTUMBA is not", ["Not drop-off", "Not substitute temple", "Not ranking club"], "launch policy", "Calm stop icons — no scare imagery"),
            ("Six-month roadmap", ["C1 Identity", "C2 Karma & modes", "C3 Bhakti"], "FIRST-SIX-MONTH curriculum", "Three equal roadmap columns"),
            ("Saturday rhythm", ["1:50 arrival", "2:00–4:00 locked", "Snack + water only"], "launch/C1-SATURDAY-CALENDAR.md", "Clock + schedule list diagram"),
            ("Covenant highlights", ["Protect calendar", "Try home practice", "No gossip/comparison"], "FAMILY-COVENANT.md", "Handshake / commitment card visual"),
            ("Child house rules", ["Safe body", "Kind words", "Freeze cue"], "CHILD-HOUSE-RULES.md", "Simple rule icons for children"),
            ("Correction ladder", ["Reminder → redirect → reset → parent"], "TEACHER-READINESS-STANDARD.md", "Ladder diagram — never shame"),
            ("Teacher readiness", ["Objective", "Source", "Boundary", "Deferral"], "TEACHER-READINESS-STANDARD.md", "Checklist graphic"),
            ("Privacy", ["No public sādhana scoring", "Private feedback"], "FAMILY-COVENANT.md", "Lock / privacy symbol"),
            ("Opening mantras", ["Praṇāma", "Pañca-tattva", "Mahā-mantra"], "OPENING-MANTRAS-HANDOUT.md", "Soft lamp + mantra cards — no invented deity action"),
            ("Primary verse ŚB 1.2.18", [ref, "Devanāgarī on screen", "IAST", "KUTUMBA teaching meaning"], url, "Left 58% verse text; right 42% warm hearing illustration"),
            ("Teaching meaning", [meaning[:110], "Regular hearing + service"], url, "Key-idea callout panel"),
            ("Cycle 1 project", ["Who Am I…", "Cumulative layers", "Non-competitive W6"], "project brief", "Project folder + week beads"),
            ("Saṅkalpa", ["Action + frequency + trigger + minimum"], "launch-pack", "Saṅkalpa card mockup"),
            ("Home practice", ["5–15 minutes", "Minimum version = success"], "family-home-practice", "Kitchen-table family practice scene"),
            ("Feedback & close", ["Private questions welcome", "End on time"], "covenant", "Closing circle — instructional"),
            ("Next week", ["C1-W2 title only", "Do not teach ontology early"], "calendar", "Simple preview card"),
        ]
        # expand to 24–26 with more operational slides
        extra = [
            ("Host-home respect", ["Common areas", "Leave cleaner", "Ask before moving items"], "host rules", "Home doorway respect scene"),
            ("Parent commitments", ["Onsite", "Communicate absences", "Model practice"], "covenant", "Parents seated with children"),
            ("Age bands", ["K–2", "Grades 4–5", "Reunite 3:10"], "operating model", "Two path icons reuniting"),
            ("Bhakti lab preview", ["Short shared practice", "No forced volume"], "launch", "Soft kīrtana circle illustration"),
            ("Materials preview", ["Print packet", "Verse card", "Craft supplies"], "print checklist", "Table of printables"),
            ("Owner Friday night", ["Open V12-START-HERE", "Print W1 packet", "Read facilitator script"], "V12-START-HERE.md", "Friday checklist graphic"),
        ]
        topics = topics[:12] + extra[:4] + topics[12:]
        slides = []
        for i, (t, copy, src, comp) in enumerate(topics[:26], 1):
            is_verse = "1.2.18" in t or "Primary verse" in t
            if is_verse:
                copy = [ref, dev, iast, f"KUTUMBA teaching meaning: {meaning[:140]}", f"Source: {url}"]
            slides.append(
                gamma_slide(
                    i, t, "master", f"Orient founding cohort — {t}",
                    copy, comp,
                    "plum for philosophy; teal for family ops; saffron for bhakti action",
                    "Title 40–48pt; body 22–28pt; Devanāgarī readable",
                    "cinematic family or instructional diagram",
                    f"Cinematic ultra-realistic warm Pennsylvania home scene for '{t}', South Asian families generically represented, no identifiable real persons, natural afternoon light, saffron-cream accents, 16:9, no temple logo, no embedded text, no caricature",
                    "Use diagram only if composition requests columns/ladder/roadmap",
                    src if not is_verse else f"{ref} — {url}",
                    f"Stay warm and firm. Block: {misconception}. Brand: {brand}",
                    "One echo or show of hands",
                    donot, access,
                )
            )
        write(g / "V12-GAMMA-MASTER-DECK-PROMPT.md", f"# {code} V12 Gamma Master Deck\n\n**Status:** prompt-only — not rendered — not approved\n\n**Design system:** 16:9 · cream ground · plum/saffron/teal · charcoal text\n\n## Slides\n\n" + "\n".join(slides))
    else:
        count = 18 if integration else 16
        base = [
            (f"Title: {title}", [title, brand, "Saturday 2:00–4:00"], "Top title; soft hero family/devotional illustration"),
            (f"Essential question", [question], "Large question typography; minimal visual"),
            (f"Primary verse {ref}", [ref, dev, iast, f"KUTUMBA teaching meaning: {meaning[:120]}", url], "Left 58% verse; right 42% illustration"),
            ("Teaching meaning", [meaning, f"Conclusion: {conclusion}"], "Key-idea panel"),
            ("Context", [f"Week objective for {code}", "Stay in week scope"], "Simple context map"),
            ("Conclusion", [conclusion, f"Block: {misconception}"], "Bold conclusion card"),
            ("Scriptural / narrative support", ["See research examples", "Paraphrase only", "No invented dialogue"], "Devotional illustration — source-bound"),
            ("Analogy with limit", ["Name analogy", "State failure point", "Pedagogy ≠ śāstra quote"], "Analogy diagram with warning label"),
            ("Constructed case", ["Fictional household case", "Mistaken conclusion", "Compassionate action"], "Anonymous vignette"),
            ("Misconception check", [misconception, "Better statement"], "Myth vs truth two panels"),
            ("Concept diagram", [f"Use visuals/V12/concept-diagram.svg for {code}"], "Embed week-specific diagram"),
            ("Parent application", ["Home cue", "Minimum version", "No confession pressure"], "Adult discussion panel"),
            ("Younger track preview", ["Story + movement + craft", "Memory phrase"], "K–2 friendly illustration"),
            ("Older track preview", ["Text observation", "Puzzle", "Scenario"], "Grades 4–5 worksheet look"),
            ("Bhakti lab / reunification", ["3:10 reunite", "One family sentence"], "Reunification circle"),
            ("Project + home practice + close", ["Project layer", "5–15 min home", "End on time"], "Checklist close"),
        ]
        if integration:
            base = [
                ("Integration welcome", [title, "Retrieval not ranking"], "Warm welcome"),
                ("Concept chain", [iast, "Prior weeks linked"], "Horizontal chain diagram"),
                ("Primary review verse layer", [ref, meaning[:100]], "Verse review panel"),
                ("Misconception sweep", [misconception, "Common mix-ups"], "Myth/truth"),
                ("Retrieval stations", ["Visit stations", "Write one sentence"], "Station map"),
                ("Presentation template", ["~10 minutes/family", "Drawing-only OK"], "Template card"),
                ("Rubric non-competitive", ["Understanding", "Application", "Teamwork", "Source accuracy"], "Rubric table"),
                ("Review-before-next-cycle", ["Extend if unclear", "No shame"], "Decision fork"),
                ("Off week / Utsava note", ["See calendar", "Local confirmation needed"], "Calendar icon"),
                ("Family gratitude", ["One thanks each"], "Gratitude circle"),
            ] + base[11:16]
        slides = []
        for i, (t, copy, comp) in enumerate(base[:count], 1):
            is_verse = "Primary verse" in t or "verse layer" in t.lower() or (i == 3 and not integration)
            src = f"{ref} — {url}" if is_verse or "Teaching meaning" in t or "Conclusion" in t else "week research + launch policy as applicable"
            if is_verse:
                copy = [ref, dev, iast, f"KUTUMBA teaching meaning: {meaning[:130]}", f"Source: {url}", "Not labeled as BBT translation"]
            slides.append(
                gamma_slide(
                    i, t.split(":")[0][:48], "master", f"Teach {code}: {t}",
                    copy, comp,
                    "plum philosophy / saffron bhakti / teal family",
                    "Title large; body 22–28pt; verse slide may reach ~100 words if readable",
                    "cinematic family or classical-inspired illustration",
                    f"Detailed 16:9 educational image for {code} '{t}': warm light, culturally respectful, no gore, no caricature, no temple logo, no embedded text, source-bound if scriptural",
                    "Follow composition; use week SVG where diagram slide",
                    src,
                    f"Do not import other weeks' full ontology. Block: {misconception}. {brand}",
                    "Ask one learner to restate conclusion",
                    donot, access,
                )
            )
        write(g / "V12-GAMMA-MASTER-DECK-PROMPT.md", f"# {code} V12 Gamma Master Deck\n\n**Status:** prompt-only — not rendered — not approved\n\n## Slides\n\n" + "\n".join(slides))

    # Audience decks — materially different
    for aud, fname, nslides, focus in [
        ("parent", "V12-GAMMA-PARENT-DECK-PROMPT.md", 12, "adult cases/saṅkalpa/speech ethics"),
        ("younger-K2", "V12-GAMMA-YOUNGER-DECK-PROMPT.md", 10, "story/movement/craft/memory"),
        ("older-4-5", "V12-GAMMA-OLDER-DECK-PROMPT.md", 12, "text observation/puzzle/scenario"),
    ]:
        slides = []
        for i in range(1, nslides + 1):
            if aud == "younger-K2":
                copy = [v.get("keywords", ["practice"])[0] if isinstance(v.get("keywords"), list) else "practice", "One idea", "Large picture"]
                words = "5–20 words"
                img = f"Gentle child-friendly illustration for {code} slide {i}, large shapes, calm faces, 16:9, no frightening content"
            elif aud == "parent":
                copy = [question if i == 1 else conclusion if i == 2 else f"Adult application point {i}", "No confession pressure"]
                words = "25–60 words"
                img = f"Realistic parent discussion scene for {code}, warm home, 16:9, no logos"
            else:
                copy = [question if i == 1 else f"Observation/puzzle step {i}", ref if i == 2 else conclusion]
                words = "15–40 words"
                img = f"Instructional older-child learning scene for {code}, notebooks, calm focus, 16:9"
            if i == 3 and aud != "younger-K2":
                copy = [ref, iast, f"Meaning: {meaning[:90]}"]
            slides.append(
                gamma_slide(
                    i, f"{aud} focus {i}", aud, focus,
                    copy, "Title top; content mid; footer source",
                    "teal/saffron by audience", words,
                    "age-appropriate visual", img, "none unless puzzle",
                    f"{ref} — {url}" if i <= 4 else "week packet",
                    f"{focus}. Block: {misconception}",
                    "One short response", donot, access,
                )
            )
        write(g / fname, f"# {code} V12 Gamma {aud} Deck\n\n**Status:** prompt-only — not rendered — not approved\n\n## Slides\n\n" + "\n".join(slides))

    write(
        g / "V12-GAMMA-SOURCE-MAP.yaml",
        f"""module: {code}
render_status: prompt-only-not-rendered
primary_verse: {ref}
primary_url: {url}
iast_present: true
devanagari_present: true
kutumba_teaching_meaning: true
brand: "KUTUMBA / Families Growing in Krishna Consciousness / Program Director: Swapnil Patil"
do_not_claim: [human-approved, publication-ready, gamma-rendered, bbt-translation-label]
""",
    )


def activities(code, slug, title, yng_core, old_core, puzzle, v):
    base = WEEKLY / slug / "activities"
    write(
        base / "CYCLE-ACTIVITY-VARIETY-MATRIX.md",
        f"""# {code} Activity Variety Row

| week | younger_core | older_core | puzzle_type | project_type | visual_type | duplicate_risk |
|---|---|---|---|---|---|---|
| {code} | {yng_core} | {old_core} | {puzzle} | cycle contribution | week-specific SVG | low if unique in cycle |
""",
    )
    memory = v["teaches"]
    write(
        base / "YOUNGER-ACTIVITY-PACK.md",
        f"""# {code} Younger Activity Pack (K–2)

## Objective
Show and say: **{memory}**

## Core activity — {yng_core}
1. Teacher demonstrates once.
2. Children participate for 5–8 minutes.
3. End with memory phrase echo.

## Story boundary
Paraphrase only from `research/DEVOTIONAL-AND-HISTORICAL-EXAMPLES.md`. No invented deity dialogue. No graphic violence.

## Movement
Freeze-and-Remember using this week's memory phrase.

## Craft / object
Week craft tied to {title}; take-home card with phrase inside.

## Printable
Color `../visuals/V12/line-art-younger.svg` (US Letter).

## Backup
Pass soft object; each child says one kind word; echo phrase.

## Materials
Printed line art, crayons, card stock, soft toss object.
""",
    )
    # Distinct older puzzles
    if puzzle == "crossword":
        older = f"""# {code} Older Activity Pack (Grades 4–5)

## Crossword (use letters)

Across
1. Eternal individual self (4)
3. Not the Supreme (3+3) hint: part
5. Primary reference for this week: {v['reference']}

Down
2. Relationship of jīva to Kṛṣṇa (7)
4. What we must not claim to be (3)

## Diagram task
Label `visuals/V12/concept-diagram.svg`.

## Scenario
Case 1 from research/CASE-STUDIES.md.

## Reflection
Did I confuse analogy with scripture?
"""
        key = f"""# {code} Older Answer Key

## Crossword
1. JIVA (or SOUL depending on grid — accept IAST jīva)
3. NOT GOD / PART
5. {v['reference']}
2. SERVICE
4. GOD (as Supreme)

## Secure responses
Conclusion: {v['teaches']}
Misconception blocked: claiming we are God.
"""
    elif puzzle == "word_search":
        older = f"""# {code} Older Activity Pack

## Word search (find and define)

TEMPORARY  LASTING  GRATITUDE  OFFERING  SHELTER  KRISHNA  HANKERING

Create 10×10 grid in print PDF; students circle words then write one sentence using three of them.

## Flow task
Draw temporary joy → fade → gratitude/offering → lasting shelter.

## Source observation
Open {v['url']} and paraphrase {v['reference']} in own words.
"""
        key = f"""# {code} Older Answer Key

Words: TEMPORARY, LASTING, GRATITUDE, OFFERING, SHELTER, KRISHNA, HANKERING
Secure paraphrase matches: {v['kutumba_teaching_meaning']}
Reject: 'science proves lasting shelter'.
"""
    elif puzzle == "time_budget":
        older = f"""# {code} Older Activity Pack

## Weekly time-budget challenge
Allocate 168 hours into Must / Should / Optional jars.
Must must include one protected spiritual practice block.

## Maze
Complete priority maze printable — path through distractions to protected hearing.

## Source
{v['reference']} — {v['url']}
"""
        key = f"""# {code} Older Answer Key

Secure: Must includes hearing/practice; Optional includes excess screens; no death-scare language.
Primary: {v['reference']}
"""
    else:
        older = f"""# {code} Older Activity Pack

## Core — {old_core}
Executable steps:
1. Read essential question.
2. Complete {puzzle} using week terms from verse pack.
3. Label concept diagram.
4. Respond to one constructed case.
5. Write reunification sentence.

## Source observation
Open {v['url']}. Write paraphrase of {v['reference']} (not long dump).

## Project
See `project/CYCLE-CONTRIBUTION.md`.
"""
        key = f"""# {code} Older Answer Key

Primary: {v['reference']}
Teaching meaning (secure paraphrase target): {v['kutumba_teaching_meaning']}
Conclusion: {v['teaches']}
Reject invented verse numbers and science-proves-metaphysics claims.
"""
    write(base / "OLDER-ACTIVITY-PACK.md", older)
    write(base / "OLDER-ANSWER-KEY.md", key)
    write(
        base / "PRINTABLES-README.md",
        f"""# {code} Printables

- Younger: `../visuals/V12/line-art-younger.svg` → PDF via V12 render
- Older: activity pack + answer key
- Verse card: `../visuals/V12/verse-card.svg`
- US Letter; branded footer; no private names
""",
    )


def teacher_guides(code, slug, title, question, conclusion, misconception, v):
    tdir = WEEKLY / slug / "teacher"
    ref, url = v["reference"], v["url"]
    write(
        tdir / "MAIN-FACILITATOR-GUIDE-V12.md",
        f"""# {code} Main Facilitator Guide — Saturday 2:00–4:00

**KUTUMBA • Families Growing in Krishna Consciousness**  
**Program Director: Swapnil Patil**  
**Status:** Internal founding-cohort teaching material — human/temple review EXTERNAL_OPEN

## Two-minute summary
{conclusion} Primary: **{ref}** ({url}).

## Essential question
{question}

## 15-minute night-before prep
1. Open {url}; reread Devanāgarī/IAST/teaching meaning from verse pack.
2. Rehearse opening script.
3. Pack younger + older materials.
4. Review misconception: {misconception}
5. Confirm snack/water (no weekly meal).

## 60-minute deep prep
1. Read research SCRIPTURAL + CASE files.
2. Mark three questions you will ask.
3. Prepare one analogy with limit.
4. Walk room zones.
5. Write minimum home-practice card.
6. Review deferral line.

## Exact primary readings
- {ref} — {url}
- Devanāgarī: {v['devanagari']}
- IAST: {v['iast']}
- KUTUMBA teaching meaning: {v['kutumba_teaching_meaning']}
- Rights: {v['rights_status']}

## One-page speaking map
Welcome → memory → verse layer → analogy+limit → case → tracks → reunification → project → home → next week

## Exact opening script
> Welcome. Today is {code}: {title}.  
> Essential question: {question}  
> From {ref}: {v['kutumba_teaching_meaning']}  
> We hear, practice in age bands, reunite, and take one small home step. We do not rank families.

## Core explanation
{conclusion}

## Analogies / cases / questions
Use week research ANALOGIES-AND-LIMITS and CASE-STUDIES. Ask discovery, understanding, and application questions. Likely adult Q: science proof? Answer: science may help habits; doctrine rests on śāstra.

## Common misconceptions
- {misconception}
- Confusing analogy with scripture
- Importing next week's ontology early

## Saturday time cues
1:50 arrival · 2:00 mantras · 2:10 opening · 2:30 tracks · 3:10 reunite · 3:30 snack · 3:40 saṅkalpa · 3:55 close · 4:00 end

## Do not claim
Human/temple/publication approval; BBT ownership of KUTUMBA materials; science proving ātman.
""",
    )
    write(
        tdir / "YOUNGER-TEACHER-GUIDE.md",
        f"""# {code} Younger Teacher Guide (K–2)

## Objective
{v['teaches']}

## Exact memory phrase
> {v['teaches']}

## Teacher background
Primary {ref}. Block: {misconception}

## Story script boundary
Paraphrase sourced example only. No invented dialogue. No gore.

## Wonder questions
1. What was new?
2. Whom can we serve?
3. When can we practice five minutes?

## Movement / hands-on / craft / coloring
See `activities/YOUNGER-ACTIVITY-PACK.md` and `visuals/V12/line-art-younger.svg`.

## Behavior redirects
Feet on floor · kind words · toy rests · quiet reset.

## Backup / materials / handoff
Backup in activity pack. Tell parent the memory phrase + home cue.
""",
    )
    write(
        tdir / "OLDER-TEACHER-GUIDE.md",
        f"""# {code} Older Teacher Guide (Grades 4–5)

## Objective
Explain: {conclusion} using {ref}.

## Text observation
Open {url}. Students write setting/key phrase/paraphrase/what it does not say.

## Diagram / puzzle / scenarios
Use V12 visuals and `activities/OLDER-ACTIVITY-PACK.md` + answer key.

## Misconception
{misconception}

## Project / reflection / extension
Cycle contribution; reflection on analogy vs scripture; reunification sentence.
""",
    )
    write(
        tdir / "PARENT-GUIDE.md",
        f"""# {code} Parent Guide

## Essential question
{question}

## Source
{ref} — teaching meaning: {v['kutumba_teaching_meaning']}

## Discussion
One realistic household tension; no compelled confession.

## Application
5–15 minute cue; minimum version counts.

## Privacy
No public scoring of sādhana.
""",
    )
    write(tdir / "PRE-WEEK-CHECKLIST.md", f"""# {code} Pre-Week Checklist\n\n- [ ] Objective clear\n- [ ] Primary URL opens\n- [ ] Verse layer printed\n- [ ] Misconception named: {misconception}\n- [ ] Younger materials\n- [ ] Older puzzle + key\n- [ ] Backup game\n- [ ] Home practice card\n""")


def visuals(code, slug, title, v):
    vdir = WEEKLY / slug / "visuals" / "V12"
    write(vdir / "concept-diagram.mmd", f"flowchart LR\n  A[{code}] --> B[{v['reference']}]\n  B --> C[{v['keywords'][0] if v.get('keywords') else 'practice'}]\n")
    write(
        vdir / "concept-diagram.svg",
        f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" role="img">
  <title>{code} concept</title>
  <rect width="800" height="420" fill="#FFF8E8"/>
  <text x="400" y="40" text-anchor="middle" font-size="20" fill="#5B1933">{code}: {title[:48]}</text>
  <rect x="80" y="120" width="200" height="80" rx="10" fill="#F4E4E8" stroke="#5B1933"/>
  <text x="180" y="165" text-anchor="middle" font-size="14">{v['reference']}</text>
  <rect x="320" y="120" width="200" height="80" rx="10" fill="#E4F0ED" stroke="#4F7C78"/>
  <text x="420" y="165" text-anchor="middle" font-size="12">{(v.get('keywords') or ['practice'])[0]}</text>
  <rect x="560" y="120" width="180" height="80" rx="10" fill="#F8E8BF" stroke="#E59B24"/>
  <text x="650" y="165" text-anchor="middle" font-size="12">apply</text>
  <text x="400" y="280" text-anchor="middle" font-size="14">{v['teaches'][:90]}</text>
  <text x="400" y="400" text-anchor="middle" font-size="10" fill="#666">KUTUMBA original · Program Director: Swapnil Patil · human review required</text>
</svg>
""",
    )
    write(
        vdir / "line-art-younger.svg",
        f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 612 792" role="img">
  <title>{code} younger line art</title>
  <rect width="612" height="792" fill="#fff"/>
  <text x="306" y="56" text-anchor="middle" font-size="18">{code} coloring</text>
  <circle cx="306" cy="320" r="120" fill="none" stroke="#000" stroke-width="3"/>
  <text x="306" y="520" text-anchor="middle" font-size="14">{v['teaches'][:70]}</text>
  <text x="306" y="760" text-anchor="middle" font-size="10">KUTUMBA · Families Growing in Krishna Consciousness</text>
</svg>
""",
    )
    write(
        vdir / "verse-card.svg",
        f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 612 792" role="img">
  <rect width="612" height="792" fill="#FFF8E8"/>
  <text x="306" y="80" text-anchor="middle" font-size="22" fill="#5B1933">{v['reference']}</text>
  <text x="40" y="160" font-size="16">{v['devanagari'][:80]}</text>
  <text x="40" y="260" font-size="14">{v['iast'][:90]}</text>
  <text x="40" y="360" font-size="14">{v['kutumba_teaching_meaning'][:120]}</text>
  <text x="40" y="700" font-size="10">{v['url']}</text>
  <text x="40" y="730" font-size="10">KUTUMBA teaching meaning — not labeled as BBT translation</text>
</svg>
""",
    )
    write(
        vdir / "IMAGE-GENERATION-PROMPTS.md",
        f"""# {code} Image Prompts

## Hero
Cinematic ultra-realistic family learning for {title}, warm light, 16:9, no logos, no embedded text.

## Scriptural (if used)
High-detail cinematic devotional illustration, not a photograph, source-bound to {v['reference']}, no gore, no invented actions.

## Negative
No caricature, no sensualization, no temple seal, no real child identities.
""",
    )
    write(
        vdir / "VISUAL-RIGHTS-REGISTER.yaml",
        f"""module: {code}
assets:
  - id: {code.lower()}-concept
    creator: KUTUMBA
    license_rights_status: kutumba-original
  - id: {code.lower()}-line-art
    creator: KUTUMBA
    license_rights_status: kutumba-original
""",
    )


def research_min(code, slug, v, conclusion, misconception):
    r = WEEKLY / slug / "research"
    # ensure SCRIPTURAL etc exist with primary
    write(
        r / "SCRIPTURAL-EXAMPLES.md",
        f"""# {code} Scriptural Examples

## Primary anchor
| Reference | URL | Teaching paraphrase | Limitation |
|---|---|---|---|
| {v['reference']} | {v['url']} | {v['kutumba_teaching_meaning']} | No full purport dump; teaching meaning ≠ BBT translation label |

## Classroom use
Open URL; state teaching meaning; name scope boundary: {v['scope_boundary']}
""",
    )
    if not (r / "CASE-STUDIES.md").exists() or len((r / "CASE-STUDIES.md").read_text(encoding="utf-8", errors="ignore")) < 400:
        write(
            r / "CASE-STUDIES.md",
            f"""# {code} Case Studies

### Constructed case 1 — fictional
- Situation: Family struggles to apply {v['reference']}
- Mistaken conclusion: {misconception}
- Principle: {conclusion}
- Compassionate response: Acknowledge effort; one small cue
- Family action: 5–15 minute practice
- What not to say: ranking, threats, public exposure
""",
        )
    if not (r / "ANALOGIES-AND-LIMITS.md").exists():
        write(r / "ANALOGIES-AND-LIMITS.md", f"# {code} Analogies\n\n| Analogy | Value | Limit |\n|---|---|---|\n| Week pedagogy analogy | Clarifies {v['keywords'][0] if v.get('keywords') else 'theme'} | Not a verse quotation |\n")
    if not (r / "SCIENCE-AND-APPLICATION.md").exists():
        write(r / "SCIENCE-AND-APPLICATION.md", f"# {code} Science\n\nEmpirical research may support pedagogy only. Never claim science proves ātman/karma/God. If unused this week, state N/A explicitly.\n")
    if not (r / "DEVOTIONAL-AND-HISTORICAL-EXAMPLES.md").exists():
        write(r / "DEVOTIONAL-AND-HISTORICAL-EXAMPLES.md", f"# {code} Devotional Examples\n\nUse only traceable VedaBase/authorised sources. If none selected, teach from primary verse + constructed cases.\n")


def project_files(code, slug, v, question, conclusion):
    p = WEEKLY / slug / "project"
    write(
        p / "CYCLE-CONTRIBUTION.md",
        f"""# {code} Cycle Contribution

## Cumulative project
Cycle project for this band — week layer for {code}.

## Essential question
{question}

## Artifact
One family artifact answering the question; ≤20 minutes optional burden.

## Primary
{v['reference']} — {v['url']}

## Boundaries
No ranking; no forced disclosure; distinguish paraphrase from analogy.
""",
    )
    write(
        p / "MODULE-PROJECT-BRIEF.md",
        f"""# {code} Module Project Brief

Objective: apply {conclusion}
Primary: {v['reference']}
Deliverable: week artifact for cycle folder
""",
    )
    write(
        p / "PRESENTATION-RUBRIC.md",
        f"""# {code} Presentation Rubric (Non-Competitive)

| Dimension | Emerging | Developing | Secure |
|---|---|---|---|
| Understanding | Vague | States conclusion | Connects to {v['reference']} |
| Application | None | One action | Cue + minimum |
| Teamwork | One speaker | Partial | Family roles |
| Source accuracy | Mixes weeks | In scope | Scripture vs analogy clear |
""",
    )


def materials(code, slug, title):
    write(
        WEEKLY / slug / "materials.md",
        f"""# {code} Materials — {title}

## Shared
- Opening mantras handout
- Verse card for this week
- Name tags optional
- Snack + water supplies (no weekly meal)

## Younger
- Line-art printable
- Crayons
- Craft card stock
- Soft toss object

## Older
- Activity pack printout
- Answer key (teacher only)
- Diagram printout
- Pencils

## Facilitator
- MAIN-FACILITATOR-GUIDE-V12
- Timer
- Run-of-show

Week-specific — do not reuse body/self materials outside C1-W2.
""",
    )
    write(
        WEEKLY / slug / "family-home-practice.md",
        f"""# {code} Family Home Practice

**5–15 minutes**

1. Say the memory/teaching line once.
2. Read the KUTUMBA teaching meaning for the primary verse (not a long purport).
3. One gratitude or service act.
4. Minimum version if tired: one sentence of thanks.

Saturday 2:00–4:00 remains the protected gathering; home practice is the daily/weekly cue.
""",
    )


def generate_week(row, verses):
    code, slug, title, question, conclusion, misconception, yng, old, puzzle = row
    v = verses[verse_key(code)]
    # fix C3-W5 url
    if code == "C3-W5":
        v["url"] = "https://vedabase.io/en/library/sb/7/5/23-24/"
    if code == "C3-W6":
        v["url"] = "https://vedabase.io/en/library/sb/7/5/23-24/"
    integration = code.endswith("W6")
    teacher_guides(code, slug, title, question, conclusion, misconception, v)
    activities(code, slug, title, yng, old, puzzle, v)
    visuals(code, slug, title, v)
    build_gamma(code, slug, title, question, conclusion, misconception, v, integration)
    research_min(code, slug, v, conclusion, misconception)
    project_files(code, slug, v, question, conclusion)
    materials(code, slug, title)
    # stub exports markdown sources for later DOCX
    exp = WEEKLY / slug / "exports"
    for name in ("FACILITATOR", "YOUNGER", "OLDER", "FAMILY"):
        src = {
            "FACILITATOR": WEEKLY / slug / "teacher" / "MAIN-FACILITATOR-GUIDE-V12.md",
            "YOUNGER": WEEKLY / slug / "teacher" / "YOUNGER-TEACHER-GUIDE.md",
            "OLDER": WEEKLY / slug / "teacher" / "OLDER-TEACHER-GUIDE.md",
            "FAMILY": WEEKLY / slug / "family-home-practice.md",
        }[name]
        write(exp / f"{code}-{name}-SOURCE.md", src.read_text(encoding="utf-8"))


def verse_packs(verses):
    for cycle, keys in [
        ("C1", [f"c1_w{i}" for i in range(1, 7)]),
        ("C2", [f"c2_w{i}" for i in range(1, 7)]),
        ("C3", [f"c3_w{i}" for i in range(1, 7)]),
    ]:
        blocks = []
        yblocks = []
        for k in keys:
            v = verses[k]
            if v["week"].endswith("W5") and cycle == "C3":
                v = dict(v)
                v["url"] = "https://vedabase.io/en/library/sb/7/5/23-24/"
            blocks.append(
                f"""## {v['week']} — {v['reference']}

- **Devanāgarī:** {v['devanagari']}
- **IAST:** {v['iast']}
- **KUTUMBA teaching meaning:** {v['kutumba_teaching_meaning']}
- **URL:** {v['url']}
- **Keywords:** {', '.join(v.get('keywords') or [])}
- **Teaches:** {v['teaches']}
- **Scope boundary:** {v['scope_boundary']}
- **Rights status:** {v['rights_status']}
"""
            )
            yblocks.append(
                {
                    "week": v["week"],
                    "reference": v["reference"],
                    "devanagari": v["devanagari"],
                    "iast": v["iast"],
                    "kutumba_teaching_meaning": v["kutumba_teaching_meaning"],
                    "url": v["url"],
                    "rights_status": v["rights_status"],
                }
            )
        write(LAUNCH / f"{cycle}-VERSE-PACK.md", f"# KUTUMBA {cycle} Verse Pack\n\n**Families Growing in Krishna Consciousness**\n**Program Director: Swapnil Patil**\n\n" + "\n".join(blocks))
        write(LAUNCH / f"{cycle}-VERSE-PACK.yaml", yaml.safe_dump(yblocks, allow_unicode=True, sort_keys=False))


def calendar():
    write(
        LAUNCH / "FIRST-SIX-MONTHS-CALENDAR.md",
        """# KUTUMBA First Six Months Calendar (V12)

**Saturday 2:00–4:00 PM locked**  
**Families Growing in Krishna Consciousness** · Program Director: Swapnil Patil

## Local confirmation note
Exact festival tithi/fasting details require local Vaiṣṇava-calendar confirmation (ISKCON Harrisburg and family temple). Dates below are planning candidates from cited ISKCON calendars — not ritual instructions for children.

## Cycle 1
| Date | Event |
|---|---|
| 2026-09-12 | C1-W1 |
| 2026-09-19 | C1-W2 |
| 2026-09-26 | C1-W3 |
| 2026-10-03 | C1-W4 |
| 2026-10-10 | C1-W5 |
| 2026-10-17 | C1-W6 |
| 2026-10-24 | Protected off week |
| 2026-10-31 | C1 Utsava / Kārtika-season family evening candidate |

Kārtika approx Oct 25–Nov 24, 2026 (example calendars).

## Cycle 2
| Date | Event |
|---|---|
| 2026-11-07 | C2-W1 |
| 2026-11-14 | C2-W2 |
| 2026-11-21 | C2-W3 |
| 2026-11-28 | C2-W4 (Thanksgiving-weekend attendance risk — owner confirm) |
| 2026-12-05 | C2-W5 |
| 2026-12-12 | C2-W6 |
| 2026-12-19 | Gītā Jayantī family Utsava candidate (official date often Dec 20, 2026) |
| 2026-12-26 | Winter break |
| 2027-01-02 | Winter break |

## Cycle 3
| Date | Event |
|---|---|
| 2027-01-09 | C3-W1 |
| 2027-01-16 | C3-W2 |
| 2027-01-23 | C3-W3 |
| 2027-01-30 | C3-W4 |
| 2027-02-06 | C3-W5 |
| 2027-02-13 | C3-W6 |
| 2027-02-20 | Nityānanda weekend Utsava candidate (official often Feb 19, 2027) |
| 2027-02-27 | Protected off / six-month reflection / makeup |
| 2027-03-06 | Optional six-month Mela / buffer |

## Lookahead
Gaura Pūrṇimā — Mar 22, 2027 — do not distort C3 to force-fit; create optional temple attendance plan.

## Rules
- Do not erase core curriculum for festivals.
- No child fasting instructions unless formally approved.
- Missed concepts are reviewed before advancing.
""",
    )
    # simple ICS
    ics = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//KUTUMBA//First Six Months//EN",
    ]
    events = [
        ("20260912", "C1-W1"),
        ("20260919", "C1-W2"),
        ("20260926", "C1-W3"),
        ("20261003", "C1-W4"),
        ("20261010", "C1-W5"),
        ("20261017", "C1-W6"),
        ("20261024", "C1 Off Week"),
        ("20261031", "C1 Utsava candidate"),
        ("20261107", "C2-W1"),
        ("20261114", "C2-W2"),
        ("20261121", "C2-W3"),
        ("20261128", "C2-W4"),
        ("20261205", "C2-W5"),
        ("20261212", "C2-W6"),
        ("20261219", "Gita Jayanti Utsava candidate"),
        ("20261226", "Winter break"),
        ("20270102", "Winter break"),
        ("20270109", "C3-W1"),
        ("20270116", "C3-W2"),
        ("20270123", "C3-W3"),
        ("20270130", "C3-W4"),
        ("20270206", "C3-W5"),
        ("20270213", "C3-W6"),
        ("20270220", "Nityananda Utsava candidate"),
        ("20270227", "Six-month reflection"),
    ]
    for d, name in events:
        ics += [
            "BEGIN:VEVENT",
            f"DTSTART;TZID=America/New_York:{d}T140000",
            f"DTEND;TZID=America/New_York:{d}T160000",
            f"SUMMARY:KUTUMBA {name}",
            "DESCRIPTION:Saturday 2-4 founding cohort. Local festival confirmation may apply.",
            "END:VEVENT",
        ]
    ics.append("END:VCALENDAR")
    write(LAUNCH / "FIRST-SIX-MONTHS-CALENDAR.ics", "\n".join(ics))


def navigation_and_rights():
    write(
        REPO / "V12-START-HERE.md",
        """# V12 START HERE — Owner Saturday Path

**KUTUMBA · Families Growing in Krishna Consciousness**  
**Program Director: Swapnil Patil**

## THIS SATURDAY (C1-W1 default)

| Action | Open |
|---|---|
| PRINT THIS | `exports/final/KUTUMBA-C1-W1-SATURDAY-PRINT-PACKET-V12.pdf` |
| READ THIS | `11-weekly-program-library/first-six-months/c1-w1-what-is-kutumba-and-why-are-we-here/teacher/MAIN-FACILITATOR-GUIDE-V12.md` |
| GIVE YOUNGER TEACHER | same week `teacher/YOUNGER-TEACHER-GUIDE.md` + activities |
| GIVE OLDER TEACHER | `teacher/OLDER-TEACHER-GUIDE.md` + activities + answer key |
| USE THIS GAMMA PROMPT | same week `gamma/V12-GAMMA-MASTER-DECK-PROMPT.md` |
| KEEP THIS OWNER PACK | `exports/final/KUTUMBA-C1-OWNER-PACKET-V12.pdf` |

## NEXT SIX WEEKS
See `launch/FIRST-SIX-MONTHS-CALENDAR.md` Cycle 1 dates.

## FIRST SIX MONTHS
C1 → off → Utsava → C2 → Gītā Jayantī/winter → C3 → Nityānanda/reflection.

## CLASSIFICATION
PRINT / READ / GIVE / GAMMA / INTERNAL — see `exports/final/README.md`.

## INTERNAL REFERENCE
Research, audits, historical packs — not required Friday night.

Human/temple approvals remain EXTERNAL_OPEN. Do not treat this file as publication approval.
""",
    )
    write(
        REPO / "RIGHTS-AND-ATTRIBUTION.md",
        """# Rights and Attribution

KUTUMBA is an original family-formation program framework prepared and directed by Swapnil Patil for the founding cohort. Original KUTUMBA lesson structures, original activities, original diagrams, original case studies and original program-design materials are identified as KUTUMBA-created material. Scriptural texts, Śrīla Prabhupāda's works, BBT text/artwork, ISKCON names/marks, third-party educational resources and externally sourced images remain the property or responsibility of their respective rights holders. KUTUMBA attribution does not transfer ownership of those materials and does not imply official ISKCON/GBC endorsement.
""",
    )
    write(
        REPO / "17-reviews-and-audits" / "BBT-RIGHTS-AND-ATTRIBUTION-NOTE.md",
        """# BBT Rights and Attribution Note (V12)

Public repository policy (see BBT permissions https://bbt.org/node/40):

| Item | Usage | Exact BBT English copied? | Art? | Permission basis | Credit | Scope | Review |
|---|---|---|---|---|---|---|---|
| Sanskrit verse text | Display + teaching | No (Sanskrit layer + KUTUMBA meaning) | No | Public VedaBase display + original paraphrase | Cite VedaBase URL | Public repo teaching | EXTERNAL_OPEN if larger BBT excerpts needed |
| Full purports | Not included | No | No | Omitted | — | — | — |
| BBT artwork | Not distributed | — | No | Unknown rights omitted | — | — | — |

KUTUMBA does not claim GBC-authorized blanket incidental-use status unless that status is established.
""",
    )
    write(
        EXPORTS / "README.md",
        """# Final exports classification

| File pattern | Class |
|---|---|
| *-PRINT-PACKET-V12.pdf | PRINT |
| *-OWNER-PACKET-V12.pdf | READ |
| *-TEACHER-PACKET-V12.pdf | READ/GIVE |
| *-VERSE-PACK* | PRINT/READ |
| Gamma prompts in week folders | GAMMA |
| build-evidence/* | INTERNAL |
""",
    )


def cycle_activity_matrix():
    rows = ["week,younger_core,older_core,puzzle_type,project_type,visual_type,duplicate_risk"]
    for row in WEEKS:
        code, slug, title, q, c, m, yng, old, puzzle = row
        rows.append(f"{code},{yng},{old},{puzzle},cycle_contribution,week_svg,low")
    write(WEEKLY / "CYCLE-ACTIVITY-VARIETY-MATRIX.md", "# Cycle Activity Variety Matrix\n\n```csv\n" + "\n".join(rows) + "\n```\n")


def opening_mantras():
    write(
        LAUNCH / "OPENING-MANTRAS-HANDOUT.md",
        """# Opening Mantras Handout — V12

**KUTUMBA · Families Growing in Krishna Consciousness**  
**Program Director: Swapnil Patil**

## 1. Śrīla Prabhupāda Praṇāma

> nama oṁ viṣṇu-pādāya kṛṣṇa-preṣṭhāya bhū-tale  
> śrīmate bhaktivedānta-svāmin iti nāmine  
> namas te sārasvate deve gaura-vāṇī-pracāriṇe  
> nirviśeṣa-śūnyavādi-pāścātya-deśa-tāriṇe

**Direct sources (verify chanting sheet locally):**
- https://vedabase.io/en/library/transcripts/690110in-los-angeles/
- https://vedabase.io/en/library/transcripts/690413sb-new-york/

**KUTUMBA plain meaning:** We offer respects to Śrīla Prabhupāda, dear to Kṛṣṇa, who carries Lord Caitanya's message.

## 2. Pañca-tattva Mantra

> (jaya) śrī-kṛṣṇa-caitanya prabhu-nityānanda  
> śrī-advaita gadādhara śrīvāsādi-gaura-bhakta-vṛnda

**Source:** https://vedabase.io/en/library/cc/adi/7/4/  
Also see transcript context: https://vedabase.io/en/library/transcripts/710328bg-bombay/

## 3. Hare Kṛṣṇa Mahā-mantra

> Hare Kṛṣṇa Hare Kṛṣṇa Kṛṣṇa Kṛṣṇa Hare Hare  
> Hare Rāma Hare Rāma Rāma Rāma Hare Hare

**Source:** use authorised chanting practice + transcript context above. Invitation only — never forced volume or punishment.

Rights: do not invent extra prayers; temple sheet is exact-text control where required.
""",
    )


def main() -> int:
    verses = load_verses()
    # URL fixes
    verses["c3_w5"]["url"] = "https://vedabase.io/en/library/sb/7/5/23-24/"
    verses["c3_w6"]["url"] = "https://vedabase.io/en/library/sb/7/5/23-24/"
    for row in WEEKS:
        generate_week(row, verses)
        print("generated", row[0])
    verse_packs(verses)
    calendar()
    navigation_and_rights()
    cycle_activity_matrix()
    opening_mantras()
    print("V12 production generation complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

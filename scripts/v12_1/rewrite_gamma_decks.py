#!/usr/bin/env python3
"""Rewrite all V12 Gamma deck prompts without truncation or generic placeholders."""
from __future__ import annotations

import re
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
VERSE = yaml.safe_load((REPO / "scripts" / "v12" / "verse_data.yaml").read_text(encoding="utf-8"))

WEEKS = [
    ("C1-W1", "c1-w1-what-is-kutumba-and-why-are-we-here", "c1_w1"),
    ("C1-W2", "c1-w2-i-am-not-this-body", "c1_w2"),
    ("C1-W3", "c1-w3-the-nature-of-the-soul", "c1_w3"),
    ("C1-W4", "c1-w4-why-human-life-is-rare-and-valuable", "c1_w4"),
    ("C1-W5", "c1-w5-the-temporary-world-and-the-search-for-permanent-happiness", "c1_w5"),
    ("C1-W6", "c1-w6-integration-night-who-am-i-and-how-should-our-family-live", "c1_w6"),
    ("C2-W1", "c2-w1-action-and-reaction-how-karma-binds", "c2_w1"),
    ("C2-W2", "c2-w2-free-will-and-responsibility-the-next-choice-matters", "c2_w2"),
    ("C2-W3", "c2-w3-birth-death-and-reincarnation", "c2_w3"),
    ("C2-W4", "c2-w4-the-three-modes-of-material-nature", "c2_w4"),
    ("C2-W5", "c2-w5-māyā-decorating-the-prison-cell", "c2_w5"),
    ("C2-W6", "c2-w6-integration-night-choice-consequence-and-the-modes", "c2_w6"),
    ("C3-W1", "c3-w1-who-is-god-the-supreme-enjoyer-proprietor-and-friend", "c3_w1"),
    ("C3-W2", "c3-w2-who-is-kṛṣṇa-the-supreme-personality-of-godhead", "c3_w2"),
    ("C3-W3", "c3-w3-guru-sādhu-and-śāstra-how-we-receive-spiritual-knowledge", "c3_w3"),
    ("C3-W4", "c3-w4-śrī-caitanya-mahāprabhu-and-the-holy-name", "c3_w4"),
    ("C3-W5", "c3-w5-the-nine-processes-of-bhakti", "c3_w5"),
    ("C3-W6", "c3-w6-bhakti-mela-kīrtana-drama-and-family-presentation", "c3_w6"),
]

SUFFIX = (
    "Negative constraints: no gore, no caricature, no temple logo, no embedded readable text, "
    "no invented deity pastimes, no identifiable real persons."
)


def slide(
    n: int,
    title: str,
    audience: str,
    objective: str,
    copy: list[str],
    layout: str,
    palette: str,
    typography: str,
    visual_type: str,
    image: str,
    source: str,
    presenter: str,
    interaction: str,
    do_not: str,
) -> str:
    bullets = "\n".join(f"  - {c}" for c in copy)
    return f"""
### Slide {n} — {title}
- **Audience:** {audience}
- **Objective:** {objective}
- **Copy:**
{bullets}
- **Layout:** {layout}
- **Palette role:** {palette}
- **Typography:** {typography}
- **Visual type:** {visual_type}
- **Image prompt:** {image} {SUFFIX}
- **Presenter note:** {presenter}
- **Interaction:** {interaction}
- **Do not claim:** {do_not}
- **Accessibility:** Large type; high contrast; read Devanāgarī/IAST aloud; alt-text for images
"""


def scene(code: str, title: str, detail: str) -> str:
    return (
        f"16:9 instructional scene for {code} '{title}': {detail}; "
        f"warm Pennsylvania living-room classroom; South Asian family learners generically represented; "
        f"soft afternoon window light; cream-saffron-teal accents; medium-wide composition."
    )


def master_deck(code: str, slug: str, v: dict) -> str:
    ref = v["reference"]
    url = v["url"]
    meaning = v["kutumba_teaching_meaning"]
    iast = v["iast"]
    dev = v.get("devanagari", "")
    teaches = v.get("teaches", code)
    boundary = v.get("scope_boundary", "Stay within this week's primary.")
    integration = code.endswith("-W6")
    title = teaches

    slides = []
    slides.append(
        slide(
            1,
            f"Title — {code}",
            "master",
            f"Open {code}",
            [title, "KUTUMBA · Families Growing in Krishna Consciousness", "Saturday 2:00–4:00 · parents onsite"],
            "Top title; soft hero family illustration",
            "plum title / cream ground",
            "Title 40–48pt; subtitle 22pt",
            "cinematic family welcome",
            scene(code, "welcome", "families arriving with notebooks; calm welcome circle"),
            f"{ref} — {url}",
            "Welcome warmly; state Saturday purpose; no ranking language.",
            "One welcome echo",
            "Do not claim temple approval or BBT ownership of KUTUMBA materials",
        )
    )
    slides.append(
        slide(
            2,
            "Essential focus",
            "master",
            "Frame the week",
            [teaches, f"Primary: {ref}", boundary],
            "Large focus line; secondary source line",
            "teal accent bar",
            "Focus 32pt",
            "simple focus card",
            scene(code, "focus", f"facilitator pointing to verse card for {ref}"),
            f"{ref} — {url}",
            "Read the focus once; invite one parent paraphrase later.",
            "Thumbs-up if clear",
            "Do not import other weeks' full ontology",
        )
    )
    slides.append(
        slide(
            3,
            f"Primary verse — {ref}",
            "master",
            "Present the primary",
            [
                ref,
                f"Devanāgarī: {dev}" if dev and not dev.startswith("(") else "See verse pack for Devanāgarī",
                f"IAST: {iast}",
                f"KUTUMBA teaching meaning: {meaning}",
                f"Source: {url}",
                "Not labeled as BBT translation",
            ],
            "Left 58% verse text; right 42% illustration",
            "plum philosophy panel",
            "Verse readable; meaning may wrap across bullets if needed — never truncate mid-sentence",
            "verse + illustration",
            scene(code, "verse", "open śāstra page beside blank notebook; respectful study posture"),
            f"{ref} — {url}",
            "Read IAST slowly; then teaching meaning; pause.",
            "One child repeats a short memory line",
            "Do not dump full purport text on slide",
        )
    )
    slides.append(
        slide(
            4,
            "Teaching meaning",
            "master",
            "Lock the conclusion",
            [meaning, f"This week teaches: {teaches}"],
            "Key-idea callout panel",
            "saffron key-idea",
            "Body 24–28pt",
            "callout panel",
            scene(code, "meaning", "family listening; one sentence on a whiteboard area without readable text"),
            f"{ref} — {url}",
            "Ask: what is the one sentence we take home?",
            "Pair share 20 seconds",
            "Do not invent dialogue for scriptural persons",
        )
    )
    slides.append(
        slide(
            5,
            "Context map",
            "master",
            "Place the week",
            [
                f"Week: {code}",
                f"Focus: {teaches}",
                f"Primary source: {ref}",
                f"Boundary: {boundary}",
            ],
            "Three-column context map",
            "teal family ops",
            "Labels 18–22pt",
            "diagram",
            scene(code, "context", "three soft cards on a table: hear / understand / apply"),
            f"teacher/MAIN-FACILITATOR-GUIDE-V12.md · {ref} — {url}",
            "Keep scope tight; defer out-of-scope questions.",
            "Show of hands: ready for analogy",
            "Do not claim this slide replaces śāstra study",
        )
    )
    slides.append(
        slide(
            6,
            "Analogy with limit",
            "master",
            "Clarify with pedagogy",
            [
                "Use one week-specific analogy from the facilitator guide",
                "State the helpful point",
                "State the failure point / limit",
                "Analogy is pedagogy — not a verse quotation",
            ],
            "Analogy diagram with warning label",
            "saffron / maroon limit tag",
            "Body 22pt",
            "diagram",
            scene(code, "analogy", "simple object metaphor on table with a small caution tag prop"),
            "research/ANALOGIES-AND-LIMITS.md (pedagogy; not a verse quotation)",
            "Name the limit out loud so children hear the boundary.",
            "Ask: what would be a wrong use of this analogy?",
            "Do not treat analogy as śāstra",
        )
    )
    slides.append(
        slide(
            7,
            "Constructed family case",
            "master",
            "Apply compassionately",
            [
                "Use one constructed household case from the facilitator guide",
                "Name the mistaken conclusion",
                "Return to the primary principle",
                "Compassionate action + what not to say",
            ],
            "Anonymous vignette layout",
            "teal case panel",
            "Body 22pt",
            "vignette illustration",
            scene(code, "case", "anonymous family conversation at kitchen table; calm faces; no shame posture"),
            "research/CASE-STUDIES.md (constructed teaching cases)",
            "Protect privacy; cases are fictional teaching tools.",
            "Parents: one sentence of better response",
            "Do not pressure real confessions",
        )
    )
    slides.append(
        slide(
            8,
            "Misconception check",
            "master",
            "Block common error",
            [
                f"Scope boundary: {boundary}",
                "Name the likely misconception from the facilitator guide",
                "Offer the better, source-bound statement",
            ],
            "Myth vs truth two panels",
            "maroon caution / teal truth",
            "Body 22pt",
            "two-panel comparison",
            scene(code, "misconception", "two cards on easel: unclear claim vs clearer claim; no readable text"),
            f"{ref} — {url} · research/MISCONCEPTIONS-AND-BOUNDARIES.md",
            "Correct gently; never embarrass a child or guest.",
            "True/false with hands",
            "Do not speculate beyond sources",
        )
    )
    slides.append(
        slide(
            9,
            "Activity preview",
            "master",
            "Preview tracks",
            [
                "K–2: story + movement + craft from younger teacher guide",
                "Grades 4–5: text observation + puzzle/scenario from older teacher guide",
                "Reunite for family synthesis",
            ],
            "Two-path preview then reunite",
            "saffron younger / teal older",
            "Body 22pt",
            "age-band icons",
            scene(code, "activities", "split room: floor craft mats left; table worksheets right"),
            "teacher/YOUNGER-TEACHER-GUIDE.md · teacher/OLDER-TEACHER-GUIDE.md",
            "Teachers already know run sheets; this is orientation only.",
            "Children point to their track",
            "Do not skip reunification",
        )
    )
    slides.append(
        slide(
            10,
            "Home practice",
            "master",
            "Send a doable practice",
            [
                "5–15 minute family practice",
                "Write action + cue + minimum version on saṅkalpa card",
                "Minimum version counts as success",
            ],
            "Checklist close",
            "plum home panel",
            "Body 22pt",
            "home practice scene",
            scene(code, "home practice", "kitchen-table family with a blank practice card; lamp light"),
            "family-home-practice.md · launch/FAMILY-COVENANT.md",
            "No confession pressure; invite, do not force volume.",
            "Families show blank card ready",
            "Do not score private sādhana publicly",
        )
    )
    if integration:
        slides.append(
            slide(
                11,
                "Review chain",
                "master",
                "Retrieve prior weeks",
                [iast, "Retrieval not ranking", "Family presentation without competitive scoring"],
                "Horizontal chain diagram",
                "plum review",
                "Body 20–24pt",
                "chain diagram",
                scene(code, "review chain", "five linked beads or cards on a table representing prior weeks"),
                f"{ref} — {url} · launch verse packs",
                "Use exact primary references — no generic placeholders.",
                "Each family names one prior week learning",
                "Do not add major new doctrine on integration night",
            )
        )
    else:
        slides.append(
            slide(
                11,
                "Concept diagram",
                "master",
                "Show the week's map",
                [f"Use visuals/V12/concept-diagram.svg for {code}", teaches],
                "Full diagram panel",
                "teal diagram",
                "Labels large",
                "SVG diagram",
                scene(code, "diagram", "projected simple concept map matching week SVG shapes"),
                f"visuals/V12/concept-diagram.svg · {ref} — {url}",
                "Walk the diagram left to right once.",
                "Child points to one node",
                "Do not treat diagram as śāstra",
            )
        )
    slides.append(
        slide(
            12,
            "Close + next week",
            "master",
            "End on time",
            ["Appreciate effort", "End by 4:00", "Preview next week title only — do not teach it now"],
            "Closing circle",
            "saffron close",
            "Body 22pt",
            "closing circle",
            scene(code, "close", "families standing in a calm closing circle; soft smiles"),
            "launch/FIRST-SIX-MONTHS-CALENDAR.md",
            "Thank host home; leave spaces cleaner.",
            "One gratitude word",
            "Do not run late into family dinner time",
        )
    )

    header = f"""# {code} V12.1 Gamma Master Deck

**Status:** prompt-only — not rendered — not approved  
**Design system:** 16:9 · cream ground · plum/saffron/teal · charcoal text  
**Brand:** KUTUMBA · Families Growing in Krishna Consciousness · Program Director: Swapnil Patil

## Slides
"""
    return header + "\n".join(slides)


def audience_deck(code: str, v: dict, audience: str, n: int) -> str:
    ref = v["reference"]
    url = v["url"]
    meaning = v["kutumba_teaching_meaning"]
    iast = v["iast"]
    teaches = v.get("teaches", code)
    slides = []
    if audience == "parent":
        focuses = [
            ("Week for parents", [teaches, "No confession pressure", "Model one home cue"], "adults seated with children; calm discussion"),
            ("Primary takeaway", [meaning, f"Source: {ref}"], "parent reading verse card quietly"),
            ("Verse card", [ref, iast, f"KUTUMBA teaching meaning: {meaning}"], "close view of respectful study"),
            ("Speech ethics", ["Protect dignity", "No gossip", "Defer hard questions"], "two parents speaking kindly"),
            ("Household case", ["Use facilitator case", "Compassionate response", "What not to say"], "kitchen-table vignette"),
            ("Saṅkalpa", ["Action + cue + minimum", "Minimum = success"], "blank sankalpa card on table"),
            ("Sibling dynamics", ["No ranking children", "Help younger track"], "older child gently helping younger"),
            ("Devices", ["Away unless assigned", "Parents model"], "phones face-down in basket"),
            ("Host-home respect", ["Common areas", "Leave cleaner"], "doorway shoes/neat entry"),
            ("Privacy", ["No public scoring of sādhana"], "soft privacy lock motif without logos"),
            ("Questions later", ["Private channel OK", "No pressure now"], "facilitator available aside"),
            ("Close", ["End on time", "One appreciation"], "parents standing to leave calmly"),
        ]
    elif audience == "younger":
        focuses = [
            ("Hello friends", ["One idea today", "Kind bodies"], "K–2 circle on floor mats"),
            ("Story time", ["Listen for one idea", teaches], "storyteller with open hands; children seated"),
            ("Wonder", ["What did you notice?", "What might help?"], "child raising hand gently"),
            ("Movement", ["Follow freeze cue", "Safe feet"], "children freezing mid-movement smiling"),
            ("Craft", ["Hands help hearts remember"], "simple craft materials on low table"),
            ("Memory phrase", ["Short line from the week"], "child repeating a short phrase"),
            ("Kind words", ["No teasing", "Help friends"], "two children sharing crayons"),
            ("Clean up", ["Toys home", "Thank you"], "children putting crayons in bin"),
            ("Parent handoff", ["Show your craft", "One sentence"], "child showing craft to parent"),
            ("Smile close", ["You did enough"], "closing wave"),
        ]
    else:
        focuses = [
            ("Observe the text", [ref, "What words stand out?"], "grades 4–5 with notebooks"),
            ("Primary meaning", [f"KUTUMBA teaching meaning: {meaning}"], "student underlining on worksheet"),
            ("Verse layer", [ref, iast, meaning], "verse card beside pencil"),
            ("Puzzle / game", ["Use older activity pack steps"], "small-group puzzle pieces"),
            ("Scenario card", ["Choose a response", "Explain why"], "scenario cards on desk"),
            ("Diagram task", ["Label the week map"], "student labeling a blank diagram"),
            ("Project contribution", ["Add this week's layer"], "project folder with week tabs"),
            ("Reflection", ["One sentence I will practice"], "quiet writing time"),
            ("Extension", ["Optional deeper question"], "optional challenge card"),
            ("Source care", ["Scripture vs analogy", "No speculation"], "two-column notes"),
            ("Teamwork", ["Include every voice"], "small group taking turns"),
            ("Close", ["Ready to reunite"], "students stacking chairs neatly"),
        ][:n]

    for i, (title, copy, detail) in enumerate(focuses[:n], 1):
        src = f"{ref} — {url}" if i <= 3 else f"teacher guides · activities · {ref} — {url}"
        slides.append(
            slide(
                i,
                title,
                audience,
                f"{audience} learning for {code}",
                copy,
                "Title top; content mid; footer source",
                "teal/saffron by audience",
                "Age-appropriate body size",
                "age-appropriate visual",
                scene(code, title, detail),
                src,
                f"Keep {audience} tone. Block speculation. Brand: KUTUMBA.",
                "One quick check for understanding",
                "Do not claim BBT translation label for KUTUMBA teaching meaning",
            )
        )

    return f"""# {code} V12.1 Gamma {audience.title()} Deck

**Status:** prompt-only — not rendered — not approved

## Slides
""" + "\n".join(slides)


def main() -> None:
    for code, slug, key in WEEKS:
        v = VERSE[key]
        g = WEEKLY / slug / "gamma"
        g.mkdir(parents=True, exist_ok=True)
        (g / "V12-GAMMA-MASTER-DECK-PROMPT.md").write_text(master_deck(code, slug, v), encoding="utf-8")
        (g / "V12-GAMMA-PARENT-DECK-PROMPT.md").write_text(audience_deck(code, v, "parent", 12), encoding="utf-8")
        (g / "V12-GAMMA-YOUNGER-DECK-PROMPT.md").write_text(audience_deck(code, v, "younger", 10), encoding="utf-8")
        (g / "V12-GAMMA-OLDER-DECK-PROMPT.md").write_text(audience_deck(code, v, "older", 12), encoding="utf-8")
        print("rewrote gamma", code)
    print("done")


if __name__ == "__main__":
    main()

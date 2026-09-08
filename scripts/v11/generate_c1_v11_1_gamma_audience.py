#!/usr/bin/env python3
"""Expand audience Gamma decks + deepen launch handbooks for V11.1."""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
LAUNCH = REPO / "launch"

WEEKS = [
    (
        "C1-W1",
        "c1-w1-what-is-kutumba-and-why-are-we-here",
        "What Is KUTUMBA, and Why Are We Here?",
        "SB 1.2.18",
        "https://vedabase.io/en/library/sb/1/2/18/",
        "Why are we committing as a family?",
        "Protected weekly hearing plus home practice creates a path for family growth.",
        "Coming to the session without home practice is enough.",
        "Regular hearing and service to Śrīmad-Bhāgavatam steadies our family's devotion.",
    ),
    (
        "C1-W2",
        "c1-w2-i-am-not-this-body",
        "I Am Not This Body",
        "BG 2.13",
        "https://vedabase.io/en/library/bg/2/13/",
        "How should knowing I am not only this body change how we speak about bodies?",
        "Body changes; conscious self continues — care for the body without mistaking it for the self.",
        "Psychology or photos prove the soul.",
        "My body changes; I continue as the conscious self.",
    ),
    (
        "C1-W3",
        "c1-w3-the-nature-of-the-soul",
        "The Nature of the Soul",
        "BG 2.20",
        "https://vedabase.io/en/library/bg/2/20/",
        "If I am a soul, how should I live?",
        "The jīva is eternal, conscious, individual, minute, and related to Kṛṣṇa in service — not God Himself.",
        "All souls are God / we are the Supreme.",
        "I am an eternal soul — conscious, individual, and meant for Kṛṣṇa's service.",
    ),
    (
        "C1-W4",
        "c1-w4-why-human-life-is-rare-and-valuable",
        "Why Human Life Is Rare and Valuable",
        "SB 11.9.29",
        "https://vedabase.io/en/library/sb/11/9/29/",
        "What deserves protected family time?",
        "Human life gives a rare opportunity for deliberate self-realization — protect inquiry and practice time.",
        "Use fear or death-pressure to motivate children.",
        "Human life is a rare chance to ask who I am and serve Kṛṣṇa.",
    ),
    (
        "C1-W5",
        "c1-w5-the-temporary-world-and-the-search-for-permanent-happiness",
        "The Temporary World and the Search for Permanent Happiness",
        "BG 8.15",
        "https://vedabase.io/en/library/bg/8/15/",
        "How can enjoyment become gratitude and service?",
        "Temporary things can be used well but cannot provide permanent fulfillment.",
        "Material things and family affection are worthless.",
        "Temporary joys can be used with gratitude; lasting fulfillment is in Kṛṣṇa.",
    ),
    (
        "C1-W6",
        "c1-w6-integration-night-who-am-i-and-how-should-our-family-live",
        "Integration Night: Who Am I, and How Should Our Family Live?",
        "Cycle 1 chain (W5=BG 8.15)",
        "https://vedabase.io/en/library/bg/8/15/",
        "Can our family explain and apply what we learned?",
        "Identity, purpose, and practice must form one coherent family life.",
        "Competition or ranking of families.",
        "We remember who we are and how our family chooses to live.",
    ),
]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def slide_block(n, title, audience, purpose, bullets, notes, src, url, visual, prompt, interaction, donot):
    bl = "\n".join(f"  - {b}" for b in bullets)
    return f"""### Slide {n} — {title}

- **Audience:** {audience}
- **Purpose:** {purpose}
- **On-slide content:**
{bl}
- **Presenter notes:** {notes}
- **Primary source:** {src} — {url}
- **Suggested visual:** {visual}
- **Image/diagram prompt:** {prompt}
- **Interaction:** {interaction}
- **Do-not-claim:** {donot}
- **Accessibility note:** Large type; high contrast; read key lines aloud.
"""


def parent_deck(code, slug, title, src, url, q, conclusion, misconception, memory):
    slides = [
        ("Adult essential question", [q, "Write silently for 30 seconds"], "Invite honesty without confession pressure", "Parent circle quiet writing", f"Warm living-room scene for: {q}"),
        ("Primary verse for parents", [src, "Open URL before class", "Paraphrase only unless verified quote"], "Keep phone/browser ready with verse page", "Verse card with VedaBase URL", f"Clean verse-reference card for {src}"),
        ("Household implication", [conclusion, "Session + home cue both matter"], "Connect to Sunday dinner / bedtime cue", "Family calendar with protected block", "Family calendar highlighting one protected practice block"),
        ("Constructed case A", ["See research/CASE-STUDIES.md case 1", "Name mistaken conclusion", "Choose one compassionate action"], "Do not use real family names", "Anonymous household vignette illustration", "Instructional vignette: family at table, no faces identifiable"),
        ("Constructed case B", ["Case 2 from research pack", "What not to say", "Minimum version"], "Block shame language", "Speech ethics icons", "Icons: kind speech, private feedback, no ranking"),
        ("What not to say at home", ["No ranking children", "No spiritual threats", "No public exposure of private struggles"], "Model repair language", "Stop-sign teaching graphic (non-frightening)", "Calm stop-sign with kind words underneath"),
        ("Home practice 5–15 minutes", [f"Memory: {memory}", "Action + trigger + minimum version"], "Write saṅkalpa on card", "Saṅkalpa card mockup", "Printed saṅkalpa card with four fields"),
        ("Co-parent / caregiver cue planning", ["Who starts?", "What if one adult is away?", "Backup cue"], "Include grandparents/caregivers if relevant", "Two adults planning calendar", "Two caregivers pointing to same calendar cue"),
        ("Screens and time conflicts", ["Name one conflict honestly", "Trade optional for protected", "No perfectionism"], "Keep compassionate", "Phone face-down beside scripture book", "Phone face-down next to open book — no brand logos"),
        ("Project contribution this week", [f"Project layer for {code}", "≤20 minutes optional burden", "Keep artifact for W6"], "Point to project/CYCLE-CONTRIBUTION.md", "Project folder icon + week label", f"Simple project folder labeled {code}"),
        ("Privacy and no comparison", ["Private feedback route", "No sādhana scoring", "No gossip"], "Remind covenant", "Lock/privacy symbol instructional", "Simple lock icon with family silhouettes"),
        ("Closing commitment sentence", ["I will…", "Minimum version is success", "End on time Saturday"], "Collect one spoken sentence per family", "Closing circle", "Families standing in closing circle — instructional, not sacred art"),
    ]
    blocks = []
    for i, (t, bullets, notes, visual, prompt) in enumerate(slides, 1):
        blocks.append(
            slide_block(
                i,
                t,
                "parent",
                f"Adult application for {code}",
                bullets,
                notes + f" Block misconception: {misconception}",
                src,
                url,
                visual,
                prompt,
                "Ask one parent to restate the household implication",
                "Not human-approved; not publication-ready; Gamma not rendered; science ≠ siddhānta",
            )
        )
    write(
        WEEKLY / slug / "gamma" / "V11-GAMMA-PARENT-DECK-PROMPT.md",
        f"# {code} V11 Gamma Parent Deck Prompt\n\n**Status:** prompt-only — not rendered — not approved\n\n## Deck identity\n- {code} — {title}\n- Audience: parents/caregivers\n\n## Slides\n\n" + "\n".join(blocks),
    )


def younger_deck(code, slug, title, src, url, q, conclusion, misconception, memory):
    slides = [
        ("Picture welcome", ["Welcome friends", code, "Sit on your spot"], "Soft voice; name helpers", "Friendly classroom welcome art", f"Warm classroom welcome for {code}; no deity caricature"),
        ("Memory phrase", [memory, "Say with me", "Whisper version OK"], "Never force volume", "Large memory phrase card", f"Large readable card: {memory[:60]}"),
        ("Story picture", ["Story from sourced example", "Paraphrase only", "Kind ending"], "See DEVOTIONAL-AND-HISTORICAL-EXAMPLES.md", "Simple story illustration", f"Age-appropriate story scene for {title}"),
        ("Wonder question 1", ["What was new?", "Raise hand gently"], "Accept short answers", "Question-mark bubble", "Child raising hand with question bubble"),
        ("Wonder question 2", ["Who can we serve?", "Name one person"], "Keep concrete", "Helping hands drawing", "Two children offering help — line art style"),
        ("Freeze and Remember game", ["Walk gently", "Freeze!", "Finish the phrase"], "Two rounds only", "Freeze game cue card", "Children freeze mid-step; teacher holding phrase card"),
        ("Hands-on object", ["Touch the object", "This reminds me that…", conclusion[:70]], "One object at a time", "Week object photo-style illustration", f"Object lesson for {code}"),
        ("Craft card", ["Draw outside", "Phrase inside", "Take home"], "Help with folding", "Folded craft card", "Folded card craft with crayons"),
        ("Coloring sheet", ["Color today's picture", "Not a recycled W1 scene unless W1"], "Use week line-art SVG", "Coloring page preview", f"Coloring page unique to {code}"),
        ("Tell parents the phrase", [memory, "Cleanup", "Line up kindly"], "Handoff at door", "Parent-child handoff", "Child telling parent a short phrase at doorway"),
    ]
    blocks = []
    for i, (t, bullets, notes, visual, prompt) in enumerate(slides, 1):
        blocks.append(
            slide_block(
                i,
                t,
                "younger-K2",
                f"K–2 executable lesson for {code}",
                bullets,
                notes + f" Avoid adult debates; block: {misconception}",
                src,
                url,
                visual,
                prompt,
                "Echo memory phrase together",
                "Not approved; not rendered; invitation-only Sanskrit; no force",
            )
        )
    write(
        WEEKLY / slug / "gamma" / "V11-GAMMA-YOUNGER-DECK-PROMPT.md",
        f"# {code} V11 Gamma Younger Deck Prompt\n\n**Status:** prompt-only — not rendered — not approved\n\n## Deck identity\n- {code} — {title}\n- Audience: K–2\n\n## Slides\n\n" + "\n".join(blocks),
    )


def older_deck(code, slug, title, src, url, q, conclusion, misconception, memory):
    slides = [
        ("Essential question", [q, "Write one sentence"], "Silent write 60 seconds", "Question slide", f"Bold essential question typography: {q}"),
        ("Open primary text", [src, url, "Observe, then paraphrase"], "Devices/printouts ready", "Browser/verse page mock", f"Clean screenshot-style frame of {src} reference"),
        ("Observation prompts", ["Who speaks / setting?", "Key phrase?", "What it does not say"], "Collect 3 written notes", "Three prompt boxes", "Worksheet with three observation boxes"),
        ("Paraphrase vs quotation", ["Use own words", "No long dumps", "Cite reference"], "Model one paraphrase", "Paraphrase vs quote diagram", "Two columns: paraphrase / quotation"),
        ("Diagram labels", ["Complete week diagram", "Every node labeled", "One arrow for conclusion"], "Use V11 concept-diagram", "Week-specific diagram", f"Diagram unique to {code}, not generic growth loop unless W1"),
        ("Matching puzzle", ["Match term → meaning", "Use activity pack", "Check with answer key later"], "Cut strips or letter match", "Matching cards", f"Matching puzzle cards for {code}"),
        ("Scenario card work", ["Case from research", "Mistaken conclusion", "Better family action"], "Pairs of 2", "Scenario card", "Scenario card with family vignette"),
        ("Misconception check", [misconception, "Why it is wrong", "Better statement"], "No shaming wrong answers", "Myth vs truth", "Two panels: misconception / correction"),
        ("Project artifact", [f"{code} project layer", "Bring to reunification", "Keep for W6"], "Point to CYCLE-CONTRIBUTION", "Artifact checklist", "Checklist of project pieces"),
        ("Reflection", ["Did I confuse analogy with scripture?", "Circle one", "Honest answer"], "Private reflection OK", "Reflection prompt", "Reflection card with three circles"),
        ("Reunification sentence", ["One sentence to share", "No ranking", "Optional drawing-only"], "Practice once", "Share sentence template", "Template: This week we will…"),
        ("Home practice", [memory, "5–15 minutes", "Minimum version"], "Write cue on card", "Home practice card", "Home practice card with clock icon"),
    ]
    blocks = []
    for i, (t, bullets, notes, visual, prompt) in enumerate(slides, 1):
        blocks.append(
            slide_block(
                i,
                t,
                "older-4-5",
                f"Grades 4–5 text work for {code}",
                bullets,
                notes + f" Conclusion: {conclusion}",
                src,
                url,
                visual,
                prompt,
                "One student restates paraphrase",
                "Not approved; not rendered; science may illustrate habits only",
            )
        )
    write(
        WEEKLY / slug / "gamma" / "V11-GAMMA-OLDER-DECK-PROMPT.md",
        f"# {code} V11 Gamma Older Deck Prompt\n\n**Status:** prompt-only — not rendered — not approved\n\n## Deck identity\n- {code} — {title}\n- Audience: Grades 4–5\n\n## Slides\n\n" + "\n".join(blocks),
    )


def deepen_handbooks():
    write(
        LAUNCH / "KUTUMBA-C1-FAMILY-ORIENTATION.md",
        """# KUTUMBA Cycle 1 Family Orientation Handout

## 1. Welcome

KUTUMBA is a family-oriented Krishna consciousness formation program. Cycle 1 serves four founding families on Saturday **2:00–4:00 PM**. Parents remain onsite for the entire window. This is **not** a drop-off childcare program, not a substitute temple, and not an initiation or certification pathway.

We gather to protect weekly hearing, practice a small home rhythm, and grow respectful spiritual friendship. We end on time so families can leave peacefully.

## 2. What KUTUMBA is / is not

| KUTUMBA is | KUTUMBA is not |
|---|---|
| Protected weekly hearing + home practice | Social club only |
| Parent-onsite shared learning | Drop-off or babysitting |
| Respectful spiritual friendship | Ranking or public sādhana scoring |
| Voluntary family commitment | Initiation eligibility track |
| Age-banded teaching with reunification | Adult lecture while children are unmanaged |
| Source-checked teaching packets | Speculative theology inventing |

## 3. First six-month map

1. **Cycle 1 — Identity foundations** (six Saturdays): KUTUMBA purpose; body and self; nature of the soul; human opportunity; temporary vs lasting fulfillment; integration night.
2. **Cycle 2 — Karma and the modes**: action, responsibility, and material nature (after C1 readiness).
3. **Cycle 3 — Bhakti**: Kṛṣṇa, guru-sādhu-śāstra, holy name, nine processes.

If Cycle 1 understanding is weak, we **review or extend C1** before starting C2. Speed is not success.

## 4. Saturday schedule (locked)

| Time | Block |
|---|---|
| 1:50–2:00 | Arrival / settle |
| 2:00–2:10 | Opening mantras / short kīrtana |
| 2:10–2:30 | Shared family opening / Prem-kī-Kathā |
| 2:30–3:10 | Parallel parent + younger (K–2) + older (Grades 4–5) |
| 3:10–3:30 | Family reunification / bhakti lab |
| 3:30–3:40 | Child snack + water (**no weekly meal**) |
| 3:40–3:55 | Saṅkalpa / project / questions / next week |
| 3:55–4:00 | Closing |
| 4:00 | End on time |

## 5. Cycle rhythm: six weeks, off week, Utsava

- Six active Saturdays (see `launch/C1-SATURDAY-CALENDAR.md`).
- One protected off week for rest and home continuity.
- C1 Utsava / showcase candidate (calendar lists Oct 31, 2026 as candidate only — not confirmed festival).
- Presentations are **non-competitive**. Drawing-only options are allowed.

## 6. Expectations of participating families

1. Protect the Saturday calendar; communicate absences early.
2. Attempt a 5–15 minute home practice; minimum versions count as success.
3. Keep parents/caregivers onsite during the session.
4. Respect host-home property and common-area rules.
5. Follow child house rules; support the correction ladder without public shame.
6. Avoid gossip, comparison, and publishing private family/child data.
7. Bring questions privately when needed; do not demand speculative answers.

## 7. Home practice

Usually **5–15 minutes**. A typical week includes:

- memory phrase;
- one verse paraphrase (not a long purport dump);
- one gratitude or service act;
- optional project layer (keep burden low).

If the week is hard: do the **minimum version** written on your saṅkalpa card.

## 8. Family project — Who Am I, and How Should Our Family Live?

Each week adds a small layer. Week 6 is integration night: ~10 minutes per family to share understanding and application. Rubric dimensions: understanding, application, teamwork, source accuracy. **No ranking.**

## 9. Rules and correction

See `launch/CHILD-HOUSE-RULES.md` and `launch/FAMILY-COVENANT.md`.

Correction ladder: reminder → redirect → quiet reset → parent involvement → sit out an activity → private conversation. Never yell, shame, force chanting, or compare children.

## 10. Feedback and privacy

Use the private feedback route named by the owner. Do not post real child names, photos, medical details, or sādhana scores in shared chats or public repos. Photography/recording is off by default unless explicit host/owner policy says otherwise for a specific moment.

## 11. Reasonable six-month destination

By the end of the first six months, a reasonable destination is:

- stronger shared vocabulary;
- clearer identity foundations;
- a small sustainable home rhythm;
- age-appropriate explanation of key ideas;
- more respectful speech about bodies and others;
- warmer temple connection where available.

We do **not** promise certification, initiation eligibility, guaranteed advancement, or publication readiness.

## 12. FAQ

**Must both parents attend every week?** Aim for whole-family participation. Communicate constraints privately; do not invent attendance penalties.

**What if we miss a Saturday?** Tell the owner; receive the home-practice card; no public penalty.

**Are Gamma slide decks required?** No. Production prompts exist; decks are **not rendered** and **not approved**.

**Can teachers answer every hard question on the spot?** No. The no-speculation rule requires verifying from Śrīla Prabhupāda's books / the source packet.

**Is snack a meal?** No. Snack + water only; no weekly meal program.

**Will my family be ranked?** No.

## Closing line for families

> We protect hearing together, practice a little at home, and grow without comparison.
""",
    )

    write(
        LAUNCH / "KUTUMBA-C1-TEACHER-HANDBOOK.md",
        """# KUTUMBA Cycle 1 Teacher Handbook

## 1. Purpose of this handbook

This handbook helps lesson-ready teachers run Cycle 1 Saturday sessions without inventing doctrine. Use it with each week's `teacher/MAIN-FACILITATOR-GUIDE-V11.md`, age-band guides, research pack, and activity packs.

## 2. Source hierarchy

1. Śrīla Prabhupāda books / BBT VedaBase (primary).
2. Traceable lectures, letters, and conversations with stable URLs when used.
3. Authorised ISKCON materials with provenance.
4. Other sources only with clear provenance and limitation.
5. Academic research for pedagogy / habit / language application only — never as proof of ātman, karma, rebirth, or God.
6. Constructed household cases clearly labelled fictional / anonymized.

## 3. No-speculation rule

If unsure, say exactly:

> "I don't want to guess. I will verify that from Śrīla Prabhupāda's books / our source packet and come back to you."

Do not invent verse wording, purport claims, or deity dialogue.

## 4. Locked Cycle 1 primary anchors

| Week | Primary | URL |
|---|---|---|
| W1 | SB 1.2.18 | https://vedabase.io/en/library/sb/1/2/18/ |
| W2 | BG 2.13 | https://vedabase.io/en/library/bg/2/13/ |
| W3 | BG 2.20 | https://vedabase.io/en/library/bg/2/20/ |
| W4 | SB 11.9.29 | https://vedabase.io/en/library/sb/11/9/29/ |
| W5 | BG 8.15 | https://vedabase.io/en/library/bg/8/15/ |
| W6 | Review W1–W5 (represent W5 as BG 8.15) | chain links in research pack |

Supporting verses (example: BG 5.22 / BG 9.27 in W5) may help application but must not replace the locked primary.

## 5. Child-development expectations

### Younger (K–2)

- Short story with paraphrase boundary
- Movement game with freeze cue
- Hands-on object + craft + coloring
- Exact memory phrase
- Invitation-only Sanskrit exposure

### Older (Grades 4–5)

- Text observation with VedaBase URL
- Diagram labels
- Matching / worksheet with answer key
- Scenario cards
- Project artifact + reunification sentence

## 6. Correction ladder

1. Reminder  
2. Redirect  
3. Quiet reset in visible space  
4. Parent involvement  
5. Sit out the current activity  
6. Private conversation after session  

Never: shame, yell, force chanting, compare children, or publish private struggles.

## 7. Preparation standards

Night-before (15 minutes): open primary URL; rehearse opening; pack materials; review misconception; confirm snack/water plan.

Deep prep (60 minutes): read research SCRIPTURAL + CASE files; mark three questions; prepare one analogy with limit; walk room zones; write minimum home-practice card; review deferral line.

Use `launch/TEACHER-PRE-WEEK-CHECKLIST.md` and each week's `teacher/PRE-WEEK-CHECKLIST.md`.

## 8. Hard questions

Separate domains:

- **Śāstra claims** — taught as KUTUMBA paraphrase from primary sources.
- **Science** — may illuminate habits, attention, gratitude measures; never "proves the soul."
- **Pastoral / medical / safeguarding** — escalate; do not diagnose.

## 9. Stories, analogies, and science

- Stories need provenance (VedaBase / authorised source) or must be omitted.
- Analogies need teaching value + failure point.
- Science needs title, authors, year, DOI/URL, finding used, limitation, and application boundary.

## 10. Parent handoff

At reunification / door:

1. Memory phrase  
2. One home cue (time + place)  
3. Minimum version  

No public child evaluations. No ranking families.

## 11. Week-by-week checklist (every Saturday)

- [ ] Objective and essential question clear  
- [ ] Primary URL opens  
- [ ] Misconception named  
- [ ] Younger materials packed  
- [ ] Older worksheet + answer key packed  
- [ ] Backup low-prep game ready  
- [ ] Reunification synthesis planned  
- [ ] Project contribution named  
- [ ] Home practice card ready  
- [ ] End-on-time plan  

## 12. Short glossary

| Term | Meaning |
|---|---|
| Paraphrase | Our plain-English rendering of a verse meaning |
| Quotation | Exact verified wording only |
| Analogy | Teaching comparison with explicit limits |
| Constructed case | Fictional anonymized teaching story |
| Saṅkalpa | Specific practice intention (action + frequency + trigger + minimum) |
| Primary anchor | Locked verse for the week |
| Supporting verse | Helps application; not the locked primary |
| Prompt-only Gamma | Slide production prompt; not rendered; not approved |

## 13. Operating model reminders

- Saturday **2:00–4:00** only for this founding cohort  
- Parents onsite  
- Snack + water; **no weekly meal**  
- Four founding families  
- Two child bands: K–2 and Grades 4–5  
- Publication / pilot remain **NO GO** until human gates close  

## 14. Where to find week packets

Owner index: `11-weekly-program-library/first-six-months/C1-V11-OWNER-INDEX.md`

Each week folder contains `teacher/`, `research/`, `activities/`, `project/`, `gamma/`, `visuals/V11/`, and `exports/`.
""",
    )


def fix_source_chain():
    # W6 module project brief
    brief = WEEKLY / "c1-w6-integration-night-who-am-i-and-how-should-our-family-live" / "project" / "MODULE-PROJECT-BRIEF.md"
    if brief.exists():
        t = brief.read_text(encoding="utf-8")
        t = t.replace(
            "SB 1.2.18 · BG 2.13 · BG 2.20 · SB 11.9.29 · BG 5.22",
            "SB 1.2.18 · BG 2.13 · BG 2.20 · SB 11.9.29 · BG 8.15",
        )
        write(brief, t)

    for name in ("prem-ki-katha.md", "prem-ki-katha-short.md"):
        p = WEEKLY / "c1-w5-the-temporary-world-and-the-search-for-permanent-happiness" / name
        if not p.exists():
            continue
        t = p.read_text(encoding="utf-8")
        t = t.replace(
            "| BG 8.15 | [vedabase](https://vedabase.io/en/library/bg/8/15/) | Key verse |\n| BG 2.14 | [vedabase](https://vedabase.io/en/library/bg/2/14/) | Key verse |\n| BG 5.22 | [vedabase](https://vedabase.io/en/library/bg/5/22/) | Key verse |\n| BG 9.27 | [vedabase](https://vedabase.io/en/library/bg/9/27/) | Key verse |",
            "| BG 8.15 | [vedabase](https://vedabase.io/en/library/bg/8/15/) | Locked primary |\n| BG 2.14 | [vedabase](https://vedabase.io/en/library/bg/2/14/) | Supporting |\n| BG 5.22 | [vedabase](https://vedabase.io/en/library/bg/5/22/) | Supporting application |\n| BG 9.27 | [vedabase](https://vedabase.io/en/library/bg/9/27/) | Supporting offering mood |",
        )
        write(p, t)

    for rel in (
        "visuals/source/c1-w6-integration-verses.svg",
        "visuals/rendered/c1-w6-integration-verses.svg",
    ):
        p = WEEKLY / "c1-w6-integration-night-who-am-i-and-how-should-our-family-live" / rel
        if p.exists():
            t = p.read_text(encoding="utf-8")
            t = t.replace(
                "SB 1.2.18 · BG 2.13 · BG 2.20 · BG 2.40 · BG 5.22 — paraphrase review only",
                "SB 1.2.18 · BG 2.13 · BG 2.20 · SB 11.9.29 · BG 8.15 — paraphrase review only",
            )
            write(p, t)


def main() -> int:
    deepen_handbooks()
    fix_source_chain()
    for row in WEEKS:
        parent_deck(*row)
        younger_deck(*row)
        older_deck(*row)
    print("audience gamma + handbooks deepened")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

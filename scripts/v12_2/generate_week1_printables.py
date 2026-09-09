#!/usr/bin/env python3
"""Generate C1-W1 v12.2 printable Markdown sources."""
from __future__ import annotations

from pathlib import Path

W = Path(__file__).resolve().parents[2] / "11-weekly-program-library" / "first-six-months" / "c1-w1-what-is-kutumba-and-why-are-we-here"
FOOT = "\n\n---\nKUTUMBA · Families Growing in Krishna Consciousness · Program Director: Swapnil Patil · Internal founding cohort · EXTERNAL_OPEN human/temple gates\n"


def w(rel: str, body: str) -> None:
    path = W / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body.strip() + FOOT, encoding="utf-8")
    print(path.relative_to(W), path.stat().st_size)


def main() -> None:
    w(
        "activities/v12_2-younger/Y01-FOUR-CORNERS-SIGNS.md",
        """# Y01 — Four Corners Signs (print 4 pages or 2 duplex)

Cut on dashed lines. Post one sign per corner. Large type for K–2.

## HEAR
**We listen to Kṛṣṇa-kathā.**

`[ ear / book icon space ]`

--- cut ---

## CHANT
**We say Kṛṣṇa's names.**

`[ beads / music icon space ]`

--- cut ---

## SERVE
**We help with love.**

`[ helping-hands icon space ]`

--- cut ---

## RESPECT
**We use kind words and care.**

`[ heart / home icon space ]`
""",
    )
    cards = [
        ("The family listens to a Kṛṣṇa story.", "HEAR"),
        ("We sing Hare Kṛṣṇa together.", "CHANT"),
        ("You help put the activity supplies away.", "SERVE"),
        ("You ask before touching a friend's toy.", "RESPECT"),
        ("You sit quietly while another child answers.", "RESPECT"),
        ("You help bring scripture to the family reading place.", "SERVE"),
        ("You repeat the memory line with the teacher.", "HEAR"),
        ("You join the mahā-mantra softly.", "CHANT"),
        ("You help a younger child find crayons.", "SERVE"),
        ("You keep feet on the floor in the host home.", "RESPECT"),
        ("You listen when a parent reads one verse.", "HEAR"),
        ("Your family chants three mahā-mantras at home.", "CHANT"),
    ]
    card_lines = ["# Y02 — Four Corners Scenario Cards", "", "Print, cut on dashed lines. One scenario per card.", ""]
    for i, (text, ans) in enumerate(cards, 1):
        card_lines += [f"## Card {i}", text, "", "--- cut ---", ""]
    card_lines += ["## Teacher answer key (do not give to children)", ""]
    for i, (_, ans) in enumerate(cards, 1):
        card_lines.append(f"{i}. {ans}")
    w("activities/v12_2-younger/Y02-FOUR-CORNERS-SCENARIO-CARDS.md", "\n".join(card_lines))

    w(
        "activities/v12_2-younger/Y03-BHAKTI-GARDEN-CRAFT.md",
        """# Y03 — Bhakti Garden Craft (one page)

Color the petals. Large crayon areas.

```
              [ HEAR ]
         ________________
        /                \\
 [CHANT]   OUR FAMILY     [SERVE]
        \\  helps one     /
         \\ another      /
          \\ remember   /
           \\ Kṛṣṇa.  /
            \\______/
             [RESPECT]
```

**Center sentence:** Our family helps one another remember Kṛṣṇa.

**This week our family will grow:** _______________________________

☐ We will try our tiny home practice at least once.
""",
    )
    w(
        "activities/v12_2-younger/Y04-MEMORY-BADGE-BOOKMARK.md",
        """# Y04 — Memory Badge / Bookmark

Cut on outer dashed line. Optional hole punch + yarn.

```
+----------------------------------+
|  WE HELP EACH OTHER              |
|  REMEMBER KṚṢṆA                  |
|                                  |
|  [Hear] [Chant] [Serve] [Respect]|
+----------------------------------+
```
""",
    )
    w(
        "activities/v12_2-younger/Y05-HOUSE-RULE-PICTURE-SORT.md",
        """# Y05 — House-Rule Picture Sort

Cut cards. Sort into **SAFE** or **NEEDS RESET** (no shame language).

1. Feet on the floor while listening.  
2. Jumping on the host couch.  
3. Asking before borrowing crayons.  
4. Throwing a block indoors.  
5. Helping clean crayons into the bin.  
6. Running into a private bedroom without asking.  
7. Using kind words when waiting for a turn.  
8. Teasing a friend about a wrong answer.

## Teacher key
SAFE: 1, 3, 5, 7  
NEEDS RESET: 2, 4, 6, 8
""",
    )

    w(
        "activities/v12_2-older/O01-SB-1-2-18-OBSERVATION.md",
        """# O01 — ŚB 1.2.18 Observation Sheet

**Source:** https://vedabase.io/en/library/sb/1/2/18/  
**IAST:** naṣṭa-prāyeṣv abhadreṣu nityaṁ bhāgavata-sevayā / bhagavaty uttama-śloke bhaktir bhavati naiṣṭhikī  
**KUTUMBA teaching meaning:** When we regularly hear and serve the Bhāgavata (book and devotee association), troubles in the heart are cleared and steady devotion to the Lord becomes established.

1. Repeated practice words I notice: _______________________________
2. What result is described? _______________________________________
3. Why might “regular” (nityaṁ) matter for a family? ________________
4. One question for the facilitator: _______________________________
""",
    )
    is_cards = [
        "family formation",
        "supports temple life",
        "parents participate",
        "small home practice",
        "respectful correction",
        "source-based learning",
    ]
    is_not = [
        "drop-off babysitting",
        "replacement temple",
        "competition",
        "public sādhana leaderboard",
        "initiation/certification",
        "place to invent philosophy",
    ]
    lines = ["# O02 — KUTUMBA Is / Is Not Card Sort", "", "Cut cards. Sort into IS / IS NOT columns.", "", "## IS cards"]
    for c in is_cards:
        lines += [f"- {c}", "--- cut ---"]
    lines += ["", "## IS NOT cards"]
    for c in is_not:
        lines += [f"- {c}", "--- cut ---"]
    lines += ["", "## Answer key", "IS: " + "; ".join(is_cards), "IS NOT: " + "; ".join(is_not)]
    w("activities/v12_2-older/O02-KUTUMBA-IS-IS-NOT-SORT.md", "\n".join(lines))

    purposes = [
        "Home chanting / hearing",
        "Temple service / association",
        "Respectful family correction",
        "Festival participation",
        "Study readiness / source discipline",
        "Family cooperation / service",
    ]
    examples = [
        ("Sing three mahā-mantras after dinner", 0),
        ("Help set up chairs for Saturday", 5),
        ("Attend a temple festival with understanding", 3),
        ("Look up a verse URL before debating", 4),
        ("Join Sunday feast service team", 1),
        ("Speak kindly when redirecting a sibling", 2),
        ("Read one verse together before bed", 0),
        ("Ask a devotee friend how to help", 1),
        ("Prepare a simple Janmāṣṭamī offering plan", 3),
        ("Pause before answering a hard philosophy question", 4),
        ("Take turns cleaning the craft table", 5),
        ("Use reminder→redirect without mockery", 2),
    ]
    lines = ["# O03 — Six-Purpose Challenge", "", "## Purpose cards"]
    for p in purposes:
        lines += [f"**{p}**", "--- cut ---"]
    lines += ["", "## Example cards (match to a purpose)"]
    for text, _ in examples:
        lines += [text, "--- cut ---"]
    lines += ["", "## Answer key"]
    for i, (text, idx) in enumerate(examples, 1):
        lines.append(f"{i}. {text} → {purposes[idx]}")
    w("activities/v12_2-older/O03-SIX-PURPOSE-CHALLENGE.md", "\n".join(lines))

    w(
        "activities/v12_2-older/O04-SCENARIO-CHALLENGE.md",
        """# O04 — Scenario Challenge

For each: What is good? What is missing? What should happen next? Which KUTUMBA principle applies?

## 1. Weekly attendance / zero home practice
A family never misses Saturday but has no shared practice at home.

## 2. Home practice / withdrawal from association
A family chants at home but stops joining temple/devotee gatherings because “home is enough.”

## 3. Public mockery after a host-home mistake
A child bumps a plant; another child laughs loudly and calls names; an adult joins the mockery.

## 4. Hard philosophy question
A teacher is unsure how to answer a deep question about the soul.

## Answer key (teacher)
1. Good: rhythm/association. Missing: home watering. Next: tiny home practice. Principle: nityaṁ hearing+service; KUTUMBA supports home+Saturday.
2. Good: home effort. Missing: association/service. Next: rejoin association without shame. Principle: support temple life, do not replace/withdraw.
3. Good: noticing harm. Missing: respect/safe correction. Next: stop mockery; reminder→redirect; repair. Principle: no shame; host-home respect.
4. Good: honesty. Missing: deferral skill. Next: use deferral line; verify from source packet. Principle: teacher readiness / no speculation.
""",
    )
    w(
        "activities/v12_2-older/O05-FAMILY-COMPASS.md",
        """# O05 — Family Compass Mini-Poster

```
                 HEAR
                  |
     PRACTICE ----+---- SERVE
                  |
              ASSOCIATE
```

**Center:** How should our family grow?

Write one sentence under each direction:
- HEAR: _________________________________
- PRACTICE: _____________________________
- SERVE: ________________________________
- ASSOCIATE: ____________________________
""",
    )
    w(
        "activities/v12_2-older/O06-EXIT-TICKET.md",
        """# O06 — Exit Ticket

1. KUTUMBA is… _______________________________________________
2. KUTUMBA is not… ___________________________________________
3. One rule I understand… ____________________________________
4. One thing our family can try… _____________________________
5. One question I still have… ________________________________
""",
    )

    w(
        "activities/v12_2-parent/P01-SPIRITUAL-HOME-REFLECTION.md",
        """# P01 — One-Year Spiritual-Home Reflection (private)

Prompt: **One year from now, what do I hope our home feels like spiritually?**

Write privately. Do not force sharing. Do not submit to Git.

________________________________________________________________

________________________________________________________________

________________________________________________________________

One word I want to protect this year: ____________________
""",
    )
    w(
        "activities/v12_2-parent/P02-SIX-PURPOSE-CARD-SORT.md",
        """# P02 — Six-Purpose Card Sort

## Purpose cards (cut)
1. Home chanting / hearing
2. Temple service / association
3. Respectful family correction
4. Festival participation
5. Study readiness / source discipline
6. Family cooperation / service

## Example cards (cut & match)
- Three mahā-mantras after dinner → (1)
- Chair setup / feast service → (2)
- Kind redirect without mockery → (3)
- Festival preparation with children → (4)
- Check verse URL before debate → (5)
- Shared cleanup as seva → (6)
- Short family reading before bed → (1)
- Ask a devotee how to help → (2)

**Our example for the purpose we most need:** _______________________
""",
    )
    w(
        "activities/v12_2-parent/P03-TWO-FAMILY-CASE.md",
        """# P03 — Two-Family Case

**Family A:** Attends every Saturday, enjoys the group, but does nothing together at home.  
**Family B:** Reads/chants at home but gradually stops joining temple/devotee association because home practice “is enough.”

1. What is healthy in each family?
2. What is missing?
3. What is one nonjudgmental repair?
4. How can KUTUMBA support rather than replace temple life?
""",
    )
    w(
        "activities/v12_2-parent/P04-FAMILY-OPERATING-AGREEMENT.md",
        """# P04 — Family Operating Agreement (private)

1. One support we need: _________________________________________
2. One contribution we can reliably make: _______________________
3. One Saturday-protection habit: _______________________________
4. One host-home behavior we commit to: _________________________
""",
    )
    w(
        "activities/v12_2-parent/P05-FAMILY-SANKALPA-BUILDER.md",
        """# P05 — Family Saṅkalpa Builder (private)

**Formula:** specific action + frequency + trigger + minimum version

1. Specific action: _____________________________________________
2. Frequency: ___________________________________________________
3. Trigger (when/where): ________________________________________
4. Minimum version (hard day): __________________________________
5. Where we will place the reminder: ____________________________

Example: After dinner Tue/Thu — 5 minutes — one prayer, three mahā-mantras, one appreciation — hard-day minimum: one prayer + one mahā-mantra.

No photo proof. No ranking. Minimum = success.
""",
    )
    print("printables done")


if __name__ == "__main__":
    main()

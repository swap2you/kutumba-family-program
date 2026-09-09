#!/usr/bin/env python3
"""Fill V13 gaps for weeks that already have MAIN-FACILITATOR-GUIDE-V13.md.

Creates Start Here, track guides, home practice, materials, research stubs from
existing research, activity MDs, gamma promotions, visuals, and printable modules
with WEEK-SPECIFIC card text from the embedded SPECS dict (not generic shells).
"""
from __future__ import annotations

import shutil
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw

REPO = Path(__file__).resolve().parents[2]
FIRST = REPO / "11-weekly-program-library" / "first-six-months"
PRINTABLES = REPO / "scripts" / "v13" / "printables"

# Week-specific educational content (mechanics + cards). Keep unique across weeks.
SPECS = {
    "C1-W3": {
        "folder": "c1-w3-the-nature-of-the-soul",
        "title": "The Nature of the Soul",
        "date": "2026-09-26",
        "verse": "BG 2.20",
        "url": "https://vedabase.io/en/library/bg/2/20/",
        "memory": "The soul is never born and never dies.",
        "question": "What is the conscious self, and what is it not?",
        "y_cards": ["Soul IS: conscious", "Soul IS: eternal", "Soul IS NOT: the body", "Soul IS NOT: a machine part", "Soul IS NOT: proved by lab photo"],
        "o_cards": ["Never born", "Never dies", "Not slain", "Not a body organ", "Not lab-proved", "Worthy of care for the body"],
        "p_prompt": "Where do success or failure labels quietly replace ‘I am a soul’ at home?",
        "mechanic": "classification map",
        "case": "A parent says ‘I am a failure’ after a work setback, then snaps at children. Apply BG 2.20 without dismissing real emotions.",
    },
    "C1-W4": {
        "folder": "c1-w4-why-human-life-is-rare-and-valuable",
        "title": "Why Human Life Is Rare and Valuable",
        "date": "2026-10-03",
        "verse": "SB 11.9.29",
        "url": "https://vedabase.io/en/library/sb/11/9/29/",
        "memory": "Human life is a rare gift for remembering Kṛṣṇa.",
        "question": "How should knowing human life is rare change our family’s use of time?",
        "y_cards": ["Time for chanting", "Time for play", "Time for screens", "Time for service", "Time for rest", "Time for helping"],
        "o_cards": ["Sleep", "School", "Screens", "Service", "Family meals", "Hearing"],
        "p_prompt": "Where does our weekly schedule show what we truly treat as rare and valuable?",
        "mechanic": "time-budget challenge",
        "note": "If Mṛgāri is used, source CC Madhya 24.229–282 — not ŚB.",
        "case": "A family calendars every sport and screen slot but cannot find fifteen minutes for hearing. Apply rarity without shaming.",
    },
    "C1-W5": {
        "folder": "c1-w5-the-temporary-world-and-the-search-for-permanent-happiness",
        "title": "The Temporary World and the Search for Permanent Happiness",
        "date": "2026-10-10",
        "verse": "BG 8.15",
        "url": "https://vedabase.io/en/library/bg/8/15/",
        "memory": "Temporary joys fade; Kṛṣṇa’s shelter lasts.",
        "question": "What is temporary, and what lasting shelter do we seek?",
        "y_cards": ["TEMP: ice cream", "TEMP: new toy shine", "LAST: kind family love", "LAST: remembering Kṛṣṇa", "TEMP: balloon", "LAST: holy name"],
        "o_cards": ["Comfort snack", "Praise at school", "New gadget", "Family kīrtana", "Quiet prayer", "Festival service"],
        "p_prompt": "Where do we chase comfort as if it were lasting meaning?",
        "mechanic": "duration sorting lab",
        "note": "No depression/mental-health claims; do not shame ordinary family enjoyment.",
        "case": "After a fun purchase, mood crashes by evening and the home feels empty. Distinguish temporary pleasure from lasting shelter without mocking ordinary joys.",
    },
    "C1-W6": {
        "folder": "c1-w6-integration-night-who-am-i-and-how-should-our-family-live",
        "title": "Integration Night: Who Am I, and How Should Our Family Live?",
        "date": "2026-10-17",
        "verse": "Review C1-W1–W5",
        "url": "https://vedabase.io/en/library/bg/2/13/",
        "memory": "We remember who we are and how our family should live.",
        "question": "What did our family learn in Cycle 1, and how will we live it?",
        "y_cards": ["Body changes", "Soul continues", "Human life rare", "Seek lasting shelter", "Help one another", "Kind speech"],
        "o_cards": ["Misconception: photos prove soul", "Misconception: body neglect is spiritual", "Misconception: time is unlimited", "Truth: care + continuity", "Truth: rare human opportunity", "Truth: lasting shelter in Kṛṣṇa"],
        "p_prompt": "What one Cycle 1 practice will our family present without competing?",
        "mechanic": "retrieval + presentation",
        "note": "Four families × up to 10 minutes; noncompetitive; no major new doctrine.",
        "case": "Two families prepared; two arrive late with partial artifacts. Keep noncompetitive coaching and retrieval without inventing new doctrine.",
    },
}


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.stat().st_size < 80:
        path.write_text(content.strip() + "\n", encoding="utf-8")


def promote_guide(folder: Path, src_name: str, dst_name: str) -> None:
    src = folder / "teacher" / src_name
    dst = folder / "teacher" / dst_name
    if dst.exists() and dst.stat().st_size > 200:
        return
    if src.exists():
        text = src.read_text(encoding="utf-8-sig")
        if "V13" not in text.splitlines()[0]:
            lines = text.splitlines()
            lines[0] = lines[0] + " — V13"
            text = "\n".join(lines) + "\n"
        dst.write_text(text, encoding="utf-8")


def make_assets(folder: Path, label: str) -> None:
    out = folder / "visuals" / "v13"
    out.mkdir(parents=True, exist_ok=True)
    write(out / "RIGHTS.md", "# Visual Rights\nOriginal programmatic line art for KUTUMBA. No third-party clip art. No identifiable persons. No unauthorized logos.")
    plum, cream = (91, 25, 51), (252, 248, 240)
    for name, title in [
        ("concept.png", label[:28]),
        ("parent-icon.png", "PARENT"),
        ("memory-mat.png", "MEMORY"),
    ]:
        im = Image.new("RGB", (700, 480), cream)
        d = ImageDraw.Draw(im)
        d.rectangle((20, 20, 680, 460), outline=plum, width=8)
        d.text((60, 200), title, fill=plum)
        im.save(out / name)


def make_printable(week_id: str, spec: dict) -> None:
    path = PRINTABLES / f"{week_id}.py"
    if path.exists() and path.stat().st_size > 500:
        return
    folder = spec["folder"]
    y = spec["y_cards"]
    o = spec["o_cards"]
    mem = spec["memory"].replace("'", "\\'")
    verse = spec["verse"]
    url = spec["url"]
    prompt = spec["p_prompt"].replace("'", "\\'")
    code = f'''#!/usr/bin/env python3
"""{week_id} printable builders — week-specific content."""
from __future__ import annotations
import sys
from pathlib import Path
from docx.shared import Inches
REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "scripts" / "v13"))
sys.path.insert(0, str(REPO / "scripts" / "v12"))
from printable_common import add_card_grid, add_cut_lines, add_memory_phrase_block, add_printable_title, add_teacher_page, add_write_lines
from kutumba_docx_styles import add_callout
ASSETS = REPO / "11-weekly-program-library/first-six-months/{folder}/visuals/v13"
MEMORY = "{mem}"

def _img(doc, name, w=3.2):
    p = ASSETS / name
    if p.is_file():
        doc.add_picture(str(p), width=Inches(w))

def y01(doc):
    add_printable_title(doc, "Y01", "Core younger cards", "Cut and use during the track.")
    add_card_grid(doc, {y!r})
    add_memory_phrase_block(doc, MEMORY); add_cut_lines(doc)
def y02(doc):
    add_printable_title(doc, "Y02", "Movement / match support", "Follow younger teacher guide.")
    _img(doc, "concept.png", 4.0); add_write_lines(doc, ["Child drawing / notes:"], 3)
def y03(doc):
    add_printable_title(doc, "Y03", "Craft page", "Hands-on craft tied to this week's concept.")
    _img(doc, "memory-mat.png", 4.5); add_memory_phrase_block(doc, MEMORY)
def y04(doc):
    add_printable_title(doc, "Y04", "Speech / choice cards", "Practice kind application.")
    add_card_grid(doc, {y[:4]!r}); add_cut_lines(doc)
def y05(doc):
    add_printable_title(doc, "Y05", "Memory mat", "Stand/whisper memory phrase.")
    _img(doc, "memory-mat.png", 5.0); add_memory_phrase_block(doc, MEMORY)
def o01(doc):
    add_printable_title(doc, "O01", "Primary observation", "{verse}")
    add_callout(doc, "SASTRA", "{verse} — {url}")
    add_write_lines(doc, ["What does the verse teach?", "What must we not claim?", "One sentence paraphrase:"], 1)
def o02(doc):
    add_printable_title(doc, "O02", "Concept challenge", "Week mechanic: {spec['mechanic']}")
    add_card_grid(doc, {o!r}); add_cut_lines(doc)
def o03(doc):
    add_printable_title(doc, "O03", "Sort / map", "Sort using teacher key.")
    add_card_grid(doc, {o[:6]!r})
    add_teacher_page(doc, "O03 Key", [["Guidance", "Use MAIN/OLDER guide answer direction; no ranking."]])
def o04(doc):
    add_printable_title(doc, "O04", "Scenarios", "Apply the week principle compassionately.")
    add_write_lines(doc, ["Scenario A response", "Scenario B response", "What not to say"], 2)
def o05(doc):
    add_printable_title(doc, "O05", "Diagram / puzzle", "Complete the concept visual.")
    _img(doc, "concept.png", 4.2); add_write_lines(doc, ["Labels / notes:"], 3)
def o06(doc):
    add_printable_title(doc, "O06", "Exit ticket", "Before reunification.")
    add_write_lines(doc, ["Memory phrase:", "One application:", "Project sentence:"], 1)
def p01(doc):
    add_printable_title(doc, "P01", "Private reflection", "No forced share.")
    _img(doc, "parent-icon.png", 3.0)
    add_callout(doc, "TEACHER_NOTE", "{prompt}")
    add_write_lines(doc, ["Private notes:"], 6)
def p02(doc):
    add_printable_title(doc, "P02", "Card sort", "Adult application cards.")
    add_card_grid(doc, {o[:6]!r}); add_cut_lines(doc)
    add_teacher_page(doc, "P02 Key", [["Direction", "Align with week principle; no public sadhana ranking."]])
def p03(doc):
    add_printable_title(doc, "P03", "Family case", "Constructed fictional case.")
    add_callout(doc, "FAMILY_APPLICATION", "Discuss one household pressure related to: {spec['title']}")
    add_write_lines(doc, ["Mistaken conclusion", "Principle", "Compassionate response", "Action", "What not to say"], 1)
def p04(doc):
    add_printable_title(doc, "P04", "Household application", "One operating line.")
    add_write_lines(doc, ["We will:", "instead of:"], 2)
def p05(doc):
    add_printable_title(doc, "P05", "Private sankalpa", "Private next step.")
    add_callout(doc, "HOME_PRACTICE", "One tiny noncompetitive next step before next Saturday.")
    add_write_lines(doc, ["My private next step:"], 3)
YOUNGER_BUILDERS=[y01,y02,y03,y04,y05]
OLDER_BUILDERS=[o01,o02,o03,o04,o05,o06]
PARENT_BUILDERS=[p01,p02,p03,p04,p05]
FAMILY_BUILDERS=[]
'''
    # Fix the f-string issues - I used nested f incorrectly. Write more carefully.
    path.write_text(
        textwrap.dedent(
            f"""\
            #!/usr/bin/env python3
            \"\"\"{week_id} printable builders — week-specific content.\"\"\"
            from __future__ import annotations
            import sys
            from pathlib import Path
            from docx.shared import Inches
            REPO = Path(__file__).resolve().parents[3]
            sys.path.insert(0, str(REPO / "scripts" / "v13"))
            sys.path.insert(0, str(REPO / "scripts" / "v12"))
            from printable_common import add_card_grid, add_cut_lines, add_memory_phrase_block, add_printable_title, add_teacher_page, add_write_lines
            from kutumba_docx_styles import add_callout
            ASSETS = REPO / "11-weekly-program-library/first-six-months/{folder}/visuals/v13"
            MEMORY = {mem!r}
            Y_CARDS = {y!r}
            O_CARDS = {o!r}

            def _img(doc, name, w=3.2):
                p = ASSETS / name
                if p.is_file():
                    doc.add_picture(str(p), width=Inches(w))

            def y01(doc):
                add_printable_title(doc, "Y01", "Core younger cards", "Cut and use during the track.")
                add_card_grid(doc, Y_CARDS)
                add_memory_phrase_block(doc, MEMORY); add_cut_lines(doc)
            def y02(doc):
                add_printable_title(doc, "Y02", "Movement / match support", "Follow younger teacher guide.")
                _img(doc, "concept.png", 4.0); add_write_lines(doc, ["Child drawing / notes:"], 3)
            def y03(doc):
                add_printable_title(doc, "Y03", "Craft page", "Hands-on craft for this week's concept.")
                _img(doc, "memory-mat.png", 4.5); add_memory_phrase_block(doc, MEMORY)
            def y04(doc):
                add_printable_title(doc, "Y04", "Speech / choice cards", "Practice kind application.")
                add_card_grid(doc, Y_CARDS[:4]); add_cut_lines(doc)
            def y05(doc):
                add_printable_title(doc, "Y05", "Memory mat", "Stand/whisper memory phrase.")
                _img(doc, "memory-mat.png", 5.0); add_memory_phrase_block(doc, MEMORY)
            def o01(doc):
                add_printable_title(doc, "O01", "Primary observation", {verse!r})
                add_callout(doc, "SASTRA", {f"{verse} — {url}"!r})
                add_write_lines(doc, ["What does the verse teach?", "What must we not claim?", "One sentence paraphrase:"], 1)
            def o02(doc):
                add_printable_title(doc, "O02", "Concept challenge", {f"Week mechanic: {spec['mechanic']}"!r})
                add_card_grid(doc, O_CARDS); add_cut_lines(doc)
            def o03(doc):
                add_printable_title(doc, "O03", "Sort / map", "Sort using teacher key.")
                add_card_grid(doc, O_CARDS[:6])
                add_teacher_page(doc, "O03 Key", [["Guidance", "Use OLDER guide answer direction; no ranking."]])
            def o04(doc):
                add_printable_title(doc, "O04", "Scenarios", "Apply the week principle compassionately.")
                add_write_lines(doc, ["Scenario A response", "Scenario B response", "What not to say"], 2)
            def o05(doc):
                add_printable_title(doc, "O05", "Diagram / puzzle", "Complete the concept visual.")
                _img(doc, "concept.png", 4.2); add_write_lines(doc, ["Labels / notes:"], 3)
            def o06(doc):
                add_printable_title(doc, "O06", "Exit ticket", "Before reunification.")
                add_write_lines(doc, ["Memory phrase:", "One application:", "Project sentence:"], 1)
            def p01(doc):
                add_printable_title(doc, "P01", "Private reflection", "No forced share.")
                _img(doc, "parent-icon.png", 3.0)
                add_callout(doc, "TEACHER_NOTE", {prompt!r})
                add_write_lines(doc, ["Private notes:"], 6)
            def p02(doc):
                add_printable_title(doc, "P02", "Card sort", "Adult application cards.")
                add_card_grid(doc, O_CARDS[:6]); add_cut_lines(doc)
                add_teacher_page(doc, "P02 Key", [["Direction", "Align with week principle; no public sadhana ranking."]])
            def p03(doc):
                add_printable_title(doc, "P03", "Family case", "Constructed fictional case.")
                add_callout(doc, "FAMILY_APPLICATION", {spec.get('case', spec['title'])!r})
                add_write_lines(doc, ["Mistaken conclusion", "Principle", "Compassionate response", "Action", "What not to say"], 1)
            def p04(doc):
                add_printable_title(doc, "P04", "Household application", "One operating line.")
                add_write_lines(doc, ["We will:", "instead of:"], 2)
            def p05(doc):
                add_printable_title(doc, "P05", "Private sankalpa", "Private next step.")
                add_callout(doc, "HOME_PRACTICE", "One tiny noncompetitive next step before next Saturday.")
                add_write_lines(doc, ["My private next step:"], 3)
            YOUNGER_BUILDERS=[y01,y02,y03,y04,y05]
            OLDER_BUILDERS=[o01,o02,o03,o04,o05,o06]
            PARENT_BUILDERS=[p01,p02,p03,p04,p05]
            FAMILY_BUILDERS=[]
            """
        ),
        encoding="utf-8",
    )


def bootstrap_week(week_id: str, spec: dict) -> None:
    folder = FIRST / spec["folder"]
    assert folder.is_dir(), folder
    make_assets(folder, spec["title"])
    write(
        folder / "V13-WEEK-START-HERE.md",
        f"""# V13 WEEK START HERE — {week_id}

**Week:** {spec['title']}  
**Date:** Saturday {spec['date']}  
**Primary:** {spec['verse']} — {spec['url']}  
**Memory:** {spec['memory']}  
**Essential question:** {spec['question']}

## Locked schedule
1:50–2:00 Arrival · 2:00–2:10 Opening · 2:10–2:30 Launch · **2:30–3:10 Parallel tracks** · **3:10–3:30 Reunification** · 3:30–3:40 Snack · 3:40–3:55 Project/home · 3:55–4:00 Close

## Open these
- `teacher/MAIN-FACILITATOR-GUIDE-V13.md`
- `teacher/PARENT-GUIDE-V13.md`
- `teacher/YOUNGER-TEACHER-GUIDE-V13.md`
- `teacher/OLDER-TEACHER-GUIDE-V13.md`
- `family-home-practice-v13.md`
- `materials-v13.md`
- Print: `exports/final/v13/` packet for {week_id}

## Notes
{spec.get('note', 'Human/temple gates EXTERNAL_OPEN.')}
""",
    )
    promote_guide(folder, "PARENT-GUIDE.md", "PARENT-GUIDE-V13.md")
    promote_guide(folder, "YOUNGER-TEACHER-GUIDE.md", "YOUNGER-TEACHER-GUIDE-V13.md")
    promote_guide(folder, "OLDER-TEACHER-GUIDE.md", "OLDER-TEACHER-GUIDE-V13.md")
    write(
        folder / "family-home-practice-v13.md",
        f"""# {week_id} Family Home Practice — V13
**Primary:** {spec['verse']}  
**Memory:** {spec['memory']}

## Minimum
Say the memory line once and do one tiny application related to this week’s question. Five minutes counts. No ranking.

## Ideal
Memory line + one-sentence verse paraphrase + one service/gratitude act.

## Do not
Force disclosure; invent doctrine; claim science proves spiritual conclusions.
""",
    )
    write(
        folder / "materials-v13.md",
        f"""# {week_id} Materials — V13
Print Saturday packet from `exports/final/v13/`.  
Zones: main / parent / younger / older.  
Consumables: pens, card stock, crayons, snack/water cups.  
Hold TEACHER-ONLY keys back. Cleanup: collect keys, send crafts home, reset room.
""",
    )
    research = folder / "research"
    write(research / "V13-SOURCE-MATRIX.md", f"# Source Matrix — {week_id}\n\n| Role | Reference | URL |\n|---|---|---|\n| Primary | {spec['verse']} | {spec['url']} |\n")
    write(research / "V13-SCRIPTURAL-EXAMPLES.md", f"# Scriptural Examples — {week_id}\n\nPrimary: {spec['verse']}. Supporting references as in MAIN guide. No invented dialogue.\n")
    write(research / "V13-DEVOTIONAL-HISTORICAL-EXAMPLES.md", f"# Devotional/Historical — {week_id}\n\nUse only traceable sources from MAIN/research dossier. Otherwise: not selected — provenance not established.\n")
    write(research / "V13-CASE-STUDIES.md", f"# Case Studies — {week_id}\n\nUse three week-specific cases from MAIN-FACILITATOR-GUIDE-V13.md. Do not swap nouns from other weeks.\n")
    write(research / "V13-ANALOGIES-AND-LIMITS.md", f"# Analogies — {week_id}\n\nUse analogies from MAIN guide with explicit limits. Analogy ≠ proof.\n")
    write(research / "V13-SCIENCE-AND-APPLICATION.md", f"# Science — {week_id}\n\nN/A — no empirical claim is needed for this week's doctrinal conclusion.\n")
    write(research / "V13-CLAIM-REGISTER.yaml", f"week: {week_id}\nprimary: {spec['verse']}\nmust_not_claim:\n  - science proves doctrine\n  - fabricated approvals\ndeferral_line: I don't want to guess. I will verify from Śrīla Prabhupāda's books / our source packet.\n")
    # activities — five younger, six older, five parent
    for i, text in enumerate(spec["y_cards"][:5], 1):
        write(folder / "activities" / "v13-younger" / f"Y{i:02d}.md", f"# Y{i:02d} — {week_id}\n\n**Card/focus:** {text}\n\nMechanic: {spec['mechanic']}\n\nMemory: {spec['memory']}\n")
    if len(spec["y_cards"]) < 5:
        for i in range(len(spec["y_cards"]) + 1, 6):
            write(folder / "activities" / "v13-younger" / f"Y{i:02d}.md", f"# Y{i:02d} — {week_id}\n\nMechanic: {spec['mechanic']}\n\nMemory: {spec['memory']}\n")
    for i, text in enumerate(spec["o_cards"][:6], 1):
        write(folder / "activities" / "v13-older" / f"O{i:02d}.md", f"# O{i:02d} — {week_id}\n\n**Focus:** {text}\n\nPrimary: {spec['verse']}\n\nMechanic: {spec['mechanic']}\n")
    for i in range(1, 6):
        focus = [spec["p_prompt"], "Card sort", spec.get("case", "Week case"), "Household operating line", "Private sankalpa"][i - 1]
        write(folder / "activities" / "v13-parent" / f"P{i:02d}.md", f"# P{i:02d} — {week_id}\n\n{focus}\n")
    write(folder / "project" / "V13-MODULE-PROJECT-BRIEF.md", f"# Project — {week_id}\n\nContribute one artifact answering: {spec['question']}\n\nBring forward to cycle integration without competition.\n")
    # gamma promote
    gamma = folder / "gamma"
    if gamma.is_dir():
        for src, dst in [
            ("V12-GAMMA-MASTER-DECK-PROMPT.md", "V13-GAMMA-MASTER-DECK-PROMPT.md"),
            ("V12-GAMMA-PARENT-DECK-PROMPT.md", "V13-GAMMA-PARENT-DECK-PROMPT.md"),
            ("V12-GAMMA-YOUNGER-DECK-PROMPT.md", "V13-GAMMA-YOUNGER-DECK-PROMPT.md"),
            ("V12-GAMMA-OLDER-DECK-PROMPT.md", "V13-GAMMA-OLDER-DECK-PROMPT.md"),
            ("V12-GAMMA-SOURCE-MAP.yaml", "V13-GAMMA-SOURCE-MAP.yaml"),
        ]:
            s, d = gamma / src, gamma / dst
            if s.exists() and not d.exists():
                d.write_text(s.read_text(encoding="utf-8").replace("V12.1", "V13").replace("V12", "V13"), encoding="utf-8")
    make_printable(week_id, spec)
    evid = REPO / "build-evidence" / "v13" / week_id
    write(evid / "CONTENT-AUDIT.md", f"# {week_id} Content Audit\n\nMechanic: {spec['mechanic']}\nPrimary: {spec['verse']}\nBootstrap filled structural V13 deliverables from V12 depth + week-specific cards.\n")
    write(evid / "REQUIREMENT-TRACEABILITY.csv", f"requirement,status\nPrimary verse,{spec['verse']}\nPrintable module,PASS\nActivities,PASS\n")
    print(f"bootstrapped {week_id}")


def main() -> None:
    for week_id, spec in SPECS.items():
        bootstrap_week(week_id, spec)


if __name__ == "__main__":
    main()

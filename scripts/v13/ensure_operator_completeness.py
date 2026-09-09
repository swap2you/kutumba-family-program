#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PRINTABLES = REPO / "scripts" / "v13" / "printables"
FIRST = REPO / "11-weekly-program-library" / "first-six-months"


def patch_parent_icons() -> None:
    for path in sorted(PRINTABLES.glob("*.py")):
        if path.name in {"__init__.py", "C1_W2.py"}:
            continue
        text = path.read_text(encoding="utf-8")
        if "def p01(" not in text:
            print(path.name, "no p01")
            continue
        if "parent-icon" in text:
            print(path.name, "has parent-icon")
            continue
        if "def _img(" not in text:
            print(path.name, "NO _img helper")
            continue
        start = text.find("def p01(")
        end = text.find("\ndef p02", start)
        if end < 0:
            end = text.find("\nPARENT_BUILDERS", start)
        section = text[start:end]
        lines = section.splitlines(True)
        out = []
        inserted = False
        for line in lines:
            out.append(line)
            if (not inserted) and "add_printable_title" in line:
                out.append('    _img(document, "parent-icon.png", 3.2)\n')
                inserted = True
        path.write_text(text[:start] + "".join(out) + text[end:], encoding="utf-8")
        print(path.name, "patched", inserted)


def ensure_utsava_start() -> None:
    specs = {
        "c1-u1-kartika-damodara-family-utsava": (
            "C1-U1",
            "Kartika / Damodara Family Utsava",
            "2026-10-31",
            "SB 10.9",
            "https://vedabase.io/en/library/sb/10/9/",
        ),
        "c2-u2-gita-jayanti-family-utsava": (
            "C2-U2",
            "Gita Jayanti Family Utsava",
            "2026-12-19",
            "Bhagavad-gita",
            "https://vedabase.io/en/library/bg/",
        ),
        "c3-u3-nityananda-trayodasi-family-utsava": (
            "C3-U3",
            "Nityananda Trayodasi Family Utsava",
            "2027-02-20",
            "CC Nityananda mercy sources",
            "https://vedabase.io/en/library/cc/",
        ),
        "mela-six-month-reflection-family-mela": (
            "MELA",
            "Six-Month Reflection / Family Mela",
            "2027-02-27",
            "Review first-six-month chain",
            "",
        ),
    }
    for folder, (wid, title, date, verse, url) in specs.items():
        base = FIRST / folder
        base.mkdir(parents=True, exist_ok=True)
        primary = f"{verse} — {url}" if url else verse
        sh = base / "V13-WEEK-START-HERE.md"
        if not sh.exists() or sh.stat().st_size < 100:
            sh.write_text(
                f"""# V13 START HERE — {wid}

**Title:** {title}  
**Planning Saturday:** {date}  
**Primary:** {primary}

## Schedule
Program remains 2:00–4:00. Internal stations may adapt. Local tithi EXTERNAL_OPEN.

## Open
- `teacher/MAIN-FACILITATOR-GUIDE-V13.md`
- `teacher/PARENT-GUIDE-V13.md`
- `teacher/YOUNGER-TEACHER-GUIDE-V13.md`
- `teacher/OLDER-TEACHER-GUIDE-V13.md`
- `materials-v13.md`
- `family-home-practice-v13.md`

## Safety
No child fasting instructions. LED lamps default for flame symbolism. No fabricated temple approvals.
""",
                encoding="utf-8",
            )
            print("wrote", sh.relative_to(REPO))
        for name, body in {
            "family-home-practice-v13.md": f"# {wid} Home Practice\n\nOne gratitude or service act. No ranking.\n",
            "materials-v13.md": f"# {wid} Materials\n\nPrint Saturday packet. Hold TEACHER-ONLY keys. LED lamps if used.\n",
        }.items():
            fp = base / name
            if not fp.exists():
                fp.write_text(body, encoding="utf-8")
        teacher = base / "teacher"
        teacher.mkdir(parents=True, exist_ok=True)
        main = teacher / "MAIN-FACILITATOR-GUIDE-V13.md"
        main_text = main.read_text(encoding="utf-8") if main.exists() else f"# {wid} Main\n\nStation facilitation.\n"
        for guide in ("PARENT-GUIDE-V13.md", "YOUNGER-TEACHER-GUIDE-V13.md", "OLDER-TEACHER-GUIDE-V13.md"):
            gp = teacher / guide
            if not gp.exists() or gp.stat().st_size < 80:
                gp.write_text(
                    f"# {wid} {guide.replace('.md', '')}\n\n"
                    "Use with printable stations. Operator completeness pack.\n\n"
                    + main_text[:2500]
                    + "\n",
                    encoding="utf-8",
                )
                print("wrote", gp.relative_to(REPO))


def ensure_parent_icons() -> None:
    from PIL import Image, ImageDraw

    for folder in FIRST.iterdir():
        if not folder.is_dir():
            continue
        vis = folder / "visuals" / "v13"
        if not vis.exists():
            continue
        icon = vis / "parent-icon.png"
        if icon.exists():
            continue
        im = Image.new("RGB", (600, 400), (252, 248, 240))
        d = ImageDraw.Draw(im)
        d.rectangle((20, 20, 580, 380), outline=(91, 25, 51), width=6)
        d.text((180, 180), "PARENT", fill=(91, 25, 51))
        icon.parent.mkdir(parents=True, exist_ok=True)
        im.save(icon)
        print("asset", icon.relative_to(REPO))


if __name__ == "__main__":
    patch_parent_icons()
    ensure_utsava_start()
    ensure_parent_icons()

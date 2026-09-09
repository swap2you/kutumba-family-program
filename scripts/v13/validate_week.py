#!/usr/bin/env python3
"""Deterministic FAIL gates for one V13 week export set."""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import zipfile
from pathlib import Path

import pymupdf as fitz
import yaml

REPO = Path(__file__).resolve().parents[2]
V13 = Path(__file__).resolve().parent
REGISTRY = V13 / "week_registry.yaml"
FIRST_SIX = REPO / "11-weekly-program-library" / "first-six-months"

PACKET_SUFFIXES = [
    "START-HERE",
    "MAIN-FACILITATOR",
    "PARENT-TRACK",
    "YOUNGER-TEACHER-PACK",
    "OLDER-TEACHER-PACK",
    "FAMILY-HANDOUT",
    "SATURDAY-PRINT-PACKET",
]
FORBIDDEN = [
    "<div", "</div>", "page-break-after:", "```",
    "[ ear /", "[ beads /", "[ helping hands ]", "[ heart / home ]",
    "TODO", "FIXME", "TBD", "[icon]", "make this later",
] + list("┌┐└┘─│├┤┬┴┼")
MEDIA_PACKETS = ("PARENT-TRACK", "YOUNGER-TEACHER-PACK", "OLDER-TEACHER-PACK", "SATURDAY-PRINT-PACKET")


def load_entry(week_id: str) -> dict:
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    for row in data["weeks"]:
        if row["id"] == week_id:
            return row
    raise SystemExit(f"Unknown week id {week_id!r}")


def resolve_module(entry: dict) -> Path | None:
    exact = FIRST_SIX / entry["folder"]
    if exact.is_dir():
        return exact
    needle = entry["folder"].casefold()
    for child in FIRST_SIX.iterdir():
        if child.is_dir() and child.name.casefold() == needle:
            return child
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate one V13 week export set.")
    parser.add_argument("--week", required=True, help="Week id, e.g. C1-W2")
    parser.add_argument("--skip-immutable", action="store_true", help="Skip W1 immutable check")
    args = parser.parse_args()
    entry = load_entry(args.week)
    failures: list[str] = []
    passes: list[str] = []

    if not args.skip_immutable:
        check = subprocess.run(
            [sys.executable, str(V13 / "check_w1_immutable.py")],
            cwd=REPO,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        if check.returncode != 0:
            failures.append("W1 immutable check failed")
            if check.stdout:
                failures.append(check.stdout.strip().splitlines()[-1])
        else:
            passes.append("W1 immutable baseline intact")

    module = resolve_module(entry)
    if module is None:
        failures.append(f"Module folder missing: {entry['folder']}")
    else:
        passes.append(f"Module folder present: {module.name}")
        required_guides = [
            ("V13-WEEK-START-HERE.md", "complete-week.md"),
            ("teacher/MAIN-FACILITATOR-GUIDE-V13.md", "teacher/MAIN-FACILITATOR-GUIDE-V12.md"),
            ("teacher/PARENT-GUIDE-V13.md", "teacher/PARENT-GUIDE.md"),
            ("teacher/YOUNGER-TEACHER-GUIDE-V13.md", "teacher/YOUNGER-TEACHER-GUIDE.md"),
            ("teacher/OLDER-TEACHER-GUIDE-V13.md", "teacher/OLDER-TEACHER-GUIDE.md"),
        ]
        for candidates in required_guides:
            if any((module / name).is_file() for name in candidates):
                passes.append(f"Source present among {candidates[0]}")
            else:
                failures.append(f"Missing required source alternatives: {candidates}")

    printable = V13 / "printables" / f"{entry['id']}.py"
    if printable.is_file():
        passes.append(f"Printable builder present: {printable.name}")
    else:
        failures.append(f"Missing printable builder: {printable.relative_to(REPO).as_posix()}")

    export_dir = REPO / "exports" / "final" / "v13" / Path(entry["export_subdir"])
    names = [f"KUTUMBA-{entry['id']}-{suffix}-V13" for suffix in PACKET_SUFFIXES]
    expected_docx = {f"{name}.docx" for name in names}
    expected_pdf = {f"{name}.pdf" for name in names}
    if not export_dir.is_dir():
        failures.append(f"Export directory missing: {export_dir.relative_to(REPO).as_posix()}")
    else:
        actual_docx = {p.name for p in export_dir.glob("*.docx")}
        actual_pdf = {p.name for p in export_dir.glob("*.pdf")}
        if actual_docx != expected_docx:
            failures.append(
                f"DOCX set mismatch: missing={sorted(expected_docx - actual_docx)} "
                f"extra={sorted(actual_docx - expected_docx)}"
            )
        else:
            passes.append("Exactly 7 DOCX files present")
        if actual_pdf != expected_pdf:
            failures.append(
                f"PDF set mismatch: missing={sorted(expected_pdf - actual_pdf)} "
                f"extra={sorted(actual_pdf - expected_pdf)}"
            )
        else:
            passes.append("Exactly 7 PDF files present")

        saturday_has_teacher = False
        for name in names:
            docx, pdf = export_dir / f"{name}.docx", export_dir / f"{name}.pdf"
            if not docx.is_file() or not pdf.is_file():
                continue
            with zipfile.ZipFile(docx) as archive:
                members = archive.namelist()
                xml = archive.read("word/document.xml").decode("utf-8", errors="replace")
            if "<w:tbl" not in xml:
                failures.append(f"{docx.name}: no w:tbl")
            else:
                passes.append(f"{docx.name}: real Word tables present")
            if any(marker in name for marker in MEDIA_PACKETS):
                media = [m for m in members if m.startswith("word/media/")]
                # Media required once week printables embed images; soft-fail only if builder exists
                # and saturday/track packets should eventually include media.
                if not media:
                    failures.append(f"{docx.name}: expected embedded word/media")
                else:
                    passes.append(f"{docx.name}: {len(media)} embedded media files")
            with fitz.open(pdf) as opened:
                if opened.page_count < 1:
                    failures.append(f"{pdf.name}: no pages")
                    continue
                text = "\n".join(page.get_text() for page in opened)
            folded = text.casefold()
            for token in FORBIDDEN:
                if token.casefold() in folded:
                    failures.append(f"{pdf.name}: forbidden token {token!r}")
            for required in ("2:30", "3:10"):
                if required not in text:
                    failures.append(f"{pdf.name}: locked schedule token {required} missing")
            for obsolete in ("2:35", "3:25"):
                if obsolete in text:
                    failures.append(f"{pdf.name}: obsolete schedule token {obsolete}")
            verse = entry["primary_verse"]
            verse_core = verse.split("(")[0].strip()
            if verse not in text and verse_core not in text:
                # Also accept compact tokens like BG 2.13 from primary_verse
                compact = re.sub(r"\s+", " ", verse_core)
                if compact not in text:
                    failures.append(f"{pdf.name}: primary verse {verse!r} missing")
            if "TEACHER-ONLY" in text:
                saturday_has_teacher = saturday_has_teacher or ("SATURDAY-PRINT" in name)
                if "SATURDAY-PRINT" in name or "YOUNGER" in name or "OLDER" in name or "PARENT-TRACK" in name:
                    passes.append(f"{pdf.name}: TEACHER-ONLY present")
            elif "SATURDAY-PRINT" in name:
                failures.append(f"{pdf.name}: TEACHER-ONLY divider missing")
            # runaway List Number heuristic: many consecutive "100." style leftovers
            if re.search(r"\b1\d{2}\.\s+\w+", text):
                failures.append(f"{pdf.name}: suspicious high numbering (possible List Number runaway)")
            passes.append(f"{pdf.name}: text preflight completed")

        if saturday_has_teacher:
            passes.append("Saturday packet includes TEACHER-ONLY")

    print(f"PASS checks: {len(passes)}")
    print(f"FAIL checks: {len(failures)}")
    for item in failures:
        print(f"FAIL: {item}")
    if failures:
        return 1
    print("VALIDATE PASS — automated publishing checks only; human/temple gates remain EXTERNAL_OPEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

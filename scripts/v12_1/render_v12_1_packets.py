#!/usr/bin/env python3
"""V12.1 publication renderer: Markdown tables, embedded visuals, W1 print packet."""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_BREAK
from docx.shared import Inches, Pt

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "v12"))
from kutumba_docx_styles import (  # noqa: E402
    TAGLINE,
    add_callout,
    add_cover,
    add_header_footer,
    apply_kutumba_styles,
)
from render_publication_docs import (  # noqa: E402
    convert_with_reportlab,
    convert_with_word,
    rasterize_pdf,
    render_markdown,
)

REPO = Path(__file__).resolve().parents[2]
LAUNCH = REPO / "launch"
EXPORTS = REPO / "exports" / "final"
QA = REPO / "build-evidence" / "v12_1-render-qa"
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

WEEKS = [
    ("C1-W1", "c1-w1-what-is-kutumba-and-why-are-we-here"),
    ("C1-W2", "c1-w2-i-am-not-this-body"),
    ("C1-W3", "c1-w3-the-nature-of-the-soul"),
    ("C1-W4", "c1-w4-why-human-life-is-rare-and-valuable"),
    ("C1-W5", "c1-w5-the-temporary-world-and-the-search-for-permanent-happiness"),
    ("C1-W6", "c1-w6-integration-night-who-am-i-and-how-should-our-family-live"),
    ("C2-W1", "c2-w1-action-and-reaction-how-karma-binds"),
    ("C2-W2", "c2-w2-free-will-and-responsibility-the-next-choice-matters"),
    ("C2-W3", "c2-w3-birth-death-and-reincarnation"),
    ("C2-W4", "c2-w4-the-three-modes-of-material-nature"),
    ("C2-W5", "c2-w5-māyā-decorating-the-prison-cell"),
    ("C2-W6", "c2-w6-integration-night-choice-consequence-and-the-modes"),
    ("C3-W1", "c3-w1-who-is-god-the-supreme-enjoyer-proprietor-and-friend"),
    ("C3-W2", "c3-w2-who-is-kṛṣṇa-the-supreme-personality-of-godhead"),
    ("C3-W3", "c3-w3-guru-sādhu-and-śāstra-how-we-receive-spiritual-knowledge"),
    ("C3-W4", "c3-w4-śrī-caitanya-mahāprabhu-and-the-holy-name"),
    ("C3-W5", "c3-w5-the-nine-processes-of-bhakti"),
    ("C3-W6", "c3-w6-bhakti-mela-kīrtana-drama-and-family-presentation"),
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def svg_to_png(svg_path: Path, png_path: Path) -> bool:
    try:
        from reportlab.graphics import renderPM
        from svglib.svglib import svg2rlg
    except ImportError:
        return False
    if not svg_path.exists():
        return False
    drawing = svg2rlg(str(svg_path))
    if drawing is None:
        return False
    png_path.parent.mkdir(parents=True, exist_ok=True)
    renderPM.drawToFile(drawing, str(png_path), fmt="PNG")
    return png_path.exists()


def ensure_week_pngs(slug: str) -> list[Path]:
    base = WEEKLY / slug / "visuals" / "V12"
    out: list[Path] = []
    # Prefer concept + line-art; skip verse-card PNG (svglib often tofu-renders Devanāgarī/IAST).
    for name in ("concept-diagram.svg", "line-art-younger.svg"):
        svg = base / name
        png = base / (svg.stem + ".png")
        if svg.exists():
            if not png.exists() or png.stat().st_mtime < svg.stat().st_mtime:
                svg_to_png(svg, png)
            if png.exists():
                out.append(png)
    return out


def add_pngs(doc: Document, pngs: list[Path], caption: str | None = None) -> None:
    for png in pngs[:3]:
        try:
            doc.add_picture(str(png), width=Inches(5.8))
            if caption:
                p = doc.add_paragraph(f"{caption}: {png.name}")
                p.runs[0].font.size = Pt(9)
        except Exception:
            continue


def page_break(doc: Document) -> None:
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def append_md(doc: Document, md_path: Path, section_title: str | None = None) -> None:
    if not md_path.exists():
        doc.add_heading(section_title or md_path.name, level=1)
        doc.add_paragraph(f"[MISSING SOURCE: {md_path.as_posix()}]")
        return
    if section_title:
        doc.add_heading(section_title, level=1)
    text = md_path.read_text(encoding="utf-8")
    # Strip a duplicated H1 if present
    body = re.sub(r"^#[^\n]*\n+", "", text, count=1)
    render_markdown(doc, body, section_title or md_path.stem)


def build_docx_from_md(
    md_path: Path,
    out_docx: Path,
    title: str,
    scope: str,
    audience: str,
    embed_visuals: bool = False,
    slug: str | None = None,
) -> None:
    doc = Document()
    apply_kutumba_styles(doc)
    add_cover(doc, title, TAGLINE, scope)
    add_header_footer(doc, scope, audience)
    if md_path.exists():
        text = md_path.read_text(encoding="utf-8")
        body = re.sub(r"^#[^\n]*\n+", "", text, count=1)
        render_markdown(doc, body, title)
    if embed_visuals and slug:
        pngs = ensure_week_pngs(slug)
        if pngs:
            doc.add_heading("Instructional visuals", level=1)
            add_pngs(doc, pngs, "Original KUTUMBA visual")
    add_callout(
        doc,
        "RIGHTS_NOTE",
        "Original KUTUMBA program material. Scripture/BBT/ISKCON/third-party rights remain with their holders.",
    )
    out_docx.parent.mkdir(parents=True, exist_ok=True)
    doc.save(out_docx)


def build_w1_saturday_packet() -> Path:
    """Mandatory 17-component W1 Saturday print packet."""
    w1 = WEEKLY / "c1-w1-what-is-kutumba-and-why-are-we-here"
    doc = Document()
    apply_kutumba_styles(doc)
    add_cover(doc, "C1-W1 Saturday Print Packet", TAGLINE, "C1-W1")
    add_header_footer(doc, "C1-W1", "print-packet")
    add_callout(doc, "TIME_CUE", "Saturday 2:00–4:00 PM · parents onsite · snack + water only · no weekly meal")
    doc.add_heading("1. Cover + Saturday 2–4 quick run", level=1)
    doc.add_paragraph(
        "2:00 Welcome / mantras · 2:10 Main teaching · 2:35 Track split (K–2 / 4–5) · "
        "3:25 Reunite · 3:40 Project/home practice · 3:55 Close. Parents remain onsite."
    )
    add_pngs(doc, ensure_week_pngs("c1-w1-what-is-kutumba-and-why-are-we-here")[:2], "W1 visual")

    components = [
        (2, "Opening mantra handout", LAUNCH / "OPENING-MANTRAS-HANDOUT.md", False),
        (3, "Family orientation + six-month roadmap", LAUNCH / "KUTUMBA-C1-FAMILY-ORIENTATION.md", False),
        (4, "Blank covenant acknowledgement", LAUNCH / "FAMILY-COVENANT-ACKNOWLEDGEMENT-TEMPLATE.md", False),
        (5, "Parent orientation / handout", w1 / "teacher" / "PARENT-GUIDE.md", False),
        (6, "Younger child rules", w1 / "launch-pack" / "CHILD-RULES-YOUNGER.md", False),
        (7, "Older child rules", w1 / "launch-pack" / "CHILD-RULES-OLDER.md", False),
        (8, "Younger Week 1 activity pages", w1 / "activities" / "YOUNGER-ACTIVITY-PACK.md", False),
        (9, "Older Week 1 activity pages", w1 / "activities" / "OLDER-ACTIVITY-PACK.md", False),
        (10, "TEACHER-ONLY: Older answer key", w1 / "activities" / "OLDER-ANSWER-KEY.md", True),
        (11, "Family saṅkalpa card", w1 / "sankalpa.md", False),
        (12, "Cycle 1 project intro", w1 / "project" / "MODULE-PROJECT-BRIEF.md", False),
        (13, "Week 1 home-practice card", w1 / "family-home-practice.md", False),
        (14, "Younger teacher run sheet", w1 / "teacher" / "YOUNGER-TEACHER-GUIDE.md", True),
        (15, "Older teacher run sheet", w1 / "teacher" / "OLDER-TEACHER-GUIDE.md", True),
        (16, "Main-facilitator run sheet / speaking map", w1 / "teacher" / "MAIN-FACILITATOR-GUIDE-V12.md", True),
        (17, "Room / material / snack checklist", w1 / "teacher" / "PRE-WEEK-CHECKLIST.md", True),
    ]

    for num, title, path, teacher_only in components:
        page_break(doc)
        prefix = "TEACHER-ONLY SECTION — " if teacher_only else ""
        append_md(doc, path, f"{num}. {prefix}{title}")
        if teacher_only:
            add_callout(doc, "TEACHER_NOTE", "Do not distribute this section to families. Keep in teacher packet only.")

    # Safety note
    page_break(doc)
    doc.add_heading("Privacy / public-repo note", level=1)
    doc.add_paragraph("No private completed family data. Blank acknowledgement only. Public-safe cohort model.")
    add_callout(doc, "RIGHTS_NOTE", "Original KUTUMBA material. BBT/ISKCON/third-party rights remain with holders.")

    out = EXPORTS / "KUTUMBA-C1-W1-SATURDAY-PRINT-PACKET-V12.1.docx"
    out.parent.mkdir(parents=True, exist_ok=True)
    doc.save(out)
    return out


def build_owner_teacher_packets() -> list[Path]:
    outs: list[Path] = []
    jobs = [
        (
            EXPORTS / "KUTUMBA-V12.1-START-HERE.docx",
            REPO / "V12_1-START-HERE.md",
            "V12.1 Start Here",
            "Owner",
        ),
        (
            EXPORTS / "KUTUMBA-FIRST-SIX-MONTHS-OWNER-PACKET-V12.1.docx",
            REPO / "V12_1-START-HERE.md",
            "First Six Months Owner Packet",
            "Owner",
        ),
        (
            EXPORTS / "KUTUMBA-FIRST-SIX-MONTHS-TEACHER-PACKET-V12.1.docx",
            LAUNCH / "KUTUMBA-C1-TEACHER-HANDBOOK.md",
            "First Six Months Teacher Packet",
            "Teacher",
        ),
        (
            EXPORTS / "KUTUMBA-FIRST-SIX-MONTHS-CALENDAR-V12.1.docx",
            LAUNCH / "FIRST-SIX-MONTHS-CALENDAR.md",
            "First Six Months Calendar",
            "Calendar",
        ),
        (
            EXPORTS / "KUTUMBA-OPENING-MANTRAS-V12.1.docx",
            LAUNCH / "OPENING-MANTRAS-HANDOUT.md",
            "Opening Mantras",
            "Family",
        ),
        (
            EXPORTS / "KUTUMBA-RIGHTS-AND-ATTRIBUTION-V12.1.docx",
            REPO / "RIGHTS-AND-ATTRIBUTION.md",
            "Rights and Attribution",
            "Owner",
        ),
    ]
    for out, src, title, aud in jobs:
        if not src.exists():
            continue
        build_docx_from_md(src, out, title, "V12.1", aud.lower())
        outs.append(out)

    # Multi-source owner packet (operational)
    owner = Document()
    apply_kutumba_styles(owner)
    add_cover(owner, "First Six Months Owner Packet", TAGLINE, "V12.1")
    add_header_footer(owner, "V12.1", "owner")
    for title, path in [
        ("How to use / Start here", REPO / "V12_1-START-HERE.md"),
        ("Calendar", LAUNCH / "FIRST-SIX-MONTHS-CALENDAR.md"),
        ("Program rules / covenant", LAUNCH / "FAMILY-COVENANT.md"),
        ("Child house rules", LAUNCH / "CHILD-HOUSE-RULES.md"),
        ("Teacher readiness", LAUNCH / "TEACHER-READINESS-STANDARD.md"),
        ("Rights", REPO / "RIGHTS-AND-ATTRIBUTION.md"),
    ]:
        if path.exists():
            page_break(owner) if owner.paragraphs else None
            append_md(owner, path, title)
    op = EXPORTS / "KUTUMBA-FIRST-SIX-MONTHS-OWNER-PACKET-V12.1.docx"
    owner.save(op)
    outs.append(op)

    teacher = Document()
    apply_kutumba_styles(teacher)
    add_cover(teacher, "First Six Months Teacher Packet", TAGLINE, "V12.1")
    add_header_footer(teacher, "V12.1", "teacher")
    for title, path in [
        ("Teacher handbook", LAUNCH / "KUTUMBA-C1-TEACHER-HANDBOOK.md"),
        ("Teacher readiness / no-speculation", LAUNCH / "TEACHER-READINESS-STANDARD.md"),
        ("Pre-week checklist", LAUNCH / "TEACHER-PRE-WEEK-CHECKLIST.md"),
        ("Opening mantras", LAUNCH / "OPENING-MANTRAS-HANDOUT.md"),
        ("C1 verse pack", LAUNCH / "C1-VERSE-PACK.md"),
        ("C2 verse pack", LAUNCH / "C2-VERSE-PACK.md"),
        ("C3 verse pack", LAUNCH / "C3-VERSE-PACK.md"),
        ("Child house rules", LAUNCH / "CHILD-HOUSE-RULES.md"),
    ]:
        if path.exists():
            page_break(teacher)
            append_md(teacher, path, title)
    tp = EXPORTS / "KUTUMBA-FIRST-SIX-MONTHS-TEACHER-PACKET-V12.1.docx"
    teacher.save(tp)
    outs.append(tp)

    for cycle in ("C1", "C2", "C3"):
        md = LAUNCH / f"{cycle}-VERSE-PACK.md"
        if md.exists():
            out = EXPORTS / f"KUTUMBA-{cycle}-VERSE-PACK-V12.1.docx"
            build_docx_from_md(md, out, f"{cycle} Verse Pack", cycle, "verse")
            outs.append(out)
    return outs


def build_weekly_packets() -> list[Path]:
    outs: list[Path] = []
    for code, slug in WEEKS:
        base = WEEKLY / slug
        for kind, rel, embed in [
            ("MAIN-FACILITATOR-GUIDE", "teacher/MAIN-FACILITATOR-GUIDE-V12.md", True),
            ("YOUNGER-TEACHER-GUIDE", "teacher/YOUNGER-TEACHER-GUIDE.md", True),
            ("OLDER-TEACHER-GUIDE", "teacher/OLDER-TEACHER-GUIDE.md", True),
            ("FAMILY-HANDOUT", "family-home-practice.md", False),
        ]:
            md = base / rel
            out = base / "exports" / f"KUTUMBA-{code}-{kind}-V12.1.docx"
            build_docx_from_md(md, out, f"{code} {kind.replace('-', ' ')}", code, kind.lower(), embed, slug)
            outs.append(out)

        # Weekly print packet W2–W18 style (also W1 mini)
        pkt = Document()
        apply_kutumba_styles(pkt)
        add_cover(pkt, f"{code} Weekly Print Packet", TAGLINE, code)
        add_header_footer(pkt, code, "weekly-print")
        add_callout(pkt, "TIME_CUE", "Saturday 2:00–4:00 · parents onsite · snack + water only")
        append_md(pkt, base / "overview.md" if (base / "overview.md").exists() else base / "teacher" / "MAIN-FACILITATOR-GUIDE-V12.md", "Week cover + objective")
        pngs = ensure_week_pngs(slug)
        if pngs:
            pkt.add_heading("Verse / concept visual", level=1)
            add_pngs(pkt, pngs[:2])
        append_md(pkt, base / "family-home-practice.md", "Family handout / home practice")
        append_md(pkt, base / "activities" / "YOUNGER-ACTIVITY-PACK.md", "Younger printable(s)")
        append_md(pkt, base / "activities" / "OLDER-ACTIVITY-PACK.md", "Older printable(s)")
        if (base / "project" / "CYCLE-CONTRIBUTION.md").exists():
            append_md(pkt, base / "project" / "CYCLE-CONTRIBUTION.md", "Project contribution")
        page_break(pkt)
        append_md(pkt, base / "activities" / "OLDER-ANSWER-KEY.md", "TEACHER-ONLY: Answer key")
        add_callout(pkt, "TEACHER_NOTE", "Teacher-only section — do not distribute to families.")
        page_break(pkt)
        append_md(pkt, base / "teacher" / "YOUNGER-TEACHER-GUIDE.md", "TEACHER-ONLY: Younger run sheet")
        append_md(pkt, base / "teacher" / "OLDER-TEACHER-GUIDE.md", "TEACHER-ONLY: Older run sheet")
        outp = EXPORTS / f"KUTUMBA-{code}-WEEKLY-PRINT-PACKET-V12.1.docx"
        pkt.save(outp)
        outs.append(outp)
    return outs


def convert_and_raster(docx_paths: list[Path]) -> list[dict]:
    QA.mkdir(parents=True, exist_ok=True)
    rows = []
    for docx in docx_paths:
        if not docx.exists():
            continue
        pdf = docx.with_suffix(".pdf")
        # Prefer Word COM; fall back to reportlab plain for resilience
        try:
            convert_with_word(docx, pdf)
        except Exception:
            # Minimal fallback: keep DOCX; skip PDF if Word unavailable
            if not pdf.exists():
                rows.append({"file": str(docx), "pdf": "", "pages": 0, "status": "PDF_CONVERT_FAIL"})
                continue
        if not pdf.exists():
            rows.append({"file": str(docx), "pdf": "", "pages": 0, "status": "PDF_MISSING"})
            continue
        try:
            pages, raster_dir = rasterize_pdf(pdf, docx)
        except Exception as exc:
            rows.append({"file": str(docx), "pdf": str(pdf), "pages": 0, "status": f"RASTER_FAIL:{exc}"})
            continue
        rows.append(
            {
                "file": str(docx.relative_to(REPO)),
                "pdf": str(pdf.relative_to(REPO)),
                "pages": pages,
                "raster_dir": str(raster_dir),
                "docx_sha256": sha256(docx),
                "pdf_sha256": sha256(pdf),
                "status": "RENDERED",
            }
        )
    return rows


def main() -> int:
    EXPORTS.mkdir(parents=True, exist_ok=True)
    all_docs: list[Path] = []
    all_docs.extend(build_owner_teacher_packets())
    all_docs.append(build_w1_saturday_packet())
    all_docs.extend(build_weekly_packets())
    # Deduplicate
    uniq: list[Path] = []
    seen = set()
    for p in all_docs:
        key = p.resolve()
        if key not in seen:
            seen.add(key)
            uniq.append(p)
    print(f"Rendered {len(uniq)} DOCX files")
    for p in uniq:
        print(" -", p.relative_to(REPO))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

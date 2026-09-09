#!/usr/bin/env python3
"""Raster Week-1 PDFs and build contact sheets for visual QA."""
from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

import pymupdf as fitz
from PIL import Image, ImageDraw

REPO = Path(__file__).resolve().parents[2]
PDF_ROOT = REPO / "exports" / "final" / "week1"
QA_ROOT = REPO / "build-evidence" / "v12_2-week1-rasters"
DPI = 190
PAGES_PER_SHEET = 8
EXPECTED_PDFS = {
    "KUTUMBA-C1-W1-START-HERE-V12.2.pdf",
    "KUTUMBA-C1-W1-OWNER-RUNBOOK-V12.2.pdf",
    "KUTUMBA-C1-W1-FAMILY-ORIENTATION-AND-COVENANT-V12.2.pdf",
    "KUTUMBA-C1-W1-PARENT-TRACK-V12.2.pdf",
    "KUTUMBA-C1-W1-YOUNGER-TEACHER-PACK-V12.2.pdf",
    "KUTUMBA-C1-W1-OLDER-TEACHER-PACK-V12.2.pdf",
    "KUTUMBA-C1-W1-SATURDAY-PRINT-PACKET-V12.2.pdf",
}


def _relative(path: Path) -> str:
    return path.resolve().relative_to(REPO.resolve()).as_posix()


def _contact_sheet(images: list[Path], output: Path, label: str) -> None:
    columns, rows = 2, 4
    thumb_width, thumb_height = 760, 984
    margin, header, gap = 30, 70, 20
    width = margin * 2 + columns * thumb_width + (columns - 1) * gap
    height = margin * 2 + header + rows * thumb_height + (rows - 1) * gap
    sheet = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(sheet)
    draw.text((margin, margin), label, fill="#5B1933")
    for index, image_path in enumerate(images):
        with Image.open(image_path) as source:
            image = source.convert("RGB")
            image.thumbnail((thumb_width, thumb_height), Image.Resampling.LANCZOS)
            column, row = index % columns, index // columns
            x = margin + column * (thumb_width + gap)
            y = margin + header + row * (thumb_height + gap)
            x += (thumb_width - image.width) // 2
            y += (thumb_height - image.height) // 2
            sheet.paste(image, (x, y))
            draw.rectangle(
                (x - 1, y - 1, x + image.width, y + image.height),
                outline="#C98916",
                width=2,
            )
    sheet.save(output, format="PNG", optimize=True)


def raster_pdf(pdf_path: Path) -> dict[str, object]:
    packet_dir = QA_ROOT / pdf_path.stem
    packet_dir.mkdir(parents=True, exist_ok=True)
    page_paths: list[Path] = []
    matrix = fitz.Matrix(DPI / 72, DPI / 72)
    with fitz.open(pdf_path) as pdf:
        if pdf.page_count < 1:
            raise RuntimeError(f"PDF contains no pages: {pdf_path}")
        for page_number, page in enumerate(pdf, 1):
            output = packet_dir / f"page-{page_number:03d}.png"
            page.get_pixmap(matrix=matrix, alpha=False).save(output)
            page_paths.append(output)

    contact_paths: list[Path] = []
    for start in range(0, len(page_paths), PAGES_PER_SHEET):
        group = page_paths[start : start + PAGES_PER_SHEET]
        sheet_number = start // PAGES_PER_SHEET + 1
        output = packet_dir / f"contact-sheet-{sheet_number:03d}.png"
        _contact_sheet(
            group,
            output,
            f"{pdf_path.stem} • pages {start + 1}–{start + len(group)}",
        )
        contact_paths.append(output)
    return {
        "pdf": _relative(pdf_path),
        "page_count": len(page_paths),
        "dpi": DPI,
        "rasters": [_relative(path) for path in page_paths],
        "contact_sheets": [_relative(path) for path in contact_paths],
    }


def main() -> int:
    missing = sorted(name for name in EXPECTED_PDFS if not (PDF_ROOT / name).is_file())
    if missing:
        raise FileNotFoundError(
            "Render the complete Week-1 set first; missing PDFs: " + ", ".join(missing)
        )
    if QA_ROOT.exists():
        shutil.rmtree(QA_ROOT)
    QA_ROOT.mkdir(parents=True)

    packets = []
    for pdf_path in sorted((PDF_ROOT / name for name in EXPECTED_PDFS), key=lambda p: p.name):
        result = raster_pdf(pdf_path)
        packets.append(result)
        print(
            f"{pdf_path.name}: {result['page_count']} pages, "
            f"{len(result['contact_sheets'])} contact sheets"
        )
    manifest = QA_ROOT / "manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "dpi": DPI,
                "max_pages_per_contact_sheet": PAGES_PER_SHEET,
                "packets": packets,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {_relative(manifest)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

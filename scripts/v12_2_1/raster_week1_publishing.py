#!/usr/bin/env python3
"""Raster all repaired C1-W1 PDFs and produce contact sheets."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

import pymupdf as fitz
from PIL import Image, ImageDraw

REPO = Path(__file__).resolve().parents[2]
PDF_ROOT = REPO / "exports" / "final" / "week1"
OUT = REPO / "build-evidence" / "v12_2_1-week1-rasters"
DPI = 190
MAX_SHEET = 8


def rel(path: Path) -> str:
    return path.resolve().relative_to(REPO.resolve()).as_posix()


def sheet(paths: list[Path], target: Path) -> tuple[int, int]:
    tw, th, gap = 570, 738, 18
    image = Image.new("RGB", (tw * 2 + gap * 3, th * 4 + gap * 5), "white")
    draw = ImageDraw.Draw(image)
    for i, path in enumerate(paths):
        with Image.open(path) as opened:
            page = opened.convert("RGB")
            page.thumbnail((tw, th), Image.Resampling.LANCZOS)
            x = gap + (i % 2) * (tw + gap) + (tw - page.width) // 2
            y = gap + (i // 2) * (th + gap) + (th - page.height) // 2
            image.paste(page, (x, y))
            draw.rectangle((x, y, x + page.width, y + page.height), outline="#5B1933", width=2)
    image.save(target, "PNG", optimize=True)
    return image.size


def main() -> int:
    pdfs = sorted(PDF_ROOT.glob("*.pdf"))
    if len(pdfs) != 7:
        raise RuntimeError(f"Expected 7 PDFs, found {len(pdfs)}")
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    manifest = {"packets": []}
    matrix = fitz.Matrix(DPI / 72, DPI / 72)
    for pdf_path in pdfs:
        directory = OUT / pdf_path.stem
        directory.mkdir()
        pages = []
        with fitz.open(pdf_path) as pdf:
            for number, page in enumerate(pdf, 1):
                path = directory / f"page-{number:03d}.png"
                pix = page.get_pixmap(matrix=matrix, alpha=False)
                pix.save(path)
                pages.append({"path": rel(path), "width": pix.width, "height": pix.height})
        contacts = []
        page_paths = [REPO / item["path"] for item in pages]
        for start in range(0, len(page_paths), MAX_SHEET):
            path = directory / f"contact-sheet-{start // MAX_SHEET + 1:03d}.png"
            width, height = sheet(page_paths[start:start + MAX_SHEET], path)
            contacts.append({"path": rel(path), "width": width, "height": height})
        manifest["packets"].append({"path": rel(pdf_path), "pages": pages, "contact_sheets": contacts})
        print(f"{pdf_path.name}: {len(pages)} pages, {len(contacts)} contact sheets")
    target = OUT / "manifest.json"
    target.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {rel(target)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

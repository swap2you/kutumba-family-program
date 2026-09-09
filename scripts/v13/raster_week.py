#!/usr/bin/env python3
"""Raster V13 week PDFs at ~200 DPI; contact sheets max 8/page. Manifest reports dimensions/paths only."""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

import pymupdf as fitz
import yaml
from PIL import Image, ImageDraw

REPO = Path(__file__).resolve().parents[2]
V13 = Path(__file__).resolve().parent
REGISTRY = V13 / "week_registry.yaml"
DPI = 200
MAX_SHEET = 8


def rel(path: Path) -> str:
    return path.resolve().relative_to(REPO.resolve()).as_posix()


def load_entry(week_id: str) -> dict:
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    for row in data["weeks"]:
        if row["id"] == week_id:
            return row
    raise SystemExit(f"Unknown week id {week_id!r}")


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
    parser = argparse.ArgumentParser(description="Raster one V13 week PDF set.")
    parser.add_argument("--week", required=True, help="Week id, e.g. C1-W2")
    args = parser.parse_args()
    entry = load_entry(args.week)
    pdf_root = REPO / "exports" / "final" / "v13" / Path(entry["export_subdir"])
    out = REPO / "build-evidence" / "v13" / entry["id"] / "rasters"
    pdfs = sorted(pdf_root.glob("*.pdf"))
    if len(pdfs) != 7:
        raise SystemExit(f"Expected 7 PDFs under {rel(pdf_root)}, found {len(pdfs)}")
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    manifest: dict = {
        "week": entry["id"],
        "dpi": DPI,
        "max_sheet": MAX_SHEET,
        "note": "Automated raster tool reports dimensions and paths only; it does not claim visual inspection.",
        "packets": [],
    }
    matrix = fitz.Matrix(DPI / 72, DPI / 72)
    for pdf_path in pdfs:
        directory = out / pdf_path.stem
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
        manifest["packets"].append({
            "path": rel(pdf_path),
            "page_count": len(pages),
            "pages": pages,
            "contact_sheets": contacts,
        })
        print(f"{pdf_path.name}: {len(pages)} pages, {len(contacts)} contact sheets")
    target = out / "manifest.json"
    target.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {rel(target)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

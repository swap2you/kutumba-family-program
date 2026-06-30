#!/usr/bin/env python3
"""Replace machine-specific absolute paths in reference indexes with portable source-root IDs."""

from __future__ import annotations

import csv
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
INDEX_DIR = REPO / "00-source-materials" / "03-external-reference-index"

ROOT_MAP = {
    r"C:\Users\swap2\Downloads\Personal\5. Devotional\1. Baktivriksha\BV Material": "jayapataka-bv",
    r"C:\Users\swap2\Downloads\Personal\5. Devotional\1. Baktivriksha": "legacy-bhaktivriksha",
    r"C:\Users\swap2\Downloads\Personal\5. Devotional\Granth": "granth",
    r"C:\Users\swap2\Downloads\Personal\0. KUTUMBA SANGA": "kutumba-sanga",
}

CSV_FILES = [
    "LEGACY-BHAKTIVRIKSHA-FILE-INDEX.csv",
    "GRANTH-PDF-CATALOG.csv",
    "JAYAPATAKA-SWAMI-BV-MATERIAL-INDEX.csv",
]


def portable_path(absolute: str) -> str:
    if not absolute:
        return absolute
    norm = absolute.replace("/", "\\")
    # longest match first
    for prefix in sorted(ROOT_MAP, key=len, reverse=True):
        if norm.lower().startswith(prefix.lower()):
            rel = norm[len(prefix) :].lstrip("\\/")
            root_id = ROOT_MAP[prefix]
            return f"{root_id}:{rel.replace(chr(92), '/')}"
    if re.match(r"^[A-Za-z]:\\", norm):
        return f"unmapped-local:{norm.split('Personal\\', 1)[-1].replace(chr(92), '/')}"
    return absolute


def migrate_csv(path: Path) -> int:
    rows: list[dict[str, str]] = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        if "source_root_id" not in fieldnames:
            fieldnames.append("source_root_id")
        if "portable_source_path" not in fieldnames:
            fieldnames.append("portable_source_path")
        for row in reader:
            local = row.get("local_source_path", "")
            portable = portable_path(local)
            if ":" in portable:
                row["source_root_id"], row["portable_source_path"] = portable.split(":", 1)
            else:
                row["source_root_id"] = ""
                row["portable_source_path"] = portable
            rows.append(row)

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def main() -> None:
    for name in CSV_FILES:
        p = INDEX_DIR / name
        count = migrate_csv(p)
        print(f"Migrated {name}: {count} rows")


if __name__ == "__main__":
    main()

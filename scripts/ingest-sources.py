#!/usr/bin/env python3
"""KUTUMBA source ingestion: copy current documents, index legacy references."""

import csv
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(r"C:\Development\Workspace\DevotionalRepo\kutumba-family-program")
CURRENT_SRC = Path(r"C:\Users\swap2\Downloads\Personal\0. KUTUMBA SANGA")
DEST_CURRENT = REPO_ROOT / "00-source-materials" / "01-current-kutumba-originals"
DEST_INDEX = REPO_ROOT / "00-source-materials" / "03-external-reference-index"
BUILD_EVIDENCE = REPO_ROOT / "build-evidence"

SUPPORTED_EXT = {
    ".docx", ".pdf", ".pptx", ".xlsx", ".md", ".txt", ".csv",
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg",
    ".mp3", ".wav", ".m4a",
}

EXCLUDE_PATTERNS = [re.compile(r"^~\$"), re.compile(r"\.tmp$"), re.compile(r"Thumbs\.db$")]

LEGACY_SOURCES = [
    {
        "id": "legacy-bhaktivriksha",
        "name": "LegacyBhaktivriksha",
        "path": Path(r"C:\Users\swap2\Downloads\Personal\5. Devotional\1. Baktivriksha"),
        "exclude_subpath": "BV Material",
        "csv": "LEGACY-BHAKTIVRIKSHA-FILE-INDEX.csv",
    },
    {
        "id": "granth",
        "name": "Granth",
        "path": Path(r"C:\Users\swap2\Downloads\Personal\5. Devotional\Granth"),
        "exclude_subpath": None,
        "csv": "GRANTH-PDF-CATALOG.csv",
    },
    {
        "id": "jayapataka-bv",
        "name": "JayapatakaSwamiBV",
        "path": Path(r"C:\Users\swap2\Downloads\Personal\5. Devotional\1. Baktivriksha\BV Material"),
        "exclude_subpath": None,
        "csv": "JAYAPATAKA-SWAMI-BV-MATERIAL-INDEX.csv",
    },
]

WORKSTREAM_MAP = {
    "governance": ["governance", "charter", "policy"],
    "curriculum-architecture": ["curriculum architecture", "three-year", "3 yrs"],
    "first-six-months": ["six-month", "6-month", "first six"],
    "children-youth": ["children", "youth"],
    "parent-formation": ["parent formation", "family care"],
    "prasadam-operations": ["prasada", "prasadam", "hospitality"],
    "kirtana-worship": ["kirtana", "worship", "bhakti lab", "devotional system", "9 steps"],
    "festivals-calendar": ["calendar", "festival", "yatra"],
    "master-operating": ["master operating"],
    "digital-repository": ["repository", "digital", "website", "drive"],
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def should_exclude(name: str) -> bool:
    return any(p.search(name) for p in EXCLUDE_PATTERNS)


def infer_workstream(rel_path: str, filename: str) -> str:
    text = (rel_path + " " + filename).lower()
    for ws, keywords in WORKSTREAM_MAP.items():
        if any(k in text for k in keywords):
            return ws
    return "unclassified"


def infer_privacy(filename: str) -> str:
    low = filename.lower()
    if any(x in low for x in ["private", "personal", "family record", "form completed"]):
        return "restricted"
    return "internal-project"


def infer_rights(ext: str, collection: str) -> str:
    if collection == "current":
        return "kutumba-authored-project-document"
    if ext == ".pdf":
        return "reference-only-rights-review-required"
    return "reference-only-index-only"


def iter_files(root: Path, exclude_subpath: str | None = None):
    if not root.exists():
        return
    for dirpath, dirnames, filenames in os.walk(root):
        if exclude_subpath:
            dirnames[:] = [d for d in dirnames if d != exclude_subpath and not d.startswith(".")]
        for fn in filenames:
            if should_exclude(fn):
                continue
            yield Path(dirpath) / fn


def copy_current_sources():
    entries = []
    counter = 1
    for src_file in sorted(iter_files(CURRENT_SRC)):
        rel = src_file.relative_to(CURRENT_SRC)
        ext = src_file.suffix.lower()
        if ext not in SUPPORTED_EXT:
            continue
        dest = DEST_CURRENT / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists() or dest.stat().st_size != src_file.stat().st_size:
            import shutil
            shutil.copy2(src_file, dest)
        file_hash = sha256_file(src_file)
        dest_hash = sha256_file(dest)
        sid = f"KUT-SRC-{counter:04d}"
        counter += 1
        entries.append({
            "source_id": sid,
            "source_folder": "0. KUTUMBA SANGA",
            "original_absolute_path": str(src_file),
            "repository_relative_path": str(dest.relative_to(REPO_ROOT)).replace("\\", "/"),
            "original_filename": src_file.name,
            "normalized_title": src_file.stem.replace("_", " "),
            "file_type": ext.lstrip("."),
            "byte_size": src_file.stat().st_size,
            "sha256": file_hash,
            "dest_sha256": dest_hash,
            "modified_timestamp": datetime.fromtimestamp(src_file.stat().st_mtime, tz=timezone.utc).isoformat(),
            "likely_workstream": infer_workstream(str(rel.parent), src_file.name),
            "version": _extract_version(src_file.name),
            "status": "ingested",
            "privacy_class": infer_privacy(src_file.name),
            "rights_status": infer_rights(ext, "current"),
            "canonicalization_status": "pending",
            "notes": "parity-verified" if file_hash == dest_hash else "HASH_MISMATCH",
        })
    return entries


def _extract_version(name: str) -> str:
    m = re.search(r"v(\d+\.\d+)", name, re.I)
    return m.group(0) if m else ""


def index_legacy_source(spec: dict) -> list[dict]:
    rows = []
    root = spec["path"]
    if not root.exists():
        return rows
    for src_file in sorted(iter_files(root, spec.get("exclude_subpath"))):
        try:
            rel = src_file.relative_to(root)
            stat = src_file.stat()
        except (OSError, ValueError):
            continue
        ext = src_file.suffix.lower()
        try:
            file_hash = sha256_file(src_file)
        except OSError:
            file_hash = ""
        rows.append({
            "collection": spec["name"],
            "local_source_path": str(src_file),
            "relative_path": str(rel).replace("\\", "/"),
            "filename": src_file.name,
            "extension": ext,
            "size_bytes": stat.st_size,
            "modified_date": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
            "sha256": file_hash,
            "title_inferred": src_file.stem[:120],
            "author_publisher": "",
            "category": _legacy_category(ext, str(rel)),
            "language": _infer_language(src_file.name),
            "likely_topic": "",
            "rights_status": infer_rights(ext, "legacy"),
            "review_status": "not-reviewed",
            "possible_kutumba_relevance": "research-only",
            "duplicate_group": "",
        })
    return rows


def _legacy_category(ext: str, rel: str) -> str:
    low = rel.lower()
    if ext == ".pdf":
        return "pdf-reference"
    if ext in {".docx", ".doc"}:
        return "document"
    if ext in {".mp3", ".wav", ".m4a"}:
        return "audio"
    if ext in {".pptx", ".ppt"}:
        return "presentation"
    if "lesson" in low or "module" in low:
        return "lesson-material"
    return "other"


def _infer_language(name: str) -> str:
    if any(x in name for x in ["Hindi", "hindi", "हिं"]):
        return "hi"
    return "en"


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def detect_duplicates(*row_sets: list[dict]) -> list[dict]:
    by_hash: dict[str, list] = {}
    for rows in row_sets:
        for r in rows:
            h = r.get("sha256", "")
            if not h:
                continue
            by_hash.setdefault(h, []).append(r)
    dups = []
    for h, group in by_hash.items():
        if len(group) > 1:
            paths = [g.get("local_source_path") or g.get("original_absolute_path", "") for g in group]
            dups.append({"sha256": h, "count": len(group), "paths": " | ".join(paths[:5])})
    return dups


def main():
    DEST_CURRENT.mkdir(parents=True, exist_ok=True)
    DEST_INDEX.mkdir(parents=True, exist_ok=True)
    BUILD_EVIDENCE.mkdir(parents=True, exist_ok=True)

    print("Copying current KUTUMBA sources...")
    current = copy_current_sources()
    print(f"  Copied {len(current)} files")

    legacy_all = []
    for spec in LEGACY_SOURCES:
        print(f"Indexing {spec['name']}...")
        rows = index_legacy_source(spec)
        legacy_all.extend(rows)
        fields = list(rows[0].keys()) if rows else [
            "collection", "local_source_path", "relative_path", "filename", "extension",
            "size_bytes", "modified_date", "sha256", "title_inferred", "author_publisher",
            "category", "language", "likely_topic", "rights_status", "review_status",
            "possible_kutumba_relevance", "duplicate_group",
        ]
        write_csv(DEST_INDEX / spec["csv"], rows, fields)
        print(f"  Indexed {len(rows)} files -> {spec['csv']}")

    dups = detect_duplicates(legacy_all)
    dup_path = DEST_INDEX / "REFERENCE-DUPLICATE-HASH-REPORT.md"
    with open(dup_path, "w", encoding="utf-8") as f:
        f.write("# Reference Duplicate Hash Report\n\n")
        f.write(f"Generated: {datetime.now(timezone.utc).isoformat()}\n\n")
        f.write(f"Duplicate hash groups found: {len(dups)}\n\n")
        for d in dups[:100]:
            f.write(f"- `{d['sha256'][:16]}...` ({d['count']} files): {d['paths']}\n")
        if len(dups) > 100:
            f.write(f"\n... and {len(dups) - 100} more groups.\n")

    manifest = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "current_source_root": str(CURRENT_SRC),
        "current_document_count": len(current),
        "legacy_index_count": len(legacy_all),
        "entries": current,
    }
    manifest_path = REPO_ROOT / "00-source-materials" / "SOURCE-MANIFEST.yaml"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        import yaml
        with open(manifest_path, "w", encoding="utf-8") as f:
            yaml.dump(manifest, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    except ImportError:
        with open(manifest_path.with_suffix(".json"), "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)
        manifest_path = manifest_path.with_suffix(".json")

    inv_path = REPO_ROOT / "00-source-materials" / "SOURCE-INVENTORY.md"
    with open(inv_path, "w", encoding="utf-8") as f:
        f.write("# KUTUMBA Source Inventory\n\n")
        f.write(f"Generated: {datetime.now(timezone.utc).isoformat()}\n\n")
        f.write("## Current KUTUMBA originals\n\n")
        f.write(f"Total: **{len(current)}** files copied to `00-source-materials/01-current-kutumba-originals/`\n\n")
        f.write("| ID | File | Workstream | SHA-256 (prefix) | Size |\n")
        f.write("|---|---|---|---|---|\n")
        for e in current:
            f.write(
                f"| {e['source_id']} | {e['original_filename']} | {e['likely_workstream']} "
                f"| `{e['sha256'][:12]}...` | {e['byte_size']} |\n"
            )
        f.write("\n## Legacy/reference collections (index only)\n\n")
        for spec in LEGACY_SOURCES:
            count = sum(1 for r in legacy_all if r["collection"] == spec["name"])
            f.write(f"- **{spec['name']}**: {count} files indexed in `03-external-reference-index/{spec['csv']}`\n")

    register = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "collections": [
            {"id": s["id"], "name": s["name"], "path": str(s["path"]), "mode": "index-only"}
            for s in LEGACY_SOURCES
        ],
        "total_indexed": len(legacy_all),
        "duplicate_groups": len(dups),
    }
    reg_path = DEST_INDEX / "REFERENCE-SOURCE-REGISTER.yaml"
    try:
        import yaml
        with open(reg_path, "w", encoding="utf-8") as f:
            yaml.dump(register, f, default_flow_style=False, sort_keys=False)
    except ImportError:
        with open(reg_path.with_suffix(".json"), "w", encoding="utf-8") as f:
            json.dump(register, f, indent=2)

    rights_path = DEST_INDEX / "REFERENCE-RIGHTS-AND-USE-REVIEW.md"
    with open(rights_path, "w", encoding="utf-8") as f:
        f.write("# Reference Rights and Use Review\n\n")
        f.write("## Policy\n\n")
        f.write("Legacy Bhaktivriksha, Granth, and Jayapataka Swami BV Material collections are ")
        f.write("**reference-only**. They are indexed in this repository but not bulk-copied into Git.\n\n")
        f.write("## Indexed collections\n\n")
        for spec in LEGACY_SOURCES:
            count = sum(1 for r in legacy_all if r["collection"] == spec["name"])
            f.write(f"- {spec['name']}: {count} files — rights status: reference-only-rights-review-required\n")
        f.write("\n## Required human review\n\n")
        f.write("- Copyright and redistribution rights for any item proposed for adoption\n")
        f.write("- Worship authorization for any liturgical content\n")
        f.write("- Child-safety review for youth-facing legacy modules\n")
        f.write("- Doctrinal alignment review before adaptation\n")

    report_path = BUILD_EVIDENCE / "SOURCE-INGESTION-REPORT.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# Source Ingestion Report\n\n")
        f.write(f"Date: {datetime.now(timezone.utc).isoformat()}\n\n")
        f.write("## Summary\n\n")
        f.write(f"- Current KUTUMBA documents copied: **{len(current)}**\n")
        f.write(f"- Legacy/reference files indexed (metadata only): **{len(legacy_all)}**\n")
        f.write(f"- Duplicate hash groups: **{len(dups)}**\n")
        f.write(f"- Original Downloads folder preserved: **yes** (copy-only operation)\n\n")
        f.write("## Current source files\n\n")
        for e in current:
            f.write(f"- `{e['source_id']}` — {e['original_filename']} — `{e['sha256']}`\n")
        f.write("\n## Legacy index outputs\n\n")
        for spec in LEGACY_SOURCES:
            f.write(f"- `03-external-reference-index/{spec['csv']}`\n")
        f.write("- `03-external-reference-index/REFERENCE-SOURCE-REGISTER.yaml`\n")
        f.write("- `03-external-reference-index/REFERENCE-RIGHTS-AND-USE-REVIEW.md`\n")
        f.write("- `03-external-reference-index/REFERENCE-DUPLICATE-HASH-REPORT.md`\n")

    summary = {
        "current_count": len(current),
        "legacy_count": len(legacy_all),
        "duplicates": len(dups),
    }
    print(json.dumps(summary))
    return 0


if __name__ == "__main__":
    sys.exit(main())

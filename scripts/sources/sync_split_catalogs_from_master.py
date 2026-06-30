#!/usr/bin/env python3
"""Regenerate split catalogs and PUBLIC-SOURCE-DIRECTORY from MASTER."""
from __future__ import annotations

import sys
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

import yaml

REPO = Path(__file__).resolve().parents[2]
CATALOG_DIR = REPO / "14-research-source-register/public-source-catalog"
MASTER_PATH = CATALOG_DIR / "MASTER-SOURCE-CATALOG.yaml"
DIRECTORY_MD = REPO / "09-digital-repository-publishing/PUBLIC-SOURCE-DIRECTORY.md"


def bucket_for(e: dict) -> str:
    url = e.get("exact_entry_url", "").lower()
    tier = e.get("authority_tier", "C")
    if tier == "supplementary":
        return "supplementary"
    if tier == "B":
        return "secondary"
    if tier == "C":
        return "media"
    if "iskconeducation" in url or "iskconcongregation" in url or "iskconmumbai" in url:
        return "education"
    return "primary"


def enrich_entry(e: dict) -> dict:
    e = dict(e)
    url = e.get("exact_entry_url", "")
    host = urlparse(url).netloc.lower()
    langs = list(e.get("languages") or ["en"])
    ctypes = list(e.get("content_types") or ["web"])
    if "/es/" in url and "es" not in langs:
        langs = ["es"] + [x for x in langs if x != "es"]
    if url.lower().endswith(".pdf") and "pdf" not in ctypes:
        ctypes.append("pdf")
    if "youtube.com" in host:
        ctypes = ["video-channel"]
    if "audio.iskcondesiretree" in host or "/audios/" in url:
        if "audio" not in ctypes:
            ctypes.append("audio")
    if "/ebook" in url or "ebooks." in host:
        if "ebook-catalog" not in ctypes:
            ctypes.append("ebook-catalog")
    e["languages"] = langs
    e["content_types"] = ctypes
    if e.get("authority_tier") == "supplementary":
        e["primary_or_secondary"] = "supplementary"
    e.pop("_catalog_bucket", None)
    return e


def write_yaml(path: Path, body: dict) -> None:
    path.write_text(yaml.safe_dump(body, sort_keys=False, allow_unicode=True, width=120), encoding="utf-8")


def build_directory(entries: list[dict]) -> str:
    today = date.today().isoformat()
    tiers = ["A", "B", "C", "supplementary"]
    lines = [
        "# Public Source Directory",
        "",
        f"Generated: {today} — user-friendly index derived from `MASTER-SOURCE-CATALOG.yaml`",
        "",
        "Canonical provenance: [PUBLIC-SOURCE-MAP-FOR-PRABHUPADA-AND-SANATANA-CONTENT.md](PUBLIC-SOURCE-MAP-FOR-PRABHUPADA-AND-SANATANA-CONTENT.md)",
        "",
        "Machine-readable catalog: [../14-research-source-register/public-source-catalog/README.md](../14-research-source-register/public-source-catalog/README.md)",
        "",
        "> Public access is not permission to redistribute. Default use: link and metadata only.",
        "",
    ]
    for tier in tiers:
        group = [e for e in entries if e.get("authority_tier") == tier]
        if not group:
            continue
        lines.append(f"## Tier {tier} ({len(group)} entries)")
        lines.append("")
        for e in sorted(group, key=lambda x: x.get("source_name", "")):
            status = e.get("status", "pending")
            rights = e.get("rights_posture", "")
            name = e.get("source_name", "")
            url = e.get("exact_entry_url", "")
            cat = e.get("source_category", "")
            lines.append(f"- [{name}]({url}) — `{cat}` — {status} — {rights}")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    data = yaml.safe_load(MASTER_PATH.read_text(encoding="utf-8"))
    entries = [enrich_entry(e) for e in data.get("entries", [])]
    data["entries"] = entries
    data["entry_count"] = len(entries)
    data["generated"] = date.today().isoformat()
    write_yaml(MASTER_PATH, data)

    buckets: dict[str, list] = {k: [] for k in ["primary", "secondary", "education", "supplementary", "media"]}
    for e in entries:
        buckets[bucket_for(e)].append(e)

    mapping = {
        "primary": "PRABHUPADA-PRIMARY-AND-ARCHIVAL.yaml",
        "secondary": "PRABHUPADA-STRUCTURED-SECONDARY.yaml",
        "education": "ISKCON-EDUCATION-AND-CONGREGATION.yaml",
        "supplementary": "SUPPLEMENTARY-GAUDIYA-SANATANA.yaml",
        "media": "MEDIA-AND-YOUTUBE-DISCOVERY.yaml",
    }
    for b, fname in mapping.items():
        write_yaml(CATALOG_DIR / fname, {"catalog_version": "1.0.0", "generated": date.today().isoformat(), "entries": buckets[b]})

    DIRECTORY_MD.write_text(build_directory(entries), encoding="utf-8")
    tiers = Counter(e["authority_tier"] for e in entries)
    print(f"Synced {len(entries)} entries; tiers={dict(tiers)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

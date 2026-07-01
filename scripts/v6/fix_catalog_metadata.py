#!/usr/bin/env python3
"""V6 catalog metadata corrections and Gita Press deduplication."""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
CATALOG_DIR = REPO / "14-research-source-register/public-source-catalog"
MASTER = CATALOG_DIR / "MASTER-SOURCE-CATALOG.yaml"
ALIAS = CATALOG_DIR / "SOURCE-ALIAS-AND-MIRROR-MAP.yaml"

sys.path.insert(0, str(REPO / "scripts" / "sources"))
from url_cleanup import clean_url  # noqa: E402


def main() -> int:
    data = yaml.safe_load(MASTER.read_text(encoding="utf-8"))
    entries = data.get("entries", [])
    removed = []
    kept = []
    for e in entries:
        url = clean_url(e.get("exact_entry_url", ""))
        e["exact_entry_url"] = url
        if e["source_id"] == "PSC-0078-gitapress-org-ebook":
            removed.append(e["source_id"])
            continue
        kept.append(e)

    by_id = {e["source_id"]: e for e in kept}
    if "PSC-0076-gitapress-org-ebook" in by_id:
        by_id["PSC-0076-gitapress-org-ebook"]["notes"] = (
            "Canonical Gita Press ebook portal; PSC-0078 removed as srsltid tracking duplicate"
        )

    if "PSC-0073-harikatha-com-audios" in by_id:
        e = by_id["PSC-0073-harikatha-com-audios"]
        e["source_category"] = "gaudiya-supplementary-audio"
        e["canonical_for"] = "narayana-maharaja-supplementary-audio"
        e["owner_or_publisher"] = "Gaudiya Vedanta Publications (Narayana Maharaja lineage)"
        e["content_types"] = ["web", "audio-archive"]
        e["notes"] = "Supplementary Gauḍīya audio — not Śrīla Prabhupāda primary audio"

    if "PSC-0079-www-bbti-org" in by_id:
        e = by_id["PSC-0079-www-bbti-org"]
        e["source_name"] = "BBT International"
        e["owner_or_publisher"] = "Bhaktivedanta Book Trust International"
        e["source_category"] = "bbt-publishing-reference"
        e["content_types"] = ["web", "publishing-info"]
        e["rights_posture"] = "link-and-metadata-only"
        e["notes"] = "BBT International publishing reference — not primary scripture access"

    if "PSC-0008-vedabase-io-es-library" in by_id:
        e = by_id["PSC-0008-vedabase-io-es-library"]
        e["languages"] = ["es"]
        e["canonical_for"] = "prabhupada-text-spanish"
        e["notes"] = "Spanish VedaBase library — language metadata es only"

    data["entries"] = list(by_id.values())
    data["catalog_version"] = "1.1.0"
    data["generated"] = str(date.today())
    data["entry_count"] = len(data["entries"])
    MASTER.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")

    alias_data = yaml.safe_load(ALIAS.read_text(encoding="utf-8")) if ALIAS.exists() else {"aliases": []}
    aliases = alias_data.get("aliases", [])
    aliases = [a for a in aliases if a.get("canonical_id") != "PSC-0078-gitapress-org-ebook"]
    aliases.append(
        {
            "alias_url": "https://gitapress.org/ebook?srsltid=AfmBOooLplTSZKY1WxEmayhC2D4KHsq1ZBmgpwpT-v1oEQakHCavH_5a",
            "canonical_id": "PSC-0076-gitapress-org-ebook",
            "reason": "srsltid tracking duplicate removed v6",
        }
    )
    alias_data["aliases"] = aliases
    ALIAS.write_text(yaml.safe_dump(alias_data, sort_keys=False, allow_unicode=True), encoding="utf-8")

    queue_path = CATALOG_DIR / "SOURCE-VERIFICATION-QUEUE.yaml"
    q = yaml.safe_load(queue_path.read_text(encoding="utf-8"))
    q["queue"] = [i for i in q.get("queue", []) if i.get("item_id") != "PSC-0078-gitapress-org-ebook"]
    queue_path.write_text(yaml.safe_dump(q, sort_keys=False, allow_unicode=True), encoding="utf-8")

    print(f"Master catalog: {len(entries)} -> {len(data['entries'])} entries")
    print(f"Removed duplicates: {removed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

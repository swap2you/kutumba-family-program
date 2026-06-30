#!/usr/bin/env python3
"""Build machine-readable public source catalogs from the canonical source map."""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

import yaml

REPO = Path(__file__).resolve().parents[2]
CANONICAL = REPO / "09-digital-repository-publishing/PUBLIC-SOURCE-MAP-FOR-PRABHUPADA-AND-SANATANA-CONTENT.md"
CATALOG_DIR = REPO / "14-research-source-register/public-source-catalog"

REPO = Path(__file__).resolve().parents[2]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from scripts.sources.url_cleanup import clean_url, extract_urls, strip_cite_markers  # noqa: E402

TODAY = date.today().isoformat()

DOMAIN_META: dict[str, dict] = {
    "vedabase.io": {
        "source_name": "Bhaktivedanta VedaBase",
        "owner_or_publisher": "Bhaktivedanta Book Trust / VedaBase",
        "authority_tier": "A",
        "catalog": "primary",
        "rights_posture": "link-and-metadata-only",
        "canonical_for": "prabhupada-text-transcripts-letters",
    },
    "www.prabhupada.com": {
        "source_name": "Bhaktivedanta Archives",
        "owner_or_publisher": "Bhaktivedanta Archives",
        "authority_tier": "A",
        "catalog": "primary",
        "rights_posture": "link-and-metadata-only",
        "canonical_for": "prabhupada-archival-provenance",
    },
    "prabhupada.com": {
        "source_name": "Bhaktivedanta Archives",
        "owner_or_publisher": "Bhaktivedanta Archives",
        "authority_tier": "A",
        "catalog": "primary",
        "rights_posture": "link-and-metadata-only",
        "canonical_for": "prabhupada-archival-provenance",
    },
    "bbt.org": {
        "source_name": "Bhaktivedanta Book Trust",
        "owner_or_publisher": "BBT",
        "authority_tier": "A",
        "catalog": "primary",
        "rights_posture": "permission-required-before-republication",
        "canonical_for": "bbt-publishing-rights",
    },
    "bbtmedia.com": {
        "source_name": "BBT Media",
        "owner_or_publisher": "BBT",
        "authority_tier": "A",
        "catalog": "primary",
        "rights_posture": "permission-required-before-republication",
        "canonical_for": "bbt-digital-editions",
    },
    "krishna.com": {
        "source_name": "Krishna.com",
        "owner_or_publisher": "BBT",
        "authority_tier": "A",
        "catalog": "primary",
        "rights_posture": "link-and-metadata-only",
        "canonical_for": "bbt-online-reading",
    },
    "www.asitis.com": {
        "source_name": "As It Is — Bhagavad-gita",
        "owner_or_publisher": "BBT-affiliated Gita front end",
        "authority_tier": "A",
        "catalog": "primary",
        "rights_posture": "link-and-metadata-only",
        "canonical_for": "bg-verse-deep-links",
    },
    "asitis.com": {
        "source_name": "As It Is — Bhagavad-gita",
        "owner_or_publisher": "BBT-affiliated Gita front end",
        "authority_tier": "A",
        "catalog": "primary",
        "rights_posture": "link-and-metadata-only",
        "canonical_for": "bg-verse-deep-links",
    },
    "prabhupadavani.org": {
        "source_name": "PrabhupadaVani",
        "owner_or_publisher": "PrabhupadaVani",
        "authority_tier": "B",
        "catalog": "secondary",
        "rights_posture": "link-and-metadata-only",
        "canonical_for": "prabhupada-audio-transcript-discovery",
        "mirror_of": "vedabase.io",
    },
    "vanisource.org": {
        "source_name": "Vanisource",
        "owner_or_publisher": "Vanipedia Foundation",
        "authority_tier": "B",
        "catalog": "secondary",
        "rights_posture": "link-and-metadata-only",
        "canonical_for": "structured-prabhupada-text-discovery",
        "mirror_of": "vedabase.io",
    },
    "vaniquotes.org": {
        "source_name": "Vaniquotes",
        "owner_or_publisher": "Vanipedia Foundation",
        "authority_tier": "B",
        "catalog": "secondary",
        "rights_posture": "link-and-metadata-only",
        "canonical_for": "thematic-quote-clustering",
        "mirror_of": "vedabase.io",
    },
    "vanipedia.org": {
        "source_name": "Vanipedia",
        "owner_or_publisher": "Vanipedia Foundation",
        "authority_tier": "B",
        "catalog": "secondary",
        "rights_posture": "link-and-metadata-only",
        "canonical_for": "encyclopedic-prabhupada-research",
        "mirror_of": "vedabase.io",
    },
    "iskconeducation.org": {
        "source_name": "ISKCON Ministry of Education",
        "owner_or_publisher": "ISKCON Ministry of Education",
        "authority_tier": "A",
        "catalog": "education",
        "rights_posture": "link-and-metadata-only",
        "canonical_for": "official-iskcon-education-resources",
    },
    "iskconcongregation.com": {
        "source_name": "ISKCON Congregational Development",
        "owner_or_publisher": "ISKCON Congregation Ministry",
        "authority_tier": "A",
        "catalog": "education",
        "rights_posture": "link-and-metadata-only",
        "canonical_for": "bhakti-vriksha-congregation-resources",
    },
    "www.iskconmumbai.com": {
        "source_name": "ISKCON Mumbai (Juhu)",
        "owner_or_publisher": "ISKCON Mumbai",
        "authority_tier": "A",
        "catalog": "education",
        "rights_posture": "link-and-metadata-only",
        "canonical_for": "temple-context-reference-only",
    },
    "iskconmumbai.com": {
        "source_name": "ISKCON Mumbai (Juhu)",
        "owner_or_publisher": "ISKCON Mumbai",
        "authority_tier": "A",
        "catalog": "education",
        "rights_posture": "link-and-metadata-only",
        "canonical_for": "temple-context-reference-only",
    },
    "www.purebhakti.com": {
        "source_name": "PureBhakti",
        "owner_or_publisher": "Gaudiya Vedanta Publications",
        "authority_tier": "supplementary",
        "catalog": "supplementary",
        "rights_posture": "link-and-metadata-only",
        "canonical_for": "recognized-gaudiya-supplementary",
    },
    "purebhakti.com": {
        "source_name": "PureBhakti",
        "owner_or_publisher": "Gaudiya Vedanta Publications",
        "authority_tier": "supplementary",
        "catalog": "supplementary",
        "rights_posture": "link-and-metadata-only",
        "canonical_for": "recognized-gaudiya-supplementary",
    },
    "harikatha.com": {
        "source_name": "Harikatha",
        "owner_or_publisher": "Gaudiya Vedanta Publications",
        "authority_tier": "supplementary",
        "catalog": "supplementary",
        "rights_posture": "link-and-metadata-only",
        "canonical_for": "recognized-gaudiya-supplementary-audio",
    },
    "gitapress.org": {
        "source_name": "Gita Press",
        "owner_or_publisher": "Gita Press Gorakhpur",
        "authority_tier": "supplementary",
        "catalog": "supplementary",
        "rights_posture": "link-and-metadata-only",
        "canonical_for": "sanatana-narrative-supplementary",
    },
    "audio.iskcondesiretree.com": {
        "source_name": "ISKCON Desire Tree Audio",
        "owner_or_publisher": "ISKCON Desire Tree",
        "authority_tier": "C",
        "catalog": "media",
        "rights_posture": "link-and-metadata-only",
        "canonical_for": "media-discovery-only",
        "discovery_only": True,
        "mirror_of": "vedabase.io",
    },
    "ebooks.iskcondesiretree.com": {
        "source_name": "ISKCON Desire Tree Ebooks",
        "owner_or_publisher": "ISKCON Desire Tree",
        "authority_tier": "C",
        "catalog": "media",
        "rights_posture": "link-and-metadata-only",
        "canonical_for": "media-discovery-only",
        "discovery_only": True,
    },
    "prabhupadabooks.com": {
        "source_name": "PrabhupadaBooks.com",
        "owner_or_publisher": "PrabhupadaBooks.com",
        "authority_tier": "C",
        "catalog": "secondary",
        "rights_posture": "edition-comparison-only",
        "canonical_for": "edition-comparison-only",
        "discovery_only": True,
    },
    "www.youtube.com": {
        "source_name": "YouTube",
        "owner_or_publisher": "Google / channel owners",
        "authority_tier": "C",
        "catalog": "media",
        "rights_posture": "link-and-metadata-only",
        "canonical_for": "media-discovery-only",
        "discovery_only": True,
    },
    "youtube.com": {
        "source_name": "YouTube",
        "owner_or_publisher": "Google / channel owners",
        "authority_tier": "C",
        "catalog": "media",
        "rights_posture": "link-and-metadata-only",
        "canonical_for": "media-discovery-only",
        "discovery_only": True,
    },
}

CATEGORY_FROM_PATH = [
    (r"/library/transcripts", "prabhupada-transcript-library"),
    (r"/library/letters", "prabhupada-letters-library"),
    (r"/library/bg", "bhagavad-gita"),
    (r"/library/sb", "srimad-bhagavatam"),
    (r"/library/cc", "caitanya-caritamrta"),
    (r"/audio", "prabhupada-audio"),
    (r"/transcriptions", "prabhupada-transcriptions"),
    (r"media_library", "education-media-library"),
    (r"bhakti-vriksha", "bhakti-vriksha"),
    (r"sunday-school", "sunday-school"),
    (r"/audios", "supplementary-audio-archive"),
    (r"/ebook", "sanatana-ebook-portal"),
    (r"youtube.com/channel", "youtube-channel"),
]


def domain_key(url: str) -> str:
    host = urlparse(url).netloc.lower()
    if host.startswith("www."):
        return host
    return host


def infer_category(url: str) -> str:
    for pattern, cat in CATEGORY_FROM_PATH:
        if re.search(pattern, url, re.I):
            return cat
    if url.endswith("/") or urlparse(url).path in ("", "/"):
        return "site-homepage"
    if url.lower().endswith(".pdf"):
        return "pdf-resource"
    return "entry-point"


def slug_from_url(url: str, idx: int) -> str:
    p = urlparse(url)
    slug = re.sub(r"[^a-z0-9]+", "-", (p.netloc + p.path).lower()).strip("-")
    return f"PSC-{idx:04d}-{slug[:48]}"


def build_entry(url: str, idx: int) -> dict:
    url = clean_url(url)
    host = domain_key(url)
    meta = DOMAIN_META.get(host) or DOMAIN_META.get(host.replace("www.", ""))
    if not meta:
        meta = {
            "source_name": host,
            "owner_or_publisher": "unknown",
            "authority_tier": "C",
            "catalog": "media",
            "rights_posture": "rights-unclear",
            "canonical_for": "pending-classification",
        }
    entry = {
        "source_id": slug_from_url(url, idx),
        "source_name": meta["source_name"],
        "owner_or_publisher": meta["owner_or_publisher"],
        "base_url": f"{urlparse(url).scheme}://{urlparse(url).netloc}/",
        "exact_entry_url": url,
        "source_category": infer_category(url),
        "authority_tier": meta["authority_tier"],
        "content_types": ["web"],
        "languages": ["en"],
        "primary_or_secondary": "primary" if meta["authority_tier"] == "A" else "secondary",
        "canonical_for": meta.get("canonical_for", ""),
        "mirror_of": meta.get("mirror_of", ""),
        "discovery_only": bool(meta.get("discovery_only", meta["authority_tier"] == "C")),
        "rights_posture": meta["rights_posture"],
        "allowed_repository_use": [
            "link-and-metadata",
            "research-planning",
            "module-source-mapping",
        ],
        "prohibited_repository_use": [
            "bulk-download",
            "re-host",
            "verbatim-republication-without-permission",
        ],
        "authentication_required": False,
        "robots_or_access_notes": "Respect site terms; rate-limit verification",
        "last_verified": "",
        "verification_method": "pending-automated-check",
        "status": "catalogued-pending-verification",
        "notes": "Derived from KUT-SRC-0013 public source map",
        "_catalog_bucket": meta["catalog"],
    }
    return entry


def split_catalogs(entries: list[dict]) -> dict[str, list[dict]]:
    buckets: dict[str, list[dict]] = {
        "primary": [],
        "secondary": [],
        "education": [],
        "supplementary": [],
        "media": [],
    }
    for e in entries:
        b = e.pop("_catalog_bucket", "media")
        buckets.setdefault(b, []).append(e)
    return buckets


def write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )


def build_alias_map(entries: list[dict]) -> dict:
    aliases = []
    canonical_hosts = {}
    for e in entries:
        if e.get("mirror_of"):
            aliases.append(
                {
                    "alias_url": e["exact_entry_url"],
                    "canonical_anchor": e["mirror_of"],
                    "relationship": "mirror-or-discovery",
                    "dedupe_rule": "one-claim-identity-per-event",
                }
            )
        host = urlparse(e["exact_entry_url"]).netloc
        if e["authority_tier"] == "A":
            canonical_hosts[host] = e["exact_entry_url"]
    return {
        "catalog_version": "1.0.0",
        "generated": TODAY,
        "canonical_anchors": canonical_hosts,
        "mirror_aliases": aliases,
    }


def build_rights_register(entries: list[dict]) -> dict:
    by_posture: dict[str, list[str]] = {}
    for e in entries:
        rp = e["rights_posture"]
        by_posture.setdefault(rp, []).append(e["source_id"])
    return {
        "catalog_version": "1.0.0",
        "generated": TODAY,
        "classifications": {
            "link-and-metadata-only": {
                "description": "Repository may store URL, title, and factual metadata only.",
                "source_ids": by_posture.get("link-and-metadata-only", []),
            },
            "permission-required-before-republication": {
                "description": "BBT and similar rights holders require permission beyond linking.",
                "source_ids": by_posture.get("permission-required-before-republication", []),
            },
            "edition-comparison-only": {
                "description": "Use for edition comparison workflows, not controlling doctrine.",
                "source_ids": by_posture.get("edition-comparison-only", []),
            },
            "rights-unclear": {
                "description": "Requires human rights review before expanded use.",
                "source_ids": by_posture.get("rights-unclear", []),
            },
        },
        "human_review_required": True,
    }


def main() -> int:
    if not CANONICAL.exists():
        print("Run normalize_source_map.py first", file=sys.stderr)
        return 1
    text = CANONICAL.read_text(encoding="utf-8")
    urls = extract_urls(strip_cite_markers(text))
    entries = [build_entry(u, i + 1) for i, u in enumerate(urls)]
    buckets = split_catalogs(entries)
    all_entries = []
    for lst in buckets.values():
        all_entries.extend(lst)

    write_yaml(
        CATALOG_DIR / "MASTER-SOURCE-CATALOG.yaml",
        {
            "catalog_version": "1.0.0",
            "generated": TODAY,
            "source_map_id": "KUT-SRC-0013",
            "entry_count": len(all_entries),
            "entries": all_entries,
        },
    )
    write_yaml(
        CATALOG_DIR / "PRABHUPADA-PRIMARY-AND-ARCHIVAL.yaml",
        {"catalog_version": "1.0.0", "generated": TODAY, "entries": buckets["primary"]},
    )
    write_yaml(
        CATALOG_DIR / "PRABHUPADA-STRUCTURED-SECONDARY.yaml",
        {"catalog_version": "1.0.0", "generated": TODAY, "entries": buckets["secondary"]},
    )
    write_yaml(
        CATALOG_DIR / "ISKCON-EDUCATION-AND-CONGREGATION.yaml",
        {"catalog_version": "1.0.0", "generated": TODAY, "entries": buckets["education"]},
    )
    write_yaml(
        CATALOG_DIR / "SUPPLEMENTARY-GAUDIYA-SANATANA.yaml",
        {"catalog_version": "1.0.0", "generated": TODAY, "entries": buckets["supplementary"]},
    )
    write_yaml(
        CATALOG_DIR / "MEDIA-AND-YOUTUBE-DISCOVERY.yaml",
        {"catalog_version": "1.0.0", "generated": TODAY, "entries": buckets["media"]},
    )
    write_yaml(CATALOG_DIR / "SOURCE-ALIAS-AND-MIRROR-MAP.yaml", build_alias_map(all_entries))
    write_yaml(CATALOG_DIR / "RIGHTS-AND-PERMISSIONS-REGISTER.yaml", build_rights_register(all_entries))
    write_yaml(
        CATALOG_DIR / "SOURCE-VERIFICATION-QUEUE.yaml",
        {
            "catalog_version": "1.0.0",
            "generated": TODAY,
            "queue": [
                {
                    "item_id": e["source_id"],
                    "url": e["exact_entry_url"],
                    "reason": "awaiting-link-verification",
                    "status": "open",
                }
                for e in all_entries
            ],
        },
    )
    readme = CATALOG_DIR / "README.md"
    readme.write_text(
        f"""# Public Source Catalog

Governed machine-readable catalogs derived from `KUT-SRC-0013` ({TODAY}).

## Authority tiers

| Tier | Role |
|------|------|
| A | Controlling or provenance-anchor sources |
| B | Structured secondary research layers |
| C | Convenience mirrors and media discovery |
| supplementary | Gauḍīya/Sanātana references — do not override Prabhupāda-first layer |

## Files

- `MASTER-SOURCE-CATALOG.yaml` — unified index ({len(all_entries)} entries)
- Tier-split catalogs for research planning
- `SOURCE-ALIAS-AND-MIRROR-MAP.yaml` — canonical/mirror relationships
- `RIGHTS-AND-PERMISSIONS-REGISTER.yaml` — rights posture by entry
- `SOURCE-VERIFICATION-QUEUE.yaml` — unresolved verification items

## Regeneration

```powershell
python scripts/sources/normalize_source_map.py
python scripts/sources/build_public_source_catalog.py
python scripts/sources/verify_public_source_catalog.py
```

Human doctrinal, rights, and publication approval remain **OPEN**.
""",
        encoding="utf-8",
    )
    print(f"Catalogued {len(all_entries)} URLs into {CATALOG_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

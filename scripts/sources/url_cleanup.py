"""Normalize and deduplicate URLs from source-map extractions."""
from __future__ import annotations

import re
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

TRACKING_PARAMS = frozenset(
    {
        "utm_source",
        "utm_medium",
        "utm_campaign",
        "utm_term",
        "utm_content",
        "fbclid",
        "gclid",
        "srsltid",
        "gclsrc",
        "msclkid",
        "mc_cid",
        "mc_eid",
        "_ga",
        "ref",
        "ref_src",
    }
)

CITE_MARKER_RE = re.compile(r"\s*[\uE000\uE001]?cite[\uE000\uE001]?turn[\w\d]+(?:[\uE000\uE001]?turn[\w\d]+)*[\uE000\uE001]?\s*")
URL_RE = re.compile(r"https?://[^\s`\)\"'<>]+")


def strip_cite_markers(text: str) -> str:
    cleaned = CITE_MARKER_RE.sub("", text)
    cleaned = re.sub(r"\s{2,}", " ", cleaned)
    return cleaned


def clean_url(url: str) -> str:
    url = url.strip().rstrip(".,;)")
    parsed = urlparse(url)
    if not parsed.query:
        return url
    qs = parse_qs(parsed.query, keep_blank_values=True)
    filtered = {k: v for k, v in qs.items() if k.lower() not in TRACKING_PARAMS}
    new_query = urlencode(filtered, doseq=True) if filtered else ""
    return urlunparse(
        (parsed.scheme, parsed.netloc, parsed.path, parsed.params, new_query, parsed.fragment)
    )


def extract_urls(text: str) -> list[str]:
    seen: set[str] = set()
    urls: list[str] = []
    for raw in URL_RE.findall(text):
        u = clean_url(raw)
        if u not in seen:
            seen.add(u)
            urls.append(u)
    return urls

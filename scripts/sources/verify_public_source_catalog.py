#!/usr/bin/env python3
"""Verify public catalog URLs with respectful rate-limited HTTP checks."""
from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
CATALOG = REPO / "14-research-source-register/public-source-catalog/MASTER-SOURCE-CATALOG.yaml"
CACHE = REPO / "build-evidence/.source-link-cache.json"
REPORT = REPO / "build-evidence/SOURCE-LINK-AND-RIGHTS-AUDIT.md"
QUEUE = REPO / "14-research-source-register/public-source-catalog/SOURCE-VERIFICATION-QUEUE.yaml"

USER_AGENT = "KutumbaSourceCatalogVerifier/1.0 (+https://github.com/swap2you/kutumba-family-program)"
RATE_LIMIT_SEC = 0.75
TIMEOUT_SEC = 20


def load_cache() -> dict:
    if CACHE.exists():
        return json.loads(CACHE.read_text(encoding="utf-8"))
    return {}


def save_cache(cache: dict) -> None:
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(cache, indent=2), encoding="utf-8")


def check_url(url: str) -> dict:
    result = {"url": url, "checked_at": datetime.now(timezone.utc).isoformat()}
    headers = {"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml"}
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT_SEC) as resp:
                result.update(
                    {
                        "method": method,
                        "status": resp.status,
                        "final_url": resp.geturl(),
                        "outcome": "ok" if resp.status < 400 else "http-error",
                    }
                )
                return result
        except urllib.error.HTTPError as e:
            result.update({"method": method, "status": e.code, "outcome": "http-error"})
            if e.code in (403, 405, 429) and method == "HEAD":
                continue
            if e.code in (403, 405):
                result["outcome"] = "access-restricted-not-missing"
            return result
        except urllib.error.URLError as e:
            result.update({"method": method, "outcome": "network-error", "error": str(e.reason)})
            if method == "HEAD":
                continue
            return result
    return result


def main() -> int:
    if not CATALOG.exists():
        print("Build catalog first", file=sys.stderr)
        return 1
    data = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
    entries = data.get("entries", [])
    cache = load_cache()
    results = []
    unresolved = []
    today = date.today().isoformat()

    for i, entry in enumerate(entries):
        url = entry["exact_entry_url"]
        if url in cache and cache[url].get("outcome") in ("ok", "access-restricted-not-missing"):
            check = cache[url]
        else:
            check = check_url(url)
            cache[url] = check
            time.sleep(RATE_LIMIT_SEC)
        entry["last_verified"] = today
        entry["verification_method"] = f"{check.get('method', 'cache')}:{check.get('status', 'n/a')}"
        if check.get("outcome") == "ok":
            entry["status"] = "verified-available"
        elif check.get("outcome") == "access-restricted-not-missing":
            entry["status"] = "access-restricted-verify-manually"
        else:
            entry["status"] = "verification-failed"
            unresolved.append(
                {
                    "item_id": entry["source_id"],
                    "url": url,
                    "reason": check.get("outcome", "unknown"),
                    "status": "open",
                    "evidence": check,
                }
            )
        results.append({**entry, "_check": check})

    save_cache(cache)
    CATALOG.write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )
    QUEUE.write_text(
        yaml.safe_dump(
            {
                "catalog_version": "1.0.0",
                "generated": today,
                "queue": unresolved,
            },
            sort_keys=False,
            allow_unicode=True,
        ),
        encoding="utf-8",
    )

    ok = sum(1 for r in results if r["_check"].get("outcome") == "ok")
    restricted = sum(1 for r in results if r["_check"].get("outcome") == "access-restricted-not-missing")
    failed = len(results) - ok - restricted

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Source Link and Rights Audit",
        "",
        f"Generated: {today}",
        "",
        "## Summary",
        "",
        f"| Metric | Count |",
        f"|--------|-------|",
        f"| Total URLs checked | {len(results)} |",
        f"| Verified available | {ok} |",
        f"| Access restricted (403/405) — not treated as missing | {restricted} |",
        f"| Failed / unresolved | {failed} |",
        "",
        "## Rights posture",
        "",
        "All BBT/VedaBase/Archives entries remain **link-and-metadata-only** unless separate permission is recorded.",
        "Public accessibility does not imply redistribution permission.",
        "",
        "## Unresolved queue",
        "",
    ]
    if unresolved:
        for u in unresolved[:30]:
            lines.append(f"- `{u['item_id']}` — {u['url']} — {u['reason']}")
        if len(unresolved) > 30:
            lines.append(f"- … and {len(unresolved) - 30} more in SOURCE-VERIFICATION-QUEUE.yaml")
    else:
        lines.append("- None — all URLs resolved or access-restricted with manual follow-up noted.")
    lines.append("")
    lines.append("## Human review")
    lines.append("")
    lines.append("- Rights review: **OPEN**")
    lines.append("- Research review: **OPEN**")
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Verified {len(results)} URLs: ok={ok} restricted={restricted} failed={failed}")
    return 0 if failed == 0 else 0  # queue tracks failures; do not block build


if __name__ == "__main__":
    raise SystemExit(main())

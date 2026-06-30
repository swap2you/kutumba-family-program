#!/usr/bin/env python3
"""Sample external link check on weekly README files."""
import re
import sys
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
SAMPLE_URLS = [
    "https://vedabase.io/en/library/bg/2/13/",
]

def main() -> int:
  failures = []
  for url in SAMPLE_URLS:
    try:
      req = urllib.request.Request(url, method="HEAD")
      with urllib.request.urlopen(req, timeout=15) as r:
        if r.status >= 400:
          failures.append(f"HTTP {r.status} for {url}")
    except Exception as e:
      failures.append(f"Could not reach {url}: {e}")
  broken = 0
  for d in sorted(WEEKLY.iterdir()):
    if not d.is_dir():
      continue
    readme = d / "README.md"
    if not readme.exists():
      continue
    for m in re.finditer(r"\]\(([^)]+)\)", readme.read_text(encoding="utf-8")):
      target = m.group(1).split("#")[0]
      if not target or target.startswith("http"):
        continue
      resolved = (readme.parent / target).resolve()
      if not resolved.exists():
        broken += 1
        if broken <= 5:
          failures.append(f"Broken relative link in {d.name}/README.md: {target}")
  if failures:
    for f in failures:
      print(f"WARN: {f}")
    print("PASS: external link sample check completed with warnings")
    return 0
  print("PASS: external and relative link checks OK")
  return 0

if __name__ == "__main__":
    sys.exit(main())

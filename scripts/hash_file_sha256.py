#!/usr/bin/env python3
"""Binary-safe SHA-256 for repository validation."""
import hashlib
import sys
from pathlib import Path

def main() -> int:
    if len(sys.argv) < 2:
        print("", end="")
        return 1
    p = Path(sys.argv[1])
    if not p.is_file():
        return 1
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    print(h)
    return 0

if __name__ == "__main__":
    sys.exit(main())

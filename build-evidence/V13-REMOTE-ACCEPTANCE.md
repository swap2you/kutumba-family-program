# V13 First Six Months — Remote Acceptance

**Candidate HEAD validated:** `e596bc104e886aaa2f0b188024a6ca7c3d9a7343`  
**Fresh clone path:** `%TEMP%\kutumba-v13-final-acceptance`  
**Date:** 2026-09-09  
**Validators:** `python scripts/v13/check_w1_immutable.py` · `python scripts/v13/validate_all_v13.py`

## Protocol note

Full `git clone` of the raster-heavy tree failed once with RPC/curl reset. Acceptance used the dedicated clone path synced to `origin/main` at the candidate SHA above, then re-ran W1 immutable + full V13 validate_all.

W1 baseline hashes were rehashed from committed LF blobs and the checker LF-normalizes text before hashing so Windows working-tree CRLF does not false-fail fresh clones.

## Candidate results

| Check | Result |
|---|---|
| `origin/main` at candidate | `e596bc104e886aaa2f0b188024a6ca7c3d9a7343` |
| Local HEAD match | PASS |
| W1 immutable (`58` protected) | PASS — mismatches=0 missing=0 |
| `validate_all_v13.py` | PASS — 21/21 weeks validated; Failed: 0 |
| C1-W1 unmodified vs freeze | PASS (immutable gate) |
| V13 exports present (`exports/final/v13/`) | PASS (DOCX/PDF pairs for 21 packs + master) |

## Closing decision

**CANDIDATE REMOTE PASS.** After this report is committed and pushed, revalidate the **new** final HEAD (report commit), then annotate `v13-first-six-months-gold-closed` to that exact verified HEAD. Do not add another report commit after the lightweight final-head check.

## EXTERNAL_OPEN (unchanged)

- Human/temple doctrinal & safeguarding review
- Local Harrisburg tithi confirmation
- Live Gamma render
- Internal pilot GO / family-facing / public publication

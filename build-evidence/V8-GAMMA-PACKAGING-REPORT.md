# V8 Gamma Packaging Report

Generated: 2026-06-29

## Status model

Replaced deprecated `render-ready` with `assets-complete-upload-required`.

## Card-level mapping

Each `GAMMA-ASSET-MAP.yaml` now includes per-card:

- card number, asset ID, SVG path, PNG path
- rights, source keys, speaker note, accessibility (alt text)

## Placeholder removal

- C1-W2 parent deck: removed photo-timeline and VISUAL-PLAN placeholders
- Deck prompts use `[ASSET: visuals/rendered/...]` paths

## Export

- Script: `scripts/export/build_gamma_cycle1_bundle.py`
- Local bundle: `build-evidence/exports/Cycle-1-Gamma-Bundle/`
- Manifest: `build-evidence/V8-GAMMA-BUNDLE-MANIFEST.json`
- ZIP generated locally for upload (not required in Git)

## Validator

`validate_gamma_asset_references.py` — PASS

Exported Gamma decks are **not** in Git; human post-render QA required.

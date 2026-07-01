# Prompt 07 — Gamma Render Readiness

## Objective

Make Cycle 1 Gamma packages genuinely render-ready. Distinguish structural scaffolds from finished deck specifications.

Gamma currently supports creating from an idea, pasted outline or imported content, generating/reworking images, themes/branding, and export to PPT, PDF, PNG or Google Slides. Treat Gamma as a renderer/editor, not as a doctrinal source.

## Scope

Deepen all three audience decks for C1-W1 through C1-W6:

- parent/family;
- Lāla–Lālī;
- Kiśora–Kiśorī.

C3 decks may remain scaffolds, but their status must remain explicit.

## Every render-ready deck must include

- deck identity and version;
- audience and age;
- exact module outcome;
- recommended card count;
- 16:9 format;
- theme and typography guidance;
- Sanskrit/diacritic handling;
- complete card text;
- card-specific speaker notes;
- exact local visual asset ID/path;
- exact source citation per factual card;
- rights status per visual;
- accessibility/alt-text note;
- interaction instruction;
- content to omit;
- no invented quotations;
- no placeholder visuals;
- no generic “deliver per facilitator guide” notes;
- no request for Gamma to rewrite doctrinal content;
- final human review checklist.

## Gamma prompt behavior

Tell Gamma:

- preserve supplied text unless explicitly asked to shorten;
- do not introduce new scripture quotations;
- do not invent Sanskrit;
- do not create devotional paintings in a copied or named-artist style;
- use supplied KUTUMBA SVG/PNG assets first;
- use abstract patterns, nature, family-safe icons and diagrams for secondary decoration;
- maintain respectful visual treatment;
- keep citations visible but unobtrusive;
- include a final references card.

## Asset package

Create per module:

```text
gamma/
├── GAMMA-MASTER-DECK-BRIEF.md
├── GAMMA-PARENT-DECK-PROMPT.md
├── GAMMA-LALA-LALI-DECK-PROMPT.md
├── GAMMA-KISORA-KISORI-DECK-PROMPT.md
├── GAMMA-ASSET-MAP.yaml
├── GAMMA-RENDER-CHECKLIST.md
└── GAMMA-POST-RENDER-QA.md
```

## Post-render QA

The user will render externally. Provide a checklist for:

- text accuracy;
- card order;
- no invented facts;
- citation visibility;
- image rights;
- no distorted sacred images;
- no cropped diacritics;
- child readability;
- color contrast;
- export parity;
- source links;
- facilitator timing.

Do not claim a rendered deck exists unless the exported file is actually supplied and inspected.

## Deliverables

- six Cycle 1 render-ready deck packages;
- honest status for all other decks;
- `build-evidence/V7-GAMMA-READINESS-REPORT.md`.

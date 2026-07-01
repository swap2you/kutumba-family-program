# Prompt 03 — Real Cycle 1 Visual Production

## Objective

Replace placeholder SVG metadata cards with real teaching visuals.

## Preserve IDs, replace substance

Retain existing asset IDs where their intended meaning is sound. Replace the file contents and enrich manifests.

Do not inflate the asset count. Quality is the gate.

## Minimum visual substance by class

### Concept diagram

Must contain:

- at least three labeled concept nodes;
- visible relationships/arrows;
- one central conclusion;
- explicit source note;
- age-appropriate variant when needed.

### Process flow

Must contain:

- ordered steps;
- directional edges;
- start/end or outcome;
- facilitator timing where relevant.

### Storyboard

Must contain:

- at least four distinct panels;
- event labels;
- sequence markers;
- source mapping per panel;
- symbolic/nonviolent presentation where required.

Do not depict sacred personalities as crude clip-art. Use respectful symbolic staging, locations, objects, text panels and line-art silhouettes.

### Analogy diagram

Must show:

- compared elements;
- what the analogy teaches;
- what it does not teach;
- source/pedagogy classification.

### Scripture reference card

Must show:

- reference;
- short KUTUMBA paraphrase;
- source link/QR-ready URL;
- no full copyrighted translation or purport;
- misconception boundary.

### Family-practice card

Must show:

- trigger;
- three-step action;
- minimum version;
- opt-out/safety note;
- home follow-up.

### Integration map

Must show:

- Cycle 1 sequence;
- six module outcomes;
- family project connection;
- noncompetitive presentation path.

## Production method

Use original SVG:

- shapes;
- paths;
- arrows;
- line art;
- symbols;
- typography.

Do not use AI devotional portraits.

Generate PNG derivatives at presentation resolution:

- 1600×1040 or equivalent;
- transparent/solid background as appropriate;
- readable at 16:9 slide display.

Use one reproducible renderer:

- CairoSVG;
- Inkscape CLI;
- headless Chromium;
- another documented local renderer.

No screenshots of Markdown.

## Per-module governance

Every module must contain:

- `VISUAL-ASSET-MANIFEST.yaml`
- `VISUAL-SOURCE-REGISTER.yaml`
- populated `image-rights-register.yaml`
- `ALT-TEXT.md`
- `VISUAL-CONTACT-SHEET.md`
- `source/`
- `rendered/*.svg`
- `rendered/*.png`

## Master catalog

Create the currently missing:

`14-research-source-register/visual-asset-library/VISUAL-ASSET-CATALOG.yaml`

Every asset must include:

- ID;
- class;
- module;
- title;
- actual source keys;
- canonical fact IDs;
- SVG path;
- PNG path;
- dimensions/viewBox;
- generation method;
- alt text;
- rights;
- doctrine review;
- design review;
- Gamma card uses;
- status.

## Quality prohibition

No final user-facing visual may contain boilerplate such as:

- `Asset class:`
- `Source anchors: see module research pack`
- `Rights: kutumba-original`

Rights/source metadata belongs in manifest/footer, not as the main visual content.

## Evidence

- `build-evidence/V8-CYCLE-1-REAL-VISUAL-COVERAGE.md`
- `build-evidence/V8-VISUAL-BEFORE-AFTER.md`
- six contact-sheet pages

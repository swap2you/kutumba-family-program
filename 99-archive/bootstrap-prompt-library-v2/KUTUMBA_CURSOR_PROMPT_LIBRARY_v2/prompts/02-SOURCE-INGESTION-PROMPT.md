# Prompt 02 — Source Ingestion and Provenance

## Objective

Copy current KUTUMBA documents into the repository safely, inventory all supplied sources, and index legacy/reference collections without turning the repository into an uncontrolled archive.

## Source locations

### Current KUTUMBA documents — copy

`C:\Users\swap2\Downloads\Personal\0. KUTUMBA SANGA`

### Legacy/reference collections — index and selectively extract metadata only

- `C:\Users\swap2\Downloads\Personal\5. Devotional\1. Baktivriksha`
- `C:\Users\swap2\Downloads\Personal\5. Devotional\Granth`
- `C:\Users\swap2\Downloads\Personal\5. Devotional\1. Baktivriksha\BV Material`

The `BV Material` path is nested under the legacy Bhaktivriksha root. Prevent double-counting and duplicate intake.

## Current-document intake rules

Recursively inspect the current KUTUMBA source folder.

Copy supported project files into:

`00-source-materials/01-current-kutumba-originals/`

Preserve relative subfolders when they carry meaning.

Include relevant:

- DOCX
- PDF
- PPTX
- XLSX
- Markdown
- text
- CSV
- image files
- audio indexes or small original recordings when clearly KUTUMBA-owned

Exclude:

- temporary Office lock files such as `~$*`
- system files
- duplicate download artifacts
- caches
- unrelated personal files
- secrets
- completed private forms
- personal family records

Never delete, rename, or alter files in the source folder.

For every copied file, calculate SHA-256 and record:

- source ID
- source folder
- original absolute path
- repository relative path
- original filename
- normalized title
- file type
- byte size
- hash
- modified timestamp
- likely workstream
- version, when stated
- status
- privacy class
- rights status
- canonicalization status
- notes

Create:

- `00-source-materials/SOURCE-MANIFEST.yaml`
- `00-source-materials/SOURCE-INVENTORY.md`
- `build-evidence/SOURCE-INGESTION-REPORT.md`

## Legacy/reference rules

The legacy Bhaktivriksha, Granth, and Jayapataka Swami Maharaj folders are reference collections.

Do not bulk-copy them into Git.

Do not commit a PDF library, book collection, commercial audio, scanned books, or third-party training packs merely because they are locally available.

Create an index under:

`00-source-materials/03-external-reference-index/`

Required outputs:

- `LEGACY-BHAKTIVRIKSHA-FILE-INDEX.csv`
- `GRANTH-PDF-CATALOG.csv`
- `JAYAPATAKA-SWAMI-BV-MATERIAL-INDEX.csv`
- `REFERENCE-SOURCE-REGISTER.yaml`
- `REFERENCE-RIGHTS-AND-USE-REVIEW.md`
- `REFERENCE-DUPLICATE-HASH-REPORT.md`

For indexed files record metadata only:

- local source path
- relative path
- filename
- extension
- size
- modified date
- hash when practical
- title inferred cautiously
- author/publisher when explicitly present
- category
- language
- likely topic
- rights status
- review status
- possible KUTUMBA relevance
- duplicate group

Do not extract or reproduce long copyrighted text.

Small user-authored notes may be copied only when authorship and privacy are reasonably clear. Otherwise index them.

## Source priority

Current KUTUMBA project documents outrank legacy structure.

Legacy Bhaktivriksha and other materials may inform research and crosswalks, but they do not override:

- KUTUMBA governance
- three-year curriculum architecture
- first-six-month detailed plan
- child-safety model
- source hierarchy
- temple-alignment boundaries

## Completion gate

Do not proceed until:

- current sources are copied and hashed
- original Downloads files remain intact
- legacy sources are indexed without bulk copying
- duplicates are identified
- rights uncertainties are recorded
- no sensitive personal data entered Git

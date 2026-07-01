# Prompt 02 — Canonical Fact and Citation Reconciliation

## Objective

Correct factual and citation drift across every derivative file. V6 corrected claim-register metadata but did not fully reconcile the downstream documents.

## Create canonical registries

Create:

```text
14-research-source-register/canonical-facts/
├── README.md
├── CANONICAL-FACT-REGISTRY.yaml
├── SOURCE-DESCRIPTION-REGISTRY.yaml
├── CONTROLLED-TERMINOLOGY.yaml
├── KNOWN-HIGH-RISK-FACTS.yaml
└── CORRECTION-HISTORY.md
```

Use `templates/CANONICAL-FACT-REGISTRY-TEMPLATE.yaml`.

Each fact needs:

- fact ID;
- canonical wording;
- compact teaching wording;
- prohibited/misleading wording;
- exact primary source keys;
- exact stable links;
- source context;
- module applicability;
- age-band notes;
- visual implications;
- rights posture;
- named human review status;
- last checked date.

## Mandatory Cycle 1 corrections

Correct actual content, not only audit notes.

### Śrīmad-Bhāgavatam 1.2.17

Do not describe it as “Bhāgavata as the ripened fruit of Vedic knowledge.”

Use a verse-accurate description: the Lord in the heart cleanses material desire from the sincere hearer who hears Kṛṣṇa-kathā.

### Śrīmad-Bhāgavatam 1.2.18

Use for regular Bhāgavata hearing/service and the development of steady, irrevocable devotional service.

### Śrīmad-Bhāgavatam 1.2.19

Do not describe it vaguely as “devotion fixed after taste develops.”

Use a verse-accurate description: passion and ignorance, lust and hankering recede; the devotee becomes established in goodness and happiness.

### Śrīmad-Bhāgavatam 1.1

Distinguish:

- 1.1.1 invocation and Absolute Truth;
- 1.1.4 onward assembly at Naimiṣāraṇya;
- exact verses used for specific questions.

Do not call 1.1.1 itself “the sages’ inquiry.”

### KUTUMBA charter claims

Statements such as:

- not a social club;
- not a substitute temple;
- not a competing preaching center;
- six charter purposes;

must directly cite the KUTUMBA charter/operating model. Scripture may be theological support but not the sole documentary source.

## Mandatory C3-W2 correction

Canonical fact:

- Kṛṣṇa appears to Devakī and Vasudeva in Mathurā.
- Vasudeva carries Him to Gokula.
- Childhood Vraja pastimes follow.
- Do not label the appearance as “birth in Vṛndāvana.”

Find and correct the stale phrase and all equivalent drift in:

- concept maps;
- media indexes;
- Gamma files;
- child lessons;
- newcomer adaptation;
- FAQs;
- source maps;
- kathā files;
- reader pages;
- scripts and active data files.

Archived historical files may retain old content only when clearly marked archived/noncanonical.

## Cross-file audit scope

For all six Cycle 1 modules, reconcile:

- `sources.yaml`
- `research/CLAIM-REGISTER.yaml`
- `research/SOURCE-MATRIX.md`
- `research/SOURCE-EXPANSION-BRIEF.md`
- `research/VERSE-AND-REFERENCE-STUDY.md`
- `research/BIBLIOGRAPHY.md`
- `katha/KATHA-SOURCE-REGISTER.yaml`
- `prem-ki-katha.md`
- `parent-lesson.md`
- both child-track lessons
- `newcomer-adaptation.md`
- `complete-week.md`
- Gamma files
- visual files
- media indexes
- reader pages

Do not merely add `context_note`; fix misleading prose at its actual point of use.

## Citation policy

Every factual teaching must be classified as one of:

- exact scripture text;
- scripture paraphrase;
- Śrīla Prabhupāda teaching;
- KUTUMBA governance;
- reviewed pedagogical inference;
- safeguarding policy;
- contemporary case;
- KUTUMBA-created analogy;
- facilitator guidance.

Require exact source keys for the first three.

No full purports in Git. Use brief compliant quotations only where necessary and otherwise paraphrase with stable links.

## Deliverables

- `build-evidence/V7-CROSS-FILE-CITATION-AUDIT.md`
- `build-evidence/V7-CANONICAL-FACT-DRIFT-REPORT.md`
- corrected Cycle 1 content
- corrected C3-W2 drift
- validator implemented in Prompt 09

## Exit criteria

- no known verse-description error remains in current files;
- no current C3-W2 file says Kṛṣṇa was born in Vṛndāvana;
- claim registers and teaching prose agree;
- governance, pedagogy and scripture sources are not conflated;
- all changes remain human-review-required.

# Prompt 10 — Gamma and NotebookLM Production Packs

## Objective

Prepare source-grounded inputs for visual and study tools without allowing those tools to become sources of truth.

## Gamma

Gamma supports:

- Generate;
- Paste;
- Import;
- Create with Agent;
- card-based presentations;
- source uploads;
- citation where possible;
- image placeholders.

Create with Agent may combine PDFs, documents, decks, webpages, images, and existing Gamma content.

## Gamma strategy

For each module create three deck briefs:

1. Parent/family deck
2. Lāla–Lālī deck
3. Kiśora–Kiśorī deck

Each brief must include actual slide/card content, not only instructions.

### Parent deck

Recommended 14–20 cards:

- title;
- essential question;
- lived problem;
- primary verse;
- source-grounded concept;
- analogy;
- misconception;
- case study;
- family discussion;
- practice;
- bhakti laboratory;
- home saṅkalpa;
- references;
- facilitator notes.

### Lāla–Lālī deck

Recommended 8–12 cards:

- story opening;
- one visual truth;
- sequence;
- movement;
- craft;
- recall line;
- family connection;
- closing.

### Kiśora–Kiśorī deck

Recommended 10–15 cards:

- hook;
- text observation;
- concept;
- controversy/misconception;
- case;
- debate;
- diagram;
- application;
- project;
- sources.

## Image strategy in Gamma

Use placeholders when rights are unresolved.

Every image prompt must specify:

- subject;
- medium;
- composition;
- mood;
- cultural context;
- audience;
- exclusions;
- no inaccurate sacred iconography.

## Gamma API

Do not require the API for this project phase.

If later enabled:

- Gamma Pro or higher is required;
- use v1.0;
- keep `GAMMA_API_KEY` outside Git;
- use the `X-API-KEY` header;
- never commit `sk-gamma-*`;
- use a pre-created theme ID;
- provide actual content in `inputText`.

Create:

- `scripts/gamma/README.md`
- `.env.example` containing only `GAMMA_API_KEY=`
- `.gitignore` protection
- no executable API call until the user explicitly enables it.

## NotebookLM

NotebookLM may be used manually for:

- source-grounded questioning;
- mind maps;
- slide decks;
- quizzes;
- flashcards;
- audio overviews;
- video overviews;
- infographics.

It can be inaccurate. Every output must be checked against the claim register and primary sources.

## Notebook design

Create one notebook source pack per cycle, plus optional module packs.

Each pack contains:

- canonical KUTUMBA module;
- source-links document;
- approved short excerpts;
- original summaries;
- claim register;
- visuals brief;
- review questions.

Do not upload participant records or unlicensed source files.

Create a NotebookLM prompt for:

- concept map;
- misconception map;
- parent study guide;
- child explanation;
- quiz;
- review checklist.

NotebookLM output is derivative and never automatically committed as approved.

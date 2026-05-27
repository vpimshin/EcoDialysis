# Copilot instructions — EcoDialysis

## What this repo is

This is **not a software project**. It is a working folder of pitch and research
artifacts for **EcoDialysis**, a submission to **ANDCS × MIT Hacking Medicine,
Track 1 (Sustainable Care), Paris 2026**.

The proposal: a sustainability label and 3-step service for French dialysis
centers — (1) a one-day eco-audit graded A–E, (2) a playbook to capture
reverse-osmosis reject water (~250 L/session) for non-clinical reuse under the
July 2024 decree, and (3) an AI agent for continuous benchmarking. Rollout via
the GHT (Groupement Hospitalier de Territoire) framework.

There is no source code, build system, package manager, test suite, or CI.
Do not invent one. Do not add `package.json`, `requirements.txt`, linters,
formatters, or GitHub Actions unless the user explicitly asks.

## Repository layout

- `EcoDialysis Pitch_v1.html`, `EcoDialysis-Pitch_v3.pdf`,
  `EcoDialysis_Pitch_v3.pptx` — current pitch deck (latest = v3). The HTML is a
  **self-contained single-file slide deck**: inline `<style>` + inline SVG, no
  external assets, no bundler step. Open it directly in a browser.
- `Deep_Research/` — source briefs from Gemini / OpenAI / Perplexity on dialysis
  sustainability. Treat as **input research**, not deliverables.
- `Guide/` — French reference PDFs (SFNDT *Guide de la néphrologie verte*,
  bonnes pratiques). Authoritative domain sources — cite these in preference to
  the LLM-generated research when claims overlap.
- `old/` — superseded pitch versions (v1, v2, Pitch.html, Pitch2.html, …),
  `Hackathon/` handbooks, `Impact environnemental/` background PDFs, and
  `_archive/`. Do **not** edit files under `old/` — copy forward to the root
  with a new version suffix instead.

## Conventions

- **Versioning by filename suffix** (`_v1`, `_v2`, `_v3`). When iterating on the
  pitch, bump the suffix and leave the previous version in place (move the
  prior root copy into `old/` only if the user asks).
- **Trilingual context**: the audience and most authoritative guides
  (`Guide/`, SFNDT) are French; the hackathon track and pitch deck are
  English. Keep the deck in English unless told otherwise; keep numeric claims
  consistent with the French source PDFs.
- **Key figures used in the pitch** (keep these consistent across versions
  unless the user updates them): ~52,000 French dialysis patients;
  ~250 L RO-reject per 4-hour session; ~4,200 m³/year saved per 100-patient
  center; ~1 t CO₂ avoided/year/center; 1–3.5 year payback (UK/IE/MY
  precedents); funding via Agences de l'Eau + CEE certificates (no hospital
  capex). Regulatory anchors: **Plan Eau 2023**, **July 2024 decree** on
  non-potable water reuse in public buildings under ARS supervision.
- **HTML deck edits**: it is a single file with one `<style>` block and
  per-slide sections. CSS custom properties (`--navy`, `--blue`, `--sky-2`,
  `--ink-2/3`, `--line`) drive the visual system — reuse them rather than
  introducing new colors. Slides use `.chrome`, `.eyebrow`, `h1.title`,
  `.stat`, `.sources` patterns; follow the existing slide template when adding
  one.

## Working with the binary assets

- `.pptx` and `.docx` are binary — do not attempt to edit them as text. If the
  user wants slide changes, edit the HTML and/or ask whether they want the
  PPTX regenerated/exported manually.
- `.pdf` files in `Deep_Research/`, `Guide/`, and `old/Impact environnemental/`
  are reference reading. When a user asks a factual question, prefer
  extracting from these (e.g. `pdftotext`) over web search.

## IMPORTANT
- Load askQuestions tool. In the end of every answer ask me how I want to proceed using this tool.

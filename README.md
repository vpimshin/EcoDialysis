# EcoDialysis

**Turning dialysis from a hidden water risk into a measurable water-resilience asset.**

EcoDialysis is a pitch project for **ANDCS × MIT Hacking Medicine — Track 1 Sustainable Care, Paris 2026**.
A 100-patient dialysis centre quietly discharges ~4,200 m³/yr of high-purity RO reject — water already paid for and treated, then lost.
Décret n°2024-796 (in force 1 Sept 2024) now authorises non-clinical reuse via the EICH (Eaux Impropres à la Consommation Humaine) framework. This repository contains the pitch, the diligence evidence library, and the Python sources used to build them.

---

## 1 · Main presentations

All in `/` (repo root). HTML is the source of truth; PDFs are exported at **true 16:9 (13.333 in × 7.5 in, 960 × 540 pt)**, one slide per page.

| File | Description |
|---|---|
| `EcoDialysis_Final_Pitch_EN.html` / `.pdf` | English deck — 53 slides (35 main + 18 appendix). Fixed 1600 × 900 canvas, keyboard / arrow / hash navigation, progress bar, slide counter. Storyline: hidden water vulnerability → measurement & reuse → international & French proof → product & ecosystem → pilot ask. |
| `EcoDialysis_Final_Pitch_FR.html` / `.pdf` | French parallel deck — 53 slides, same IDs as EN. Uses polished French terminology: résilience hydrique, vulnérabilité hydrique cachée, EICH, carnet sanitaire, GHT, sobriété hydrique, etc. |
| `EcoDialysis_Executive_Summary_EN.html` / `.pdf` | One-page A4 portrait executive summary — hook, 5 KPI tiles, what-we-deliver, proof base, three pilots, ask, claims discipline, source credit. |
| `EcoDialysis_Executive_Summary_FR.html` / `.pdf` | French executive summary, same layout. |

### How to use the decks

- Open the HTML in any modern browser.
- Navigate: `←` / `→`, `PgUp` / `PgDn`, `Space`, `Home`, `End`, or the on-screen arrows.
- Direct-link to any slide via hash, e.g. `#slide-apx-s26`, `#slide-pilots`, `#slide-apx-sources-registry`.
- Click any source chip (Per, Gem, Ope, S23, S26, Gov, TSP, Ird, HCW, Pch) to jump to the source registry anchor.

### Appendix structure (A1 – A16 + source registry)

A1 source map · A2 chip registry · A3 DR-Water table (18 facts) · A4 DR-France (12) · A5 DR-Tech (15) · A6 SFNDT-2023 framework · A7 SFNDT-2026 long guide (20 operational facts) · A8 Gov / EICH / Décret 2024-796 · A9 health-system decarbonation context (why water is adaptation-first) · A10 equipment ecosystem matrix · A11 supplier landscape · A12 financial sensitivity · A13 maturity matrix · A14 risk register · A15 pilot timeline (week-by-week) · A16 claims discipline (allowed vs forbidden) · Appendix I full source anchors.

---

## 2 · `ecodeck/` — Python sources

All five Python sources used to generate the decks live in [`ecodeck/`](./ecodeck). Edit these, rebuild, re-export — do **not** edit the generated HTML by hand if you want changes to survive a rebuild.

| File | Role |
|---|---|
| `style_js.py` | Exports `CSS` (1600 × 900 fixed canvas, viewport scaling, true 16:9 `@page`, navigation, progress bar, source chips, print rules) and `JS` (keyboard / arrow / hash navigation, slide counter, click-on-chip sync). Single source of truth for visual identity. |
| `content_en.py` | All 53 EN slides as `SLIDES_EN` list of tuples `(sid, kind, title, body_html, notes)`. Helper `C(*ids)` renders source chips. Helper `add(sid, kind, title, body, notes)` appends a slide. |
| `content_fr.py` | French parallel — same slide IDs, same structure, polished FR wording. |
| `build.py` | Assembler. Imports CSS+JS from `style_js`, slides from `content_en` / `content_fr`, emits the two final HTML files in the repo root. |
| `exec.py` | Generator for the one-page executive summary (EN + FR). |

### Rebuild workflow

```bash
# 1 · regenerate HTML decks after editing content_en.py / content_fr.py / style_js.py
cd ecodeck
python3 build.py
# → writes ../EcoDialysis_Final_Pitch_EN.html and ..._FR.html

# 2 · regenerate executive summaries
python3 exec.py

# 3 · re-export PDFs at true 16:9
cd ..
for L in EN FR; do
  google-chrome --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
    --print-to-pdf="EcoDialysis_Final_Pitch_${L}.pdf" \
    "file://$PWD/EcoDialysis_Final_Pitch_${L}.html"
  google-chrome --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
    --print-to-pdf="EcoDialysis_Executive_Summary_${L}.pdf" \
    "file://$PWD/EcoDialysis_Executive_Summary_${L}.html"
done
```

### Adding or editing a slide

```python
# inside content_en.py or content_fr.py
add(
    "my-slide-id",          # sid — also becomes the URL hash #slide-my-slide-id
    "content",              # kind ∈ {"cover","divider","content","appendix"}
    "Slide title",
    """<p class="lead">Body HTML here.</p>
       <p>Source chip → """ + C("ope","s26") + """</p>""",
    "Speaker notes here."
)
```

EN and FR must have the same `sid`s and the same count (53). The builder enforces stable IDs so source chips and deep-links keep working.

---

## 3 · `Deep_Research/` — deep-research syntheses

LLM-assisted deep-research outputs used as moderate-confidence inputs. Cross-referenced against high-confidence sources (Guides, government, peer-reviewed) before being quoted in the deck.

| File | Source | Use in deck |
|---|---|---|
| `EcoDialysis_Perplexity.pdf` / `.docx` | Perplexity deep research — French dialysis market & GTM | Chip **Per** · ~51,700 patients, ~77 % in-centre/UDM, reference 100-patient site model, RO reject scenario range. Appendix A4. |
| `Water Sustainability Practices in Dialysis_OpenAI.pdf` | OpenAI deep research — water sustainability | Chip **Ope** · Canterbury, Bristol, Ashford, East Kent (UK); ANZSN cluster; modern vs old AU RO (357 L/3.1 kWh vs 548 L/7.2 kWh); Spain 20-centre mean 476.5 L. Appendix A3. |
| `Clinical and Technical Advancements in Dialysis_Gemini.pdf` / `.docx` | Gemini deep research — clinical & technical | Chip **Gem** · taxonomy of reuse / RO optimisation / disinfection / heat recovery; conductivity-routed reuse logic; sorbent/portable roadmap. Appendix A5. |
| `EcoDialysis_OpenAI.pdf` / `EcoDialysis_Open_AI.docx` | OpenAI broader synthesis | Background cross-check. |

> Reliability note: deep-research outputs are flagged "Medium" / "Medium-high" in the appendix and never cited alone for a regulatory or financial claim — they are always paired with a Guide / Gov / TSP / SFNDT source.

---

## 4 · `Guides/` — high-confidence reports & guides

These are the **regulatory and learned-society anchors** of the diligence library.

### `Guides/` root

| File | Source | Use in deck |
|---|---|---|
| `SFNDT_guide complet-VF-HD-2_260526_231531.pdf` | SFNDT 2023 — green nephrology framework | Chip **S23** · measure-first logic, governance, lifecycle procurement, continuous improvement frame. Appendix A6. |
| `Guide_des_bonnes_pratiques_en_néphrologie_verte_Ve_260526_231812.pdf` | SFNDT 2026 — long guide | Chip **S26** · Qd 500→400 ml/min saves ~24 L dialysate + 60–100 L pretreated/session; RO reject reuse section; **Clinique Saint-Exupéry Toulouse: ~1,128 m³/yr, ~30 k€, 5–6 yr payback**; AP-HM Marseille studies; centralised concentrate distribution. Appendix A7 — closest match to the EcoDialysis playbook. |
| `Guide_de_la_néphrologie_verte_Version_courte_2026_260526_231654.pdf` | SFNDT 2026 — short guide | Companion to the long guide, used to cross-check operational claims. |

### `Guides/Impact environnemental du systeme de sante/`

Strategic and methodological reports framing why water is **adaptation-first** in dialysis (the carbon weight of water is real but secondary — ~1.0–1.1 tCO₂e on 4,200 m³ — water resilience and OPEX dominate the case).

| File | Source | Use in deck |
|---|---|---|
| `Planification écologique du système de santé.pdf` | French government — health system ecological planning roadmap | Chip **Gov** · health > 8 % of national GHG; care delivery ~45 %, products & medicines ~55 %; Scope 3 procurement dominates. Appendix A8, A9. |
| `TSP-Decarbonons-les-industries-des-medicaments-RF.pdf` | The Shift Project — decarbonising the medicines industry | Chip **TSP** · methodology spine for carbon claims; scope 3 framing. Appendix A9, A14. |
| `[PPJS] Guide méthodologique pour l_évaluation carbone des parcours de soin.pdf` | The Shift Project — care-pathway carbon methodology | Chip **TSP** · methodology box required on every quantified claim. Appendix A12, A16. |
| `240404-Rapport-Decarbonons-lAutonomie-The-Shift-Project-1-1.pdf` | The Shift Project — Decarbonising Autonomy | Chip **TSP** · system-resilience framing aligned with EcoDialysis positioning. |
| `La soutenabilité environnementale des systèmes de santé...` (IRDES) | IRDES — literature review on the environmental sustainability of health systems | Chip **Ird** · waste-stream context, DASRI/DAOM hierarchy, French action frame. Appendix A9, A10. |
| `L_empreinte climatique du secteur de la santé Health Care Without Harm.pdf` | HCWH — global health-sector climate footprint | Chip **HCW** · global-scale anchor. |
| `Green health how to decarbonise global healthcare systems.pdf` | HCWH / partners | Chip **HCW** · roadmap framing. |
| `Climate-friendly healthcare reducing the impacts of the healthcare sector on the world's climate.pdf` | HCWH | Chip **HCW** · background. |

---

## 5 · Other folders

| Folder | Contents |
|---|---|
| `Hackathon_PPT/` | ANDCS × MIT Hacking Medicine briefing materials — `Frameworks.pdf`, `Hack 101 - [PA26].pdf`, `Participant-handbook ANDCS x MIT.docx.pdf`. |
| `Old_Presentations/` | Historical pitch artefacts (v1 / v3 PPTX, intermediate HTML versions, pre-merge backups). Kept for traceability — **not** part of the current deck. |
| `_extracted_text_vendor_upgrade/` | Raw text extractions used during the evidence-audit phase. |
| `EcoDialysis_upgrade_evidence_audit.md` | Master integration checklist — every fact extracted from every source, mapped to its appendix slide. The single internal audit document behind the appendix. |

---

## 6 · Reliability ladder

The deck and executive summaries follow a strict source-reliability hierarchy:

1. **High** — regulation (Décret 2024-796), government roadmap, learned-society guides (SFNDT 2023 / 2026), The Shift Project, IRDES.
2. **Medium-high** — HCWH, corporate / vendor official sources, peer-reviewed.
3. **Medium** — deep-research syntheses (Per, Gem, Ope). Always paired with a higher-confidence source for any quantified claim.
4. **Low / excluded** — never cited.

---

## 7 · Discipline — what the deck refuses to claim

- No clinical-contact reuse. No used-dialysate recycling.
- No "carbon neutral" or "zero impact" claims. The water-only carbon caveat (~1.0–1.1 tCO₂e on 4,200 m³) is repeated everywhere the water case is made.
- No vendor lock-in. Neutral metrology, neutral integrator.
- No "approved by ARS at every site" — each site is a local decision.
- No CEE / Agence de l'Eau eligibility claim without written confirmation per basin.

See appendix slide **A16** for the full allowed-vs-forbidden claims table.

---

## 8 · Contact

Project owner: Victor Pimshin (@vpimshin).

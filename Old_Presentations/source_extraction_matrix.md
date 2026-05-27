# EcoDialysis Source Extraction Matrix

Prepared before HTML rewrite (deep-research integration step).

## 1) `Deep_Research/Water Sustainability Practices in Dialysis_OpenAI.pdf`
- **Source type:** PDF (deep research synthesis)
- **Key claims/data points (10-20):**
  1. RO reject reuse spans from ~1,000 L/week (small rural) to 13,140 m3/year (Bristol) (extracted lines ~8-10, 569-570).
  2. Canterbury case: 800 L/h reject recovery (lines 547-548, 728).
  3. Canterbury savings around GBP 7,500/year and capex around GBP 15,000 (lines 548-549, 730-733).
  4. Ashford implementation cost around GBP 2,500 in new-build context (lines 550, 753-755).
  5. Bristol water saving 13,140 m3/year (lines 569, 768-769).
  6. Bristol savings >GBP 15,000/year and capex ~GBP 45,000 (lines 570, 772-775).
  7. East Kent heat exchangers: ~0.86 kWh/treatment and projected 27,905 kWh/year over 52 machines (lines 791-795, 255-256).
  8. ANZSN disinfection optimization: >160,000 L/year water, 6.4 MWh/year power, 720 L citric acid avoided, ~USD 2,400 product savings (lines 961-974).
  9. Modern vs older Australian RO: 357 L and 3.1 kWh per treatment vs 548 L and 7.2 kWh (lines 1060-1068).
  10. Spain 20-center data: mean 476.5 L/HD; daily-opening 430.20 L/HD + 10.82 kWh/HD vs three-times-weekly 629.81 L/HD + 16.79 kWh/HD (lines 1002-1022).
  11. Barwon reuse reported ~100 kL/week service-wide and >20 kL/week one site (lines 877-879, 869-873).
  12. Bendigo reported ~1.7 ML/year potable substitution (lines 897-900).
  13. Queen Elizabeth Hospital reported ~1.5-2 ML/year (lines 947-948).
  14. Donald small-unit project around 1,000 L/week and A$4,110 system cost (lines 924-929).
  15. REDY concept ~6 L/treatment (line 675).
  16. NeoKidney cited 4.5-5 L/session and approvals pending (lines 676-678).
  17. AWAK pilot listed as pilot-stage wearable/regenerative pathway (lines 1078-1106).
  18. Evidence hierarchy explicitly distinguishes scalable near-term options vs low-readiness closed-loop patient-contact options (lines 1108-1124).
- **Relevant page/section:** Measured outcomes table and stakeholder sections in extracted text (lines 520-1124).
- **Confidence:** High for quoted case numbers where explicit; Medium for narrative extrapolations.
- **Insert into dossier:** Sections D, E, F, G, K, M.

## 2) `Deep_Research/Water Sustainability Practices in Dialysis_OpenAI.pdf` (cross-check in prior extraction copy)
- **Source type:** PDF
- **Key claims/data points:** Confirms same dataset and case-study set used above (Canterbury, Ashford, Bristol, Bendigo, Barwon, QEH, ANZSN, Spain, modern vs old RO, REDY/NeoKidney/AWAK).
- **Relevant page/section:** Prior `_extracted_text` version and `_extracted_text_upgrade` consistency check.
- **Confidence:** High (duplicate extraction consistency).
- **Insert into dossier:** Quality-control note in Appendix M.

## 3) `Deep_Research/EcoDialysis_Perplexity.pdf`
- **Source type:** PDF (market sizing and segmentation synthesis)
- **Key claims/data points (10-20):**
  1. France dialysis patients around 51,700 (2022 reference in extracted line 1).
  2. Around 77% in non-autonomous in-center/UDM units (line 1).
  3. Typical HD session range around 400-500 L feedwater and 50-70% RO reject (line 1).
  4. CHU/CHRU + large private clinics highlighted as first adopters.
  5. French health establishments count around 2,965 (public + private split shown in extracted text).
  6. Dialysis network estimate around 1,100-1,200 units (including 1,166 cited in source text).
  7. Segmentation logic: CHU/CHRU, large CH, large private clinics, medium hospitals, small units/home/self-dialysis.
  8. Reference center assumptions: 100 patients, 3 sessions/week, 156 sessions/year -> 15,600 sessions/year.
  9. RO reject assumption in model: 270 L/session.
  10. Potential saving ~4,200 m3/year from reference center model.
  11. CO2 estimate around 1.0-1.1 tCO2e/year for water-supply factor only.
  12. Explicit caveat that wastewater-treatment emissions are excluded in that estimate.
- **Relevant page/section:** Single-slide narrative extract text, model segments embedded.
- **Confidence:** Medium (secondary synthesis; requires primary-source confirmation for legal/official claims).
- **Insert into dossier:** Sections C, G, H, I, J, M.

## 4) `Deep_Research/EcoDialysis_Perplexity.docx`
- **Source type:** DOCX (zipxml extraction)
- **Key claims/data points (10-20):**
  1. Mirrors Perplexity PDF narrative.
  2. Reiterates 51,700 dialysis patients.
  3. Reiterates 77% non-autonomous in-center/UDM concentration.
  4. Reiterates 2,965 establishments estimate.
  5. Reiterates ~1,100-1,200 dialysis units figure.
  6. Contains CHU/CHRU-first adopter narrative.
  7. Contains 100-patient reference center assumptions.
  8. Contains 15,600 sessions/year calculation.
  9. Contains 270 L/session reject assumption.
  10. Contains ~4,200 m3/year water-saving estimate.
- **Relevant page/section:** Extracted text body; mirrors PDF deck text.
- **Confidence:** Medium.
- **Insert into dossier:** C, G, J, M (supporting duplicate source line).

## 5) `Deep_Research/Clinical and Technical Advancements in Dialysis_Gemini.pdf`
- **Source type:** PDF (technology taxonomy and maturity synthesis)
- **Key claims/data points (10-20):**
  1. 20-center Spain benchmark mean ~476.5 L/session.
  2. RO thermodynamic reject fraction often 50-67% in conventional systems.
  3. Distinguishes conductivity bands for reuse applications (<1500 vs 1500-2400 uS/cm) as operational design guide.
  4. Captures Canterbury 800 L/h reuse example.
  5. Captures Ashford laundry integration as design-in case.
  6. Captures Bristol boiler-steam diversion case.
  7. Captures high-recovery RO systems up to ~85% conversion claim (manufacturer-linked).
  8. Captures disinfection-optimization logic reducing redundant cycles.
  9. Captures heat-recovery examples (East Kent, Newcastle).
  10. Captures low-flow sorbent pathways (NeoKidney 4.5-5 L/session).
  11. Captures AWAK pilot safety/performance references.
  12. Provides maturity framing: proven / site-specific / pilot / conceptual.
  13. Recommends staged roadmap and metering-first deployment.
- **Relevant page/section:** Taxonomy and roadmap sections in extracted full-text.
- **Confidence:** Medium for synthesis, High for cited values reproduced from referenced cases.
- **Insert into dossier:** E, F, K, L, M.

## 6) `Deep_Research/Clinical and Technical Advancements in Dialysis_Gemini.docx`
- **Source type:** DOCX (zipxml extraction)
- **Key claims/data points (10-20):**
  1. Duplicates core taxonomy in PDF.
  2. Defines RO reject reuse as mature in selected non-clinical cases.
  3. Defines high-recovery RO optimization as ready-now optimization.
  4. Defines disinfection optimization as zero/low-capex operational lever.
  5. Defines heat recovery as implementation-ready in some contexts.
  6. Frames mixed wastewater/spent dialysate reuse as higher risk/complexity.
  7. Frames sorbent and portable systems as pilot/early clinical.
  8. Includes NeoKidney and AWAK references.
  9. Includes barriers: retrofit cost, metering gaps, governance.
  10. Includes phased implementation logic.
- **Relevant page/section:** Full-body extracted doc text.
- **Confidence:** Medium.
- **Insert into dossier:** E, K, L, M.

## 7) `Deep_Research/EcoDialysis_OpenAI.pdf`
- **Source type:** PDF (earlier strategic synthesis)
- **Key claims/data points (10-20):**
  1. Reinforces Measure-Reduce-Reuse narrative.
  2. Frames French launch with hospital-infrastructure focus.
  3. Supports sustainability-label concept.
  4. Supports operational (boiler-room) framing over abstract ESG.
  5. Highlights dialysis water waste salience.
  6. Uses in-center concentration logic for early GTM.
  7. Mentions non-clinical reuse boundary.
  8. Mentions case-led credibility approach.
  9. Mentions phased deployment and proof generation.
  10. Mentions performance dashboard and benchmarking as product core.
- **Relevant page/section:** extracted narrative text.
- **Confidence:** Medium (secondary synthesis).
- **Insert into dossier:** A, H, I, J, M.

## 8) `Deep_Research/EcoDialysis_Open_AI.docx`
- **Source type:** DOCX (zipxml extraction)
- **Key claims/data points (10-20):**
  1. Mirrors `EcoDialysis_OpenAI.pdf` messaging.
  2. Emphasizes measurable savings.
  3. Emphasizes non-clinical reuse only.
  4. Emphasizes pilot-to-scale logic.
  5. Emphasizes hospital infrastructure integration.
  6. Emphasizes label/certification concept.
  7. Emphasizes regulatory-readiness needs.
  8. Emphasizes economic framing for hospital buyers.
  9. Emphasizes monitoring and audit modules.
  10. Emphasizes no overclaiming for reimbursement.
- **Relevant page/section:** full-body extracted doc text.
- **Confidence:** Medium.
- **Insert into dossier:** A, H, I, J, M.

## 9) `Guide/Guide_des_bonnes_pratiques_en_néphrologie_verte_Ve_260526_231812.pdf`
- **Source type:** PDF (French professional guide, broad nephrology green practices 2026)
- **Key claims/data points (10-20):**
  1. Concrete action lever: reduce dialysate flow with safety framing.
  2. Example saving from Qd reduction 500->400 ml/min: ~24 L dialysate/session and ~60-100 L pretreated water/session.
  3. Mentions multicenter French trial planned on Qd reduction safety.
  4. Discusses HDF optimization scenarios and dialysate volumes.
  5. Discusses centralized acid concentrate distribution and reductions (e.g., liters saved).
  6. Dedicated section on reuse of RO reject (`réutiliser les rejets de l’osmose inverse`).
  7. Provides French examples (e.g., Saint-Exupéry Toulouse, AP-HM Marseille initiative).
  8. Reports Saint-Exupéry: ~1,128 m3/year saving, capex ~EUR30,000, payback ~5-6 years.
  9. Highlights storage constraints (72h, temperature, distance) from operational guidance.
  10. Explicitly separates potential uses and exclusions (e.g., not dialysate reuse for first-line practice).
  11. Covers energy levers and Eco Energie Tertiaire context.
  12. Covers waste/plastic and procurement/process levers.
  13. Includes organizational levers: governance, training, implementation planning.
  14. Includes hygiene/ARS context references for implementation.
  15. Provides checklists/focus sheets format suitable for EcoDialysis deployment playbook.
- **Relevant page/section:** extraction lines ~1220-1670 and ~1440-1600.
- **Confidence:** High for direct guide statements.
- **Insert into dossier:** D, E, F, H, K, L, M.

## 10) `Guide/Guide_de_la_néphrologie_verte_Version_courte_2026_260526_231654.pdf`
- **Source type:** PDF (short 2026 nephrology green guide)
- **Key claims/data points (10-20):**
  1. Provides condensed action priorities for nephrology teams.
  2. Covers water, energy, waste, procurement and behavior levers.
  3. Useful for communication-ready checklist framing.
  4. Supports green-team governance and training emphasis.
  5. Supports indicator tracking and action sequencing.
  6. Reinforces non-clinical reuse framing in operational context.
  7. Reinforces resource-intensity awareness across nephrology pathways.
  8. Supports implementation pragmatism for unit-level action.
  9. Useful bridge between technical guide and executive audience.
  10. Supports RSE/ESG integration language for hospitals.
- **Relevant page/section:** short guide full extract.
- **Confidence:** High for qualitative orientation; Medium for numeric details (fewer explicit values than full guide).
- **Insert into dossier:** A, H, J, L, M.

## 11) `Guide/SFNDT_guide complet-VF-HD-2_260526_231531.pdf`
- **Source type:** PDF (full SFNDT guide, 2023/updated extracts)
- **Key claims/data points (10-20):**
  1. Comprehensive nephrology-green recommendations.
  2. Emphasizes structured environmental management in dialysis units.
  3. Supports water reduction pathways across clinical and technical processes.
  4. Supports energy reduction pathways and monitoring practices.
  5. Supports waste and plastics reduction pathways.
  6. Supports training and culture-change as core implementation enablers.
  7. Supports use of audit/self-evaluation style tools.
  8. Supports integration with quality and procurement routines.
  9. Supports explicit safety boundaries in environmental actions.
  10. Supports progressive deployment and benchmarking mindset.
- **Relevant page/section:** full guide extraction (operational and recommendations sections).
- **Confidence:** High (professional guideline source).
- **Insert into dossier:** E, H, K, L, M.

## 12) `EcoDialysis/EcoDialysis_Pitch_v3.pptx` + `EcoDialysis-Pitch_v3.pdf`
- **Source type:** PPTX and PDF (company pitch material)
- **Key claims/data points (10-20):**
  1. Core brand line: sustainability label for nephrology.
  2. Core promise: turn wasted hospital water into measured savings, lower carbon, brand value.
  3. Narrative frame: boiler rooms, not boardrooms.
  4. Measure -> Reduce -> Reuse sequence.
  5. France-first rollout logic then Europe.
  6. Savings-based business model framing.
  7. Indicates French context around regulation and funding windows.
  8. Includes sample model values for reference-center economics.
  9. Emphasizes non-clinical boundary.
  10. Emphasizes stakeholder alignment and pilot asks.
- **Relevant page/section:** Slides 1-7 extracted in `_extracted_text_upgrade/EcoDialysis_Pitch_v3.txt`.
- **Confidence:** High for company positioning; Medium for market/regulatory claims unless externally validated.
- **Insert into dossier:** A, H, I, J.

## 13) `EcoDialysis/EcoDialysis Pitch_v1.html`
- **Source type:** HTML (design + prior narrative baseline)
- **Key claims/data points (10-20):**
  1. Defines visual identity (navy/blue, card/table style) to preserve.
  2. Existing seven-slide structure transformed to long-form dossier.
  3. Existing key numbers echoed from prior research and pitch narrative.
  4. Existing messaging around France launch opportunity.
  5. Existing emphasis on non-clinical reuse boundary.
  6. Existing value proposition around measurable hospital outcomes.
  7. Existing roadmap framing from pilot to scale.
  8. Existing business-model anchor around audit + monitoring + implementation.
  9. Existing source-footing style to replace with real source-specific citations.
  10. Existing deck style adapted for print-friendly long-form HTML.
- **Relevant page/section:** Embedded template/deck structure in HTML.
- **Confidence:** High for style and internal positioning use.
- **Insert into dossier:** global style + section layout.

## 14) Official French regulation/policy web sources used for legal framing
- **Source type:** Official web/legal texts retrieved in prior step
- **Key claims/data points (10-20):**
  1. Decree n°2024-796 (12 July 2024) created EICH domestic-use CSP framework.
  2. Framework entered into force Sept 1, 2024.
  3. Health establishments are sensitive ERP in this framework.
  4. Prefectural authorization generally required for sensitive ERP systems.
  5. ARS provides key technical/health review role.
  6. Separation of potable/non-potable networks required.
  7. Signage and anti-cross-connection obligations required.
  8. Sanitary logbook (carnet sanitaire) and maintenance obligations required.
  9. Certain uses are allowed under conditions, with category and site constraints.
  10. Plan Eau objective includes national -10% abstraction trajectory to 2030.
- **Relevant page/section:** Decree/ministerial pages extracted into local `agent-tools/*.txt` during legal check.
- **Confidence:** High for direct decree statements; Medium for implementation interpretation.
- **Insert into dossier:** B, K, L, M.

---

## Extraction status summary
- **All target PDFs:** extracted successfully.
- **All target DOCX:** extracted successfully via zip-XML fallback.
- **PPTX:** extracted successfully via zip-XML fallback.
- **Failed extraction files:** none.

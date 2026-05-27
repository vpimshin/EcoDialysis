# Source chip helper
def C(*ids):
    labels={'per':'Per','gem':'Gem','ope':'Ope','s23':'S23','s26':'S26','gov':'Gov','tsp':'TSP','ird':'Ird','hcw':'HCW','pch':'Pch'}
    return ' '.join(f'<a class="src" href="#src-{i}">{labels[i]}</a>' for i in ids)

# Each slide: (id, kind, title, html_inner, speaker_notes)
# kind: 'cover'|'divider'|'content'|'appendix'

SLIDES_EN = []

def add(sid, kind, title, body, notes=""):
    SLIDES_EN.append((sid, kind, title, body, notes))

# =========== PART 1: HOOK & URGENCY ===========
add("title","cover","",
"""
<div class="eyebrow">ANDCS × MIT Hacking Medicine · Sustainable Care · Paris 2026</div>
<h1>Dialysis has a hidden<br/>water vulnerability.</h1>
<p class="lead">EcoDialysis turns wasted dialysis water into a managed<br/>resilience asset — measurable, redesigned, certified.</p>
<div style="margin-top:32px;display:flex;gap:32px;color:#cfe1f7;font-size:14px;letter-spacing:1.5px">
  <span><b style="color:var(--blue2)">270 L</b> rejected per session</span>
  <span><b style="color:var(--blue2)">15,600</b> sessions / yr / center</span>
  <span><b style="color:var(--blue2)">~4,200 m³</b> wasted / yr / center</span>
</div>
""",
"Open on water vulnerability framing. Adaptation first, mitigation second. Dialysis is the wedge into hospital water resilience.")

add("agenda","content","Strategic agenda — from hidden waste to certified water resilience",
"""
<p class="lead">Six moves. Each one is also an EcoDialysis revenue line.</p>
<div class="grid3">
  <div class="card"><h3>1 · See the problem</h3><p>Make a hospital's hidden dialysis water flow visible at session level.</p></div>
  <div class="card"><h3>2 · Choose the right reuse</h3><p>Green / orange / red map of every non-clinical reuse route.</p></div>
  <div class="card"><h3>3 · File the dossier</h3><p>EICH-compliant ARS / préfecture safety case per site.</p></div>
  <div class="card"><h3>4 · Implement &amp; meter</h3><p>4-point metering, separated network, anti-backflow, carnet sanitaire.</p></div>
  <div class="card"><h3>5 · Verify savings</h3><p>SaaS dashboard, monthly verification, KPI proofs to ARS and finance.</p></div>
  <div class="card"><h3>6 · Certify &amp; scale</h3><p>EcoDialysis label → GHT / private-network rollout → European expansion.</p></div>
</div>
<p style="margin-top:12px;font-size:13px;color:#56698a">Adaptation first, mitigation second. """+C('pch','s26','gov')+"""</p>
""",
"Frame the agenda as a six-step asset. Each step maps to a revenue line.")

add("why-now","content","Why water, why now — hospitals enter a water-constrained decade",
"""
<div class="grid">
  <div>
    <div class="card accent"><h3>The new operating reality</h3>
      <ul>
        <li><b>Scarcity:</b> France basins facing structural deficit (Loire, Adour-Garonne, PACA).</li>
        <li><b>Regulation:</b> Décret n°2024-796 (12 July 2024, in force 1 Sept 2024) opens non-clinical reuse pathway.</li>
        <li><b>Tariffs:</b> water + sewer indexation hitting hospital opex; sewer often &gt; potable.</li>
        <li><b>Continuity:</b> droughts and restrictions threaten technical functions in summer.</li>
        <li><b>Reporting:</b> Planification écologique du système de santé requires per-establishment water plans. """+C('gov','tsp','ird')+"""</li>
      </ul>
    </div>
  </div>
  <div>
    <div class="banner">Water will become an <b>operating constraint</b>,<br/>not a sustainability metric.</div>
    <div class="card"><h3>Why hospitals can't wait</h3>
      <ul>
        <li>Healthcare = <b>&gt;8% of national GHG</b>, ~50 MtCO₂e (offer of care 45%, products 55%). """+C('gov','hcw')+"""</li>
        <li>Care offer = buildings, energy, <b>water</b>, waste, transport.</li>
        <li>Dialysis is the most water-intensive recurring hospital workflow.</li>
        <li>Water adaptation pays back in opex <b>before</b> carbon counts.</li>
      </ul>
    </div>
  </div>
</div>
""",
"Lead with scarcity, regulation, tariffs, continuity. Carbon is co-benefit. Cite Décret 2024-796.")

add("why-dialysis","content","Why dialysis is the right first hospital department",
"""
<div class="grid3">
  <div class="card"><h3>Measurable</h3><p>Closed technical loop. Every session has a known feedwater, reject volume, energy draw. <b>~400–500 L</b> feedwater, <b>50–70%</b> reject. """+C('per','gem','ope')+"""</p></div>
  <div class="card"><h3>Recurring</h3><p>~156 sessions / patient / year. 100-patient center = <b>15,600 sessions / yr</b>. Predictable savings.</p></div>
  <div class="card"><h3>Technically actionable</h3><p>RO reject = controlled technical stream, not patient wastewater. Reuse routes already proven internationally. """+C('ope','gem')+"""</p></div>
  <div class="card"><h3>Clinically bounded</h3><p>No patient contact reuse. Never back to dialysis-water production. Never spent dialysate. Boundary is the wedge of trust.</p></div>
  <div class="card"><h3>Policy-aligned</h3><p>SFNDT Guide des bonnes pratiques 2026 explicitly covers RO-reject reuse. """+C('s26','s23')+"""</p></div>
  <div class="card dark"><h3>Strategic</h3><p>Win dialysis first → expand to sterilization, laundry, kitchens, technical loops.</p></div>
</div>
""",
"Five reasons dialysis is the entry point. Sixth card = expansion logic.")

add("what-wasted","content","What exactly is wasted — the dialysis water flow",
"""
<div class="grid">
  <div>
    <h3>One session, simplified</h3>
    <div class="flow">
      <div class="step">Mains potable</div><span class="arrow">›</span>
      <div class="step">Pretreatment<br/><small>filters · softener · carbon</small></div><span class="arrow">›</span>
      <div class="step">RO skid<br/><small>permeate / reject</small></div><span class="arrow">›</span>
      <div class="step">Dialysate loop<br/><small>generator + dialyzer</small></div><span class="arrow">›</span>
      <div class="step">Drain</div>
    </div>
    <div class="grid3" style="margin-top:8px">
      <div class="kpi"><div class="v">400–500 L</div><div class="l">Feedwater / session</div><div class="s">"""+C('per','gem')+"""</div></div>
      <div class="kpi"><div class="v">50–70 %</div><div class="l">RO reject fraction</div><div class="s">"""+C('per','ope')+"""</div></div>
      <div class="kpi"><div class="v">270 L</div><div class="l">Base reject / session</div><div class="s">220 low · 320 high · """+C('per')+"""</div></div>
    </div>
  </div>
  <div>
    <div class="card"><h3>The hidden three streams</h3>
      <ul>
        <li><b>RO concentrate (reject):</b> clean, low-salt, controlled. Highest reuse value.</li>
        <li><b>Disinfection &amp; rinse water:</b> intermittent, contains residual chemicals — reuse only after dilution / neutralization.</li>
        <li><b>Spent dialysate:</b> patient-contact — <b>never</b> reused. <span class="tag-bad">RED</span></li>
      </ul>
    </div>
    <div class="card accent"><h3>Hidden energy too</h3>
      <p>Older Australian RO: <b>548 L + 7.2 kWh</b> / treatment. Modern RO: <b>357 L + 3.1 kWh</b>. """+C('ope')+"""</p>
      <p>East Kent heat exchangers: <b>0.86 kWh/treatment</b> recoverable, <b>27,905 kWh/yr</b> projected. """+C('ope')+"""</p>
    </div>
  </div>
</div>
""",
"Show one-session flow. Three streams: green (reject), orange (rinse), red (spent dialysate).")

# =========== PART 2: MEASUREMENT & REUSE ===========
add("div-measure","divider","Part 2 — Measurement & Reuse",
"""<p class="lead">If you cannot measure the water, you cannot redesign it.<br/>If you cannot redesign it, you cannot certify it.</p>""",
"Transition. Measurement-first principle from SFNDT.")

add("measure","content","How the water is measured — 4-point metering architecture",
"""
<div class="grid">
  <div>
    <h3>The four meters</h3>
    <div class="card"><ul>
      <li><b>M1 · Mains-in</b> — total feedwater entering the dialysis water plant.</li>
      <li><b>M2 · RO permeate</b> — water actually delivered to dialysate loop.</li>
      <li><b>M3 · RO reject</b> — controlled technical stream candidate for reuse.</li>
      <li><b>M4 · Reuse delivery</b> — water actually substituted in toilets / cooling / cleaning.</li>
    </ul></div>
    <div class="card accent"><h3>Plus context channels</h3>
      <ul>
        <li>Conductivity on M3 → routing logic (high salt → drain, low salt → reuse). """+C('gem')+"""</li>
        <li>Pressure + flow on reuse loop → leak and stagnation detection.</li>
        <li>Energy submeter on RO + heat-exchanger (optional).</li>
        <li>Time-stamped to session log → L/session benchmark.</li>
      </ul>
    </div>
  </div>
  <div>
    <h3>Why measurement-first wins</h3>
    <div class="card dark"><p>SFNDT 2023 and SFNDT 2026 both place <b>measurement-first</b> at the heart of green nephrology. """+C('s23','s26')+"""</p>
    <p>TSP Pathway methodology: objective, perimeter, transparent assumptions, uncertainty studies. """+C('tsp')+"""</p>
    <p>No measurement → no ARS dossier, no CEE, no savings claim.</p></div>
    <div class="card"><h3>From meter to evidence</h3>
      <ul>
        <li>Baseline 4–6 weeks before any intervention.</li>
        <li>Continuous logging post-intervention.</li>
        <li>Monthly verification report to direction, technique, hygiene.</li>
        <li>Quarterly KPI bundle to ARS &amp; finance.</li>
      </ul>
    </div>
  </div>
</div>
""",
"Four meters, plus conductivity, pressure, energy. Measurement is the moat.")

add("reference","content","Reference center model — 100 patients, 15,600 sessions",
"""
<p class="lead">A standard mid-size French in-center / UDM unit. The math hospitals can verify against their own bills. """+C('per')+"""</p>
<div class="grid4">
  <div class="kpi"><div class="v">100</div><div class="l">Patients</div></div>
  <div class="kpi"><div class="v">156</div><div class="l">Sessions / patient / yr</div></div>
  <div class="kpi"><div class="v">15,600</div><div class="l">Sessions / yr</div></div>
  <div class="kpi"><div class="v">~4,200 m³</div><div class="l">Reject / yr (base)</div></div>
</div>
<div class="grid3" style="margin-top:14px">
  <div class="card"><h3>Low scenario</h3>
    <p><b>220 L</b> reject / session</p>
    <p><b>3,432 m³</b> / yr</p>
    <p>Modern RO, optimized disinfection.</p>
  </div>
  <div class="card accent"><h3>Central scenario</h3>
    <p><b>270 L</b> reject / session</p>
    <p><b>4,212 m³</b> / yr</p>
    <p>Typical mid-life equipment.</p>
  </div>
  <div class="card"><h3>High scenario</h3>
    <p><b>320 L</b> reject / session</p>
    <p><b>4,992 m³</b> / yr</p>
    <p>Aging RO + 3×/week schedule. """+C('ope')+"""</p>
  </div>
</div>
<p style="margin-top:10px;font-size:13px;color:#56698a">Water-only carbon caveat: ~1.0–1.1 tCO₂e / yr for the 4,200 m³ band — secondary to opex resilience. """+C('per','tsp')+"""</p>
""",
"Three scenarios, hospital can verify itself. Carbon is secondary co-benefit.")

add("reuse-map","content","What can be reused — the green / orange / red map",
"""
<div class="grid3">
  <div class="card" style="border-left:6px solid var(--ok)">
    <h3 style="color:var(--ok)">GREEN — reuse now</h3>
    <ul>
      <li>Toilet flushing in non-clinical zones</li>
      <li>Floor &amp; outdoor cleaning</li>
      <li>HVAC cooling-tower make-up (with treatment)</li>
      <li>Garden / outdoor watering</li>
      <li>Technical washing (carts, bins)</li>
    </ul>
    <p style="font-size:12px;color:var(--ok)"><b>Evidence:</b> Canterbury, Bristol, Ashford, ANZSN. """+C('ope','gem')+"""</p>
  </div>
  <div class="card" style="border-left:6px solid var(--warn)">
    <h3 style="color:var(--warn)">ORANGE — site-specific</h3>
    <ul>
      <li>Laundry pre-wash</li>
      <li>Sterilization feed (non-final-rinse)</li>
      <li>Boiler / cooling make-up with extra polishing</li>
      <li>Pretreatment recycle (recovery RO) — vendor-specific</li>
      <li>Disinfection rinse reuse — only after neutralization</li>
    </ul>
    <p style="font-size:12px;color:var(--warn)"><b>Caveat:</b> requires dossier, local water quality, vendor sign-off.</p>
  </div>
  <div class="card" style="border-left:6px solid var(--bad)">
    <h3 style="color:var(--bad)">RED — never reuse</h3>
    <ul>
      <li>Spent dialysate (patient contact)</li>
      <li>Any return to dialysis-water production</li>
      <li>Drinking / food-prep water</li>
      <li>Patient-contact equipment final rinse</li>
      <li>Endoscope / surgical-instrument final rinse</li>
    </ul>
    <p style="font-size:12px;color:var(--bad)"><b>Non-negotiable.</b> The safety boundary is the wedge of trust.</p>
  </div>
</div>
<div class="banner" style="margin-top:14px">The question is <b>not</b> whether water can be reused.<br/>The question is <b>which water, where, under which legal and safety conditions</b>.</div>
""",
"Decision map. Boundary is non-negotiable.")

add("legal-eich","content","Current law vs new EICH framework",
"""
<div class="grid">
  <div>
    <div class="card"><h3>Before — pre 1 Sept 2024</h3>
      <ul>
        <li>No general non-potable reuse framework in healthcare.</li>
        <li>Ad-hoc derogations from ARS / DDETSPP.</li>
        <li>Reuse projects stalled in legal uncertainty.</li>
      </ul>
    </div>
    <div class="card accent"><h3>After — <b>Décret n°2024-796</b>, in force 1 Sept 2024</h3>
      <p><b>EICH</b> = Eaux Impropres à la Consommation Humaine (non-potable waters) framework for sensitive establishments including healthcare. """+C('gov','s26')+"""</p>
      <ul>
        <li>Permits non-clinical reuse with site-specific authorization.</li>
        <li>Requires ARS / préfecture safety case.</li>
        <li>Separate network, anti-backflow, signage, carnet sanitaire.</li>
        <li>Monitoring &amp; emergency stop required.</li>
        <li>Defines authorized uses, not a blanket licence.</li>
      </ul>
    </div>
  </div>
  <div>
    <div class="card dark"><h3>What EICH does NOT do</h3>
      <ul>
        <li>Does not authorize any patient-contact reuse.</li>
        <li>Does not pre-approve any site — every dossier is local.</li>
        <li>Does not waive hygiene committee (CLIN) sign-off.</li>
        <li>Does not guarantee tariff savings — local sewer / potable structure decides.</li>
      </ul>
    </div>
    <div class="banner">EICH opens the door.<br/>EcoDialysis builds the dossier.</div>
    <p style="font-size:12px;color:#56698a">Caveat: exact ARS pathway and monitoring frequency vary by basin and establishment type. Confirm at each filing. See Appendix H. """+C('gov')+"""</p>
  </div>
</div>
""",
"Décret 2024-796 is the unlock. EcoDialysis turns it into a repeatable dossier.")

add("dossier","content","What an ARS / préfecture dossier must contain",
"""
<div class="grid">
  <div>
    <h3>Mandatory technical content</h3>
    <div class="card"><ul>
      <li>Source description: RO reject characterization (conductivity, microbio, chemicals).</li>
      <li>Use description: target uses, volumes, locations.</li>
      <li>Separated network: schematic, materials, anti-backflow devices (EA / EB / AA).</li>
      <li>Storage: volume, residence time, materials, anti-stagnation logic.</li>
      <li>Treatment if any: UV-C, filtration, disinfection.</li>
      <li>Monitoring plan: parameters, frequency, alarms.</li>
      <li>Emergency stop &amp; fallback to potable.</li>
      <li>Carnet sanitaire entry and responsibilities.</li>
    </ul></div>
  </div>
  <div>
    <h3>Mandatory governance content</h3>
    <div class="card accent"><ul>
      <li>Risk analysis (HACCP-like) per use.</li>
      <li>Sign-off chain: direction, technique, hygiène (CLIN), médical, qualité.</li>
      <li>Staff training plan + signage program.</li>
      <li>Maintenance plan + service contracts.</li>
      <li>Annual review &amp; reporting to ARS.</li>
      <li>Stakeholder map (ARS, préfecture, Agence de l'Eau, hygiène).</li>
    </ul></div>
    <div class="banner">EcoDialysis delivers <b>both</b> stacks as a single repeatable playbook.</div>
  </div>
</div>
<p style="margin-top:8px;font-size:12px;color:#56698a">Sources: """+C('gov','s26','s23')+"""</p>
""",
"Walk through dossier contents. Show technical + governance stacks.")

add("tailored","content","Why every site needs a tailored playbook",
"""
<p class="lead">A site-specific playbook is not optional. The same RO reject does not have the same destiny in every hospital.</p>
<div class="grid">
  <div class="card"><h3>What varies by site</h3>
    <ul>
      <li><b>Water quality:</b> mains hardness, chloride, silica — drives reuse polishing need.</li>
      <li><b>Tariff structure:</b> water + sewer per m³ — drives ROI.</li>
      <li><b>Layout:</b> dialysis unit floor, toilets distance, technical loops accessibility — drives CAPEX.</li>
      <li><b>RO age:</b> determines reject volume (220–320 L).</li>
      <li><b>Demand profile:</b> session schedule vs reuse-point demand — drives storage sizing.</li>
      <li><b>Governance:</b> CHU vs CH vs private — drives sign-off path.</li>
    </ul>
  </div>
  <div class="card accent"><h3>Why a generic tank fails</h3>
    <ul>
      <li>Wrong size → either overflow or starvation.</li>
      <li>Wrong polishing → biofilm or chemistry mismatch.</li>
      <li>Wrong network → backflow risk, ARS rejection.</li>
      <li>Wrong demand match → empty &lt;30% of the time.</li>
      <li>Wrong reporting → no ROI verification, no certification.</li>
    </ul>
    <p style="margin-top:8px"><b>Hospitals do not need another ESG dashboard.<br/>They need an operational water-resilience playbook.</b></p>
  </div>
</div>
""",
"Justify playbook over generic product. Six variables → tailored dossier.")

# =========== PART 3: PROOF ===========
add("div-proof","divider","Part 3 — Proof",
"""<p class="lead">International centers already prove that reuse and optimization work.<br/>The hard part is not the tank — it is the repeatable site-specific dossier.</p>""",
"Transition to evidence.")

add("intl-map","content","International proof — eight reference centers",
"""
<div class="grid4">
  <div class="card"><h3>Canterbury · UK</h3><p><b>800 L/h</b> RO-reject recovery, <b>~£7,500/yr</b>. """+C('ope')+"""</p></div>
  <div class="card"><h3>Bristol · UK</h3><p><b>13,140 m³/yr</b>, <b>&gt;£15,000/yr</b>. """+C('ope')+"""</p></div>
  <div class="card"><h3>Ashford · UK</h3><p>Design-in route at <b>~£2,500</b>. """+C('ope')+"""</p></div>
  <div class="card"><h3>East Kent · UK</h3><p>Heat recovery <b>0.86 kWh/Tx</b>, <b>27,905 kWh/yr</b>. """+C('ope','gem')+"""</p></div>
  <div class="card"><h3>Bendigo · AU</h3><p>RO-reject reuse, named ANZSN benchmark.</p></div>
  <div class="card"><h3>Queen Elizabeth · AU</h3><p>Modern RO retrofit, lower L+kWh per Tx.</p></div>
  <div class="card"><h3>Barwon · AU</h3><p>Process optimization &amp; metering case.</p></div>
  <div class="card"><h3>Spain · 20 centers</h3><p>Mean <b>476.5 L/session</b>; daily-opening <b>430 L</b> vs 3×/wk <b>630 L</b>. """+C('ope','gem')+"""</p></div>
</div>
<p style="margin-top:10px;font-size:13px;color:#56698a">All evidence aggregated and verifiable via Appendix B (case-study table) and Appendix I (sources).</p>
""",
"Eight cards = international proof. Detail in cluster slides next.")

add("uk-cluster","content","UK case cluster — Canterbury · Bristol · Ashford · East Kent",
"""
<table>
<tr><th>Center</th><th>Intervention</th><th>Volume saved</th><th>Money saved</th><th>Energy / co-benefit</th><th>Source</th></tr>
<tr><td>Canterbury</td><td>RO-reject recovery → toilets &amp; cleaning</td><td><b>800 L/h</b></td><td>~£7,500/yr</td><td>—</td><td>"""+C('ope')+"""</td></tr>
<tr><td>Bristol</td><td>RO-reject reuse (large center)</td><td><b>13,140 m³/yr</b></td><td>&gt;£15,000/yr</td><td>—</td><td>"""+C('ope')+"""</td></tr>
<tr><td>Ashford</td><td>Design-in at new build</td><td>n/a low capex</td><td>~£2,500 design-in</td><td>—</td><td>"""+C('ope')+"""</td></tr>
<tr><td>East Kent</td><td>Heat exchanger recovery</td><td>—</td><td>—</td><td><b>0.86 kWh/Tx · 27,905 kWh/yr</b></td><td>"""+C('ope','gem')+"""</td></tr>
</table>
<div class="grid" style="margin-top:14px">
  <div class="card accent"><h3>Pattern</h3>
    <ul>
      <li>Design-in beats retrofit on capex (Ashford).</li>
      <li>Bigger centers compound savings (Bristol).</li>
      <li>RO-reject is the dominant lever (Canterbury, Bristol).</li>
      <li>Heat recovery is a second lever — pairs with reject reuse (East Kent).</li>
    </ul>
  </div>
  <div class="card"><h3>Translation to France</h3>
    <ul>
      <li>UK uses NHS-style local approvals — France adds ARS / EICH layer.</li>
      <li>UK tariffs differ — French ROI uses local water+sewer per m³.</li>
      <li>UK shows reuse is technically routine — the missing layer in France is the dossier.</li>
    </ul>
  </div>
</div>
""",
"UK cluster shows reuse + heat recovery patterns; France-specific layer is dossier.")

add("anz-cluster","content","Australia / New Zealand — ANZSN, Bendigo, Queen Elizabeth, Barwon",
"""
<div class="grid">
  <div>
    <div class="card"><h3>ANZSN aggregated impact</h3>
      <ul>
        <li><b>&gt;160,000 L/yr</b> water saved</li>
        <li><b>6.4 MWh/yr</b> electricity saved</li>
        <li><b>720 L</b> citric acid solution avoided</li>
        <li><b>~AU$2,400</b> product savings</li>
      </ul>
      <p style="font-size:12px;color:#56698a">Source: """+C('ope')+"""</p>
    </div>
    <div class="card accent"><h3>Modern vs old RO — measured</h3>
      <table>
        <tr><th></th><th>Old</th><th>Modern</th></tr>
        <tr><td>L / treatment</td><td>548</td><td><b>357</b></td></tr>
        <tr><td>kWh / treatment</td><td>7.2</td><td><b>3.1</b></td></tr>
      </table>
      <p style="font-size:12px;margin-top:6px">RO replacement alone yields a <b>~35% water + 57% energy</b> per-treatment cut. """+C('ope')+"""</p>
    </div>
  </div>
  <div>
    <div class="card dark"><h3>Why this matters for the playbook</h3>
      <ul>
        <li>Even <b>without</b> reuse, RO replacement is a major lever.</li>
        <li>Disinfection optimization (citric / heat) saves chemicals + water + carbon together.</li>
        <li>Process improvement and reuse are <b>additive</b>, not alternatives.</li>
        <li>ANZSN proves a green-nephrology network can publish results — basis for the EcoDialysis label.</li>
      </ul>
    </div>
    <div class="card"><h3>Bendigo · Queen Elizabeth · Barwon</h3>
      <p>Each is a named ANZSN benchmark in RO-reject reuse, modern-RO retrofit, and process metering respectively. They form a triple-case template the French market currently lacks. """+C('ope','gem')+"""</p>
    </div>
  </div>
</div>
""",
"ANZSN aggregated savings + measured RO replacement evidence.")

add("optim","content","Process optimization proof — Spain, modern RO, disinfection",
"""
<div class="grid">
  <div>
    <h3>Spain · 20-center benchmark</h3>
    <div class="card">
      <table>
        <tr><th>Cohort</th><th>L / HD</th><th>kWh / HD</th></tr>
        <tr><td>20-center mean</td><td><b>476.5</b></td><td>—</td></tr>
        <tr><td>Daily-opening centers</td><td><b>430.20</b></td><td><b>10.82</b></td></tr>
        <tr><td>3×/week centers</td><td><b>629.81</b></td><td><b>16.79</b></td></tr>
      </table>
      <p style="font-size:12px;margin-top:6px">Schedule shape is a <b>direct</b> water + energy lever. """+C('ope','gem')+"""</p>
    </div>
  </div>
  <div>
    <h3>The three optimization levers</h3>
    <div class="card accent"><ul>
      <li><b>Equipment:</b> modern RO (357 L vs 548 L; 3.1 kWh vs 7.2 kWh). """+C('ope')+"""</li>
      <li><b>Schedule:</b> daily vs 3×/week pattern (430 L vs 630 L / HD). """+C('ope')+"""</li>
      <li><b>Disinfection:</b> citric vs heat, frequency optimization, water + chemical avoidance. """+C('gem','s26')+"""</li>
    </ul></div>
    <div class="card"><h3>Inside the dialysate loop</h3>
      <ul>
        <li>Qd reduction (e.g. 500 → 400 ml/min): <b>~24 L dialysate</b> savings/session in cited framing. """+C('s26')+"""</li>
        <li><b>60–100 L</b> pretreated water economy per session in same context. """+C('s26')+"""</li>
        <li>HDF tuning, conductivity-routed reject. """+C('gem')+"""</li>
      </ul>
    </div>
  </div>
</div>
""",
"Three optimization levers, all measured.")

add("fr-proof","content","French proof — Saint-Exupéry, AP-HM, SFNDT playbook",
"""
<div class="grid">
  <div>
    <div class="card"><h3>Clinique Saint-Exupéry · Toulouse</h3>
      <ul>
        <li><b>~1,128 m³/yr</b> water saved (RO-reject reuse). """+C('s26')+"""</li>
        <li>Investment <b>~€30k</b>, payback <b>5–6 years</b>.</li>
        <li>French operational template — the closest match to EcoDialysis reference center.</li>
      </ul>
    </div>
    <div class="card accent"><h3>AP-HM · Marseille</h3>
      <ul>
        <li>Larger-reuse-potential studies referenced.</li>
        <li>Shows CHU-scale interest and ARS pathway feasibility. """+C('s26')+"""</li>
      </ul>
    </div>
  </div>
  <div>
    <div class="card dark"><h3>SFNDT 2026 playbook — what it confirms</h3>
      <ul>
        <li>RO-reject reuse is a recommended action sheet. """+C('s26')+"""</li>
        <li>Centralized acid-concentrate reduces waste &amp; consumption.</li>
        <li>Storage constraints: duration, temperature, distance.</li>
        <li>Separate-network requirements.</li>
        <li>No direct leap to high-risk reuse.</li>
        <li>Energy management obligations, waste reduction, staff actions, RSE communication.</li>
      </ul>
    </div>
    <div class="banner">France has the cases.<br/>France has the guide.<br/>France lacks the <b>repeatable dossier engine</b>.</div>
  </div>
</div>
""",
"Saint-Exupéry is the French anchor. SFNDT 2026 = the playbook source.")

# =========== PART 4: PRODUCT ===========
add("div-product","divider","Part 4 — Product",
"""<p class="lead">Not a tank. Not an ESG report. A site-specific water-resilience playbook<br/>delivered as audit + dossier + implementation + monitoring + label.</p>""",
"Transition to product.")

add("not-tank","content","Why not just buy a tank?",
"""
<div class="grid">
  <div>
    <h3>The tank fantasy</h3>
    <div class="card"><p>"Just install a tank under the RO and reuse the water."</p>
    <p style="margin-top:6px;color:#56698a"><i>This view dies on first contact with the hospital water plant.</i></p></div>
    <h3 style="margin-top:14px">What a tank cannot do</h3>
    <ul class="xlist">
      <li>Cannot characterize the reject stream</li>
      <li>Cannot match volumes to non-clinical demand</li>
      <li>Cannot file the EICH dossier</li>
      <li>Cannot operate the separated network</li>
      <li>Cannot pass CLIN review</li>
      <li>Cannot prove the savings</li>
      <li>Cannot scale across a GHT</li>
    </ul>
  </div>
  <div>
    <h3>What EcoDialysis does instead</h3>
    <ul class="checklist">
      <li><b>Audit</b> — 4-point metering + bills + plans + RO inventory.</li>
      <li><b>Map</b> — green/orange/red reuse routes for this exact site.</li>
      <li><b>Size</b> — storage + network + treatment matched to demand profile.</li>
      <li><b>File</b> — EICH-compliant ARS dossier with sign-off chain.</li>
      <li><b>Implement</b> — partner with plumbers / integrators / RO vendors.</li>
      <li><b>Meter</b> — continuous SaaS monitoring + monthly verification.</li>
      <li><b>Certify</b> — EcoDialysis label per site, benchmarkable.</li>
    </ul>
    <div class="banner" style="margin-top:8px">A tank is a component.<br/>A <b>dossier engine</b> is the product.</div>
  </div>
</div>
""",
"Tank vs dossier engine. Contrast is the positioning.")

add("product","content","Product architecture — audit · playbook · implementation · monitoring · label",
"""
<div class="grid5">
  <div class="card"><h3>1 · Audit</h3>
    <ul>
      <li>Site visit + data pull</li>
      <li>4-point meter install</li>
      <li>Bills &amp; tariff analysis</li>
      <li>Demand map</li>
      <li>Baseline 4–6 wk</li>
    </ul>
    <p><span class="pill">€8–18k</span></p>
  </div>
  <div class="card"><h3>2 · Playbook</h3>
    <ul>
      <li>Green / orange / red map</li>
      <li>Scenario ROI</li>
      <li>EICH dossier draft</li>
      <li>Risk register</li>
      <li>Go / no-go</li>
    </ul>
    <p><span class="pill">€10–25k</span></p>
  </div>
  <div class="card"><h3>3 · Implementation</h3>
    <ul>
      <li>Tender support</li>
      <li>Integrator coordination</li>
      <li>Hygiene sign-off</li>
      <li>Commissioning</li>
      <li>Staff training</li>
    </ul>
    <p><span class="pill">5–15 % of CAPEX</span></p>
  </div>
  <div class="card"><h3>4 · Monitoring</h3>
    <ul>
      <li>SaaS dashboard</li>
      <li>4-point + conductivity</li>
      <li>Monthly verification</li>
      <li>ARS reporting</li>
      <li>Alarms &amp; carnet</li>
    </ul>
    <p><span class="pill">€600–1,400 / month</span></p>
  </div>
  <div class="card dark"><h3>5 · Label</h3>
    <ul>
      <li>EcoDialysis certification</li>
      <li>Benchmark database</li>
      <li>Annual audit</li>
      <li>Public registry</li>
      <li>Network effect</li>
    </ul>
    <p style="color:#cfe1f7"><span class="pill" style="background:#1d4a8d;color:#fff">€3–8k / yr</span></p>
  </div>
</div>
<p style="margin-top:10px;font-size:13px;color:#56698a">Wedge = audit. Repeatability = playbook. Recurring = monitoring. Network = label. Defensibility = benchmark database. """+C('pch','per','s26')+"""</p>
""",
"Five product layers map to five revenue lines.")

add("ecosystem","content","Equipment &amp; supplier ecosystem",
"""
<table>
<tr><th>Layer</th><th>Equipment</th><th>Reference suppliers</th><th>EcoDialysis touchpoint</th></tr>
<tr><td>Dialysis generator</td><td>Hemodialysis machines</td><td>Fresenius, B. Braun, Baxter/Vantive, Nikkiso, Nipro, JMS, Quanta, Outset/Tablo, NxStage</td><td>Qd / HDF tuning, energy submetering</td></tr>
<tr><td>Water-treatment plant</td><td>Pretreatment + RO skid + loop</td><td>B. Braun AQUAboss, Fresenius, integrators</td><td>4-point metering, reject characterization</td></tr>
<tr><td>Dialyzer + bloodlines</td><td>Membranes &amp; circuits</td><td>Asahi Kasei, Toray, Fresenius, B. Braun, Nipro</td><td>Procurement scorecard (Phase 3)</td></tr>
<tr><td>Acid concentrate / bicarbonate</td><td>Liquid + cartridge</td><td>Fresenius, B. Braun, Baxter, regional</td><td>Centralized distribution playbook """+C('s26')+"""</td></tr>
<tr><td>Disinfection</td><td>Citric, heat, peracetic</td><td>Vendor-bundled</td><td>Frequency optimization """+C('gem','ope')+"""</td></tr>
<tr><td>Reuse hardware</td><td>Tanks, pumps, UV-C, backflow prevention</td><td>Local integrators</td><td>Sizing, anti-backflow class (EA/EB/AA)</td></tr>
<tr><td>Metering &amp; IoT</td><td>Flow, conductivity, energy</td><td>Endress+Hauser, Siemens, regional</td><td>SaaS data ingestion</td></tr>
<tr><td>Waste &amp; consumables</td><td>DASRI/DAOM</td><td>Veolia, Suez, regional</td><td>Sorting + reduction (Phase 3)</td></tr>
<tr><td>Future / pilot</td><td>NeoKidney, AWAK, REDY sorbent</td><td>NextKidney, AWAK, vendor R&amp;D</td><td>Watch &amp; pilot integration """+C('gem')+"""</td></tr>
</table>
<p style="margin-top:10px;font-size:12px;color:#56698a">Detailed supplier landscape with caveats &amp; partnership roles in Appendix A11.</p>
""",
"Supplier landscape compressed. Full detail in appendix.")

add("maturity","content","Technology maturity — ready now / site-specific / pilot only",
"""
<table>
<tr><th>Lever</th><th>Maturity</th><th>Water</th><th>Energy</th><th>Waste</th><th>Clinical risk</th><th>EcoDialysis phase</th></tr>
<tr><td>RO-reject → non-clinical reuse</td><td><span class="tag-ok">Ready</span></td><td>+++</td><td>0</td><td>+</td><td>None (boundary)</td><td>Phase 1</td></tr>
<tr><td>RO replacement (357 L vs 548 L)</td><td><span class="tag-ok">Ready</span></td><td>+++</td><td>+++</td><td>+</td><td>None</td><td>Phase 1</td></tr>
<tr><td>Disinfection optimization</td><td><span class="tag-ok">Ready</span></td><td>++</td><td>+</td><td>++</td><td>Vendor sign-off</td><td>Phase 1</td></tr>
<tr><td>Heat recovery (East Kent)</td><td><span class="tag-ok">Ready</span></td><td>0</td><td>++</td><td>0</td><td>None</td><td>Phase 2</td></tr>
<tr><td>Qd reduction (500→400 ml/min)</td><td><span class="tag-warn">Site-specific</span></td><td>++</td><td>+</td><td>+</td><td>Clinical sign-off</td><td>Phase 2</td></tr>
<tr><td>Centralized acid concentrate</td><td><span class="tag-warn">Site-specific</span></td><td>+</td><td>+</td><td>++</td><td>Low</td><td>Phase 2</td></tr>
<tr><td>Conductivity-routed reuse</td><td><span class="tag-warn">Site-specific</span></td><td>++</td><td>0</td><td>0</td><td>Engineering</td><td>Phase 1–2</td></tr>
<tr><td>Pretreatment recovery RO</td><td><span class="tag-warn">Site-specific</span></td><td>++</td><td>−</td><td>0</td><td>Vendor</td><td>Phase 2</td></tr>
<tr><td>HDF dialysate volume tuning</td><td><span class="tag-warn">Site-specific</span></td><td>+</td><td>0</td><td>0</td><td>Clinical sign-off</td><td>Phase 2</td></tr>
<tr><td>Sorbent / portable (REDY, AWAK)</td><td><span class="tag-bad">Pilot only</span></td><td>+++</td><td>+</td><td>+</td><td>High</td><td>Watch</td></tr>
<tr><td>NeoKidney wearable</td><td><span class="tag-bad">Pilot only</span></td><td>+++</td><td>+</td><td>+</td><td>High</td><td>Watch</td></tr>
<tr><td>Spent dialysate reuse</td><td><span class="tag-bad">Not deployable</span></td><td>n/a</td><td>n/a</td><td>n/a</td><td>Boundary</td><td>Never</td></tr>
</table>
<p style="margin-top:8px;font-size:12px;color:#56698a">Full 18-row matrix in Appendix A13. Sources: """+C('gem','ope','s26')+"""</p>
""",
"Maturity matrix is the credibility slide. Boundary at bottom.")

add("business","content","Business model — audit · playbook · SaaS · success · label",
"""
<div class="grid">
  <div>
    <h3>Five revenue lines</h3>
    <div class="card">
      <table>
        <tr><th>Line</th><th>Logic</th><th>Range</th></tr>
        <tr><td>Audit</td><td>Wedge, paid pilot</td><td>€8–18k</td></tr>
        <tr><td>Playbook + EICH dossier</td><td>Per site</td><td>€10–25k</td></tr>
        <tr><td>Implementation support</td><td>% of CAPEX</td><td>5–15 %</td></tr>
        <tr><td>SaaS monitoring</td><td>Recurring</td><td>€600–1,400 / mo</td></tr>
        <tr><td>Success fee</td><td>% of verified savings</td><td>10–20 % yr 1–3</td></tr>
        <tr><td>Label + benchmark</td><td>Annual</td><td>€3–8k / yr</td></tr>
      </table>
    </div>
    <p style="font-size:12px;color:#56698a;margin-top:6px">Pricing illustrative; calibrated on first pilots.</p>
  </div>
  <div>
    <h3>Channels &amp; expansion</h3>
    <div class="card accent"><ul>
      <li><b>Direct:</b> CHU sustainability office, biomedical engineering.</li>
      <li><b>GHT rollout:</b> one CH wins → cluster follows.</li>
      <li><b>Private networks:</b> AURA / Diaverum / NephroCare / Echo-style chains.</li>
      <li><b>Supplier partnerships:</b> RO &amp; generator vendors include EcoDialysis audit at sale.</li>
      <li><b>Subsidy partners:</b> Agences de l'Eau (basin-specific), CEE (verify category), ADEME.</li>
    </ul></div>
    <div class="card dark"><h3>Why this compounds</h3>
      <ul>
        <li>Audit data → benchmark database → defensibility.</li>
        <li>Playbook reuse → margin expansion.</li>
        <li>Label adoption → network effect among nephrology directors.</li>
      </ul>
    </div>
  </div>
</div>
""",
"Five revenue lines, four channels, three compounding forces.")

add("buyers","content","Buyer map — who signs, who pays, who scales",
"""
<table>
<tr><th>Buyer</th><th>Pain</th><th>Decision unit</th><th>Wedge</th><th>Expansion</th></tr>
<tr><td><b>CHU</b> · large public</td><td>Reporting + reputation + scarcity</td><td>Sustainability office + bioméd + direction</td><td>Audit + flagship pilot</td><td>Other departments (sterilization, laundry)</td></tr>
<tr><td><b>CH / GHT</b></td><td>Multi-site scarcity + opex</td><td>GHT direction + technique</td><td>One CH pilot → GHT framework</td><td>Cluster rollout</td></tr>
<tr><td><b>Private dialysis network</b></td><td>Margin compression + ESG mandates</td><td>Medical director + ops + finance</td><td>Network-wide audit deal</td><td>Cross-country rollout</td></tr>
<tr><td><b>Medium independent unit</b></td><td>Opex sensitivity</td><td>Owner-medical-director</td><td>Audit + light SaaS</td><td>Reference for similar units</td></tr>
<tr><td><b>New-build / renovation</b></td><td>Design-in window</td><td>Architect + bioméd + procurement</td><td>Ashford-style design-in</td><td>Architect partnerships</td></tr>
</table>
<p style="margin-top:10px;font-size:13px;color:#56698a">Reference market: ~2,965 health establishments · ~1,100–1,200 dialysis units · 51,700 patients · 77 % in-center/UDM. """+C('per')+"""</p>
""",
"Five buyer types, each with wedge + expansion.")

# =========== PART 5: PILOT & ASK ===========
add("div-ask","divider","Part 5 — Pilot, risk &amp; ask",
"""<p class="lead">Three pilots. Six months. A repeatable dossier engine for France.</p>""",
"Transition to pilot.")

add("pilots","content","Three-pilot plan — CHU · GHT · private network",
"""
<div class="grid3">
  <div class="card"><h3>Pilot A · CHU flagship</h3>
    <p><b>Target:</b> AP-HM / CHU Toulouse / CHU Lyon class.</p>
    <ul>
      <li>~150 patients</li>
      <li>Full reuse + heat recovery</li>
      <li>EICH dossier proof</li>
      <li>SFNDT publication path</li>
    </ul>
    <p><span class="pill">6 months</span> <span class="pill">€80–120k</span></p>
  </div>
  <div class="card accent"><h3>Pilot B · GHT mid-size</h3>
    <p><b>Target:</b> CH in water-stressed basin (Adour-Garonne / Loire).</p>
    <ul>
      <li>~80 patients</li>
      <li>Reuse + RO upgrade scoping</li>
      <li>GHT framework agreement</li>
      <li>Agence de l'Eau co-funding</li>
    </ul>
    <p><span class="pill">6 months</span> <span class="pill">€60–90k</span></p>
  </div>
  <div class="card dark"><h3>Pilot C · Private network</h3>
    <p><b>Target:</b> AURA / Diaverum / regional chain.</p>
    <ul>
      <li>3 sites, ~100 patients each</li>
      <li>Repeatable playbook test</li>
      <li>SaaS + label deployment</li>
      <li>Network-rollout option</li>
    </ul>
    <p style="color:#cfe1f7"><span class="pill" style="background:#1d4a8d;color:#fff">9 months</span> <span class="pill" style="background:#1d4a8d;color:#fff">€140–200k</span></p>
  </div>
</div>
<p style="margin-top:10px;font-size:13px;color:#56698a">All three together test: technical feasibility, dossier repeatability, and channel scalability.</p>
""",
"Three pilots = three different validations: feasibility, repeatability, scalability.")

add("need","content","What we need from each pilot hospital",
"""
<div class="grid">
  <div class="card"><h3>Access</h3>
    <ul>
      <li>Water plant &amp; RO room access</li>
      <li>Technical plans (water, drainage, electricity)</li>
      <li>Dialysis floor session schedule</li>
      <li>Non-clinical demand map (toilets, cleaning, HVAC, garden)</li>
      <li>Permission to install 4 meters</li>
    </ul>
  </div>
  <div class="card"><h3>Data</h3>
    <ul>
      <li>12 months water + sewer bills</li>
      <li>RO + generator inventory + age</li>
      <li>Energy bills for water-treatment area</li>
      <li>Session log (sessions/yr per machine)</li>
      <li>Existing maintenance &amp; disinfection logs</li>
    </ul>
  </div>
  <div class="card accent"><h3>People</h3>
    <ul>
      <li>Bioméd / services techniques referent</li>
      <li>Hygiene / CLIN referent</li>
      <li>Direction sponsor</li>
      <li>Medical referent (nephrology)</li>
      <li>ARS / préfecture pre-file contact</li>
    </ul>
  </div>
</div>
<p style="margin-top:10px;font-size:13px;color:#56698a">No clinical data. No patient data. The hospital remains the data controller and operational owner.</p>
""",
"Concrete asks. No clinical data needed.")

add("deliver","content","What we deliver in 30 days",
"""
<div class="grid">
  <div>
    <div class="card"><h3>Day 1 – 10 · Eco-audit</h3>
      <ul>
        <li>Site visit + interviews</li>
        <li>4-point meter install</li>
        <li>Bills + plans analysis</li>
        <li>RO + generator inventory</li>
      </ul>
    </div>
    <div class="card"><h3>Day 10 – 20 · Mapping</h3>
      <ul>
        <li>Green/orange/red reuse routes</li>
        <li>Demand profile vs reject profile</li>
        <li>Three reuse scenarios sized</li>
      </ul>
    </div>
  </div>
  <div>
    <div class="card"><h3>Day 20 – 25 · Scenario ROI</h3>
      <ul>
        <li>Low / central / high reject</li>
        <li>50 / 70 / 90 % capture</li>
        <li>Tariff + CAPEX sensitivity</li>
        <li>Subsidy stacking option</li>
      </ul>
    </div>
    <div class="card accent"><h3>Day 25 – 30 · Decision pack</h3>
      <ul>
        <li>Risk register</li>
        <li>EICH dossier draft</li>
        <li>Go / no-go recommendation</li>
        <li>Implementation timeline</li>
      </ul>
    </div>
  </div>
</div>
<p style="margin-top:10px;font-size:13px;color:#56698a">Output: A4 dossier + 1-page board memo + live SaaS dashboard baseline.</p>
""",
"30-day audit clock. Concrete deliverables.")

add("refuse","content","What we refuse to do",
"""
<div class="grid">
  <div>
    <h3>Boundaries we will not cross</h3>
    <ul class="xlist">
      <li>No patient-contact reuse, ever.</li>
      <li>No reuse fed back to dialysis-water production.</li>
      <li>No spent-dialysate reuse.</li>
      <li>No guarantee of ARS approval — every dossier is local.</li>
      <li>No unverified CNAM / tariff claim.</li>
      <li>No full carbon-neutrality claim — water adaptation first.</li>
      <li>No black-box calculation — methodology is published.</li>
      <li>No vendor lock-in recommendation without comparative evidence.</li>
    </ul>
  </div>
  <div>
    <div class="banner"><b>Trust is the wedge.</b><br/>What we refuse to do is the moat.</div>
    <div class="card"><h3>How this maps to claim control</h3>
      <ul>
        <li>Methodology box on every report.</li>
        <li>Objective, perimeter, assumptions, uncertainty. """+C('tsp')+"""</li>
        <li>Caveat language standardized.</li>
        <li>Forbidden-claim list maintained in Appendix A16.</li>
      </ul>
    </div>
  </div>
</div>
""",
"Refusal list is the trust moat. Maps to claim control.")

add("kpis","content","KPIs &amp; success criteria",
"""
<div class="grid4">
  <div class="kpi"><div class="v">≥ 50 %</div><div class="l">Reject capture rate</div><div class="s">Target after commissioning</div></div>
  <div class="kpi"><div class="v">≥ 70 %</div><div class="l">Substitution rate</div><div class="s">Non-clinical demand met</div></div>
  <div class="kpi"><div class="v">&lt; 6 yr</div><div class="l">Payback</div><div class="s">Saint-Exupéry benchmark</div></div>
  <div class="kpi"><div class="v">0</div><div class="l">Clinical incidents</div><div class="s">Boundary held</div></div>
</div>
<div class="grid" style="margin-top:14px">
  <div class="card"><h3>Operational KPIs</h3>
    <ul>
      <li>L/session reject — measured continuously.</li>
      <li>L/session substituted — measured at reuse meter.</li>
      <li>kWh/session — RO + dialysate loop.</li>
      <li>Disinfection chemical avoided.</li>
      <li>Conductivity excursions = 0.</li>
    </ul>
  </div>
  <div class="card accent"><h3>Dossier &amp; trust KPIs</h3>
    <ul>
      <li>Time-to-dossier (target ≤ 60 days).</li>
      <li>ARS approval rate.</li>
      <li>Carnet sanitaire compliance.</li>
      <li>Monthly verification on time.</li>
      <li>EcoDialysis-labelled centers count.</li>
    </ul>
  </div>
</div>
""",
"KPI set covers ops, dossier, trust.")

add("risk","content","Risk &amp; trust — what could go wrong, how we protect",
"""
<table>
<tr><th>Risk</th><th>Why it matters</th><th>Mitigation</th><th>Owner</th></tr>
<tr><td>ARS rejection / delay</td><td>No deployment without dossier</td><td>Pre-file early; templated EICH dossier</td><td>EcoDialysis + hospital direction</td></tr>
<tr><td>Biofilm / cross-connection</td><td>Patient &amp; staff safety</td><td>Separated network, anti-backflow (EA/EB/AA), monitoring, emergency stop</td><td>Bioméd + hygiène</td></tr>
<tr><td>Demand-supply mismatch</td><td>Empty reuse loop = no ROI</td><td>Pre-sizing storage + demand mapping</td><td>EcoDialysis</td></tr>
<tr><td>Tariff weakening ROI</td><td>Low water/sewer tariff = poor payback</td><td>Site triage; refuse low-ROI sites; subsidy stacking</td><td>EcoDialysis</td></tr>
<tr><td>Capex retrofit cost</td><td>Layout-dependent</td><td>Site triage; design-in for new-build (Ashford)</td><td>Hospital + EcoDialysis</td></tr>
<tr><td>Overclaiming ESG / carbon</td><td>Loss of trust</td><td>Methodology box; refusal list; published caveats</td><td>EcoDialysis</td></tr>
<tr><td>Patient / staff perception</td><td>Social licence</td><td>Communication kit + boundary clarity</td><td>Hospital direction + EcoDialysis</td></tr>
<tr><td>Supplier lock-in</td><td>Bias risk</td><td>Comparative evidence requirement, vendor-neutral specs</td><td>EcoDialysis</td></tr>
</table>
<p style="margin-top:8px;font-size:12px;color:#56698a">Full register with evidence sources in Appendix A14.</p>
""",
"Risk register, eight rows. Full register in appendix.")

add("defensibility","content","Defensibility — five compounding moats",
"""
<div class="grid5">
  <div class="card"><h3>Benchmark DB</h3><p>Every audit feeds a France-specific water/energy benchmark unavailable elsewhere.</p></div>
  <div class="card"><h3>Playbook library</h3><p>Repeatable EICH dossiers shorten each new project — margin compounds.</p></div>
  <div class="card"><h3>Source-labelled evidence</h3><p>Every claim chip-linked to a primary source — defensible vs consultants.</p></div>
  <div class="card"><h3>EcoDialysis label</h3><p>Network effect among nephrology directors and ARS reviewers.</p></div>
  <div class="card dark"><h3>Supplier scorecard</h3><p>Procurement leverage as we expand into devices and consumables.</p></div>
</div>
<div class="banner" style="margin-top:14px">EcoDialysis wins when every dialysis unit can say:<br/><b>we know our water · we know our safe reuse route · we can prove the savings.</b></div>
""",
"Five moats, one slogan.")

add("expansion","content","Future expansion — water first, then four more layers",
"""
<div class="flow">
  <div class="step">1 · Water</div><span class="arrow">›</span>
  <div class="step">2 · Energy</div><span class="arrow">›</span>
  <div class="step">3 · Consumables</div><span class="arrow">›</span>
  <div class="step">4 · Procurement scorecard</div><span class="arrow">›</span>
  <div class="step">5 · Label &amp; benchmark</div>
</div>
<div class="grid5" style="margin-top:14px">
  <div class="card"><h3>Water</h3><p>RO reject, heat recovery, Qd tuning, disinfection.</p></div>
  <div class="card"><h3>Energy</h3><p>RO replacement, heat exchangers, schedule optimization.</p></div>
  <div class="card"><h3>Consumables</h3><p>Acid concentrate centralization, dialyzer scorecard, packaging.</p></div>
  <div class="card"><h3>Procurement</h3><p>Supplier sustainability scoring with TSP / IDMD logic. """+C('tsp','ird')+"""</p></div>
  <div class="card dark"><h3>Label</h3><p>EcoDialysis as a recognized standard across nephrology in France &amp; EU.</p></div>
</div>
""",
"Five-phase expansion roadmap.")

add("close","cover","",
"""
<div class="eyebrow">EcoDialysis · Paris 2026</div>
<h1>Hospitals do not need<br/>another ESG dashboard.</h1>
<p class="lead">They need an operational water-resilience playbook.<br/>EcoDialysis builds it — site by site, dossier by dossier, certification by certification.</p>
<div style="margin-top:32px;display:flex;gap:24px;color:#cfe1f7;font-size:15px">
  <span>Three pilots · six months · one repeatable engine for France.</span>
</div>
<div style="margin-top:18px;font-size:13px;color:#9ec5ef;letter-spacing:1px">Adaptation first · mitigation second · boundary non-negotiable</div>
""",
"Close. Slogan. Ask.")


# =========== APPENDIX (A1 - A16) ===========
add("div-appendix","divider","Appendix — diligence evidence library",
"""<p class="lead">23 extracted sources · 0 extraction failures · all key facts traced to a primary document.</p>""",
"Appendix divider.")

add("apx-sources","appendix","A1 · Source map — 23 extracted sources, zero extraction failures",
"""
<table>
<tr><th>Chip</th><th>ID</th><th>Source</th><th>Type</th><th>Quality</th></tr>
<tr><td>Per</td><td>DR-France</td><td>EcoDialysis_Perplexity.pdf (+ .docx)</td><td>Deep-research strategy synthesis</td><td>Medium</td></tr>
<tr><td>Gem</td><td>DR-Tech</td><td>Clinical and Technical Advancements in Dialysis_Gemini.pdf (+ .docx)</td><td>Deep technical synthesis</td><td>Medium-high</td></tr>
<tr><td>Ope</td><td>DR-Water</td><td>Water Sustainability Practices in Dialysis_OpenAI.pdf</td><td>Deep-research synthesis</td><td>Medium-high</td></tr>
<tr><td>S23</td><td>SFNDT-2023</td><td>SFNDT_guide complet-VF-HD-2_260526.pdf</td><td>Professional society guidance</td><td>High</td></tr>
<tr><td>S26</td><td>SFNDT-2026-L</td><td>Guide_des_bonnes_pratiques_en_néphrologie_verte_Ve_260526.pdf</td><td>Professional society guidance (long)</td><td>High</td></tr>
<tr><td>S26</td><td>SFNDT-2026-S</td><td>Guide_de_la_néphrologie_verte_Version_courte_2026_260526.pdf</td><td>Professional society guidance (short)</td><td>High</td></tr>
<tr><td>Gov</td><td>Gov-Health-Roadmap</td><td>Planification écologique du système de santé.pdf</td><td>Government roadmap</td><td>High</td></tr>
<tr><td>TSP</td><td>TSP-Health</td><td>TSP-Decarbonons-les-industries-des-medicaments-RF.pdf</td><td>The Shift Project report</td><td>High</td></tr>
<tr><td>TSP</td><td>TSP-Pathway</td><td>[PPJS] Guide méthodologique pour l'évaluation carbone des parcours de soin.pdf</td><td>Methodological guide</td><td>High</td></tr>
<tr><td>TSP</td><td>TSP-Med</td><td>240404-Rapport-Decarbonons-lAutonomie-The-Shift-Project-1-1.pdf</td><td>Report</td><td>Medium-high</td></tr>
<tr><td>Ird</td><td>IRDES-Sustainability</td><td>IRDES · Soutenabilité environnementale des systèmes de santé.pdf</td><td>Literature review</td><td>High</td></tr>
<tr><td>HCW</td><td>HCWH</td><td>L'empreinte climatique du secteur de la santé Health Care Without Harm.pdf</td><td>NGO global analysis</td><td>Medium-high</td></tr>
<tr><td>HCW</td><td>Global-Green-Health</td><td>Green health how to decarbonise global healthcare systems.pdf</td><td>Global report</td><td>Medium-high</td></tr>
<tr><td>HCW</td><td>Climate-friendly-healthcare</td><td>Climate-friendly healthcare reducing the impacts of the healthcare sector.pdf</td><td>Global report</td><td>Medium</td></tr>
<tr><td>Pch</td><td>Pitch-v3</td><td>EcoDialysis_Pitch_v3.pptx + .pdf</td><td>Internal pitch</td><td>High (narrative)</td></tr>
<tr><td>Pch</td><td>Base-v1</td><td>EcoDialysis Pitch_v1.html</td><td>Internal HTML baseline</td><td>Internal style</td></tr>
<tr><td>—</td><td>Vendor-block</td><td>Official corporate / regulatory pages (Fresenius, B. Braun, Vantive/Baxter, Nipro, Nikkiso, Asahi Kasei, Toray, JMS, Quanta, NxStage, SNITEM/C2DS/AFNOR SPEC 2313)</td><td>Corporate &amp; regulatory</td><td>Medium-high to High</td></tr>
</table>
<p style="margin-top:8px;font-size:11px;color:#56698a">Reliability legend — High: official regulation, government, professional society. Medium-high: official corporate, peer-reviewed. Medium: secondary synthesis. Low: excluded.</p>
""",
"A1: full source registry.")

add("apx-chips","appendix","A2 · Source chip registry",
"""
<div class="grid5">
  <div class="card"><h3>Per</h3><p>France market &amp; GTM deep research (Perplexity).</p><a class="src" href="#src-per">Per</a></div>
  <div class="card"><h3>Gem</h3><p>Technology deep research (Gemini).</p><a class="src" href="#src-gem">Gem</a></div>
  <div class="card"><h3>Ope</h3><p>Water sustainability deep research (OpenAI).</p><a class="src" href="#src-ope">Ope</a></div>
  <div class="card"><h3>S23</h3><p>SFNDT 2023 green nephrology guide.</p><a class="src" href="#src-s23">S23</a></div>
  <div class="card"><h3>S26</h3><p>SFNDT 2026 long &amp; short guides.</p><a class="src" href="#src-s26">S26</a></div>
  <div class="card"><h3>Gov</h3><p>Planification écologique du système de santé.</p><a class="src" href="#src-gov">Gov</a></div>
  <div class="card"><h3>TSP</h3><p>The Shift Project (health, pathway, autonomy).</p><a class="src" href="#src-tsp">TSP</a></div>
  <div class="card"><h3>Ird</h3><p>IRDES literature review.</p><a class="src" href="#src-ird">Ird</a></div>
  <div class="card"><h3>HCW</h3><p>Health Care Without Harm + global green health.</p><a class="src" href="#src-hcw">HCW</a></div>
  <div class="card"><h3>Pch</h3><p>EcoDialysis pitch v1 / v3 baseline.</p><a class="src" href="#src-pch">Pch</a></div>
</div>
""",
"A2: chip registry.")

add("apx-dr-water","appendix","A3 · DR-Water insight table — 18 facts",
"""
<table>
<tr><th>#</th><th>Fact</th><th>Quantity</th></tr>
<tr><td>1</td><td>Canterbury RO-reject recovery</td><td>800 L/h</td></tr>
<tr><td>2</td><td>Canterbury annual savings</td><td>~£7,500/yr</td></tr>
<tr><td>3</td><td>Ashford design-in route</td><td>~£2,500</td></tr>
<tr><td>4</td><td>Bristol water saving</td><td>13,140 m³/yr</td></tr>
<tr><td>5</td><td>Bristol annual savings</td><td>&gt;£15,000/yr</td></tr>
<tr><td>6</td><td>East Kent heat exchangers</td><td>0.86 kWh/treatment</td></tr>
<tr><td>7</td><td>East Kent projected annual recovery</td><td>27,905 kWh/yr</td></tr>
<tr><td>8</td><td>ANZSN aggregated water saved</td><td>&gt;160,000 L/yr</td></tr>
<tr><td>9</td><td>ANZSN aggregated electricity saved</td><td>6.4 MWh/yr</td></tr>
<tr><td>10</td><td>ANZSN citric acid avoided</td><td>720 L</td></tr>
<tr><td>11</td><td>ANZSN product savings</td><td>~AU$2,400</td></tr>
<tr><td>12</td><td>Modern AU RO water per treatment</td><td>357 L (vs 548 L old)</td></tr>
<tr><td>13</td><td>Modern AU RO energy per treatment</td><td>3.1 kWh (vs 7.2 kWh old)</td></tr>
<tr><td>14</td><td>Spain 20-center mean</td><td>476.5 L/session</td></tr>
<tr><td>15</td><td>Spain daily-opening centers</td><td>430.20 L/HD · 10.82 kWh/HD</td></tr>
<tr><td>16</td><td>Spain 3×/week centers</td><td>629.81 L/HD · 16.79 kWh/HD</td></tr>
<tr><td>17</td><td>Named benchmarks</td><td>Bendigo · Barwon · Queen Elizabeth</td></tr>
<tr><td>18</td><td>Future / pilot track</td><td>REDY · NeoKidney · AWAK</td></tr>
</table>
<p style="margin-top:6px;font-size:11px;color:#56698a">Primary chip: """+C('ope')+""" (DR-Water). Cross-confirmed by """+C('gem')+""".</p>
""",
"A3: 18 DR-Water facts.")

add("apx-dr-france","appendix","A4 · DR-France insight table — 12 facts",
"""
<table>
<tr><th>#</th><th>Fact</th><th>Value</th></tr>
<tr><td>1</td><td>French dialysis patients</td><td>~51,700</td></tr>
<tr><td>2</td><td>In-center / UDM share</td><td>~77 %</td></tr>
<tr><td>3</td><td>Feedwater per session</td><td>~400–500 L</td></tr>
<tr><td>4</td><td>RO reject fraction</td><td>50–70 %</td></tr>
<tr><td>5</td><td>First adopters</td><td>CHU / CHRU + large private</td></tr>
<tr><td>6</td><td>Health establishments</td><td>~2,965 (context-dependent)</td></tr>
<tr><td>7</td><td>Dialysis units (est.)</td><td>~1,100–1,200</td></tr>
<tr><td>8</td><td>Reference center</td><td>100 patients</td></tr>
<tr><td>9</td><td>Sessions / patient / yr</td><td>156</td></tr>
<tr><td>10</td><td>Total sessions / yr</td><td>15,600</td></tr>
<tr><td>11</td><td>Reject / session assumption</td><td>270 L (low 220 · high 320)</td></tr>
<tr><td>12</td><td>Reference reject volume</td><td>~4,200 m³/yr · ~1.0–1.1 tCO₂e water-only caveat</td></tr>
</table>
<p style="margin-top:6px;font-size:11px;color:#56698a">Primary chip: """+C('per')+""". Carbon caveat aligned with """+C('tsp')+""" methodology.</p>
""",
"A4: 12 DR-France facts.")

add("apx-dr-tech","appendix","A5 · DR-Tech insight table — 15 facts",
"""
<table>
<tr><th>#</th><th>Fact</th></tr>
<tr><td>1</td><td>Taxonomy: reuse · RO optimization · disinfection · heat recovery</td></tr>
<tr><td>2</td><td>Supports 476.5 L/session multicenter benchmark</td></tr>
<tr><td>3</td><td>High-recovery RO architecture pathway</td></tr>
<tr><td>4</td><td>Conductivity-based routing logic for reuse decisions</td></tr>
<tr><td>5</td><td>Consolidates Canterbury / Ashford / Bristol evidence</td></tr>
<tr><td>6</td><td>Confirms ANZSN disinfection optimization logic</td></tr>
<tr><td>7</td><td>Heat-recovery cases (East Kent, Newcastle)</td></tr>
<tr><td>8</td><td>Distinguishes low-risk non-clinical vs higher-risk pathways</td></tr>
<tr><td>9</td><td>Sorbent / portable systems as emerging track</td></tr>
<tr><td>10</td><td>NeoKidney and AWAK pilot status</td></tr>
<tr><td>11</td><td>Retrofit cost and governance barriers identified</td></tr>
<tr><td>12</td><td>Recommends staged implementation roadmap</td></tr>
<tr><td>13</td><td>Reinforces metering and process controls</td></tr>
<tr><td>14</td><td>Positions spent dialysate reuse as not first-wave</td></tr>
<tr><td>15</td><td>Supports evidence-level stratification table</td></tr>
</table>
<p style="margin-top:6px;font-size:11px;color:#56698a">Primary chip: """+C('gem')+""". Reinforces maturity matrix in Appendix A13.</p>
""",
"A5: 15 DR-Tech facts.")

add("apx-s23","appendix","A6 · SFNDT 2023 — green nephrology framework",
"""
<table>
<tr><th>#</th><th>Insight</th></tr>
<tr><td>1</td><td>Structured green nephrology action framework</td></tr>
<tr><td>2</td><td>Water · energy · waste levers integrated</td></tr>
<tr><td>3</td><td>Governance and team-level ownership emphasized</td></tr>
<tr><td>4</td><td>Training and implementation culture central</td></tr>
<tr><td>5</td><td>Procurement and life-cycle orientation</td></tr>
<tr><td>6</td><td>Risk-aware operational transition framing</td></tr>
<tr><td>7</td><td>Dialysis footprint reduction hierarchy</td></tr>
<tr><td>8</td><td>Measurement-first logic (matches EcoDialysis architecture)</td></tr>
<tr><td>9</td><td>Continuous improvement approach</td></tr>
<tr><td>10</td><td>Quality-and-safety co-framing of sustainability</td></tr>
<tr><td>11</td><td>Multi-domain indicator tracking</td></tr>
<tr><td>12</td><td>Basis for actionable checklists</td></tr>
</table>
<p style="margin-top:6px;font-size:11px;color:#56698a">Primary chip: """+C('s23')+""". Clinical credibility anchor.</p>
""",
"A6: SFNDT 2023.")

add("apx-s26","appendix","A7 · SFNDT 2026 long guide — 20 operational facts",
"""
<table>
<tr><th>#</th><th>Fact</th><th>Quantity if any</th></tr>
<tr><td>1</td><td>Detailed action sheets for dialysis &amp; nephrology operations</td><td>—</td></tr>
<tr><td>2</td><td>Qd reduction pathway with quantified per-session savings</td><td>see #3, #4</td></tr>
<tr><td>3</td><td>Dialysate savings from 500→400 ml/min framing</td><td><b>~24 L/session</b></td></tr>
<tr><td>4</td><td>Pretreated water economy in the same context</td><td><b>~60–100 L/session</b></td></tr>
<tr><td>5</td><td>Multicenter French Qd evaluation context</td><td>—</td></tr>
<tr><td>6</td><td>HDF optimization &amp; dialysate volume tradeoffs</td><td>—</td></tr>
<tr><td>7</td><td>Centralized acid-concentrate distribution</td><td>waste + consumption ↓</td></tr>
<tr><td>8</td><td>Dedicated section on RO-reject reuse</td><td>—</td></tr>
<tr><td>9</td><td>French case: Clinique Saint-Exupéry Toulouse</td><td>—</td></tr>
<tr><td>10</td><td>Saint-Exupéry reported saving</td><td><b>~1,128 m³/yr</b></td></tr>
<tr><td>11</td><td>Saint-Exupéry investment / payback</td><td><b>~€30k · 5–6 yr</b></td></tr>
<tr><td>12</td><td>AP-HM Marseille larger-reuse-potential studies</td><td>—</td></tr>
<tr><td>13</td><td>Practical storage constraints (duration, temp, distance)</td><td>—</td></tr>
<tr><td>14</td><td>Separate-network requirements</td><td>—</td></tr>
<tr><td>15</td><td>No direct leap to high-risk reuse</td><td>boundary</td></tr>
<tr><td>16</td><td>Energy management obligations</td><td>—</td></tr>
<tr><td>17</td><td>Waste reduction pathways</td><td>—</td></tr>
<tr><td>18</td><td>Staff / organizational actions</td><td>—</td></tr>
<tr><td>19</td><td>RSE and communication logic</td><td>—</td></tr>
<tr><td>20</td><td>Reusable as implementation playbook</td><td>—</td></tr>
</table>
<p style="margin-top:6px;font-size:11px;color:#56698a">Primary chip: """+C('s26')+""". The closest match to EcoDialysis operational playbook.</p>
""",
"A7: SFNDT 2026 long, 20 facts.")

add("apx-gov","appendix","A8 · Government / regulation appendix — EICH &amp; Décret 2024-796",
"""
<div class="grid">
  <div>
    <h3>Décret n°2024-796 · in force 1 Sept 2024</h3>
    <div class="card"><ul>
      <li>EICH framework = Eaux Impropres à la Consommation Humaine.</li>
      <li>Covers sensitive establishments including healthcare.</li>
      <li>Authorizes non-clinical reuse subject to ARS / préfecture file.</li>
      <li>Mandatory separated network.</li>
      <li>Anti-backflow devices required.</li>
      <li>Signage program required.</li>
      <li>Carnet sanitaire entries required.</li>
      <li>Monitoring &amp; maintenance plan required.</li>
      <li>Emergency stop to potable fallback required.</li>
      <li>No patient-contact reuse permitted.</li>
    </ul></div>
  </div>
  <div>
    <h3>Stakeholder map</h3>
    <div class="card accent"><ul>
      <li><b>ARS</b> — health authority sign-off.</li>
      <li><b>Préfecture</b> — administrative authorization where required.</li>
      <li><b>Agence de l'Eau</b> — co-funding by basin.</li>
      <li><b>CLIN / hygiène</b> — internal safety committee.</li>
      <li><b>Direction</b> — administrative sponsor.</li>
      <li><b>Services techniques + bioméd</b> — operational owners.</li>
      <li><b>Médical + nephrology</b> — clinical sign-off.</li>
    </ul></div>
    <p style="font-size:11px;color:#56698a">Remaining uncertainties (carried into Appendix A16): exact ARS pathway per basin · monitoring frequency · tariff structure interaction · Agence de l'Eau eligibility · CEE category. Sources: """+C('gov','s26')+"""</p>
  </div>
</div>
""",
"A8: EICH stakeholder map.")

add("apx-decarb","appendix","A9 · Health-system decarbonization context — why water is adaptation first",
"""
<div class="grid">
  <div class="card"><h3>Macro context</h3>
    <ul>
      <li>Healthcare &gt; 8 % of national GHG footprint. """+C('gov','hcw')+"""</li>
      <li>~50 MtCO₂e order of magnitude.</li>
      <li>Offer of care ~45 % · medicines &amp; medical products ~55 %.</li>
      <li>Scope 3 procurement dominates.</li>
    </ul>
  </div>
  <div class="card"><h3>Health-system roadmap axes</h3>
    <ul>
      <li>Buildings &amp; energy</li>
      <li>Industries / products</li>
      <li>Sustainable procurement</li>
      <li>Eco-responsible care</li>
      <li>Waste · transport · digital · training</li>
    </ul>
    <p style="font-size:11px;color:#56698a">Source: """+C('gov')+""" Planification écologique.</p>
  </div>
  <div class="card accent"><h3>Why water is adaptation first</h3>
    <ul>
      <li>Water resilience is a continuity issue, not an ESG metric.</li>
      <li>Tariff &amp; scarcity hit opex immediately.</li>
      <li>Carbon weight of water is real but secondary (1.0–1.1 tCO₂e on 4,200 m³). """+C('per','tsp')+"""</li>
      <li>Medical devices &amp; consumables matter for Scope 3 — addressed in EcoDialysis Phase 3.</li>
      <li>System-level resilience framing aligns with TSP &amp; IRDES. """+C('tsp','ird')+"""</li>
    </ul>
  </div>
</div>
""",
"A9: macro framing.")

add("apx-equip","appendix","A10 · Equipment ecosystem — environmental, data, intervention, boundary",
"""
<table>
<tr><th>Layer</th><th>Environmental issue</th><th>Data needed</th><th>Intervention</th><th>Boundary</th><th>Owner</th></tr>
<tr><td>Dialysis generator</td><td>Energy + water tuning</td><td>Sessions/machine, Qd settings</td><td>Qd reduction, HDF tuning</td><td>Clinical sign-off</td><td>Bioméd + nephro</td></tr>
<tr><td>Water-treatment plant</td><td>Reject volume</td><td>Mains-in, permeate, reject flows</td><td>Modern RO, conductivity routing</td><td>Vendor sign-off</td><td>Services techniques</td></tr>
<tr><td>RO skid</td><td>L+kWh / treatment</td><td>Age, model, performance</td><td>Replacement / retrofit</td><td>Vendor</td><td>Bioméd</td></tr>
<tr><td>Pretreatment</td><td>Chemical use, backwash</td><td>Filter change cycles</td><td>Optimization, recovery RO</td><td>Vendor</td><td>Bioméd</td></tr>
<tr><td>Dialysate loop</td><td>Disinfection cycles</td><td>Citric / heat frequency</td><td>Optimization, chemical reduction</td><td>Vendor sign-off</td><td>Bioméd + hygiène</td></tr>
<tr><td>Dialyzer membranes</td><td>Single-use waste</td><td>Vendor scorecard</td><td>Procurement scoring (Phase 3)</td><td>Clinical</td><td>Direction + médical</td></tr>
<tr><td>Bloodlines / needles / catheters</td><td>Single-use waste</td><td>Volume + supplier</td><td>Packaging + procurement</td><td>Clinical</td><td>Pharma + procurement</td></tr>
<tr><td>Acid concentrate</td><td>Logistics + packaging</td><td>Local vs central feed</td><td>Centralized distribution """+C('s26')+"""</td><td>Hygiène</td><td>Services techniques</td></tr>
<tr><td>Bicarbonate</td><td>Cartridge waste</td><td>Consumption / session</td><td>Procurement scorecard</td><td>Clinical</td><td>Pharma</td></tr>
<tr><td>Saline / disinfectants</td><td>Chemicals</td><td>Volumes</td><td>Optimization</td><td>Hygiène</td><td>Pharma + hygiène</td></tr>
<tr><td>Packaging</td><td>Cardboard / plastic</td><td>Supplier audit</td><td>Procurement scorecard</td><td>Logistics</td><td>Procurement</td></tr>
<tr><td>DASRI / DAOM waste</td><td>High-carbon waste stream</td><td>Sort rates</td><td>Sorting + reduction """+C('ird')+"""</td><td>Hygiène</td><td>Services généraux</td></tr>
<tr><td>Sensors / meters</td><td>—</td><td>Existing inventory</td><td>4-point install</td><td>—</td><td>EcoDialysis</td></tr>
<tr><td>Tanks / pumps</td><td>Reuse hardware</td><td>Demand profile</td><td>Sizing</td><td>Engineering</td><td>Integrator</td></tr>
<tr><td>UV-C</td><td>Reuse polishing</td><td>Flow + microbio</td><td>Inline reuse loop</td><td>Vendor</td><td>Integrator</td></tr>
<tr><td>Backflow prevention</td><td>Cross-connection risk</td><td>Network plan</td><td>EA/EB/AA per use</td><td>Regulatory</td><td>Plumbing + hygiène</td></tr>
</table>
""",
"A10: equipment ecosystem table.")

add("apx-supp","appendix","A11 · Supplier landscape (verify local relevance)",
"""
<table>
<tr><th>Company</th><th>Category</th><th>Relevant products</th><th>EcoDialysis lever</th><th>Caveat</th></tr>
<tr><td>Fresenius Medical Care</td><td>Generator + RO + dialyzer</td><td>5008/6008, AquaA/AquaB, dialyzers, NxStage</td><td>Modern RO, generator tuning, procurement</td><td>Vendor neutrality required</td></tr>
<tr><td>B. Braun</td><td>Generator + water</td><td>Dialog, AQUAboss</td><td>Water plant, reject reuse</td><td>—</td></tr>
<tr><td>Baxter / Vantive</td><td>Generator + PD</td><td>Artis, AK series; PD</td><td>Generator tuning</td><td>Recent spin-off</td></tr>
<tr><td>Nipro</td><td>Generator + dialyzer</td><td>Surdial, dialyzers</td><td>Procurement scorecard</td><td>EU footprint variable</td></tr>
<tr><td>Nikkiso</td><td>Generator</td><td>DBB-EXA, water systems</td><td>Generator tuning</td><td>—</td></tr>
<tr><td>Asahi Kasei Medical</td><td>Dialyzer</td><td>Membranes</td><td>Procurement</td><td>—</td></tr>
<tr><td>Toray</td><td>Dialyzer</td><td>Membranes</td><td>Procurement</td><td>—</td></tr>
<tr><td>JMS</td><td>Dialyzer + bloodlines</td><td>Products</td><td>Procurement</td><td>Regional footprint</td></tr>
<tr><td>Quanta</td><td>Generator</td><td>SC+ portable</td><td>New low-water entrant</td><td>Pilot scale</td></tr>
<tr><td>Outset / Tablo</td><td>Generator</td><td>Tablo</td><td>Water-light alternative</td><td>US-focused</td></tr>
<tr><td>NextKidney (NeoKidney)</td><td>Future</td><td>Wearable</td><td>Watch &amp; pilot</td><td>Pre-deployment</td></tr>
<tr><td>AWAK</td><td>Future</td><td>Sorbent</td><td>Watch &amp; pilot</td><td>Pre-deployment</td></tr>
<tr><td>Endress+Hauser / Siemens</td><td>Metering / IoT</td><td>Flow, conductivity</td><td>SaaS data layer</td><td>—</td></tr>
<tr><td>Veolia / Suez</td><td>Water &amp; waste</td><td>Operator</td><td>Reuse hardware, waste audit</td><td>Bias risk → vendor neutrality</td></tr>
<tr><td>SNITEM / C2DS / AFNOR SPEC 2313</td><td>Procurement framework</td><td>IDMD</td><td>Scorecard alignment</td><td>—</td></tr>
</table>
<p style="margin-top:6px;font-size:11px;color:#56698a">Sources: official corporate pages + vendor landscape evidence block (see A1).</p>
""",
"A11: supplier landscape.")

add("apx-fin","appendix","A12 · Financial model — scenarios &amp; sensitivities",
"""
<div class="grid">
  <div>
    <h3>Reject scenario × capture rate</h3>
    <table>
      <tr><th>Reject</th><th>m³/yr</th><th>50 % capture</th><th>70 %</th><th>90 %</th></tr>
      <tr><td>Low 220 L</td><td>3,432</td><td>1,716</td><td>2,402</td><td>3,089</td></tr>
      <tr><td>Central 270 L</td><td>4,212</td><td>2,106</td><td>2,948</td><td>3,791</td></tr>
      <tr><td>High 320 L</td><td>4,992</td><td>2,496</td><td>3,494</td><td>4,493</td></tr>
    </table>
    <p style="font-size:11px;color:#56698a">All figures m³/yr for the reference 100-patient center. """+C('per')+"""</p>
  </div>
  <div>
    <h3>Tariff &amp; payback sensitivity</h3>
    <table>
      <tr><th>Water + sewer €/m³</th><th>Savings at 2,948 m³ reuse</th><th>Indicative payback @ €30k</th></tr>
      <tr><td>2.50</td><td>~€7,400/yr</td><td>~4 yr</td></tr>
      <tr><td>3.50</td><td>~€10,300/yr</td><td>~3 yr</td></tr>
      <tr><td>5.00</td><td>~€14,700/yr</td><td>~2 yr</td></tr>
    </table>
    <p style="font-size:11px;color:#56698a">Saint-Exupéry anchor: ~1,128 m³, ~€30k, 5–6 yr payback. """+C('s26')+"""</p>
  </div>
</div>
<div class="grid" style="margin-top:12px">
  <div class="card"><h3>What cannot be quantified yet</h3>
    <ul>
      <li>Exact CEE category and €/MWh equivalence for water reuse.</li>
      <li>Agence de l'Eau co-funding per basin and project.</li>
      <li>CNAM tariff impact (none assumed — caveat required).</li>
      <li>Carbon credit eligibility (not claimed).</li>
    </ul>
  </div>
  <div class="card accent"><h3>Decision rule</h3>
    <ul>
      <li>Refuse sites with tariff &lt; €1.80/m³ unless subsidy or scarcity-risk override.</li>
      <li>Prefer design-in over retrofit when window exists (Ashford pattern).</li>
      <li>Couple reuse with RO replacement when RO &gt; 10 yr.</li>
    </ul>
  </div>
</div>
""",
"A12: financials, sensitivities, decision rule.")

add("apx-mat","appendix","A13 · Technology maturity full matrix",
"""
<table>
<tr><th>Lever</th><th>Maturity</th><th>Evidence</th><th>Water</th><th>Energy</th><th>Waste</th><th>Capex</th><th>Reg</th><th>Phase</th></tr>
<tr><td>RO-reject non-clinical reuse</td><td><span class="tag-ok">Ready</span></td><td>UK + AU + ES</td><td>+++</td><td>0</td><td>+</td><td>Med</td><td>EICH dossier</td><td>1</td></tr>
<tr><td>Modern RO replacement</td><td><span class="tag-ok">Ready</span></td><td>AU measured</td><td>+++</td><td>+++</td><td>+</td><td>High</td><td>Vendor</td><td>1</td></tr>
<tr><td>Heat recovery (exchangers)</td><td><span class="tag-ok">Ready</span></td><td>East Kent</td><td>0</td><td>++</td><td>0</td><td>Med</td><td>Eng</td><td>2</td></tr>
<tr><td>Disinfection optimization</td><td><span class="tag-ok">Ready</span></td><td>ANZSN</td><td>++</td><td>+</td><td>++</td><td>Low</td><td>Vendor</td><td>1</td></tr>
<tr><td>Conductivity-routed reuse</td><td><span class="tag-warn">Site</span></td><td>Tech synthesis</td><td>++</td><td>0</td><td>0</td><td>Low</td><td>Eng</td><td>1–2</td></tr>
<tr><td>Pretreatment recovery RO</td><td><span class="tag-warn">Site</span></td><td>Tech synthesis</td><td>++</td><td>−</td><td>0</td><td>Med</td><td>Vendor</td><td>2</td></tr>
<tr><td>Qd reduction (500→400)</td><td><span class="tag-warn">Site</span></td><td>SFNDT 2026</td><td>++</td><td>+</td><td>+</td><td>Low</td><td>Clinical</td><td>2</td></tr>
<tr><td>HDF dialysate volume tuning</td><td><span class="tag-warn">Site</span></td><td>SFNDT 2026</td><td>+</td><td>0</td><td>0</td><td>Low</td><td>Clinical</td><td>2</td></tr>
<tr><td>Centralized acid concentrate</td><td><span class="tag-warn">Site</span></td><td>SFNDT 2026</td><td>+</td><td>+</td><td>++</td><td>Med</td><td>Hygiène</td><td>2</td></tr>
<tr><td>Schedule shape (daily vs 3×/wk)</td><td><span class="tag-warn">Site</span></td><td>Spain</td><td>+++</td><td>+++</td><td>0</td><td>Low</td><td>Clinical</td><td>2</td></tr>
<tr><td>Toilet flushing reuse</td><td><span class="tag-ok">Ready</span></td><td>UK</td><td>++</td><td>0</td><td>0</td><td>Low</td><td>EICH</td><td>1</td></tr>
<tr><td>Cleaning &amp; outdoor reuse</td><td><span class="tag-ok">Ready</span></td><td>UK</td><td>+</td><td>0</td><td>0</td><td>Low</td><td>EICH</td><td>1</td></tr>
<tr><td>HVAC cooling-tower make-up</td><td><span class="tag-warn">Site</span></td><td>Industry</td><td>++</td><td>0</td><td>0</td><td>Med</td><td>Eng</td><td>2</td></tr>
<tr><td>Laundry pre-wash reuse</td><td><span class="tag-warn">Site</span></td><td>Cross-sector</td><td>++</td><td>0</td><td>0</td><td>Med</td><td>EICH</td><td>2</td></tr>
<tr><td>Sterilization feed (non-final)</td><td><span class="tag-warn">Site</span></td><td>Cross-sector</td><td>+</td><td>0</td><td>0</td><td>Med</td><td>EICH + hygiène</td><td>2</td></tr>
<tr><td>Sorbent / portable (REDY/AWAK)</td><td><span class="tag-bad">Pilot</span></td><td>Vendor R&amp;D</td><td>+++</td><td>+</td><td>+</td><td>—</td><td>High</td><td>Watch</td></tr>
<tr><td>NeoKidney wearable</td><td><span class="tag-bad">Pilot</span></td><td>Vendor R&amp;D</td><td>+++</td><td>+</td><td>+</td><td>—</td><td>High</td><td>Watch</td></tr>
<tr><td>Spent dialysate reuse</td><td><span class="tag-bad">Boundary</span></td><td>—</td><td>n/a</td><td>n/a</td><td>n/a</td><td>—</td><td>Forbidden</td><td>Never</td></tr>
</table>
""",
"A13: full 18-row maturity matrix.")

add("apx-risk","appendix","A14 · Risk register",
"""
<table>
<tr><th>Risk</th><th>Why</th><th>Mitigation</th><th>Owner</th><th>Evidence</th></tr>
<tr><td>ARS rejection / delay</td><td>No reuse without dossier</td><td>Pre-file, templated EICH dossier, prior-art casework</td><td>EcoDialysis + direction</td><td>"""+C('gov','s26')+"""</td></tr>
<tr><td>Biofilm / infection</td><td>Patient safety</td><td>UV-C polishing, anti-stagnation, monitoring</td><td>Bioméd + hygiène</td><td>"""+C('s26','gem')+"""</td></tr>
<tr><td>Cross-connection</td><td>Potable contamination</td><td>Separated network, EA/EB/AA backflow, signage</td><td>Plumbing + hygiène</td><td>"""+C('gov')+"""</td></tr>
<tr><td>Conductivity excursion</td><td>Reuse quality drift</td><td>Inline routing to drain</td><td>Bioméd</td><td>"""+C('gem')+"""</td></tr>
<tr><td>Demand-supply mismatch</td><td>Empty reuse loop</td><td>Storage sizing, demand mapping</td><td>EcoDialysis</td><td>"""+C('s26','ope')+"""</td></tr>
<tr><td>Retrofit capex blow-out</td><td>ROI risk</td><td>Site triage, design-in option (Ashford)</td><td>Direction + EcoDialysis</td><td>"""+C('ope')+"""</td></tr>
<tr><td>Low tariff weakens ROI</td><td>Payback &gt; 7 yr</td><td>Site triage, subsidy stacking</td><td>EcoDialysis</td><td>"""+C('per')+"""</td></tr>
<tr><td>Procurement delays</td><td>Months added</td><td>Framework agreements, GHT route</td><td>Direction</td><td>—</td></tr>
<tr><td>Overclaiming ESG / carbon</td><td>Reputational</td><td>Methodology box, claim-control list</td><td>EcoDialysis</td><td>"""+C('tsp')+"""</td></tr>
<tr><td>Patient / staff perception</td><td>Social licence</td><td>Communication kit, boundary clarity</td><td>Direction</td><td>"""+C('s26')+"""</td></tr>
<tr><td>Ownership split</td><td>Operational drift</td><td>RACI per site, contracts</td><td>EcoDialysis</td><td>—</td></tr>
<tr><td>Supplier lock-in</td><td>Bias risk</td><td>Vendor-neutral specs, comparative evidence</td><td>EcoDialysis</td><td>"""+C('tsp')+"""</td></tr>
</table>
""",
"A14: risk register.")

add("apx-pilot","appendix","A15 · Pilot implementation appendix — week-by-week",
"""
<table>
<tr><th>Week</th><th>Phase</th><th>Deliverables</th><th>Hospital data needed</th><th>Approvals</th></tr>
<tr><td>0</td><td>Mobilization</td><td>Kick-off, NDA, sponsor letter</td><td>Org chart, contacts</td><td>Direction sign-off</td></tr>
<tr><td>1–2</td><td>Site audit</td><td>Visit, plans review, RO inventory</td><td>Plans, RO logs, 12-mo bills</td><td>Services techniques</td></tr>
<tr><td>2–3</td><td>Metering install</td><td>4 meters + conductivity</td><td>Plumbing access</td><td>Bioméd + hygiène</td></tr>
<tr><td>3–7</td><td>Baseline</td><td>Continuous logging, demand mapping</td><td>Session schedule</td><td>—</td></tr>
<tr><td>7–9</td><td>Scenario design</td><td>Green/orange/red map, sizing, ROI</td><td>Tariffs</td><td>Direction + technique</td></tr>
<tr><td>9–12</td><td>Dossier draft</td><td>EICH file, risk analysis, sign-off chain</td><td>—</td><td>Hygiène + direction</td></tr>
<tr><td>12–14</td><td>Pre-file ARS</td><td>Informal review</td><td>—</td><td>ARS</td></tr>
<tr><td>14–18</td><td>Implementation</td><td>Plumbing, tank, UV-C, backflow, SaaS</td><td>Site access</td><td>CLIN, ARS final</td></tr>
<tr><td>18–20</td><td>Commissioning</td><td>Testing, training, signage</td><td>Staff time</td><td>Bioméd + hygiène</td></tr>
<tr><td>20–24</td><td>Verification</td><td>Monthly reports, KPI bundle</td><td>—</td><td>Direction + finance</td></tr>
</table>
<p style="margin-top:6px;font-size:11px;color:#56698a">RACI matrix and reporting templates available in playbook pack.</p>
""",
"A15: implementation calendar.")

add("apx-claims","appendix","A16 · Claim control — allowed vs forbidden",
"""
<div class="grid">
  <div>
    <h3>Allowed claims</h3>
    <ul class="checklist">
      <li>"Captured X m³ of RO reject this month (M3 meter)."</li>
      <li>"Substituted Y m³ in non-clinical uses (M4 meter)."</li>
      <li>"Saved €Z based on local tariff bill verification."</li>
      <li>"Reduced disinfection cycles by N — chemicals avoided."</li>
      <li>"EICH-compliant dossier filed at ARS [date]."</li>
      <li>"Carnet sanitaire updated; zero conductivity excursions."</li>
      <li>"Energy savings X kWh from RO replacement (measured)."</li>
    </ul>
  </div>
  <div>
    <h3>Forbidden claims</h3>
    <ul class="xlist">
      <li>"Carbon neutral" — never.</li>
      <li>"Zero impact" — never.</li>
      <li>"ARS-approved at every site" — local decision.</li>
      <li>"Patient water reused" — never.</li>
      <li>"Spent dialysate recycled" — never.</li>
      <li>"Equivalent to X cars off the road" without TSP methodology disclosure.</li>
      <li>"Eligible for CEE / Agence de l'Eau" without written confirmation.</li>
      <li>"Saves the hospital N €" without verified bill comparison.</li>
    </ul>
  </div>
</div>
<p style="margin-top:8px;font-size:11px;color:#56698a">Methodology box mandatory on every report: objective, perimeter, assumptions, uncertainty, data quality, caveats. """+C('tsp')+"""</p>
""",
"A16: claim control.")

# Source anchors (Appendix I)
add("apx-sources-registry","appendix","Appendix I · Full source registry (chip anchors)",
"""
<div class="cols2" style="height:780px">
  <p id="src-per"><a class="src">Per</a> <b>DR-France · Perplexity</b><br/>EcoDialysis_Perplexity.pdf (+ .docx) — France market, ~51,700 patients, 77% in-center/UDM, reference-center model. Quality: Medium (secondary synthesis).</p>
  <p id="src-gem"><a class="src">Gem</a> <b>DR-Tech · Gemini</b><br/>Clinical and Technical Advancements in Dialysis_Gemini.pdf (+ .docx) — technology taxonomy, conductivity routing, maturity matrix support. Quality: Medium-high.</p>
  <p id="src-ope"><a class="src">Ope</a> <b>DR-Water · OpenAI</b><br/>Water Sustainability Practices in Dialysis_OpenAI.pdf — Canterbury, Bristol, Ashford, East Kent, ANZSN, modern vs old AU RO, Spain 20-center. Quality: Medium-high.</p>
  <p id="src-s23"><a class="src">S23</a> <b>SFNDT 2023</b><br/>SFNDT_guide complet-VF-HD-2_260526.pdf — green nephrology framework, measurement-first, governance. Quality: High.</p>
  <p id="src-s26"><a class="src">S26</a> <b>SFNDT 2026</b><br/>Guide_des_bonnes_pratiques_en_néphrologie_verte_Ve_260526.pdf + Guide_de_la_néphrologie_verte_Version_courte_2026_260526.pdf — Qd savings, Saint-Exupéry case, AP-HM, RO-reject reuse playbook. Quality: High.</p>
  <p id="src-gov"><a class="src">Gov</a> <b>Government / regulation</b><br/>Planification écologique du système de santé.pdf + Décret n°2024-796 (12 July 2024, in force 1 Sept 2024, EICH). Quality: High.</p>
  <p id="src-tsp"><a class="src">TSP</a> <b>The Shift Project</b><br/>TSP-Decarbonons-les-industries-des-medicaments-RF.pdf · [PPJS] Guide méthodologique pour l'évaluation carbone des parcours de soin.pdf · 240404-Rapport-Decarbonons-lAutonomie-The-Shift-Project-1-1.pdf. Quality: High.</p>
  <p id="src-ird"><a class="src">Ird</a> <b>IRDES</b><br/>La soutenabilité environnementale des systèmes de santé. Une revue de littérature sur l'empreinte écologique des systèmes de santé. Quality: High.</p>
  <p id="src-hcw"><a class="src">HCW</a> <b>Health Care Without Harm + Global Green Health</b><br/>L'empreinte climatique du secteur de la santé Health Care Without Harm.pdf + Green health how to decarbonise global healthcare systems.pdf + Climate-friendly healthcare reducing the impacts of the healthcare sector on the world's climate.pdf. Quality: Medium-high.</p>
  <p id="src-pch"><a class="src">Pch</a> <b>Pitch baseline</b><br/>EcoDialysis_Pitch_v3.pptx + EcoDialysis-Pitch_v3.pdf + EcoDialysis Pitch_v1.html — internal narrative, positioning, GTM skeleton. Quality: High (narrative), internal style baseline.</p>
</div>
""",
"Source anchors live here.")

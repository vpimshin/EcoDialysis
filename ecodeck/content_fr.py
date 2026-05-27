def C(*ids):
    labels={'per':'Per','gem':'Gem','ope':'Ope','s23':'S23','s26':'S26','gov':'Gov','tsp':'TSP','ird':'Ird','hcw':'HCW','pch':'Pch'}
    return ' '.join(f'<a class="src" href="#src-{i}">{labels[i]}</a>' for i in ids)

SLIDES_FR = []
def add(sid, kind, title, body, notes=""):
    SLIDES_FR.append((sid, kind, title, body, notes))

# PART 1
add("title","cover","",
"""
<div class="eyebrow">ANDCS × MIT Hacking Medicine · Sustainable Care · Paris 2026</div>
<h1>La dialyse a une<br/>vulnérabilité hydrique cachée.</h1>
<p class="lead">EcoDialysis transforme l'eau de dialyse gaspillée en un actif<br/>de résilience géré — mesuré, redessiné, certifié.</p>
<div style="margin-top:32px;display:flex;gap:32px;color:#cfe1f7;font-size:14px;letter-spacing:1.5px">
  <span><b style="color:var(--blue2)">270 L</b> rejetés / séance</span>
  <span><b style="color:var(--blue2)">15 600</b> séances / an / centre</span>
  <span><b style="color:var(--blue2)">~4 200 m³</b> gaspillés / an / centre</span>
</div>
""", "Ouverture sur la vulnérabilité hydrique cachée. Adaptation d'abord, atténuation ensuite.")

add("agenda","content","Agenda stratégique — du gaspillage caché à la résilience hydrique certifiée",
"""
<p class="lead">Six mouvements. Chacun est aussi une ligne de revenus EcoDialysis.</p>
<div class="grid3">
  <div class="card"><h3>1 · Voir le problème</h3><p>Rendre visible le flux d'eau caché de la dialyse à l'échelle de la séance.</p></div>
  <div class="card"><h3>2 · Choisir la bonne réutilisation</h3><p>Carte vert / orange / rouge de chaque voie de réutilisation non clinique.</p></div>
  <div class="card"><h3>3 · Monter le dossier</h3><p>Dossier de sécurité ARS / préfecture conforme EICH par site.</p></div>
  <div class="card"><h3>4 · Mettre en œuvre &amp; mesurer</h3><p>Métrologie 4 points, réseau séparé, prévention des interconnexions, carnet sanitaire.</p></div>
  <div class="card"><h3>5 · Vérifier les économies</h3><p>Tableau de bord SaaS, vérification mensuelle, preuves KPI pour ARS et direction financière.</p></div>
  <div class="card"><h3>6 · Certifier &amp; déployer</h3><p>Label EcoDialysis → déploiement GHT / réseau privé → expansion européenne.</p></div>
</div>
<p style="margin-top:12px;font-size:13px;color:#56698a">Adaptation d'abord, atténuation ensuite. """+C('pch','s26','gov')+"""</p>
""", "Six étapes = six lignes de revenus.")

add("why-now","content","Pourquoi l'eau, pourquoi maintenant — la décennie hospitalière sous contrainte hydrique",
"""
<div class="grid">
  <div>
    <div class="card accent"><h3>La nouvelle réalité opérationnelle</h3>
      <ul>
        <li><b>Raréfaction :</b> bassins français en déficit structurel (Loire, Adour-Garonne, PACA).</li>
        <li><b>Réglementation :</b> Décret n°2024-796 (12 juillet 2024, en vigueur 1er sept. 2024) ouvre la voie de la réutilisation non clinique.</li>
        <li><b>Tarifs :</b> indexation eau + assainissement pèse sur l'OPEX ; assainissement souvent &gt; eau potable.</li>
        <li><b>Continuité :</b> sécheresses et arrêtés menacent les fonctions techniques en été.</li>
        <li><b>Reporting :</b> Planification écologique du système de santé impose des plans eau par établissement. """+C('gov','tsp','ird')+"""</li>
      </ul>
    </div>
  </div>
  <div>
    <div class="banner">L'eau deviendra une <b>contrainte d'exploitation</b>,<br/>pas une métrique de durabilité.</div>
    <div class="card"><h3>Pourquoi les hôpitaux ne peuvent attendre</h3>
      <ul>
        <li>Santé = <b>&gt; 8 % des GES nationaux</b>, ~50 MtCO₂e (offre de soins 45 %, produits 55 %). """+C('gov','hcw')+"""</li>
        <li>Offre de soins = bâtiments, énergie, <b>eau</b>, déchets, transport.</li>
        <li>La dialyse est le flux hospitalier récurrent le plus intensif en eau.</li>
        <li>L'adaptation hydrique rembourse l'OPEX <b>avant</b> que le carbone ne compte.</li>
      </ul>
    </div>
  </div>
</div>
""", "Raréfaction, réglementation, tarifs, continuité.")

add("why-dialysis","content","Pourquoi la dialyse est le bon premier service hospitalier",
"""
<div class="grid3">
  <div class="card"><h3>Mesurable</h3><p>Boucle technique fermée. Chaque séance a une eau d'alimentation, un volume de rejet et une énergie connus. <b>~400–500 L</b> d'alimentation, <b>50–70 %</b> de rejet. """+C('per','gem','ope')+"""</p></div>
  <div class="card"><h3>Récurrent</h3><p>~156 séances / patient / an. Centre de 100 patients = <b>15 600 séances / an</b>. Économies prévisibles.</p></div>
  <div class="card"><h3>Techniquement actionnable</h3><p>Le rejet d'osmose inverse est un flux technique maîtrisé, pas une eau usée patient. Voies de réutilisation déjà éprouvées à l'international. """+C('ope','gem')+"""</p></div>
  <div class="card"><h3>Cliniquement borné</h3><p>Aucun contact patient. Jamais de retour vers la production d'eau de dialyse. Jamais de dialysat usagé. La limite est le coin de confiance.</p></div>
  <div class="card"><h3>Aligné aux politiques</h3><p>Le Guide SFNDT des bonnes pratiques 2026 couvre explicitement la réutilisation du rejet d'osmose. """+C('s26','s23')+"""</p></div>
  <div class="card dark"><h3>Stratégique</h3><p>Gagner la dialyse d'abord → étendre à la stérilisation, blanchisserie, cuisines, boucles techniques.</p></div>
</div>
""", "Cinq raisons + expansion.")

add("what-wasted","content","Ce qui est précisément gaspillé — le flux d'eau de dialyse",
"""
<div class="grid">
  <div>
    <h3>Une séance, simplifiée</h3>
    <div class="flow">
      <div class="step">Eau potable</div><span class="arrow">›</span>
      <div class="step">Prétraitement<br/><small>filtres · adoucisseur · charbon</small></div><span class="arrow">›</span>
      <div class="step">Osmose inverse<br/><small>perméat / rejet</small></div><span class="arrow">›</span>
      <div class="step">Boucle dialysat<br/><small>générateur + dialyseur</small></div><span class="arrow">›</span>
      <div class="step">Égout</div>
    </div>
    <div class="grid3" style="margin-top:8px">
      <div class="kpi"><div class="v">400–500 L</div><div class="l">Eau d'alimentation / séance</div><div class="s">"""+C('per','gem')+"""</div></div>
      <div class="kpi"><div class="v">50–70 %</div><div class="l">Fraction rejet osmose</div><div class="s">"""+C('per','ope')+"""</div></div>
      <div class="kpi"><div class="v">270 L</div><div class="l">Rejet base / séance</div><div class="s">220 bas · 320 haut · """+C('per')+"""</div></div>
    </div>
  </div>
  <div>
    <div class="card"><h3>Les trois flux cachés</h3>
      <ul>
        <li><b>Concentrat d'osmose (rejet) :</b> propre, faiblement salin, maîtrisé. Plus forte valeur de réutilisation.</li>
        <li><b>Eau de désinfection &amp; rinçage :</b> intermittente, résidus chimiques — réutilisation après dilution / neutralisation seulement.</li>
        <li><b>Dialysat usagé :</b> contact patient — <b>jamais</b> réutilisé. <span class="tag-bad">ROUGE</span></li>
      </ul>
    </div>
    <div class="card accent"><h3>Énergie cachée aussi</h3>
      <p>Ancienne OI australienne : <b>548 L + 7,2 kWh</b> / traitement. OI moderne : <b>357 L + 3,1 kWh</b>. """+C('ope')+"""</p>
      <p>East Kent — échangeurs de chaleur : <b>0,86 kWh/traitement</b>, <b>27 905 kWh/an</b> projetés. """+C('ope')+"""</p>
    </div>
  </div>
</div>
""", "Flux d'une séance. Trois flux : vert (rejet), orange (rinçage), rouge (dialysat).")

# PART 2
add("div-measure","divider","Partie 2 — Mesurer et réutiliser",
"""<p class="lead">Sans mesure, pas de redessin.<br/>Sans redessin, pas de certification.</p>""", "Transition.")

add("measure","content","Comment l'eau est mesurée — architecture de métrologie 4 points",
"""
<div class="grid">
  <div>
    <h3>Les quatre compteurs</h3>
    <div class="card"><ul>
      <li><b>M1 · Entrée potable</b> — eau totale entrant dans la centrale de traitement d'eau.</li>
      <li><b>M2 · Perméat OI</b> — eau effectivement délivrée à la boucle dialysat.</li>
      <li><b>M3 · Rejet OI</b> — flux technique maîtrisé candidat à la réutilisation.</li>
      <li><b>M4 · Livraison réutilisation</b> — eau effectivement substituée (toilettes / nettoyage / refroidissement).</li>
    </ul></div>
    <div class="card accent"><h3>Plus voies contextuelles</h3>
      <ul>
        <li>Conductivité sur M3 → logique de routage (forte salinité → égout, faible → réutilisation). """+C('gem')+"""</li>
        <li>Pression + débit sur la boucle de réutilisation → détection fuite et stagnation.</li>
        <li>Sous-compteur énergie sur OI + échangeur (optionnel).</li>
        <li>Horodaté avec le journal de séance → benchmark L/séance.</li>
      </ul>
    </div>
  </div>
  <div>
    <h3>Pourquoi mesurer d'abord gagne</h3>
    <div class="card dark"><p>SFNDT 2023 et 2026 placent toutes deux la <b>mesure d'abord</b> au cœur de la néphrologie verte. """+C('s23','s26')+"""</p>
    <p>Méthodologie TSP-Pathway : objectif, périmètre, hypothèses transparentes, étude d'incertitude. """+C('tsp')+"""</p>
    <p>Pas de mesure → pas de dossier ARS, pas de CEE, pas d'allégation d'économie.</p></div>
    <div class="card"><h3>Du compteur à la preuve</h3>
      <ul>
        <li>Référentiel 4–6 sem. avant toute intervention.</li>
        <li>Enregistrement continu après intervention.</li>
        <li>Rapport mensuel à direction, technique, hygiène.</li>
        <li>Bundle KPI trimestriel pour ARS &amp; finance.</li>
      </ul>
    </div>
  </div>
</div>
""", "4 compteurs + conductivité + énergie. La mesure est la douve.")

add("reference","content","Centre de référence — 100 patients, 15 600 séances",
"""
<p class="lead">Une UDM française moyenne typique. Les chiffres que les hôpitaux peuvent vérifier sur leurs propres factures. """+C('per')+"""</p>
<div class="grid4">
  <div class="kpi"><div class="v">100</div><div class="l">Patients</div></div>
  <div class="kpi"><div class="v">156</div><div class="l">Séances / patient / an</div></div>
  <div class="kpi"><div class="v">15 600</div><div class="l">Séances / an</div></div>
  <div class="kpi"><div class="v">~4 200 m³</div><div class="l">Rejet / an (base)</div></div>
</div>
<div class="grid3" style="margin-top:14px">
  <div class="card"><h3>Scénario bas</h3>
    <p><b>220 L</b> rejet / séance</p>
    <p><b>3 432 m³</b> / an</p>
    <p>OI moderne, désinfection optimisée.</p>
  </div>
  <div class="card accent"><h3>Scénario central</h3>
    <p><b>270 L</b> rejet / séance</p>
    <p><b>4 212 m³</b> / an</p>
    <p>Équipement mi-vie typique.</p>
  </div>
  <div class="card"><h3>Scénario haut</h3>
    <p><b>320 L</b> rejet / séance</p>
    <p><b>4 992 m³</b> / an</p>
    <p>OI vieillissante + 3×/sem. """+C('ope')+"""</p>
  </div>
</div>
<p style="margin-top:10px;font-size:13px;color:#56698a">Caveat carbone eau-seule : ~1,0–1,1 tCO₂e / an pour la tranche 4 200 m³ — secondaire face à la résilience OPEX. """+C('per','tsp')+"""</p>
""", "Trois scénarios. Caveat carbone explicite.")

add("reuse-map","content","Ce qui peut être réutilisé — la carte vert / orange / rouge",
"""
<div class="grid3">
  <div class="card" style="border-left:6px solid var(--ok)">
    <h3 style="color:var(--ok)">VERT — réutiliser dès maintenant</h3>
    <ul>
      <li>Chasses d'eau en zones non cliniques</li>
      <li>Nettoyage des sols &amp; extérieur</li>
      <li>Appoint tours aéroréfrigérantes (CTA) avec traitement</li>
      <li>Arrosage jardin / extérieur</li>
      <li>Lavage technique (chariots, bacs)</li>
    </ul>
    <p style="font-size:12px;color:var(--ok)"><b>Preuves :</b> Canterbury, Bristol, Ashford, ANZSN. """+C('ope','gem')+"""</p>
  </div>
  <div class="card" style="border-left:6px solid var(--warn)">
    <h3 style="color:var(--warn)">ORANGE — spécifique au site</h3>
    <ul>
      <li>Prélavage blanchisserie</li>
      <li>Alimentation stérilisation (hors rinçage final)</li>
      <li>Appoint chaudière / refroidissement avec polissage</li>
      <li>Recirculation prétraitement (OI à récupération) — selon vendeur</li>
      <li>Réutilisation du rinçage désinfection — seulement après neutralisation</li>
    </ul>
    <p style="font-size:12px;color:var(--warn)"><b>Caveat :</b> exige dossier, qualité de l'eau locale, validation vendeur.</p>
  </div>
  <div class="card" style="border-left:6px solid var(--bad)">
    <h3 style="color:var(--bad)">ROUGE — jamais réutiliser</h3>
    <ul>
      <li>Dialysat usagé (contact patient)</li>
      <li>Toute remontée vers la production d'eau de dialyse</li>
      <li>Eau de boisson / préparation alimentaire</li>
      <li>Rinçage final équipement à contact patient</li>
      <li>Rinçage final endoscopes / instruments chirurgicaux</li>
    </ul>
    <p style="font-size:12px;color:var(--bad)"><b>Non négociable.</b> La limite de sécurité est le coin de confiance.</p>
  </div>
</div>
<div class="banner" style="margin-top:14px">La question n'est <b>pas</b> de savoir si l'eau peut être réutilisée.<br/>La question est <b>quelle eau, où, sous quelles conditions légales et de sécurité</b>.</div>
""", "Carte décisionnelle. Limite non négociable.")

add("legal-eich","content","Droit actuel vs cadre EICH",
"""
<div class="grid">
  <div>
    <div class="card"><h3>Avant — pré-1er sept. 2024</h3>
      <ul>
        <li>Pas de cadre général de réutilisation non potable en santé.</li>
        <li>Dérogations ad hoc ARS / DDETSPP.</li>
        <li>Projets de réutilisation bloqués par l'incertitude juridique.</li>
      </ul>
    </div>
    <div class="card accent"><h3>Après — <b>Décret n°2024-796</b>, en vigueur 1er sept. 2024</h3>
      <p><b>EICH</b> = Eaux Impropres à la Consommation Humaine pour établissements sensibles dont la santé. """+C('gov','s26')+"""</p>
      <ul>
        <li>Autorise la réutilisation non clinique sous autorisation site-spécifique.</li>
        <li>Dossier de sécurité ARS / préfecture exigé.</li>
        <li>Réseau séparé, prévention des interconnexions, signalisation, carnet sanitaire.</li>
        <li>Surveillance &amp; arrêt d'urgence exigés.</li>
        <li>Définit des usages autorisés, pas une licence générale.</li>
      </ul>
    </div>
  </div>
  <div>
    <div class="card dark"><h3>Ce qu'EICH ne fait PAS</h3>
      <ul>
        <li>N'autorise aucune réutilisation à contact patient.</li>
        <li>Ne pré-approuve aucun site — chaque dossier est local.</li>
        <li>Ne dispense pas de la validation hygiène (CLIN).</li>
        <li>Ne garantit pas d'économie tarifaire — structure assainissement / potable locale décide.</li>
      </ul>
    </div>
    <div class="banner">EICH ouvre la porte.<br/>EcoDialysis construit le dossier.</div>
    <p style="font-size:12px;color:#56698a">Caveat : la voie ARS exacte et la fréquence de surveillance varient selon le bassin et le type d'établissement. À confirmer à chaque dépôt. Voir Annexe H. """+C('gov')+"""</p>
  </div>
</div>
""", "Décret 2024-796 est le déclencheur. EcoDialysis en fait un dossier répétable.")

add("dossier","content","Ce que doit contenir un dossier ARS / préfecture",
"""
<div class="grid">
  <div>
    <h3>Contenu technique obligatoire</h3>
    <div class="card"><ul>
      <li>Description de la source : caractérisation du rejet OI (conductivité, microbio, chimie).</li>
      <li>Description des usages : usages cibles, volumes, emplacements.</li>
      <li>Réseau séparé : schéma, matériaux, dispositifs anti-retour (EA / EB / AA).</li>
      <li>Stockage : volume, temps de séjour, matériaux, anti-stagnation.</li>
      <li>Traitement le cas échéant : UV-C, filtration, désinfection.</li>
      <li>Plan de surveillance : paramètres, fréquence, alarmes.</li>
      <li>Arrêt d'urgence &amp; bascule vers potable.</li>
      <li>Entrée carnet sanitaire et responsabilités.</li>
    </ul></div>
  </div>
  <div>
    <h3>Contenu gouvernance obligatoire</h3>
    <div class="card accent"><ul>
      <li>Analyse de risque (type HACCP) par usage.</li>
      <li>Chaîne de validation : direction, technique, hygiène (CLIN), médical, qualité.</li>
      <li>Plan de formation du personnel + signalétique.</li>
      <li>Plan de maintenance + contrats de service.</li>
      <li>Revue annuelle &amp; rapport à l'ARS.</li>
      <li>Carte des parties prenantes (ARS, préfecture, Agence de l'Eau, hygiène).</li>
    </ul></div>
    <div class="banner">EcoDialysis livre <b>les deux piles</b> dans un seul playbook répétable.</div>
  </div>
</div>
<p style="margin-top:8px;font-size:12px;color:#56698a">Sources : """+C('gov','s26','s23')+"""</p>
""", "Contenu du dossier ARS.")

add("tailored","content","Pourquoi chaque site exige un playbook sur mesure",
"""
<p class="lead">Un playbook spécifique au site n'est pas optionnel. Le même rejet d'osmose n'a pas le même destin dans tous les hôpitaux.</p>
<div class="grid">
  <div class="card"><h3>Ce qui varie selon le site</h3>
    <ul>
      <li><b>Qualité de l'eau :</b> dureté, chlorure, silice du réseau — détermine le polissage requis.</li>
      <li><b>Structure tarifaire :</b> eau + assainissement €/m³ — détermine le ROI.</li>
      <li><b>Implantation :</b> étage UDM, distance toilettes, accessibilité boucles techniques — détermine le CAPEX.</li>
      <li><b>Âge OI :</b> détermine le volume de rejet (220–320 L).</li>
      <li><b>Profil de demande :</b> planning séances vs demande aux points d'usage — détermine le dimensionnement du stockage.</li>
      <li><b>Gouvernance :</b> CHU vs CH vs privé — détermine le chemin de validation.</li>
    </ul>
  </div>
  <div class="card accent"><h3>Pourquoi une cuve générique échoue</h3>
    <ul>
      <li>Mauvaise taille → débordement ou pénurie.</li>
      <li>Mauvais polissage → biofilm ou incompatibilité chimique.</li>
      <li>Mauvais réseau → risque d'interconnexion, refus ARS.</li>
      <li>Mauvaise adéquation demande → vide &gt; 30 % du temps.</li>
      <li>Mauvais reporting → pas de vérification du ROI, pas de certification.</li>
    </ul>
    <p style="margin-top:8px"><b>Les hôpitaux n'ont pas besoin d'un autre tableau ESG.<br/>Ils ont besoin d'un playbook opérationnel de résilience hydrique.</b></p>
  </div>
</div>
""", "Justifier le playbook contre le produit générique.")

# PART 3
add("div-proof","divider","Partie 3 — Preuves",
"""<p class="lead">Des centres internationaux prouvent déjà que la réutilisation et l'optimisation fonctionnent.<br/>Le plus dur n'est pas la cuve — c'est le dossier site-spécifique répétable.</p>""", "Transition preuves.")

add("intl-map","content","Preuve internationale — huit centres de référence",
"""
<div class="grid4">
  <div class="card"><h3>Canterbury · UK</h3><p>Récupération <b>800 L/h</b>, <b>~7 500 £/an</b>. """+C('ope')+"""</p></div>
  <div class="card"><h3>Bristol · UK</h3><p><b>13 140 m³/an</b>, <b>&gt; 15 000 £/an</b>. """+C('ope')+"""</p></div>
  <div class="card"><h3>Ashford · UK</h3><p>Conception-intégrée <b>~2 500 £</b>. """+C('ope')+"""</p></div>
  <div class="card"><h3>East Kent · UK</h3><p>Récup. chaleur <b>0,86 kWh/Tx</b>, <b>27 905 kWh/an</b>. """+C('ope','gem')+"""</p></div>
  <div class="card"><h3>Bendigo · AU</h3><p>Réutilisation rejet OI, benchmark ANZSN.</p></div>
  <div class="card"><h3>Queen Elizabeth · AU</h3><p>Rétrofit OI moderne, L+kWh/Tx réduits.</p></div>
  <div class="card"><h3>Barwon · AU</h3><p>Optimisation procédé &amp; métrologie.</p></div>
  <div class="card"><h3>Espagne · 20 centres</h3><p>Moyenne <b>476,5 L/séance</b> ; quotidien <b>430 L</b> vs 3×/sem <b>630 L</b>. """+C('ope','gem')+"""</p></div>
</div>
<p style="margin-top:10px;font-size:13px;color:#56698a">Preuves agrégées et vérifiables dans Annexes B (tableau cas) et I (sources).</p>
""", "8 cartes preuve internationale.")

add("uk-cluster","content","Cluster UK — Canterbury · Bristol · Ashford · East Kent",
"""
<table>
<tr><th>Centre</th><th>Intervention</th><th>Volume économisé</th><th>Économie €</th><th>Énergie / co-bénéfice</th><th>Source</th></tr>
<tr><td>Canterbury</td><td>Récup. rejet OI → toilettes &amp; nettoyage</td><td><b>800 L/h</b></td><td>~7 500 £/an</td><td>—</td><td>"""+C('ope')+"""</td></tr>
<tr><td>Bristol</td><td>Réutilisation rejet OI (grand centre)</td><td><b>13 140 m³/an</b></td><td>&gt; 15 000 £/an</td><td>—</td><td>"""+C('ope')+"""</td></tr>
<tr><td>Ashford</td><td>Conception-intégrée bâtiment neuf</td><td>n/a faible capex</td><td>~2 500 £ design-in</td><td>—</td><td>"""+C('ope')+"""</td></tr>
<tr><td>East Kent</td><td>Récupération chaleur échangeur</td><td>—</td><td>—</td><td><b>0,86 kWh/Tx · 27 905 kWh/an</b></td><td>"""+C('ope','gem')+"""</td></tr>
</table>
<div class="grid" style="margin-top:14px">
  <div class="card accent"><h3>Schéma</h3>
    <ul>
      <li>Conception-intégrée bat le rétrofit en CAPEX (Ashford).</li>
      <li>Les grands centres composent leurs économies (Bristol).</li>
      <li>Le rejet OI est le levier dominant (Canterbury, Bristol).</li>
      <li>La récupération de chaleur est un second levier — couplée au rejet (East Kent).</li>
    </ul>
  </div>
  <div class="card"><h3>Traduction française</h3>
    <ul>
      <li>UK = approbations locales NHS — France ajoute la couche ARS / EICH.</li>
      <li>Tarifs UK ≠ FR — ROI français basé sur eau+assainissement local €/m³.</li>
      <li>UK montre que la réutilisation est techniquement routinière — la couche manquante en France est le dossier.</li>
    </ul>
  </div>
</div>
""", "Cluster UK + traduction française.")

add("anz-cluster","content","Australie / Nouvelle-Zélande — ANZSN, Bendigo, Queen Elizabeth, Barwon",
"""
<div class="grid">
  <div>
    <div class="card"><h3>Impact agrégé ANZSN</h3>
      <ul>
        <li><b>&gt; 160 000 L/an</b> d'eau économisée</li>
        <li><b>6,4 MWh/an</b> d'électricité économisée</li>
        <li><b>720 L</b> de solution d'acide citrique évités</li>
        <li><b>~2 400 AU$</b> d'économies produit</li>
      </ul>
      <p style="font-size:12px;color:#56698a">Source : """+C('ope')+"""</p>
    </div>
    <div class="card accent"><h3>OI moderne vs ancienne — mesuré</h3>
      <table>
        <tr><th></th><th>Ancienne</th><th>Moderne</th></tr>
        <tr><td>L / traitement</td><td>548</td><td><b>357</b></td></tr>
        <tr><td>kWh / traitement</td><td>7,2</td><td><b>3,1</b></td></tr>
      </table>
      <p style="font-size:12px;margin-top:6px">Le remplacement OI seul donne <b>~35 % eau + 57 % énergie</b> en moins par traitement. """+C('ope')+"""</p>
    </div>
  </div>
  <div>
    <div class="card dark"><h3>Pourquoi cela compte pour le playbook</h3>
      <ul>
        <li>Même <b>sans</b> réutilisation, le remplacement OI est un levier majeur.</li>
        <li>Optimiser la désinfection (citrique / chaleur) économise produits + eau + carbone.</li>
        <li>Optimisation procédé et réutilisation sont <b>additives</b>, pas alternatives.</li>
        <li>ANZSN prouve qu'un réseau de néphrologie verte peut publier — base du label EcoDialysis.</li>
      </ul>
    </div>
    <div class="card"><h3>Bendigo · Queen Elizabeth · Barwon</h3>
      <p>Chacun est un benchmark ANZSN nommé en réutilisation rejet OI, rétrofit OI moderne et métrologie procédé. Triple-modèle dont le marché français manque. """+C('ope','gem')+"""</p>
    </div>
  </div>
</div>
""", "Cluster ANZ + leçons.")

add("optim","content","Preuves d'optimisation — Espagne, OI moderne, désinfection",
"""
<div class="grid">
  <div>
    <h3>Espagne · benchmark 20 centres</h3>
    <div class="card">
      <table>
        <tr><th>Cohorte</th><th>L / HD</th><th>kWh / HD</th></tr>
        <tr><td>Moyenne 20 centres</td><td><b>476,5</b></td><td>—</td></tr>
        <tr><td>Centres ouverts quotidiennement</td><td><b>430,20</b></td><td><b>10,82</b></td></tr>
        <tr><td>Centres 3×/semaine</td><td><b>629,81</b></td><td><b>16,79</b></td></tr>
      </table>
      <p style="font-size:12px;margin-top:6px">Le rythme d'ouverture est un <b>levier direct</b> eau + énergie. """+C('ope','gem')+"""</p>
    </div>
  </div>
  <div>
    <h3>Les trois leviers d'optimisation</h3>
    <div class="card accent"><ul>
      <li><b>Équipement :</b> OI moderne (357 L vs 548 L ; 3,1 kWh vs 7,2 kWh). """+C('ope')+"""</li>
      <li><b>Planning :</b> quotidien vs 3×/sem. (430 L vs 630 L / HD). """+C('ope')+"""</li>
      <li><b>Désinfection :</b> citrique vs chaleur, optimisation fréquence, eau + chimie évitées. """+C('gem','s26')+"""</li>
    </ul></div>
    <div class="card"><h3>Dans la boucle dialysat</h3>
      <ul>
        <li>Réduction Qd (ex. 500 → 400 ml/min) : <b>~24 L de dialysat</b> économisés/séance dans le cadrage cité. """+C('s26')+"""</li>
        <li><b>60–100 L</b> d'eau prétraitée économisés par séance dans le même contexte. """+C('s26')+"""</li>
        <li>Réglage HDF, rejet routé par conductivité. """+C('gem')+"""</li>
      </ul>
    </div>
  </div>
</div>
""", "Trois leviers, tous mesurés.")

add("fr-proof","content","Preuves françaises — Saint-Exupéry, AP-HM, playbook SFNDT",
"""
<div class="grid">
  <div>
    <div class="card"><h3>Clinique Saint-Exupéry · Toulouse</h3>
      <ul>
        <li><b>~1 128 m³/an</b> d'eau économisée (réutilisation rejet OI). """+C('s26')+"""</li>
        <li>Investissement <b>~30 k€</b>, retour <b>5–6 ans</b>.</li>
        <li>Modèle opérationnel français — la correspondance la plus proche du centre de référence EcoDialysis.</li>
      </ul>
    </div>
    <div class="card accent"><h3>AP-HM · Marseille</h3>
      <ul>
        <li>Études à potentiel de réutilisation plus large référencées.</li>
        <li>Démontre l'intérêt à l'échelle CHU et la faisabilité ARS. """+C('s26')+"""</li>
      </ul>
    </div>
  </div>
  <div>
    <div class="card dark"><h3>SFNDT 2026 playbook — ce qu'il confirme</h3>
      <ul>
        <li>La réutilisation du rejet OI est une fiche-action recommandée. """+C('s26')+"""</li>
        <li>Distribution centralisée d'acide concentré réduit déchets &amp; consommation.</li>
        <li>Contraintes de stockage : durée, température, distance.</li>
        <li>Exigences de réseau séparé.</li>
        <li>Pas de saut direct vers la réutilisation à haut risque.</li>
        <li>Obligations de gestion énergétique, réduction des déchets, actions équipe, communication RSE.</li>
      </ul>
    </div>
    <div class="banner">La France a les cas.<br/>La France a le guide.<br/>Il manque le <b>moteur à dossiers répétable</b>.</div>
  </div>
</div>
""", "Saint-Exupéry + SFNDT 2026 = ancrage français.")

# PART 4
add("div-product","divider","Partie 4 — Produit",
"""<p class="lead">Pas une cuve. Pas un rapport ESG. Un playbook de résilience hydrique site-spécifique<br/>livré comme audit + dossier + mise en œuvre + monitoring + label.</p>""", "Transition produit.")

add("not-tank","content","Pourquoi pas juste une cuve ?",
"""
<div class="grid">
  <div>
    <h3>Le fantasme de la cuve</h3>
    <div class="card"><p>« Installez juste une cuve sous l'osmose et réutilisez l'eau. »</p>
    <p style="margin-top:6px;color:#56698a"><i>Cette vision meurt au premier contact avec la centrale eau hospitalière.</i></p></div>
    <h3 style="margin-top:14px">Ce qu'une cuve ne peut pas faire</h3>
    <ul class="xlist">
      <li>Ne peut pas caractériser le flux de rejet</li>
      <li>Ne peut pas adapter les volumes à la demande non clinique</li>
      <li>Ne peut pas monter le dossier EICH</li>
      <li>Ne peut pas exploiter le réseau séparé</li>
      <li>Ne peut pas passer la revue CLIN</li>
      <li>Ne peut pas prouver les économies</li>
      <li>Ne peut pas se déployer sur un GHT</li>
    </ul>
  </div>
  <div>
    <h3>Ce que fait EcoDialysis à la place</h3>
    <ul class="checklist">
      <li><b>Audit</b> — métrologie 4 points + factures + plans + inventaire OI.</li>
      <li><b>Cartographie</b> — voies vert/orange/rouge pour ce site précis.</li>
      <li><b>Dimensionnement</b> — stockage + réseau + traitement adaptés au profil de demande.</li>
      <li><b>Dépôt</b> — dossier ARS conforme EICH avec chaîne de validation.</li>
      <li><b>Mise en œuvre</b> — partenariat plombiers / intégrateurs / vendeurs OI.</li>
      <li><b>Mesure</b> — monitoring SaaS continu + vérification mensuelle.</li>
      <li><b>Certification</b> — label EcoDialysis par site, comparable.</li>
    </ul>
    <div class="banner" style="margin-top:8px">Une cuve est un composant.<br/>Un <b>moteur à dossiers</b> est le produit.</div>
  </div>
</div>
""", "Cuve vs moteur à dossiers.")

add("product","content","Architecture produit — audit · playbook · mise en œuvre · monitoring · label",
"""
<div class="grid5">
  <div class="card"><h3>1 · Audit</h3>
    <ul>
      <li>Visite site + données</li>
      <li>Pose 4 compteurs</li>
      <li>Analyse factures &amp; tarifs</li>
      <li>Cartographie demande</li>
      <li>Référentiel 4–6 sem.</li>
    </ul>
    <p><span class="pill">8–18 k€</span></p>
  </div>
  <div class="card"><h3>2 · Playbook</h3>
    <ul>
      <li>Carte vert / orange / rouge</li>
      <li>Scénarios ROI</li>
      <li>Brouillon dossier EICH</li>
      <li>Registre des risques</li>
      <li>Go / no-go</li>
    </ul>
    <p><span class="pill">10–25 k€</span></p>
  </div>
  <div class="card"><h3>3 · Mise en œuvre</h3>
    <ul>
      <li>Accompagnement appel d'offres</li>
      <li>Coordination intégrateurs</li>
      <li>Validation hygiène</li>
      <li>Mise en service</li>
      <li>Formation équipe</li>
    </ul>
    <p><span class="pill">5–15 % du CAPEX</span></p>
  </div>
  <div class="card"><h3>4 · Monitoring</h3>
    <ul>
      <li>Tableau de bord SaaS</li>
      <li>4 points + conductivité</li>
      <li>Vérification mensuelle</li>
      <li>Reporting ARS</li>
      <li>Alarmes &amp; carnet</li>
    </ul>
    <p><span class="pill">600–1 400 €/mois</span></p>
  </div>
  <div class="card dark"><h3>5 · Label</h3>
    <ul>
      <li>Certification EcoDialysis</li>
      <li>Base benchmark</li>
      <li>Audit annuel</li>
      <li>Registre public</li>
      <li>Effet réseau</li>
    </ul>
    <p style="color:#cfe1f7"><span class="pill" style="background:#1d4a8d;color:#fff">3–8 k€ / an</span></p>
  </div>
</div>
<p style="margin-top:10px;font-size:13px;color:#56698a">Coin = audit. Répétabilité = playbook. Récurrence = monitoring. Réseau = label. Défense = base benchmark. """+C('pch','per','s26')+"""</p>
""", "Cinq couches produit.")

add("ecosystem","content","Écosystème équipement &amp; fournisseurs",
"""
<table>
<tr><th>Couche</th><th>Équipement</th><th>Fournisseurs référence</th><th>Point de contact EcoDialysis</th></tr>
<tr><td>Générateur dialyse</td><td>Machines d'hémodialyse</td><td>Fresenius, B. Braun, Baxter/Vantive, Nikkiso, Nipro, JMS, Quanta, Outset/Tablo, NxStage</td><td>Réglage Qd / HDF, sous-comptage énergie</td></tr>
<tr><td>Centrale traitement eau</td><td>Prétraitement + OI + boucle</td><td>B. Braun AQUAboss, Fresenius, intégrateurs</td><td>Métrologie 4 points, caractérisation rejet</td></tr>
<tr><td>Dialyseur + lignes</td><td>Membranes &amp; circuits</td><td>Asahi Kasei, Toray, Fresenius, B. Braun, Nipro</td><td>Scorecard achats (Phase 3)</td></tr>
<tr><td>Acide concentré / bicarbonate</td><td>Liquide + cartouche</td><td>Fresenius, B. Braun, Baxter, régional</td><td>Playbook distribution centralisée """+C('s26')+"""</td></tr>
<tr><td>Désinfection</td><td>Citrique, chaleur, peracétique</td><td>Bundle vendeur</td><td>Optimisation fréquence """+C('gem','ope')+"""</td></tr>
<tr><td>Matériel réutilisation</td><td>Cuves, pompes, UV-C, anti-retour</td><td>Intégrateurs locaux</td><td>Dimensionnement, classes anti-retour (EA/EB/AA)</td></tr>
<tr><td>Métrologie &amp; IoT</td><td>Débit, conductivité, énergie</td><td>Endress+Hauser, Siemens, régional</td><td>Ingestion SaaS</td></tr>
<tr><td>Déchets &amp; consommables</td><td>DASRI/DAOM</td><td>Veolia, Suez, régional</td><td>Tri + réduction (Phase 3)</td></tr>
<tr><td>Futur / pilote</td><td>NeoKidney, AWAK, sorbant REDY</td><td>NextKidney, AWAK, R&amp;D vendeurs</td><td>Veille &amp; intégration pilote """+C('gem')+"""</td></tr>
</table>
<p style="margin-top:10px;font-size:12px;color:#56698a">Paysage fournisseur détaillé avec caveats &amp; rôles partenariats en Annexe A11.</p>
""", "Écosystème fournisseurs résumé.")

add("maturity","content","Maturité technologique — prêt / spécifique site / pilote seulement",
"""
<table>
<tr><th>Levier</th><th>Maturité</th><th>Eau</th><th>Énergie</th><th>Déchets</th><th>Risque clinique</th><th>Phase EcoDialysis</th></tr>
<tr><td>Rejet OI → réutilisation non clinique</td><td><span class="tag-ok">Prêt</span></td><td>+++</td><td>0</td><td>+</td><td>Aucun (limite)</td><td>Phase 1</td></tr>
<tr><td>Remplacement OI moderne</td><td><span class="tag-ok">Prêt</span></td><td>+++</td><td>+++</td><td>+</td><td>Aucun</td><td>Phase 1</td></tr>
<tr><td>Optimisation désinfection</td><td><span class="tag-ok">Prêt</span></td><td>++</td><td>+</td><td>++</td><td>Validation vendeur</td><td>Phase 1</td></tr>
<tr><td>Récupération de chaleur (East Kent)</td><td><span class="tag-ok">Prêt</span></td><td>0</td><td>++</td><td>0</td><td>Aucun</td><td>Phase 2</td></tr>
<tr><td>Réduction Qd (500→400 ml/min)</td><td><span class="tag-warn">Site</span></td><td>++</td><td>+</td><td>+</td><td>Validation clinique</td><td>Phase 2</td></tr>
<tr><td>Acide concentré centralisé</td><td><span class="tag-warn">Site</span></td><td>+</td><td>+</td><td>++</td><td>Faible</td><td>Phase 2</td></tr>
<tr><td>Réutilisation routée par conductivité</td><td><span class="tag-warn">Site</span></td><td>++</td><td>0</td><td>0</td><td>Ingénierie</td><td>Phase 1–2</td></tr>
<tr><td>OI à récupération prétraitement</td><td><span class="tag-warn">Site</span></td><td>++</td><td>−</td><td>0</td><td>Vendeur</td><td>Phase 2</td></tr>
<tr><td>Réglage volume dialysat HDF</td><td><span class="tag-warn">Site</span></td><td>+</td><td>0</td><td>0</td><td>Validation clinique</td><td>Phase 2</td></tr>
<tr><td>Sorbant / portable (REDY, AWAK)</td><td><span class="tag-bad">Pilote</span></td><td>+++</td><td>+</td><td>+</td><td>Élevé</td><td>Veille</td></tr>
<tr><td>NeoKidney portable</td><td><span class="tag-bad">Pilote</span></td><td>+++</td><td>+</td><td>+</td><td>Élevé</td><td>Veille</td></tr>
<tr><td>Réutilisation dialysat usagé</td><td><span class="tag-bad">Non déployable</span></td><td>n/a</td><td>n/a</td><td>n/a</td><td>Limite</td><td>Jamais</td></tr>
</table>
<p style="margin-top:8px;font-size:12px;color:#56698a">Matrice 18 lignes complète en Annexe A13. Sources : """+C('gem','ope','s26')+"""</p>
""", "Matrice de maturité.")

add("business","content","Modèle économique — audit · playbook · SaaS · succès · label",
"""
<div class="grid">
  <div>
    <h3>Cinq lignes de revenus</h3>
    <div class="card">
      <table>
        <tr><th>Ligne</th><th>Logique</th><th>Fourchette</th></tr>
        <tr><td>Audit</td><td>Coin d'entrée, pilote payé</td><td>8–18 k€</td></tr>
        <tr><td>Playbook + dossier EICH</td><td>Par site</td><td>10–25 k€</td></tr>
        <tr><td>Accompagnement mise en œuvre</td><td>% du CAPEX</td><td>5–15 %</td></tr>
        <tr><td>Monitoring SaaS</td><td>Récurrent</td><td>600–1 400 €/mois</td></tr>
        <tr><td>Honoraires succès</td><td>% des économies vérifiées</td><td>10–20 % an 1–3</td></tr>
        <tr><td>Label + benchmark</td><td>Annuel</td><td>3–8 k€/an</td></tr>
      </table>
    </div>
    <p style="font-size:12px;color:#56698a;margin-top:6px">Tarification indicative ; calibrée sur les premiers pilotes.</p>
  </div>
  <div>
    <h3>Canaux &amp; expansion</h3>
    <div class="card accent"><ul>
      <li><b>Direct :</b> RSE / DD CHU, ingénierie biomédicale.</li>
      <li><b>Déploiement GHT :</b> un CH gagné → cluster suit.</li>
      <li><b>Réseaux privés :</b> AURA / Diaverum / NephroCare / chaînes régionales.</li>
      <li><b>Partenariats fournisseurs :</b> vendeurs OI &amp; générateurs intègrent l'audit EcoDialysis à la vente.</li>
      <li><b>Partenaires subventions :</b> Agences de l'Eau (par bassin), CEE (catégorie à confirmer), ADEME.</li>
    </ul></div>
    <div class="card dark"><h3>Pourquoi cela compose</h3>
      <ul>
        <li>Données audit → base benchmark → défensibilité.</li>
        <li>Réutilisation playbook → expansion de marge.</li>
        <li>Adoption label → effet réseau entre directeurs de néphrologie.</li>
      </ul>
    </div>
  </div>
</div>
""", "Cinq lignes, quatre canaux, trois forces composantes.")

add("buyers","content","Carte des acheteurs — qui signe, qui paie, qui scale",
"""
<table>
<tr><th>Acheteur</th><th>Douleur</th><th>Unité de décision</th><th>Coin d'entrée</th><th>Expansion</th></tr>
<tr><td><b>CHU</b> · grand public</td><td>Reporting + réputation + raréfaction</td><td>RSE/DD + bioméd + direction</td><td>Audit + pilote vitrine</td><td>Autres services (stérilisation, blanchisserie)</td></tr>
<tr><td><b>CH / GHT</b></td><td>Raréfaction multi-sites + OPEX</td><td>Direction GHT + technique</td><td>Un CH pilote → accord-cadre GHT</td><td>Déploiement cluster</td></tr>
<tr><td><b>Réseau dialyse privé</b></td><td>Compression de marge + ESG</td><td>Directeur médical + ops + finance</td><td>Audit cadre réseau</td><td>Déploiement transfrontalier</td></tr>
<tr><td><b>Unité indépendante moyenne</b></td><td>Sensibilité OPEX</td><td>Médecin propriétaire</td><td>Audit + SaaS léger</td><td>Référence pour unités similaires</td></tr>
<tr><td><b>Neuf / rénovation</b></td><td>Fenêtre conception-intégrée</td><td>Architecte + bioméd + achats</td><td>Design-in à la Ashford</td><td>Partenariats architectes</td></tr>
</table>
<p style="margin-top:10px;font-size:13px;color:#56698a">Marché de référence : ~2 965 établissements de santé · ~1 100–1 200 unités de dialyse · 51 700 patients · 77 % en centre/UDM. """+C('per')+"""</p>
""", "Cinq archétypes acheteurs.")

# PART 5
add("div-ask","divider","Partie 5 — Pilote, risque &amp; demande",
"""<p class="lead">Trois pilotes. Six mois. Un moteur à dossiers répétable pour la France.</p>""", "Transition.")

add("pilots","content","Plan trois pilotes — CHU · GHT · réseau privé",
"""
<div class="grid3">
  <div class="card"><h3>Pilote A · CHU vitrine</h3>
    <p><b>Cible :</b> AP-HM / CHU Toulouse / CHU Lyon.</p>
    <ul>
      <li>~150 patients</li>
      <li>Réutilisation complète + récup. chaleur</li>
      <li>Preuve dossier EICH</li>
      <li>Voie publication SFNDT</li>
    </ul>
    <p><span class="pill">6 mois</span> <span class="pill">80–120 k€</span></p>
  </div>
  <div class="card accent"><h3>Pilote B · GHT taille moyenne</h3>
    <p><b>Cible :</b> CH en bassin stressé (Adour-Garonne / Loire).</p>
    <ul>
      <li>~80 patients</li>
      <li>Réutilisation + cadrage modernisation OI</li>
      <li>Accord-cadre GHT</li>
      <li>Co-financement Agence de l'Eau</li>
    </ul>
    <p><span class="pill">6 mois</span> <span class="pill">60–90 k€</span></p>
  </div>
  <div class="card dark"><h3>Pilote C · Réseau privé</h3>
    <p><b>Cible :</b> AURA / Diaverum / chaîne régionale.</p>
    <ul>
      <li>3 sites, ~100 patients chacun</li>
      <li>Test playbook répétable</li>
      <li>Déploiement SaaS + label</li>
      <li>Option déploiement réseau</li>
    </ul>
    <p style="color:#cfe1f7"><span class="pill" style="background:#1d4a8d;color:#fff">9 mois</span> <span class="pill" style="background:#1d4a8d;color:#fff">140–200 k€</span></p>
  </div>
</div>
<p style="margin-top:10px;font-size:13px;color:#56698a">Les trois ensemble testent : faisabilité technique, répétabilité du dossier, et scalabilité par canal.</p>
""", "Trois pilotes.")

add("need","content","Ce dont nous avons besoin de chaque hôpital pilote",
"""
<div class="grid">
  <div class="card"><h3>Accès</h3>
    <ul>
      <li>Centrale eau &amp; local OI</li>
      <li>Plans techniques (eau, évacuation, électricité)</li>
      <li>Planning séances UDM</li>
      <li>Carte demande non clinique (toilettes, nettoyage, CTA, jardin)</li>
      <li>Autorisation pose 4 compteurs</li>
    </ul>
  </div>
  <div class="card"><h3>Données</h3>
    <ul>
      <li>12 mois factures eau + assainissement</li>
      <li>Inventaire OI + générateurs + âge</li>
      <li>Factures énergie zone traitement eau</li>
      <li>Journal séances (sessions/an par machine)</li>
      <li>Journaux maintenance &amp; désinfection</li>
    </ul>
  </div>
  <div class="card accent"><h3>Personnes</h3>
    <ul>
      <li>Référent bioméd / services techniques</li>
      <li>Référent hygiène / CLIN</li>
      <li>Sponsor direction</li>
      <li>Référent médical (néphrologie)</li>
      <li>Contact pré-instruction ARS / préfecture</li>
    </ul>
  </div>
</div>
<p style="margin-top:10px;font-size:13px;color:#56698a">Aucune donnée clinique. Aucune donnée patient. L'hôpital reste responsable du traitement et propriétaire opérationnel.</p>
""", "Demandes concrètes. Pas de données cliniques.")

add("deliver","content","Ce que nous livrons en 30 jours",
"""
<div class="grid">
  <div>
    <div class="card"><h3>Jour 1–10 · Éco-audit</h3>
      <ul>
        <li>Visite site + entretiens</li>
        <li>Pose 4 compteurs</li>
        <li>Analyse factures + plans</li>
        <li>Inventaire OI + générateurs</li>
      </ul>
    </div>
    <div class="card"><h3>Jour 10–20 · Cartographie</h3>
      <ul>
        <li>Voies vert/orange/rouge</li>
        <li>Profil demande vs profil rejet</li>
        <li>Trois scénarios de réutilisation dimensionnés</li>
      </ul>
    </div>
  </div>
  <div>
    <div class="card"><h3>Jour 20–25 · ROI scénarios</h3>
      <ul>
        <li>Bas / central / haut rejet</li>
        <li>Taux de capture 50 / 70 / 90 %</li>
        <li>Sensibilité tarif + CAPEX</li>
        <li>Option empilement subventions</li>
      </ul>
    </div>
    <div class="card accent"><h3>Jour 25–30 · Pack décision</h3>
      <ul>
        <li>Registre des risques</li>
        <li>Brouillon dossier EICH</li>
        <li>Recommandation go / no-go</li>
        <li>Calendrier mise en œuvre</li>
      </ul>
    </div>
  </div>
</div>
<p style="margin-top:10px;font-size:13px;color:#56698a">Sortie : dossier A4 + note conseil 1 page + tableau de bord SaaS référentiel.</p>
""", "Horloge 30 jours.")

add("refuse","content","Ce que nous refusons de faire",
"""
<div class="grid">
  <div>
    <h3>Limites que nous ne franchirons pas</h3>
    <ul class="xlist">
      <li>Aucun contact patient, jamais.</li>
      <li>Aucune réutilisation alimentant la production d'eau de dialyse.</li>
      <li>Aucune réutilisation de dialysat usagé.</li>
      <li>Aucune garantie d'approbation ARS — chaque dossier est local.</li>
      <li>Aucune allégation CNAM / tarif non vérifiée.</li>
      <li>Aucune neutralité carbone — adaptation hydrique d'abord.</li>
      <li>Aucun calcul boîte noire — méthodologie publiée.</li>
      <li>Aucune recommandation de verrouillage vendeur sans preuve comparative.</li>
    </ul>
  </div>
  <div>
    <div class="banner"><b>La confiance est le coin.</b><br/>Ce que nous refusons de faire est la douve.</div>
    <div class="card"><h3>Comment cela se traduit en contrôle des allégations</h3>
      <ul>
        <li>Encadré méthodologie sur chaque rapport.</li>
        <li>Objectif, périmètre, hypothèses, incertitude. """+C('tsp')+"""</li>
        <li>Langage caveat standardisé.</li>
        <li>Liste d'allégations interdites maintenue en Annexe A16.</li>
      </ul>
    </div>
  </div>
</div>
""", "Liste de refus = douve de confiance.")

add("kpis","content","KPI &amp; critères de succès",
"""
<div class="grid4">
  <div class="kpi"><div class="v">≥ 50 %</div><div class="l">Taux de capture rejet</div><div class="s">Cible après mise en service</div></div>
  <div class="kpi"><div class="v">≥ 70 %</div><div class="l">Taux de substitution</div><div class="s">Demande non clinique couverte</div></div>
  <div class="kpi"><div class="v">&lt; 6 ans</div><div class="l">Retour</div><div class="s">Benchmark Saint-Exupéry</div></div>
  <div class="kpi"><div class="v">0</div><div class="l">Incident clinique</div><div class="s">Limite tenue</div></div>
</div>
<div class="grid" style="margin-top:14px">
  <div class="card"><h3>KPI opérationnels</h3>
    <ul>
      <li>L/séance rejet — mesuré en continu.</li>
      <li>L/séance substitué — mesuré au compteur réutilisation.</li>
      <li>kWh/séance — OI + boucle dialysat.</li>
      <li>Produit de désinfection évité.</li>
      <li>Excursions conductivité = 0.</li>
    </ul>
  </div>
  <div class="card accent"><h3>KPI dossier &amp; confiance</h3>
    <ul>
      <li>Délai au dossier (cible ≤ 60 jours).</li>
      <li>Taux d'approbation ARS.</li>
      <li>Conformité carnet sanitaire.</li>
      <li>Vérification mensuelle à l'heure.</li>
      <li>Nombre de centres labellisés EcoDialysis.</li>
    </ul>
  </div>
</div>
""", "KPI = ops, dossier, confiance.")

add("risk","content","Risque &amp; confiance — ce qui peut mal tourner, comment nous protégeons",
"""
<table>
<tr><th>Risque</th><th>Pourquoi</th><th>Mitigation</th><th>Propriétaire</th></tr>
<tr><td>Refus / retard ARS</td><td>Pas de déploiement sans dossier</td><td>Pré-dépôt précoce ; dossier EICH templatisé</td><td>EcoDialysis + direction</td></tr>
<tr><td>Biofilm / interconnexion</td><td>Sécurité patient &amp; personnel</td><td>Réseau séparé, anti-retour (EA/EB/AA), surveillance, arrêt d'urgence</td><td>Bioméd + hygiène</td></tr>
<tr><td>Inadéquation offre/demande</td><td>Boucle réutilisation vide = pas de ROI</td><td>Dimensionnement stockage + cartographie demande</td><td>EcoDialysis</td></tr>
<tr><td>Tarif faible affaiblit ROI</td><td>Eau/assainissement faible = mauvais retour</td><td>Triage site ; refus sites faible ROI ; empilement subventions</td><td>EcoDialysis</td></tr>
<tr><td>Coût rétrofit CAPEX</td><td>Dépendant de la configuration</td><td>Triage site ; option design-in (Ashford)</td><td>Hôpital + EcoDialysis</td></tr>
<tr><td>Surclamage ESG / carbone</td><td>Perte de confiance</td><td>Encadré méthodologique ; liste de refus ; caveats publiés</td><td>EcoDialysis</td></tr>
<tr><td>Perception patient / personnel</td><td>Licence sociale</td><td>Kit de communication + clarté de la limite</td><td>Direction + EcoDialysis</td></tr>
<tr><td>Verrouillage fournisseur</td><td>Risque de biais</td><td>Preuve comparative requise, specs neutres</td><td>EcoDialysis</td></tr>
</table>
<p style="margin-top:8px;font-size:12px;color:#56698a">Registre complet avec sources en Annexe A14.</p>
""", "Registre des risques.")

add("defensibility","content","Défensibilité — cinq douves composantes",
"""
<div class="grid5">
  <div class="card"><h3>Base benchmark</h3><p>Chaque audit alimente un benchmark eau/énergie spécifique France indisponible ailleurs.</p></div>
  <div class="card"><h3>Bibliothèque playbooks</h3><p>Dossiers EICH répétables raccourcissent chaque nouveau projet — marge compose.</p></div>
  <div class="card"><h3>Preuves source-labellisées</h3><p>Chaque allégation reliée par chip à une source primaire — défendable face aux consultants.</p></div>
  <div class="card"><h3>Label EcoDialysis</h3><p>Effet réseau entre directeurs de néphrologie et examinateurs ARS.</p></div>
  <div class="card dark"><h3>Scorecard fournisseurs</h3><p>Levier achats à mesure que nous nous étendons aux dispositifs et consommables.</p></div>
</div>
<div class="banner" style="margin-top:14px">EcoDialysis gagne quand chaque unité de dialyse peut dire :<br/><b>nous connaissons notre eau · nous connaissons notre voie de réutilisation sûre · nous prouvons les économies.</b></div>
""", "Cinq douves.")

add("expansion","content","Expansion future — eau d'abord, puis quatre couches",
"""
<div class="flow">
  <div class="step">1 · Eau</div><span class="arrow">›</span>
  <div class="step">2 · Énergie</div><span class="arrow">›</span>
  <div class="step">3 · Consommables</div><span class="arrow">›</span>
  <div class="step">4 · Scorecard achats</div><span class="arrow">›</span>
  <div class="step">5 · Label &amp; benchmark</div>
</div>
<div class="grid5" style="margin-top:14px">
  <div class="card"><h3>Eau</h3><p>Rejet OI, récupération chaleur, réglage Qd, désinfection.</p></div>
  <div class="card"><h3>Énergie</h3><p>Remplacement OI, échangeurs de chaleur, optimisation planning.</p></div>
  <div class="card"><h3>Consommables</h3><p>Centralisation acide concentré, scorecard dialyseur, emballages.</p></div>
  <div class="card"><h3>Achats</h3><p>Scoring durabilité fournisseurs avec logique TSP / IDMD. """+C('tsp','ird')+"""</p></div>
  <div class="card dark"><h3>Label</h3><p>EcoDialysis comme standard reconnu en néphrologie en France &amp; UE.</p></div>
</div>
""", "Cinq phases d'expansion.")

add("close","cover","",
"""
<div class="eyebrow">EcoDialysis · Paris 2026</div>
<h1>Les hôpitaux n'ont pas besoin<br/>d'un autre tableau ESG.</h1>
<p class="lead">Ils ont besoin d'un playbook opérationnel de résilience hydrique.<br/>EcoDialysis le construit — site par site, dossier par dossier, certification par certification.</p>
<div style="margin-top:32px;display:flex;gap:24px;color:#cfe1f7;font-size:15px">
  <span>Trois pilotes · six mois · un moteur répétable pour la France.</span>
</div>
<div style="margin-top:18px;font-size:13px;color:#9ec5ef;letter-spacing:1px">Adaptation d'abord · atténuation ensuite · limite non négociable</div>
""", "Clôture.")

# APPENDIX FR
add("div-appendix","divider","Annexe — bibliothèque de preuves diligence",
"""<p class="lead">23 sources extraites · 0 échec d'extraction · chaque fait clé tracé à un document primaire.</p>""", "Annexe.")

add("apx-sources","appendix","A1 · Carte des sources — 23 sources extraites, zéro échec",
"""
<table>
<tr><th>Chip</th><th>ID</th><th>Source</th><th>Type</th><th>Qualité</th></tr>
<tr><td>Per</td><td>DR-France</td><td>EcoDialysis_Perplexity.pdf (+ .docx)</td><td>Synthèse stratégie deep-research</td><td>Moyenne</td></tr>
<tr><td>Gem</td><td>DR-Tech</td><td>Clinical and Technical Advancements in Dialysis_Gemini.pdf (+ .docx)</td><td>Synthèse technique deep</td><td>Moyenne-haute</td></tr>
<tr><td>Ope</td><td>DR-Water</td><td>Water Sustainability Practices in Dialysis_OpenAI.pdf</td><td>Synthèse deep-research</td><td>Moyenne-haute</td></tr>
<tr><td>S23</td><td>SFNDT-2023</td><td>SFNDT_guide complet-VF-HD-2_260526.pdf</td><td>Guide société savante</td><td>Haute</td></tr>
<tr><td>S26</td><td>SFNDT-2026-L</td><td>Guide_des_bonnes_pratiques_en_néphrologie_verte_Ve_260526.pdf</td><td>Guide société savante (long)</td><td>Haute</td></tr>
<tr><td>S26</td><td>SFNDT-2026-S</td><td>Guide_de_la_néphrologie_verte_Version_courte_2026_260526.pdf</td><td>Guide société savante (court)</td><td>Haute</td></tr>
<tr><td>Gov</td><td>Gov-Health-Roadmap</td><td>Planification écologique du système de santé.pdf</td><td>Feuille de route gouvernementale</td><td>Haute</td></tr>
<tr><td>TSP</td><td>TSP-Health</td><td>TSP-Decarbonons-les-industries-des-medicaments-RF.pdf</td><td>Rapport The Shift Project</td><td>Haute</td></tr>
<tr><td>TSP</td><td>TSP-Pathway</td><td>[PPJS] Guide méthodologique pour l'évaluation carbone des parcours de soin.pdf</td><td>Guide méthodologique</td><td>Haute</td></tr>
<tr><td>TSP</td><td>TSP-Med</td><td>240404-Rapport-Decarbonons-lAutonomie-The-Shift-Project-1-1.pdf</td><td>Rapport</td><td>Moyenne-haute</td></tr>
<tr><td>Ird</td><td>IRDES-Sustainability</td><td>IRDES · Soutenabilité environnementale des systèmes de santé.pdf</td><td>Revue de littérature</td><td>Haute</td></tr>
<tr><td>HCW</td><td>HCWH</td><td>L'empreinte climatique du secteur de la santé Health Care Without Harm.pdf</td><td>Analyse globale ONG</td><td>Moyenne-haute</td></tr>
<tr><td>HCW</td><td>Global-Green-Health</td><td>Green health how to decarbonise global healthcare systems.pdf</td><td>Rapport global</td><td>Moyenne-haute</td></tr>
<tr><td>HCW</td><td>Climate-friendly-healthcare</td><td>Climate-friendly healthcare reducing the impacts of the healthcare sector.pdf</td><td>Rapport global</td><td>Moyenne</td></tr>
<tr><td>Pch</td><td>Pitch-v3</td><td>EcoDialysis_Pitch_v3.pptx + .pdf</td><td>Pitch interne</td><td>Haute (narratif)</td></tr>
<tr><td>Pch</td><td>Base-v1</td><td>EcoDialysis Pitch_v1.html</td><td>Base HTML interne</td><td>Style interne</td></tr>
<tr><td>—</td><td>Vendor-block</td><td>Pages corporate / réglementaires officielles</td><td>Corporate &amp; régl.</td><td>Moy-haute à Haute</td></tr>
</table>
<p style="margin-top:8px;font-size:11px;color:#56698a">Légende fiabilité — Haute : réglementation, gouvernement, société savante. Moyenne-haute : corporate officiel, pairs. Moyenne : synthèse secondaire. Faible : exclue.</p>
""", "A1 FR.")

add("apx-chips","appendix","A2 · Registre des chips sources",
"""
<div class="grid5">
  <div class="card"><h3>Per</h3><p>Deep-research marché &amp; GTM France (Perplexity).</p><a class="src" href="#src-per">Per</a></div>
  <div class="card"><h3>Gem</h3><p>Deep-research technologie (Gemini).</p><a class="src" href="#src-gem">Gem</a></div>
  <div class="card"><h3>Ope</h3><p>Deep-research durabilité eau (OpenAI).</p><a class="src" href="#src-ope">Ope</a></div>
  <div class="card"><h3>S23</h3><p>Guide SFNDT 2023 néphrologie verte.</p><a class="src" href="#src-s23">S23</a></div>
  <div class="card"><h3>S26</h3><p>Guides SFNDT 2026 long &amp; court.</p><a class="src" href="#src-s26">S26</a></div>
  <div class="card"><h3>Gov</h3><p>Planification écologique du système de santé.</p><a class="src" href="#src-gov">Gov</a></div>
  <div class="card"><h3>TSP</h3><p>The Shift Project (santé, parcours, autonomie).</p><a class="src" href="#src-tsp">TSP</a></div>
  <div class="card"><h3>Ird</h3><p>Revue littérature IRDES.</p><a class="src" href="#src-ird">Ird</a></div>
  <div class="card"><h3>HCW</h3><p>Health Care Without Harm + global green health.</p><a class="src" href="#src-hcw">HCW</a></div>
  <div class="card"><h3>Pch</h3><p>Base pitch EcoDialysis v1 / v3.</p><a class="src" href="#src-pch">Pch</a></div>
</div>
""", "A2 FR.")

add("apx-dr-water","appendix","A3 · Table DR-Water — 18 faits",
"""
<table>
<tr><th>#</th><th>Fait</th><th>Valeur</th></tr>
<tr><td>1</td><td>Récupération rejet OI Canterbury</td><td>800 L/h</td></tr>
<tr><td>2</td><td>Économie annuelle Canterbury</td><td>~7 500 £/an</td></tr>
<tr><td>3</td><td>Conception-intégrée Ashford</td><td>~2 500 £</td></tr>
<tr><td>4</td><td>Économie eau Bristol</td><td>13 140 m³/an</td></tr>
<tr><td>5</td><td>Économie annuelle Bristol</td><td>&gt; 15 000 £/an</td></tr>
<tr><td>6</td><td>Échangeurs chaleur East Kent</td><td>0,86 kWh/traitement</td></tr>
<tr><td>7</td><td>Récupération annuelle projetée East Kent</td><td>27 905 kWh/an</td></tr>
<tr><td>8</td><td>Eau agrégée économisée ANZSN</td><td>&gt; 160 000 L/an</td></tr>
<tr><td>9</td><td>Électricité agrégée économisée ANZSN</td><td>6,4 MWh/an</td></tr>
<tr><td>10</td><td>Acide citrique évité ANZSN</td><td>720 L</td></tr>
<tr><td>11</td><td>Économies produit ANZSN</td><td>~2 400 AU$</td></tr>
<tr><td>12</td><td>OI moderne AU eau / traitement</td><td>357 L (vs 548 L)</td></tr>
<tr><td>13</td><td>OI moderne AU énergie / traitement</td><td>3,1 kWh (vs 7,2 kWh)</td></tr>
<tr><td>14</td><td>Moyenne 20 centres Espagne</td><td>476,5 L/séance</td></tr>
<tr><td>15</td><td>Centres ouverts quotidiennement Espagne</td><td>430,20 L/HD · 10,82 kWh/HD</td></tr>
<tr><td>16</td><td>Centres 3×/sem. Espagne</td><td>629,81 L/HD · 16,79 kWh/HD</td></tr>
<tr><td>17</td><td>Benchmarks nommés</td><td>Bendigo · Barwon · Queen Elizabeth</td></tr>
<tr><td>18</td><td>Voie future / pilote</td><td>REDY · NeoKidney · AWAK</td></tr>
</table>
<p style="margin-top:6px;font-size:11px;color:#56698a">Chip primaire : """+C('ope')+""". Confirmation croisée : """+C('gem')+""".</p>
""", "A3 FR.")

add("apx-dr-france","appendix","A4 · Table DR-France — 12 faits",
"""
<table>
<tr><th>#</th><th>Fait</th><th>Valeur</th></tr>
<tr><td>1</td><td>Patients dialysés en France</td><td>~51 700</td></tr>
<tr><td>2</td><td>Part en centre / UDM</td><td>~77 %</td></tr>
<tr><td>3</td><td>Eau d'alimentation par séance</td><td>~400–500 L</td></tr>
<tr><td>4</td><td>Fraction rejet OI</td><td>50–70 %</td></tr>
<tr><td>5</td><td>Premiers adoptants</td><td>CHU / CHRU + grands privés</td></tr>
<tr><td>6</td><td>Établissements de santé</td><td>~2 965 (selon contexte)</td></tr>
<tr><td>7</td><td>Unités de dialyse (estim.)</td><td>~1 100–1 200</td></tr>
<tr><td>8</td><td>Centre de référence</td><td>100 patients</td></tr>
<tr><td>9</td><td>Séances / patient / an</td><td>156</td></tr>
<tr><td>10</td><td>Total séances / an</td><td>15 600</td></tr>
<tr><td>11</td><td>Hypothèse rejet / séance</td><td>270 L (bas 220 · haut 320)</td></tr>
<tr><td>12</td><td>Volume rejet de référence</td><td>~4 200 m³/an · ~1,0–1,1 tCO₂e caveat eau-seule</td></tr>
</table>
<p style="margin-top:6px;font-size:11px;color:#56698a">Chip primaire : """+C('per')+""". Caveat carbone aligné méthodologie """+C('tsp')+""".</p>
""", "A4 FR.")

add("apx-dr-tech","appendix","A5 · Table DR-Tech — 15 faits",
"""
<table>
<tr><th>#</th><th>Fait</th></tr>
<tr><td>1</td><td>Taxonomie : réutilisation · optimisation OI · désinfection · récupération chaleur</td></tr>
<tr><td>2</td><td>Soutient le benchmark multicentrique 476,5 L/séance</td></tr>
<tr><td>3</td><td>Voie architecture OI à haut taux de récupération</td></tr>
<tr><td>4</td><td>Logique de routage par conductivité pour décisions de réutilisation</td></tr>
<tr><td>5</td><td>Consolide les preuves Canterbury / Ashford / Bristol</td></tr>
<tr><td>6</td><td>Confirme la logique d'optimisation désinfection ANZSN</td></tr>
<tr><td>7</td><td>Cas de récupération chaleur (East Kent, Newcastle)</td></tr>
<tr><td>8</td><td>Distingue voies non cliniques à faible risque vs voies à plus haut risque</td></tr>
<tr><td>9</td><td>Systèmes sorbants / portables comme voie émergente</td></tr>
<tr><td>10</td><td>Statut pilote NeoKidney et AWAK</td></tr>
<tr><td>11</td><td>Barrières coût rétrofit et gouvernance identifiées</td></tr>
<tr><td>12</td><td>Recommande une feuille de route à étapes</td></tr>
<tr><td>13</td><td>Renforce métrologie et contrôles de procédé</td></tr>
<tr><td>14</td><td>Positionne la réutilisation du dialysat usagé comme non-première-vague</td></tr>
<tr><td>15</td><td>Soutient une stratification par niveau de preuve</td></tr>
</table>
<p style="margin-top:6px;font-size:11px;color:#56698a">Chip primaire : """+C('gem')+""". Renforce la matrice de maturité A13.</p>
""", "A5 FR.")

add("apx-s23","appendix","A6 · SFNDT 2023 — cadre néphrologie verte",
"""
<table>
<tr><th>#</th><th>Insight</th></tr>
<tr><td>1</td><td>Cadre d'action structuré néphrologie verte</td></tr>
<tr><td>2</td><td>Leviers eau · énergie · déchets intégrés</td></tr>
<tr><td>3</td><td>Gouvernance et appropriation d'équipe soulignées</td></tr>
<tr><td>4</td><td>Formation et culture de mise en œuvre centrales</td></tr>
<tr><td>5</td><td>Orientation achats et cycle de vie</td></tr>
<tr><td>6</td><td>Transition opérationnelle attentive aux risques</td></tr>
<tr><td>7</td><td>Hiérarchie de réduction empreinte dialyse</td></tr>
<tr><td>8</td><td>Logique mesure d'abord (correspond à l'architecture EcoDialysis)</td></tr>
<tr><td>9</td><td>Approche amélioration continue</td></tr>
<tr><td>10</td><td>Co-cadrage qualité-sécurité de la durabilité</td></tr>
<tr><td>11</td><td>Suivi multi-domaines</td></tr>
<tr><td>12</td><td>Base de listes de contrôle actionnables</td></tr>
</table>
<p style="margin-top:6px;font-size:11px;color:#56698a">Chip primaire : """+C('s23')+""". Ancrage crédibilité clinique.</p>
""", "A6 FR.")

add("apx-s26","appendix","A7 · SFNDT 2026 guide long — 20 faits opérationnels",
"""
<table>
<tr><th>#</th><th>Fait</th><th>Quantité si dispo</th></tr>
<tr><td>1</td><td>Fiches-actions détaillées dialyse &amp; néphrologie</td><td>—</td></tr>
<tr><td>2</td><td>Voie réduction Qd avec économies / séance quantifiées</td><td>voir #3, #4</td></tr>
<tr><td>3</td><td>Économies dialysat 500→400 ml/min</td><td><b>~24 L/séance</b></td></tr>
<tr><td>4</td><td>Économie eau prétraitée dans le même contexte</td><td><b>~60–100 L/séance</b></td></tr>
<tr><td>5</td><td>Contexte évaluation Qd multicentrique française</td><td>—</td></tr>
<tr><td>6</td><td>Optimisation HDF &amp; compromis volume dialysat</td><td>—</td></tr>
<tr><td>7</td><td>Distribution centralisée acide concentré</td><td>déchets + conso ↓</td></tr>
<tr><td>8</td><td>Section dédiée réutilisation rejet OI</td><td>—</td></tr>
<tr><td>9</td><td>Cas français : Clinique Saint-Exupéry Toulouse</td><td>—</td></tr>
<tr><td>10</td><td>Économie Saint-Exupéry rapportée</td><td><b>~1 128 m³/an</b></td></tr>
<tr><td>11</td><td>Investissement / retour Saint-Exupéry</td><td><b>~30 k€ · 5–6 ans</b></td></tr>
<tr><td>12</td><td>AP-HM Marseille études potentiel plus large</td><td>—</td></tr>
<tr><td>13</td><td>Contraintes pratiques stockage (durée, temp, distance)</td><td>—</td></tr>
<tr><td>14</td><td>Exigences réseau séparé</td><td>—</td></tr>
<tr><td>15</td><td>Pas de saut direct vers réutilisation à haut risque</td><td>limite</td></tr>
<tr><td>16</td><td>Obligations de gestion énergétique</td><td>—</td></tr>
<tr><td>17</td><td>Voies de réduction des déchets</td><td>—</td></tr>
<tr><td>18</td><td>Actions personnel / organisationnelles</td><td>—</td></tr>
<tr><td>19</td><td>Logique RSE et communication</td><td>—</td></tr>
<tr><td>20</td><td>Réutilisable comme playbook de mise en œuvre</td><td>—</td></tr>
</table>
<p style="margin-top:6px;font-size:11px;color:#56698a">Chip primaire : """+C('s26')+""". Correspondance la plus proche du playbook opérationnel EcoDialysis.</p>
""", "A7 FR.")

add("apx-gov","appendix","A8 · Gouvernement / réglementation — EICH &amp; Décret 2024-796",
"""
<div class="grid">
  <div>
    <h3>Décret n°2024-796 · en vigueur 1er sept. 2024</h3>
    <div class="card"><ul>
      <li>Cadre EICH = Eaux Impropres à la Consommation Humaine.</li>
      <li>Couvre les établissements sensibles dont la santé.</li>
      <li>Autorise la réutilisation non clinique sous dossier ARS / préfecture.</li>
      <li>Réseau séparé obligatoire.</li>
      <li>Dispositifs anti-retour requis.</li>
      <li>Programme de signalisation requis.</li>
      <li>Entrées au carnet sanitaire requises.</li>
      <li>Plan de surveillance &amp; maintenance requis.</li>
      <li>Arrêt d'urgence et bascule vers potable requis.</li>
      <li>Aucune réutilisation à contact patient autorisée.</li>
    </ul></div>
  </div>
  <div>
    <h3>Carte des parties prenantes</h3>
    <div class="card accent"><ul>
      <li><b>ARS</b> — validation autorité santé.</li>
      <li><b>Préfecture</b> — autorisation administrative.</li>
      <li><b>Agence de l'Eau</b> — co-financement par bassin.</li>
      <li><b>CLIN / hygiène</b> — comité interne de sécurité.</li>
      <li><b>Direction</b> — sponsor administratif.</li>
      <li><b>Services techniques + bioméd</b> — propriétaires opérationnels.</li>
      <li><b>Médical + néphrologie</b> — validation clinique.</li>
    </ul></div>
    <p style="font-size:11px;color:#56698a">Incertitudes restantes (A16) : voie ARS exacte par bassin · fréquence surveillance · interaction tarifaire · éligibilité Agence de l'Eau · catégorie CEE. Sources : """+C('gov','s26')+"""</p>
  </div>
</div>
""", "A8 FR.")

add("apx-decarb","appendix","A9 · Contexte décarbonation système de santé — pourquoi l'eau est adaptation d'abord",
"""
<div class="grid">
  <div class="card"><h3>Contexte macro</h3>
    <ul>
      <li>Santé &gt; 8 % de l'empreinte GES nationale. """+C('gov','hcw')+"""</li>
      <li>~50 MtCO₂e ordre de grandeur.</li>
      <li>Offre de soins ~45 % · médicaments &amp; produits ~55 %.</li>
      <li>Scope 3 achats domine.</li>
    </ul>
  </div>
  <div class="card"><h3>Axes feuille de route</h3>
    <ul>
      <li>Bâtiments &amp; énergie</li>
      <li>Industries / produits</li>
      <li>Achats durables</li>
      <li>Soins éco-responsables</li>
      <li>Déchets · transport · numérique · formation</li>
    </ul>
    <p style="font-size:11px;color:#56698a">Source : """+C('gov')+""" Planification écologique.</p>
  </div>
  <div class="card accent"><h3>Pourquoi l'eau est adaptation d'abord</h3>
    <ul>
      <li>La résilience hydrique est un enjeu de continuité, pas une métrique ESG.</li>
      <li>Tarif &amp; raréfaction touchent l'OPEX immédiatement.</li>
      <li>Poids carbone de l'eau réel mais secondaire (1,0–1,1 tCO₂e sur 4 200 m³). """+C('per','tsp')+"""</li>
      <li>Dispositifs médicaux &amp; consommables comptent pour le Scope 3 — adressés en Phase 3 EcoDialysis.</li>
      <li>Cadrage résilience système aligné TSP &amp; IRDES. """+C('tsp','ird')+"""</li>
    </ul>
  </div>
</div>
""", "A9 FR.")

add("apx-equip","appendix","A10 · Écosystème équipement — environnemental, données, intervention, limite",
"""
<table>
<tr><th>Couche</th><th>Enjeu environnemental</th><th>Données requises</th><th>Intervention</th><th>Limite</th><th>Propriétaire</th></tr>
<tr><td>Générateur dialyse</td><td>Réglage énergie + eau</td><td>Séances/machine, paramètres Qd</td><td>Réduction Qd, réglage HDF</td><td>Validation clinique</td><td>Bioméd + néphro</td></tr>
<tr><td>Centrale eau</td><td>Volume rejet</td><td>Débits entrée, perméat, rejet</td><td>OI moderne, routage conductivité</td><td>Validation vendeur</td><td>Services techniques</td></tr>
<tr><td>Skid OI</td><td>L+kWh / traitement</td><td>Âge, modèle, performance</td><td>Remplacement / rétrofit</td><td>Vendeur</td><td>Bioméd</td></tr>
<tr><td>Prétraitement</td><td>Chimie, contre-lavage</td><td>Cycles changement filtres</td><td>Optimisation, OI à récupération</td><td>Vendeur</td><td>Bioméd</td></tr>
<tr><td>Boucle dialysat</td><td>Cycles désinfection</td><td>Fréquence citrique / chaleur</td><td>Optimisation, réduction chimie</td><td>Validation vendeur</td><td>Bioméd + hygiène</td></tr>
<tr><td>Membranes dialyseur</td><td>Déchet à usage unique</td><td>Scorecard fournisseur</td><td>Scoring achats (Phase 3)</td><td>Clinique</td><td>Direction + médical</td></tr>
<tr><td>Lignes / aiguilles / cathéters</td><td>Déchet à usage unique</td><td>Volume + fournisseur</td><td>Emballage + achats</td><td>Clinique</td><td>Pharma + achats</td></tr>
<tr><td>Acide concentré</td><td>Logistique + emballage</td><td>Local vs central</td><td>Distribution centralisée """+C('s26')+"""</td><td>Hygiène</td><td>Services techniques</td></tr>
<tr><td>Bicarbonate</td><td>Déchet cartouche</td><td>Consommation / séance</td><td>Scorecard achats</td><td>Clinique</td><td>Pharma</td></tr>
<tr><td>Soluté / désinfectants</td><td>Chimie</td><td>Volumes</td><td>Optimisation</td><td>Hygiène</td><td>Pharma + hygiène</td></tr>
<tr><td>Emballages</td><td>Carton / plastique</td><td>Audit fournisseur</td><td>Scorecard achats</td><td>Logistique</td><td>Achats</td></tr>
<tr><td>Déchets DASRI / DAOM</td><td>Flux fort carbone</td><td>Taux de tri</td><td>Tri + réduction """+C('ird')+"""</td><td>Hygiène</td><td>Services généraux</td></tr>
<tr><td>Capteurs / compteurs</td><td>—</td><td>Inventaire</td><td>Pose 4 points</td><td>—</td><td>EcoDialysis</td></tr>
<tr><td>Cuves / pompes</td><td>Matériel réutilisation</td><td>Profil demande</td><td>Dimensionnement</td><td>Ingénierie</td><td>Intégrateur</td></tr>
<tr><td>UV-C</td><td>Polissage réutilisation</td><td>Débit + microbio</td><td>Boucle réutilisation en ligne</td><td>Vendeur</td><td>Intégrateur</td></tr>
<tr><td>Anti-retour</td><td>Risque interconnexion</td><td>Plan réseau</td><td>EA/EB/AA selon usage</td><td>Réglementaire</td><td>Plomberie + hygiène</td></tr>
</table>
""", "A10 FR.")

add("apx-supp","appendix","A11 · Paysage fournisseurs (vérifier pertinence locale)",
"""
<table>
<tr><th>Société</th><th>Catégorie</th><th>Produits</th><th>Levier EcoDialysis</th><th>Caveat</th></tr>
<tr><td>Fresenius Medical Care</td><td>Générateur + OI + dialyseur</td><td>5008/6008, AquaA/AquaB, dialyseurs, NxStage</td><td>OI moderne, réglage générateur, achats</td><td>Neutralité vendeur requise</td></tr>
<tr><td>B. Braun</td><td>Générateur + eau</td><td>Dialog, AQUAboss</td><td>Centrale eau, réutilisation rejet</td><td>—</td></tr>
<tr><td>Baxter / Vantive</td><td>Générateur + DP</td><td>Artis, série AK ; DP</td><td>Réglage générateur</td><td>Spin-off récent</td></tr>
<tr><td>Nipro</td><td>Générateur + dialyseur</td><td>Surdial, dialyseurs</td><td>Scorecard achats</td><td>Présence UE variable</td></tr>
<tr><td>Nikkiso</td><td>Générateur</td><td>DBB-EXA, systèmes eau</td><td>Réglage générateur</td><td>—</td></tr>
<tr><td>Asahi Kasei Medical</td><td>Dialyseur</td><td>Membranes</td><td>Achats</td><td>—</td></tr>
<tr><td>Toray</td><td>Dialyseur</td><td>Membranes</td><td>Achats</td><td>—</td></tr>
<tr><td>JMS</td><td>Dialyseur + lignes</td><td>Produits</td><td>Achats</td><td>Présence régionale</td></tr>
<tr><td>Quanta</td><td>Générateur</td><td>SC+ portable</td><td>Nouvel entrant low-water</td><td>Échelle pilote</td></tr>
<tr><td>Outset / Tablo</td><td>Générateur</td><td>Tablo</td><td>Alternative eau-légère</td><td>US-centré</td></tr>
<tr><td>NextKidney (NeoKidney)</td><td>Futur</td><td>Portable</td><td>Veille &amp; pilote</td><td>Pré-déploiement</td></tr>
<tr><td>AWAK</td><td>Futur</td><td>Sorbant</td><td>Veille &amp; pilote</td><td>Pré-déploiement</td></tr>
<tr><td>Endress+Hauser / Siemens</td><td>Métrologie / IoT</td><td>Débit, conductivité</td><td>Couche données SaaS</td><td>—</td></tr>
<tr><td>Veolia / Suez</td><td>Eau &amp; déchets</td><td>Exploitant</td><td>Matériel réutilisation, audit déchets</td><td>Risque biais → neutralité</td></tr>
<tr><td>SNITEM / C2DS / AFNOR SPEC 2313</td><td>Cadre achats</td><td>IDMD</td><td>Alignement scorecard</td><td>—</td></tr>
</table>
""", "A11 FR.")

add("apx-fin","appendix","A12 · Modèle financier — scénarios &amp; sensibilités",
"""
<div class="grid">
  <div>
    <h3>Scénario rejet × taux de capture</h3>
    <table>
      <tr><th>Rejet</th><th>m³/an</th><th>Capture 50 %</th><th>70 %</th><th>90 %</th></tr>
      <tr><td>Bas 220 L</td><td>3 432</td><td>1 716</td><td>2 402</td><td>3 089</td></tr>
      <tr><td>Central 270 L</td><td>4 212</td><td>2 106</td><td>2 948</td><td>3 791</td></tr>
      <tr><td>Haut 320 L</td><td>4 992</td><td>2 496</td><td>3 494</td><td>4 493</td></tr>
    </table>
    <p style="font-size:11px;color:#56698a">Tous chiffres m³/an pour le centre de référence 100 patients. """+C('per')+"""</p>
  </div>
  <div>
    <h3>Sensibilité tarif &amp; retour</h3>
    <table>
      <tr><th>Eau + assain. €/m³</th><th>Économie @ 2 948 m³</th><th>Retour indicatif @ 30 k€</th></tr>
      <tr><td>2,50</td><td>~7 400 €/an</td><td>~4 ans</td></tr>
      <tr><td>3,50</td><td>~10 300 €/an</td><td>~3 ans</td></tr>
      <tr><td>5,00</td><td>~14 700 €/an</td><td>~2 ans</td></tr>
    </table>
    <p style="font-size:11px;color:#56698a">Ancrage Saint-Exupéry : ~1 128 m³, ~30 k€, retour 5–6 ans. """+C('s26')+"""</p>
  </div>
</div>
<div class="grid" style="margin-top:12px">
  <div class="card"><h3>Ce qui ne peut pas être quantifié</h3>
    <ul>
      <li>Catégorie CEE exacte et équivalence €/MWh pour réutilisation eau.</li>
      <li>Co-financement Agence de l'Eau par bassin et projet.</li>
      <li>Impact tarif CNAM (aucun supposé — caveat requis).</li>
      <li>Éligibilité crédit carbone (non revendiquée).</li>
    </ul>
  </div>
  <div class="card accent"><h3>Règle de décision</h3>
    <ul>
      <li>Refuser sites avec tarif &lt; 1,80 €/m³ sauf subvention ou risque pénurie.</li>
      <li>Préférer design-in au rétrofit quand fenêtre ouverte (modèle Ashford).</li>
      <li>Coupler réutilisation avec remplacement OI quand OI &gt; 10 ans.</li>
    </ul>
  </div>
</div>
""", "A12 FR.")

add("apx-mat","appendix","A13 · Matrice complète de maturité technologique",
"""
<table>
<tr><th>Levier</th><th>Maturité</th><th>Preuve</th><th>Eau</th><th>Énergie</th><th>Déchets</th><th>Capex</th><th>Régl.</th><th>Phase</th></tr>
<tr><td>Rejet OI non clinique</td><td><span class="tag-ok">Prêt</span></td><td>UK + AU + ES</td><td>+++</td><td>0</td><td>+</td><td>Moy</td><td>Dossier EICH</td><td>1</td></tr>
<tr><td>Remplacement OI moderne</td><td><span class="tag-ok">Prêt</span></td><td>Mesure AU</td><td>+++</td><td>+++</td><td>+</td><td>Élevé</td><td>Vendeur</td><td>1</td></tr>
<tr><td>Récupération chaleur</td><td><span class="tag-ok">Prêt</span></td><td>East Kent</td><td>0</td><td>++</td><td>0</td><td>Moy</td><td>Ing.</td><td>2</td></tr>
<tr><td>Optimisation désinfection</td><td><span class="tag-ok">Prêt</span></td><td>ANZSN</td><td>++</td><td>+</td><td>++</td><td>Faible</td><td>Vendeur</td><td>1</td></tr>
<tr><td>Réutilisation routée conductivité</td><td><span class="tag-warn">Site</span></td><td>Synthèse tech</td><td>++</td><td>0</td><td>0</td><td>Faible</td><td>Ing.</td><td>1–2</td></tr>
<tr><td>OI à récupération prétraitement</td><td><span class="tag-warn">Site</span></td><td>Synthèse tech</td><td>++</td><td>−</td><td>0</td><td>Moy</td><td>Vendeur</td><td>2</td></tr>
<tr><td>Réduction Qd (500→400)</td><td><span class="tag-warn">Site</span></td><td>SFNDT 2026</td><td>++</td><td>+</td><td>+</td><td>Faible</td><td>Clinique</td><td>2</td></tr>
<tr><td>Réglage volume HDF</td><td><span class="tag-warn">Site</span></td><td>SFNDT 2026</td><td>+</td><td>0</td><td>0</td><td>Faible</td><td>Clinique</td><td>2</td></tr>
<tr><td>Acide concentré centralisé</td><td><span class="tag-warn">Site</span></td><td>SFNDT 2026</td><td>+</td><td>+</td><td>++</td><td>Moy</td><td>Hygiène</td><td>2</td></tr>
<tr><td>Forme planning (quotidien vs 3×/sem)</td><td><span class="tag-warn">Site</span></td><td>Espagne</td><td>+++</td><td>+++</td><td>0</td><td>Faible</td><td>Clinique</td><td>2</td></tr>
<tr><td>Réutilisation toilettes</td><td><span class="tag-ok">Prêt</span></td><td>UK</td><td>++</td><td>0</td><td>0</td><td>Faible</td><td>EICH</td><td>1</td></tr>
<tr><td>Nettoyage &amp; extérieur</td><td><span class="tag-ok">Prêt</span></td><td>UK</td><td>+</td><td>0</td><td>0</td><td>Faible</td><td>EICH</td><td>1</td></tr>
<tr><td>Appoint CTA</td><td><span class="tag-warn">Site</span></td><td>Industrie</td><td>++</td><td>0</td><td>0</td><td>Moy</td><td>Ing.</td><td>2</td></tr>
<tr><td>Prélavage blanchisserie</td><td><span class="tag-warn">Site</span></td><td>Inter-secteur</td><td>++</td><td>0</td><td>0</td><td>Moy</td><td>EICH</td><td>2</td></tr>
<tr><td>Alim. stérilisation (non-final)</td><td><span class="tag-warn">Site</span></td><td>Inter-secteur</td><td>+</td><td>0</td><td>0</td><td>Moy</td><td>EICH + hygiène</td><td>2</td></tr>
<tr><td>Sorbant / portable</td><td><span class="tag-bad">Pilote</span></td><td>R&amp;D vendeurs</td><td>+++</td><td>+</td><td>+</td><td>—</td><td>Élevé</td><td>Veille</td></tr>
<tr><td>NeoKidney portable</td><td><span class="tag-bad">Pilote</span></td><td>R&amp;D vendeurs</td><td>+++</td><td>+</td><td>+</td><td>—</td><td>Élevé</td><td>Veille</td></tr>
<tr><td>Réutilisation dialysat usagé</td><td><span class="tag-bad">Limite</span></td><td>—</td><td>n/a</td><td>n/a</td><td>n/a</td><td>—</td><td>Interdit</td><td>Jamais</td></tr>
</table>
""", "A13 FR.")

add("apx-risk","appendix","A14 · Registre des risques",
"""
<table>
<tr><th>Risque</th><th>Pourquoi</th><th>Mitigation</th><th>Propriétaire</th><th>Preuve</th></tr>
<tr><td>Refus / retard ARS</td><td>Pas de réutilisation sans dossier</td><td>Pré-dépôt, dossier EICH templatisé, jurisprudence</td><td>EcoDialysis + direction</td><td>"""+C('gov','s26')+"""</td></tr>
<tr><td>Biofilm / infection</td><td>Sécurité patient</td><td>Polissage UV-C, anti-stagnation, surveillance</td><td>Bioméd + hygiène</td><td>"""+C('s26','gem')+"""</td></tr>
<tr><td>Interconnexion</td><td>Contamination potable</td><td>Réseau séparé, anti-retour EA/EB/AA, signalisation</td><td>Plomberie + hygiène</td><td>"""+C('gov')+"""</td></tr>
<tr><td>Excursion conductivité</td><td>Dérive qualité réutilisation</td><td>Routage en ligne vers égout</td><td>Bioméd</td><td>"""+C('gem')+"""</td></tr>
<tr><td>Inadéquation offre/demande</td><td>Boucle vide</td><td>Dimensionnement stockage, cartographie demande</td><td>EcoDialysis</td><td>"""+C('s26','ope')+"""</td></tr>
<tr><td>Dérapage CAPEX rétrofit</td><td>Risque ROI</td><td>Triage site, option design-in (Ashford)</td><td>Direction + EcoDialysis</td><td>"""+C('ope')+"""</td></tr>
<tr><td>Tarif faible affaiblit ROI</td><td>Retour &gt; 7 ans</td><td>Triage site, empilement subventions</td><td>EcoDialysis</td><td>"""+C('per')+"""</td></tr>
<tr><td>Retards achats</td><td>Mois ajoutés</td><td>Accords-cadres, voie GHT</td><td>Direction</td><td>—</td></tr>
<tr><td>Surclamage ESG / carbone</td><td>Réputation</td><td>Encadré méthodologie, liste de contrôle</td><td>EcoDialysis</td><td>"""+C('tsp')+"""</td></tr>
<tr><td>Perception patient / personnel</td><td>Licence sociale</td><td>Kit communication, clarté de limite</td><td>Direction</td><td>"""+C('s26')+"""</td></tr>
<tr><td>Partage propriété</td><td>Dérive opérationnelle</td><td>RACI par site, contrats</td><td>EcoDialysis</td><td>—</td></tr>
<tr><td>Verrouillage fournisseur</td><td>Risque biais</td><td>Specs neutres, preuve comparative</td><td>EcoDialysis</td><td>"""+C('tsp')+"""</td></tr>
</table>
""", "A14 FR.")

add("apx-pilot","appendix","A15 · Annexe mise en œuvre pilote — semaine par semaine",
"""
<table>
<tr><th>Semaine</th><th>Phase</th><th>Livrables</th><th>Données hôpital</th><th>Approbations</th></tr>
<tr><td>0</td><td>Mobilisation</td><td>Kick-off, NDA, lettre sponsor</td><td>Org chart, contacts</td><td>Direction</td></tr>
<tr><td>1–2</td><td>Audit site</td><td>Visite, revue plans, inventaire OI</td><td>Plans, journaux OI, 12 mois factures</td><td>Services techniques</td></tr>
<tr><td>2–3</td><td>Pose métrologie</td><td>4 compteurs + conductivité</td><td>Accès plomberie</td><td>Bioméd + hygiène</td></tr>
<tr><td>3–7</td><td>Référentiel</td><td>Enregistrement continu, cartographie demande</td><td>Planning séances</td><td>—</td></tr>
<tr><td>7–9</td><td>Conception scénarios</td><td>Carte vert/orange/rouge, dimensionnement, ROI</td><td>Tarifs</td><td>Direction + technique</td></tr>
<tr><td>9–12</td><td>Brouillon dossier</td><td>Dossier EICH, analyse risque, chaîne de validation</td><td>—</td><td>Hygiène + direction</td></tr>
<tr><td>12–14</td><td>Pré-instruction ARS</td><td>Revue informelle</td><td>—</td><td>ARS</td></tr>
<tr><td>14–18</td><td>Mise en œuvre</td><td>Plomberie, cuve, UV-C, anti-retour, SaaS</td><td>Accès site</td><td>CLIN, ARS final</td></tr>
<tr><td>18–20</td><td>Mise en service</td><td>Tests, formation, signalisation</td><td>Temps personnel</td><td>Bioméd + hygiène</td></tr>
<tr><td>20–24</td><td>Vérification</td><td>Rapports mensuels, bundle KPI</td><td>—</td><td>Direction + finance</td></tr>
</table>
""", "A15 FR.")

add("apx-claims","appendix","A16 · Contrôle des allégations — autorisées vs interdites",
"""
<div class="grid">
  <div>
    <h3>Allégations autorisées</h3>
    <ul class="checklist">
      <li>« X m³ de rejet OI captés ce mois (compteur M3). »</li>
      <li>« Y m³ substitués en usages non cliniques (compteur M4). »</li>
      <li>« Z € économisés selon vérification des factures locales. »</li>
      <li>« N cycles de désinfection réduits — chimie évitée. »</li>
      <li>« Dossier conforme EICH déposé à l'ARS le [date]. »</li>
      <li>« Carnet sanitaire à jour ; zéro excursion de conductivité. »</li>
      <li>« X kWh économisés par remplacement OI (mesuré). »</li>
    </ul>
  </div>
  <div>
    <h3>Allégations interdites</h3>
    <ul class="xlist">
      <li>« Neutre carbone » — jamais.</li>
      <li>« Impact zéro » — jamais.</li>
      <li>« Approuvé ARS sur chaque site » — décision locale.</li>
      <li>« Eau patient réutilisée » — jamais.</li>
      <li>« Dialysat usagé recyclé » — jamais.</li>
      <li>« Équivalent à X voitures hors route » sans divulgation méthodo TSP.</li>
      <li>« Éligible CEE / Agence de l'Eau » sans confirmation écrite.</li>
      <li>« Économise N € à l'hôpital » sans vérification factures.</li>
    </ul>
  </div>
</div>
<p style="margin-top:8px;font-size:11px;color:#56698a">Encadré méthodologie obligatoire sur chaque rapport : objectif, périmètre, hypothèses, incertitude, qualité données, caveats. """+C('tsp')+"""</p>
""", "A16 FR.")

add("apx-sources-registry","appendix","Annexe I · Registre complet des sources (ancres chips)",
"""
<div class="cols2" style="height:780px">
  <p id="src-per"><a class="src">Per</a> <b>DR-France · Perplexity</b><br/>EcoDialysis_Perplexity.pdf (+ .docx) — marché France, ~51 700 patients, 77 % en centre/UDM, modèle de référence. Qualité : Moyenne.</p>
  <p id="src-gem"><a class="src">Gem</a> <b>DR-Tech · Gemini</b><br/>Clinical and Technical Advancements in Dialysis_Gemini.pdf (+ .docx) — taxonomie technologique, routage conductivité, support matrice maturité. Qualité : Moyenne-haute.</p>
  <p id="src-ope"><a class="src">Ope</a> <b>DR-Water · OpenAI</b><br/>Water Sustainability Practices in Dialysis_OpenAI.pdf — Canterbury, Bristol, Ashford, East Kent, ANZSN, OI moderne vs ancienne AU, 20 centres Espagne. Qualité : Moyenne-haute.</p>
  <p id="src-s23"><a class="src">S23</a> <b>SFNDT 2023</b><br/>SFNDT_guide complet-VF-HD-2_260526.pdf — cadre néphrologie verte, mesure d'abord, gouvernance. Qualité : Haute.</p>
  <p id="src-s26"><a class="src">S26</a> <b>SFNDT 2026</b><br/>Guide_des_bonnes_pratiques_en_néphrologie_verte_Ve_260526.pdf + Guide_de_la_néphrologie_verte_Version_courte_2026_260526.pdf — économies Qd, cas Saint-Exupéry, AP-HM, playbook réutilisation rejet OI. Qualité : Haute.</p>
  <p id="src-gov"><a class="src">Gov</a> <b>Gouvernement / réglementation</b><br/>Planification écologique du système de santé.pdf + Décret n°2024-796 (12 juillet 2024, en vigueur 1er sept. 2024, EICH). Qualité : Haute.</p>
  <p id="src-tsp"><a class="src">TSP</a> <b>The Shift Project</b><br/>TSP-Decarbonons-les-industries-des-medicaments-RF.pdf · [PPJS] Guide méthodologique pour l'évaluation carbone des parcours de soin.pdf · 240404-Rapport-Decarbonons-lAutonomie-The-Shift-Project-1-1.pdf. Qualité : Haute.</p>
  <p id="src-ird"><a class="src">Ird</a> <b>IRDES</b><br/>La soutenabilité environnementale des systèmes de santé. Une revue de littérature sur l'empreinte écologique des systèmes de santé. Qualité : Haute.</p>
  <p id="src-hcw"><a class="src">HCW</a> <b>Health Care Without Harm + Global Green Health</b><br/>L'empreinte climatique du secteur de la santé Health Care Without Harm.pdf + Green health how to decarbonise global healthcare systems.pdf + Climate-friendly healthcare reducing the impacts of the healthcare sector on the world's climate.pdf. Qualité : Moyenne-haute.</p>
  <p id="src-pch"><a class="src">Pch</a> <b>Base pitch</b><br/>EcoDialysis_Pitch_v3.pptx + EcoDialysis-Pitch_v3.pdf + EcoDialysis Pitch_v1.html — narratif interne, positionnement, ossature GTM. Qualité : Haute (narratif), base style interne.</p>
</div>
""", "Ancres sources FR.")

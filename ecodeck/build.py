#!/usr/bin/env python3
import sys, os, json
sys.path.insert(0, '/tmp/ecodeck')
from style_js import CSS, JS
from content_en import SLIDES_EN
from content_fr import SLIDES_FR

PART_MAP_EN = {
  "title":"Cover","agenda":"Agenda","why-now":"Part 1 · Hook","why-dialysis":"Part 1 · Hook","what-wasted":"Part 1 · Hook",
  "div-measure":"Part 2","measure":"Part 2 · Measurement","reference":"Part 2 · Reference site","reuse-map":"Part 2 · Reuse map",
  "legal-eich":"Part 2 · Regulation","dossier":"Part 2 · Dossier","tailored":"Part 2 · Tailored fit",
  "div-proof":"Part 3","intl-map":"Part 3 · Proof","uk-cluster":"Part 3 · UK","anz-cluster":"Part 3 · ANZ",
  "optim":"Part 3 · Optimisation","fr-proof":"Part 3 · France",
  "div-product":"Part 4","not-tank":"Part 4 · Product","product":"Part 4 · Product","ecosystem":"Part 4 · Equipment",
  "maturity":"Part 4 · Maturity","business":"Part 4 · Business","buyers":"Part 4 · Buyers",
  "div-ask":"Part 5","pilots":"Part 5 · Pilots","need":"Part 5 · Need","deliver":"Part 5 · Delivery",
  "refuse":"Part 5 · Discipline","kpis":"Part 5 · KPIs","risk":"Part 5 · Risk",
  "defensibility":"Part 5 · Moat","expansion":"Part 5 · Expansion","close":"Close",
}
PART_MAP_FR = {
  "title":"Couverture","agenda":"Sommaire","why-now":"Partie 1 · Accroche","why-dialysis":"Partie 1 · Accroche","what-wasted":"Partie 1 · Accroche",
  "div-measure":"Partie 2","measure":"Partie 2 · Mesure","reference":"Partie 2 · Site de référence","reuse-map":"Partie 2 · Carte réutilisation",
  "legal-eich":"Partie 2 · Réglementation","dossier":"Partie 2 · Dossier","tailored":"Partie 2 · Sur mesure",
  "div-proof":"Partie 3","intl-map":"Partie 3 · Preuves","uk-cluster":"Partie 3 · UK","anz-cluster":"Partie 3 · ANZ",
  "optim":"Partie 3 · Optimisation","fr-proof":"Partie 3 · France",
  "div-product":"Partie 4","not-tank":"Partie 4 · Produit","product":"Partie 4 · Produit","ecosystem":"Partie 4 · Équipement",
  "maturity":"Partie 4 · Maturité","business":"Partie 4 · Modèle","buyers":"Partie 4 · Acheteurs",
  "div-ask":"Partie 5","pilots":"Partie 5 · Pilotes","need":"Partie 5 · Besoin","deliver":"Partie 5 · Livraison",
  "refuse":"Partie 5 · Discipline","kpis":"Partie 5 · KPIs","risk":"Partie 5 · Risque",
  "defensibility":"Partie 5 · Défense","expansion":"Partie 5 · Expansion","close":"Clôture",
}

def render(slides, lang, title, brand, part_map):
    notes = {}
    secs = []
    total = len(slides)
    for i,(sid,kind,t,body,nt) in enumerate(slides):
        idx = i+1
        part = part_map.get(sid, "Appendix" if lang=="en" else "Annexe") if kind!="appendix" else ("Appendix" if lang=="en" else "Annexe")
        if sid.startswith("apx-") or sid=="div-appendix":
            part = "Appendix" if lang=="en" else "Annexe"
        title_html = f'<h1>{t}</h1>' if kind in ("content","appendix","divider") else f'<h1 class="cover-title">{t}</h1>'
        secs.append(f'''<section class="slide {kind}" id="slide-{sid}" data-idx="{idx}">
  <div class="slide-inner">
    {title_html}
    <div class="body">{body}</div>
  </div>
  <footer class="sfoot"><span class="brand">{brand}</span><span class="part">{part}</span><span class="cnt-foot">{idx} / {total}</span></footer>
</section>''')
        notes[f"slide-{sid}"] = nt or ""
    nav = '''<div class="nav"><button id="prev" aria-label="Previous">‹</button><span id="cnt">1 / %d</span><button id="next" aria-label="Next">›</button></div><div class="progress"><div id="prog"></div></div>''' % total
    html = f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><style>{CSS}</style></head><body>
<div class="stage"><div class="deck" id="deck">{''.join(secs)}</div></div>
{nav}
<script type="application/json" id="speaker-notes">{json.dumps(notes,ensure_ascii=False)}</script>
<script>{JS}</script>
</body></html>'''
    return html

OUT = "/home/victor/_aprojects/EcoDialysis"
open(f"{OUT}/EcoDialysis_Final_Pitch_EN.html","w",encoding="utf-8").write(
    render(SLIDES_EN,"en","EcoDialysis — Final Pitch (EN)","EcoDialysis · ANDCS × MIT Hacking Medicine · Paris 2026", PART_MAP_EN))
open(f"{OUT}/EcoDialysis_Final_Pitch_FR.html","w",encoding="utf-8").write(
    render(SLIDES_FR,"fr","EcoDialysis — Pitch Final (FR)","EcoDialysis · ANDCS × MIT Hacking Medicine · Paris 2026", PART_MAP_FR))
print("EN bytes:", os.path.getsize(f"{OUT}/EcoDialysis_Final_Pitch_EN.html"))
print("FR bytes:", os.path.getsize(f"{OUT}/EcoDialysis_Final_Pitch_FR.html"))

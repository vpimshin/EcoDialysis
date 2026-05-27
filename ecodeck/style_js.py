CSS = r"""
:root{--slide-w:1600px;--slide-h:900px;--navy:#0A2A55;--navy2:#0E3C7A;--blue:#2E7FE8;--blue2:#4F9CFF;--sky:#E6F0FB;--sky2:#F4F8FD;--line:#D9E3EF;--ink:#0B1A2E;--ok:#1f7a47;--warn:#a26413;--bad:#9d1f1f}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;background:#0b1320;color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Inter,Helvetica,Arial,sans-serif;overflow:hidden}
.stage{position:fixed;inset:0;display:flex;align-items:center;justify-content:center}
.deck{position:relative;width:var(--slide-w);height:var(--slide-h);transform-origin:center center;background:#fff;box-shadow:0 12px 40px rgba(0,0,0,.35)}
.slide{position:absolute;inset:0;width:100%;height:100%;padding:54px 72px 64px 72px;background:#fff;color:var(--ink);display:none;flex-direction:column;overflow:hidden}
.slide.active{display:flex}
.slide.cover{background:linear-gradient(135deg,var(--navy) 0%,var(--navy2) 60%,#10498e 100%);color:#fff;justify-content:center}
.slide.cover h1{color:#fff;font-size:64px;line-height:1.05;margin-bottom:18px}
.slide.cover .eyebrow{color:var(--blue2)}
.slide.cover .lead{color:#cfe1f7;font-size:22px;max-width:1100px}
.slide.divider{background:linear-gradient(135deg,#0E3C7A,#2E7FE8);color:#fff;justify-content:center;align-items:flex-start}
.slide.divider h1{color:#fff;font-size:54px}
.slide.divider .eyebrow{color:#cfe1f7}
.slide.divider .lead{color:#e8f1fc;font-size:22px;max-width:1100px}
.slide h1{font-size:34px;color:var(--navy);margin-bottom:6px;line-height:1.15}
.slide h2{font-size:22px;color:var(--navy2);margin-bottom:6px}
.slide h3{font-size:15px;color:var(--navy);text-transform:uppercase;letter-spacing:1px;margin-bottom:6px}
.eyebrow{font-size:12px;letter-spacing:2.5px;color:var(--blue);text-transform:uppercase;margin-bottom:8px;font-weight:700}
.lead{font-size:18px;color:var(--ink);max-width:1380px;margin:8px 0 14px;line-height:1.45}
.slide footer{position:absolute;left:72px;right:72px;bottom:22px;display:flex;justify-content:space-between;color:#56698a;font-size:11px;border-top:1px solid var(--line);padding-top:8px;letter-spacing:.5px}
.slide footer .brand{color:var(--navy);font-weight:700}
.grid,.grid3,.grid4,.grid5{display:grid;gap:12px}
.grid{grid-template-columns:1fr 1fr}
.grid3{grid-template-columns:repeat(3,1fr)}
.grid4{grid-template-columns:repeat(4,1fr)}
.grid5{grid-template-columns:repeat(5,1fr)}
.col-1-2{grid-column:span 2}
.card{background:var(--sky2);border:1px solid var(--line);border-radius:10px;padding:12px 14px}
.card h3{margin-bottom:6px;font-size:13px}
.card p,.card li{font-size:13.5px;line-height:1.45;color:var(--ink)}
.card ul{padding-left:18px}
.card.dark{background:var(--navy);color:#fff;border-color:var(--navy2)}
.card.dark h3,.card.dark p,.card.dark li{color:#fff}
.card.dark h3{color:var(--blue2)}
.card.accent{background:#eaf2fc;border-color:#bcd2ee}
.kpi{background:var(--navy);color:#fff;border-radius:12px;padding:14px 16px;display:flex;flex-direction:column;justify-content:space-between}
.kpi .v{font-size:28px;font-weight:700;color:var(--blue2);line-height:1.05}
.kpi .l{font-size:11px;letter-spacing:1px;text-transform:uppercase;opacity:.85;margin-top:6px}
.kpi .s{font-size:11px;color:#cfe1f7;margin-top:4px}
table{width:100%;border-collapse:collapse;font-size:12px}
th,td{padding:5px 8px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}
th{background:var(--sky);color:var(--navy);font-weight:600;font-size:11px;text-transform:uppercase;letter-spacing:.5px}
tr:nth-child(even) td{background:#fbfcfe}
.src{display:inline-block;background:var(--navy);color:#fff;font-size:10px;padding:1px 6px;border-radius:8px;text-decoration:none;margin:0 1px;font-weight:700;letter-spacing:.5px}
.src:hover{background:var(--blue)}
.tag-ok,.tag-warn,.tag-bad{padding:2px 8px;border-radius:6px;font-size:11px;font-weight:700;display:inline-block;letter-spacing:.5px}
.tag-ok{background:#e0f1e6;color:var(--ok)}
.tag-warn{background:#fbe9d2;color:var(--warn)}
.tag-bad{background:#f6dada;color:var(--bad)}
.pill{display:inline-block;background:var(--sky);color:var(--navy);font-size:11px;padding:2px 8px;border-radius:10px;font-weight:600;margin-right:4px}
.bignum{font-size:54px;font-weight:800;color:var(--navy);line-height:1}
.bignum .u{font-size:18px;color:var(--blue);margin-left:6px;font-weight:600;letter-spacing:1px}
.flow{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin:12px 0}
.flow .step{background:var(--sky2);border:1px solid var(--line);border-radius:8px;padding:8px 12px;font-size:12px;color:var(--navy);font-weight:600}
.flow .arrow{color:var(--blue);font-weight:800}
.checklist li{list-style:none;padding-left:22px;position:relative;margin-bottom:4px;font-size:13px}
.checklist li:before{content:"✓";position:absolute;left:0;color:var(--ok);font-weight:800}
.xlist li{list-style:none;padding-left:22px;position:relative;margin-bottom:4px;font-size:13px}
.xlist li:before{content:"✗";position:absolute;left:0;color:var(--bad);font-weight:800}
.banner{background:linear-gradient(90deg,var(--navy),var(--navy2));color:#fff;padding:14px 20px;border-radius:10px;font-size:18px;line-height:1.4;margin:10px 0}
.banner b{color:var(--blue2)}
.appendix{background:#fafcff}
.appendix th,.appendix td{font-size:10.5px;padding:3px 6px}
.src-anchor{margin-bottom:6px;padding:6px 10px;border-left:3px solid var(--blue);background:var(--sky2);font-size:11.5px;border-radius:0 6px 6px 0}
.src-anchor b{color:var(--navy)}
.cols2{column-count:2;column-gap:24px}
.cols2 p{break-inside:avoid;margin-bottom:8px;font-size:12.5px;line-height:1.4}
.scroll-fit{overflow:hidden}
/* nav */
.nav{position:fixed;bottom:14px;right:14px;display:flex;gap:6px;align-items:center;z-index:50;background:rgba(255,255,255,.95);border:1px solid var(--line);border-radius:24px;padding:5px 12px;box-shadow:0 2px 8px rgba(0,0,0,.18)}
.nav button{background:transparent;border:0;cursor:pointer;color:var(--navy);font-size:16px;padding:2px 8px;font-weight:700}
.nav button:hover{color:var(--blue)}
.counter{font-size:11px;color:var(--navy);min-width:54px;text-align:center;font-variant-numeric:tabular-nums;font-weight:600}
.progress{position:fixed;top:0;left:0;height:3px;background:var(--blue);width:0;z-index:60;transition:width .15s ease}
.brand-mini{position:absolute;left:72px;top:22px;font-size:11px;letter-spacing:2px;color:var(--blue);font-weight:700;text-transform:uppercase}
@media print{
  @page{size:13.333in 7.5in;margin:0}
  html,body{background:#fff;overflow:visible;height:auto}
  .stage{position:static;display:block}
  .deck{transform:none!important;width:13.333in;height:7.5in;box-shadow:none}
  .slide{display:flex!important;position:relative;width:13.333in;height:7.5in;page-break-after:always;break-after:page;inset:auto}
  .slide:last-child{page-break-after:auto}
  .nav,.progress{display:none!important}
}
"""

JS = r"""
(function(){
  const slides=[...document.querySelectorAll('.slide')];
  let i=0;
  function show(n){
    i=Math.max(0,Math.min(slides.length-1,n));
    slides.forEach((s,k)=>s.classList.toggle('active',k===i));
    const c=document.getElementById('cnt'); if(c) c.textContent=(i+1)+' / '+slides.length;
    const p=document.getElementById('prog'); if(p) p.style.width=((i+1)/slides.length*100)+'%';
    const id='#'+slides[i].id;
    if(location.hash!==id) history.replaceState(null,'',id);
  }
  function fit(){
    const d=document.querySelector('.deck'); if(!d) return;
    const s=Math.min(innerWidth/1600,innerHeight/900);
    d.style.transform='scale('+s+')';
  }
  addEventListener('resize',fit);
  addEventListener('keydown',e=>{
    if(e.target&&/^(input|textarea)$/i.test(e.target.tagName))return;
    if(['ArrowRight','PageDown',' '].includes(e.key)){show(i+1);e.preventDefault();}
    else if(['ArrowLeft','PageUp'].includes(e.key)){show(i-1);e.preventDefault();}
    else if(e.key==='Home'){show(0);e.preventDefault();}
    else if(e.key==='End'){show(slides.length-1);e.preventDefault();}
  });
  addEventListener('hashchange',()=>{
    const k=slides.findIndex(s=>'#'+s.id===location.hash);
    if(k>=0) show(k);
  });
  document.addEventListener('click',e=>{
    const a=e.target.closest('a.src'); if(!a) return;
    // let default hash nav happen then sync
    setTimeout(()=>{
      const k=slides.findIndex(s=>'#'+s.id===location.hash);
      if(k>=0) show(k);
    },10);
  });
  document.getElementById('prev').onclick=()=>show(i-1);
  document.getElementById('next').onclick=()=>show(i+1);
  const init=slides.findIndex(s=>'#'+s.id===location.hash);
  show(init>=0?init:0); fit();
})();
"""

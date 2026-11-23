#!/usr/bin/env python3
"""Build a calm, step-by-step buyer selection page.
usage: build_selection.py OUTDIR CLIENT_NAME STORAGE_KEY
Images: Necessidades/Olival photos are copied from the old page folder (img/), Santos is hotlinked."""
import sys, json, html, shutil, os

OUT, CLIENT, KEY = sys.argv[1], sys.argv[2], sys.argv[3]
SLUG = os.path.basename(os.path.normpath(OUT))
MAP = open('/home/claude/work/map_base.svg').read()

exec(open('/home/claude/clients/am_round2.py').read())

def ccard(h):
    c=CONTACT.get(h['id'])
    if not c: return '<p class="agb">'+e(h['agency'])+'</p>'
    off,ref,oph,ag,aph,tip=c
    priv=off=='Particular'
    tel=lambda n:'<a href="tel:+351'+n.replace(' ','')+'">'+e(n)+'</a>'
    cb=lambda k,lab:'<input type="checkbox" class="'+k+'" title="'+lab+'" aria-label="'+lab+'">'
    cls=' priv' if priv else (' ev' if off.startswith('Engel') else '')
    rows=''
    if not priv: rows+='<div class="cr">'+cb('tk1','Kantoor gebeld')+'<span>Agência</span><b>'+e(off)+'</b>'+(tel(oph) if oph else '')+'<em>Ref <b class="sel">'+e(ref)+'</b></em></div>'
    rows+='<div class="cr">'+cb('tk2','Eigenaar gecontacteerd' if priv else 'Agent gebeld')+'<span>'+('Vendedor' if priv else 'Agente')+'</span><b>'+e(ag or 'nome a pedir')+'</b>'+(tel(aph) if aph else '')+('<em>Ref <b class="sel">'+e(ref)+'</b></em>' if priv else '')+'</div>'
    if tip: rows+='<p class="ctip">'+e(tip)+'</p>'
    return '<div class="ccard'+cls+'">'+rows+'</div>'

SUG=globals().get('SUG',{})
DONE=globals().get('DONE',{})
KEEP=os.environ.get('KEEP')
if KEEP:
    order=KEEP.split(',');HOUSES=sorted([h for h in HOUSES if h['id'] in order],key=lambda h:order.index(h['id']))
for i,h in enumerate(HOUSES): h['n']=i+1
MARKET={'casimiro':'Op de markt: volgens de advertentie beschikbaar sinds mei 2026, laatste update 7/10. Al een half jaar te koop: ruimte om te onderhandelen.',
 'boavista':'Op de markt: laatste update 2/10. Prijshistoriek nog niet zichtbaar.',
 'algesrio':'Op de markt: gezien sinds 15/11. Prijs gezakt van 660 000 € naar 640 000 € (19/11).',
 'boahora7':'Op de markt: gezien op 19/11, rond 13/11 op Idealista gezet, laatste update 18/11. Particuliere verkoper, wil geen makelaars: eerst vragen of hij met mij wil werken.',
 'casimiro170':'Op de markt: nieuw, gezien op 23/11. KW deelt 50/50 met alle agentschappen.',
 'cruzq':'Op de markt: nieuw sinds 22/11. Particulier, verhuurd met huurders: eerst vragen of het vrij komt.',
 'algesrep':'Op de markt: nieuw sinds 20/11.',
 'estrela102':'Op de markt: nieuw, gezien op 23/11.',
 'casimiro185':'Op de markt: online sinds 15/09, ruim 2 maanden. Waarschijnlijk dezelfde flat als RE/MAX Siimgroup aan 725 000 €.',
 'belemt4':'Op de markt: sinds 4/11. Exclusief bij KW LEAD, deelt 50/50.',
 'tristao':'Op de markt: sinds 9/11.',
 'santost5':'Op de markt: E&V-pand van Oscar Baptista, op de E&V-site sinds minstens 1/11. Interne deling, geen schriftelijke partilha nodig.'}
for h in HOUSES:
    if h['id'] in MARKET: h['market']=MARKET[h['id']]
    elif not h.get('market'): h['market']='Op de markt: nog onbekend. Ik volg de prijs vanaf nu elke week.'
PROFILE = dict(
  ess=['Espaço para a família: T3, ou T2+1 com um terceiro quarto a sério','Sala grande com cozinha aberta, ou possível de abrir','Luz, carácter e pé-direito alto','De Santos a Algés, perto do rio e do comboio','Compra mais obras até 800 000 €'],
  bonus=['Varanda ou terraço','Duas casas de banho','Garagem para o carro elétrico'])

e = html.escape
svg=''
def legend():
    def brand(h):
        off=(CONTACT.get(h['id']) or (h['agency'],))[0]
        k='priv' if off=='Particular' else 'kw' if off.startswith('KW') else 'c21' if 'entury' in off else 'remax' if 'RE/MAX' in off else 'jll' if 'JLL' in off else 'ev' if off.startswith('Engel') else 'pf' if 'Christie' in off else 'oth'
        return f'<i class="br {k}">{e(off)}</i>'
    li = ''.join(f'<li data-hid="{h["id"]}" role="button" tabindex="0"><b class="{"" if h["ready"] else "rn"}">{h["n"]}</b><span>{e(h["name"])} <em class="go">↗</em><small>{e(h["price"])} · {e(h["ppm"])} · {e(h["state"])}</small><span class="lb">{brand(h)}<i class="cs"></i></span>{('<span class="sg">'+e(SUG[h['id']][1])+'</span>') if h['id'] in SUG else ''}</span><span class="pk"><button type="button" data-v="Voorstellen" title="Voorstellen">✓</button><button type="button" data-v="Twijfel" title="Twijfel">?</button><button type="button" data-v="Niet voorstellen" title="Niet voorstellen">✕</button></span></li>' for h in HOUSES)
    return f'<ol class="leg">{li}</ol>'

def house(h):
    ph = h['photos']
    thumbs = ''.join(f'<button type="button" class="th" data-i="{i}" aria-label="Fotografia {i+1}" style="background-image:url(\'{p}\')"></button>' for i, p in enumerate(ph)) if len(ph) > 1 else ''
    fit = ''.join(f'<li class="{k}"><i>{"✓" if k=="ok" else "≈"}</i>{e(t)}</li>' for k, t in h['fit'])
    why = ''.join(f'<li>{e(w)}</li>' for w in h['why'])
    facts = ''.join(f'<div><small>{e(a)}</small>{e(b)}</div>' for a, b in h['facts'])
    nav = f'<button type="button" class="nv prev" aria-label="Anterior">‹</button><button type="button" class="nv next" aria-label="Seguinte">›</button><span class="cnt">1 / {len(ph)}</span>' if len(ph) > 1 else ''
    return f'''<section class="step house" data-id="{h['id']}" data-name="{e(h['name'])}" hidden>
  <div class="pcol"><div class="gal" data-photos='{json.dumps(ph)}' data-caps='{json.dumps(h.get("caps",[]))}'>
    <div class="main" role="img" aria-label="{e(h['name'])}" style="background-image:url('{ph[0]}')"></div>
    <span class="tag{'' if h['ready'] else ' rn'}{' ex' if h.get('extra') else ''}">{e(h['state'])}</span>{nav}<span class="pcap"></span>
  </div>
  {f'<div class="thumbs">{thumbs}</div>' if thumbs else ''}</div>
  <div class="pad">
    <div class="head"><h2><span class="num{'' if h['ready'] else ' rn'}">{h['n']}</span><a class="hlink" href="{e(h['link'])}" target="_blank" rel="noopener">{e(h['name'])} ↗</a></h2><p class="price">{e(h['price'])}<small class="ppm">{e(h['ppm'])}</small></p></div>
    <p class="line">{e(h['line'])}</p>{('<p class="mkt">'+e(h['market'])+'</p>') if h.get('market') else ''}{ccard(h)}<label class="agl">Contact met {'de eigenaar' if h['agency'].startswith('Particular') else 'het agentschap'}<textarea class="agnote" rows="2" placeholder="Bijvoorbeeld: gebeld 18/11, partilha ja 50%, prijs bespreekbaar tot 650k, planta volgt"></textarea></label>
    <h3>Porquê esta casa</h3>
    <ul class="why">{why}</ul>
    <ul class="fit" aria-label="O vosso essencial">{fit}</ul>
    <p class="note"><b>A ter em conta:</b> {e(h['note'])}</p>
    <div class="row2"><details class="more"><summary>Mais detalhes</summary><div class="facts">{facts}</div>
</details>
    <div class="links">{f'<a href="{h["link"]}" target="_blank" rel="noopener">Ver anúncio e todas as fotos ↗</a>' if h.get('link') else ''}<a href="https://www.google.com/maps/search/?api=1&query={e(h['maps']).replace(' ','+')}" target="_blank" rel="noopener">Ver no mapa ↗</a></div></div>
    <div class="react">
      <p class="rq">Voorstellen aan {e(CLIENT)}?</p>
      <div class="btns" hidden><button type="button" data-v="Voorstellen" class="b-love">✓ Voorstellen</button><button type="button" data-v="Twijfel" class="b-maybe">Twijfel</button><button type="button" data-v="Niet voorstellen" class="b-no">✕ Niet voorstellen</button></div>
      <textarea rows="1" placeholder="Waarom? Alleen voor jou."></textarea>
    </div>
  </div>
</section>'''

ess = ''.join(f'<li>{e(x)}</li>' for x in PROFILE['ess'])
bon = ''.join(f'<li>{e(x)}</li>' for x in PROFILE['bonus'])
vis = ''.join(f'<label><input type="checkbox" value="{e(h["name"])}"><span>{h["n"]}. {e(h["name"])}</span></label>' for h in HOUSES)

page = f'''<!doctype html><html lang="pt"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Voorselectie {e(CLIENT)} · tool van Pascale</title>
<meta name="robots" content="noindex,nofollow"><meta name="referrer" content="no-referrer">
<meta property="og:title" content="Seleção 2 para {e(CLIENT)}">
<meta property="og:description" content="{len(HOUSES)} casas escolhidas para vocês · Pascale Lepoutre, Engel &amp; Völkers Lisboa">
<meta property="og:image" content="https://pascalelisbonhomes.com/img/share.png">
<meta property="og:url" content="https://pascalelisbonhomes.com/s/{SLUG}/">
<meta property="og:type" content="website"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg"><link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"><script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Syne:wght@500;600&family=Inter:wght@300;400;500&display=swap">
<style>
:root{{--bg:#fffdf9;--cream:#fcf3e3;--sand:#f2e0c2;--sun:#f7d98b;--ink:#2a2420;--muted:#6f655a;--line:#efe3d0;--gold:#b08429;--ok:#2e7d4f;--card:#fff;--red:#c8102e;
--mland:#efe6d6;--mroad:#fff;--mmaj:#f6dfa8;--water:#d3e4ea;--display:"Syne","Avenir Next",Arial,sans-serif;--body:"Inter",-apple-system,"Segoe UI",Arial,sans-serif;color-scheme:light}}
*{{box-sizing:border-box}}[hidden]{{display:none!important}}
body{{margin:0;background:var(--bg);color:var(--ink);font:300 16px/1.55 var(--body)}}
.wrap{{max-width:760px;margin:0 auto;padding:18px max(16px,env(safe-area-inset-left)) 16px}}
.top{{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-bottom:12px;border-bottom:1px solid var(--line)}}
.brand{{font:500 12px var(--display);letter-spacing:.24em;text-transform:uppercase}}.brand{{display:grid;grid-template-columns:auto 1fr;column-gap:12px;align-items:center}}.brand .av{{grid-row:span 2;width:42px;height:42px;border-radius:50%;object-fit:cover;object-position:center}}.brand small{{display:block;font:400 10px var(--body);letter-spacing:.16em;color:var(--muted);margin-top:3px}}
.topart{{height:38px;width:auto;fill:none;stroke:var(--ink);stroke-width:2}}.topart .g{{stroke:var(--gold)}}
h1{{font:500 clamp(26px,5vw,34px)/1.15 var(--display);margin:22px 0 8px;text-wrap:balance}}
.eyebrow{{font:500 11px var(--body);letter-spacing:.18em;text-transform:uppercase;color:var(--gold)}}
.lead{{color:var(--muted);margin:0 0 18px;max-width:60ch}}
.intro-grid{{display:grid;gap:16px}}
.box{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px}}
.box h3,.pad h3{{font:500 11px var(--body);letter-spacing:.16em;text-transform:uppercase;color:var(--gold);margin:0 0 8px}}
.box ul{{margin:0 0 12px;padding-left:18px}}.box li{{margin:3px 0}}
.btns{{display:flex;flex-wrap:wrap;gap:8px}}
.btns button{{font:400 15px var(--body);padding:9px 16px;border-radius:999px;border:1px solid var(--line);background:var(--cream);color:var(--ink);cursor:pointer}}
.btns button[aria-pressed="true"]{{border-color:var(--ink);background:var(--ink);color:#fff}}
.b-love[aria-pressed="true"]{{background:var(--ok)!important;border-color:var(--ok)!important}}
.b-no[aria-pressed="true"]{{background:var(--red)!important;border-color:var(--red)!important}}
.b-maybe[aria-pressed="true"]{{background:var(--sun)!important;border-color:var(--gold)!important;color:var(--ink)!important}}
textarea{{width:100%;margin-top:10px;font:15px/1.4 var(--body);padding:10px 12px;border:1px solid var(--sand);border-radius:12px;min-height:56px;resize:none;overflow:hidden;background:#fff}}
.mapa{{width:100%;height:auto;display:block;border-radius:14px;border:1px solid var(--line)}}
.m-land{{fill:var(--mland)}}.m-water{{fill:var(--water)}}
.m-r,.m-t,.m-m{{fill:none;stroke-linecap:round;stroke-linejoin:round}}.m-r{{stroke:var(--mroad);stroke-width:2.6}}.m-t{{stroke:var(--mroad);stroke-width:4.5}}.m-m{{stroke:var(--mmaj);stroke-width:6.5}}
.m-area{{font:600 15px var(--body);letter-spacing:.3em;fill:var(--muted);opacity:.55}}.m-water-l{{font:italic 14px var(--body);fill:var(--muted)}}.m-road{{font:10px var(--body);fill:var(--muted)}}
.m-pin circle{{fill:var(--ink);stroke:#fff;stroke-width:3}}.m-pin text{{font:600 21px var(--body);fill:#fff}}.m-pin.rn circle{{fill:var(--gold)}}
.m-home circle{{fill:var(--ok);stroke:#fff;stroke-width:3}}.m-home path{{fill:none;stroke:#fff;stroke-width:2;stroke-linejoin:round}}.m-home-l{{font:600 15px var(--body);fill:var(--ok)}}
.leg li[data-hid]{{cursor:pointer;padding:6px 8px;margin:0 -8px;border-radius:10px}}.leg li[data-hid]:hover{{background:#f3efe6}}.leg .go{{font-style:normal;color:var(--gold)}}.lb{{display:flex;flex-wrap:wrap;gap:6px;margin-top:4px}}.br,.cs{{font:600 11px var(--body);font-style:normal;padding:2px 9px;border-radius:999px;color:#fff;background:#6b7a8c}}.br.kw{{background:#b40101}}.br.c21{{background:#beaf87;color:#252526}}.br.remax{{background:#003da5}}.br.jll{{background:#e30613}}.br.ev{{background:#1d1d1b}}.br.pf{{background:#000}}.br.priv{{background:#5b2d7a}}.cs:empty{{display:none}}.cs{{background:#2b7a4b}}.cs.half{{background:#d9a23a;color:#2b2b2b}}
.sg{{display:block;margin-top:3px;font:500 12.5px var(--body);color:#5c4a1e}}.pk{{flex:none;margin-left:auto;display:flex;gap:4px;align-self:center}}.pk button{{width:32px;height:32px;border-radius:50%;border:1.5px solid #d8d2c4;background:#fff;font:700 14px var(--body);color:#8a8272;cursor:pointer}}.pk button[aria-pressed="true"][data-v="Voorstellen"]{{background:#2b7a4b;border-color:#2b7a4b;color:#fff}}.pk button[aria-pressed="true"][data-v="Twijfel"]{{background:#d9a23a;border-color:#d9a23a;color:#fff}}.pk button[aria-pressed="true"][data-v="Niet voorstellen"]{{background:#9a9a9a;border-color:#9a9a9a;color:#fff}}.leg li.off>span{{opacity:.5}}
.leg{{list-style:none;margin:12px 0 0;padding:0;display:grid;gap:8px}}.leg li{{display:flex;gap:10px;align-items:flex-start}}
.leg b,.num{{flex:none;display:inline-grid;place-items:center;width:26px;height:26px;border-radius:50%;background:var(--ink);color:#fff;font:600 13px var(--body)}}.leg b.rn,.num.rn{{background:var(--gold)}}
.leg small{{display:block;color:var(--muted);font-size:12.5px}}
.house{{background:var(--card);border:1px solid var(--line);border-radius:18px;overflow:hidden;margin-top:14px}}
.gal{{position:relative}}.gal .main{{height:clamp(220px,52vw,380px);background:center 55%/cover no-repeat var(--sand)}}
.tag{{position:absolute;left:12px;bottom:12px;font:500 11px var(--body);letter-spacing:.12em;text-transform:uppercase;background:rgba(255,255,255,.93);padding:5px 11px;border-radius:999px}}.tag.rn{{background:var(--gold);color:#fff}}.tag.ex{{background:var(--ink);color:#fff}}
.nv{{position:absolute;top:50%;transform:translateY(-50%);width:40px;height:40px;border-radius:50%;border:0;background:rgba(255,255,255,.9);font:400 26px/1 var(--body);cursor:pointer;color:var(--ink)}}.nv.prev{{left:10px}}.nv.next{{right:10px}}
.cnt{{position:absolute;right:12px;bottom:12px;font:12px var(--body);background:rgba(0,0,0,.55);color:#fff;padding:3px 9px;border-radius:999px}}
.thumbs{{display:flex;gap:6px;overflow-x:auto;padding:8px 10px 0}}.th{{flex:none;width:64px;height:46px;border-radius:8px;border:2px solid transparent;background:center/cover no-repeat var(--sand);cursor:pointer}}.th.on{{border-color:var(--gold)}}
.pad{{padding:16px 18px 20px}}
.head{{display:flex;justify-content:space-between;align-items:baseline;gap:12px}}
.head h2{{font:500 clamp(20px,4.2vw,24px)/1.2 var(--display);margin:0;display:flex;gap:10px;align-items:center}}
.price{{font:600 clamp(19px,4vw,22px) var(--display);color:var(--gold);margin:0;white-space:nowrap}}
.line{{margin:4px 0 14px;color:var(--muted);font-size:15px}}
.why{{margin:0 0 14px;padding-left:18px}}.why li{{margin:4px 0}}
.fit{{list-style:none;padding:0;margin:0 0 12px;display:flex;flex-wrap:wrap;gap:6px}}
.fit li{{font-size:13.5px;padding:4px 11px;border-radius:999px;border:1px solid}}.fit i{{font-style:normal;margin-right:5px;font-weight:600}}
.fit .ok{{border-color:#bfdccb;color:var(--ok);background:#f1f8f3}}.fit .mid{{border-color:var(--sand);color:#8a6a1f;background:var(--cream)}}
.note{{font-size:14.5px;background:var(--cream);border-radius:12px;padding:10px 13px;margin:0 0 10px}}
.more{{margin:0 0 16px}}.more summary{{cursor:pointer;font-size:14px;color:var(--gold);font-weight:500;padding:6px 0}}
.facts{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;margin:8px 0}}.facts div{{background:var(--cream);border-radius:10px;padding:8px 10px;font-size:14px}}.facts small{{display:block;font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}}
.links{{display:flex;flex-wrap:wrap;gap:8px 18px;margin:0 0 16px}}.links a{{font-size:14px;color:var(--ink);text-decoration:none;border-bottom:1px solid var(--gold);padding-bottom:1px}}
.rq span{{display:block;font-weight:300;font-size:13px;color:var(--muted)}}
.rbar{{display:flex;gap:6px;flex:1;justify-content:center}}.rbar button{{font:500 14px var(--body);padding:11px 14px;border-radius:999px;border:1px solid var(--line);background:var(--cream);color:var(--ink);cursor:pointer;white-space:nowrap}}
.rbar button[data-v="Voorstellen"][aria-pressed="true"]{{background:var(--ok);border-color:var(--ok);color:#fff}}.rbar button[data-v="Twijfel"][aria-pressed="true"]{{background:var(--sun);border-color:var(--gold)}}.rbar button[data-v="Niet voorstellen"][aria-pressed="true"]{{background:var(--red);border-color:var(--red);color:#fff}}
.bar .back{{min-width:44px}}.bar .go.arrow{{padding:13px 16px}}
.progress{{height:4px;background:var(--line);border-radius:4px;margin:12px 0 0;overflow:hidden}}.progress i{{display:block;height:100%;background:var(--gold);width:0;transition:width .3s}}
@media (max-width:899px){{.intro-left,.intro-right{{display:contents}}.cta-row{{order:4}}.intro-grid{{display:flex;flex-direction:column;gap:14px}}.i-txt{{order:1}}.intro-grid .mapbox{{order:2}}.intro-grid .prof{{order:3}}.intro h1{{margin:0}}.intro .lead{{margin:0}}}}

.react{{border-top:1px solid var(--line);padding-top:14px}}.rq{{margin:0 0 8px;font-weight:500}}
.final .vis label{{display:flex;gap:10px;align-items:center;padding:10px 12px;border:1px solid var(--line);border-radius:12px;margin:6px 0;background:#fff;cursor:pointer}}
.final .vis input{{width:20px;height:20px;accent-color:var(--gold)}}
.sum{{list-style:none;padding:0;margin:0 0 14px}}.sum li{{display:flex;justify-content:space-between;gap:10px;padding:7px 0;border-bottom:1px solid var(--line);font-size:15px}}.sum em{{white-space:nowrap;flex:none;font-style:normal;color:var(--muted)}}
.send{{display:block;width:100%;margin-top:14px;font:500 14px var(--display);letter-spacing:.14em;text-transform:uppercase;padding:16px;border:0;border-radius:999px;background:var(--ink);color:#fff;cursor:pointer}}.send[aria-busy="true"]{{opacity:.6}}
.ty{{margin-top:6px}}.ty-head{{display:flex;gap:20px;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:20px}}
.ty-photo{{width:112px;height:112px;border-radius:50%;object-fit:cover;object-position:center;flex:none;border:3px solid var(--sun)}}
.ty-big{{font:500 30px var(--display);margin:0 0 4px}}.ty-txt{{margin:0;font-size:16px;line-height:1.5}}.ty-sig{{margin:8px 0 0;font:italic 400 18px var(--display);color:var(--gold)}}
.ty-eye{{font:600 12px var(--body);letter-spacing:.2em;text-transform:uppercase;color:var(--gold);margin:22px 0 10px}}
.tiles{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}}.tile{{display:flex;flex-direction:column;gap:6px;padding:16px;border-radius:16px;background:var(--cream);border:1px solid var(--line);color:var(--ink);text-decoration:none;transition:transform .15s,box-shadow .15s}}
.tile:hover{{transform:translateY(-2px);box-shadow:0 6px 18px rgba(42,36,32,.08)}}.tile svg{{width:30px;height:30px;padding:7px;border-radius:50%;background:var(--sun);fill:none;stroke:var(--ink);stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round;box-sizing:content-box}}
.tile b{{font-weight:600;font-size:15px;line-height:1.3}}.tile span{{font-size:13px;color:var(--muted);line-height:1.4}}
.wa{{display:flex;width:max-content;align-items:center;gap:8px;margin:16px auto 0;padding:9px 18px;border-radius:999px;background:#25d366;color:#fff;font:600 14px var(--body);text-decoration:none}}.wa .wai{{width:18px;height:18px}}
@media(max-width:519px){{.topart{{display:none}}}}@media(max-width:820px){{.tiles{{grid-template-columns:1fr 1fr}}}}@media(max-width:520px){{.ty-head{{flex-direction:column;text-align:center}}.ty-photo{{width:120px;height:120px}}.tile{{padding:14px}}}}
.cta-row{{display:flex;justify-content:flex-end;margin-top:18px}}.cta{{background:var(--sun);border:0;font:600 14px var(--display);letter-spacing:.14em;text-transform:uppercase;padding:16px 28px;border-radius:999px;cursor:pointer;color:var(--ink)}}
.backlink{{background:none;border:0;padding:16px 0 0;font:500 13px var(--body);letter-spacing:.08em;text-transform:uppercase;color:var(--muted);cursor:pointer}}
@media (max-width:519px){{.cta{{width:100%}}}}
.sent{{background:#f1f8f3;border:1px solid #bfdccb;border-radius:14px;padding:16px;margin-top:14px}}
.bar{{position:static;margin:12px 0 0;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:10px 12px}}
.bar-in{{display:flex;align-items:center;gap:12px}}
.bar .back{{background:none;border:0;font:500 13px var(--body);letter-spacing:.1em;text-transform:uppercase;color:var(--muted);cursor:pointer;padding:12px 6px}}
.bar .mid{{flex:1;text-align:center;font-size:12.5px;color:var(--muted)}}.dots{{display:flex;justify-content:center;gap:6px;margin-bottom:3px}}.dots i{{width:8px;height:8px;border-radius:50%;background:var(--sand)}}.dots i.on{{background:var(--gold)}}
.bar .go{{background:var(--sun);border:0;font:600 13px var(--display);letter-spacing:.14em;text-transform:uppercase;padding:13px 22px;border-radius:999px;cursor:pointer;color:var(--ink)}}
footer{{margin-top:26px;font-size:12px;color:var(--muted)}}
.react .rbar{{justify-content:flex-start;flex:none;margin:2px 0 4px}}.react .rbar button{{padding:10px 18px;font-size:15px}}
.pad .bar{{margin:14px 0 0;border:0;border-top:1px solid var(--line);border-radius:0;padding:12px 0 0;background:none}}
/* compact: less scrolling */
.row2{{display:flex;flex-wrap:wrap;align-items:baseline;gap:6px 22px;margin:0 0 12px}}.row2 .more{{margin:0}}.row2 .links{{margin:0}}.row2 .more[open]{{flex-basis:100%}}
.why{{margin-bottom:10px}}.why li{{margin:2px 0}}.note{{margin-bottom:8px}}.react{{padding-top:10px}}.rq{{margin-bottom:4px}}
textarea[rows="1"]{{min-height:42px}}
@media (min-width:900px){{
 .wrap{{max-width:1120px}}
 .intro h1{{margin:8px 0 8px;font-size:30px}}.intro .lead{{margin-bottom:12px}}
 .intro .box{{padding:14px 16px}}.intro .box ul{{margin-bottom:8px}}.intro .box li{{margin:1px 0}}
 .intro .mapa{{height:290px}}
 .intro .box.prof ul{{columns:1}}
 .leg{{grid-template-columns:1fr 1fr;gap:6px 14px;margin-top:10px}}
 .intro textarea{{min-height:42px}}
 .cta-row{{margin-top:12px}}
 .house{{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);align-items:stretch}}
 .pcol{{display:flex;flex-direction:column;background:var(--cream)}}.pcol .gal{{flex:1;display:flex}}.pcol .gal .main{{flex:1;height:auto;min-height:440px}}
 .pcol .thumbs{{padding:8px 10px 10px}}
 .pad{{padding:18px 22px 16px}}.line{{margin-bottom:10px}}
 .intro-grid{{grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:28px;align-items:stretch}}
 .pcols{{display:grid;grid-template-columns:1.25fr 1fr;gap:18px}}
 .intro-right{{display:flex;flex-direction:column;align-self:stretch!important}}.intro-right .cta-row{{margin-top:auto!important;padding-top:14px;justify-content:center}}.intro-right .mapbox{{flex:1;display:flex;flex-direction:column}}.intro-right .mapa{{flex:1;height:auto!important;min-height:300px}}.intro-right .leg{{margin-top:12px}}
 .intro-left .box{{margin-top:14px}}
 .intro .mapbox{{margin-top:20px}}
 .intro-grid>.cta-row{{grid-column:2;justify-content:center;margin-top:0}}
 .intro-left .box.prof{{margin-bottom:0}}.intro-right .cta-row{{margin-top:14px}}
}}
@media (max-width:519px){{.rbar button{{padding:10px 11px;font-size:13.5px}}.bar .back{{font-size:0!important;padding:10px 6px!important}}.bar .back::before{{content:"←";font-size:22px;color:var(--ink)}}.bar .go.arrow{{font-size:20px!important;padding:9px 18px!important;letter-spacing:0!important}}.bar-in{{gap:8px}}}}
/* keep the bar clear of the hosting badge (Netlify) when it is present */

@media (min-width:1180px){{body.nlb .bar{{padding-bottom:calc(8px + env(safe-area-inset-bottom))}}}}
@media (min-width:760px){{.intro-grid{{grid-template-columns:1fr 1fr;align-items:start}}.facts{{grid-template-columns:repeat(3,minmax(0,1fr))}}}}

.bar-in{{justify-content:space-between}}
.bar .back{{display:inline-flex;align-items:center;justify-content:center;gap:6px;background:var(--card)!important;border:1px solid var(--line)!important;border-radius:999px;padding:12px 18px!important;color:var(--ink)!important;font:600 13px var(--display)!important;letter-spacing:.14em!important;text-transform:uppercase}}
.bar .mid{{flex:1;text-align:center;font:600 11px var(--body);letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}}
@media (max-width:519px){{.bar .back{{width:48px;height:48px;padding:0!important;font-size:0!important;letter-spacing:0!important}}.bar .back::before{{content:"←";font-size:20px!important;margin:0!important}}}}
.price .ppm{{display:block;font:400 12.5px var(--body);color:var(--muted);text-align:right;letter-spacing:0}}
#lmap{{height:340px;border-radius:12px;margin:4px 0 14px;z-index:0}}
.lpin{{width:28px;height:28px;border-radius:50%;background:var(--ink);color:#fff;font:600 13px/28px var(--body);text-align:center;border:2px solid #fff;box-shadow:0 1px 4px rgba(0,0,0,.35)}}.lpin.rn{{background:var(--gold)}}.lpin.ref{{background:var(--red)}}.lpin.home{{background:#fff;color:var(--ink)}}
.pbanner{{background:var(--ink);color:#fff;text-align:center;padding:9px 14px;font:600 13px var(--body);letter-spacing:.04em}}
.rbar{{flex-wrap:wrap}}
.pcap{{position:absolute;right:12px;bottom:48px;font:600 12px var(--body);background:rgba(42,36,32,.82);color:#fff;padding:5px 11px;border-radius:999px}}
.sum em{{white-space:nowrap;flex:none;font-style:normal;font-weight:600;font-size:13px;padding:4px 12px;border-radius:999px}}.sum em.v-yes{{background:#e3f1e8;color:var(--ok)}}.sum em.v-mid{{background:#fbefc9;color:#8a6516}}.sum em.v-no{{background:#f8dfe2;color:var(--red)}}.sum em.v-none{{background:var(--cream);color:var(--muted)}}
.ccard{{margin:4px 0 12px;padding:10px 14px;border-radius:14px;background:#eef3f9;border-left:4px solid #2b4a72;display:grid;gap:5px}}.ccard.priv{{background:#f4ecf8;border-color:#5b2d7a}}.ccard.ev{{background:#fbecee;border-color:var(--red)}}.cr{{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 12px;font:400 15px var(--body)}}.cr input{{width:20px;height:20px;margin:0;accent-color:#2b7a4b;align-self:center;cursor:pointer}}.cr em{{margin-left:auto;font:600 11px var(--body);letter-spacing:.1em;text-transform:uppercase;color:#6b7a8c;font-style:normal}}.cr em b{{font:600 15px var(--body);letter-spacing:0;text-transform:none;color:#1d2733}}.cr span{{min-width:72px;font:600 11px var(--body);letter-spacing:.1em;text-transform:uppercase;color:#6b7a8c}}.cr b{{font-weight:600}}.cr a{{color:#2b4a72;font-weight:600;text-decoration:none;border-bottom:1px solid currentColor}}.cr .sel{{user-select:all}}.ctip{{margin:2px 0 0;font:500 13px var(--body);color:#a4520c}}.hlink{{color:inherit;text-decoration:none}}.hlink:hover{{text-decoration:underline}}\n.mkt{{margin:0 0 6px;font:500 13px var(--body);color:#a4520c}}.agb{{display:inline-block;margin:2px 0 10px;font:600 12.5px var(--body);padding:5px 12px;border-radius:999px;background:#e8eef6;color:#2b4a72}}.agb.priv{{background:#efe4f6;color:#5b2d7a}}.agb.ev{{background:#f8dfe2;color:var(--red)}}
.ticks{{display:flex;flex-wrap:wrap;gap:8px 18px;margin:0 0 10px}}.ticks label{{display:flex;align-items:center;gap:6px;font:500 14px var(--body);cursor:pointer}}.ticks input{{width:20px;height:20px;accent-color:#2b7a4b}}
.agl{{display:block;margin:0 0 14px;font:600 11px var(--body);letter-spacing:.12em;text-transform:uppercase;color:#2b4a72}}.agl textarea{{display:block;width:100%;margin-top:6px;font:400 15px var(--body);letter-spacing:0;text-transform:none;border:1px solid #c9d6e6;background:#f4f7fb;border-radius:12px;padding:10px 12px;color:var(--ink);resize:vertical}}
</style></head><body>
<div class="pbanner">Jouw tool · voorselectie voor {e(CLIENT)} · niet naar de klant sturen</div>
<div class="wrap">
  <div class="top"><div class="brand"><img class="av" src="/img/pascale-lepoutre-portrait.webp" alt="">Pascale Lepoutre<small>Lisbon Homes · Engel &amp; Völkers</small></div>
  <svg class="topart" viewBox="0 0 520 120" aria-hidden="true"><line x1="0" y1="110" x2="520" y2="110"/><path d="M40 110V58h46v52M40 58l23-16 23 16M52 70h8v10h-8zM68 70h8v10h-8z"/><rect x="110" y="44" width="70" height="66"/><path d="M126 44v-10a19 19 0 0 1 38 0v10M135 110V92a10 10 0 0 1 20 0v18"/><path d="M200 110V66h40v44M200 66l20-14 20 14"/><rect class="g" x="258" y="64" width="96" height="34" rx="6"/><circle cx="276" cy="102" r="5"/><circle cx="336" cy="102" r="5"/><path d="M306 64l-10-20 22-8"/><path d="M374 110V52h44v58M374 52l22-15 22 15"/><circle class="g" cx="446" cy="70" r="12"/><path d="M446 82v28"/></svg></div>
  <div class="progress"><i id="prog"></i></div>

  <section class="step intro" data-label="Início">
    <div class="intro-grid">
      <div class="intro-left">
        <p class="eyebrow i-txt" style="margin-top:20px">Jouw tool · voorselectie ronde 2</p>
        <h1 class="i-txt">Welke huizen stel je voor aan {e(CLIENT)}?</h1>
        <p class="lead i-txt">Dit is jouw voorselectie. De huizen zie je precies zoals zij ze zullen zien, met de Portugese teksten. Kies per huis: voorstellen, twijfel of niet voorstellen, en schrijf kort waarom. Alleen wat je voorstelt komt op hun pagina.</p>
        <div class="box prof"><div class="pcols"><div><h3>Essencial para vocês</h3><ul>{ess}</ul></div><div><h3>Seria bom</h3><ul>{bon}</ul></div></div>
          <p class="rq" hidden>Este perfil está certo?</p>
          <div class="btns" id="pBtns" hidden><button type="button" data-v="Está certo">Está certo</button><button type="button" data-v="Quero ajustar">Quero ajustar</button></div>
          <textarea id="pTxt" hidden placeholder="O que mudariam? Por exemplo: o elevador é essencial."></textarea></div>
      </div>
      <div class="intro-right"><div class="box mapbox"><h3>As casas no mapa</h3><div id="lmap"></div><p class="mleg"><span class="lpin" style="display:inline-block;width:18px;height:18px;line-height:18px;font-size:10px">1</span> pronta a habitar · <span class="lpin rn" style="display:inline-block;width:18px;height:18px;line-height:18px;font-size:10px">2</span> para remodelar · <span class="lpin ref" style="display:inline-block;width:18px;height:18px;line-height:18px;font-size:10px">★</span> Calçada das Necessidades · <span class="lpin home" style="display:inline-block;width:18px;height:18px;line-height:18px;font-size:10px">⌂</span> onde vivem</p>{legend()}<p class="note" style="margin-top:10px"><b>A referência:</b> o 3.º andar na Calçada das Necessidades, que visitaram a 14 de novembro. Cada casa aqui deve ser melhor no preço ou na qualidade.</p></div></div>
      <div class="cta-row"><button type="button" class="cta" id="start">Ver as casas →</button></div>
    </div>
  </section>

  {''.join(house(h) for h in HOUSES)}

  <section class="step final" hidden data-label="Enviar">
    <button type="button" class="backlink" id="backHouses">← Voltar às casas</button>
    <h1 style="font-size:26px;margin-top:10px">Jouw keuze</h1>
    <div class="box"><h3>Overzicht</h3><ul class="sum" id="sum"></ul>
      <h3 hidden>Quais querem visitar?</h3><div class="vis" hidden>{vis}</div>
      <h3 style="margin-top:14px" hidden>Quando podem visitar?</h3>
      <div class="btns" id="wBtns" hidden><button type="button" data-v="Semana de 24 de novembro">Semana de 24 nov.</button><button type="button" data-v="Fim de semana 28 e 29 de novembro">28 e 29 nov.</button><button type="button" data-v="Outra data">Outra data</button></div>
      <h3 style="margin-top:14px">Nog iets voor Claude?</h3>
      <textarea id="oTxt" placeholder="Bijvoorbeeld: Bica alleen als de straat rustig is."></textarea>
      <button type="button" class="send" id="send">Opslaan en doorsturen naar Claude</button>
    </div>
    <div class="ty" id="afterSend" hidden>
      <div class="ty-head"><img class="ty-photo" src="/img/pascale-lepoutre-portrait.webp" alt="Pascale Lepoutre">
        <div><p class="ty-big">Opgeslagen</p><p class="ty-txt">Je keuze is doorgestuurd. Zeg in de chat dat je klaar bent, dan maak ik hun pagina.</p><p class="ty-sig">Pascale</p></div></div>
      <p class="ty-eye">Enquanto esperam</p>
      <div class="tiles">
        <a class="tile" href="/pt/buying/" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5zM4 20.5A2.5 2.5 0 0 0 6.5 23H20v-5"/></svg><b>Guia para comprar casa em Lisboa</b><span>Passo a passo, da procura à escritura</span></a>
        <a class="tile" href="/pt/buying/#calc" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="2.5" width="14" height="19" rx="2.5"/><path d="M8.5 6.5h7M8.5 11h.01M12 11h.01M15.5 11h.01M8.5 14.5h.01M12 14.5h.01M15.5 14.5h.01M8.5 18h.01M12 18h.01M15.5 18h.01"/></svg><b>Calcular os custos de compra</b><span>IMT, imposto do selo e escritura</span></a>
        <a class="tile" href="/pt/buying/#mortgage" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="7.5" cy="15.5" r="4.5"/><path d="m10.7 12.3 9.8-9.8M17 6l3 3M14.5 8.5l2 2"/></svg><b>Crédito à habitação</b><span>Apresento-vos uma intermediária de confiança</span></a>
        <a class="tile" href="https://www.instagram.com/pascalelisbonhomes/" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/></svg><b>@pascalelisbonhomes</b><span>O bairro, as casas e a vida em Lisboa</span></a>
      </div>
      <a class="wa" href="https://wa.me/351920609225" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" aria-hidden="true" class="wai"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.7a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.2-.2-.5-.3z"/></svg>Falar comigo no WhatsApp</a>
    </div>
  </section>

<nav class="bar" aria-label="Navegação"><div class="bar-in">
  <button type="button" class="back" id="back">← Anterior</button>
  <div class="mid" id="midlbl"><span id="lbl"></span></div>
  <div class="rbar" id="rbar" hidden><button type="button" data-v="Voorstellen">✓ Voorstellen</button><button type="button" data-v="Twijfel">Twijfel</button><button type="button" data-v="Niet voorstellen">✕ Niet voorstellen</button></div>
  <button type="button" class="go" id="go">Começar →</button>
</div></nav>
  <footer>Pascale Lepoutre · Consultora Imobiliária, Engel &amp; Völkers · +351 920 609 225</footer>
</div>

<form name="selection-feedback" method="POST" data-netlify="true" netlify-honeypot="bot-field" hidden>
<input type="hidden" name="form-name" value="selection-feedback"><input name="cliente"><input name="ronda"><textarea name="opiniao"></textarea><input name="respostas"><input name="bot-field">
</form>
<script>
(function(){{
const CLIENT={json.dumps(CLIENT)}, KEY={json.dumps(KEY)};
const steps=[...document.querySelectorAll('.step')], houses=steps.filter(s=>s.classList.contains('house'));
let cur=0; const rbar=document.getElementById('rbar'), midl=document.getElementById('midlbl');
function show(i){{cur=Math.max(0,Math.min(steps.length-1,i));steps.forEach((s,k)=>s.hidden=k!==cur);
 document.getElementById('prog').style.width=(cur/(steps.length-1)*100)+'%';
 const s=steps[cur]; const hi=houses.indexOf(s);
 rbar.hidden=hi<0; midl.hidden=hi<0; document.querySelector('.bar').hidden=hi<0; place(); syncBar(); steps[cur].querySelectorAll('textarea').forEach(grow);
 document.getElementById('lbl').textContent= hi<0?s.dataset.label:('Casa '+(hi+1)+' de '+houses.length);
 document.getElementById('back').style.visibility=cur?'visible':'hidden';
 const go=document.getElementById('go'); go.hidden=cur===steps.length-1;
 go.textContent= cur===0?'Ver as casas →': (cur===steps.length-2?'Concluir →':'Seguinte →');
 if(s.classList.contains('final'))summary();
 window.scrollTo({{top:0,behavior:'smooth'}}); save();}}
document.getElementById('go').onclick=()=>show(cur+1);
document.getElementById('back').onclick=()=>show(cur-1);
document.getElementById('start').onclick=()=>show(1);
document.getElementById('backHouses').onclick=()=>show(steps.length-2);
// galleries
document.querySelectorAll('.house').forEach(h=>{{const g=h.querySelector('.gal'),ph=JSON.parse(g.dataset.photos),cp=JSON.parse(g.dataset.caps||'[]'),pc=g.querySelector('.pcap'),m=g.querySelector('.main'),c=g.querySelector('.cnt'),th=[...h.querySelectorAll('.th')];let i=0;
 function set(n){{i=(n+ph.length)%ph.length;m.style.backgroundImage="url('"+ph[i]+"')";if(c)c.textContent=(i+1)+' / '+ph.length;if(pc){{pc.textContent=cp[i]||'';pc.hidden=!cp[i];}}th.forEach((t,k)=>t.classList.toggle('on',k===i));}}
 g.querySelector('.prev')?.addEventListener('click',()=>set(i-1));g.querySelector('.next')?.addEventListener('click',()=>set(i+1));
 th.forEach(t=>t.addEventListener('click',()=>set(+t.dataset.i)));set(0);
 let x0=null;m.addEventListener('touchstart',e=>x0=e.touches[0].clientX,{{passive:true}});m.addEventListener('touchend',e=>{{if(x0==null)return;const dx=e.changedTouches[0].clientX-x0;if(Math.abs(dx)>40)set(i+(dx<0?1:-1));x0=null;}});}});
// reactions
document.querySelectorAll('.btns').forEach(b=>b.querySelectorAll('button').forEach(x=>{{x.setAttribute('aria-pressed','false');x.addEventListener('click',()=>{{b.querySelectorAll('button').forEach(y=>y.setAttribute('aria-pressed','false'));x.setAttribute('aria-pressed','true');save();}});}}));
document.querySelectorAll('textarea,.vis input').forEach(t=>t.addEventListener('input',save));
function grow(t){{t.style.height='auto';t.style.height=(t.scrollHeight+2)+'px';}}
document.querySelectorAll('textarea').forEach(t=>t.addEventListener('input',()=>grow(t)));
document.querySelectorAll('.vis input').forEach(t=>t.addEventListener('change',save));
const DONE={json.dumps(DONE)};houses.forEach(h=>{{const d=DONE[h.dataset.id]||[];const a=h.querySelector('.tk1'),b=h.querySelector('.tk2');if(a&&d[0])a.checked=true;if(b&&d[1])b.checked=true;}});
document.querySelectorAll('.ccard input').forEach(t=>t.addEventListener('change',()=>{{save();legSync();}}));
function legSync(){{document.querySelectorAll('.leg li[data-hid]').forEach(li=>{{const h=houses.find(x=>x.dataset.id===li.dataset.hid),cs=li.querySelector('.cs');if(!h||!cs)return;const a=(h.querySelector('.tk1')||{{}}).checked,b=(h.querySelector('.tk2')||{{}}).checked,priv=!h.querySelector('.tk1');cs.className='cs'+(b?'':' half');cs.textContent=b?(priv?'Contactado ✓':'Agente ✓'):(a?'Agência ✓':'');const v=val(h.querySelector('.btns'));li.querySelectorAll('.pk button').forEach(x=>x.setAttribute('aria-pressed',String(x.dataset.v===v)));li.classList.toggle('off',v==='Niet voorstellen');}});}}
document.querySelectorAll('.leg .pk button').forEach(b=>b.addEventListener('click',ev=>{{ev.stopPropagation();const li=b.closest('li'),h=houses.find(x=>x.dataset.id===li.dataset.hid);if(!h)return;h.querySelectorAll('.btns button').forEach(x=>x.setAttribute('aria-pressed',String(x.dataset.v===b.dataset.v)));save();legSync();}}));
document.querySelectorAll('.leg li[data-hid]').forEach(li=>{{const go=()=>{{const h=houses.find(x=>x.dataset.id===li.dataset.hid);if(h){{show(steps.indexOf(h));window.scrollTo({{top:0}});}}}};li.addEventListener('click',go);li.addEventListener('keydown',ev=>{{if(ev.key==='Enter')go();}});}});
setTimeout(legSync,0);
function place(){{const s=steps[cur];if(!s.classList.contains('house'))return;const bar=document.querySelector('.bar'),react=s.querySelector('.react');react.insertBefore(rbar,react.querySelector('textarea'));
 if(window.innerWidth>=900)s.querySelector('.pad').appendChild(bar);else s.after(bar);}}
window.addEventListener('resize',()=>{{place();}});
function syncBar(){{const h=steps[cur];if(!h.classList.contains('house'))return;const v=val(h.querySelector('.btns'));rbar.querySelectorAll('button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.v===v)));}}
rbar.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{{const h=steps[cur];h.querySelectorAll('.btns button').forEach(x=>x.setAttribute('aria-pressed',String(x.dataset.v===b.dataset.v)));syncBar();save();}}));
const val=b=>(b&&b.querySelector('[aria-pressed="true"]')||{{}}).dataset?.v||'';
function summary(){{const ul=document.getElementById('sum');ul.textContent='';houses.forEach(h=>{{const li=document.createElement('li');li.innerHTML='<span></span><em></em>';li.firstChild.textContent=h.dataset.name;li.lastChild.textContent=val(h.querySelector('.btns'))||'geen keuze';{{const v=val(h.querySelector('.btns'));li.lastChild.className=/Voorstellen|Adoro/.test(v)&&!/Niet/.test(v)?'v-yes':/Twijfel|Talvez/.test(v)?'v-mid':/Niet|Não/.test(v)?'v-no':'v-none';}}ul.appendChild(li);}});}}
function text(){{const L=['VOORSELECTIE door Pascale, ronda 2:'];
 const pv=val(document.getElementById('pBtns')),pt=document.getElementById('pTxt').value.trim();L.push('Perfil: '+(pv||'sem resposta')+(pt?' · '+pt:''));
 houses.forEach(h=>{{const t=h.querySelector('.react textarea').value.trim(),an=((h.querySelector('.agnote')||{{}}).value||'').trim();L.push(h.dataset.name+': '+(val(h.querySelector('.btns'))||'geen keuze')+(t?' · '+t:'')+(an?' · CONTACT: '+an:''));}});
 const v=[...document.querySelectorAll('.vis input:checked')].map(i=>i.value);L.push('Queremos visitar: '+(v.length?v.join(', '):'ainda não sabemos'));
 const w=val(document.getElementById('wBtns'));if(w)L.push('Quando: '+w);
 const o=document.getElementById('oTxt').value.trim();if(o)L.push('Outros: '+o);L.push(CLIENT);return L.join('\\n');}}
function save(){{try{{const st={{c:cur,p:val(document.getElementById('pBtns')),pt:document.getElementById('pTxt').value,o:document.getElementById('oTxt').value,w:val(document.getElementById('wBtns')),v:[...document.querySelectorAll('.vis input')].map(i=>i.checked),h:houses.map(h=>[val(h.querySelector('.btns')),h.querySelector('.react textarea').value,(h.querySelector('.agnote')||{{}}).value||'',!!(h.querySelector('.tk1')||{{}}).checked,!!(h.querySelector('.tk2')||{{}}).checked,h.dataset.id])}};localStorage.setItem(KEY,JSON.stringify(st));}}catch(e){{}}}}
function load(){{let st;try{{st=JSON.parse(localStorage.getItem(KEY)||'null')}}catch(e){{}}if(!st)return 0;
 const press=(b,v)=>b.querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed',String(x.dataset.v===v)));
 press(document.getElementById('pBtns'),st.p);press(document.getElementById('wBtns'),st.w);document.getElementById('pTxt').value=st.pt||'';document.getElementById('oTxt').value=st.o||'';
 (st.v||[]).forEach((c,k)=>{{const i=document.querySelectorAll('.vis input')[k];if(i)i.checked=c;}});
 const OLD=['algesrio','casimiro','boahora7','casimiro170','madragoa','boavista','becoolival','cruzq','algesrep','estrela102','santos','olival','santost5'];const byId={{}};houses.forEach(h=>byId[h.dataset.id]=h);
 (st.h||[]).forEach((x,k)=>{{const h=byId[x[5]||OLD[k]];if(!h)return;press(h.querySelector('.btns'),x[0]);h.querySelector('.react textarea').value=x[1]||'';const an=h.querySelector('.agnote');if(an)an.value=x[2]||'';if(x[3]!==undefined){{const a=h.querySelector('.tk1'),b=h.querySelector('.tk2');if(a)a.checked=!!x[3]||a.checked;if(b)b.checked=!!x[4]||b.checked;}}}});return st.c||0;}}
// max 3 visits
document.querySelectorAll('.vis input').forEach(i=>i.addEventListener('change',()=>{{const on=document.querySelectorAll('.vis input:checked').length;document.querySelectorAll('.vis input').forEach(x=>x.disabled=on>=3&&!x.checked);}}));
// send through the website form (email to Pascale); WhatsApp only as fallback
document.getElementById('send').addEventListener('click',async function(){{const btn=this,txt=text();btn.setAttribute('aria-busy','true');btn.textContent='A enviar…';
 try{{const r=await fetch('https://api.web3forms.com/submit',{{method:'POST',headers:{{'Content-Type':'application/json',Accept:'application/json'}},body:JSON.stringify(Object.assign({{access_key:'4947213d-2aed-426f-ae63-a5d337eceac8',from_name:'pascalelisbonhomes.com',subject:'Client page feedback'}},{{'form-name':'selection-feedback','cliente':CLIENT,'ronda':'voorselectie 2','opiniao':txt,'respostas':VURL()}}))}});if(!r.ok)throw 0;
  const fin=btn.closest('.final');fin.querySelectorAll(':scope > *').forEach(x=>x.hidden=x.id!=='afterSend');document.querySelector('.bar').hidden=true;document.getElementById('prog')&&(document.getElementById('prog').parentElement.hidden=true);window.scrollTo({{top:0,behavior:'smooth'}});
  try{{localStorage.removeItem(KEY)}}catch(e){{}}
 }}catch(e){{btn.removeAttribute('aria-busy');btn.textContent='Enviar por WhatsApp';btn.onclick=()=>window.open('https://wa.me/351920609225?text='+encodeURIComponent(txt),'_blank');alert('Não foi possível enviar agora. Carreguem outra vez para enviar por WhatsApp.');}}}});
function VURL(){{try{{save();const j=localStorage.getItem(KEY)||'';return location.origin+location.pathname+'#ver='+btoa(unescape(encodeURIComponent(j))).replace(/\\+/g,'-').replace(/\\//g,'_').replace(/=+$/,'');}}catch(e){{return ''}}}}
const VW=location.hash.indexOf('#ver=')===0;if(VW){{try{{let b=location.hash.slice(5).replace(/-/g,'+').replace(/_/g,'/');while(b.length%4)b+='=';localStorage.setItem(KEY,decodeURIComponent(escape(atob(b))));}}catch(e){{}}}}

try{{const M=L.map('lmap',{{scrollWheelZoom:false}});L.tileLayer('https://tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png',{{attribution:'© OpenStreetMap',maxZoom:19}}).addTo(M);
const P={json.dumps([[h['n'],h['geo'][0],h['geo'][1],h['ready'],h['name'],h['price']] for h in HOUSES])};const pts=[];
P.forEach(([n,la,lo,rd,nm,pr])=>{{L.marker([la,lo],{{icon:L.divIcon({{className:'',html:'<div class="lpin'+(rd?'':' rn')+'">'+n+'</div>',iconSize:[28,28],iconAnchor:[14,14]}})}}).addTo(M).bindPopup('<b>'+n+'. '+nm+'</b><br>'+pr);pts.push([la,lo]);}});
L.marker([38.7075,-9.1702],{{icon:L.divIcon({{className:'',html:'<div class="lpin ref">★</div>',iconSize:[28,28],iconAnchor:[14,14]}})}}).addTo(M).bindPopup('Calçada das Necessidades, 3.º andar');
L.marker([38.7062,-9.1738],{{icon:L.divIcon({{className:'',html:'<div class="lpin home">⌂</div>',iconSize:[28,28],iconAnchor:[14,14]}})}}).addTo(M).bindPopup('Onde vivem agora');
M.fitBounds(pts,{{padding:[24,24]}});}}catch(e){{}}
const PRE={{"algesrio":"Voorstellen","casimiro":"Twijfel","boavista":"Twijfel","becoolival":"Twijfel","madragoa":"Twijfel"}};
if(!localStorage.getItem(KEY)){{houses.forEach(h=>{{const v=PRE[h.dataset.id];if(v)h.querySelectorAll('.btns button').forEach(x=>x.setAttribute('aria-pressed',String(x.dataset.v===v)));}});}}
load();{{const SUG={json.dumps({k:v[0] for k,v in SUG.items()})},SK=KEY+':sug2311c';try{{if(!localStorage.getItem(SK)){{houses.forEach(h=>{{const v=SUG[h.dataset.id];if(v)h.querySelectorAll('.btns button').forEach(x=>x.setAttribute('aria-pressed',String(x.dataset.v===v)));}});save();localStorage.setItem(SK,'1');}}}}catch(e){{}}}}legSync();show(0);
if(VW){{const sb=document.getElementById('send');if(sb){{sb.disabled=true;sb.textContent='Respostas enviadas pelo cliente';}}const bn=document.createElement('div');bn.textContent='Respostas de '+CLIENT+' · só para a Pascale';bn.style.cssText='background:#2e7d4f;color:#fff;text-align:center;padding:8px 12px;font:600 14px Inter,Arial,sans-serif';document.body.prepend(bn);}}
const nb=()=>{{if(document.getElementById('nl-badge-frame'))document.body.classList.add('nlb');}};nb();setTimeout(nb,800);setTimeout(nb,2500);
}})();
</script>
</body></html>'''

os.makedirs(OUT + '/img', exist_ok=True)
src = '/home/claude/pascalelisbonhomes-site/source/selections/antonio-mafalda-r7k2/img'
for h in HOUSES:
    for p in h['photos']:
        if p.startswith('img/'):
            dst = os.path.join(OUT, p)
            if not os.path.exists(dst): shutil.copy(os.path.join(src, os.path.basename(p)), dst)
open(OUT + '/index.html', 'w').write(page)
print('ok', len(page))

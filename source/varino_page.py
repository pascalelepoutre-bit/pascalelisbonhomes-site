"""Build the Varino 15 project page in EN/PT/FR/NL from the built For sale pages.
Run after build_site.py:  python3 source/varino_page.py
No prices, floor plans or finishes (developer's rule)."""
import re, pathlib, urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent / "site"
P = "/photos/varino15/"
GAL = [("varino-15-aerial-river-view.webp", 1262, 1474), ("varino-15-facade-balconies.webp", 1183, 1245), ("varino-15-living-room.webp", 1010, 634),
       ("varino-15-kitchen.webp", 1011, 636), ("varino-15-bedroom.webp", 1010, 636),
       ("varino-15-street-evening.webp", 1010, 635), ("varino-15-avenida-24-de-julho.webp", 1182, 1478),
       ("varino-15-courtyard-parking.webp", 1182, 1216)]

T = {
 "en": dict(pre="", title="Varino 15 · New apartments in Santos, Lisbon | Pascale Lepoutre",
  desc="Varino 15: 26 new turnkey apartments on Avenida 24 de Julho, between Santos and the river. T0+1 duplex to T3, terraces, parking with charging points. Completion early 2027.",
  eye="New development · Santos", h1="Varino 15",
  sub="26 new turnkey apartments on Avenida 24 de Julho, between Santos and the river",
  facts=[("T0+1 to T3", "from a one-bedroom to a duplex with rooftop"), ("63 to 127 m²", "balconies and terraces up to 55 m²"),
         ("26 homes", "two blocks of up to five floors"), ("Early 2027", "planned completion")],
  h2a="Why I like it", p1="A new building on Avenida 24 de Julho, a few minutes' walk from Santos and Madragoa. Every apartment is delivered turnkey, with an interior design by Varino: you move in without works or choices to make. Many homes have balconies or terraces, several with views of the river, and the top floors have private rooftops.",
  p2="Around the corner: Jardim de Santos, the Museu de Arte Antiga and the river. Santos station takes you to the Cascais beaches, and the centre is ten minutes away.",
  h2b="At a glance", list=["New build, turnkey, interior design by Varino", "T0+1 duplex, T1, T2 and T3", "Balconies and terraces, several with river views; private rooftops on the top floors", "Parking with charging points for electric cars", "Payment: 20% at the promissory contract, 80% at the deed", "Legal guarantee on new homes: 10 years for structural defects, 5 years for other defects", "Architects Francisco Monteiro and Artur Vilaça, Grupo Socicorreia"],
  h2c="Prices and floor plans", cta="Prices, floor plans and finishes are shared personally. Tell me what you are looking for and I'll send you the homes that are still available, with all the details, and arrange a visit.",
  wa="Ask me about Varino 15", call="Book a call", back="← All homes for sale", note="Images are 3D renders from the developer. Information subject to change.",
  wamsg="Hi Pascale, I'm interested in Varino 15 on Avenida 24 de Julho. Could you send me the available apartments and prices?"),
 "pt": dict(pre="/pt", title="Varino 15 · Apartamentos novos em Santos, Lisboa | Pascale Lepoutre",
  desc="Varino 15: 26 apartamentos novos chave na mão na Avenida 24 de Julho, entre Santos e o rio. Do T0+1 duplex ao T3, terraços, estacionamento com carregamento. Conclusão prevista no início de 2027.",
  eye="Empreendimento novo · Santos", h1="Varino 15",
  sub="26 apartamentos novos chave na mão na Avenida 24 de Julho, entre Santos e o rio",
  facts=[("T0+1 a T3", "do T1 ao duplex com rooftop"), ("63 a 127 m²", "varandas e terraços até 55 m²"),
         ("26 casas", "dois blocos até cinco pisos"), ("Início de 2027", "conclusão prevista")],
  h2a="Porque gosto deste projeto", p1="Um edifício novo na Avenida 24 de Julho, a poucos minutos a pé de Santos e da Madragoa. Cada apartamento é entregue chave na mão, com design de interiores da Varino: muda-se sem obras nem escolhas por fazer. Muitas casas têm varanda ou terraço, várias com vista rio, e os últimos pisos têm rooftop privado.",
  p2="Mesmo ao lado: o Jardim de Santos, o Museu de Arte Antiga e o rio. A estação de Santos leva-o às praias de Cascais e o centro fica a dez minutos.",
  h2b="Em resumo", list=["Construção nova, chave na mão, design de interiores Varino", "T0+1 duplex, T1, T2 e T3", "Varandas e terraços, vários com vista rio; rooftops privados nos últimos pisos", "Estacionamento com carregamento para carros elétricos", "Pagamento: 20% no CPCV, 80% na escritura", "Garantia legal de construção nova: 10 anos para defeitos estruturais, 5 anos para outros defeitos", "Arquitetos Francisco Monteiro e Artur Vilaça, Grupo Socicorreia"],
  h2c="Preços e plantas", cta="Os preços, plantas e acabamentos são partilhados pessoalmente. Diga-me o que procura e envio-lhe as casas ainda disponíveis, com todos os detalhes, e marcamos uma visita.",
  wa="Pergunte-me pelo Varino 15", call="Marcar uma chamada", back="← Todas as casas à venda", note="Imagens 3D do promotor. Informação sujeita a alterações.",
  wamsg="Olá Pascale, tenho interesse no Varino 15 na Avenida 24 de Julho. Pode enviar-me os apartamentos disponíveis e os preços?"),
 "fr": dict(pre="/fr", title="Varino 15 · Appartements neufs à Santos, Lisbonne | Pascale Lepoutre",
  desc="Varino 15 : 26 appartements neufs clés en main sur l'Avenida 24 de Julho, entre Santos et le fleuve. Du T0+1 duplex au T3, terrasses, parking avec recharge. Livraison prévue début 2027.",
  eye="Programme neuf · Santos", h1="Varino 15",
  sub="26 appartements neufs clés en main sur l'Avenida 24 de Julho, entre Santos et le fleuve",
  facts=[("T0+1 à T3", "du T1 au duplex avec rooftop"), ("63 à 127 m²", "balcons et terrasses jusqu'à 55 m²"),
         ("26 logements", "deux bâtiments jusqu'à cinq étages"), ("Début 2027", "livraison prévue")],
  h2a="Pourquoi j'aime ce projet", p1="Un immeuble neuf sur l'Avenida 24 de Julho, à quelques minutes à pied de Santos et de Madragoa. Chaque appartement est livré clés en main, avec un design intérieur signé Varino : vous emménagez sans travaux ni choix à faire. Beaucoup de logements ont un balcon ou une terrasse, plusieurs avec vue sur le fleuve, et les derniers étages ont un rooftop privé.",
  p2="Juste à côté : le Jardim de Santos, le Museu de Arte Antiga et le fleuve. La gare de Santos vous emmène aux plages de Cascais, et le centre est à dix minutes.",
  h2b="En bref", list=["Construction neuve, clés en main, design intérieur Varino", "T0+1 duplex, T1, T2 et T3", "Balcons et terrasses, plusieurs avec vue sur le fleuve ; rooftops privés aux derniers étages", "Parking avec bornes de recharge pour voitures électriques", "Paiement : 20 % au compromis, 80 % à l'acte", "Garantie légale du neuf : 10 ans pour les défauts structurels, 5 ans pour les autres défauts", "Architectes Francisco Monteiro et Artur Vilaça, Grupo Socicorreia"],
  h2c="Prix et plans", cta="Les prix, plans et finitions sont partagés personnellement. Dites-moi ce que vous cherchez et je vous envoie les logements encore disponibles, avec tous les détails, et nous organisons une visite.",
  wa="Demandez-moi Varino 15", call="Réserver un appel", back="← Toutes les maisons à vendre", note="Images 3D du promoteur. Informations susceptibles d'évoluer.",
  wamsg="Bonjour Pascale, Varino 15 sur l'Avenida 24 de Julho m'intéresse. Pouvez-vous m'envoyer les appartements disponibles et les prix ?"),
 "nl": dict(pre="/nl", title="Varino 15 · Nieuwe appartementen in Santos, Lissabon | Pascale Lepoutre",
  desc="Varino 15: 26 nieuwe, instapklare appartementen aan de Avenida 24 de Julho, tussen Santos en de rivier. Van T0+1 duplex tot T3, terrassen, parking met laadpunten. Oplevering begin 2027.",
  eye="Nieuwbouwproject · Santos", h1="Varino 15",
  sub="26 nieuwe, instapklare appartementen aan de Avenida 24 de Julho, tussen Santos en de rivier",
  facts=[("T0+1 tot T3", "van één slaapkamer tot duplex met dakterras"), ("63 tot 127 m²", "balkons en terrassen tot 55 m²"),
         ("26 woningen", "twee blokken tot vijf verdiepingen"), ("Begin 2027", "geplande oplevering")],
  h2a="Waarom ik het mooi vind", p1="Een nieuw gebouw aan de Avenida 24 de Julho, op een paar minuten wandelen van Santos en Madragoa. Elk appartement wordt instapklaar opgeleverd, met een interieurontwerp van Varino: je trekt erin zonder werken of keuzes. Veel woningen hebben een balkon of terras, verschillende met zicht op de rivier, en de bovenste verdiepingen hebben een eigen dakterras.",
  p2="Om de hoek: de Jardim de Santos, het Museu de Arte Antiga en de rivier. Vanuit station Santos ben je zo aan de stranden van Cascais, en het centrum ligt op tien minuten.",
  h2b="In het kort", list=["Nieuwbouw, instapklaar, interieurontwerp van Varino", "T0+1 duplex, T1, T2 en T3", "Balkons en terrassen, verschillende met rivierzicht; eigen dakterrassen op de bovenste verdiepingen", "Parking met laadpunten voor elektrische wagens", "Betaling: 20% bij de voorlopige koopovereenkomst, 80% bij de akte", "Wettelijke garantie op nieuwbouw: 10 jaar voor structurele gebreken, 5 jaar voor andere gebreken", "Architecten Francisco Monteiro en Artur Vilaça, Grupo Socicorreia"],
  h2c="Prijzen en plannen", cta="Prijzen, plannen en afwerking deel ik persoonlijk. Vertel me wat je zoekt, dan stuur ik je de woningen die nog beschikbaar zijn, met alle details, en plannen we een bezoek.",
  wa="Vraag me naar Varino 15", call="Plan een gesprek", back="← Alle woningen te koop", note="Beelden zijn 3D-renders van de projectontwikkelaar. Informatie onder voorbehoud.",
  wamsg="Hallo Pascale, ik ben geïnteresseerd in Varino 15 aan de Avenida 24 de Julho. Kun je me de beschikbare appartementen en prijzen sturen?"),
}

CSS = """<style>
.v15-hero{position:relative;min-height:min(82vh,700px);display:grid;align-items:end;background:#1d2430 url(/photos/varino15/varino-15-hero.webp) center 40%/cover no-repeat}
.v15-hero::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 35%,rgba(0,0,0,.55))}
.v15-hero .wrap{position:relative;z-index:1;padding-top:120px;padding-bottom:44px;color:#fff}
.v15-hero .eyebrow{color:#f7d98b}
.v15-hero h1{font-family:var(--display);font-weight:500;font-size:clamp(2.6rem,7vw,4.6rem);line-height:1;margin:.25em 0 .2em;color:#fff}
.v15-hero p{font-size:clamp(1.05rem,2.4vw,1.3rem);max-width:40ch}
.v15-back{display:inline-block;margin:28px 0 0;font-size:.95rem;color:var(--muted)}
.v15-facts{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;margin:28px 0 8px}
.v15-facts div{background:var(--sand,#f3ead9);border-radius:18px;padding:20px 18px}
.v15-facts b{display:block;font-family:var(--display);font-weight:500;font-size:1.45rem;line-height:1.15}
.v15-facts span{display:block;color:var(--muted);font-size:.95rem;margin-top:6px}
.v15-grid{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);gap:40px;margin:44px 0}
.v15 h2{font-family:var(--display);font-weight:500;font-size:clamp(1.5rem,3vw,2rem);margin-bottom:14px}
.v15 p.txt{font-size:1.08rem;line-height:1.65;margin-bottom:14px}
.v15 ul.v15-list{list-style:none;padding:0;margin:0;display:grid;gap:10px}
.v15 ul.v15-list li{position:relative;padding-left:26px;font-size:1.02rem;line-height:1.5}
.v15 ul.v15-list li::before{content:"";position:absolute;left:0;top:.55em;width:10px;height:10px;border-radius:50%;background:#f7d98b}
.v15-gal{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin:8px 0 44px}
.v15-gal img{width:100%;height:100%;aspect-ratio:4/3;object-fit:cover;border-radius:14px;cursor:zoom-in}
.v15-cta{background:#f7d98b;color:#2a2420;border-radius:24px;padding:34px 30px;margin:0 0 28px;display:grid;gap:18px}
.v15-cta p{font-size:1.1rem;line-height:1.6;max-width:62ch}
.v15-cta .row{display:flex;flex-wrap:wrap;gap:12px}
.v15-cta .btn{display:inline-flex;width:auto;border-radius:999px;border:1.5px solid #2a2420;color:#2a2420;background:transparent;padding:14px 24px}
.v15-cta .btn.solid{background:#2a2420;color:#fff}
.v15-note{color:var(--muted);font-size:.85rem;margin-bottom:56px}
.v15-lb{position:fixed;inset:0;z-index:90;background:rgba(15,15,15,.92);display:grid;place-items:center;padding:16px}
.v15-lb img{max-width:100%;max-height:90vh;border-radius:10px}
@media (max-width:860px){.v15-facts{grid-template-columns:repeat(2,minmax(0,1fr))}.v15-facts b{font-size:1.15rem}.v15-facts div{padding:16px 14px}.v15-grid{grid-template-columns:1fr;gap:28px}.v15-gal{grid-template-columns:repeat(2,minmax(0,1fr))}}
</style>"""

def page(lang):
    d = T[lang]; pre = d["pre"]
    src = (ROOT / (pre.strip("/") + "/for-sale/index.html" if pre else "for-sale/index.html")).read_text(encoding="utf-8")
    head, rest = src.split("<main id=\"top\">", 1)
    foot = rest.split("</main>", 1)[1]
    head = re.sub(r"<title>.*?</title>", "<title>" + d["title"] + "</title>", head, flags=re.S)
    head = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + d["desc"].replace('"', "&quot;"), head)
    for blob in (head, foot):
        pass
    fix = lambda s: re.sub(r'(href="(?:https://pascalelisbonhomes\.com)?(?:/pt|/fr|/nl)?/for-sale/)"', r'\1varino-15/"', s)
    head, foot = fix(head), fix(foot)
    head = head.replace("</head>", '<meta name="robots" content="noindex">\n' + CSS + "\n</head>", 1)
    wa = "https://wa.me/351920609225?text=" + urllib.parse.quote(d["wamsg"])
    facts = "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in d["facts"])
    lis = "".join(f"<li>{x}</li>" for x in d["list"])
    gal = "".join(f'<img src="{P}{f}" alt="Varino 15, Santos, Lisbon" loading="lazy" decoding="async" width="{w}" height="{h}">' for f, w, h in GAL)
    main = f"""<main id="top" class="v15">
<section class="v15-hero"><div class="wrap"><p class="eyebrow">{d['eye']}</p><h1>{d['h1']}</h1><p>{d['sub']}</p></div></section>
<div class="wrap">
<a class="v15-back" href="{pre}/for-sale/">{d['back']}</a>
<div class="v15-facts">{facts}</div>
<div class="v15-grid"><div><h2>{d['h2a']}</h2><p class="txt">{d['p1']}</p><p class="txt">{d['p2']}</p></div>
<div><h2>{d['h2b']}</h2><ul class="v15-list">{lis}</ul></div></div>
<div class="v15-gal">{gal}</div>
<div class="v15-cta"><h2>{d['h2c']}</h2><p>{d['cta']}</p><div class="row"><a class="btn solid" href="{wa}" target="_blank" rel="noopener">{d['wa']}</a><a class="btn" href="https://calendar.app.google/ThCV6Y9NR81k7fhr6" target="_blank" rel="noopener">{d['call']}</a></div></div>
<p class="v15-note">{d['note']}</p>
</div>
<script>document.querySelectorAll('.v15-gal img').forEach(function(i){{i.addEventListener('click',function(){{var b=document.createElement('div');b.className='v15-lb';b.innerHTML='<img alt="">';b.firstChild.src=i.src;b.onclick=function(){{b.remove()}};document.body.appendChild(b)}})}})</script>
</main>"""
    out = ROOT / ((pre.strip("/") + "/") if pre else "") / "for-sale/varino-15/index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(head + main + foot, encoding="utf-8")
    print("wrote", out)

for l in T:
    page(l)

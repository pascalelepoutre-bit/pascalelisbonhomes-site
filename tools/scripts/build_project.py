#!/usr/bin/env python3
"""Copy the Calçada project page (projeto-necessidades) for another house of a selection.
usage: KEEP=id1,id2 python3 build_project.py PORTAL_DIR
Writes PORTAL_DIR/projeto-<id>/index.html for each house. Not linked from the portal until the clients pick a visit."""
import os, re, html, json, sys
PORTAL = sys.argv[1]
TPL = open(os.path.join(PORTAL, 'projeto-necessidades/index.html')).read()
HOUSES=[];exec(open('/home/claude/clients/am_round2.py').read())
e = html.escape
eur = lambda n: f"{round(n):,}".replace(',', '.') + ' €'
ids = os.environ['KEEP'].split(',')
sel = [h for i in ids for h in HOUSES if h['id'] == i]
for h in sel:
    if h['id'] in globals().get('CLIENTNOTE',{}): h['note']=CLIENTNOTE[h['id']]
    if h['id'] in globals().get('CLIENTFIT',{}): h['fit']=CLIENTFIT[h['id']]
price = lambda h: int(h['price'].replace(' ', '').replace('€', ''))
# works scales: (min, max, default, three labels)
FULL = (1200, 1800, 1500, ('Simples', 'Boa qualidade', 'Alto padrão'))
UPD = (500, 1500, 1000, ('Atualizar', 'Média', 'Completa'))
READY = (0, 1000, 300, ('Sem obras', 'Pequenas', 'Médias'))
WORKS = {'casimiro185': FULL, 'casimiro170': UPD, 'algesrio': UPD}
LISBON_MKT = True
for h in sel:
    s = TPL
    pid, a, p = h['id'], AREA[h['id']], price(h)
    lo_m, hi_m, dflt, labs = WORKS.get(pid, READY)
    lisboa = 'Algés' not in h['name']
    # title, header
    s = s.replace('<title>Projeto Calçada das Necessidades</title>', f'<title>Projeto {e(h["name"])}</title>')
    s = re.sub(r'<header>.*?</header>', f'''<header>
    <p class="eyebrow">Para o António e a Mafalda · seleção 2</p>
    <h1>{e(h["name"])}</h1>
    <p class="lede">O custo total desta casa: compra, obras e impostos, para decidirem com números claros antes e depois da visita.</p>
    <div class="facts">{''.join(f'<span>{e(b)}</span>' for k, b in h['facts'] if k not in ('Planta','Estado'))}<span>Preço pedido {eur(p)}</span><span>{e(h["state"])}</span></div>
  </header>''', s, count=1, flags=re.S)
    s = re.sub(r'<section class="photos".*?</section>', f'<section class="photos" aria-label="Fotografia"><img class="hero" src="{h["photos"][0]}" alt="{e(h["name"])}"></section>', s, count=1, flags=re.S)
    val = f'Entre {eur(round(a*6547/1000)*1000)} e {eur(round(a*7000/1000)*1000)}. Valor criado: <em id="r-gain"></em>.' if lisboa else 'A confirmar com os preços de venda em Algés. <em id="r-gain" hidden></em>'
    s = re.sub(r'<section class="resumo".*?</section>', f'''<section class="resumo" aria-labelledby="h-res">
    <h2 id="h-res">Em resumo</h2>
    <ul>
      <li><b>A casa</b><span>{e(h["line"])}. {e(h["why"][0])}</span></li>
      <li><b>O custo total</b><span>Cerca de <em id="r-total"></em>, com a compra a <em id="r-price"></em>, obras de <em id="r-q"></em> e impostos.</span></li>
      <li><b>O valor depois</b><span>{val}</span></li>
    </ul>
  </section>''', s, count=1, flags=re.S)
    # calculator ranges
    step = 5000
    pmin = p - round(p * 0.2 / step) * step
    s = s.replace('<input type="range" id="price" min="480000" max="600000" step="5000" value="595000">', f'<input type="range" id="price" min="{pmin}" max="{p}" step="5000" value="{p}">')
    s = s.replace('<input type="range" id="m2" min="1200" max="1800" step="50" value="1500">', f'<input type="range" id="m2" min="{lo_m}" max="{hi_m}" step="50" value="{dflt}">')
    mid = (lo_m + hi_m) // 2
    s = re.sub(r'<div class="scale-q">.*?</div>', f'<div class="scale-q"><span>{labs[0]}<br>{eur(lo_m)}</span><span>{labs[1]}<br>{eur(mid)}</span><span>{labs[2]}<br>{eur(hi_m)}</span></div>', s, count=1, flags=re.S)
    s = s.replace('Começa em boa qualidade, à vossa medida.', 'O ponto de partida é uma estimativa para esta casa.')
    aru = ('Grande parte do centro de Lisboa fica na Área de Reabilitação Urbana, Aviso n.º 8391/2015. Confirmamos com a Câmara para este prédio. Uma empreitada de reabilitação pode ter IVA a 6%. O empreiteiro confirma.' if lisboa else
           'Em Oeiras há várias Áreas de Reabilitação Urbana. Confirmamos com a Câmara se este prédio está incluído; só aí uma empreitada de reabilitação pode ter IVA a 6%.')
    s = re.sub(r'<small>O prédio fica na Área de Reabilitação Urbana.*?</small>', f'<small>{aru}</small>', s, count=1, flags=re.S)
    s = s.replace('cerca de 120 m² ×', f'cerca de {a} m² ×')
    s = s.replace('valor mínimo: 786.000 €', f'valor mínimo: {eur(round(a*6547/1000)*1000)}').replace('pode chegar até 840.000 €', f'pode chegar até {eur(round(a*7000/1000)*1000)}').replace('120 m² × 6.547 a 7.000 €/m², o preço dos T4 mais caros vendidos na Estrela.', f'{a} m² × 6.547 a 7.000 €/m², o preço das casas renovadas mais caras vendidas na Estrela.')
    # JS constants
    s = s.replace('const AREA=120, FEES=8000, MAX=800000;', f'const AREA={a}, FEES=8000, MAX=800000;')
    s = s.replace('$("r-q").textContent=(m<1350?"qualidade simples":m<1650?"boa qualidade":"alto padrão")', f'$("r-q").textContent=(m<{lo_m+(hi_m-lo_m)//3}?"{labs[0].lower()}":m<{lo_m+2*(hi_m-lo_m)//3}?"{labs[1].lower()}":"{labs[2].lower()}")')
    s = s.replace('$("m-big").textContent=you<6547?`Remodelado, o apartamento custa-vos', '$("m-big").textContent=you<6547?`Com obras, a casa custa-vos').replace('Um T4 renovado na Estrela vende-se normalmente por mais de 6.547 €/m².', 'Uma casa renovada na Estrela vende-se normalmente por mais de 6.547 €/m².').replace(':`Remodelado, o apartamento custa-vos ${eur(you)}/m², ao nível do que se paga por um T4 renovado na Estrela.`', ':`Com obras, a casa custa-vos ${eur(you)}/m², ao nível do que se paga por uma casa renovada na Estrela.`')
    s = s.replace('["here","Este apartamento hoje, para remodelar",here]', '["here","Esta casa hoje, ao preço de compra",here]')
    # plan section and its script removed
    s = re.sub(r'<section aria-labelledby="h-idea">.*?</section>\s*(?=<section aria-labelledby="h-works">)', '', s, count=1, flags=re.S)
    i = s.find('/* Floor-plan planner')
    if i != -1:
        j = s.find('</script>', i); s = s[:i] + s[j:]
    # works list
    wl = {'FULL': ['Eletricidade e canalização novas', 'Cozinha aberta para a sala, com móveis e eletrodomésticos', 'Casas de banho completas', 'Pavimentos, paredes, tetos e pintura', 'Janelas novas com bom isolamento', 'Projeto, licenças e acompanhamento da obra'],
          'UPD': ['Pintura, pavimentos e pequenas reparações', 'Cozinha nova ou aberta para a sala', 'Atualização das casas de banho', 'Verificação da eletricidade e canalização'],
          'READY': ['Pequenos ajustes ao vosso gosto: pintura, luzes, armários', 'Mais, se quiserem abrir a cozinha ou mudar uma casa de banho']}
    kind = 'FULL' if (lo_m, hi_m) == FULL[:2] else 'UPD' if (lo_m, hi_m) == UPD[:2] else 'READY'
    s = re.sub(r'<section aria-labelledby="h-works">.*?</section>', f'''<section aria-labelledby="h-works">
    <h2 id="h-works">O que entra nas obras</h2>
    <ul class="incl">{''.join(f'<li>{x}</li>' for x in wl[kind])}</ul>
    <p class="note">Os valores por m² são médias com IVA a 23%, projeto e licenças. Depois da visita, pedimos orçamentos a empreiteiros.</p>
  </section>''', s, count=1, flags=re.S)
    others = ''.join(f'<div class="row"><div><b>{e(o["name"])}</b><br><span>{e(o["state"])}</span></div><em>{eur(price(o))}</em></div>' for o in sel if o['id'] != pid)
    s = re.sub(r'<section aria-labelledby="h-compare">.*?</section>', f'''<section aria-labelledby="h-compare">
    <h2 id="h-compare">Comparado com as outras casas</h2>
    <p>As outras casas da seleção 2, ao preço pedido:</p>
    <div class="compare">{others}<div class="row you"><div><b>{e(h["name"])}</b><br><span>com obras e impostos, tudo incluído</span></div><em id="c-total"></em></div></div>
  </section>''', s, count=1, flags=re.S)
    s = re.sub(r'<section aria-labelledby="h-future">.*?</section>\s*', '', s, count=1, flags=re.S)
    chk = [t for k, t in h['fit'] if k != 'ok'] + ['A luz em cada divisão', 'O estado das janelas, do chão e dos tetos', 'As partes comuns do prédio e obras previstas, na ata do condomínio', 'As medidas, para pedir orçamentos de obra']
    s = re.sub(r'<section aria-labelledby="h-visit">.*?</section>', f'''<section aria-labelledby="h-visit">
    <h2 id="h-visit">Para ver na visita</h2>
    <ul class="check">{''.join(f'<li>{e(x)}</li>' for x in chk)}</ul>
  </section>''', s, count=1, flags=re.S)
    s = re.sub(r'<section aria-labelledby="h-good">.*?</section>', f'''<section aria-labelledby="h-good">
    <h2 id="h-good">Bom saber</h2>
    <p>{e(h["note"])}</p>
    <p>Os valores das obras e dos impostos são estimativas prudentes para orientar a decisão. Depois da visita, podemos pedir orçamentos a empreiteiros e conversar sobre uma proposta.</p>
  </section>''', s, count=1, flags=re.S)
    if not lisboa:
        s = s.replace('</style>', '#h-mkt,#h-mkt~*,.vc{display:none!important}section[aria-labelledby="h-mkt"]{display:none}</style>', 1)
    os.makedirs(os.path.join(PORTAL, 'projeto-' + pid), exist_ok=True)
    open(os.path.join(PORTAL, 'projeto-' + pid, 'index.html'), 'w').write(s)
    print('ok', pid)

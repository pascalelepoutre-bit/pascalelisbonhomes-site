#!/usr/bin/env python3
"""Add the 'Homes for sale' view (E&V listings in Estrela, Lapa, Santos) to pascale-site.html.
Each card: photo gallery (5 photos), a short description in Pascale's voice, key features.
Re-runnable: replaces the view if it already exists. Areas = área bruta privativa (E&V 'total surface')."""
import re, html, urllib.parse

P = '/home/claude/pascale-site.html'
t = open(P, encoding='utf-8').read()

# ref, area, title, specs, price, photos, description, features
L = [
 dict(ref='W-049SUP', area='Lapa', title='Furnished T1 on Rua de Buenos Aires', specs=['1 bedroom','1 bathroom','55 m²'], price=385000,
      imgs='5aa1feb1-e306-4e1c-b47c-22dae07f9b34 a8ab2167-c52c-4d67-93b2-ff7717ab95de 09dd430c-4228-4a35-a29c-5ae060f88a3e e6f575b9-f939-4cbb-9e33-0f21a156358b df526567-f9a9-4b64-a7c0-fa2ebc3c522b',
      desc="A stylish ground-floor T1 on one of Lapa's most sought-after streets, with an open living and dining room and an integrated kitchen. Sold furnished, so you can move in or rent it out straight away.",
      feat=['Furnished','Ground floor','Investment or first home']),
 dict(ref='W-048RLP', area='Lapa', title='Bright T2 with balconies', specs=['2 bedrooms','1 bathroom','83 m²'], price=495000,
      imgs='aae7cf73-50dc-42fa-b2db-af1278a45953 e46bb2b6-6ead-4489-b7d4-06d357ad66ed d65defbc-880e-42b9-90e7-08839b81bc73 e054ce23-57aa-4a54-aadf-9f293b530133 d5abc231-7f4e-4c50-b724-1f891edebe16',
      desc="A light-filled T2 on the 2nd floor in a quiet street of Lapa, with a large living room and a kitchen that both open onto balconies. Good to know: it is sold with a lifetime usufruct, so it's a long-term investment rather than a home to move into now.",
      feat=['Balconies','Lift','Sold with usufruct']),
 dict(ref='W-02WI97', area='Santos', title='T2 in a fully renovated building', specs=['2 bedrooms','2 bathrooms','68 m²'], price=550000,
      imgs='2439356c-2680-49a0-8839-dc3e20acdc5e 132f47fb-e12d-461e-9115-2b62f9865b29 b711bcca-f22e-4189-82da-01eaf8c4f67c ddb58069-d3ed-4f84-b507-5d806410c412 760cf515-9bee-402e-8f7e-62c6f2a5ae53',
      desc="On the 4th floor of a building where every apartment had its own architecture and lighting project. Quality finishes, a fully equipped kitchen with plenty of storage, and Largo de Santos with its restaurants and shops at your door.",
      feat=['Lift','Renovated building','Next to Largo de Santos']),
 dict(ref='W-048DID', area='Estrela', title='Furnished T2 with river views', specs=['2 bedrooms','2 bathrooms','110 m²'], price=550000,
      imgs='75ac774e-a33d-407f-83d9-4e5f2e05169c ef5054f2-c866-4ff6-bafb-7203d80b6395 d2ca74ca-a357-45d1-9410-99ecfb043d81 bb956360-b633-4d0e-938a-1b8627f3563a 0e82165c-6d56-4f05-8780-e90f064f805e',
      desc="In a typical Portuguese building with views over the river. Two bedrooms (one en suite), two bathrooms, a living and dining room and a fully equipped kitchen. Sold fully furnished: ready to live in or to rent out.",
      feat=['River view','Furnished','En suite']),
 dict(ref='INFANTE', area='Estrela · Lapa', title='Infante Residences: new T1 and T2+1 flats', specs=['1 to 2+1 bedrooms','56 to 116 m²'], price=555000,
      imgs='e5e72359-9457-45da-b10b-928173afb91b da3304bb-78fc-406c-b627-8f2f604409fd 9dca806f-e06c-45a8-a350-3c8bf68fce81 c75b8ccf-25a8-4696-bec5-37a3511a2516 4dd0c7f1-2c4e-4a8f-accd-10e35ead1d3f',
      desc="A new luxury development at Avenida Infante Santo 34. T1 and T2+1 flats with en suite bedrooms, an open kitchen and living room, and a home office in the larger ones. Ten homes available, from € 555.000 to € 1.015.000.",
      feat=['New build','Pool','Parking space','Air conditioning','Lift']),
 dict(ref='W-04AAS5', area='Santos', title='Riverside T2 on Avenida 24 de Julho', specs=['2 bedrooms','3 bathrooms','115 m²'], price=650000,
      imgs='06fd8889-9764-4921-8521-d35f67ff932c 50864259-f2ab-4b45-a4c8-4080a4558876 d0c8aaed-a2cb-46b8-aaa4-24ad384ea32b 81407ef9-09a9-4793-b2d2-e2cf7689492a 538d0f8a-47a0-458f-a364-0d59e4c00904',
      desc="Fully renovated and designed by architect Ricardo Rosa, with views over the Tagus, the 25 de Abril Bridge and Cristo Rei. Lots of natural light, good sun all day and refined finishes throughout.",
      feat=['River and bridge view','Renovated','Architect design']),
 dict(ref='W-02LZMA', area='Estrela', title='T2 with garden and swimming pool', specs=['2 bedrooms','1 bathroom','111 m²'], price=750000,
      imgs='0cd3000c-f0fb-41b9-b8e1-810fb590fa94 025f746c-878a-4074-a910-b644c5547833 5624a441-92bc-4011-9465-18f246d120fa 1a8ed294-d6df-4ab8-b292-4be801fff49e 73a6dcfe-d810-4693-b661-76977499ea8e',
      desc="In a condominium with a tropical garden, swimming pool and 24-hour concierge, rare in the middle of Estrela. Bright, with views over the garden and the river. Kitchen with pantry and balcony, storage room and a parking space included.",
      feat=['Pool','Garden','Concierge','Garage','Lift']),
 dict(ref='W-04BNAR', area='Estrela', title='T2 with private terrace and garage', specs=['2 bedrooms','2 bathrooms','106 m²'], price=750000,
      imgs='db543573-2c7e-40cc-b493-cafa41ba937f c2e878d3-caef-400d-ad36-86ae7325f124 8472aff1-6b48-4ffa-943c-ae701da0e715 08fc15c4-3d32-4b18-a0f4-b26f96a3269c 8ad1588e-dd33-4c41-a7e8-d8f15f883c7c',
      desc="Move-in ready on Travessa da Costa, in a building fully renovated in 2023. Third floor with lift, facing south and west, with a generous terrace and a private parking space. Energy rating B.",
      feat=['Terrace','Parking space','Lift','Energy class B']),
 dict(ref='W-049HVO', area='Santos', title='Pombaline apartment with river view', specs=['2 bedrooms + 3 rooms','2 bathrooms','145 m²'], price=770000,
      imgs='b4eb64e8-c4d5-4506-9a62-b8f7fd906299 0d970b89-fc60-4c07-bbda-c31a3810b0c6 310868fe-5a8a-4143-8239-198ca9a9136d b238acd2-d9e8-42ea-b42d-d0ee29d990be 027516fb-226d-4238-9569-98b965461073',
      desc="In an elegant Pombaline building with a frontal view of the river and two independent entrances. Two bedrooms with small balconies, plus three flexible rooms for an office, a walk-in closet or guests, and a spacious living and dining room.",
      feat=['River view','Balconies','Historic building']),
 dict(ref='W-04AF7D', area='Estrela', title='T4 duplex near Jardim da Estrela', specs=['4 bedrooms','2 bathrooms','132 m²'], price=850000,
      imgs='51d72630-49ee-4329-b56d-12407927d1b8 4a85cbac-24b1-47b6-9c1c-51961ce85aa3 c10b7bde-5433-4fd7-a0a2-6ce36b73069f fc3c5cb5-98ba-4818-8784-eabe0128e888 8a0d6d2f-e237-4623-b3d8-4963e89cfe9c',
      desc="A charismatic duplex with hardwood floors and lovely light. Living room, separate dining room, kitchen and bathroom downstairs; the bedrooms with built-in wardrobes and a second bathroom upstairs. Storage room in the building.",
      feat=['Duplex','Hardwood floors','Storage room']),
 dict(ref='W-04BOIG', area='Lapa', title='T4+1 with terrace, lift and garage', specs=['4 bedrooms','2 bathrooms','178 m²'], price=895000,
      imgs='7d292675-f614-460e-b417-1ee209054cca 43997531-1abb-4c5a-88f8-79159d312759 f23cc589-039c-4be1-9bd4-ee25df6f5a83 1d3e0f34-16fa-4b99-9dc1-0bb6dc7fae8b 40a45ccc-41e3-4f00-8e42-e748e0a830c2',
      desc="A period building in Lapa with what is so rare in Lisbon: garage, lift and a private terrace. South-facing living room, a formal dining room with high ceilings and original wood floors. Kitchen, bathrooms and infrastructure renovated in 2016.",
      feat=['Terrace','Garage','Lift','South facing']),
 dict(ref='W-04BWE8', area='Lapa', title='Renovated house with 3 suites', specs=['3 suites','4 bathrooms','245 m²'], price=900000,
      imgs='c59fc764-a155-4b9b-9978-a20b9cd565e0 a38c718f-a87f-4094-8230-7f9c6a64dc43 4ba3c2f9-c8b4-4a63-ad6c-ac5eeb83fb15 d611cb64-0c1b-4e60-afcf-d3727d1af139 ee66d1af-1b40-4fb7-9465-3d89e4e9e181',
      desc="A whole house over three floors, fully rehabilitated while keeping its original charm. Living room, modern kitchen and a patio on the entrance floor, two suites above, and a top floor entirely for the master suite.",
      feat=['Patio','Air conditioning','Independent house']),
 dict(ref='W-02WRUI', area='Santos', title='Designer T2 in the Santos Townhouse', specs=['2 bedrooms','2 bathrooms','103 m²'], price=915000,
      imgs='33dc22d2-e1de-4aaf-b9d2-83344687b03c ac3fdebc-e3ad-4eeb-b90d-a520f549dfa2 6429eb15-05da-4db5-b1c8-4ed139395977 74a21e8d-5d70-40f2-afb3-e23881a58531 415851f6-3b71-45b3-a7da-608863ef8027',
      desc="A historic building with a beautiful tiled façade, between Lapa and Santos. Contemporary interiors by renowned designers: a bright living room, open kitchen, two bedrooms (one en suite) and a work area. Third floor with lift.",
      feat=['Lift','Tiled façade','Designer interiors']),
 dict(ref='W-04ARF3', area='Estrela', title='Plot with approved project for a house with pool', specs=['137 m² plot','350 m² approved'], price=1050000,
      imgs='751a5c14-aa60-45a1-b117-8babdbe24517 a61b3eea-ece4-4be4-b290-396061fe29a3 885e4c27-9741-4bc1-8ab0-b4ac0000c6db ae7bb223-887e-460e-b820-1cc5fdf91ea7 2cfd4a54-9e38-4a80-89e7-216c99e8af45',
      desc="In one of Estrela's quietest residential streets, with the architecture project already approved by Lisbon City Council, so building can start right away. A house with 3 bedrooms, garden and pool, plus a 36 m² courtyard.",
      feat=['Approved project','Pool planned','Courtyard']),
 dict(ref='W-0497KP', area='Santos', title='Renovated T3 penthouse', specs=['3 bedrooms','2 bathrooms','175 m²'], price=1150000,
      imgs='138e085b-c913-4ae6-89e7-06a82822c7a4 937917d0-dbe8-4b1c-9f5f-5af1162e616d 116298d0-91fa-40e8-b0cc-c87793994f54 36f72a09-6991-4034-950f-48b2fb588bf1 6396b276-030e-4447-97ae-279d9908861d',
      desc="A fully renovated penthouse in a historic Santos building, with a contemporary design. Well-proportioned rooms with light from many windows, a large living and dining room, a carefully designed kitchen and three bedrooms.",
      feat=['Penthouse','Renovated','Historic building']),
 dict(ref='W-04AF90', area='Estrela', title='T4+1 with river view on Infante Santo', specs=['4 suites','5 bathrooms','192 m²'], price=1200000,
      imgs='4553cb21-dd81-460a-8276-087f37b40127 34753d28-6d55-47d7-9c9a-078d26c6e6b4 59e42bac-1ef8-421d-b3fe-d7e210d9cbae 159371b7-7793-4097-a080-6283a098c832 8b98657e-6d4f-4dba-9788-7eef492e9417',
      desc="On Avenida Infante Santo, with a view over the Tagus. Four en suite bedrooms plus an office, generous living spaces full of light, and a parking space. Fifth floor.",
      feat=['River view','4 suites','Office','Parking space']),
 dict(ref='W-049YUJ', area='Estrela', title='Contemporary villa in Necessidades', specs=['3 suites','6 bathrooms','377 m²'], price=2250000,
      imgs='ced8a59c-b0d1-42db-9761-2125a748b93f c9624cd9-2d5f-4f1e-8cac-9df9f33531ee 6f55cd7f-79a4-417d-946d-77670ce3a8c6 d103e4ed-2e0b-421a-9df2-b737cf8db31e 094000cb-9d23-4534-9423-bb13d817b286',
      desc="A singular contemporary villa over four floors, with its own lift between the levels. Three spacious suites, an extra room on the top floor, high-quality finishes, a river view and parking.",
      feat=['Private lift','River view','Parking space']),
 dict(ref='W-047PXH', area='Lapa', title='Building with 4 apartments and AL licence', specs=['4 apartments','8 bathrooms','310 m²'], price=2500000,
      imgs='548ea43e-7500-4c5f-8b01-1daca8e0ebdf f9294034-88fa-4378-b614-86c99258ed00 16b6a0e2-83c6-4d37-a1e8-644c65fb5868 70017ce6-e33b-4c72-85ab-2ef8b93342e6 cfa445c8-ef6d-41b9-b5d5-15367f291877',
      desc="An early 20th-century building with one apartment of about 75 m² per floor, with a local accommodation (AL) licence. Close to the river, the embassies, Jardim da Estrela and tram 28: strong demand from both visitors and residents.",
      feat=['Whole building','AL licence','Terrace']),
 dict(ref='W-04AG11', area='Estrela', title='Riverside loft in a Gustave Eiffel building', specs=['1 bedroom','2 bathrooms','360 m²'], price=2600000,
      imgs='c54e171d-beff-47fd-9caa-08c5aec733d9 77a9645e-79bf-469f-b276-55b21e790d00 0292a67e-60a0-41fb-9483-b210e8699cf8 9eb9f8db-50f5-4b8e-8198-00035696028a 160f1d38-f1d7-4cf1-a3a5-94183442f833',
      desc="A duplex loft with mezzanine in an iconic building originally designed by Gustave Eiffel. Open plan with panoramic windows and unobstructed views over the Tagus, high ceilings, a fireplace, a premium kitchen and two parking spaces.",
      feat=['River view','Fireplace','2 parking spaces','Air conditioning']),
 dict(ref='W-049R1S', area='Estrela', title='Contemporary house with pool', specs=['4 bedrooms','4 bathrooms','420 m²'], price=4700000,
      imgs='94c17179-39da-4c7f-985b-4f9249155781 5a835f4d-28b8-4c85-82ba-fb2ed908cadd 942131a6-12bf-43ea-86c1-a3cb260c121a b52a6de0-836b-49eb-9f48-4193cee7d130 dbba0b5f-11d7-42d3-87d8-37eb582ee2da',
      desc="A contemporary house over three floors, with large windows that bring in light all day and connect inside and outside. Private pool, a mezzanine for a gym or studio, and parking for three cars. Close to the riverside and Santos.",
      feat=['Private pool','3 parking spaces','Gym mezzanine']),
 dict(ref='W-04BF4C', area='Lapa', title='Penthouse with private pool and river views', specs=['4 bedrooms','4 bathrooms','652 m²'], price=5600000,
      imgs='4a8e3989-bc26-4d60-90ef-196560445a41 7d3cad37-7df0-4f50-9ec1-c5cf6bf16b25 d7725d53-d07c-4dbd-8b15-a36e3b7f73d2 4c1d60fc-da06-4b7a-8595-bd199aa5101a 26ab4e10-1b5e-4aa0-a76c-50fae6ef7efa',
      desc="A duplex penthouse with double-height ceilings and floor-to-ceiling windows framing the Tagus and the 25 de Abril Bridge. Open living, dining and kitchen area, a gallery upstairs, a terrace with private pool and two parking spaces.",
      feat=['Private pool','Terrace','River view','2 parking spaces']),
]

BEDS = {'INFANTE': '1,2', 'W-04ARF3': 3, 'W-047PXH': ''}
FEATS = {'W-049SUP': '', 'W-048RLP': 'lift', 'W-02WI97': 'lift', 'W-048DID': 'river', 'INFANTE': 'lift,garage', 'W-04AAS5': 'river', 'W-02LZMA': 'river,garden,lift,garage', 'W-04BNAR': 'terrace,lift,garage', 'W-049HVO': 'river', 'W-04AF7D': '', 'W-04BOIG': 'terrace,lift,garage', 'W-04BWE8': 'terrace,garden', 'W-02WRUI': 'lift', 'W-04ARF3': 'garden', 'W-0497KP': '', 'W-04AF90': 'river,garage', 'W-049YUJ': 'river,lift,garage', 'W-047PXH': 'terrace', 'W-04AG11': 'river,garage', 'W-049R1S': 'garage', 'W-04BF4C': 'river,terrace,garage'}
MINE_EXTRA = 'b1198778-1882-4ddf-98c0-29fa2c35e6c4 f3f98073-fb05-4115-8583-ed5ac8ca25b2 f35fe61a-7a5a-4fb3-81c9-fb6fc897ab46 9197649c-ec99-48dc-b069-dc7ee96955c1'

eur = lambda n: '€ ' + f'{n:,}'.replace(',', '.')
img = lambda i: f'https://uploadcare.engelvoelkers.com/{i}/-/format/webp/-/stretch/off/-/progressive/yes/-/scale_crop/800x600/center/-/quality/lighter/'
e = lambda s: html.escape(s, quote=True)

def wa(ref, title, area, price_txt):
    head = f'Ref. {ref} · ' if ref != 'INFANTE' else ''
    msg = f"Hi Pascale, I'm interested in this home:\n{head}{title}, {area.split(' · ')[0]} · {price_txt}\nCould you tell me more and arrange a viewing?"
    return 'https://wa.me/351920609225?text=' + urllib.parse.quote(msg, safe='')

def gallery(srcs, alt, pills):
    n = len(srcs)
    imgs = ''.join(f'<img src="{s}" alt="{e(alt)}{"" if i == 0 else f", photo {i+1}"}" loading="lazy" decoding="async" width="800" height="600">' for i, s in enumerate(srcs))
    nav = (f'<button type="button" class="g-btn g-prev" aria-label="Previous photo">‹</button>'
           f'<button type="button" class="g-btn g-next" aria-label="Next photo">›</button>'
           f'<span class="g-count">1 / {n}</span>') if n > 1 else ''
    return f'<div class="photo gal"><div class="g-track">{imgs}</div>{nav}{pills}</div>'

cards = []
# my own listing: my bridge photo first, then the E&V photos
mine = re.search(r'<article class="listing">\s*<div class="photo"[^>]*><span class="pill mine">.*?</article>', t, re.S).group(0)
mine_src = re.search(r'url\((data:image/[^)]+)\)', mine).group(1)
mine_pills = re.search(r'(<span class="pill mine">.*?</span><span class="pill inv">.*?</span>)', mine).group(1)
mine_alt = 'T4 apartment for sale on Calçada das Necessidades, Estrela, Lisbon, with a view of the 25 de Abril bridge'
mine_card = re.sub(r'<div class="photo".*?</div>', gallery([mine_src] + [img(i) for i in MINE_EXTRA.split()], mine_alt, mine_pills), mine, count=1, flags=re.S)
mine_card = re.sub(r'<p class="feat">.*?</p>',
    '<p class="feat">A four-bedroom apartment between Estrela, Lapa and Alcântara, with views over the river and the bridge. '
    'It is sold with a tenant under a lease from 1984, so it is for long-term investors rather than for living in. '
    'Ask me for the investor study with the expected rental return.</p>\n            '
    '<p class="hl"><span>Investor opportunity</span><span>River and bridge view</span><span>Energy class F</span></p>\n            '
    '<p class="g-note">Interior photos show the identical apartment one floor below.</p>', mine_card, count=1, flags=re.S)
cards.append(mine_card.replace('<article class="listing">', '<article class="listing" data-area="Estrela" data-beds="4" data-feat="river">', 1))

for x in L:
    ref, area, title, price = x['ref'], x['area'], x['title'], x['price']
    price_txt = ('From ' if ref == 'INFANTE' else '') + eur(price)
    ref_html = f'<span class="ref">Ref. {ref}</span>' if ref != 'INFANTE' else '<span class="ref">10 homes available</span>'
    alt = f'{title}, for sale in {area.replace(" · ", " and ")}, Lisbon'
    beds = BEDS.get(ref)
    if beds is None:
        m = re.match(r'(\d+)', x['specs'][0]); beds = int(m.group(1)) if m and 'bed' in x['specs'][0] or m and 'suite' in x['specs'][0] else ''
    cards.append(f'''        <article class="listing" data-area="{e(area)}" data-beds="{beds}" data-feat="{FEATS.get(ref, '')}">
          {gallery([img(i) for i in x['imgs'].split()], alt, '<span class="pill">Engel &amp; Völkers</span>')}
          <div class="info">
            <span class="parts">{e(area)}</span>{ref_html}
            <h3>{e(title)}</h3>
            <p class="specs">{''.join(f'<span>{s}</span>' for s in x['specs'])}</p>
            <p class="feat">{e(x['desc'])}</p>
            <p class="hl">{''.join(f'<span>{e(f)}</span>' for f in x['feat'])}</p>
            <p class="price">{price_txt}</p>
            <a class="more" href="{wa(ref, title, area, price_txt)}" target="_blank" rel="noopener">Ask me about this home →</a>
          </div>
        </article>''')

invite = re.search(r'<article class="listing invite">.*?</article>', t, re.S).group(0)

view = f'''<div class="view" data-view="homes" hidden>
  <section class="page-head">
    <div class="wrap center" style="margin-bottom:0">
      <p class="eyebrow">For sale</p>
      <h1>Homes for sale in Estrela, Lapa &amp; Santos</h1>
      <p class="sub">My own listings and those of my Engel &amp; Völkers colleagues in the Estrela parish. Interested in one? Message me directly. I'll send you all the details and arrange your viewing.</p>
    </div>
  </section>
  <section class="tight" id="all-homes">
    <div class="wrap">
      <div class="tabs" id="home-filter" aria-label="Filter by neighbourhood">
        <button type="button" class="on" aria-pressed="true" data-f="">All</button>
        <button type="button" aria-pressed="false" data-f="Estrela">Estrela</button>
        <button type="button" aria-pressed="false" data-f="Lapa">Lapa</button>
        <button type="button" aria-pressed="false" data-f="Santos">Santos</button>
      </div>
      <div class="tabs beds" id="bed-filter" aria-label="Number of bedrooms">
        <span class="f-label">Bedrooms</span>
        <button type="button" class="on" aria-pressed="true" data-b="0">Any</button>
        <button type="button" aria-pressed="false" data-b="1">T1</button>
        <button type="button" aria-pressed="false" data-b="2">T2</button>
        <button type="button" aria-pressed="false" data-b="3">T3</button>
        <button type="button" aria-pressed="false" data-b="4">T4+</button>
      </div>
      <div class="tabs beds" id="feat-filter" aria-label="Must have">
        <span class="f-label">Must have</span>
        <button type="button" aria-pressed="false" data-x="river">River view</button>
        <button type="button" aria-pressed="false" data-x="terrace">Terrace</button>
        <button type="button" aria-pressed="false" data-x="garden">Garden</button>
        <button type="button" aria-pressed="false" data-x="lift">Lift</button>
        <button type="button" aria-pressed="false" data-x="garage">Garage</button>
      </div>
      <p class="f-none" id="f-none" hidden>No homes match these choices right now. <a href="#contact">Tell me what you're looking for</a> and I'll let you know when one comes up.</p>
      <div class="listings">
{chr(10).join(cards)}
        {invite}
      </div>
      <p class="hood-src">Prices and availability as published by Engel &amp; Völkers. Areas are the área bruta privativa. Updated November 2026.</p>
    </div>
  </section>
</div>
'''

t = re.sub(r'<div class="view" data-view="homes" hidden>.*?\n</div>\n', '', t, flags=re.S)
t = t.replace('</main>', view + '</main>', 1)

btn = '\n      <div class="center see-all" style="margin:44px 0 0"><a class="btn" href="#homes">See all homes in Estrela, Lapa &amp; Santos</a></div>'
if 'class="center see-all"' not in t:
    i = t.index('id="for-sale"')
    j = t.index('<article class="listing invite">', i)
    j = t.index('</div>', t.index('</article>', j)) + len('</div>')
    t = t[:j] + btn + t[j:]

t = t.replace('<li><a href="#for-sale">For sale</a></li>', '<li><a href="#homes">For sale</a></li>')
t = t.replace("const VIEWS=['home','neighbourhoods','my-lisbon','buying'];", "const VIEWS=['home','neighbourhoods','my-lisbon','buying','homes'];")

JS = '''
const hf=document.getElementById('home-filter'),bf=document.getElementById('bed-filter'),xf=document.getElementById('feat-filter');
if(hf&&bf){let fa='',fb=0;const fx=new Set();
  const apply=()=>{let n=0;hf.parentElement.querySelectorAll('.listing[data-area]').forEach(c=>{const bs=c.dataset.beds===''?[]:c.dataset.beds.split(',').map(Number);
    const ok=(!fa||c.dataset.area.includes(fa))&&(!fb||bs.some(b=>fb===4?b>=4:b===fb))&&[...fx].every(x=>c.dataset.feat.split(',').includes(x));c.hidden=!ok;if(ok)n++;});document.getElementById('f-none').hidden=n>0;};
  const pick=(box,b)=>box.querySelectorAll('button').forEach(x=>{const on=x===b;x.classList.toggle('on',on);x.setAttribute('aria-pressed',on);});
  hf.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;pick(hf,b);fa=b.dataset.f;apply();});
  bf.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;pick(bf,b);fb=+b.dataset.b;apply();});
  if(xf)xf.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;const on=!fx.has(b.dataset.x);on?fx.add(b.dataset.x):fx.delete(b.dataset.x);b.classList.toggle('on',on);b.setAttribute('aria-pressed',on);apply();});}
document.querySelectorAll('.gal').forEach(g=>{const tr=g.querySelector('.g-track'),ct=g.querySelector('.g-count');if(!ct)return;const n=tr.children.length;
  const idx=()=>Math.round(tr.scrollLeft/tr.clientWidth);
  const go=d=>{const i=(idx()+d+n)%n;tr.scrollTo({left:i*tr.clientWidth,behavior:'smooth'});};
  g.querySelector('.g-prev').addEventListener('click',()=>go(-1));g.querySelector('.g-next').addEventListener('click',()=>go(1));
  tr.addEventListener('scroll',()=>{ct.textContent=(idx()+1)+' / '+n;},{passive:true});});
'''
s0 = t.rindex('<script>')
script = t[s0:]
script = re.sub(r"\nconst hf=document\.getElementById\('home-filter'\).*?(?=</script>)", '', script, flags=re.S)
script = script.replace('</script>', JS + '</script>', 1)
t = t[:s0] + script

CSS = ('.gal .g-track{position:absolute;inset:0;display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none}'
       '.gal .g-track::-webkit-scrollbar{display:none}'
       '.gal .g-track img{flex:0 0 100%;width:100%;height:100%;max-width:none;object-fit:cover;scroll-snap-align:start;display:block;color:transparent;font-size:0}'
       '.g-btn{position:absolute;top:50%;transform:translateY(-50%);z-index:2;width:34px;height:34px;border-radius:50%;border:0;background:rgb(255 255 255 / .85);color:#2a2420;font-size:1.3rem;line-height:1;cursor:pointer;opacity:0;transition:opacity .2s}'
       '.g-prev{left:10px}.g-next{right:10px}.listing:hover .g-btn,.g-btn:focus-visible{opacity:1}'
       '@media (hover:none){.g-btn{opacity:.9}}'
       '.g-count{position:absolute;right:12px;bottom:12px;z-index:2;background:rgb(42 36 32 / .6);color:#fff;font-size:.72rem;padding:3px 9px;border-radius:999px}'
       '.g-note{font-size:.78rem;color:var(--muted);font-style:italic}'
       '.listing .hl{margin-top:2px}'
       '#home-filter,#bed-filter{margin-bottom:12px}.tabs.beds{align-items:center;gap:6px}.tabs.beds button{padding:8px 16px}'
       '.f-label{font-family:var(--display);font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin-right:6px}'
       '@media (max-width:600px){#home-filter,.tabs.beds{gap:6px}#feat-filter button{padding:7px 11px}#home-filter button,.tabs.beds button{padding:8px 12px;font-size:.64rem;letter-spacing:.1em}.f-label{width:100%;text-align:center;margin:4px 0 0}}'
       '.f-none{text-align:center;color:var(--muted);margin:-12px 0 32px}.f-none a{color:var(--red);text-decoration:underline;text-underline-offset:3px}')
t = re.sub(r'\n/\* gallery \*/.*', '', t)
t = t.replace('.tabs button.on{', '\n/* gallery */' + CSS + '\n.tabs button.on{', 1) if '/* gallery */' not in t else t
if '/* gallery */' not in t:
    raise SystemExit('css anchor missing')

open(P, 'w', encoding='utf-8').write(t)
print('cards:', len(cards))

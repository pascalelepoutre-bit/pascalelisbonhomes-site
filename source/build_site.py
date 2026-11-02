#!/usr/bin/env python3
"""Build the multi-page SEO version of Pascale's site from pascale-site.html.
Design and text stay identical; only structure, head tags, images and links change."""
import re, io, base64, json, html, shutil, os
from PIL import Image

SRC = '/home/claude/pascale-site.html'
OUT = '/home/claude/site'
DOMAIN = 'https://pascalelisbonhomes.com'
TODAY = '2026-11-01'

t = open(SRC, encoding='utf-8').read()
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT + '/img')

# ---------- 1. split the source ----------
css = re.search(r'<style>(.*?)</style>', t, re.S).group(1)
symbols = re.search(r'<svg width="0" height="0".*?</svg>', t, re.S).group(0)
header = re.search(r'<header>.*?</header>', t, re.S).group(0)
footer = re.search(r'<footer>.*?</footer>', t, re.S).group(0)
script = t[t.rindex('<script>'):t.rindex('</script>') + 9]
fonts = re.findall(r'<link rel="(?:preconnect|stylesheet)"[^>]*>', t)
fonts_url = [l for l in fonts if 'stylesheet' in l][0]

views = {}
starts = [(m.start(), m.group(1)) for m in re.finditer(r'<div class="view" data-view="([^"]+)"', t)]
main_end = t.index('</main>')
for i, (s, name) in enumerate(starts):
    e = starts[i + 1][0] if i + 1 < len(starts) else main_end
    views[name] = t[s:e].rstrip()

# ---------- 2. images: data URIs -> real files ----------
ALTS = {
    'W-04BZY4': ('necessidades', 'T4 apartment for sale on Calçada das Necessidades, Estrela, Lisbon, with a view of the 25 de Abril bridge'),
    'W-04BOIG': ('t4-lapa', 'T4 apartment with terrace for sale in Lapa, Lisbon'),
    'W-04BF4C': ('penthouse-lapa', 'Penthouse with private pool and river views for sale in Lapa, Lisbon'),
    'W-04BNAR': ('t2-estrela', 'T2 apartment with private terrace for sale in Estrela, Lisbon'),
    'W-02XVJ7': ('t3-unique-belem', 'T3 apartment with garage in the Unique Belém development, Lisbon'),
    'Último Porto': ('ultimo-porto', 'Inside Último Porto restaurant, by the port of Lisbon'),
    'Maiz do Mar': ('maiz-do-mar', 'Inside Maiz do Mar, Mexican fusion restaurant in Lisbon'),
    'Clube de Jornalistas': ('clube-de-jornalistas', 'Clube de Jornalistas restaurant logo, Lapa, Lisbon'),
    'Baraza Yoga': ('baraza-yoga', 'The yoga room at Baraza Yoga, Lisbon'),
    'mvmt.studio': ('mvmt-studio', 'Inside mvmt.studio, movement classes in Lisbon'),
}

def save_img(b64, slug, maxw=1400):
    im = Image.open(io.BytesIO(base64.b64decode(b64)))
    has_alpha = im.mode in ('RGBA', 'LA', 'P')
    im = im.convert('RGBA' if has_alpha else 'RGB')
    if im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    path = f'img/{slug}.webp'
    im.save(f'{OUT}/{path}', 'WEBP', quality=80, method=6)
    return '/' + path, im.size

bg_re = re.compile(r'<div class="(photo|place-photo[^"]*)"([^>]*?) style="background:([^"]*?)url\(data:image/\w+;base64,([A-Za-z0-9+/=]+)\)\s*([^"]*)"([^>]*)>')

def bg_to_img(chunk):
    def rep(m):
        cls, aria, bgcolor, b64, rest, aria2 = m.groups()
        context = re.sub(r'<[^>]+>', ' ', chunk[m.end():m.end() + 1200])
        hits = [(context.find(k), k) for k in ALTS if k in context]
        key = min(hits)[1]
        slug, alt = ALTS[key]
        src, (w, h) = save_img(b64, slug)
        pos, _, size = rest.partition('/')
        size = size.replace('no-repeat', '').strip()
        fit = 'cover' if size == 'cover' else 'contain'
        style = f'object-fit:{fit};object-position:{pos.strip() or "center"}'
        if fit == 'contain':  # logo shown at 80% height on white
            style += ';top:10%;height:80%'
        bg = f' style="background:{bgcolor.strip()}"' if bgcolor.strip() else ''
        return (f'<div class="{cls}"{bg}><img class="cover-img" src="{src}" alt="{html.escape(alt, quote=True)}" '
                f'width="{w}" height="{h}" loading="lazy" decoding="async" style="{style}">')
    return bg_re.sub(rep, chunk)

for k in views:
    views[k] = bg_to_img(views[k])
    def rep_img(m):
        alt = re.search(r'alt="([^"]*)"', m.group(2)).group(1).lower()
        slug = 'necessidades' if 'necessidades' in alt else ('living-room-sessions-logo' if 'living room' in alt else re.sub(r'[^a-z0-9]+', '-', alt)[:40].strip('-'))
        src, _ = save_img(m.group(1), slug, 1400 if slug == 'necessidades' else 600)
        return f'<img src="{src}" loading="lazy" decoding="async"{m.group(2)}>'
    views[k] = re.sub(r'<img src="data:image/\w+;base64,([A-Za-z0-9+/=]+)"([^>]*)>', rep_img, views[k])
    assert 'base64' not in views[k], k

shutil.copy('/home/claude/img/share.png', f'{OUT}/img/share.png')
if os.path.exists('/home/claude/SETUP.md'): shutil.copy('/home/claude/SETUP.md', f'{OUT}/SETUP.md')

# ---------- 3. links: hash views -> real URLs ----------
PATH = {'home': '/', 'neighbourhoods': '/neighbourhoods/', 'my-lisbon': '/my-lisbon/', 'buying': '/buying/', 'homes': '/for-sale/', 'market-report': '/market-report/'}
id_page = {}
for name, chunk in views.items():
    for i in re.findall(r'id="([^"]+)"', chunk):
        id_page.setdefault(i, name)

def fix_links(chunk, page):
    # landmark band -> open the right neighbourhood tab
    chunk = re.sub(r'href="#homes" data-goarea="([^"]+)"', lambda m: f'href="/for-sale/#{m.group(1).lower()}" data-goarea="{m.group(1)}"', chunk)
    chunk = re.sub(r'href="#neighbourhoods" data-hood="([^"]+)"', lambda m: f'href="/neighbourhoods/#{m.group(1)}" data-hood="{m.group(1)}"', chunk)
    def rep(m):
        target = m.group(1)
        if target.startswith('i-'):
            return m.group(0)
        if target in PATH:
            return f'href="{PATH[target]}"'
        p = id_page.get(target)
        if p is None:
            return m.group(0)
        return f'href="#{target}"' if p == page else f'href="{PATH[p]}#{target}"'
    return re.sub(r'href="#([^"]+)"', rep, chunk)

# ---------- 4. CSS file (+ base rules the preview wrapper used to supply) ----------
base_css = ('html,body{margin:0;padding:0}img{max-width:100%}'
            '[hidden]:not([hidden=until-found i]){display:none!important}\n'
            '.photo,.place-photo{position:relative;overflow:hidden}'
            '.cover-img{position:absolute;inset:0;width:100%;height:100%;max-width:none;display:block}\n')
open(f'{OUT}/style.css', 'w').write(base_css + css.strip() + '\n')

# ---------- 5. JS: real pages instead of the hash router ----------
js = script[len('<script>'):-len('</script>')]
router = js[js.index("const VIEWS="):js.index("window.addEventListener('hashchange',fromHash);fromHash();") + len("window.addEventListener('hashchange',fromHash);fromHash();")]
menu = ("const mb=document.getElementById('menu-btn'),ml=document.querySelector('.nav ul');\n"
        "mb.addEventListener('click',()=>{const o=ml.classList.toggle('open');mb.setAttribute('aria-expanded',o);});\n"
        "ml.addEventListener('click',e=>{if(e.target.closest('a')){ml.classList.remove('open');mb.setAttribute('aria-expanded','false');}});")
js = js.replace(router, menu)
# landmark band click handler no longer needed (it now links to the tab)
js = re.sub(r"document\.querySelectorAll\('\.hb-item'\).*?\n", '', js)
js += ("\n// open a neighbourhood tab from the URL, e.g. /neighbourhoods/#tab-lapa\n"
       "function tabFromHash(){const tb=document.getElementById(location.hash.slice(1));"
       "if(tb&&tb.getAttribute('role')==='tab'){sel(tb);markPins();const a=document.getElementById('areas');a&&a.scrollIntoView();}}\n"
       "window.addEventListener('hashchange',tabFromHash);tabFromHash();\n")
open(f'{OUT}/site.js', 'w').write(js.strip() + '\n')

# ---------- 6. head + structured data ----------
PAGES = {
    'home': dict(title='Pascale Lepoutre | Lisbon Homes · Estrela, Lapa & Santos',
                 desc='Selling or buying in Estrela, Lapa or Santos? Real estate consultant at Engel & Völkers Lisbon. Free market study and valuation of your home. PT · EN · FR · NL.'),
    'buying': dict(title='Buying a home in Estrela, Lapa & Santos, Lisbon | Pascale Lepoutre',
                   desc='Looking for a home in Estrela, Lapa, Santos or nearby? Tell me what you are looking for and get personal support from the first viewing to the final deed.'),
    'neighbourhoods': dict(title='Estrela, Lapa & Santos neighbourhood guide | Pascale Lepoutre',
                           desc='A local guide to Estrela, Lapa, Santos, Campo de Ourique, Alcântara, Ajuda and Belém: what each neighbourhood is like, asking prices and tips from someone who lives here.'),
    'market-report': dict(title='Estrela property market report: real sale prices | Pascale Lepoutre',
                          desc='What really happens when you sell in Estrela, Lisbon: real sale prices versus asking prices, price reductions and typologies, compared with Lisbon as a whole.'),
    'homes': dict(title='Homes for sale in Estrela, Lapa & Santos, Lisbon | Pascale Lepoutre',
                  desc='Apartments and houses for sale in Estrela, Lapa and Santos, Lisbon: my own listings and those of my Engel & Völkers colleagues. Message me for details and a viewing.'),
    'my-lisbon': dict(title='My Lisbon: favourite places in Estrela and Lapa | Pascale Lepoutre',
                      desc='A local’s Lisbon: my favourite restaurants, yoga and movement studios, a museum garden and the monthly Living Room Sessions in Estrela, Lapa and around.'),
}
CRUMB = {'buying': 'Buying', 'neighbourhoods': 'Neighbourhoods & market', 'my-lisbon': 'My Lisbon', 'homes': 'Homes for sale', 'market-report': 'Market report'}

AREAS = ['Estrela', 'Lapa', 'Santos', 'Campo de Ourique', 'Alcântara', 'Ajuda', 'Belém']
agent = {
    '@type': 'RealEstateAgent',
    '@id': DOMAIN + '/#agent',
    'name': 'Pascale Lepoutre | Lisbon Homes',
    'alternateName': 'Pascale Lepoutre',
    'slogan': 'Your Lisbon home, in happy hands',
    'description': 'Real estate consultant with Engel & Völkers in Lisbon, specialised in the Estrela parish: Estrela, Lapa and Santos. Selling and buying homes, free market study.',
    'url': DOMAIN + '/',
    'image': DOMAIN + '/img/share.png',
    'telephone': '+351 920 609 225',
    'email': 'pascale.lepoutre@engelvoelkers.com',
    'address': {'@type': 'PostalAddress', 'addressLocality': 'Lisboa', 'addressCountry': 'PT'},
    'areaServed': [{'@type': 'Place', 'name': f'{a}, Lisboa'} for a in AREAS],
    'knowsLanguage': ['pt', 'en', 'fr', 'nl'],
    'sameAs': ['https://www.instagram.com/pascalelisbonhomes/', 'https://www.facebook.com/profile.php?id=61596316672646'],
    'memberOf': {'@type': 'Organization', 'name': 'Engel & Völkers', 'url': 'https://www.engelvoelkers.com'},
    'employee': {'@type': 'Person', 'name': 'Pascale Lepoutre', 'jobTitle': 'Real estate consultant',
                 'knowsLanguage': ['pt', 'en', 'fr', 'nl'],
                 'worksFor': {'@type': 'Organization', 'name': 'Engel & Völkers'}},
}
website = {'@type': 'WebSite', '@id': DOMAIN + '/#website', 'url': DOMAIN + '/', 'name': 'Pascale Lepoutre | Lisbon Homes',
           'inLanguage': 'en', 'publisher': {'@id': DOMAIN + '/#agent'}}

def faq_ld(chunk, faq_id):
    m = re.search(rf'id="{faq_id}".*?(?=</section>)', chunk, re.S)
    if not m:
        return None
    qa = []
    for d in re.findall(r'<details>(.*?)</details>', m.group(0), re.S):
        q = re.search(r'<summary>(.*?)</summary>', d, re.S).group(1)
        a = ' '.join(re.findall(r'<p>(.*?)</p>', d, re.S))
        clean = lambda s: html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s))).strip()
        qa.append({'@type': 'Question', 'name': clean(q), 'acceptedAnswer': {'@type': 'Answer', 'text': clean(a)}})
    return {'@type': 'FAQPage', 'mainEntity': qa} if qa else None

def head(page, chunk):
    p = PAGES[page]
    url = DOMAIN + PATH[page]
    graph = [agent, website] if page == 'home' else [{'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': DOMAIN + '/'},
        {'@type': 'ListItem', 'position': 2, 'name': CRUMB[page], 'item': url}]}]
    f = faq_ld(chunk, 'faq' if page == 'home' else 'buy-faq')
    if f:
        f['@id'] = url + '#faq'
        graph.append(f)
    ld = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, indent=1)
    e = lambda s: html.escape(s, quote=True)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(p["title"])}</title>
<meta name="description" content="{e(p["desc"])}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Pascale Lepoutre | Lisbon Homes">
<meta property="og:title" content="{e(p["title"])}">
<meta property="og:description" content="{e(p["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/img/share.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#f0deaa">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<!-- Google Search Console: paste the verification tag here only if you don't verify through DNS -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{fonts_url}
<link rel="stylesheet" href="/style.css">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
'''

def page_html(page, chunk):
    hd = fix_links(header, page)
    ft = fix_links(footer, page)
    chunk = re.sub(r'(<div class="view" data-view="[^"]+") hidden>', r'\1>', fix_links(chunk, page))
    return (head(page, chunk) + symbols + '\n\n' + hd + '\n\n<main id="top">\n' + chunk + '\n</main>\n\n'
            + ft + '\n\n<script src="/site.js" defer></script>\n</body>\n</html>\n')

for page, chunk in views.items():
    d = OUT + PATH[page].rstrip('/')
    os.makedirs(d, exist_ok=True)
    open(f'{d}/index.html', 'w', encoding='utf-8').write(page_html(page, chunk))

# ---------- 7. 404, favicon, sitemap, robots, headers ----------
nf = '''<div class="view" data-view="404">
  <section class="page-head" style="min-height:60vh">
    <div class="wrap center">
      <p class="eyebrow">Page not found</p>
      <h1>This page doesn't exist</h1>
      <p class="sub">The link may be old. Let's take you back home.</p>
      <a class="btn" href="/">Back to the homepage</a>
    </div>
  </section>
</div>'''
PAGES['404'] = dict(title='Page not found | Pascale Lepoutre | Lisbon Homes', desc='This page does not exist.')
PATH['404'] = '/404.html'
CRUMB['404'] = 'Page not found'
p404 = page_html('404', nf).replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')
p404 = re.sub(r'<link rel="canonical"[^>]*>\n', '', p404)
p404 = re.sub(r'<script type="application/ld\+json">.*?</script>\n', '', p404, flags=re.S)
open(f'{OUT}/404.html', 'w').write(p404)

open(f'{OUT}/favicon.svg', 'w').write(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#f0deaa"/>'
    '<text x="32" y="43" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="30" fill="#2a2420" letter-spacing="1">PL</text></svg>\n')

urls = ['/', '/for-sale/', '/neighbourhoods/', '/market-report/', '/buying/', '/my-lisbon/']
open(f'{OUT}/sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    ''.join(f'  <url><loc>{DOMAIN}{u}</loc><lastmod>{TODAY}</lastmod></url>\n' for u in urls) + '</urlset>\n')

robots = open('/home/claude/robots.txt').read()
robots = re.sub(r'# Add your sitemap.*', f'Sitemap: {DOMAIN}/sitemap.xml\n', robots, flags=re.S)
open(f'{OUT}/robots.txt', 'w').write(robots)

open(f'{OUT}/_headers', 'w').write('/img/*\n  Cache-Control: public, max-age=31536000, immutable\n/*.css\n  Cache-Control: public, max-age=86400\n/*.js\n  Cache-Control: public, max-age=86400\n')

print('built', sorted(os.listdir(OUT)))
for root, _, files in os.walk(OUT):
    for fn in files:
        print(f'{os.path.getsize(os.path.join(root, fn))//1024:>5} KB  {os.path.join(root, fn)[len(OUT):]}')

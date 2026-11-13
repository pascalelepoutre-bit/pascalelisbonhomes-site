#!/usr/bin/env python3
"""Build the multi-page SEO version of Pascale's site from pascale-site.html.
Design and text stay identical; only structure, head tags, images and links change."""
import re, io, base64, json, html, shutil, os
from PIL import Image

SRC = '/home/claude/pascale-site.html'
OUT = '/home/claude/site'
DOMAIN = 'https://pascalelisbonhomes.com'
TODAY = '2026-11-10'

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
    'W-04CD4V': ('studio-pinzaleiro-santos', 'Furnished studio for sale at Pátio do Pinzaleiro, Santos, Lisbon'),
    'W-04BZY4': ('necessidades', 'T4 apartment for sale on Calçada das Necessidades, Estrela, Lisbon, with a view of the 25 de Abril bridge'),
    'W-04BOIG': ('t4-lapa', 'T4 apartment with terrace for sale in Lapa, Lisbon'),
    'W-04BF4C': ('penthouse-lapa', 'Penthouse with private pool and river views for sale in Lapa, Lisbon'),
    'W-04BNAR': ('t2-estrela', 'T2 apartment with private terrace for sale in Estrela, Lisbon'),
    'W-02XVJ7': ('t3-unique-belem', 'T3 apartment with garage in the Unique Belém development, Lisbon'),
    'Último Porto': ('ultimo-porto', 'Inside Último Porto restaurant, by the port of Lisbon'),
    'Maiz do Mar': ('maiz-do-mar', 'Ceviche with toasted corn at Maiz do Mar, Mexican fusion restaurant in Lisbon'),
    'Clube de Jornalistas': ('clube-de-jornalistas', 'The garden terrace of Clube de Jornalistas restaurant, Lapa, Lisbon'),
    'Baraza Yoga': ('baraza-yoga', 'The yoga room at Baraza Yoga, Lisbon'),
    'mvmt.studio': ('mvmt-studio', 'Inside mvmt.studio, movement classes in Lisbon'),
    'Museu do Oriente': ('museu-do-oriente', 'Museu do Oriente logo, Fundação Oriente, Lisbon'),
    'From my home to Belém': ('sunrise-run-maat-lisbon', 'Sunrise run along the river by MAAT, with the 25 de Abril bridge, Lisbon'),
    'O Melhor Bolo': ('o-melhor-bolo-de-chocolate', 'A slice of O Melhor Bolo de Chocolate do Mundo on Lisbon calçada, Campo de Ourique'),
    'Garden of the Museu': ('museu-arte-antiga-garden', 'Jacarandas in bloom in the garden of the Museu Nacional de Arte Antiga, Lapa, Lisbon'),
}

def save_img(b64, slug, maxw=1400):
    im = Image.open(io.BytesIO(base64.b64decode(b64)))
    has_alpha = im.mode in ('RGBA', 'LA', 'P')
    im = im.convert('RGBA' if has_alpha else 'RGB')
    if im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    path = f'img/{slug}.webp'
    ex = Image.Exif()
    ex[0x010E] = 'Published on pascalelisbonhomes.com (Pascale Lepoutre, Lisbon Homes). Not for reuse without permission.'
    if slug.startswith('pascale-lepoutre'):
        ex[0x8298] = 'Copyright: photo shoot commissioned by Pascale Lepoutre for pascalelisbonhomes.com. All rights reserved.'
    im.save(f'{OUT}/{path}', 'WEBP', quality=80, method=6, exif=ex.tobytes())
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
        if 'pinzaleiro' in alt:
            n = re.search(r'photo (\d+)', alt); slug = 'studio-pinzaleiro-' + (n.group(1) if n else '1')
        src, _ = save_img(m.group(1), slug, 1400 if slug == 'necessidades' else (800 if 'pinzaleiro' in slug else (1000 if alt.startswith('pascale') else 600)))
        if 'bird of paradise' in alt or 'red door' in alt: return f'<img src="{src}" fetchpriority="high" decoding="async"{m.group(2)}>'
        return f'<img src="{src}" loading="lazy" decoding="async"{m.group(2)}>'
    views[k] = re.sub(r'<img src="data:image/\w+;base64,([A-Za-z0-9+/=]+)"([^>]*)>', rep_img, views[k])
    assert 'base64' not in views[k], k

shutil.copy('/home/claude/img/share.png', f'{OUT}/img/share.png')
shutil.copy('/home/claude/i18n/streets.json', f'{OUT}/streets.json')
shutil.copytree('/home/claude/photos', f'{OUT}/photos', dirs_exist_ok=True)
if os.path.exists('/home/claude/SETUP.md'): shutil.copy('/home/claude/SETUP.md', f'{OUT}/SETUP.md')

# ---------- 3. links: hash views -> real URLs ----------
PATH = {'home': '/', 'selling': '/selling/', 'search': '/your-search/', 'neighbourhoods': '/neighbourhoods/', 'my-lisbon': '/my-lisbon/', 'buying': '/buying/', 'homes': '/for-sale/', 'market-report': '/market-report/', 'faq': '/faq/', 'privacy': '/privacy/', 'review': '/review/'}
id_page = {}
for name, chunk in views.items():
    for i in re.findall(r'id="([^"]+)"', chunk):
        id_page.setdefault(i, name)

PFX = ''
def P(page): return PFX + PATH[page]
def fix_links(chunk, page):
    # landmark band -> open the right neighbourhood tab
    chunk = re.sub(r'href="#homes" data-goarea="([^"]+)"', lambda m: f'href="{P("homes")}#{m.group(1).lower()}" data-goarea="{m.group(1)}"', chunk)
    chunk = re.sub(r'href="#neighbourhoods" data-hood="([^"]+)"', lambda m: f'href="{P("neighbourhoods")}#{m.group(1)}" data-hood="{m.group(1)}"', chunk)
    def rep(m):
        target = m.group(1)
        if target.startswith('i-'):
            return m.group(0)
        if target in PATH:
            return f'href="{P(target)}"'
        p = id_page.get(target)
        if p is None:
            return m.group(0)
        return f'href="#{target}"' if p == page else f'href="{P(p)}#{target}"'
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
        "ml.addEventListener('click',e=>{if(e.target.closest('a')){ml.classList.remove('open');mb.setAttribute('aria-expanded','false');}});\n"
        "(function(){const strip=p=>p.replace(/^\\/(pt|fr|nl)(?=\\/)/,'');const cp=strip(location.pathname);document.querySelectorAll('.nav ul a').forEach(a=>{const ap=strip(new URL(a.href,location.href).pathname);if(ap!=='/'&&cp.startsWith(ap))a.setAttribute('aria-current','page');});})();")
js = js.replace(router, menu)
# landmark band click handler no longer needed (it now links to the tab)
js = re.sub(r"document\.querySelectorAll\('\.hb-item'\).*?\n", '', js)
js += ("\n// open a neighbourhood tab from the URL, e.g. /neighbourhoods/#tab-lapa\n"
       "function tabFromHash(){const tb=document.getElementById(location.hash.slice(1));"
       "if(tb&&tb.getAttribute('role')==='tab'){sel(tb);markPins();const a=document.getElementById('areas');a&&a.scrollIntoView();}}\n"
       "window.addEventListener('hashchange',tabFromHash);tabFromHash();\n")
import sys as _sys
_sys.path.insert(0, '/home/claude/i18n')
from jsi18n import i18n_js
open(f'{OUT}/site.js', 'w').write(i18n_js(js).strip() + '\n')

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
    'search': dict(title='Tell me what you are looking for: buying in Lisbon | Pascale Lepoutre',
                   desc='Tell me what home you are looking for in Estrela, Lapa, Santos or nearby, and I prepare a personal selection for you.'),
    'selling': dict(title='Selling your home in Estrela, Lapa & Santos, Lisbon | Pascale Lepoutre',
                    desc='Sell your home in Estrela, Lapa or Santos at the right price from day one: free market study with real sale prices, strong marketing and weekly updates. PT · EN · FR · NL.'),
    'faq': dict(title='Frequently asked questions: selling and buying in Lisbon | Pascale Lepoutre',
                desc='Answers to the questions sellers and buyers ask most about selling or buying a home in Estrela, Lapa and Santos: price, exclusivity, commission, documents, mortgages and timing.'),
    'privacy': dict(title='Privacy policy | Pascale Lepoutre | Lisbon Homes',
                    desc='How Pascale Lepoutre, real estate consultant at Engel & Völkers Lisbon, uses the details you send through this website, and your rights.'),
    'review': dict(title='Your review | Pascale Lepoutre', desc='Share how it was to work with Pascale Lepoutre, real estate consultant in Lisbon.'),
    'my-lisbon': dict(title='My Lisbon: favourite places in Estrela and Lapa | Pascale Lepoutre',
                      desc='A local’s Lisbon: my favourite restaurants, yoga and movement studios, a museum garden and the monthly Living Room Sessions in Estrela, Lapa and around.'),
}
CRUMB = {'faq': 'FAQ', 'search': 'Your search', 'selling': 'Selling', 'privacy': 'Privacy policy', 'buying': 'Buying', 'neighbourhoods': 'Neighbourhoods & market', 'my-lisbon': 'My Lisbon', 'homes': 'Homes for sale', 'market-report': 'Market report', 'review': 'Your review'}

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
    'sameAs': ['https://www.instagram.com/pascalelisbonhomes/', 'https://www.facebook.com/profile.php?id=61596316672646', 'https://www.linkedin.com/in/pascale-lepoutre-2809b07/'],
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
    p = PAGESL[LANG][page]
    url = DOMAIN + P(page)
    graph = [agent, website] if page == 'home' else [{'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': HOMEW[LANG], 'item': DOMAIN + PFX + '/'},
        {'@type': 'ListItem', 'position': 2, 'name': CRUMBL[LANG][page], 'item': url}]}]
    f = faq_ld(chunk, 'faq') if page == 'faq' else None
    if f:
        f['@id'] = url + '#faq'
        graph.append(f)
    ld = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, indent=1)
    e = lambda s: html.escape(s, quote=True)
    return f'''<!doctype html>
<html lang="{LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(p["title"])}</title>
<meta name="description" content="{e(p["desc"])}">
<link rel="canonical" href="{url}">
{alternates(page)}
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Pascale Lepoutre | Lisbon Homes">
<meta property="og:title" content="{e(p["title"])}">
<meta property="og:description" content="{e(p["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/img/share.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{LOCALE[LANG]}">
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
<!-- Cloudflare Web Analytics: cookieless visitor statistics -->
<script type="module" src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token": "ab5d0e89d55f41bdb7433cca6967af08"}}'></script>
</head>
<body>
'''

# ---------- languages ----------
import sys
sys.path.insert(0, '/home/claude/i18n')
from engine import translate
LANGS = [l for l in ['en', 'pt', 'fr', 'nl'] if l == 'en' or os.path.exists(f'/home/claude/i18n/{l}.txt')]
META = json.load(open('/home/claude/i18n/meta.json'))
PAGESL = {'en': PAGES}
CRUMBL = {'en': CRUMB}
HOMEW = {'en': 'Home'}
LOCALE = {'en': 'en_GB'}
WA = {'en': 'Hi%20Pascale%2C%20'}
LANGNAME = {'en': 'English', 'pt': 'Português', 'fr': 'Français', 'nl': 'Nederlands'}
SWITCHW = {'en': 'Language'}
NF = {'en': ['Page not found', "This page doesn't exist", "The link may be old. Let's take you back home.", 'Back to the homepage']}
for l, m in META.items():
    PAGESL[l] = {k: dict(title=v[0], desc=v[1]) for k, v in m['pages'].items()}
    CRUMBL[l] = m['crumb']; HOMEW[l] = m['home']; LOCALE[l] = m['locale']; WA[l] = m['wa']; NF[l] = m['nf']; SWITCHW[l] = m['switch']
PAGES['404'] = dict(title='Page not found | Pascale Lepoutre | Lisbon Homes', desc='This page does not exist.')
CRUMB['404'] = 'Page not found'

from dicts import load_dict
DICTS = {l: load_dict(l) for l in LANGS if l != 'en'}
MISSING = {l: set() for l in LANGS}

def pre(l): return '' if l == 'en' else '/' + l

def alternates(page):
    if page == '404': return ''
    out = [f'<link rel="alternate" hreflang="{l}" href="{DOMAIN}{pre(l)}{PATH[page]}">' for l in LANGS]
    out.append(f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}{PATH[page]}">')
    return '\n'.join(out)

def switcher(page):
    items = ''.join(f'<a href="{pre(l)}{PATH[page]}" hreflang="{l}" lang="{l}"' + (' aria-current="true"' if l == LANG else '') + f'>{l.upper()}<span> · {LANGNAME[l]}</span></a>' for l in ['pt', 'en', 'fr', 'nl'])
    return (f'<details class="lang-sw"><summary aria-label="{SWITCHW[LANG]}"><svg class="fi" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8"/><path d="M4 12h16M12 4c2.4 2.4 2.4 13.6 0 16M12 4c-2.4 2.4-2.4 13.6 0 16"/></svg>{LANG.upper()}</summary>'
            f'<div>{items}</div></details>')

def localise(html_, page):
    # header switcher, footer language links, WhatsApp greeting, default language, site language field
    html_ = html_.replace('<button class="menu"', switcher(page) + '\n    <button class="menu"', 1)
    html_ = re.sub(r'<span>(PT|EN|FR|NL)</span>', lambda m: f'<a href="{pre(m.group(1).lower())}{PATH[page]}" hreflang="{m.group(1).lower()}"' + (' aria-current="true"' if m.group(1).lower() == LANG else '') + f'>{m.group(1)}</a>', html_)
    import sys; sys.path.insert(0,'/home/claude/i18n'); from wa import localise_wa
    html_ = localise_wa(html_, LANG)
    if LANG != 'en':
        html_ = html_.replace('name="Language" value="English" checked>', 'name="Language" value="English">')
        html_ = html_.replace(f'name="Language" value="{LANGNAME[LANG]}">', f'name="Language" value="{LANGNAME[LANG]}" checked>')
        html_ = html_.replace('<option selected>English</option>', '<option>English</option>').replace(f'<option>{LANGNAME[LANG]}</option>', f'<option selected>{LANGNAME[LANG]}</option>')
    html_ = re.sub(r'(<input type="hidden" name="form-name" value="[^"]+">)', r'\1<input type="hidden" name="Site language" value="' + LANG.upper() + '">', html_)
    return html_

def page_html(page, chunk):
    hd = fix_links(header, page)
    ft = fix_links(footer, page)
    chunk = re.sub(r'(<div class="view" data-view="[^"]+") hidden>', r'\1>', fix_links(chunk, page))
    if LANG != 'en':
        hd, ft, chunk = (translate(x, DICTS[LANG], LANG, MISSING[LANG]) for x in (hd, ft, chunk))
    hd, ft, chunk = (localise(x, page) for x in (hd, ft, chunk))
    return (head(page, chunk) + symbols + '\n\n' + hd + '\n\n<main id="top">\n' + chunk + '\n</main>\n\n'
            + ft + '\n\n<script src="/site.js" defer></script>\n</body>\n</html>\n')

nf_tpl = """<div class="view" data-view="404">
  <section class="page-head" style="min-height:60vh">
    <div class="wrap center">
      <p class="eyebrow">{0}</p>
      <h1>{1}</h1>
      <p class="sub">{2}</p>
      <a class="btn" href="{4}/">{3}</a>
    </div>
  </section>
</div>"""
PATH['404'] = '/404.html'
redirects = []
for LANG in LANGS:
    PFX = pre(LANG)
    website['inLanguage'] = LANG
    for page, chunk in views.items():
        d = OUT + PFX + PATH[page].rstrip('/')
        os.makedirs(d, exist_ok=True)
        out_html = page_html(page, chunk)
        if page == 'review':
            out_html = out_html.replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')
        out_html = out_html.replace('src="photos/', 'src="/photos/')
        if LANG == 'pt': out_html = out_html.replace('engelvoelkers.com/pt/en/exposes/', 'engelvoelkers.com/pt/pt/exposes/')
        open(f'{d}/index.html', 'w', encoding='utf-8').write(out_html)
    nf = nf_tpl.format(*[html.escape(x, quote=False) for x in NF[LANG]], PFX)
    p404 = page_html('404', nf).replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')
    p404 = re.sub(r'<link rel="canonical"[^>]*>\n', '', p404)
    p404 = re.sub(r'<script type="application/ld\+json">.*?</script>\n', '', p404, flags=re.S)
    open(f'{OUT}{PFX}/404.html', 'w').write(p404)
    if PFX: redirects.append(f'{PFX}/*  {PFX}/404.html  404')
website['inLanguage'] = 'en'
open(f'{OUT}/_redirects', 'w').write('\n'.join(redirects) + '\n')
KEEP = set(open('/home/claude/i18n/keep.txt', encoding='utf-8').read().splitlines())
for l in LANGS:
    MISSING[l] = {x for x in MISSING[l] if x not in KEEP and x not in NF[l] and not re.fullmatch(r'[\d,.]+ m²\+?|Ref\. [\w-]+', x)}
    if MISSING[l]:
        print(f'--- {l}: {len(MISSING[l])} untranslated'); [print('   ', x[:150]) for x in sorted(MISSING[l])]
LANG = 'en'; PFX = ''

open(f'{OUT}/favicon.svg', 'w').write(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#f0deaa"/>'
    '<text x="32" y="43" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="30" fill="#2a2420" letter-spacing="1">PL</text></svg>\n')

urls = ['/', '/selling/', '/your-search/', '/for-sale/', '/neighbourhoods/', '/market-report/', '/buying/', '/my-lisbon/', '/faq/']
def sm_entry(u, l):
    alts = ''.join(f'<xhtml:link rel="alternate" hreflang="{a}" href="{DOMAIN}{pre(a)}{u}"/>' for a in LANGS)
    return f'  <url><loc>{DOMAIN}{pre(l)}{u}</loc><lastmod>{TODAY}</lastmod>{alts}</url>\n'
open(f'{OUT}/sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' +
    ''.join(sm_entry(u, l) for l in LANGS for u in urls) + '</urlset>\n')

robots = open('/home/claude/robots.txt').read()
robots = re.sub(r'# Add your sitemap.*', f'Sitemap: {DOMAIN}/sitemap.xml\n', robots, flags=re.S)
open(f'{OUT}/robots.txt', 'w').write(robots)

# Google Search Console verification file
open(f'{OUT}/google8c8b8ec375dc62f8.html', 'w').write('google-site-verification: google8c8b8ec375dc62f8.html')
open(f'{OUT}/_headers', 'w').write('/*\n  X-Frame-Options: SAMEORIGIN\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=()\n  Strict-Transport-Security: max-age=31536000\n/img/*\n  Cache-Control: public, max-age=31536000, immutable\n/*.css\n  Cache-Control: public, max-age=86400\n/*.js\n  Cache-Control: public, max-age=86400\n/s/*\n  X-Robots-Tag: noindex, nofollow\n')

print('built', sorted(os.listdir(OUT)))
for root, _, files in os.walk(OUT):
    for fn in files:
        print(f'{os.path.getsize(os.path.join(root, fn))//1024:>5} KB  {os.path.join(root, fn)[len(OUT):]}')

# Cache-busting: give style.css and site.js a version tag so browsers fetch new versions after each update
import hashlib, glob as _g
def _h(p): return hashlib.md5(open(p,'rb').read()).hexdigest()[:8]
_cv, _jv = _h(f'{OUT}/style.css'), _h(f'{OUT}/site.js')
for _p in _g.glob(f'{OUT}/**/*.html', recursive=True):
    _s = open(_p).read().replace('href="/style.css"', f'href="/style.css?v={_cv}"').replace('src="/site.js"', f'src="/site.js?v={_jv}"')
    open(_p, 'w').write(_s)

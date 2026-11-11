"""Private multi-language preview: one SPA per language, images as shared files."""
import re, base64, hashlib, os, json, sys, shutil, io
sys.path.insert(0, '/home/claude/i18n'); sys.path.insert(0, '/home/claude')
from engine import translate
from jsi18n import i18n_js
from PIL import Image
OUT = '/tmp/claude-0/-home-claude/cc545ed1-e2a8-53b2-a692-703eb5e28d3d/scratchpad/prev'
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT + '/img')
s = open('/home/claude/pascale-site.html', encoding='utf-8').read()
seen = {}
def ext_img(m):
    mime, b64 = m.group(1), m.group(2)
    h = hashlib.md5(b64.encode()).hexdigest()[:12]
    if h not in seen:
        raw = base64.b64decode(b64)
        if mime in ('jpeg', 'jpg', 'png') and len(raw) > 60000:
            im = Image.open(io.BytesIO(raw)); im = im.convert('RGBA' if im.mode in ('RGBA', 'LA', 'P') else 'RGB')
            if im.width > 1400: im = im.resize((1400, round(im.height * 1400 / im.width)))
            fn = f'img/{h}.webp'; im.save(f'{OUT}/{fn}', 'WEBP', quality=82)
        else:
            e = {'svg+xml': 'svg', 'jpeg': 'jpg'}.get(mime, mime); fn = f'img/{h}.{e}'
            open(f'{OUT}/{fn}', 'wb').write(raw)
        seen[h] = fn
    return seen[h]
s = re.sub(r'data:image/([\w+.-]+);base64,([A-Za-z0-9+/=]+)', ext_img, s)
# fonts or other data URIs stay
LANGS = ['en', 'pt', 'fr', 'nl']; FILE = {'en': 'index.html', 'pt': 'pt.html', 'fr': 'fr.html', 'nl': 'nl.html'}
NAME = {'en': 'English', 'pt': 'Português', 'fr': 'Français', 'nl': 'Nederlands'}
WA = {'en': 'Hi%20Pascale%2C%20', 'pt': 'Ol%C3%A1%20Pascale%2C%20', 'fr': 'Bonjour%20Pascale%2C%20', 'nl': 'Hallo%20Pascale%2C%20'}
SW = {'en': 'Language', 'pt': 'Idioma', 'fr': 'Langue', 'nl': 'Taal'}
import importlib.util
spec = importlib.util.spec_from_file_location('bs_dicts', '/home/claude/i18n/dicts.py'); dm = importlib.util.module_from_spec(spec); spec.loader.exec_module(dm)
st = s.index('</style>'); sc = s.rindex('<script>')
for L in LANGS:
    head, body, script = s[:st], s[st:sc], s[sc:]
    if L != 'en':
        miss = set(); body = translate(body, dm.load_dict(L), L, miss)
    items = ''.join(f'<a href="{FILE[l]}" hreflang="{l}"' + (' aria-current="true"' if l == L else '') + f'>{l.upper()}<span> · {NAME[l]}</span></a>' for l in ['pt', 'en', 'fr', 'nl'])
    sw = (f'<details class="lang-sw"><summary aria-label="{SW[L]}"><svg class="fi" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8"/><path d="M4 12h16M12 4c2.4 2.4 2.4 13.6 0 16M12 4c-2.4 2.4-2.4 13.6 0 16"/></svg>{L.upper()}</summary><div>{items}</div></details>\n')
    body = body.replace('<button class="menu"', sw + '<button class="menu"', 1)
    body = re.sub(r'<span>(PT|EN|FR|NL)</span>', lambda m: f'<a href="{FILE[m.group(1).lower()]}"' + (' aria-current="true"' if m.group(1).lower() == L else '') + f'>{m.group(1)}</a>', body)
    import sys; sys.path.insert(0,'/home/claude/i18n'); from wa import localise_wa
    body = localise_wa(body, L)
    if L != 'en':
        body = body.replace('name="Language" value="English" checked>', 'name="Language" value="English">').replace(f'name="Language" value="{NAME[L]}">', f'name="Language" value="{NAME[L]}" checked>')
    js = script[len('<script>'):script.rindex('</script>')]
    js = i18n_js(js) + "\ndocument.querySelectorAll('.lang-sw a,.f-lang a').forEach(a=>a.addEventListener('click',()=>{a.href=a.getAttribute('href').split('#')[0]+location.hash;}));\n"
    page = f'<!doctype html>\n<html lang="{L}">\n<meta charset="utf-8">\n<style>.reveal{{opacity:1!important;transform:none!important}}</style>\n' + head.replace('<title>', '<title>PRIVATE PREVIEW · ', 1) + body + '<script>' + js + '</script>\n'
    open(f'{OUT}/{FILE[L]}', 'w', encoding='utf-8').write(page)
shutil.copy('/home/claude/i18n/streets.json', OUT + '/streets.json')
shutil.copytree('/home/claude/photos', OUT + '/photos', dirs_exist_ok=True)
print(len(seen), 'images', {f: os.path.getsize(f'{OUT}/{f}') // 1024 for f in FILE.values()}, sum(os.path.getsize(f'{OUT}/{x}') for x in seen.values()) // 1024, 'KB img')

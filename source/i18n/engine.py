import re, json
PROTECT = re.compile(r'(<script\b.*?</script>|<style\b.*?</style>|<svg\b.*?</svg>|<!--.*?-->)', re.S)
TXT = re.compile(r'(?:(?<=>)|^)([^<>]+)(?=<|$)')
ATTR = re.compile(r'\b(alt|placeholder|aria-label|title)="([^"]*)"')
PHOTO = re.compile(r'^(.*), photo (\d+)$')
FORSALE = re.compile(r'^(.*), for sale in (.*), Lisbon$')

def make_lookup(d, lang, miss):
    W = {'pt': ('foto', 'à venda em', 'Lisboa'), 'fr': ('photo', 'à vendre à', 'Lisbonne'), 'nl': ('foto', 'te koop in', 'Lissabon')}[lang]
    AREA = {'pt': {'Estrela and Lapa': 'Estrela e Lapa'}, 'fr': {'Estrela and Lapa': 'Estrela et Lapa'}, 'nl': {'Estrela and Lapa': 'Estrela en Lapa'}}[lang]
    def look(s):
        if s in d: return d[s]
        m = PHOTO.match(s)
        if m:
            b = look(m.group(1))
            return None if b is None else f'{b}, {W[0]} {m.group(2)}'
        m = FORSALE.match(s)
        if m and m.group(1) in d:
            return f'{d[m.group(1)]}, {W[1]} {AREA.get(m.group(2), m.group(2))}, {W[2]}'
        return None
    def get(s):
        r = look(s)
        if r is None:
            miss.add(s); return s
        return r
    return get

def translate(html, d, lang, miss):
    get = make_lookup(d, lang, miss)
    parts = PROTECT.split(html)
    out = []
    for i, p in enumerate(parts):
        if i % 2 == 1:
            if p.startswith('<svg'):
                p = re.sub(r'(<(?:text|tspan)\b[^>]*>)([^<]*[A-Za-z][^<]*)(<)', lambda m: m.group(1) + get(m.group(2).strip()) + m.group(3), p)
            out.append(p); continue
        def tx(m):
            raw = m.group(1); s = raw.strip()
            if not s or not re.search(r'[A-Za-zÀ-ÿ]', s): return m.group(0)
            lead = raw[:len(raw) - len(raw.lstrip())]; trail = raw[len(raw.rstrip()):]
            return lead + get(s) + trail
        p = TXT.sub(tx, p)
        def at(m):
            s = m.group(2).strip()
            if not s or not re.search(r'[A-Za-z]', s): return m.group(0)
            return f'{m.group(1)}="{get(s)}"'
        # attributes live inside tags only
        p = re.sub(r'<[a-zA-Z][^>]*>', lambda t: ATTR.sub(at, t.group(0)), p)
        out.append(p)
    return ''.join(out)

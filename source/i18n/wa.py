import re, urllib.parse
# Visitor's WhatsApp message, per language: greeting line, closing question, Enigma lines
P = {
 'en': ("Hi Pascale, I'd like to visit this home:", "When can we arrange a viewing?", "Hi Pascale, I'm interested in the Enigma Collection villas", "Could you tell me more and arrange a visit?"),
 'pt': ("Olá Pascale, gostava de visitar esta casa:", "Quando podemos marcar uma visita?", "Olá Pascale, tenho interesse nas moradias Enigma Collection", "Pode dar-me mais informações e marcar uma visita?"),
 'fr': ("Bonjour Pascale, j'aimerais visiter ce bien :", "Quand pourrions-nous organiser une visite ?", "Bonjour Pascale, les villas Enigma Collection m'intéressent", "Pourriez-vous m'en dire plus et organiser une visite ?"),
 'nl': ("Hallo Pascale, ik zou deze woning graag bezoeken:", "Wanneer kunnen we een bezoek inplannen?", "Hallo Pascale, ik heb interesse in de Enigma Collection-villa's", "Kunt u me meer vertellen en een bezoek plannen?"),
}
GREET = {'en': 'Hi Pascale, ', 'pt': 'Olá Pascale, ', 'fr': 'Bonjour Pascale, ', 'nl': 'Hallo Pascale, '}
# Words that need translating; T-codes stay as they are
W = {
 'Studio':    {'en':'Studio','pt':'Estúdio','fr':'Studio','nl':'Studio'},
 'House':     {'en':'House','pt':'Moradia','fr':'Maison','nl':'Huis'},
 'Villa':     {'en':'Villa','pt':'Moradia','fr':'Villa','nl':'Villa'},
 'Plot':      {'en':'Plot','pt':'Terreno','fr':'Terrain','nl':'Bouwgrond'},
 'Building':  {'en':'Building','pt':'Prédio','fr':'Immeuble','nl':'Gebouw'},
 'Loft':      {'en':'Loft','pt':'Loft','fr':'Loft','nl':'Loft'},
}
# Ref -> (typology, street or neighbourhood)
INFO = {
 'W-04BZY4': ('T4', 'Calçada das Necessidades, Estrela'),
 'W-04CD4V': ('Studio', 'Pátio do Pinzaleiro, Santos'),
 'W-04BOIG': ('T4', 'Lapa'),
 'W-04BF4C': ('T4 Penthouse', 'Lapa'),
 'W-049SUP': ('T1', 'Rua de Buenos Aires, Lapa'),
 'W-048RLP': ('T2', 'Lapa'),
 'W-02WI97': ('T2', 'Santos'),
 'W-048DID': ('T2', 'Estrela'),
 'W-04AAS5': ('T2', 'Avenida 24 de Julho, Santos'),
 'W-02LZMA': ('T2', 'Estrela'),
 'W-04BNAR': ('T2', 'Estrela'),
 'W-049HVO': ('T2+3', 'Santos'),
 'W-04BWE8': ('House', 'Lapa'),
 'W-02WRUI': ('T2', 'Santos'),
 'W-04ARF3': ('Plot', 'Estrela'),
 'W-0497KP': ('T3 Penthouse', 'Santos'),
 'W-04AF90': ('T4+1', 'Avenida Infante Santo, Estrela'),
 'W-049YUJ': ('Villa', 'Necessidades, Estrela'),
 'W-047PXH': ('Building', 'Lapa'),
 'W-04AG11': ('Loft', 'Estrela'),
 'W-049R1S': ('House', 'Estrela'),
}
INFANTE = {'en': 'Infante Residences · T1 and T2+1 · Estrela · From € 555.000',
 'pt': 'Infante Residences · T1 e T2+1 · Estrela · Desde € 555.000',
 'fr': 'Infante Residences · T1 et T2+1 · Estrela · À partir de € 555.000',
 'nl': 'Infante Residences · T1 en T2+1 · Estrela · Vanaf € 555.000'}
def label(ref, lang):
    t, place = INFO[ref]
    parts = [W[p][lang] if p in W else p for p in t.split(' ')]
    return ' '.join(parts) + ' · ' + place

def localise_wa(html, lang):
    a, b, c, d = P[lang]
    def rep(m):
        txt = urllib.parse.unquote(m.group(1))
        lines = txt.split('\n')
        if lines[0].startswith("Hi Pascale, I'm interested in this home:") and len(lines) >= 2:
            ref = lines[1].split(' · ')
            code = ref[0].replace('Ref. ', '').strip()
            if lines[1].startswith('Infante Residences'):
                keep = INFANTE[lang]
            elif ref[0].startswith('Ref.') and code in INFO:
                keep = ' · '.join([ref[0], label(code, lang), ref[-1]])
            else:
                keep = lines[1]
            txt = a + '\n' + keep + '\n' + b
        elif lines[0].startswith("Hi Pascale, I'm interested in the Enigma Collection"):
            txt = c + '\n' + d
        elif txt.startswith('Hi Pascale, '):
            txt = GREET[lang] + txt[len('Hi Pascale, '):]
        return 'wa.me/351920609225?text=' + urllib.parse.quote(txt, safe='')
    return re.sub(r'wa\.me/351920609225\?text=([^"\']*)', rep, html)

# Number format in the E&V strip (called from localise_wa so build and preview both get it)
NUM = {'pt': {'1,000+': '1.000+', '16,700+': '16.700+'}, 'fr': {'1,000+': '1 000+', '16,700+': '16 700+'}, 'nl': {'1,000+': '1.000+', '16,700+': '16.700+'}}
_orig_localise_wa = localise_wa
def localise_wa(html, lang):
    html = _orig_localise_wa(html, lang)
    for k, v in NUM.get(lang, {}).items():
        html = html.replace(f'<b>{k}</b>', f'<b>{v}</b>')
    return html

import re, json

def i18n_js(js):
    JSI = json.load(open('/home/claude/i18n/js.json'))
    js = js.replace("'Step '+(i+1)+' of '+N", "tr('Step {i} of {n}').replace('{i}',i+1).replace('{n}',N)")
    js = js.replace("(k==1?' home':' homes')", "(k==1?tr(' home'):tr(' homes'))")
    js = js.replace('"Please check your number. Not in Portugal? Add your country code, e.g. +32."', "tr('Please check your number. Not in Portugal? Add your country code, e.g. +32.')")
    for key in JSI['pt']:
        if key.startswith(' ') or key.startswith('Step') or key.startswith('Please check'): continue
        n = js.count(key)
        assert n, key
        js = js.replace(key, "'+tr('" + key + "')+'")
    KWJS = ("const KW={terrace:/(?<!(no|without|sem|sans|zonder) )(terra[cç]|terrace|terrass|terras\\b|varanda|balcon|balkon|rooftop|dakterras)/i,"
            "lift:/(?<!(no|without|sem|sans|zonder) )(\\blift|elevador|elevator|ascenseur)/i,"
            "garage:/(?<!(no|without|sem|sans|zonder) )(garage|garagem|parking|estacionamento|parkeerplaats|stationnement)/i,"
            "river:/river view|vista (sobre o )?(rio|tejo)|vista rio|tagus|tage|taag|fleuve|rivierzicht|rivier|views? over the (river|tagus)/i};")
    js, nkw = re.subn(r'const KW=\{.*?\};', lambda m: KWJS, js, count=1, flags=re.S)
    assert nkw == 1
    prelude = ("const LANG=(document.documentElement.lang||'en').slice(0,2);const I18N=" + json.dumps({k: v for k, v in JSI.items()}, ensure_ascii=False)
               + ";const tr=s=>(I18N[LANG]&&I18N[LANG][s])||s;\n"
               "document.querySelectorAll('.lang-sw').forEach(d=>document.addEventListener('click',e=>{if(!d.contains(e.target))d.removeAttribute('open')}));\n")
    return prelude + js

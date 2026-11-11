import re, json

def load_dict(lang):
    u = json.load(open('/home/claude/i18n/strings.json'))
    d = {}
    for line in open(f'/home/claude/i18n/{lang}.txt', encoding='utf-8'):
        line = line.rstrip('\n')
        if not line.strip(): continue
        if line.startswith('@|'):
            _, en, tr_ = line.split('|', 2); d[en] = tr_
        else:
            i, tr_ = line.split('|', 1); d[u[int(i)]] = tr_
    if lang == 'fr':
        d = {k: re.sub(r' ([?!:;»])', '\u00a0\\1', v).replace('« ', '«\u00a0') for k, v in d.items()}
    return d

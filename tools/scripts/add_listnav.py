#!/usr/bin/env python3
"""Give an older selection page (built before 23/11) the list-and-detail layout of selection 2:
always-visible top menu with home, house cards with the map on the left on wide screens, profile box hidden.
usage: add_listnav.py PAGE.html HOME_HREF LABEL"""
import re, sys, json, html
p, HOME, LABEL = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(p).read()
if 'class="topnav"' in s: sys.exit('already done')
e = html.escape
cards = ''
for m in re.finditer(r'<section class="step house" data-id="([^"]+)" data-name="([^"]+)"', s):
    hid, name = m.group(1), m.group(2)
    sec = s[m.start(): s.find('</section>', m.start())]
    ph = json.loads(html.unescape(re.search(r"data-photos='([^']*)'", sec).group(1)))[0]
    price = re.search(r'<p class="price">([^<]*)', sec).group(1)
    tag = re.search(r'<span class="tag([^"]*)">([^<]*)', sec)
    num = re.search(r'<span class="num[^"]*">(\d+)</span>', sec).group(1)
    rn = ' rn' if 'rn' in tag.group(1) else ''
    cards += f'<li><button type="button" class="scard" data-hid="{hid}"><span class="sth" style="background-image:url(\'{ph}\')"></span><b class="{rn.strip()}">{num}</b><span>{e(name)}<small>{price} · {e(tag.group(2))}</small></span></button></li>'
top = f'''<nav class="topnav" aria-label="Menu"><div class="tn-in"><span class="tn-brand">Pascale Lepoutre<small>Engel &amp; Völkers</small></span>
<a class="tn-home" href="{HOME}">⌂ O vosso espaço</a><button type="button" class="tn-b" id="tnStart">{LABEL}</button><button type="button" class="tn-b tn-list" id="tnList">As casas ☰</button><button type="button" class="tn-b tn-send" id="tnSend">As vossas respostas</button></div></nav>
<aside class="side" id="side" aria-label="As casas"><div class="side-in"><div id="sideMap"></div><ol class="scards">{cards}</ol></div></aside>'''
s = s.replace('<body>', '<body>' + top, 1)
css = '''.box.prof{display:none}
.topnav{position:sticky;top:0;z-index:50;background:rgba(255,253,249,.96);backdrop-filter:blur(6px);border-bottom:1px solid var(--sand)}.tn-in{max-width:1240px;margin:0 auto;display:flex;gap:8px;align-items:center;padding:8px 14px;overflow-x:auto}
.tn-brand{font:600 12px var(--body);letter-spacing:.12em;text-transform:uppercase;margin-right:10px;white-space:nowrap;display:none}.tn-brand small{display:block;font-weight:500;letter-spacing:.1em;color:var(--muted);font-size:10px}
.tn-home{font:600 14px var(--body);color:var(--ink);text-decoration:none;padding:8px 12px;border-radius:999px;background:var(--cream);white-space:nowrap}.tn-b{font:600 14px var(--body);border:1.5px solid var(--sand);background:#fff;color:var(--ink);padding:7px 12px;border-radius:999px;cursor:pointer;white-space:nowrap}.tn-send{margin-left:auto;background:var(--ink);color:#fff;border-color:var(--ink)}
.side{display:none}.scards{list-style:none;margin:0;padding:0;display:grid;gap:8px}.scard{width:100%;display:flex;gap:10px;align-items:center;text-align:left;background:#fff;border:1.5px solid var(--sand);border-radius:14px;padding:8px;cursor:pointer;font:500 14px var(--body);color:var(--ink)}.scard.on{border-color:var(--ink);box-shadow:0 2px 10px rgba(0,0,0,.08)}.scard small{display:block;color:var(--muted);font-size:12.5px;margin-top:2px}.scard b{flex:none;width:24px;height:24px;border-radius:50%;background:var(--ink);color:#fff;display:grid;place-items:center;font:600 12px var(--body)}.scard b.rn{background:var(--gold)}.sth{flex:none;width:58px;height:46px;border-radius:9px;background:center/cover #eee}
#sideMap .mapbox{margin:0 0 10px;padding:10px}#sideMap .mapbox>*:not(h3):not(svg){display:none}
@media (min-width:980px){.tn-brand{display:block}.wrap>.top,.wrap>.progress{display:none}.side{display:block;position:fixed;left:max(14px,calc(50vw - 620px));top:58px;bottom:0;width:340px;overflow:auto;padding:12px 4px 90px 0}.wrap{margin-left:max(372px,calc(50vw - 620px + 372px));max-width:calc(100vw - 400px);margin-right:auto}.tn-list{display:none}}
@media (min-width:1400px){.wrap{max-width:860px}}
@media (max-width:979px){.side.open{display:block;position:fixed;inset:52px 0 0 0;z-index:49;background:var(--bg);overflow:auto;padding:12px 14px 100px}}
'''
s = s.replace('</style>', css + '</style>', 1)
early = "\nconst SIDE=document.getElementById('side');if(window.matchMedia('(min-width:980px)').matches){const mb=document.querySelector('.mapbox');if(mb)document.getElementById('sideMap').append(mb);}\n"
i = s.find('<script>', s.find('</nav>', s.find('class="bar"'))) if 'class="bar"' in s else s.find('<script>')
j = s.find('(function(){', i)
s = s[:j + len('(function(){')] + early + s[j + len('(function(){'):]
wire = '''
function sideSync(){const s=steps[cur];document.querySelectorAll('.scard[data-hid]').forEach(c=>c.classList.toggle('on',s&&s.dataset.id===c.dataset.hid));}
const _show=show;show=function(i){_show(i);sideSync();};
document.querySelectorAll('.scard[data-hid]').forEach(c=>c.addEventListener('click',()=>{const h=houses.find(x=>x.dataset.id===c.dataset.hid);if(h){show(steps.indexOf(h));window.scrollTo({top:0});}SIDE.classList.remove('open');}));
const fin=steps.findIndex(s=>s.classList.contains('final'));
document.getElementById('tnSend').addEventListener('click',()=>{show(fin);window.scrollTo({top:0});SIDE.classList.remove('open');});
document.getElementById('tnStart').addEventListener('click',()=>{show(0);window.scrollTo({top:0});SIDE.classList.remove('open');});
document.getElementById('tnList').addEventListener('click',()=>SIDE.classList.toggle('open'));
sideSync();
'''
k = s.index('})();', j)
s = s[:k] + wire + s[k:]
open(p, 'w').write(s)
print('ok')

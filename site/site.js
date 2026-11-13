const LANG=(document.documentElement.lang||'en').slice(0,2);const I18N={"pt": {" home": " casa", " homes": " casas", "Step {i} of {n}": "Passo {i} de {n}", "Where can I send your selection?": "Para onde envio a sua seleção?", "← Back": "← Voltar", "Next": "Seguinte", "Please fill in your name and phone number first.": "Preencha primeiro o seu nome e número de telefone.", "Thank you! WhatsApp is opening with your message. Just press send. I reply within one working day.": "Obrigada! O WhatsApp está a abrir com a sua mensagem. Basta carregar em enviar. Respondo num dia útil.", "Sorry, that did not go through. Please send me a message on WhatsApp: +351 920 609 225": "Desculpe, não foi possível enviar. Envie-me uma mensagem por WhatsApp: +351 920 609 225", "Copied": "Copiado", "Copy": "Copiar", "Please check your number. Not in Portugal? Add your country code, e.g. +32.": "Verifique o seu número. Não está em Portugal? Acrescente o indicativo do país, p. ex. +32.", "Hi Pascale, I would like a free market study for my home.": "Olá Pascale, gostaria de um estudo de mercado gratuito para a minha casa.", "Hi Pascale, I am looking for a home in Lisbon.": "Olá Pascale, procuro uma casa em Lisboa.", "This file is too big: up to 8 MB in total. Please send it by WhatsApp or email.": "Este ficheiro é demasiado grande: até 8 MB no total. Envie-o por WhatsApp ou email.", "Now add the number and floor, e.g. 59, 3.º Esq.": "Agora acrescente o número e o andar, p. ex. 59, 3.º Esq.", "Remove file": "Remover ficheiro"}, "fr": {" home": " bien", " homes": " biens", "Step {i} of {n}": "Étape {i} sur {n}", "Where can I send your selection?": "Où puis-je vous envoyer votre sélection ?", "← Back": "← Retour", "Next": "Suivant", "Please fill in your name and phone number first.": "Indiquez d’abord votre nom et votre numéro de téléphone.", "Thank you! WhatsApp is opening with your message. Just press send. I reply within one working day.": "Merci ! WhatsApp s’ouvre avec votre message. Il ne reste qu’à appuyer sur envoyer. Je réponds sous un jour ouvrable.", "Sorry, that did not go through. Please send me a message on WhatsApp: +351 920 609 225": "Désolée, l’envoi n’a pas fonctionné. Envoyez-moi un message sur WhatsApp : +351 920 609 225", "Copied": "Copié", "Copy": "Copier", "Please check your number. Not in Portugal? Add your country code, e.g. +32.": "Vérifiez votre numéro. Vous n’êtes pas au Portugal ? Ajoutez l’indicatif de votre pays, par ex. +32.", "Hi Pascale, I would like a free market study for my home.": "Bonjour Pascale, je souhaite une étude de marché gratuite pour mon bien.", "Hi Pascale, I am looking for a home in Lisbon.": "Bonjour Pascale, je cherche un logement à Lisbonne.", "This file is too big: up to 8 MB in total. Please send it by WhatsApp or email.": "Ce fichier est trop lourd : 8 Mo maximum au total. Envoyez-le par WhatsApp ou par e-mail.", "Now add the number and floor, e.g. 59, 3.º Esq.": "Ajoutez maintenant le numéro et l’étage, par ex. 59, 3.º Esq.", "Remove file": "Supprimer le fichier"}, "nl": {" home": " woning", " homes": " woningen", "Step {i} of {n}": "Stap {i} van {n}", "Where can I send your selection?": "Waar mag ik jouw selectie naartoe sturen?", "← Back": "← Terug", "Next": "Volgende", "Please fill in your name and phone number first.": "Vul eerst jouw naam en telefoonnummer in.", "Thank you! WhatsApp is opening with your message. Just press send. I reply within one working day.": "Dank je! WhatsApp opent met jouw bericht. Druk gewoon op verzenden. Ik antwoord binnen één werkdag.", "Sorry, that did not go through. Please send me a message on WhatsApp: +351 920 609 225": "Sorry, dat is niet gelukt. Stuur me een bericht via WhatsApp: +351 920 609 225", "Copied": "Gekopieerd", "Copy": "Kopiëren", "Please check your number. Not in Portugal? Add your country code, e.g. +32.": "Controleer jouw nummer. Niet in Portugal? Voeg jouw landcode toe, bv. +32.", "Hi Pascale, I would like a free market study for my home.": "Hallo Pascale, ik wil graag een gratis marktstudie voor mijn woning.", "Hi Pascale, I am looking for a home in Lisbon.": "Hallo Pascale, ik zoek een woning in Lissabon.", "This file is too big: up to 8 MB in total. Please send it by WhatsApp or email.": "Dit bestand is te groot: maximaal 8 MB in totaal. Stuur het via WhatsApp of e-mail.", "Now add the number and floor, e.g. 59, 3.º Esq.": "Voeg nu het huisnummer en de verdieping toe, bv. 59, 3.º Esq.", "Remove file": "Bestand verwijderen"}};const tr=s=>(I18N[LANG]&&I18N[LANG][s])||s;
document.querySelectorAll('.lang-sw').forEach(d=>document.addEventListener('click',e=>{if(!d.contains(e.target))d.removeAttribute('open')}));

document.querySelectorAll('.copy').forEach(b=>b.addEventListener('click',()=>{
  const done=()=>{b.textContent=''+tr('Copied')+'';setTimeout(()=>b.textContent=''+tr('Copy')+'',1600)};
  try{navigator.clipboard.writeText(b.dataset.t).then(done).catch(()=>{})}catch(e){}
}));

const tabs=[...document.querySelectorAll('[role="tab"]')];
function sel(t){tabs.forEach(x=>{const on=x===t;x.setAttribute('aria-selected',on);x.tabIndex=on?0:-1;document.getElementById(x.getAttribute('aria-controls')).hidden=!on;});}
tabs.forEach((t,i)=>{t.addEventListener('click',()=>sel(t));t.addEventListener('keydown',e=>{let j=null;if(e.key==='ArrowRight')j=(i+1)%tabs.length;if(e.key==='ArrowLeft')j=(i-1+tabs.length)%tabs.length;if(j!==null){e.preventDefault();sel(tabs[j]);tabs[j].focus();}});});

document.querySelectorAll('form.leadform').forEach(f=>{
  const a=f.querySelector('a.send'),done=f.querySelector('.done');
  if(!a)return;
  const build=()=>{const fd=new FormData(f),map={};
    for(const [k,v] of fd){if(!String(v).trim())continue;(map[k]=map[k]||[]).push(v);}
    const head=f.dataset.kind==='seller'?''+tr('Hi Pascale, I would like a free market study for my home.')+'':''+tr('Hi Pascale, I am looking for a home in Lisbon.')+'';
    a.href='https://wa.me/351920609225?text='+encodeURIComponent(head+'\n\n'+Object.entries(map).map(([k,v])=>k+': '+v.join(', ')).join('\n'));};
  f.addEventListener('input',build);f.addEventListener('change',build);build();
  a.addEventListener('click',e=>{let ok=true;
    f.querySelectorAll('[required]').forEach(i=>{const bad=i.type==='checkbox'?!i.checked:(!i.value.trim()||(i.type==='tel'&&!telOk(i.value)));i.setAttribute('aria-invalid',bad);if(bad)ok=false;});
    if(!ok){e.preventDefault();done.hidden=false;done.innerHTML='<p class="err">'+tr('Please fill in your name and phone number first.')+'</p>';return;}
    build();done.hidden=false;done.innerHTML='<p>'+tr('Thank you! WhatsApp is opening with your message. Just press send. I reply within one working day.')+'</p>';});
  f.addEventListener('submit',e=>{e.preventDefault();a.click();});
});

const mb=document.getElementById('menu-btn'),ml=document.querySelector('.nav ul');
mb.addEventListener('click',()=>{const o=ml.classList.toggle('open');mb.setAttribute('aria-expanded',o);});
ml.addEventListener('click',e=>{if(e.target.closest('a')){ml.classList.remove('open');mb.setAttribute('aria-expanded','false');}});
(function(){const strip=p=>p.replace(/^\/(pt|fr|nl)(?=\/)/,'');const cp=strip(location.pathname);document.querySelectorAll('.nav ul a').forEach(a=>{const ap=strip(new URL(a.href,location.href).pathname);if(ap!=='/'&&cp.startsWith(ap))a.setAttribute('aria-current','page');});})();

(function(){const c=document.getElementById('b-bo'),w=document.getElementById('bo-wrap');if(c&&w){c.addEventListener('change',()=>{w.hidden=!c.checked;if(c.checked)document.getElementById('bo-input').focus();});}})();
const oth=document.getElementById('b-a7'),ow=document.getElementById('b-other-wrap');
if(oth&&ow){oth.addEventListener('change',()=>{ow.hidden=!oth.checked;if(oth.checked)document.getElementById('b-other').focus();});}

document.querySelectorAll('.m-pin').forEach(g=>{g.setAttribute('tabindex','0');g.setAttribute('role','button');
  const go=()=>{const tb=document.getElementById(g.dataset.tab);if(tb){sel(tb);markPins();}};
  g.addEventListener('click',go);g.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();go();}});});
function markPins(){document.querySelectorAll('.m-pin').forEach(g=>{const tb=document.getElementById(g.dataset.tab);g.classList.toggle('on',tb&&tb.getAttribute('aria-selected')==='true');});}
document.querySelectorAll('[role="tab"]').forEach(x=>x.addEventListener('click',markPins));markPins();


const nf=document.getElementById('news-form');
if(nf){nf.addEventListener('submit',e=>{e.preventDefault();if(!nf.checkValidity()){nf.reportValidity();return;}
  const done=()=>{nf.querySelector('.news-done').hidden=false;nf.querySelector('.news-row').hidden=true;const c=nf.querySelector('.consent');if(c)c.hidden=true;};
  const preview=/claude/.test(location.hostname)||location.protocol==='file:';if(preview){done();return;}
  const btn=nf.querySelector('button');btn.disabled=true;
  fetch('/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:new URLSearchParams(new FormData(nf)).toString()})
   .then(r=>{if(!r.ok)throw 0;done();})
   .catch(()=>{btn.disabled=false;const d=nf.querySelector('.news-done');d.hidden=false;d.textContent=''+tr('Sorry, that did not go through. Please send me a message on WhatsApp: +351 920 609 225')+'';});});}

let lastOpen=null;
function openModal(id){const m=document.getElementById(id);if(!m)return;m.hidden=false;document.body.style.overflow='hidden';const f=m.querySelector('input:not([type=hidden]):not([name=bot-field])');f&&f.focus();}
function closeModal(m){m.hidden=true;document.body.style.overflow='';lastOpen&&lastOpen.focus&&lastOpen.focus();}
document.addEventListener('click',e=>{const o=e.target.closest('[data-open]');if(o){lastOpen=o;if(o.dataset.pick){const r=document.getElementById(o.dataset.pick);if(r)r.checked=true;}if(o.dataset.region){const g=document.getElementById('r-region');if(g)g.value=o.dataset.region;}openModal(o.dataset.open);return;}
 const c=e.target.closest('[data-close]');if(c){closeModal(c.closest('.ref-modal'));return;}
 if(e.target.classList&&e.target.classList.contains('ref-modal'))closeModal(e.target);});
document.addEventListener('keydown',e=>{if(e.key==='Escape'){const m=[...document.querySelectorAll('.ref-modal')].find(x=>!x.hidden);m&&closeModal(m);}});
const FORM_ANCHOR={contact:'modal-seller-form',mortgage:'modal-mort-form'};
window.addEventListener('load',()=>{const h=location.hash.slice(1);if(FORM_ANCHOR[h])setTimeout(()=>openModal(FORM_ANCHOR[h]),500);});
document.addEventListener('click',e=>{const a=e.target.closest('a[href^="#"]');if(!a)return;const t=a.getAttribute('href').slice(1);if(FORM_ANCHOR[t]&&!a.closest('header')){setTimeout(()=>{lastOpen=a;openModal(FORM_ANCHOR[t]);},350);}});
const rf=document.getElementById('ref-form');
if(rf){rf.addEventListener('submit',e=>{e.preventDefault();if(!rf.checkValidity()){rf.reportValidity();return;}
  const d=rf.querySelector('.mort-done'),btn=rf.querySelector('button[type=submit]');
  const done=()=>{[...rf.children].forEach(c=>{if(c!==d&&c.type!=='hidden')c.hidden=true;});d.hidden=false;try{d.scrollIntoView({block:'center',behavior:'smooth'})}catch(_){}};
  if(/claude/.test(location.hostname)||location.protocol==='file:'){done();return;}
  btn.disabled=true;
  fetch('/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:new URLSearchParams(new FormData(rf)).toString()})
   .then(r=>{if(!r.ok)throw 0;done();})
   .catch(()=>{btn.disabled=false;d.hidden=false;d.textContent=''+tr('Sorry, that did not go through. Please send me a message on WhatsApp: +351 920 609 225')+'';});});}

['seller-form','buyer-form','review-form'].forEach(id=>{const f=document.getElementById(id);if(!f)return;
 f.addEventListener('submit',e=>{e.preventDefault();
  let ok=true;f.querySelectorAll('[required]').forEach(i=>{const bad=!i.value.trim()||(i.type==='email'&&!i.checkValidity())||(i.type==='tel'&&!telOk(i.value));i.setAttribute('aria-invalid',bad);if(bad)ok=false;});
  if(!ok){const first=f.querySelector('[aria-invalid="true"]');first&&first.focus();return;}
  const d=f.querySelector('.mort-done'),btn=f.querySelector('button[type=submit]');
  const done=()=>{[...f.children].forEach(c=>{if(c!==d&&c.type!=='hidden')c.hidden=true;});d.hidden=false;try{d.scrollIntoView({block:'center',behavior:'smooth'})}catch(_){}};
  if(/claude/.test(location.hostname)||location.protocol==='file:'){done();return;}
  btn.disabled=true;
  fetch('/',f.enctype==='multipart/form-data'?{method:'POST',body:new FormData(f)}:{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:new URLSearchParams(new FormData(f)).toString()})
   .then(r=>{if(!r.ok)throw 0;done();})
   .catch(()=>{btn.disabled=false;d.hidden=false;d.textContent=''+tr('Sorry, that did not go through. Please send me a message on WhatsApp: +351 920 609 225')+'';});});});

(function(){const f=document.getElementById('buyer-form');if(!f)return;
 const v=n=>{const x=f.querySelector('input[name="'+n+'"]:checked');return x?x.value:'';};
 const upd=()=>{const r=v('Renovation');{const qw=document.getElementById('q-works');if(qw)qw.hidden=!(r==='Small works, yes'||r==='Yes, full renovation');}
  const m=v('Mortgage');const need=m==='Yes'||m==='Not sure yet';document.getElementById('q-pre').hidden=!need;document.getElementById('q-broker').hidden=!need;
  const o=f.querySelector('input[name="Areas"][value="Other"]');document.getElementById('b-other-wrap').hidden=!(o&&o.checked);
  const ck=(n,val)=>{const x=f.querySelector('input[name="'+n+'"][value="'+val+'"]');return !!(x&&x.checked)};
  document.getElementById('b-nice-other-wrap').hidden=!ck('Nice to have','Other');document.getElementById('b-must-other-wrap').hidden=!ck('Must-haves','Other');document.getElementById('b-no-other-wrap').hidden=!ck('Deal-breakers','Other');
  document.getElementById('q-pa').hidden=!(need&&v('Pre-approval')==='Yes, we have one');
  const ws=r==='Small works, yes'?['Up to €10,000','Up to €25,000','Up to €50,000','More','Not sure yet']:['Up to €50,000','Up to €100,000','Up to €150,000','More','Not sure yet'];
  f.querySelectorAll('input[name="Works budget"]').forEach((x,n)=>{if(x.value!==ws[n]){x.value=ws[n];x.checked=false;x.nextElementSibling.textContent=ws[n]}});
  const must=[...f.querySelectorAll('input[name="Must-haves"]')],nice=[...f.querySelectorAll('input[name="Nice to have"]')];
  const pm=new Set(must.filter(x=>x.checked).map(x=>x.value));
  nice.forEach(x=>{const off=x.value!=='Other'&&pm.has(x.value);if(off)x.checked=false;x.disabled=off;x.parentNode.title=off?'Already a must-have':''});
  const mFull=must.filter(x=>x.checked).length>=3;must.forEach(x=>{x.disabled=mFull&&!x.checked});
  const nFull=nice.filter(x=>x.checked).length>=3;nice.forEach(x=>{if(nFull&&!x.checked)x.disabled=true});};
 const bud=document.getElementById('b-budget');bud&&bud.addEventListener('blur',()=>{const n=parseInt(bud.value.replace(/\D/g,''),10);if(n){const val=n<10000?n*1000:n;bud.value='€'+val.toLocaleString('en-GB')}});
 f.addEventListener('change',upd);upd();})();

(function(){const f=document.getElementById('buyer-form');if(!f)return;
 const steps=[...f.querySelectorAll('.qstep')];if(steps.length<2)return;
 const about=steps[0];const last=steps[steps.length-1];last.after(about);
 const h=about.querySelector('h2');if(h)h.innerHTML='<span>'+steps.length+'</span>'+tr('Where can I send your selection?')+'';
 const order=[...f.querySelectorAll('.qstep')];const N=order.length;f.classList.add('wiz');
 const prog=document.createElement('div');prog.className='wz-prog';prog.innerHTML='<p></p><div class="wz-bar"><i></i></div>';order[0].before(prog);
 const nav=document.createElement('div');nav.className='wz-nav';nav.innerHTML='<button type="button" class="wz-back">'+tr('← Back')+'</button><button type="button" class="btn fill wz-next">'+tr('Next')+'</button>';
 const sub=f.querySelector('button[type=submit]');const note=sub.previousElementSibling&&sub.previousElementSibling.classList.contains('f-note')?sub.previousElementSibling:null;
 (note||sub).before(nav);let i=0;
 function show(n,scroll){i=n;order.forEach((st,k)=>st.hidden=k!==i);prog.querySelector('p').textContent=tr('Step {i} of {n}').replace('{i}',i+1).replace('{n}',N);prog.querySelector('i').style.width=((i+1)/N*100)+'%';
  nav.querySelector('.wz-back').hidden=i===0;const lastStep=i===N-1;nav.querySelector('.wz-next').hidden=lastStep;sub.hidden=!lastStep;if(note)note.hidden=!lastStep;
  if(scroll){try{prog.scrollIntoView({block:'start',behavior:'smooth'})}catch(_){}}}
 nav.querySelector('.wz-next').addEventListener('click',()=>show(Math.min(N-1,i+1),true));
 nav.querySelector('.wz-back').addEventListener('click',()=>show(Math.max(0,i-1),true));
 const mo=new MutationObserver(()=>{const d=f.querySelector('.mort-done');if(d&&!d.hidden){mo.disconnect();prog.hidden=true;nav.hidden=true;order.forEach(st=>st.hidden=true)}});mo.observe(f.querySelector('.mort-done'),{attributes:true,attributeFilter:['hidden']});
 show(0,false);})();

function telOk(v){const d=String(v).replace(/\D/g,'');return d.length>=9&&d.length<=15}
document.querySelectorAll('input[type=tel]').forEach(i=>{const h=document.createElement('small');h.className='tel-hint';h.hidden=true;h.textContent=tr('Please check your number. Not in Portugal? Add your country code, e.g. +32.');i.after(h);
 i.addEventListener('input',()=>{const c=i.value.replace(/[^0-9+ ()-]/g,'');if(c!==i.value)i.value=c;if(telOk(i.value)){h.hidden=true;i.removeAttribute('aria-invalid')}});
 i.addEventListener('blur',()=>{const bad=i.value.trim()&&!telOk(i.value);h.hidden=!bad;if(bad)i.setAttribute('aria-invalid','true')});
 i.setCustomValidity&&i.addEventListener('input',()=>i.setCustomValidity(i.value.trim()&&!telOk(i.value)?'Please check your number':''));});
const mf=document.getElementById('mort-form');
if(mf){mf.addEventListener('submit',e=>{e.preventDefault();if(!mf.checkValidity()){mf.reportValidity();return;}
  const d=mf.querySelector('.mort-done'),btn=mf.querySelector('button[type=submit]');
  const done=()=>{[...mf.children].forEach(c=>{if(c!==d&&c.type!=='hidden')c.hidden=true;});d.hidden=false;try{d.scrollIntoView({block:'center',behavior:'smooth'})}catch(_){}};
  if(/claude/.test(location.hostname)||location.protocol==='file:'){done();return;}
  btn.disabled=true;
  fetch('/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:new URLSearchParams(new FormData(mf)).toString()})
   .then(r=>{if(!r.ok)throw 0;done();})
   .catch(()=>{btn.disabled=false;d.hidden=false;d.textContent=''+tr('Sorry, that did not go through. Please send me a message on WhatsApp: +351 920 609 225')+'';});});}

document.querySelectorAll('.pm-pin,.pm-note').forEach(g=>{const go=()=>{const el=document.getElementById(g.dataset.target);if(!el)return;el.scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'center'});el.classList.add('flash');setTimeout(()=>el.classList.remove('flash'),1600);};
  g.addEventListener('click',go);g.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();go();}});});

const hf=document.getElementById('home-filter'),bf=document.getElementById('bed-filter'),xf=document.getElementById('feat-filter');
if(hf&&bf){let fa='',fb=0;const fx=new Set();
  /* add features that the listing text itself mentions, so a filter never misses an obvious one */
  const KW={terrace:/(?<!(no|without|sem|sans|zonder) )(terra[cç]|terrace|terrass|terras\b|varanda|balcon|balkon|rooftop|dakterras)/i,lift:/(?<!(no|without|sem|sans|zonder) )(\blift|elevador|elevator|ascenseur)/i,garage:/(?<!(no|without|sem|sans|zonder) )(garage|garagem|parking|estacionamento|parkeerplaats|stationnement)/i,river:/river view|vista (sobre o )?(rio|tejo)|vista rio|tagus|tage|taag|fleuve|rivierzicht|rivier|views? over the (river|tagus)/i};
  hf.parentElement.querySelectorAll('.listing[data-area]').forEach(c=>{const t=[...c.querySelectorAll('h3,.feat,.hl span')].map(e=>e.textContent).join(' ');const fs=new Set((c.dataset.feat||'').split(',').filter(Boolean));for(const[k,re] of Object.entries(KW))if(re.test(t))fs.add(k);c.dataset.feat=[...fs].join(',');});
  const apply=()=>{let n=0;hf.parentElement.querySelectorAll('.listing[data-area]').forEach(c=>{const bs=c.dataset.beds===''?[]:c.dataset.beds.split(',').map(Number);
    const ok=(!fa||c.dataset.area.includes(fa))&&(!fb||bs.some(b=>fb===4?b>=4:b===fb))&&[...fx].every(x=>c.dataset.feat.split(',').includes(x));c.hidden=!ok;if(ok)n++;});document.getElementById('f-none').hidden=n>0;const cl=document.getElementById('f-clear');if(cl)cl.hidden=!(fa||fb||fx.size);};
  const pick=(box,b)=>box.querySelectorAll('button').forEach(x=>{const on=x===b;x.classList.toggle('on',on);x.setAttribute('aria-pressed',on);});
  hf.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;pick(hf,b);fa=b.dataset.f;apply();});
  bf.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;pick(bf,b);fb=+b.dataset.b;apply();});
  const clr=document.getElementById('f-clear');if(clr)clr.addEventListener('click',()=>{fa='';fb=0;fx.clear();pick(hf,hf.querySelector('button[data-f=""]'));pick(bf,bf.querySelector('button[data-b="0"]'));if(xf)xf.querySelectorAll('button').forEach(x=>{x.classList.remove('on');x.setAttribute('aria-pressed','false')});apply();});
  if(xf)xf.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;const on=!fx.has(b.dataset.x);on?fx.add(b.dataset.x):fx.delete(b.dataset.x);b.classList.toggle('on',on);b.setAttribute('aria-pressed',on);apply();});}
document.querySelectorAll('.gal').forEach(g=>{const tr=g.querySelector('.g-track'),ct=g.querySelector('.g-count');if(!ct)return;const n=tr.children.length;
  const idx=()=>Math.round(tr.scrollLeft/tr.clientWidth);
  const go=d=>{const i=(idx()+d+n)%n;tr.scrollTo({left:i*tr.clientWidth,behavior:'smooth'});};
  g.querySelector('.g-prev').addEventListener('click',()=>go(-1));g.querySelector('.g-next').addEventListener('click',()=>go(1));
  tr.addEventListener('scroll',()=>{ct.textContent=(idx()+1)+' / '+n;},{passive:true});});

/* fade-in on scroll */
(function(){if(!('IntersectionObserver' in window))return;const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}}),{threshold:0,rootMargin:'0px 0px -60px 0px'});
document.querySelectorAll('main section:not(.page-head):not(.buy-hero):not(.hero) .wrap > *').forEach(el=>{if(el.matches('.ref-modal')||el.querySelector('.ref-modal'))return;el.classList.add('reveal');io.observe(el);});})();

/* buying cost calculator, 2026 IMT tables, mainland Portugal */
(function(){const f=document.getElementById('calc');if(!f)return;
const HPP=[[106346,0,0],[145470,.02,2126.92],[198347,.05,6491.02],[330539,.07,10457.96],[660982,.08,13763.35]];
const SEC=[[106346,.01,0],[145470,.02,1063.46],[198347,.05,5427.56],[330539,.07,9394.50],[633931,.08,12699.89]];
const num=v=>+String(v).replace(/[^0-9]/g,'')||0;
const grp=n=>String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g,'.');const eur=n=>'€ '+grp(n);
function imt(p,t,flat6){for(const [lim,r,d] of t){if(p<=lim)return Math.max(0,p*r-d);}return p<=1150853?p*.06:p*.075;}
function calc(){const p=num(f.querySelector('#c-price').value),loan=num(f.querySelector('#c-loan').value);
 const use=f.querySelector('input[name=c-use]:checked').value;const yb=f.querySelector('#c-young');const young=use==='hpp'&&yb.checked;
 f.querySelector('.c-young').style.opacity=use==='hpp'?1:.4;yb.disabled=use!=='hpp';
 let I,S;
 if(young&&p<=330539){I=0;S=0;}
 else if(young&&p<=660982){I=(p-330539)*.08;S=(p-330539)*.008;}
 else{I=imt(p,use==='hpp'?HPP:SEC);S=p*.008;}
 const L=loan>0?loan*.006:0,B=loan>0?800:0,D=p>0?(loan>0?700:375):0,T=I+S+L+B+D;
 const set=(id,v)=>{const e=document.getElementById(id);if(e)e.textContent=eur(v)};
 set('o-imt',I);set('o-is',S);set('o-isl',L);set('o-bank',B);set('o-deed',D);set('o-tot',T);set('o-all',p+T);set('o-cash',Math.max(0,p-loan)+T);{const e=document.getElementById('o-pct');if(e)e.textContent=p>0?(T/p*100).toFixed(1).replace('.',',')+'%':'–'};
 document.querySelectorAll('#costs .o-loan').forEach(x=>x.style.display=loan>0?'':'none');document.querySelectorAll('#costs .o-noloan').forEach(x=>x.style.display=loan>0?'none':'');}
f.addEventListener('input',e=>{if(e.target.matches('#c-price,#c-loan')){const c=e.target.selectionStart,l=e.target.value.length;const n=num(e.target.value);e.target.value=n?grp(n):'';}calc();});
f.addEventListener('change',calc);calc();})();

document.querySelectorAll('#hood-band .hb-item svg path').forEach(p=>{const d=p.getAttribute('d')||'';if(/q10 -4 20 0/.test(d))p.classList.add('wave');else if(/z/.test(d)&&!/q/i.test(d)&&p.getBBox().width<60)p.classList.add('win');});
(function(){const t=document.getElementById('m-badge-t'),r=document.getElementById('m-badge-r');function fit(){try{const b=t.getBBox();if(!b.width)return;r.setAttribute('x',b.x-12);r.setAttribute('width',b.width+24);}catch(e){}}fit();document.fonts&&document.fonts.ready.then(fit);addEventListener('hashchange',()=>setTimeout(fit,50));})();
document.querySelectorAll('.hood-art svg path').forEach(p=>{const d=p.getAttribute('d')||'';if(/q10 -4 20 0/.test(d))p.classList.add('wave');else if(/z/i.test(d)&&!/q/i.test(d)){try{if(p.getBBox().width<60)p.classList.add('win')}catch(e){}}});

/* Where: Lisbon / Beyond / Both -> show matching areas and wishes */
(function(){const W=()=>{const v=[...document.querySelectorAll('input[name="Where"]:checked')].map(x=>x.value);return v.length===2?'Both':(v[0]||'');};
function setWhere(v){const r=document.querySelector('input[name="Where"][value="'+v+'"]');if(r)r.checked=true;sync();}
function sync(){const w=W(),lis=w==='In Lisbon'||w==='Both',bey=w==='Beyond Lisbon'||w==='Both';
 const fl=document.getElementById('q-lis'),fb=document.getElementById('q-bey');if(!fl||!fb)return;fl.hidden=!lis;fb.hidden=!bey;
 const clear=(fs)=>fs.querySelectorAll('input:checked').forEach(i=>{i.checked=false;i.dispatchEvent(new Event('change',{bubbles:true}))});
 if(!lis){clear(fl);const ow=document.getElementById('b-other-wrap');if(ow)ow.hidden=true;}if(!bey){clear(fb);const bw=document.getElementById('bo-wrap');if(bw)bw.hidden=true;}
 document.querySelectorAll('.chip.bx').forEach(c=>{c.hidden=!bey;if(!bey)clear(c);});
 const lift=document.querySelector('input[name="Must-haves"][value="Lift"]');if(lift){const off=w==='Beyond Lisbon';lift.parentNode.hidden=off;if(off&&lift.checked)clear(lift.parentNode);}}
function apply(a){if(!a)return;setWhere('Beyond Lisbon');if(a==='beyond')return;
 const b=[...document.querySelectorAll('input[name="Areas"]')].find(x=>x.value===a);if(b&&!b.checked){b.checked=true;b.dispatchEvent(new Event('change',{bubbles:true}));}}
document.addEventListener('click',e=>{const a=e.target.closest('[data-area]');if(!a)return;try{sessionStorage.setItem('bl-area',a.dataset.area)}catch(_){}setTimeout(()=>apply(a.dataset.area),0);});
document.addEventListener('change',e=>{if(e.target.name==='Where')sync();});
let a=null;try{a=new URLSearchParams(location.search).get('area')||sessionStorage.getItem('bl-area');sessionStorage.removeItem('bl-area')}catch(_){}
if(document.querySelector('input[name="Where"]')){if(a)apply(a);sync();}})();

/* header height -> --hh so page titles never touch the header */
(function(){const h=document.querySelector('header');if(!h)return;const f=()=>document.documentElement.style.setProperty('--hh',h.offsetHeight+'px');f();addEventListener('resize',f);addEventListener('load',f);})();

/* For sale: illustrated map filters the listings */
(function(){const pins=[...document.querySelectorAll('.fs-pin')];if(!pins.length)return;
const L=()=>[...document.querySelectorAll('#all-homes .listing[data-area]')];
pins.forEach(g=>{const n=g.dataset.f;const k=L().filter(x=>x.dataset.area.includes(n)).length;const c=g.querySelector('.m-count');if(c)c.textContent=k+(k==1?tr(' home'):tr(' homes'));
 const act=()=>{const b=document.querySelector('#home-filter [data-f="'+n+'"]');if(b)b.click();const l=document.querySelector('#home-filter');if(l)l.scrollIntoView({behavior:'smooth',block:'start'});};
 g.addEventListener('click',act);g.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();act();}});});})();

/* seller form: town field for outside Lisbon */
(function(){const w=document.getElementById('s-town-wrap');if(!w)return;const f=()=>{const r=document.querySelector('input[name="Location"]:checked');w.hidden=!(r&&r.value==='Outside Lisbon');};document.addEventListener('change',e=>{if(e.target.name==='Location')f();});document.addEventListener('click',e=>{if(e.target.closest('[data-pick="s-loc3"],[data-open="modal-seller-form"]'))setTimeout(f,0);});f();})();

/* For sale: counts on the neighbourhood filter buttons */
(function(){const bs=document.querySelectorAll('#home-filter [data-f]');if(!bs.length)return;const L=[...document.querySelectorAll('#all-homes .listing[data-area]')];
bs.forEach(b=>{const n=b.dataset.f;const k=n?L.filter(x=>x.dataset.area.includes(n)).length:L.length;const s=document.createElement('span');s.className='f-count';s.textContent=k;b.appendChild(s);});})();

(function(){const c=document.querySelector('.bl-count');if(c)c.textContent=document.querySelectorAll('.listing.beyond').length;})();

/* market study: street suggestions while typing (all Lisbon streets, Estrela area first) */
(function(){const inp=document.getElementById('s-addr');if(!inp)return;let data=null,loading=null,sel=-1,items=[];
const norm=t=>t.normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase();
const wrap=document.createElement('div');wrap.className='st-wrap';inp.parentNode.insertBefore(wrap,inp);wrap.appendChild(inp);
const ul=document.createElement('ul');ul.className='st-list';ul.hidden=true;ul.setAttribute('role','listbox');ul.id='st-list';wrap.appendChild(ul);
inp.setAttribute('role','combobox');inp.setAttribute('aria-autocomplete','list');inp.setAttribute('aria-controls','st-list');inp.setAttribute('aria-expanded','false');inp.autocomplete='off';
const load=()=>loading||(loading=fetch('/streets.json').then(r=>{if(!r.ok)throw 0;return r.json()}).catch(()=>fetch('streets.json').then(r=>r.json())).then(d=>{data=d.map(([n,z])=>[n,z,norm(n)]);}).catch(()=>{}));
const close=()=>{ul.hidden=true;inp.setAttribute('aria-expanded','false');sel=-1;};
const hint=document.createElement('small');hint.className='st-hint';hint.hidden=true;hint.textContent=''+tr('Now add the number and floor, e.g. 59, 3.º Esq.')+'';wrap.after(hint);
const pick=n=>{inp.value=n+' ';close();inp.focus();hint.hidden=false;inp.dispatchEvent(new Event('input',{bubbles:true}));};
inp.addEventListener('input',()=>{if(/\d/.test(inp.value))hint.hidden=true;});
const render=()=>{ul.innerHTML='';items.forEach((n,k)=>{const li=document.createElement('li');li.setAttribute('role','option');li.id='st-'+k;li.setAttribute('aria-selected',k===sel);li.textContent=n;li.addEventListener('mousedown',e=>{e.preventDefault();pick(n);});ul.appendChild(li);});ul.hidden=!items.length;inp.setAttribute('aria-expanded',!!items.length);};
inp.addEventListener('focus',load);
inp.addEventListener('input',e=>{if(!e.isTrusted&&e.type==='input'&&inp.value.endsWith(' ')&&items.length===0)return;
  const q=norm(inp.value).replace(/[\d,]+.*$/,'').trim();if(q.length<3||!data){items=[];render();if(!data)load().then(()=>{if(document.activeElement===inp)inp.dispatchEvent(new Event('input'))});return;}
  const toks=q.split(/\s+/);const res=[];
  for(const [n,z,k] of data){if(toks.every(t=>k.includes(t))){const w=k.split(/\s+/);const starts=toks.every(t=>w.some(x=>x.startsWith(t)));res.push([n,(z?2:0)+(starts?1:0)]);}}
  res.sort((a,b)=>b[1]-a[1]);items=res.slice(0,6).map(x=>x[0]);if(items.length===1&&norm(items[0])===q)items=[];sel=-1;render();});
inp.addEventListener('keydown',e=>{if(ul.hidden)return;if(e.key==='ArrowDown'){sel=(sel+1)%items.length;render();e.preventDefault();}else if(e.key==='ArrowUp'){sel=(sel-1+items.length)%items.length;render();e.preventDefault();}else if(e.key==='Enter'&&sel>=0){e.preventDefault();pick(items[sel]);}else if(e.key==='Escape')close();});
inp.addEventListener('blur',()=>setTimeout(close,120));})();
/* uploads: small cross to remove a chosen file */
(function(){document.querySelectorAll('form input[type=file]').forEach(i=>{const b=document.createElement('button');b.type='button';b.className='file-x';b.hidden=true;b.setAttribute('aria-label',''+tr('Remove file')+'');b.title=''+tr('Remove file')+'';b.textContent='×';
const row=document.createElement('span');row.className='file-row';i.parentNode.insertBefore(row,i);row.appendChild(i);row.appendChild(b);
const upd=()=>{b.hidden=!(i.files&&i.files.length);};i.addEventListener('change',upd);
b.addEventListener('click',e=>{e.preventDefault();e.stopPropagation();i.value='';i.dispatchEvent(new Event('change',{bubbles:true}));upd();i.focus();});});})();
/* market study: documents up to 8 MB in total */
(function(){const f=document.getElementById('seller-form');if(!f)return;const h=f.querySelector('.file-hint');if(!h)return;const t0=h.textContent;
f.querySelectorAll('input[type=file]').forEach(i=>i.addEventListener('change',()=>{let tot=0;f.querySelectorAll('input[type=file]').forEach(x=>{for(const fl of x.files)tot+=fl.size;});
 if(tot>8*1024*1024){i.value='';h.textContent=''+tr('This file is too big: up to 8 MB in total. Please send it by WhatsApp or email.')+'';h.classList.add('err');}else{h.textContent=t0;h.classList.remove('err');}}));})();

/* remember name, phone and email in this browser only, and pre-fill the other forms */
(function(){const K='pl-contact';const get=()=>{try{return JSON.parse(localStorage.getItem(K)||'{}')}catch(_){return{}}};
const fill=()=>{const d=get();document.querySelectorAll('form input[autocomplete="name"],form input[autocomplete="tel"],form input[autocomplete="email"]').forEach(i=>{const v=d[i.autocomplete];if(v&&!i.value){i.value=v;i.dispatchEvent(new Event('input',{bubbles:true}));}});};
document.addEventListener('input',e=>{const i=e.target;if(!i.matches||!i.matches('form input[autocomplete="name"],form input[autocomplete="tel"],form input[autocomplete="email"]')||!e.isTrusted)return;const d=get();d[i.autocomplete]=i.value.trim();try{localStorage.setItem(K,JSON.stringify(d))}catch(_){}});
fill();document.addEventListener('click',e=>{if(e.target.closest&&e.target.closest('[data-open],a[href*="mortgage"],a[href*="contact"],a[href*="search"]'))setTimeout(fill,50);});window.addEventListener('hashchange',()=>setTimeout(fill,50));})();

/* review page: pre-fill from a personal link, e.g. /review/#n=Marie%20D.&f=Belgium&t=sold&h=T3%20in%20Lapa%2C%202027 */
(function(){const f=document.getElementById('review-form');if(!f)return;const run=()=>{const q=new URLSearchParams((location.hash.split('#')[1]||'').replace(/^review&?/,''));if(![...q.keys()].length)return;
const set=(id,v)=>{const i=document.getElementById(id);if(i&&v&&!i.value)i.value=v;};set('v-name',q.get('n'));set('v-from',q.get('f'));set('v-what',q.get('h'));
const t={sold:'v-t1',bought:'v-t2',other:'v-t3'}[q.get('t')];if(t)document.getElementById(t).checked=true;};run();window.addEventListener('hashchange',run);})();

// open a neighbourhood tab from the URL, e.g. /neighbourhoods/#tab-lapa
function tabFromHash(){const tb=document.getElementById(location.hash.slice(1));if(tb&&tb.getAttribute('role')==='tab'){sel(tb);markPins();const a=document.getElementById('areas');a&&a.scrollIntoView();}}
window.addEventListener('hashchange',tabFromHash);tabFromHash();

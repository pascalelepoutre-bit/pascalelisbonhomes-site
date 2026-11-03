document.querySelectorAll('.copy').forEach(b=>b.addEventListener('click',()=>{
  const done=()=>{b.textContent='Copied';setTimeout(()=>b.textContent='Copy',1600)};
  try{navigator.clipboard.writeText(b.dataset.t).then(done).catch(()=>{})}catch(e){}
}));

const tabs=[...document.querySelectorAll('[role="tab"]')];
function sel(t){tabs.forEach(x=>{const on=x===t;x.setAttribute('aria-selected',on);x.tabIndex=on?0:-1;document.getElementById(x.getAttribute('aria-controls')).hidden=!on;});}
tabs.forEach((t,i)=>{t.addEventListener('click',()=>sel(t));t.addEventListener('keydown',e=>{let j=null;if(e.key==='ArrowRight')j=(i+1)%tabs.length;if(e.key==='ArrowLeft')j=(i-1+tabs.length)%tabs.length;if(j!==null){e.preventDefault();sel(tabs[j]);tabs[j].focus();}});});

document.querySelectorAll('form.leadform').forEach(f=>{
  const a=f.querySelector('a.send'),done=f.querySelector('.done');
  const build=()=>{const fd=new FormData(f),map={};
    for(const [k,v] of fd){if(!String(v).trim())continue;(map[k]=map[k]||[]).push(v);}
    const head=f.dataset.kind==='seller'?'Hi Pascale, I would like a free market study for my home.':'Hi Pascale, I am looking for a home in Lisbon.';
    a.href='https://wa.me/351920609225?text='+encodeURIComponent(head+'\n\n'+Object.entries(map).map(([k,v])=>k+': '+v.join(', ')).join('\n'));};
  f.addEventListener('input',build);f.addEventListener('change',build);build();
  a.addEventListener('click',e=>{let ok=true;
    f.querySelectorAll('[required]').forEach(i=>{const bad=!i.value.trim();i.setAttribute('aria-invalid',bad);if(bad)ok=false;});
    if(!ok){e.preventDefault();done.hidden=false;done.innerHTML='<p class="err">Please fill in your name and phone number first.</p>';return;}
    build();done.hidden=false;done.innerHTML='<p>Thank you! WhatsApp is opening with your message. Just press send. I reply within one working day.</p>';});
  f.addEventListener('submit',e=>{e.preventDefault();a.click();});
});

const mb=document.getElementById('menu-btn'),ml=document.querySelector('.nav ul');
mb.addEventListener('click',()=>{const o=ml.classList.toggle('open');mb.setAttribute('aria-expanded',o);});
ml.addEventListener('click',e=>{if(e.target.closest('a')){ml.classList.remove('open');mb.setAttribute('aria-expanded','false');}});

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
   .catch(()=>{btn.disabled=false;const d=nf.querySelector('.news-done');d.hidden=false;d.textContent='Sorry, that did not go through. Please send me a message on WhatsApp: +351 920 609 225';});});}

document.querySelectorAll('.pm-pin,.pm-note').forEach(g=>{const go=()=>{const el=document.getElementById(g.dataset.target);if(!el)return;el.scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'center'});el.classList.add('flash');setTimeout(()=>el.classList.remove('flash'),1600);};
  g.addEventListener('click',go);g.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();go();}});});

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

// open a neighbourhood tab from the URL, e.g. /neighbourhoods/#tab-lapa
function tabFromHash(){const tb=document.getElementById(location.hash.slice(1));if(tb&&tb.getAttribute('role')==='tab'){sel(tb);markPins();const a=document.getElementById('areas');a&&a.scrollIntoView();}}
window.addEventListener('hashchange',tabFromHash);tabFromHash();

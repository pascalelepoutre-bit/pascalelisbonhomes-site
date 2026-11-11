// Website forms -> email to Pascale (replaces Netlify Forms).
// Runs as a Cloudflare Pages Function at POST /api/form.
// Needs two settings in Cloudflare (Settings > Variables and secrets):
//   RESEND_API_KEY  (secret)  key from resend.com, domain pascalelisbonhomes.com verified there
//   FORM_TO         (text)    pascale@pascalelisbonhomes.com
// Optional: FORM_FROM (default "Website Pascale <site@pascalelisbonhomes.com>")

const FORMS = {
  'buyer-search': 'Procura de comprador',
  'market-study': 'Estudo de mercado',
  'mortgage': 'Crédito habitação',
  'newsletter': 'Newsletter',
  'review': 'Avaliação',
  'referral': 'Recomendação',
  'selection-feedback': 'Opinião sobre seleção',
};
const MAX_TOTAL = 15 * 1024 * 1024; // 15 MB of attachments per submission
const SKIP = new Set(['form-name', 'bot-field', 'g-recaptcha-response']);

const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const json = (o, status = 200) => new Response(JSON.stringify(o), { status, headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' } });

function b64(buf) {
  let s = '', bytes = new Uint8Array(buf);
  for (let i = 0; i < bytes.length; i += 0x8000) s += String.fromCharCode.apply(null, bytes.subarray(i, i + 0x8000));
  return btoa(s);
}

export async function onRequestPost({ request, env }) {
  let fd;
  try { fd = await request.formData(); } catch { return json({ ok: false, error: 'bad form' }, 400); }

  const form = String(fd.get('form-name') || '');
  if (!FORMS[form]) return json({ ok: false, error: 'unknown form' }, 400);
  if (String(fd.get('bot-field') || '').trim()) return json({ ok: true }); // honeypot: quietly drop spam

  const rows = [], attachments = []; let total = 0, replyTo = '', who = '';
  for (const [k, v] of fd.entries()) {
    if (SKIP.has(k)) continue;
    if (typeof v === 'object' && v && 'arrayBuffer' in v) {
      if (!v.size) continue;
      total += v.size;
      if (total > MAX_TOTAL) { rows.push([k, `${v.name} (too large, not attached)`]); continue; }
      attachments.push({ filename: v.name || k, content: b64(await v.arrayBuffer()) });
      rows.push([k, `📎 ${v.name}`]);
      continue;
    }
    const val = String(v).trim();
    if (!val) continue;
    rows.push([k, val]);
    if (!replyTo && /e-?mail/i.test(k) && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val)) replyTo = val;
    if (!who && /^(name|nome|nom|naam|cliente)$/i.test(k)) who = val;
  }
  if (!rows.length) return json({ ok: false, error: 'empty' }, 400);

  const page = request.headers.get('Referer') || '';
  const subject = `Website: ${FORMS[form]}${who ? ' · ' + who : ''}`;
  const text = rows.map(([k, v]) => `${k}: ${v}`).join('\n') + `\n\nFormulário: ${form}\nPágina: ${page}\n`;
  const html = `<h2 style="font-family:Arial,sans-serif">${esc(FORMS[form])}</h2>
<table cellpadding="6" style="font-family:Arial,sans-serif;font-size:14px;border-collapse:collapse">
${rows.map(([k, v]) => `<tr><td style="color:#6f655a;vertical-align:top;border-bottom:1px solid #eee"><b>${esc(k)}</b></td><td style="border-bottom:1px solid #eee;white-space:pre-wrap">${esc(v)}</td></tr>`).join('\n')}
</table>
<p style="font-family:Arial,sans-serif;font-size:12px;color:#999">Formulário: ${esc(form)} · Página: ${esc(page)}</p>`;

  const msg = {
    from: env.FORM_FROM || 'Website Pascale <site@pascalelisbonhomes.com>',
    to: String(env.FORM_TO || 'pascale@pascalelisbonhomes.com').split(',').map(s => s.trim()),
    subject, text, html,
  };
  if (replyTo) msg.reply_to = replyTo;
  if (attachments.length) msg.attachments = attachments;

  if (env.DRY_RUN) return json({ ok: true, dry: { ...msg, attachments: attachments.map(a => a.filename) } });
  if (!env.RESEND_API_KEY) return json({ ok: false, error: 'email not configured' }, 500);

  const r = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify(msg),
  });
  if (!r.ok) return json({ ok: false, error: 'send failed', status: r.status, detail: (await r.text()).slice(0, 300) }, 502);
  return json({ ok: true });
}

export const onRequest = () => json({ ok: false, error: 'POST only' }, 405);

# pascalelisbonhomes.com

- `site/` is the live website, published by Netlify.
- `source/` holds the single-page source and the build scripts that generate `site/`.

## Hosting: Cloudflare Pages (since Nov 2026, replaces Netlify)
- Build command: none. Build output directory: `site`. Production branch: `main`.
- Forms: every form posts to `/api/form` → `functions/api/form.js` → email via Resend to FORM_TO.
- Settings needed in Cloudflare (Variables and secrets): `RESEND_API_KEY` (secret), `FORM_TO` = pascale@pascalelisbonhomes.com.
- Private buyer selection pages: `source/selections/<slug>/` → `/s/<slug>/` (noindex).

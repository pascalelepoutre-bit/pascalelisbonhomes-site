# Going live: pascalelisbonhomes.com

## What's in this folder
| File | What it is |
|---|---|
| index.html | Homepage (selling, a selection for sale, FAQ, newsletter) |
| for-sale/ | All homes for sale in Estrela, Lapa & Santos |
| buying/ · neighbourhoods/ · market-report/ · my-lisbon/ | One page each, with its own address |
| 404.html | Shown when someone opens a wrong link |
| style.css · site.js | Design and behaviour, shared by all pages |
| img/ | Photos (compressed WebP) and the sharing image |
| sitemap.xml · robots.txt | For Google, Bing and AI search tools |
| _headers | Tells the browser to keep photos in cache (Netlify) |

Colleagues' listing photos load directly from the Engel & Völkers photo server, so they always stay up to date.

## 1. Put the site online (Netlify)
1. Log in at app.netlify.com with your personal email.
2. Add new site → Deploy manually → drag this whole folder onto the page.
3. Site settings → Domain management → Add domain → pascalelisbonhomes.com. Follow the steps to point the domain (DNS) to Netlify, and turn on HTTPS (automatic).
4. Forms → enable form detection, so the newsletter sign-ups arrive in Netlify (Forms → newsletter). Set an email notification to yourself.
5. Check that https://pascalelisbonhomes.com and https://www.pascalelisbonhomes.com both open the site.

## 2. Google Search Console
1. search.google.com/search-console → Add property → **Domain** → pascalelisbonhomes.com.
2. Add the TXT record Google shows at your domain provider (DNS settings), then click Verify.
3. Sitemaps → enter `sitemap.xml` → Submit.
4. URL inspection → paste each page address → Request indexing:
   - https://pascalelisbonhomes.com/
   - https://pascalelisbonhomes.com/for-sale/
   - https://pascalelisbonhomes.com/neighbourhoods/
   - https://pascalelisbonhomes.com/market-report/
   - https://pascalelisbonhomes.com/buying/
   - https://pascalelisbonhomes.com/my-lisbon/
5. Optional check: search.google.com/test/rich-results with the homepage address. It should find "Local business" and "FAQ".

## 3. Bing (also feeds ChatGPT search)
bing.com/webmasters → Import from Google Search Console. One click.

## 4. Google Business Profile (biggest effect for "real estate agent Estrela")
- Category: Real estate agent
- Service-area business: hide the address, service areas Estrela, Lapa, Santos, Campo de Ourique
- Website: https://pascalelisbonhomes.com
- Ask happy clients for a review there.

## 5. When something changes
New listings, new photo, new text: just ask Claude. Claude updates the GitHub repository pascalelepoutre-bit/pascalelisbonhomes-site and Netlify publishes it automatically within a minute. No zip or drag and drop needed.

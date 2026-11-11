#!/bin/bash
# Rebuild the site and push it to GitHub; Netlify publishes automatically.
set -e
cd /home/claude
python3 build_site.py >/dev/null
R=/home/claude/pascalelisbonhomes-site
rm -rf $R/site && cp -r site $R/site && rm -f $R/site/SETUP.md && date -u +%Y-%m-%dT%H:%M:%SZ > $R/site/version.txt
# private buyer selection pages (not in the sitemap, noindex): source/selections/<slug> -> /s/<slug>/
mkdir -p $R/site/s && cp -r $R/source/selections/. $R/site/s/
# extra files used by the selection pages, e.g. /img/pascale-lepoutre-portrait.webp
[ -d $R/source/extra ] && cp -r $R/source/extra/. $R/site/
cp pascale-site.html build_site.py add_homes.py SETUP.md robots.txt deploy.sh $R/source/
cp img/share.png $R/source/img/
cd $R
git add -A
git -c user.name="Pascale Lepoutre" -c user.email="pascalelepoutre@yahoo.com" commit -qm "${1:-Website update}

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01STAcs2V5tfNV6w3r8MR3hh" || { echo "nothing to commit"; exit 0; }
git push -q
git log --oneline -1

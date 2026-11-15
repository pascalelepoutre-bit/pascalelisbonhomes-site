Build tools for buyer selection pages. Not published: Netlify only publishes site/.

Setup in a fresh session:
  mkdir -p /home/claude/scripts /home/claude/clients /home/claude/work
  cp tools/scripts/* /home/claude/scripts/; cp tools/clients/* /home/claude/clients/; cp tools/work/* /home/claude/work/

Pascale's pre-selection tool, António & Mafalda round 2:
  KEEP=<ids in order> python3 /home/claude/scripts/build_preselect.py source/selections/am-voorselectie-p9x4 "António & Mafalda" am-pre2c-p9x4
Client page:
  KEEP=<her picks> python3 /home/claude/scripts/build_selection2.py source/selections/antonio-mafalda-selecao2-p9x4 "António & Mafalda" <new storage key>
Then: cp -r source/selections/<dir> site/s/ ; commit ; git pull --rebase --autostash ; push. Netlify deploys in about a minute.
House data lives in tools/clients/am_round2.py (HOUSES list plus appended blocks). Keep it in sync when adding houses.

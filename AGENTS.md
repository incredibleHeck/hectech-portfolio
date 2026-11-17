# Agent instructions — HecTech portfolio

Hector Aryiku's portfolio: one static page (`index.html`), a portfolio PDF and a CV,
served from Firebase Hosting at `hectech.web.app`. No build step, no framework.
**This repository is public.**

**Read first:** [`README.md`](README.md), then [`documents/README.md`](documents/README.md)
for how the PDFs and CV are built.

## Rules that are not style preferences

**Every figure carries its provenance.** Each number is paired with the file or
deployment it came from. Change a number and you change its source line in the
same edit.

**All line counts come from one rule, on one date.** Git-tracked application
source (`.ts .tsx .js .jsx .mjs .cjs .css .scss .py .rs .html .sql .vue .svelte`),
excluding lockfiles, `.min.*` and build output. The current figures and the date
are in [`documents/README.md`](documents/README.md). If you re-measure one
project, re-measure all ten — a figure on a different basis from the one beside
it is worse than no figure.

**Never state a claim you have not verified in the source.** Read the project's
code, not its README and not this repository. If two sources disagree, trust the
code and say which document is stale.

**Never claim a technology absent from the project repositories** — including to
make a CV fit a job advert.

**Two CV variants, and the private one never ships.** `CV_Hector_Aryiku` says
references are available on request. `CV_Hector_Aryiku_with-references` carries
referees' contact details: gitignored, never deployed, never committed — and that
includes the *source* the build reads from.

**Check every URL you write returns 200.** `heckteck-school.web.app` is dead; the
school portal is `sais-portal.web.app`.

**Keep the PDFs crawlable and `noindex`.** They are served with
`X-Robots-Tag: noindex, noarchive`; `robots.txt` must not Disallow them, or crawlers
never fetch them and never see the header.

**Never delete `googlee24267d6dad38a06.html`** — it verifies the Search Console
property. `cleanUrls` stays `false`, because it redirected that exact path.

**Do not deploy.** A human runs
`npx firebase deploy --only hosting --project hectech-portfolio`.

## Before you say something works

Serve the folder (`python -m http.server 5177`) and look at the page. After editing
`documents/`, rebuild the PDFs with the commands in `documents/README.md` and check
the page counts and text of what was produced.

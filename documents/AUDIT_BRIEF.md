# Brief: audit and strengthen Hector Aryiku's professional presence

You are auditing a working engineer's public materials — a portfolio site, a
portfolio PDF, a CV, and the GitHub presence around them — and proposing
specific, evidenced improvements. Read this whole brief before touching
anything.

---

## 1. Who this is for

**Hector Nii Armaakwei Aryiku**, Accra, Ghana. Systems and full-stack product
engineer, and a practising Cambridge Computing, Digital Literacy and Mathematics
teacher at St. Adelaide International Schools since August 2021. He builds the
software that school runs on — grading, timetabling, diagnostics, reporting —
and several of those systems are live and in daily use.

BSc Telecommunication Engineering (Ghana Technology University College, degree
awarded by KNUST, conferred 2018). Database Manager at UMB Bank 2019–2020.
No formal employment as a software engineer at a software company.

**The through-line of his work:** software that keeps working when conditions
don't cooperate — offline-first because the network fails, one-time purchase
because subscriptions don't suit the market, thermal printers driven from raw
bytes because there is no vendor driver — and claims that survive checking.

**What he wants:** engineering roles and consultancy work, locally in Ghana and
internationally/remote. He is also considering a Master's in CS/AI. He is not
well known, so his detail *is* his credential — do not assume brevity is an
improvement.

---

## 2. What exists, and where

### The website — `https://hectech.web.app`
Source: this repository. Single static page, no build step, no framework.

```
index.html                 the entire site
assets/                    logo variants, photo, the served PDFs
documents/                 sources for the PDFs (not deployed)
firebase.json              hosting config, headers, redirects
firestore.rules            contact-form rules, create-only
robots.txt  sitemap.xml    crawl directives
```

Deployed with `npx firebase deploy --only hosting --project hectech-portfolio`.
Hosting site is `hectech`; project is `hectech-portfolio`.

### The documents
`documents/portfolio.html` → the 9-page portfolio PDF.
`documents/cv.html` → the CV, 3 pages, via `documents/build_cv.py`.
`documents/build_cv_supertech.py` → a worked example of tailoring the CV to one
job advert. Read `documents/README.md` first.

### GitHub — `github.com/incredibleHeck`
`hectech-portfolio` (this repo, public) and `incredibleHeck` (profile README,
public). **Every other project repository is private**, because they hold live
school and customer data. The public profile otherwise shows prototypes and
two forks, which is why the profile README exists to explain the gap.

### The projects themselves
Read these directly. They are the evidence base:

| Project | Path |
|---|---|
| BaseCamp Diagnostics | `C:\Users\me\BaseCamp` |
| SAIS Portal | `C:\Users\me\reportsystem\report-system-website` |
| EduScheduler Pro | `C:\EduScheduler` |
| Nexus Inventory | `C:\Users\me\nexus pro\nexus` |
| Victor draughts engine | `C:\Users\me\victor` |
| Doxamix Foods | `C:\Users\me\doxamix-foods` |
| Academic Compliance | `C:\Users\me\lpauditor` |
| Report Generator | `C:\googlesheets` |
| QuantSports Engine | `C:\Users\me\quantsportsengine` |
| 3D Ludo | `C:\Users\me\3Dludo` |

Live: `sais-portal.web.app`, `sais-lessons.web.app`, `basecamp-pilot.web.app`,
`doxamix-foods.web.app`.

Deliberately excluded so far: **Lanita LMS** (a VPS hardening job he says is
unfinished) and **my-timetable-app** (superseded by EduScheduler). Do not add
either without asking.

---

## 3. Rules you must not break

These were decided deliberately. If you think one is wrong, argue it in your
report — do not just change it.

**Every figure carries its provenance.** The site and PDF pair each number with
the file or deployment it came from (`615 periods … / CHANGELOG.md v1.0.0`). If
you change a number, change its source line in the same edit. This is the
design's central idea, not decoration.

**Never state a claim you have not verified in the source.** An earlier pass
found three errors this way: a migration count that was five in the docs and
seven in the code, an "in daily use" claim contradicted by an unsigned Android
build, and a performance figure taken from a stale CV. Read the code, not the
README, and not this brief.

**Never claim a technology absent from the repositories.** He does **not** use
Java, Spring Boot, Kafka, Keycloak, Angular, Oracle or SSRS. Adding any of these
to make a CV fit an advert is out of bounds.

**The two CV variants must stay separate.** `CV_Hector_Aryiku` says references
are available on request. `CV_Hector_Aryiku_with-references` carries referees'
names, email and phone numbers, is gitignored, and is never deployed. Referees
consented to being contacted by an employer, not to being indexed.

**`heckteck-school.web.app` is dead** (404). The portal is `sais-portal.web.app`.
Check every URL you touch actually resolves — one dead link already shipped.

**Keep `noindex` on the PDFs and keep them crawlable.** They are served with
`X-Robots-Tag: noindex, noarchive`, and `robots.txt` must *not* Disallow them —
a crawler has to fetch a file to read that header. Those two directives cancel
out if you block the fetch.

**Do not delete `googlee24267d6dad38a06.html`.** It is the Search Console
verification file; removing it un-verifies the property. `cleanUrls` is `false`
because it 301'd that exact path and broke verification.

---

## 4. What to audit

Work through these. For each, decide whether there is a real problem before
proposing a change — "could be improved" is not a finding.

### A. Accuracy and evidence
Re-verify every factual claim on the site, in the portfolio PDF and in the CV
against the actual source code. List anything that is wrong, unverifiable, or
stated more strongly than the evidence supports. This matters more than anything
else in this brief: the portfolio's entire argument is that its claims hold up.

### B. The website as a persuasion document
Does the page make the case in the first screen? Is the ordering right for a
hiring manager who will give it ninety seconds? Is anything load-bearing buried?
Assess the actual reading experience, not the code.

Check accessibility properly — contrast ratios, keyboard focus, heading order,
alt text, reduced-motion — and report measured numbers, not impressions.

### C. Discoverability
The site is new and has almost no inbound links. What would actually make him
findable when someone searches his name, or searches for an engineer with his
skills in Accra? Consider structured data (`Person`, `SoftwareApplication`),
metadata, page titles, and where a real inbound link could plausibly come from.
Be concrete; generic SEO advice is not useful.

### D. The gap between what he has and what he shows
He has strong private work and a thin public footprint. What is the highest-value
thing he could publish that costs him nothing in client confidentiality? Consider
whether any project could be extracted, anonymised, or written up as an article
rather than a repository.

Victor — the draughts engine — is the obvious candidate: no customer data, real
systems depth, and a public release planned for **January 2027**. Assess whether
that timing should change and what should ship alongside it.

### E. Positioning, local and international
He is competing in two different markets with one set of materials. Does that
work? Consider what an Accra employer, a remote-first international company, and
a Master's admissions committee each need to see, and whether one page can serve
all three or whether something should be split.

The teacher-who-builds angle is his strongest differentiator — almost no
engineer can say they are the domain expert *and* the implementer. Assess whether
the materials use it hard enough, or whether it reads as a side note.

### F. Everything else
Contact form, performance, the GitHub profile README, LinkedIn, whether a
writing habit would pay off, and anything you notice that this brief did not
anticipate. The last category is the valuable one.

---

## 5. How to report

Produce **`documents/AUDIT_FINDINGS.md`**. Structure it as:

1. **What is wrong** — factual errors and broken things, most serious first.
   Each with the file, the line, the evidence, and the fix.
2. **What is weak** — real but not broken. Same structure.
3. **What is missing** — opportunities, ranked by value against effort.
4. **What I would do first** — five things, in order, with reasoning.

For every finding, state **how you verified it**. A finding without evidence is
a guess, and guesses are worse than silence here.

Rank by impact on his actual goal — getting hired and getting client work — not
by how easy something is to fix.

**Do not make changes yet.** Report first. He decides what to act on.

Two exceptions you may fix in place, because they are unambiguous: a URL that
returns 404, and a factual claim contradicted by the source code. Note any such
fix clearly in the report.

---

## 6. Ground rules

- Read the actual code before describing what a project does.
- Verify externally-facing URLs return 200 before writing them anywhere.
- When you cite a number, say where you read it.
- If two sources disagree, trust the code, then say which document is stale.
- If something is genuinely good, say so briefly and move on. Don't pad.
- If you think an instruction in this brief is wrong, say so and explain why.

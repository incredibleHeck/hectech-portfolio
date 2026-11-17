# Document sources

The portfolio PDF and the CV are generated from the HTML in this folder, so the
web and print versions of the same facts cannot drift apart.

| Source | Produces |
|---|---|
| `portfolio.html` | `assets/Hector_Aryiku_Engineering_Portfolio.pdf` — 10 pages |
| `cv.html` | the CV, in two variants (below) |
| `build_cv.py` | both CV variants, PDF and .docx |
| `build_cv_supertech.py` | a role-tailored CV; copy it per application |

## Rebuilding

```bash
cd documents
python build_cv.py            # both CV variants
```

The portfolio PDF renders with headless Chrome. **Both paths must be absolute and
the input must be a `file:///` URL.** Given a bare filename, Chrome treats it as a
hostname, fails to resolve it, and exits without writing anything — leaving the
previous PDF in place and looking like a successful build. That happened once;
check the file's timestamp afterwards.

```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --headless --disable-gpu --no-sandbox --no-pdf-header-footer --virtual-time-budget=20000 --print-to-pdf="C:\Users\me\hectech-portfolio\assets\Hector_Aryiku_Engineering_Portfolio.pdf" "file:///C:/Users/me/hectech-portfolio/documents/portfolio.html"
```

Then confirm what was produced:

```bash
python -c "from pypdf import PdfReader; print(len(PdfReader(r'../assets/Hector_Aryiku_Engineering_Portfolio.pdf').pages))"
```

## Two CV variants, and why

`build_cv.py` emits both from the same source:

- **`CV_Hector_Aryiku`** — says "references available on request". This is the
  one on the website and the one to upload anywhere public.
- **`CV_Hector_Aryiku_with-references`** — carries the referees' names, email and
  phone numbers. **Never publish this.** It is gitignored and not deployed. Send it
  to a named employer who has asked.

Referees gave those details so they could be passed to an employer, not so they
could be indexed. The split exists to keep that true by construction.

## How the line counts are measured

Every `~NNk LOC` figure on the site, in the portfolio PDF and in the CV comes from
one rule, so the projects are comparable with each other:

> **Git-tracked application source.** Files matching
> `.ts .tsx .js .jsx .mjs .cjs .css .scss .py .rs .html .sql .vue .svelte`, taken
> from `git ls-files`, excluding lockfiles, `.min.*`, and anything under
> `dist/ build/ out/ .next/ target/ node_modules/`.

It deliberately excludes markdown, JSON data fixtures and binary assets. Counting
those made the largest project the one with the biggest curriculum file, which is
not what the figure is meant to say. Measured on **2026-11-17**:

| Project | Lines | Files | Last commit |
|---|---:|---:|---|
| Academic Compliance | 125,220 | 512 | 2026-11-15 |
| SAIS Portal | 101,436 | 424 | 2026-11-17 |
| BaseCamp Diagnostics | 76,212 | 321 | 2026-09-15 |
| EduScheduler Pro | 71,916 | 413 | 2026-09-07 |
| Victor | 29,433 | 140 | 2026-10-26 |
| 3D Ludo | 28,663 | 123 | 2026-11-10 |
| Nexus Inventory | 23,107 | 231 | 2026-10-22 |
| QuantSports Engine | 19,949 | 87 | 2026-09-19 |
| Report Generator | 12,224 | 54 | 2026-07-03 |
| Doxamix Foods | 10,523 | 106 | 2026-09-30 |

Nexus is measured from a fresh clone of the private `incredibleHeck/nexuspearl`
repository; it is no longer on this machine.

If you re-measure, re-measure **all of them**, and change the date in the receipt
line on `index.html` in the same edit. A figure taken on a different basis from
the one beside it is worse than no figure at all.

## Rules that are not style preferences

- **Every figure carries its provenance.** If you change a number, change the
  source line under it in the same edit. That pairing is the whole design.
- **Never claim a technology that is not in the repositories.** The tailored CV
  build asserts this; keep it that way.
- Rendered PDFs are gitignored here and committed under `assets/` only when they
  are the version being served.

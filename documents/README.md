# Document sources

The portfolio PDF and the CV are generated from the HTML in this folder, so the
web and print versions of the same facts cannot drift apart.

| Source | Produces |
|---|---|
| `portfolio.html` | `assets/Hector_Aryiku_Engineering_Portfolio.pdf` — 9 pages |
| `cv.html` | the CV, in two variants (below) |
| `build_cv.py` | both CV variants, PDF and .docx |
| `build_cv_supertech.py` | a role-tailored CV; copy it per application |

## Rebuilding

```bash
cd documents
python build_cv.py            # both CV variants
```

The portfolio PDF renders with headless Chrome:

```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --headless --disable-gpu \
  --no-pdf-header-footer --virtual-time-budget=15000 \
  --print-to-pdf="..\assets\Hector_Aryiku_Engineering_Portfolio.pdf" portfolio.html
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

## Rules that are not style preferences

- **Every figure carries its provenance.** If you change a number, change the
  source line under it in the same edit. That pairing is the whole design.
- **Never claim a technology that is not in the repositories.** The tailored CV
  build asserts this; keep it that way.
- Rendered PDFs are gitignored here and committed under `assets/` only when they
  are the version being served.

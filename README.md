# HecTech — portfolio site

Personal engineering portfolio for Hector Aryiku. One static HTML page, no build
step, no framework, no tracker. Open `index.html` and it works.

```
index.html          the whole site
assets/hector.jpg   portrait
assets/*.pdf        downloadable portfolio (10 pages) and public CV (4 pages)
firebase.json       hosting config — site name "hectech"
firestore.rules     contact-form rules (create-only, no reads)
```

## Preview locally

```bash
python -m http.server 5177
```

Then open <http://127.0.0.1:5177>. Any static server works; there is nothing to compile.

## Deploy

The hosting site is named `hectech`, which gives `hectech.web.app` regardless of
which Firebase project it belongs to — the same pattern `lpauditor` uses to serve
`sais-lessons.web.app` from a project called `lpauditor-app`.

Create the site once, then deploy:

```bash
npx firebase login
npx firebase use <your-project-id>
npx firebase hosting:sites:create hectech
npx firebase deploy --only hosting
```

If `hectech` is already taken, pick another name and change `hosting.site` in
`firebase.json` to match.

## Contact form

**Where messages go.** Set `FORM_ENDPOINT` near the bottom of `index.html` to a
Formspree form address (`https://formspree.io/f/…`). Each message is then POSTed
there, emailed to the Formspree account's address, and kept in the Formspree
dashboard. The free plan covers 50 messages a month.

**With `FORM_ENDPOINT` empty** — and whenever the POST fails — the form opens the
visitor's mail app with the message filled in, and copies the message to their
clipboard. A `mailto:` link does nothing on a device with no mail app configured,
so the copy is what stops a message being lost. The page only ever says "sent"
after Formspree confirms delivery.

The honeypot field (`company`) is hidden from people; if a bot fills it the
submission is dropped before anything is sent.

`firestore.rules` is from an earlier design that stored messages in Firestore.
It was never deployed — Firestore is not enabled on the `hectech-portfolio`
project — and nothing uses it now.

## Notes

- **The reveal animation is progressive.** Content is visible by default; the
  scroll reveal only arms itself once JS sets `.js` on `<html>`. A script failure
  cannot leave the page blank, and `prefers-reduced-motion` skips it entirely.
- **`heckteck-school.web.app` is dead** (404). The school portal now lives at
  `sais-portal.web.app`. Do not link the old address anywhere.
- **Every figure on the page carries its source.** If you change a number, change
  the provenance line under it too — that pairing is the point of the design.

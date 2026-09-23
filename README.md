# HecTech — portfolio site

Personal engineering portfolio for Hector Aryiku. One static HTML page, no build
step, no framework, no tracker. Open `index.html` and it works.

```
index.html          the whole site
assets/hector.jpg   portrait
assets/*.pdf        downloadable portfolio (4 pages)
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

The form works with no setup: it opens the visitor's mail client with the message
prefilled. That is the fallback, and it is the current behaviour.

To collect messages in Firestore instead, add a config block before the closing
`</body>` tag in `index.html`:

```html
<script>
  window.__HECTECH_FIREBASE__ = {
    apiKey: "...",
    authDomain: "<project>.firebaseapp.com",
    projectId: "<project>",
    appId: "..."
  };
</script>
```

Then deploy the rules:

```bash
npx firebase deploy --only firestore:rules
```

Messages land in the `contact_messages` collection. The rules allow `create` only —
nobody can read, edit or delete a message from the browser, including the sender.
Read them in the Firebase console, or with the CLI.

Three things guard the form: a hidden honeypot field that bots fill and humans
never see, field-length caps enforced in the rules rather than only in the client,
and a strict field allow-list so an extra key in the payload is rejected outright.

If the Firestore write fails for any reason, the form falls back to the mail client
rather than failing silently. The visitor always gets a definite outcome.

## Notes

- **The reveal animation is progressive.** Content is visible by default; the
  scroll reveal only arms itself once JS sets `.js` on `<html>`. A script failure
  cannot leave the page blank, and `prefers-reduced-motion` skips it entirely.
- **`heckteck-school.web.app` is spelled that way on purpose.** It is the live URL
  of a school's production system. The brand is "HecTech" everywhere else; the
  domain cannot be respelled without standing up a new hosting site and migrating
  the users on it.
- **Every figure on the page carries its source.** If you change a number, change
  the provenance line under it too — that pairing is the point of the design.

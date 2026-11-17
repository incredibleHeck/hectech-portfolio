# Review — `hectech_portfolio_and_pitches.md`

Checked against the codebases on 2026-11-17. Every figure below was measured
from **git-tracked source** (`git ls-files` piped to `wc -l`), which is the same
basis the live site's provenance lines claim, so the numbers are comparable.

---

## 1. The finding that matters most

**Academic Compliance is now your largest and most active project, and your
materials describe it as a minor one.**

| Project | Tracked lines | Files | Last commit |
|---|---:|---:|---|
| **Academic Compliance** (`lpauditor`) | **123,110** | 502 | **2026-11-15** |
| BaseCamp Diagnostics | 75,584 | 317 | 2026-09-15 |
| EduScheduler Pro | 71,555 | 410 | 2026-09-07 |
| Victor | 28,966 | 134 | 2026-10-26 |
| 3D Ludo | 28,495 | 120 | 2026-11-10 |
| QuantSports Engine | 18,696 | 84 | 2026-09-19 |
| Doxamix Foods | 10,249 | 103 | 2026-09-30 |

Two consequences:

**The site's claim that BaseCamp is "the largest codebase" is now false.**
Academic Compliance is 63% bigger. That is a provenance-carrying figure on the
hero, so it needs correcting or requalifying.

**It is no longer a lesson-plan auditor.** Since September it has grown a lesson
**video pipeline** (upload, library, player, AI suggestions, coverage tracking,
review workflow, channel settings, S3 storage), a **standalone pupil portal**, an
**interactive AI chat panel**, **lesson packs** with print sheets and a plenary
projector view, an **admin staff directory**, and an **Inngest** background-job
system — a 1,670-line functions module with a 2,520-line test against it.
195 of its 502 files are tests.

Its access control is enforced in **four layers**: Firestore rules, Storage
rules, a Next.js edge proxy, and server-action permission checks. That is a
stronger version of the "client check is never the boundary" argument your
portfolio already makes, and it is currently invisible.

It is also on **Next.js 16 and React 19** — directly relevant to the roles this
pitch document targets, and not claimed anywhere.

**Recommendation:** promote it to a flagship, rewrite it from the current code,
and move the "largest codebase" figure onto it.

---

## 2. Errors to fix before sending anything

### 2.1 Twelve broken links

Three URLs appear wrapped in Google search redirects, 12 times in total:

```
https://www.google.com/search?q=https://basecamp-pilot.web.app/   (×4)
https://www.google.com/search?q=https://sais-lessons.web.app/     (×5)
https://www.google.com/search?q=https://sais-portal.web.app/      (×3)
```

These are in the cover letters and the Upwork proposal. They are not links to
your work — they are links to a Google results page. Replace with the direct
addresses, all of which return 200.

### 2.2 EduScheduler is not a Rust engine

The document calls it a *"~72k LOC Rust/Tauri constraint-solving timetable
engine"* (Track A and Pitch 2). Measured:

```
src-tauri/build.rs        3 lines
src-tauri/src/lib.rs     18 lines
src-tauri/src/main.rs     6 lines
                     --------------
TOTAL RUST               27 lines
```

The Rust is Tauri shell boilerplate. **The solver is TypeScript** — 11,443 lines
under `src/features/generator/`, with `solver.ts`, `heuristics.ts`, `search.ts`,
`tabu.ts` and the repair controller.

Say "Tauri v2 desktop app with a TypeScript constraint solver". The work is
impressive on its own terms; the current phrasing collapses the moment someone
asks what the Rust does.

### 2.3 The solver description is out of date — in your favour

The materials say "MRV ordering with backtracking". The code now also contains
**tabu search** (60 references) and a **repair phase** (137 references,
`repair-controller.ts` / `repair-executor.ts`). It is a hybrid local-search
solver, which is a stronger claim than the one being made.

### 2.4 "Recognized by the UNICEF StartUp Lab"

Used repeatedly. What you have is a **Certificate of Participation** in the
Learning Gaps Challenge, March 2026. "Recognized by" implies selection or an
award. This distinction was deliberate in the existing CV; the pitch document
drops it. One sceptical reader checking this costs you more than the phrase buys.

### 2.5 "127+ automated test suites"

It is **127 tests**, not suites, and the `+` inflates a counted number. Also note
Nexus is no longer on this machine — see §3.

### 2.6 LinkedIn handle conflict

The document header says `hectorheckteck`. Your CV, site and GitHub profile all
say `hector-aryiku-028b3b203`. LinkedIn returns HTTP 999 to automated checks so I
could not resolve which is current. **Confirm before sending** — a dead LinkedIn
link in a cover letter is worse than none.

---

## 3. Nexus Inventory is no longer on this machine

`C:\Users\me\nexus pro\` does not exist. I searched for `printer.rs`, `nusb` and
any `nexus*` directory and found nothing locally.

The GitHub repository is alive — `incredibleHeck/nexuspearl`, private, last
pushed **2026-10-22** — so the project is fine. But its claims (127 tests,
ESC/POS over TCP and USB, seven migrations, AES-256-GCM) can no longer be
verified from source here. If you keep citing them, clone it back so the numbers
stay checkable.

---

## 4. What the document gets right

Worth saying, because most of it is sound:

- **`~77k` for BaseCamp is accurate.** Tracked source is 75,584 lines. I
  initially thought this was wrong — it is not, and the live provenance line
  ("tracked source, measured 2026-09-23") is honest.
- **`~28k` for Victor is accurate** (28,966 tracked).
- **`~72k` for EduScheduler is accurate** (71,555 tracked) — only the "Rust"
  attribution is wrong.
- **26 tests for Doxamix, 10 departments, 5 years of grading data, 615 periods,
  7 British Council certifications** — all check out.
- All five live URLs return 200.
- The service-card structure and the three CV tracks are a genuinely good idea.
  The Upwork "AI app rescue" angle is well matched to what you have actually
  built.

---

## 5. One strategic concern

The document tries to serve two incompatible audiences from one hero.

"**Vibe Coding Instructor**" is exactly right for the Academy of Digital
Industries and Kraftshala roles. It is a liability for the G2i and Phantom
engineering roles, where "vibe coding" is widely used as a pejorative for
unverified AI output.

Your actual differentiator is the **opposite** of that connotation: guardrails in
`AGENTS.md`, tests as gates, a published Elo claim retracted when the benchmark
proved faulty. The existing portfolio makes that argument well. A hero that leads
with "Vibe Coding" invites a senior engineer to assume the thing you have spent
most effort disproving.

**Suggestion:** keep one hero — the engineer — and put the instruction offer in
the services section, where it reads as range rather than as your identity. The
instructor cover letters can lead with teaching without the site having to.

Two smaller notes: **"founder of HecTech"** implies a registered entity — if it
is a trading name rather than a company, "I build as HecTech" is safer. And
**"10 shipped systems"** is used alongside "10+ live systems"; four are live, ten
are built. Keep the two words apart.

---

## 6. What I would do, in order

1. **Fix the 12 Google-redirect links.** Five minutes, and they appear in
   material you are about to send.
2. **Correct the EduScheduler Rust claim** everywhere it appears.
3. **Confirm the LinkedIn URL.**
4. **Rewrite Academic Compliance from its current code** and promote it to a
   flagship on the site, in the portfolio PDF and in the CV. It is your largest,
   most active and most commercially legible system, and it is currently a
   footnote.
5. **Decide the hero question** in §5 before rewriting any site copy.

Items 1–3 are corrections. Item 4 is the one that changes how strong you look.

---

## 7. What was fixed — 2026-11-17

Everything in §1–§6 above was acted on, plus what re-measuring turned up. The
figures below were taken the same day on one rule (`documents/README.md`).

### Corrected findings in this report

| § | Finding | Action |
|---|---|---|
| 1 | Academic Compliance presented as a minor system | Rewritten from current source and promoted to **slot 01** on the site, to lead the Education Technology flagship in the portfolio PDF, and to the **first project entry** in the CV |
| 1 | "BaseCamp is the largest codebase" | Receipt now reads **~125k · Academic Compliance · tracked source, measured 2026-11-17** |
| 2.1 | Twelve Google-redirect links | All replaced with direct URLs in `documents/pitches.md`; every URL re-checked (13 return 200, 3 are bot-blocks that load in a browser) |
| 2.2 | EduScheduler called a Rust engine | Now "**11,443 lines of TypeScript — not Rust**"; the rail says "27-line Rust shell"; the bare `Rust` chip is gone |
| 2.3 | Solver description understated | **Tabu search** and the **repair phase** named on the site, in the PDF, in the CV skills line and in the competencies block |
| 2.4 | "Recognized by the UNICEF StartUp Lab" | **Certificate of Participation**, Learning Gaps Challenge, March 2026 — everywhere |
| 2.5 | "127+ automated test suites" | Replaced with run figures: **2,392 passing** (Academic Compliance), **140** (Doxamix), **129 counted in source** (Nexus) |
| 2.6 | LinkedIn handle conflict | Made consistent at `hectorheckteck`; **still unverified** — LinkedIn returns 999. The GitHub profile README disagrees and needs the same fix once you confirm which loads |
| 5 | Hero serving two incompatible audiences | Settled, with a surface-by-surface table in §0 of `documents/pitches.md`. "Vibe coding" now appears only where it is the advertised job title |
| 5 | "founder of HecTech" | "I build as HecTech" |
| 5 | "10 shipped" vs "10+ live" | "Ten built; seven running in a school or business; four on public URLs" |

### Found while re-measuring, also fixed

- **SAIS Portal is ~101k lines and was committed today** — second largest here,
  and that was in neither document. Added to the index and its rail.
- **Doxamix has 140 tests, not 26**, across 34 files (`npx vitest run`, green).
- **The September audit's most serious code finding was remediated.** The Doxamix
  orders collection no longer carries `allow create: if true`: there is schema
  validation with `hasOnly`, bounded line items, `status` pinned to `pending`,
  `createdAt` pinned to server time, `email_verified` on order reads, a
  `mergeOrderItems` helper rejecting zero/negative/fractional/string quantities,
  and an idempotency guard. The claim on the site has been rewritten **upward**
  to four layers, and it now states that an earlier version of the page made a
  claim the rules did not support.
- **Nexus "key derivation" was wrong.** `derive_key` is a single
  `SHA-256(salt ‖ passphrase)`, confirmed in a fresh clone of `nexuspearl`. The
  site and PDF now say so plainly, and name Argon2id as the fix.
- **Nexus delivery is now evidenced** — `docs/STATUS.md` carries a dated
  owner confirmation (2026-09-23), cited in the rail.
- **Report Generator is 12 spreadsheets, not 13**, and one campus, not three
  (`dev-tools/fleet/fleet_inventory.json`).
- **"Each repository carries an AGENTS.md"** → "the main repositories", which is
  what is true.
- **PostgreSQL/Prisma removed from the CV skills line** — it exists in one 2026
  Victor backend, and listing it beside Firebase implied equal depth.
- **The documented PDF build command was broken.** Given a bare filename, Chrome
  treats it as a hostname, fails to resolve it and exits without writing — so a
  "successful" build silently kept the old PDF. Fixed in `documents/README.md`
  with absolute paths, a `file:///` URL and a page-count check afterwards.

### The one instruction I did not follow

**The 14 classes / 39 teachers figure.** You asked for it on the website. The
source does not support it and I think using it would cost you:

- `scripts/diagnostics/fixtures/local/sais-2026-27.json` is **named "SAIS
  Dansoman 2026/27"** and holds **20 classes, 63 teachers**, 20 subjects, 24
  rooms and 4 divisions. The 615-period run documented in `CHANGELOG.md` v1.0.0
  and `docs/delivery-readiness.md:44-58` is that fixture.
- The 14-class fixture is `dansoman.json`, which holds **55 teachers, not 39**,
  and **zero divisions** — and `delivery-readiness.md:141` records it as the
  *wrong* fixture for exactly that reason, since the delivery school runs four.
- So "14 classes and 39 teachers" matches no run in the repository, and the
  smaller fixture is the one the docs call unrepresentative.

The site keeps **20 classes · 63 teachers · 615 periods**, cited to the changelog
and the readiness doc. If you did perform a separate 39-teacher run, write a
dated line into `docs/delivery-readiness.md` saying so and I will cite that
instead — the figure needs a file behind it, same as every other number here.

### Still open, and yours to decide

1. **Confirm the LinkedIn URL**, then fix the GitHub profile README to match.
2. **The services section** (`documents/pitches.md` §1.3) is written but not
   built on the site. It is the one piece of copy that turns a reader into a
   client rather than an employer.
3. **Victor's repository goes public in January 2027.** It is the only project
   with no customer data in it, and the only one a stranger can read.

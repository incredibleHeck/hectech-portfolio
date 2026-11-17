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

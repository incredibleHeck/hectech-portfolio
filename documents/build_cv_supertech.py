"""Tailored CV for the SuperTech mid-level fullstack role.

Built from cv.html so the facts stay identical — only emphasis changes:
  * profile rewritten around the requirements -> build -> train cycle the JD asks for
  * skills reordered to follow their own list, and honest about what is absent
  * projects reordered so the customer-facing, Postgres/Next.js work leads
  * referees stay redacted; they go to a named employer on request
"""
import io, os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
src = io.open(os.path.join(HERE, "cv.html"), encoding="utf-8").read()

# ── 1. public referee block (this goes to an employer, not the open web) ──
PRIVATE = '''  <div class="two">
    <div class="note"><b>Dr. Ruhiya Abubakar</b> — Dean, Faculty of Engineering, Ghana Communication Technology University · rabubakar@gctu.edu.gh · +233 20 832 4097 <i>(academic referee)</i></div>
    <div class="note"><b>Mrs. Theodora Hammond</b> — Administrator, St. Adelaide International Schools · +233 24 482 6879 <i>(current employer)</i></div>
  </div>
'''
PUBLIC = '''  <div class="note"><b>References available on request</b> — an academic referee (Dean, Faculty of Engineering, Ghana Communication Technology University) and my current employer at St. Adelaide International Schools.</div>
'''
assert PRIVATE in src
src = src.replace(PRIVATE, PUBLIC, 1)

# ── 2. profile aimed at the JD's actual duties ────────────────────────────
old_profile = re.search(r'<p class="profile">(.*?)</p>', src, re.S).group(0)
new_profile = '''<p class="profile">
    Software engineer who has taken production systems end to end for real users — gathering requirements,
    building, testing, integrating, documenting and then <b>training the people who use them daily</b>.
    I teach the Cambridge Computing, Digital Literacy and Mathematics curricula at St. Adelaide
    International Schools and build the software that school runs on: a report-card and grading portal, a
    timetable generator, and a lesson-plan compliance system, all live and in daily administrative use.
    My working stack is <b>TypeScript, JavaScript, Python, React and Next.js over PostgreSQL and Firebase</b>,
    with Vitest and Playwright for automated testing and GitHub Actions for CI. I also work lower down the
    stack in Rust and C++ — a constraint solver and a game engine with a neural evaluation — which is where
    the habits behind the rest of this come from.
  </p>'''
src = src.replace(old_profile, new_profile, 1)

# ── 3. skills, reordered to mirror their requirement list ─────────────────
skills_block = re.search(r'(<div class="skill">.*?</div>)\s*(?=<div class="sec">)', src, re.S).group(1)
start = src.index('<div class="skill">')
end = src.index('<div class="sec">', start)
new_skills = '''<div class="skill"><b>Languages:</b> TypeScript, JavaScript (ES6+ and vanilla), Python, SQL, Rust, C++</div>
  <div class="skill"><b>Frontend:</b> React 18/19, <b>Next.js</b>, Vite, Tailwind CSS, HTML5/CSS3, Progressive Web Apps, Three.js</div>
  <div class="skill"><b>Backend &amp; data:</b> Node.js, <b>PostgreSQL</b> (Prisma, Supabase), SQLite, Firebase (Firestore, Auth, Cloud Functions), REST APIs</div>
  <div class="skill"><b>Testing &amp; QA:</b> <b>Vitest</b> (Jest-compatible API), <b>Playwright</b> end-to-end, React Testing Library, test-case authoring, code review</div>
  <div class="skill"><b>Engineering practice:</b> Git/GitHub, <b>GitHub Actions CI/CD</b>, Docker Compose, Linux shell, SOLID principles, secure coding, applied cryptography (Ed25519, AES-256-GCM), technical documentation and user manuals</div>
  <div class="skill"><b>Architecture:</b> Offline-first design, role-based access control and server-side authorisation rules, transactional integrity under concurrency, constraint satisfaction (MRV, backtracking)</div>
  <div class="skill"><b>AI tooling:</b> Google Gemini multimodal pipelines, LLM API integration, PyTorch (NNUE training, int16 quantisation)</div>
  '''
src = src[:start] + new_skills + src[end:]

# ── 4. reorder projects: user-facing delivery first ───────────────────────
proj_start = src.index('<div class="e">', src.index('Selected Engineering Projects'))
proj_end = src.index('<div class="sec">', proj_start)
region = src[proj_start:proj_end]
blocks = re.findall(r'<div class="e">.*?(?=<div class="e">|$)', region, re.S)


def title_of(b):
    m = re.search(r'<h3>(.*?)</h3>', b, re.S)
    return re.sub(r"<[^>]+>", "", m.group(1)) if m else ""


order = ["SAIS Portal", "Doxamix", "BaseCamp", "EduScheduler", "Victor", "Nexus", "Additional"]
ranked = sorted(blocks, key=lambda b: next(
    (i for i, k in enumerate(order) if k.lower() in title_of(b).lower()), 99))
src = src[:proj_start] + "".join(ranked) + src[proj_end:]

src = src.replace("<title>Hector Nii Armaakwei Aryiku — CV</title>",
                  "<title>Hector Nii Armaakwei Aryiku — CV</title>", 1)

out_html = os.path.join(HERE, "_cv_supertech.html")
io.open(out_html, "w", encoding="utf-8").write(src)
subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
                f"--print-to-pdf={os.path.join(HERE, 'CV_Hector_Aryiku_SuperTech.pdf')}",
                "--virtual-time-budget=15000", "file:///" + out_html.replace("\\", "/")],
               capture_output=True)

print("project order:")
for b in ranked:
    print("   ", title_of(b)[:60])

from pypdf import PdfReader
r = PdfReader(os.path.join(HERE, "CV_Hector_Aryiku_SuperTech.pdf"))
t = "\n".join(p.extract_text() or "" for p in r.pages)
print("\npages:", len(r.pages))
print("claims Java:", "Java" in t and "JavaScript" not in t.replace("Java", "", t.count("JavaScript")))
for k in ("Next.js", "PostgreSQL", "Playwright", "GitHub Actions", "training", "Abubakar"):
    print(f"  {k:<16} {'yes' if k in t else 'NO'}")

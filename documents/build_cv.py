"""Build both CV variants from one source.

  public  — "References available on request". Goes on the website and to
            job portals. Contains no third-party contact details.
  full    — names, emails and phone numbers. Email this to a named employer
            when they ask; never publish it.

Produces a .pdf and a .docx of each, so the four files can never drift.
"""
import io, os, re, html, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# cv.html is the PUBLIC CV: it says references are available on request and
# carries no third-party contact details, so it is safe in a public repository.
# The referees' details live only in referees.local.html, which is gitignored;
# the full variant is built only when that file is present on this machine.
# Which CV to build: `python build_cv.py` builds cv.html (the engineering CV the
# website serves); `python build_cv.py cv_teaching.html` builds the teaching CV.
SOURCES = {"cv.html": "CV_Hector_Aryiku", "cv_teaching.html": "CV_Hector_Aryiku_Teaching"}
SRC = sys.argv[1] if len(sys.argv) > 1 else "cv.html"
assert SRC in SOURCES, f"unknown CV source {SRC!r}; expected one of {sorted(SOURCES)}"
BASE = SOURCES[SRC]
src = io.open(os.path.join(HERE, SRC), encoding="utf-8").read()
REF_BLOCK = re.compile(r"<!-- REFERENCES -->.*?<!-- /REFERENCES -->", re.S)
assert REF_BLOCK.search(src), f"REFERENCES markers not found in {SRC}"

REFEREES = os.path.join(HERE, "referees.local.html")
private = io.open(REFEREES, encoding="utf-8").read() if os.path.exists(REFEREES) else None

variants = {BASE: src}
if private:
    variants[BASE + "_with-references"] = REF_BLOCK.sub(lambda _m: private, src, count=1)
else:
    print("referees.local.html not found - building the public CV only")

# ── render each to PDF ────────────────────────────────────────────────
for name, content in variants.items():
    tmp = os.path.join(HERE, f"_{name}.html")
    io.open(tmp, "w", encoding="utf-8").write(content)
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer",
                    f"--print-to-pdf={os.path.join(HERE, name + '.pdf')}",
                    "--virtual-time-budget=15000",
                    "file:///" + tmp.replace("\\", "/")],
                   capture_output=True)

# ── and to .docx, from the same HTML ──────────────────────────────────
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

INK  = RGBColor(0x1A, 0x17, 0x14)
INK2 = RGBColor(0x3D, 0x37, 0x2F)
GOLD = RGBColor(0x81, 0x66, 0x2C)
GREY = RGBColor(0x63, 0x5B, 0x50)

PATTERN = (
    r'<h1>(.*?)</h1>'
    r'|<div class="role">(.*?)</div>'
    r'|<div class="meta">(.*?)</div>\s*</header>'
    r'|<div class="sec"><h2>(.*?)</h2>'
    r'|<p class="profile">(.*?)</p>'
    r'|<div class="skill">(.*?)</div>'
    r'|<div class="e-h"><h3>(.*?)</h3>(?:<span class="when">(.*?)</span>)?</div>'
    r'|<div class="e-m">(.*?)</div>'
    r'|<li>(.*?)</li>'
    r'|<div class="note"[^>]*>(.*?)</div>'
)


def runs(t):
    t = re.sub(r"<i>(.*?)</i>", r"\1", t, flags=re.S)
    parts, pos = [], 0
    for m in re.finditer(r"<b>(.*?)</b>", t, flags=re.S):
        if t[pos:m.start()]:
            parts.append((t[pos:m.start()], False))
        parts.append((m.group(1), True))
        pos = m.end()
    if t[pos:]:
        parts.append((t[pos:], False))
    out = []
    for txt, b in parts:
        txt = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", txt)))
        if txt:
            out.append((txt, b))
    return out or [("", False)]


def flat(t):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", t))).strip()


def build_docx(content, out_path):
    body = content.split("</style>", 1)[1]
    body = re.sub(r'<div class="no-print".*?</div>', "", body, flags=re.S)
    body = re.sub(r"<footer.*?</footer>", "", body, flags=re.S)

    doc = Document()
    for s in doc.sections:
        s.top_margin = s.bottom_margin = Inches(0.5)
        s.left_margin = s.right_margin = Inches(0.62)
    st = doc.styles["Normal"]
    st.font.name = "Calibri"; st.font.size = Pt(11); st.font.color.rgb = INK2
    st.paragraph_format.space_after = Pt(0); st.paragraph_format.space_before = Pt(0)
    st.paragraph_format.line_spacing = 1.08

    def para(before=0, after=0, indent=0.0, hang=0.0):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(before)
        p.paragraph_format.space_after = Pt(after)
        if indent: p.paragraph_format.left_indent = Inches(indent)
        if hang:   p.paragraph_format.first_line_indent = Inches(-hang)
        return p

    def emit(p, text, size=11, bold=False, italic=False, color=INK2, caps=False, spacing=None):
        r = p.add_run(text); r.font.size = Pt(size); r.bold = bold; r.italic = italic
        r.font.color.rgb = color; r.font.name = "Calibri"
        if caps: r.font.all_caps = True
        if spacing is not None:
            rPr = r._element.get_or_add_rPr()
            el = OxmlElement("w:spacing"); el.set(qn("w:val"), str(int(spacing*20))); rPr.append(el)

    def rule(p):
        pPr = p._p.get_or_add_pPr(); pbdr = OxmlElement("w:pBdr")
        b = OxmlElement("w:bottom")
        b.set(qn("w:val"), "single"); b.set(qn("w:sz"), "6")
        b.set(qn("w:space"), "2"); b.set(qn("w:color"), "81662C")
        pbdr.append(b); pPr.append(pbdr)

    first = True
    for m in re.finditer(PATTERN, body, flags=re.S):
        g = m.groups()
        if g[0] is not None:
            p = para(after=1); emit(p, flat(g[0]), size=20, bold=True, color=INK, spacing=0.5)
        elif g[1] is not None:
            p = para(after=4); emit(p, flat(g[1]), size=10, bold=True, color=GOLD)
        elif g[2] is not None:
            txt = re.sub(r"</div>\s*<div>", " | ", g[2])
            txt = re.sub(r"<br\s*/?>", " | ", txt)
            p = para(after=0); emit(p, flat(txt), size=9.5)
        elif g[3] is not None:
            p = para(before=0 if first else 9, after=3.5)
            emit(p, flat(g[3]), size=9.5, bold=True, color=GOLD, caps=True, spacing=1.2)
            rule(p); first = False
        elif g[4] is not None:
            p = para(after=0)
            for t, b in runs(g[4]): emit(p, t, size=11, bold=b, color=INK if b else INK2)
        elif g[5] is not None:
            p = para(after=1.8)
            for t, b in runs(g[5]): emit(p, t, size=11, bold=b, color=INK if b else INK2)
        elif g[6] is not None:
            p = para(before=6, after=0); emit(p, flat(g[6]), size=12, bold=True, color=INK)
            if g[7]: emit(p, "   " + flat(g[7]), size=9, color=GREY)
        elif g[8] is not None:
            p = para(after=2.4)
            for t, b in runs(g[8]): emit(p, t, size=10, italic=not b, bold=b, color=GOLD if b else GREY)
        elif g[9] is not None:
            p = para(indent=0.17, hang=0.17, after=1.8)
            emit(p, "\u25aa  ", size=9, color=GOLD)
            for t, b in runs(g[9]): emit(p, t, size=11, bold=b, color=INK if b else INK2)
        elif g[10] is not None:
            p = para(before=2, after=1.8)
            for t, b in runs(g[10]): emit(p, t, size=10.5, bold=b, color=INK if b else INK2)

    doc.save(out_path)


for name, content in variants.items():
    build_docx(content, os.path.join(HERE, name + ".docx"))
    os.remove(os.path.join(HERE, f"_{name}.html"))

# ── verify the split actually held ────────────────────────────────────
# The strings to look for come from the private file itself — names, emails
# and phone numbers — so nothing personal has to be written into this script.
if private:
    LEAKS = set(re.findall(r"<b>(.*?)</b>", private))
    LEAKS |= set(re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", private))
    LEAKS |= set(re.findall(r"\+\d[\d ]{7,}\d", private))
else:
    LEAKS = set()
print(f"{'file':<42} {'pages':>5}   referee-detail hits")
for name in variants:
    pdf = open(os.path.join(HERE, name + ".pdf"), "rb").read()
    pages = pdf.count(b"/Type /Page") - pdf.count(b"/Type /Pages")
    doc = Document(os.path.join(HERE, name + ".docx"))
    text = "\n".join(p.text for p in doc.paragraphs)
    hits = sum(text.count(x) for x in LEAKS)
    print(f"{name + '.pdf/.docx':<42} {pages:>5}   {hits}")
    if name == BASE:
        assert hits == 0, "the public CV contains referee details"

# The website serves assets/CV_Hector_Aryiku.pdf. Copy the public build there so
# a rebuilt CV can't be left behind when the site is deployed.
if SRC == "cv.html":
    import shutil
    shutil.copyfile(os.path.join(HERE, "CV_Hector_Aryiku.pdf"),
                    os.path.join(HERE, "..", "assets", "CV_Hector_Aryiku.pdf"))
    print("copied the public CV to assets/ - deploy to publish it")

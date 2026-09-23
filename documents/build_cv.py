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

PRIVATE_BLOCK = '''  <div class="two">
    <div class="note"><b>Dr. Ruhiya Abubakar</b> — Dean, Faculty of Engineering, Ghana Communication Technology University · rabubakar@gctu.edu.gh · +233 20 832 4097 <i>(academic referee)</i></div>
    <div class="note"><b>Mrs. Theodora Hammond</b> — Administrator, St. Adelaide International Schools · +233 24 482 6879 <i>(current employer)</i></div>
  </div>
'''

PUBLIC_BLOCK = '''  <div class="note"><b>References available on request</b> — an academic referee (Dean, Faculty of Engineering, Ghana Communication Technology University) and my current employer at St. Adelaide International Schools. Contact details supplied directly to a prospective employer.</div>
'''

src = io.open(os.path.join(HERE, "cv.html"), encoding="utf-8").read()
assert PRIVATE_BLOCK in src, "referee block not found — did cv.html change?"

variants = {
    "CV_Hector_Aryiku":                 src.replace(PRIVATE_BLOCK, PUBLIC_BLOCK),
    "CV_Hector_Aryiku_with-references": src,
}

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
    st.font.name = "Calibri"; st.font.size = Pt(9.8); st.font.color.rgb = INK2
    st.paragraph_format.space_after = Pt(0); st.paragraph_format.space_before = Pt(0)
    st.paragraph_format.line_spacing = 1.08

    def para(before=0, after=0, indent=0.0, hang=0.0):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(before)
        p.paragraph_format.space_after = Pt(after)
        if indent: p.paragraph_format.left_indent = Inches(indent)
        if hang:   p.paragraph_format.first_line_indent = Inches(-hang)
        return p

    def emit(p, text, size=9.8, bold=False, italic=False, color=INK2, caps=False, spacing=None):
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
            p = para(after=1); emit(p, flat(g[0]), size=19, bold=True, color=INK, spacing=0.5)
        elif g[1] is not None:
            p = para(after=4); emit(p, flat(g[1]), size=10, bold=True, color=GOLD)
        elif g[2] is not None:
            txt = re.sub(r"</div>\s*<div>", " | ", g[2])
            txt = re.sub(r"<br\s*/?>", " | ", txt)
            p = para(after=0); emit(p, flat(txt).replace("in/ ", "in/"), size=9.4)
        elif g[3] is not None:
            p = para(before=0 if first else 9, after=3.5)
            emit(p, flat(g[3]), size=9.2, bold=True, color=GOLD, caps=True, spacing=1.2)
            rule(p); first = False
        elif g[4] is not None:
            p = para(after=0)
            for t, b in runs(g[4]): emit(p, t, size=9.7, bold=b, color=INK if b else INK2)
        elif g[5] is not None:
            p = para(after=1.8)
            for t, b in runs(g[5]): emit(p, t, size=9.7, bold=b, color=INK if b else INK2)
        elif g[6] is not None:
            p = para(before=6, after=0); emit(p, flat(g[6]), size=10.4, bold=True, color=INK)
            if g[7]: emit(p, "   " + flat(g[7]), size=9.3, color=GREY)
        elif g[8] is not None:
            p = para(after=2.4)
            for t, b in runs(g[8]): emit(p, t, size=9.3, italic=not b, bold=b, color=GOLD if b else GREY)
        elif g[9] is not None:
            p = para(indent=0.17, hang=0.17, after=1.8)
            emit(p, "\u25aa  ", size=8.6, color=GOLD)
            for t, b in runs(g[9]): emit(p, t, size=9.6, bold=b, color=INK if b else INK2)
        elif g[10] is not None:
            p = para(before=2, after=1.8)
            for t, b in runs(g[10]): emit(p, t, size=9.5, bold=b, color=INK if b else INK2)

    doc.save(out_path)


for name, content in variants.items():
    build_docx(content, os.path.join(HERE, name + ".docx"))
    os.remove(os.path.join(HERE, f"_{name}.html"))

# ── verify the split actually held ────────────────────────────────────
LEAKS = ("rabubakar@gctu", "+233 20 832 4097", "+233 24 482 6879", "Abubakar", "Hammond")
print(f"{'file':<42} {'pages':>5}   referee-detail hits")
for name in variants:
    pdf = open(os.path.join(HERE, name + ".pdf"), "rb").read()
    pages = pdf.count(b"/Type /Page") - pdf.count(b"/Type /Pages")
    doc = Document(os.path.join(HERE, name + ".docx"))
    text = "\n".join(p.text for p in doc.paragraphs)
    hits = sum(text.count(x) for x in LEAKS)
    print(f"{name + '.pdf/.docx':<42} {pages:>5}   {hits}")

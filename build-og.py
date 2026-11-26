#!/usr/bin/env python3
"""Render this demo site's link-preview card, og.png (1200x630), with headless Chrome, and stamp it (register M-0026).

    python3 build-og.py

/build Default 7's fourth piece (roadmap A477, 2026-11-26), in the shape of demo.333.eco's build-og.py: the B-Emblem from the
brand layer (drawn by its own box, never a transform), this demo's accent, the host named at the foot. Chrome needs the
network for the fonts; offline it renders the fallback stack and looks wrong without erroring — look at the image first.
"""
import io, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
MA = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
STAMP = os.path.join(MA, ".claude", "skills", "media", "scripts", "stamp.py")
EMBLEM = io.open(os.path.join(MA, "333", "333.eco", "brand.333.eco", "emblem", "emblem.path.txt"), encoding="utf-8").read().strip()
BOX = "3.6824 2.2349 18.0828 18.0851"
ACCENT = "#c084fc"   # this demo's purple (#9333ea), lifted for a dark ground

CARD = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,500;6..72,600&family=IBM+Plex+Sans:wght@400;500&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
  *{box-sizing:border-box;margin:0}
  html,body{width:1200px;height:630px;overflow:hidden}
  body{background:#0f0e14;color:#f3f1f7;font-family:"IBM Plex Sans",system-ui,sans-serif;display:flex;flex-direction:column;
       justify-content:center;padding:0 92px 40px;position:relative;-webkit-font-smoothing:antialiased}
  body::before{content:"";position:absolute;left:-160px;bottom:-260px;width:760px;height:760px;border-radius:50%%;
       background:radial-gradient(circle,rgba(192,132,252,.20),transparent 62%%)}
  .inner{position:relative}
  .em{width:92px;height:92px;display:block;margin-bottom:34px}
  h1{font-family:"Newsreader",Georgia,serif;font-weight:600;font-size:86px;letter-spacing:-.022em;line-height:1.03;margin-bottom:24px}
  p{font-size:30px;line-height:1.5;color:#a29eab;max-width:32ch}
  .foot{position:absolute;left:92px;bottom:56px;display:flex;align-items:center;gap:14px;
        font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:22px;color:%(accent)s}
  .rule{width:52px;height:2px;background:%(accent)s;opacity:.5}
</style></head><body><div class="inner">
<svg class="em" viewBox="%(box)s" aria-hidden="true"><path fill="%(accent)s" d="%(emblem)s"/></svg>
<h1>Working pages</h1>
<p>For thonly.org and book.thonly.org: the native readers' Khmer reviews, and the book's drawings.</p>
</div><div class="foot"><span class="rule"></span>demo.thonly.org</div></body></html>""" % dict(accent=ACCENT, box=BOX, emblem=EMBLEM)

if not os.path.exists(CHROME):
    sys.exit("Chrome not found at %s" % CHROME)
out = os.path.join(HERE, "og.png")
with tempfile.TemporaryDirectory() as tmp:
    src = os.path.join(tmp, "card.html")
    io.open(src, "w", encoding="utf-8").write(CARD)
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--window-size=1200,630", "--virtual-time-budget=4000", "--screenshot=" + out, "file://" + src],
                   check=True, capture_output=True)
subprocess.run(["python3", STAMP, out, "--source", "drawn", "--rights", "reserved", "--register", "M-0026",
                "--disclosure", "https://demo.thonly.org/", "--note", "the demo site's link-preview card, drawn by code"],
               check=True, capture_output=True)
print("og.png %d bytes, stamped M-0026" % os.path.getsize(out))

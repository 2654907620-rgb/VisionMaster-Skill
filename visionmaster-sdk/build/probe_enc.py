# -*- coding: utf-8 -*-
import os, re, json
BASE = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\net"
samples = ["usergroup1.html", "index.html", "modules.html", "_xE7_xAE_x97_xE6_xB3_x95_xE7_x8A_xB6_xE6_x80_x81_xE7_xA0_x81.html"]
out = []
for f in samples:
    p = os.path.join(BASE, f)
    if not os.path.exists(p):
        out.append("MISS " + f); continue
    raw = open(p, "rb").read()
    m = re.search(rb"charset=[\"']?([A-Za-z0-9_\-]+)", raw[:3000], re.I)
    out.append("== %s size=%d meta=%s" % (f, len(raw), m.group(1).decode() if m else "NONE"))
    for enc in ("utf-8", "gb18030", "gbk"):
        try:
            t = raw.decode(enc)
            # count CJK
            cjk = len(re.findall(r"[\u4e00-\u9fff]", t))
            out.append("   %-8s ok  cjk=%d  sample=%s" % (enc, cjk, t[:0]))
            if cjk:
                # find a chinese snippet
                snip = re.findall(r"[\u4e00-\u9fff][\u4e00-\u9fff\uff0c\u3002]{3,}", t)[:3]
                out.append("      snip: " + " | ".join(snip))
        except Exception as e:
            out.append("   %-8s FAIL %s" % (enc, e))
with open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_enc_probe.txt", "w", encoding="utf-8") as fh:
    fh.write("\n".join(out))
print("ok")

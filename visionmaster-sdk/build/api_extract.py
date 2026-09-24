# -*- coding: utf-8 -*-
"""Extract a compact, structured .NET API reference from the decompiled Doxygen HTML.

Output: one markdown file per 接口函数 大类, listing 模块 > 类 > 成员(签名 + 简述).
"""
import os, re, json
from bs4 import BeautifulSoup

BASE = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\net"
OUT = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\api_ref"
os.makedirs(OUT, exist_ok=True)

with open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\md_net\_index.json", "r", encoding="utf-8") as fh:
    IDX = json.load(fh)["index"]
PATHOF = {it["src"]: (it.get("path") or []) for it in IDX}

def txt(el):
    if el is None:
        return ""
    s = el.get_text(" ", strip=True)
    s = re.sub(r"\s+", " ", s)
    return s.replace("更多...", "").strip()

def parse_class(fname):
    p = os.path.join(BASE, fname)
    raw = open(p, "rb").read().decode("gb18030", errors="ignore")
    soup = BeautifulSoup(raw, "lxml")
    name = ""
    ht = soup.find("div", class_="headertitle")
    if ht:
        name = txt(ht.find(["h1", "h2", "div", "span"]))
    if not name:
        t = soup.find("title")
        name = txt(t)
    # brief
    brief = ""
    bd = soup.find("div", class_="textblock")
    if bd:
        brief = txt(bd)
    # inheritance
    inh = ""
    ti = soup.find("p", class_="inherits") or soup.find("p", class_="inherited")
    if ti:
        inh = txt(ti)
    else:
        for p_ in soup.find_all("p"):
            if "继承自" in p_.get_text():
                inh = txt(p_)
                break
    # member decl tables
    members = []   # (section, type, name, brief)
    for tbl in soup.find_all("table", class_="memberdecls"):
        rows = tbl.find_all("tr")
        section = ""
        for tr in rows:
            cl = " ".join(tr.get("class") or [])
            if "heading" in cl:
                section = txt(tr)
                continue
            left = tr.find("td", class_="memItemLeft")
            right = tr.find("td", class_="memItemRight")
            desc = tr.find("td", class_="mdescRight")
            if right is None:
                # brief-only row -> attach to previous member
                if desc is not None and members:
                    d = txt(desc)
                    if d:
                        s, t, n, old = members[-1]
                        members[-1] = (s, t, n, (old + " " + d).strip())
                continue
            nm = txt(right)
            ty = txt(left)
            d = txt(desc)
            if not nm:
                continue
            members.append((section, ty, nm, d))
    return {"name": name, "brief": brief, "inherits": inh, "members": members}

def build():
    # group by L1/L2 from TOC path
    buckets = {}
    for it in IDX:
        src = it["src"]
        if not src.lower().startswith("class_"):
            continue
        if src.lower().endswith("-members.html"):
            continue   # doxygen member-index pages carry no descriptions
        p = PATHOF.get(src) or []
        if len(p) >= 3 and p[0] == "接口函数":
            key = p[1]
            mod = p[2]
        else:
            key = "其他/公共"
            mod = p[-1] if p else src
        buckets.setdefault(key, {}).setdefault(mod, []).append(it)

    allindex = []
    for big in sorted(buckets.keys()):
        lines = ["# VM .NET SDK 接口参考 — %s\n" % big,
                 "> 由官方 SDK 开发指南 V4.4.3（.NET）自动提取。签名以官方文档为准。\n"]
        for mod in sorted(buckets[big].keys()):
            lines.append("\n## %s\n" % mod)
            for it in buckets[big][mod]:
                try:
                    c = parse_class(it["src"])
                except Exception as e:
                    lines.append("- ⚠️ 解析失败 %s: %r" % (it["src"], e))
                    continue
                if c["brief"]:
                    lines.append("**%s** — %s" % (c["name"] or it["src"], c["brief"]))
                else:
                    lines.append("**%s**" % (c["name"] or it["src"]))
                if c["inherits"]:
                    lines.append("")
                    lines.append("_%s_" % c["inherits"])
                if c["members"]:
                    lines.append("")
                    lines.append("| 成员 | 签名 | 说明 |")
                    lines.append("| --- | --- | --- |")
                    seen = set()
                    for section, ty, nm, d in c["members"]:
                        k = (nm, ty)
                        if k in seen:
                            continue
                        seen.add(k)
                        sec = ("*%s* " % section) if section else ""
                        lines.append("| %s%s | `%s` | %s |" % (sec, nm.replace("|", "\\|"), (ty or "").replace("|", "\\|"), d.replace("|", "\\|")))
                lines.append("")
                allindex.append({"big": big, "module": mod, "class": c["name"] or it["src"], "src": it["src"],
                                 "brief": c["brief"], "nmembers": len(c["members"])})
        safe = re.sub(r'[\\/:*?"<>|]', "_", big)
        with open(os.path.join(OUT, safe + ".md"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))
    with open(os.path.join(OUT, "_api_index.json"), "w", encoding="utf-8") as fh:
        json.dump(allindex, fh, ensure_ascii=False, indent=1)
    print("classes", len(allindex), "buckets", len(buckets))

if __name__ == "__main__":
    build()

# -*- coding: utf-8 -*-
"""Convert decompiled Doxygen CHM (VisionMaster SDK .NET) into Markdown KB."""
import os, re, json, html
from bs4 import BeautifulSoup
import markdownify

BASE = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\net"
OUT  = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\md_net"
os.makedirs(OUT, exist_ok=True)

DROP_CLASSES = {
    "header", "footer", "navpath", "nav-sync", "tabs", "tabs2", "tabs3",
    "tablist", "tabsearch", "sm-dox", "ingroups", "ingroup", "directories",
    "directory", "title", "summary", "memtitle", "navelem", "navigation",
    "mlabel", "mlabels", "mlabels-left", "mlabels-right", "fieldtable",
}
KEEP_CLASSES = {"contents", "textblock", "headertitle"}

def clean(soup):
    for t in soup(["script", "style", "noscript", "iframe"]):
        t.decompose()
    # prefer main content div
    node = soup.find("div", class_="contents") or soup.find("div", id="doc-content")
    if node is None:
        node = soup.body or soup
    # remove leftover nav blocks inside
    for cls in ("navpath", "tabs", "tabs2", "tabs3", "nav-sync", "sm-dox", "header", "footer"):
        for t in node.find_all(class_=cls):
            t.decompose()
    for t in node.find_all("div", class_=("summary", "headertitle")):
        pass
    return node

def html_to_md(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as fh:
        raw = fh.read()
    soup = BeautifulSoup(raw, "lxml")
    title = ""
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
    node = clean(soup)
    md = markdownify.markdownify(str(node), heading_style="ATX", bullets="-", strip=["a"])
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = re.sub(r"[ \t]+\n", "\n", md)
    return title, md.strip()

def main():
    htm = [f for f in os.listdir(BASE) if f.lower().endswith((".html", ".htm"))]
    htm.sort()
    cat = {"guide": [], "api_class": [], "api_group": [], "api_file": [], "api_ns": [], "other": []}
    for f in htm:
        lf = f.lower()
        if lf.startswith("class_"):
            cat["api_class"].append(f)
        elif lf.startswith("group___") or lf.startswith("group_"):
            cat["api_group"].append(f)
        elif lf.startswith("namespace") or lf.startswith("struct") or lf.startswith("interface"):
            cat["api_ns"].append(f)
        elif lf.startswith("_"):
            cat["guide"].append(f)
        elif re.match(r"^[a-z_]+\.html$", lf) and not lf.startswith("class_"):
            cat["other"].append(f)
        else:
            cat["other"].append(f)
    stats = {k: len(v) for k, v in cat.items()}
    total_chars = 0
    index = []
    for f in htm:
        src = os.path.join(BASE, f)
        try:
            title, md = html_to_md(src)
        except Exception as e:
            title, md = f, "!!ERR " + str(e)
        total_chars += len(md)
        dst = os.path.join(OUT, f[:-5] + ".md")
        with open(dst, "w", encoding="utf-8") as fh:
            fh.write("# " + (title or f) + "\n\n" + md + "\n")
        index.append({"src": f, "title": title, "chars": len(md)})
    with open(os.path.join(OUT, "_index.json"), "w", encoding="utf-8") as fh:
        json.dump({"stats": stats, "total_chars": total_chars, "index": index}, fh, ensure_ascii=False, indent=1)
    print(json.dumps(stats, ensure_ascii=False), "total_chars=", total_chars)

if __name__ == "__main__":
    main()

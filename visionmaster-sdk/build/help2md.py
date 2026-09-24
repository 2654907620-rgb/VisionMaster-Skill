# -*- coding: utf-8 -*-
"""VM 应用帮助文档（Oxygen WebHelp, CH）→ Markdown 知识库。
TOC 内嵌在 CH/index.html 的 ul.menu_ul 中，条目为 a.topicref[data-href]。
"""
import os, re, json
from bs4 import BeautifulSoup
import markdownify

BASE = r"D:\VisionMaster4.4.0\Applications\Help\CH"
OUT = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\help_md"
os.makedirs(OUT, exist_ok=True)

# ---------- 1. TOC ----------
def parse_toc():
    raw = open(os.path.join(BASE, "index.html"), "r", encoding="utf-8", errors="ignore").read()
    soup = BeautifulSoup(raw, "lxml")
    root = soup.find("ul", class_=lambda c: c and "menu_ul" in c)
    crumbs = {}
    order = []
    entries = []

    def walk(ul, depth, trail):
        for li in ul.find_all("li", recursive=False):
            a = li.find("a", recursive=False)
            name, href = "", ""
            if a is not None:
                name = a.get_text(" ", strip=True)
                href = (a.get("data-href") or "").strip()
            sub = li.find("ul", recursive=False)
            mytrail = trail + [name] if name else list(trail)
            if name:
                entries.append({"depth": depth, "name": name, "href": href, "trail": list(mytrail)})
                if href:
                    crumbs.setdefault(href, list(mytrail))
                    if href not in order:
                        order.append(href)
            if sub is not None:
                walk(sub, depth + 1, mytrail)

    walk(root, 0, [])
    return entries, crumbs, order

# ---------- 2. HTML -> MD ----------
DROP = ("nav", "header", "footer", "breadcrumbs", "wt_breadcrumbs", "wh_header",
        "wh_footer", "tabnav", "search", "related-links", "linklist", "shortdesc_toolbar",
        "wt_topic_content_tools", "topicToolbar", "wh_tools")

def clean(soup):
    for t in soup(["script", "style", "noscript", "iframe"]):
        t.decompose()
    body = soup.find("div", class_="body") or soup.find("div", class_="topic") or \
           soup.body or soup
    for cls in DROP:
        for t in body.find_all(class_=cls):
            t.decompose()
        for t in body.find_all(id=cls):
            t.decompose()
    # code blocks / pre
    for pre in body.find_all("pre"):
        pre.string = pre.get_text("").replace("\xa0", " ")
    return body

def convert(path):
    raw = open(path, "rb").read()
    txt = raw.decode("utf-8", errors="ignore")
    soup = BeautifulSoup(txt, "lxml")
    title = ""
    for sel in ("h1.topictitle1", "h1.topictitle2", "h1", "title"):
        el = soup.select_one(sel)
        if el:
            title = el.get_text(" ", strip=True)
            if title:
                break
    node = clean(soup)
    md = markdownify.markdownify(str(node), heading_style="ATX", strip=["a"])
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = re.sub(r"[ \t]+\n", "\n", md)
    return title, md.strip(), txt

def main():
    entries, crumbs, order = parse_toc()
    htm = [f for f in os.listdir(BASE) if f.lower().endswith(".html")]
    htm = [f for f in htm if f.upper().startswith("GUID")]
    htm.sort(key=lambda f: (order.index(f) if f in order else 10 ** 6, f))
    index = []
    total = 0
    for f in htm:
        try:
            title, md, _ = convert(os.path.join(BASE, f))
        except Exception as e:
            title, md = f, "!!ERR " + repr(e)
        total += len(md)
        crumb = crumbs.get(f, [])
        hdr = "<!-- src:%s -->\n" % f
        if crumb:
            hdr += "<!-- path:%s -->\n" % " > ".join(crumb)
        with open(os.path.join(OUT, f[:-5] + ".md"), "w", encoding="utf-8") as fh:
            fh.write(hdr + "# " + (title or f[:-5]) + "\n\n" + md + "\n")
        index.append({"src": f, "title": title, "path": crumb, "chars": len(md)})
    with open(os.path.join(OUT, "_index.json"), "w", encoding="utf-8") as fh:
        json.dump({"total_chars": total, "count": len(index), "index": index}, fh, ensure_ascii=False, indent=1)
    json.dump(entries, open(os.path.join(OUT, "_toc.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("toc", len(entries), "html", len(htm), "chars", total)

if __name__ == "__main__":
    main()

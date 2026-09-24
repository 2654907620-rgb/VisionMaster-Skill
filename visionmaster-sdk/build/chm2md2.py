# -*- coding: utf-8 -*-
"""Convert decompiled Doxygen CHM (VisionMaster SDK .NET, GB2312) into Markdown KB
   + parse index.hhc to attach breadcrumb paths to every page."""
import os, re, json
from bs4 import BeautifulSoup
import markdownify

BASE = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\net"
OUT = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\md_net"
os.makedirs(OUT, exist_ok=True)

# ---------- 1. parse TOC ----------
def parse_hhc(path):
    with open(path, "r", encoding="gb18030", errors="ignore") as fh:
        raw = fh.read()
    soup = BeautifulSoup(raw, "lxml")
    crumbs = {}          # filename -> breadcrumb list
    order = []           # filename in toc order
    stack = []           # current path of names
    depth_from_ul = 0

    body = soup.body or soup
    # walk LI elements in document order tracking UL nesting
    ul_depth = 0
    for el in body.find_all(["ul"]):
        pass

    # simpler: linear scan over raw text tokens
    pat = re.compile(r"(<UL>)|(</UL>)|(<LI><OBJECT type=\"text/sitemap\">(.*?)</OBJECT>)", re.S | re.I)
    for m in pat.finditer(raw):
        if m.group(1):
            ul_depth += 1
        elif m.group(2):
            ul_depth -= 1
        else:
            payload = m.group(4)
            nm = re.search(r'name="Name"\s+value="([^"]*)"', payload, re.I)
            lo = re.search(r'name="Local"\s+value="([^"]*)"', payload, re.I)
            if not nm or not lo:
                continue
            name = html_unescape(nm.group(1))
            local = html_unescape(lo.group(1))
            fname, _, anchor = local.partition("#")
            d = max(ul_depth - 1, 0)
            stack = stack[:d]
            stack.append(name)
            if fname not in crumbs or len(stack) < len(crumbs.get(fname, [])):
                crumbs[fname] = list(stack)
            if fname not in order:
                order.append(fname)
    return crumbs, order

def html_unescape(s):
    return (s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
             .replace("&quot;", '"').replace("&#39;", "'").replace("&nbsp;", " "))

# ---------- 2. html -> md ----------
def clean(soup):
    for t in soup(["script", "style", "noscript", "iframe"]):
        t.decompose()
    node = soup.find("div", class_="contents") or soup.find("div", id="doc-content") or soup.body or soup
    for cls in ("navpath", "tabs", "tabs2", "tabs3", "nav-sync", "sm-dox", "header", "footer", "navtab"):
        for t in node.find_all(class_=cls):
            t.decompose()
    # collapse doxygen code fragments into <pre> so markdownify emits fenced blocks.
    # doxygen wraps every token in <span>; must join with "" and split only on <div class="line">.
    for frag in node.find_all("div", class_="fragment"):
        lines = []
        for ln in frag.find_all("div", class_="line"):
            lines.append(ln.get_text(""))
        if not lines:
            lines = [frag.get_text("")]
        txt = "\n".join(lines).replace("\xa0", " ")
        pre = soup.new_tag("pre")
        pre.string = txt.strip("\n")
        frag.replace_with(pre)
    # doxygen member tables -> keep as-is (markdownify renders rows)
    return node

def convert(path):
    raw = open(path, "rb").read()
    txt = raw.decode("gb18030", errors="ignore")
    soup = BeautifulSoup(txt, "lxml")
    title = ""
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
    # prefer the headertitle h1
    ht = soup.find("div", class_="headertitle")
    if ht:
        h1 = ht.find(["h1", "h2", "div", "span"])
        if h1:
            t2 = h1.get_text(" ", strip=True)
            if t2:
                title = t2
    node = clean(soup)
    md = markdownify.markdownify(str(node), heading_style="ATX", strip=["a", "img"])
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = re.sub(r"[ \t]+\n", "\n", md)
    return title, md.strip()

def main():
    crumbs, order = parse_hhc(os.path.join(BASE, "index.hhc"))
    htm = [f for f in os.listdir(BASE) if f.lower().endswith(".html")]
    htm.sort(key=lambda f: (order.index(f) if f in order else 10**6, f))
    index = []
    total = 0
    for f in htm:
        try:
            title, md = convert(os.path.join(BASE, f))
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
    print("converted", len(index), "chars", total)

if __name__ == "__main__":
    main()

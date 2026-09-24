"""算子开发包 .NET CHM → Markdown（GB18030 解码 + Doxygen 代码块拼行 + 面包屑）"""
import os, re, sys, io, json
from bs4 import BeautifulSoup
from markdownify import markdownify as md

SRC = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\man_net"
DST = r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\md_man_net"
os.makedirs(DST, exist_ok=True)

# ---- 1. 解析 index.hhc 目录树，建立 文件 → 面包屑 ----
hhc = os.path.join(SRC, "index.hhc")
raw = open(hhc, "rb").read().decode("gb18030", errors="ignore")
pat = re.compile(r"(<UL>)|(</UL>)|(<LI><OBJECT type=\"text/sitemap\">(.*?)</OBJECT>)", re.S | re.I)
depth = 0
stack = {}
pathmap = {}   # local file -> breadcrumb string
for m in pat.finditer(raw):
    if m.group(1):
        depth += 1
    elif m.group(2):
        stack.pop(depth, None)
        depth -= 1
    else:
        payload = m.group(4)
        nm = re.search(r'name="Name"\s+value="(.*?)"', payload, re.I)
        lo = re.search(r'name="Local"\s+value="(.*?)"', payload, re.I)
        if not nm:
            continue
        name = nm.group(1).strip()
        stack[depth] = name
        if lo:
            f = lo.group(1).split("#")[0].strip()
            if f:
                crumb = " > ".join(stack[d] for d in sorted(stack) if d <= depth)
                # 只记最深的第一个（顶层章节优先）
                if f not in pathmap:
                    pathmap[f] = crumb

# ---- 2. 转换 ----
def decode(raw_bytes):
    m = re.search(rb"charset=[\"']?([A-Za-z0-9_\-]+)", raw_bytes[:3000])
    enc = m.group(1).decode().lower() if m else "gb18030"
    if enc in ("gb2312", "gbk", "gb18030"):
        enc = "gb18030"
    return raw_bytes.decode(enc, errors="ignore")

def clean(soup):
    for t in soup(["script", "style", "noscript", "iframe"]):
        t.decompose()
    node = (soup.find("div", class_="contents") or soup.find("div", id="doc-content")
            or soup.find("div", id="content") or soup.body or soup)
    for cls in ("navpath", "tabs", "tabs2", "tabs3", "nav-sync", "sm-dox",
                "header", "footer", "navtab", "title", "summary", "dynheader"):
        for t in node.find_all(class_=cls):
            t.decompose()
    return node

def join_code(node):
    """Doxygen: div.fragment > div.line > span...  必须按 line 拼，否则逐 token 断行"""
    for frag in node.find_all("div", class_="fragment"):
        lines = [ln.get_text("") for ln in frag.find_all("div", class_="line")]
        if not lines:
            lines = [frag.get_text("")]
        pre = node.new_tag("pre")
        pre.string = "\n".join(lines).replace("\xa0", " ")
        frag.replace_with(pre)

n_ok = n_err = 0
files = [f for f in os.listdir(SRC) if f.lower().endswith((".html", ".htm"))]
for f in files:
    try:
        b = open(os.path.join(SRC, f), "rb").read()
        txt = decode(b)
        soup = BeautifulSoup(txt, "lxml")
        node = clean(soup)
        join_code(node)
        body = md(str(node), heading_style="ATX", strip=["a", "img"])
        body = re.sub(r"\n{3,}", "\n\n", body).strip()
        crumb = pathmap.get(f, "")
        head = f"<!-- src:{f} -->\n"
        if crumb:
            head += f"<!-- path:{crumb} -->\n"
        open(os.path.join(DST, f.replace(".html", ".md").replace(".htm", ".md")),
             "w", encoding="utf-8").write(head + "\n" + body)
        n_ok += 1
    except Exception as e:
        n_err += 1
        if n_err <= 5:
            print(f"ERR {f}: {e}")

msg = f"算子开发包(.NET): 转换成功 {n_ok}, 失败 {n_err}, 目录项映射 {len(pathmap)}"
open(r"C:\Users\Administrator\WorkBuddy\VisionMaster\.workbuddy\vmkb\_log_man_net.txt", "w", encoding="utf-8").write(msg)
print(msg)

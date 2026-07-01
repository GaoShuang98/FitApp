import pathlib, re
p = pathlib.Path(r"C:\Users\hgs\Documents\Codex\2026-07-01\xi\work\index.html")
f = p.read_text(encoding="utf-8")
s = f.find("<script>")
e = f.find("</script>")
js = f[s:e]
# Find all remaining broken strings
broken = re.findall(r"\u0027\u003f{2,}\u0027", js)
print(f"Remaining broken: {len(broken)}")
for b in set(broken):
    cnt = js.count(b)
    idx = js.find(b)
    ctx = js[max(0,idx-15):idx+len(b)+10]
    print(f"  {b} x{cnt}: {ctx}")

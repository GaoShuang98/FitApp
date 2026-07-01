# -*- coding: utf-8 -*-
import pathlib

p = pathlib.Path(r"C:\Users\hgs\Documents\Codex\2026-07-01\xi\work\index.html")
f = p.read_text(encoding="utf-8")

# 1. Add data-theme to html tag
f = f.replace('<html lang="zh-CN">', '<html lang="zh-CN" data-theme="dark">')

# 2. Add theme CSS overrides before </style>
theme_css = """
/* Light Theme */
[data-theme=light]{--bg:#f2f2f7;--gls1:rgba(0,0,0,0.04);--gls2:rgba(0,0,0,0.06);--gls3:rgba(0,0,0,0.08);--gls-card:rgba(255,255,255,0.55);--gls-side:rgba(255,255,255,0.5);--gb:rgba(0,0,0,0.1);--gb-focus:rgba(0,0,0,0.18);--gsh:0 4px 24px rgba(0,0,0,0.08),0 1px 4px rgba(0,0,0,0.05);--gsh-lift:0 12px 40px rgba(0,0,0,0.12),0 2px 8px rgba(0,0,0,0.06);--t1:#1d1d1f;--t2:#6e6e73;--t3:#aeaeb2}
[data-theme=light] .bg-wallpaper{background:radial-gradient(ellipse 90% 70% at 15% 15%,rgba(0,0,0,0.04),transparent 55%),radial-gradient(ellipse 80% 60% at 85% 85%,rgba(0,0,0,0.03),transparent 55%),linear-gradient(175deg,#e8e8ed 0%,#f2f2f7 30%,#eaeaef 60%,#f0f0f5 100%)!important}
[data-theme=light] .bg-wallpaper::before{background:radial-gradient(circle 400px at 20% 30%,rgba(100,100,130,0.04),transparent),radial-gradient(circle 350px at 75% 65%,rgba(80,100,120,0.03),transparent)!important}
[data-theme=light] .bg-wallpaper::after{opacity:0.02!important;mix-blend-mode:multiply!important}
[data-theme=light] .fi,[data-theme=light] .fs,[data-theme=light] .ft{background:rgba(255,255,255,0.7);border-color:rgba(0,0,0,0.12);color:#1d1d1f}
[data-theme=light] .fi option,[data-theme=light] .fs option,[data-theme=light] .ft option{background:#fff;color:#1d1d1f}
[data-theme=light] .cs-trigger{background:rgba(255,255,255,0.7);border-color:rgba(0,0,0,0.12);color:#1d1d1f}
[data-theme=light] .cs-drop{background:rgba(255,255,255,0.85);border-color:rgba(0,0,0,0.12);box-shadow:0 12px 40px rgba(0,0,0,0.12),inset 0 1px 0 rgba(255,255,255,0.5)}
[data-theme=light] .cs-opt:hover{background:rgba(0,0,0,0.05)}
[data-theme=light] .cs-opt.sel{color:#30d158}
[data-theme=light] .ibtn{background:rgba(255,255,255,0.6);border-color:rgba(0,0,0,0.1);color:#6e6e73}
[data-theme=light] .ibtn.sel{background:rgba(48,209,88,0.12);border-color:#30d158;color:#30d158}
[data-theme=light] .exi{background:rgba(255,255,255,0.5)}
[data-theme=light] .exi:hover{background:rgba(255,255,255,0.75)}
[data-theme=light] .stag{background:rgba(255,255,255,0.6);border-color:rgba(0,0,0,0.1)}
[data-theme=light] .fchip{background:rgba(255,255,255,0.6);border-color:rgba(0,0,0,0.1)}
[data-theme=light] .pli{background:rgba(255,255,255,0.5)}
[data-theme=light] .ti{border-bottom-color:rgba(0,0,0,0.06)}
[data-theme=light] .side-ft{border-top-color:rgba(0,0,0,0.08)}
[data-theme=light] .card::after{background:linear-gradient(90deg,transparent,rgba(0,0,0,0.03) 30%,rgba(0,0,0,0.04) 50%,rgba(0,0,0,0.03) 70%,transparent)}
[data-theme=light] input[type=date]::-webkit-calendar-picker-indicator{filter:invert(0.3)}

/* Colorful Theme */
[data-theme=colorful]{--bg:#0a0a12;--ex:#5ef566;--exs:rgba(94,245,102,0.18);--exg:rgba(94,245,102,0.4);--cy:#ff4d6d;--cys:rgba(255,77,109,0.18);--cyg:rgba(255,77,109,0.4);--wm:#ffb340}
[data-theme=colorful] .bg-wallpaper{background:radial-gradient(ellipse 90% 70% at 15% 15%,rgba(120,80,140,0.3),transparent 55%),radial-gradient(ellipse 80% 60% at 85% 85%,rgba(60,120,180,0.25),transparent 55%),radial-gradient(ellipse 100% 50% at 50% 50%,rgba(140,100,60,0.2),transparent 70%),linear-gradient(175deg,#0d0d18 0%,#0a0a14 30%,#0c0c18 60%,#0e0e1a 100%)!important}
[data-theme=colorful] .bg-wallpaper::before{background:radial-gradient(circle 400px at 20% 30%,rgba(180,120,200,0.08),transparent),radial-gradient(circle 350px at 75% 65%,rgba(80,150,200,0.07),transparent),radial-gradient(circle 300px at 50% 20%,rgba(200,150,80,0.05),transparent),radial-gradient(circle 250px at 80% 15%,rgba(200,120,100,0.06),transparent)!important}
[data-theme=colorful] .bg-wallpaper::after{opacity:0.06!important}
[data-theme=colorful] .card::after{background:linear-gradient(90deg,transparent,rgba(255,255,255,0.08) 30%,rgba(255,255,255,0.14) 50%,rgba(255,255,255,0.08) 70%,transparent)}
[data-theme=colorful] .sv.ex{text-shadow:0 0 40px rgba(94,245,102,0.5)}
[data-theme=colorful] .sv.cy{text-shadow:0 0 40px rgba(255,77,109,0.5)}
[data-theme=colorful] .sv.wm{text-shadow:0 0 40px rgba(255,179,64,0.4)}
"""

f = f.replace("</style>", theme_css + "\n</style>")

# 3. Add theme toggle button in sidebar footer
old_sidebar_ft = '<div class="side-ft"><div class="uinfo"><div class="uav">'
new_sidebar_ft = '<div class="side-ft"><div class="uinfo"><div class="uav">\u745e</div><span>\u745e\u5178\u5065\u5eb7\u65e5\u5fd7</span></div><div class="theme-switch" style="margin-top:10px;display:flex;gap:4px"><button class="theme-btn active" data-t="dark" title="\u6697\u8272\u6a21\u5f0f">🌙</button><button class="theme-btn" data-t="light" title="\u4eae\u8272\u6a21\u5f0f">☀️</button><button class="theme-btn" data-t="colorful" title="\u5f69\u8272\u6a21\u5f0f">🌈</button></div></div>'
# Actually need the old string to match. Let me find the exact sidebar footer
idx2 = f.find('<div class="side-ft">')
end2 = f.find('</div>\n</nav>', idx2)
side_ft_section = f[idx2:end2]

# Replace the whole side-ft block
new_side_ft = """<div class="side-ft">
<div class="uinfo"><div class="uav">瑞</div><span>瑞典健康日志</span></div>
<div class="theme-row" style="margin-top:8px;display:flex;gap:4px">
<button class="tbtn active" data-t="dark" title="暗色模式">🌙</button>
<button class="tbtn" data-t="light" title="亮色模式">☀️</button>
<button class="tbtn" data-t="colorful" title="彩色模式">🌈</button>
</div>
</div>"""

idx3 = f.find('<div class="side-ft">')
end3 = f.find('</nav>', idx3)
# Find the closing </div> before </nav>
# Actually, let me find side-ft and its closing
import re
m = re.search(r'<div class="side-ft">.*?</div>\s*</nav>', f[idx3:], re.DOTALL)
if m:
    old_block = m.group()
    new_block = new_side_ft + "\n</nav>"
    f = f[:idx3] + new_block + f[idx3 + len(old_block):]
    print("Sidebar footer replaced")
else:
    print("Sidebar footer not found with regex")

# 4. Add CSS for theme buttons
tbtn_css = """
.tbtn{width:28px;height:28px;border-radius:50%;border:1px solid var(--gb);background:var(--gls1);cursor:pointer;font-size:13px;display:flex;align-items:center;justify-content:center;transition:all var(--e1);padding:0;line-height:1}
.tbtn:hover{background:var(--gls2);border-color:var(--gb-focus)}
.tbtn.active{border-color:var(--ex);box-shadow:0 0 8px var(--exs)}
"""
f = f.replace("</style>", tbtn_css + "</style>")

# 5. Add theme switching JS
theme_js = """
// Theme switcher
(function(){
const html=document.documentElement;
const saved=localStorage.getItem('luna_theme');
if(saved)html.setAttribute('data-theme',saved);
document.querySelectorAll('.tbtn').forEach(b=>{
if(b.dataset.t===saved)b.classList.add('active');
else b.classList.remove('active');
b.addEventListener('click',()=>{
const t=b.dataset.t;
html.setAttribute('data-theme',t);
localStorage.setItem('luna_theme',t);
document.querySelectorAll('.tbtn').forEach(x=>x.classList.remove('active'));
b.classList.add('active');
});
});
})();
"""

idx4 = f.rfind("</script>")
f = f[:idx4] + theme_js + "\n" + f[idx4:]

p.write_text(f, encoding="utf-8")
print("Theme system added!")

# verify
v = p.read_text(encoding="utf-8")
print("data-theme:", "data-theme" in v[0:200])
print("light theme:", "[data-theme=light]" in v)
print("colorful theme:", "[data-theme=colorful]" in v)
print("tbtn:", "tbtn" in v)

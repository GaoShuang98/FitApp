# -*- coding: utf-8 -*-
import pathlib

p = pathlib.Path(r"C:\Users\hgs\Documents\Codex\2026-07-01\xi\work\index.html")
f = p.read_text(encoding="utf-8")

# Add CSS for custom glass dropdowns before </style>
css_add = """
.cs-wrap{position:relative;user-select:none}
.cs-wrap select{position:absolute;opacity:0;pointer-events:none;width:100%;height:100%}
.cs-trigger{width:100%;padding:10px 34px 10px 13px;border:1px solid var(--gb);border-radius:var(--r1);font-size:14px;font-family:var(--f);background:var(--gls1);color:var(--t1);cursor:pointer;transition:all var(--e1);letter-spacing:-0.1px;position:relative}
.cs-trigger::after{content:'';position:absolute;right:12px;top:50%;transform:translateY(-50%);width:12px;height:12px;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%2398989d' stroke-width='2'%3E%3Cpath d='M6 9l6 6 6-6'%3E%3C/path%3E%3C/svg%3E");background-repeat:no-repeat;background-position:center;transition:transform var(--e1)}
.cs-trigger.open::after{transform:translateY(-50%) rotate(180deg)}
.cs-trigger:focus,.cs-trigger:hover{border-color:var(--ex);box-shadow:0 0 0 3px var(--exs),0 0 20px var(--exs)}
.cs-drop{position:absolute;top:calc(100% + 4px);left:0;right:0;z-index:100;background:rgba(26,26,36,0.85);backdrop-filter:blur(30px) saturate(1.6);-webkit-backdrop-filter:blur(30px) saturate(1.6);border:1px solid var(--gb);border-radius:var(--r1);box-shadow:0 12px 40px rgba(0,0,0,0.5),inset 0 1px 0 rgba(255,255,255,0.04);max-height:260px;overflow-y:auto;display:none}
.cs-drop.open{display:block;animation:cdIn 0.18s var(--e1)}
@keyframes cdIn{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:translateY(0)}}
.cs-opt{padding:9px 13px;font-size:14px;font-family:var(--f);color:var(--t1);cursor:pointer;transition:background var(--e1);letter-spacing:-0.1px}
.cs-opt:hover{background:var(--gls2)}
.cs-opt.sel{color:var(--ex);font-weight:520}
"""

f = f.replace("</style>", css_add + "</style>")

# Add JS to transform selects
js_add = """
// Custom glass dropdowns
function initCustomSelects(){
document.querySelectorAll('select.fs').forEach(sel=>{
if(sel.closest('.cs-wrap'))return;
const wrap=document.createElement('div');wrap.className='cs-wrap';
const trigger=document.createElement('div');trigger.className='cs-trigger';
const drop=document.createElement('div');drop.className='cs-drop';
const options=[];
sel.querySelectorAll('option').forEach(opt=>{
const o=document.createElement('div');o.className='cs-opt';o.textContent=opt.textContent||opt.label;
o.dataset.value=opt.value;if(opt.selected)o.classList.add('sel');
o.addEventListener('click',e=>{e.stopPropagation();
drop.querySelectorAll('.cs-opt').forEach(c=>c.classList.remove('sel'));o.classList.add('sel');
sel.value=opt.value;trigger.innerHTML=opt.textContent||opt.label+'<span style="display:none">_</span>';
drop.classList.remove('open');trigger.classList.remove('open');
sel.dispatchEvent(new Event('change',{bubbles:true}));
if(opt.value==='custom'){const ci=document.getElementById('exCustom');if(ci)ci.style.display=''}
else{const ci=document.getElementById('exCustom');if(ci)ci.style.display='none'}
});
drop.appendChild(o);options.push(o);
});
trigger.addEventListener('click',e=>{e.stopPropagation();
const isOpen=drop.classList.contains('open');
document.querySelectorAll('.cs-drop.open').forEach(d=>{d.classList.remove('open');d.previousElementSibling?.classList.remove('open')});
if(!isOpen){drop.classList.add('open');trigger.classList.add('open')}
});
sel.parentNode.insertBefore(wrap,sel);wrap.appendChild(sel);wrap.appendChild(trigger);wrap.appendChild(drop);
const selOpt=sel.querySelector('option[selected]')||sel.querySelector('option');
if(selOpt)trigger.innerHTML=selOpt.textContent||selOpt.label;
});
}
document.addEventListener('click',e=>{if(!e.target.closest('.cs-wrap'))document.querySelectorAll('.cs-drop.open').forEach(d=>{d.classList.remove('open');d.previousElementSibling?.classList.remove('open')})});
initCustomSelects();
"""

# Insert before the closing </script>
idx = f.rfind("</script>")
f = f[:idx] + js_add + "\n" + f[idx:]

p.write_text(f, encoding="utf-8")
print("Custom glass dropdowns added!")
print("cs-wrap:", "cs-wrap" in p.read_text(encoding="utf-8"))

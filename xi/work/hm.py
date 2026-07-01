import pathlib
p = pathlib.Path(r"C:\Users\hgs\Documents\Codex\2026-07-01\xi\work\index.html")
f = p.read_text(encoding="utf-8")

# Add heatmap CSS before </style>
heatmap_css = """
/* Activity Heatmap */
.heatmap-wrap{margin-top:8px}
.heatmap-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px}
.heatmap-header h3{font-size:15px;font-weight:560}
.heatmap-header .hm-total{font-size:12px;color:var(--t2)}
.heatmap-grid{display:flex;gap:3px;overflow-x:auto;padding-bottom:4px}
.heatmap-week{display:flex;flex-direction:column;gap:3px}
.heatmap-cell{width:12px;height:12px;border-radius:2px;background:var(--gls1);transition:all var(--e1);cursor:default;position:relative;flex-shrink:0}
.heatmap-cell:hover{outline:1px solid var(--gb-focus);z-index:2;transform:scale(1.4)}
.heatmap-cell[data-tip]:hover::after{content:attr(data-tip);position:absolute;bottom:calc(100% + 6px);left:50%;transform:translateX(-50%);white-space:nowrap;font-size:10px;font-family:var(--f);color:var(--t1);background:rgba(26,26,36,0.95);backdrop-filter:blur(20px);border:1px solid var(--gb);border-radius:6px;padding:4px 8px;pointer-events:none;z-index:10}
.heatmap-labels{display:flex;flex-direction:column;gap:3px;margin-right:5px;padding-top:2px}
.heatmap-labels span{font-size:9px;color:var(--t3);height:12px;line-height:12px}
.heatmap-months{display:flex;gap:3px;margin-top:4px;padding-left:20px}
.heatmap-months span{font-size:9px;color:var(--t3);flex-shrink:0}
.heatmap-legend{display:flex;align-items:center;gap:4px;margin-top:6px;font-size:10px;color:var(--t2)}
.heatmap-legend .leg-cell{width:10px;height:10px;border-radius:2px;flex-shrink:0}
"""

f = f.replace("</style>", heatmap_css + "</style>")

# Add heatmap HTML to exercise page - right before the exercise section closing
old_ex_close = '<section class="pg" id="pg-ex">'
idx = f.find(old_ex_close)
# Find the closing of exercise section
ex_section_end = f.find('</section>', f.find('id="pg-ex"'))
# Add heatmap before the closing </section> of pg-ex
# Actually, let me add it inside the exercise page, after the exercise-layout div
# Find: </div>\n</section>\n\n<section class="pg" id="pg-cy">
old_marker = '</div>\n</section>\n\n<section class="pg" id="pg-cy">'

heatmap_html = """</div>
<div class="card heatmap-wrap">
<div class="heatmap-header"><h3>📊 运动热力图</h3><span class="hm-total" id="hmTotal"></span></div>
<div style="display:flex;align-items:flex-start">
<div class="heatmap-labels" id="hmLabels"></div>
<div style="flex:1;overflow-x:auto">
<div class="heatmap-grid" id="hmGrid"></div>
<div class="heatmap-months" id="hmMonths"></div>
<div class="heatmap-legend">少<span class="leg-cell" style="background:var(--gls1)"></span><span class="leg-cell" style="background:rgba(48,209,88,0.2)"></span><span class="leg-cell" style="background:rgba(48,209,88,0.45)"></span><span class="leg-cell" style="background:rgba(48,209,88,0.7)"></span><span class="leg-cell" style="background:var(--ex)"></span>多</div>
</div>
</div>
</div>
</section>

<section class="pg" id="pg-cy">"""

f = f.replace(old_marker, heatmap_html)

# Add JS for heatmap rendering
old_render = """function re(){
document.getElementById('eddisp').textContent='📅 '+now();
document.getElementById('exDate').value=now();document.getElementById('exDur').value=30;"""

new_render_start = """function re(){
document.getElementById('eddisp').textContent='📅 '+now();
document.getElementById('exDate').value=now();document.getElementById('exDur').value=30;
renderHeatmap();"""

f = f.replace(old_render, new_render_start)

# Add the renderHeatmap function before the re() function
heatmap_js = """
function renderHeatmap(){
const weeks=20,now2=new Date();now2.setHours(0,0,0,0);
const endDay=new Date(now2);endDay.setDate(endDay.getDate()-(endDay.getDay()+1)%7+6);
const startDay=new Date(endDay);startDay.setDate(startDay.getDate()-weeks*7+1);
const grid=document.getElementById('hmGrid'),labels=document.getElementById('hmLabels'),months=document.getElementById('hmMonths'),total=document.getElementById('hmTotal');
labels.innerHTML='';for(let i=1;i<=7;i++){const d=new Date(startDay);d.setDate(d.getDate()+i-1);labels.innerHTML+='<span>'+['','一','','三','','五',''][i-1]+'</span>'}
let totalMin=0,html='';const todayStr=now();const dayData={};
D.ex.forEach(e=>{const m=e.duration||0;dayData[e.date]=(dayData[e.date]||0)+m});
const curMonth=-1;let monthHtml='';
for(let w=0;w<weeks;w++){
html+='<div class="heatmap-week">';
for(let d=0;d<7;d++){
const date=new Date(startDay);date.setDate(date.getDate()+w*7+d);const ds=fmt(date);
const mins=dayData[ds]||0;totalMin+=mins;let bg='var(--gls1)';let tip='';
if(mins>0){if(mins<=15)bg='rgba(48,209,88,0.15)';else if(mins<=30)bg='rgba(48,209,88,0.3)';else if(mins<=60)bg='rgba(48,209,88,0.55)';else bg='var(--ex)';tip=ds+' : '+mins+'分钟'}
if(ds===todayStr)bg=bg.replace('var(--gls1)','var(--gls2)');
html+='<div class="heatmap-cell" style="background:'+bg+'"'+(tip?' data-tip="'+tip+'"':'')+'></div>';
const m=date.getMonth();if(d===0&&m!==curMonth){monthHtml+='<span style="width:'+(12*7+3*7)+'px">'+['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月'][m]+'</span>'}
}
html+='</div>';
}
grid.innerHTML=html;months.innerHTML=monthHtml;total.textContent='总计 '+totalMin+' 分钟';
}
"""

# Insert renderHeatmap before the re() function
old_re_func = "function re(){\ndocument.getElementById('eddisp')"
f = f.replace(old_re_func, heatmap_js + "\n" + old_re_func)

p.write_text(f, encoding="utf-8")
print("Heatmap added!")

# verify
v = p.read_text(encoding="utf-8")
print("heatmap-grid:", "heatmap-grid" in v)
print("renderHeatmap:", "renderHeatmap" in v)

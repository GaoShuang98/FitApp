# -*- coding: utf-8 -*-
import pathlib
import re

p = pathlib.Path(r"C:\Users\hgs\Documents\Codex\2026-07-01\xi\work\index.html")
f = p.read_text(encoding="utf-8")

# Extract HTML/CSS part
script_start = f.find("<script>")
script_end = f.find("</script>") + len("</script>")
html_css = f[:script_start]
closing = f[script_end:]

# Write completely clean JavaScript
clean_js = """<script>
'use strict';
const SK='luna_v1';
function ld(){try{const d=localStorage.getItem(SK);return d?JSON.parse(d):{ex:[],pd:[]}}catch(e){return{ex:[],pd:[]}}}
function sd(d){localStorage.setItem(SK,JSON.stringify(d))}
let D=ld();
const fmt=d=>{const y=d.getFullYear(),m=String(d.getMonth()+1).padStart(2,'0'),day=String(d.getDate()).padStart(2,'0');return y+'-'+m+'-'+day};
const now=()=>fmt(new Date());
const im={running:'🏃',walking:'🚶',yoga:'🧘',swimming:'🏊',cycling:'🚴',gym:'🏋️',dancing:'💃',pilates:'🤸',hiking:'🥾',aerobic:'🏋',jump_rope:'🪢',rowing:'🚣',badminton:'🏸',custom:'📝'};
const nm={running:'跑步',walking:'散步',yoga:'瑜伽',swimming:'游泳',cycling:'骑行',gym:'力量训练',dancing:'跳舞',aerobic:'跳操',pilates:'普拉提',hiking:'徒步',jump_rope:'跳绳',rowing:'划船',badminton:'羽毛球',custom:'自定义'};
const icm={running:'run',walking:'walk',yoga:'yoga',swimming:'swim',cycling:'cyc',gym:'gym',dancing:'run',aerobic:'run',pilates:'yoga',hiking:'walk',jump_rope:'run',rowing:'swim',badminton:'run',custom:'run'};
const iv={'light':'轻松','moderate':'适中','intense':'高强度'};
const fv={'light':'少量','medium':'中量','heavy':'大量'};
const sv={'cramps':'腹痛','headache':'头痛','fatigue':'疲劳','bloating':'腹胀','mood':'情绪波动','backache':'腰酸'};

function nav(p){
document.querySelectorAll('.ni').forEach(b=>b.classList.remove('act'));
document.querySelector('.ni[data-page="'+p+'"]').classList.add('act');
document.querySelectorAll('.pg').forEach(pg=>pg.classList.remove('act'));
document.getElementById('pg-'+p).classList.add('act');
if(p==='dash')rd();if(p==='ex')re();if(p==='cy')rc();if(p==='hist')rh();
}
document.querySelectorAll('.ni').forEach(b=>b.addEventListener('click',()=>nav(b.dataset.page)));

function rd(){
document.getElementById('tdisp').textContent='📅 '+now();
const t=now(),te=D.ex.filter(e=>e.date===t),tm=te.reduce((s,e)=>s+e.duration,0);
const wa=new Date();wa.setDate(wa.getDate()-7);const ws=fmt(wa);
const we=D.ex.filter(e=>e.date>=ws),wm=we.reduce((s,e)=>s+e.duration,0),wc=we.length;
const pds=D.pd.sort((a,b)=>b.startDate.localeCompare(a.startDate)),lp=pds[0];
let ci='暂无记录';
if(lp){const sd2=new Date(lp.startDate),td2=new Date(),dd=Math.floor((td2-sd2)/(86400000));ci='上次 '+lp.startDate+' ('+dd+'天前)';if(lp.endDate&&t<=lp.endDate&&t>=lp.startDate)ci='🩸 当前经期中'}
const cp=pds.find(p=>t>=p.startDate&&t<=(p.endDate||p.startDate));
document.getElementById('badge').style.display=cp?'inline':'none';
document.getElementById('dstats').innerHTML=
'<div class="card sc"><div class="sv ex">'+tm+'</div><div class="sl">今日运动（分）</div><div class="ss">'+te.length+' 次</div></div>'+
'<div class="card sc"><div class="sv ex">'+wm+'</div><div class="sl">本周运动（分）</div><div class="ss">'+wc+' 次</div></div>'+
'<div class="card sc"><div class="sv cy">'+(pds.length||'0')+'</div><div class="sl">经期记录</div><div class="ss">'+ci+'</div></div>'+
'<div class="card sc"><div class="sv wm">'+(lp?Math.round((new Date(lp.endDate||lp.startDate)-new Date(lp.startDate))/86400000)+1:'-')+'</div><div class="sl">最近经期天数</div></div>';
const days2=['日','一','二','三','四','五','六'],ch2=document.getElementById('wchart');ch2.innerHTML='';
for(let i=6;i>=0;i--){const d=new Date();d.setDate(d.getDate()-i);const ds=fmt(d),de=D.ex.filter(e=>e.date===ds),m=de.reduce((s,e)=>s+e.duration,0),h=Math.max(3,Math.min(120,m*1.8));ch2.innerHTML+='<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:5px"><span style="font-size:11px;color:var(--t2)">'+m+'</span><div style="width:100%;max-width:40px;height:'+h+'px;background:'+(i===0?'var(--ex)':'rgba(52,199,89,0.3)')+';border-radius:7px 7px 3px 3px"></div><span style="font-size:10px;color:var(--t3)">'+days2[d.getDay()]+'</span></div>'}
const rc=[...D.ex.map(e=>({...e,it:'ex'})),...D.pd.map(p=>({...p,it:'pd'}))].sort((a,b)=>new Date(b.date||b.startDate)-new Date(a.date||a.startDate)).slice(0,6);
const ra=document.getElementById('recent');
if(rc.length===0){ra.innerHTML='<div class="emp"><div class="eic">📝</div><p>还没有记录</p></div>';return}
ra.innerHTML=rc.map(r=>{if(r.it==='pd')return '<div class="ti"><div class="td">'+r.startDate+(r.endDate!==r.startDate?' ~ '+r.endDate:'')+'</div><div class="tc"><h4>🌸 经期</h4><p>流量: '+fv[r.flow||'medium']+((r.symptoms||[]).length?' · '+r.symptoms.map(s=>sv[s]||s).join('、'):'')+'</p></div></div>';return '<div class="ti"><div class="td">'+r.date+'</div><div class="tc"><h4>'+im[r.type]+' '+(nm[r.type]||(r.customName||'自定义'))+' · '+r.duration+'分钟</h4><p>'+iv[r.intensity||'moderate']+(r.notes?' · '+r.notes:'')+'</p></div></div>'}).join('');
}

let eid=null;
function renderHeatmap(){
const weeks=24,now2=new Date();now2.setHours(0,0,0,0);
const endDay=new Date(now2);endDay.setDate(endDay.getDate()-(endDay.getDay()+1)%7+6);
const startDay=new Date(endDay);startDay.setDate(startDay.getDate()-weeks*7+1);
const body=document.getElementById('hmBody'),total=document.getElementById('hmTotal');
const todayStr=now();const dayData={};let totalMin=0;
D.ex.forEach(e=>{const m=e.duration||0;dayData[e.date]=(dayData[e.date]||0)+m});
const dlabels=['','一','','三','','五',''];
let monthRow='<tr><td></td>';let lastMonth=-1;
for(let w=0;w<weeks;w++){
const d=new Date(startDay);d.setDate(d.getDate()+w*7);const m=d.getMonth();
if(m!==lastMonth){lastMonth=m;monthRow+='<td class="hm-month" colspan="7">'+['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月'][m]+'</td>'}
}
monthRow+='</tr>';
let rows='';
for(let dow=0;dow<7;dow++){
let r='<tr>';
r+=dow%2===1?'<td class="hm-label">'+dlabels[dow]+'</td>':'<td class="hm-label"></td>';
for(let w=0;w<weeks;w++){
const date=new Date(startDay);date.setDate(date.getDate()+w*7+dow);const ds=fmt(date);
const mins=dayData[ds]||0;totalMin+=mins;
let bg='var(--gls1)';let tip='';
if(mins>0){if(mins<=15)bg='rgba(48,209,88,0.15)';else if(mins<=30)bg='rgba(48,209,88,0.3)';else if(mins<=60)bg='rgba(48,209,88,0.55)';else bg='var(--ex)';tip=ds+' : '+mins+'分钟'}
if(!mins&&ds===todayStr)bg='var(--gls2)';
r+='<td><div class="heatmap-cell" style="background:'+bg+'"'+(tip?' data-tip="'+tip+'"':'')+'></div></td>';
}
r+='</tr>';rows+=r;
}
body.innerHTML=monthRow+rows;total.textContent='总计 '+totalMin+' 分钟';
}
function re(){
document.getElementById('eddisp').textContent='📅 '+now();
document.getElementById('exDate').value=now();document.getElementById('exDur').value=30;
document.getElementById('exNotes').value='';document.getElementById('exType').value='running';
document.querySelectorAll('#igrp .ibtn').forEach(b=>b.classList.remove('sel'));
document.querySelector('#igrp .ibtn[data-v="moderate"]').classList.add('sel');
eid=null;document.getElementById('btnEx').textContent='记录运动';rte();renderHeatmap();
}
function rte(){
const t=now(),list=D.ex.filter(e=>e.date===t).sort((a,b)=>b.id-a.id),el=document.getElementById('todayEx');
if(list.length===0){el.innerHTML='<div class="emp"><div class="eic">💪</div><p>今天还没有运动</p></div>';return}
el.innerHTML=list.map(e=>'<div class="exi"><div class="ei '+icm[e.type]+'">'+im[e.type]+'</div><div class="exif"><div class="en">'+(nm[e.type]||(e.customName||'自定义'))+'</div><div class="em">'+iv[e.intensity||'moderate']+(e.notes?' · '+e.notes:'')+'</div></div><div class="ed">'+e.duration+' 分钟</div><button class="btn btn-d" onclick="edite('+e.id+')">编辑</button><button class="btn btn-d" onclick="dele('+e.id+')">✕</button></div>').join('');
}
document.getElementById('btnEx').addEventListener('click',()=>{
const date=document.getElementById('exDate').value||now();let type=document.getElementById('exType').value;let customName='';
if(type==='custom'){customName=document.getElementById('exCustom').value.trim();if(!customName){alert('请输入自定义运动名称');return}}
const dur=parseInt(document.getElementById('exDur').value)||0;const inten=document.querySelector('#igrp .ibtn.sel')?.dataset.v||'moderate';
const notes=document.getElementById('exNotes').value.trim();
if(dur<=0){alert('请输入运动时长');return}
if(eid!==null){const i=D.ex.findIndex(e=>e.id===eid);if(i!==-1){if(type==='custom')D.ex[i]={...D.ex[i],date,type:'custom',duration:dur,intensity:inten,notes,customName:customName};else D.ex[i]={...D.ex[i],date,type,duration:dur,intensity:inten,notes}};eid=null;document.getElementById('btnEx').textContent='记录运动'}
else{if(type==='custom')D.ex.push({id:Date.now(),date,type:'custom',duration:dur,intensity:inten,notes,customName:customName});else D.ex.push({id:Date.now(),date,type,duration:dur,intensity:inten,notes})}
sd(D);re();rd();
});
function edite(id){const e=D.ex.find(x=>x.id===id);if(!e)return;document.getElementById('exDate').value=e.date;document.getElementById('exType').value=e.type==='custom'?'custom':e.type;if(e.customName){document.getElementById('exCustom').value=e.customName;document.getElementById('exCustom').style.display=''}document.getElementById('exDur').value=e.duration;document.getElementById('exNotes').value=e.notes||'';document.querySelectorAll('#igrp .ibtn').forEach(b=>b.classList.remove('sel'));const b=document.querySelector('#igrp .ibtn[data-v="'+e.intensity+'"]');if(b)b.classList.add('sel');eid=id;document.getElementById('btnEx').textContent='更新运动';document.getElementById('pg-ex').scrollIntoView({behavior:'smooth'})}
function dele(id){if(confirm('删除这条记录？')){D.ex=D.ex.filter(e=>e.id!==id);sd(D);re();rd()}}
document.querySelectorAll('#igrp .ibtn').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('#igrp .ibtn').forEach(x=>x.classList.remove('sel'));b.classList.add('sel')}));
document.getElementById('exType').addEventListener('change',()=>{const v=document.getElementById('exType').value;document.getElementById('exCustom').style.display=v==='custom'?'':'none'});

let cy,cm,pid=null,ssym=[];
function rc(){
document.getElementById('cddisp').textContent='📅 '+now();
const nd=new Date();cy=nd.getFullYear();cm=nd.getMonth();
rcal();document.getElementById('pStart').value=now();document.getElementById('pEnd').value='';
document.getElementById('pFlow').value='medium';document.getElementById('pNotes').value='';ssym=[];
document.querySelectorAll('#stags .stag').forEach(t=>t.classList.remove('sel'));
pid=null;document.getElementById('btnPeriod').style.display='';
document.getElementById('btnUpdPeriod').style.display='none';
document.getElementById('btnCancelPeriod').style.display='none';rcs();
}
function rcal(){
document.getElementById('cTitle').textContent=cy+'年 '+(cm+1)+'月';
const g=document.getElementById('cGrid'),dhs=['日','一','二','三','四','五','六'];
let h=dhs.map(d=>'<div class="cdh">'+d+'</div>').join('');
const fd=new Date(cy,cm,1).getDay(),dim2=new Date(cy,cm+1,0).getDate(),tn=now();
const pds=new Set(),pss=new Set(),pes=new Set();
D.pd.forEach(p=>{const s=new Date(p.startDate),e=new Date(p.endDate||p.startDate);for(let d=new Date(s);d<=e;d.setDate(d.getDate()+1)){const ds=fmt(d);pds.add(ds);if(fmt(d)===p.startDate)pss.add(ds);if(fmt(d)===(p.endDate||p.startDate))pes.add(ds)}});
const prs=new Set(),ovs=new Set();
if(D.pd.length>=2){const ps=D.pd.sort((a,b)=>a.startDate.localeCompare(b.startDate));let tc2=0;for(let i=1;i<ps.length;i++)tc2+=Math.round((new Date(ps[i].startDate)-new Date(ps[i-1].startDate))/86400000);const ac=Math.round(tc2/(ps.length-1))||28;const ls=new Date(ps[ps.length-1].startDate),ps2=new Date(ls);ps2.setDate(ps2.getDate()+ac);const pe=new Date(ps2);pe.setDate(pe.getDate()+4);for(let d=new Date(ps2);d<=pe;d.setDate(d.getDate()+1))prs.add(fmt(d));const ov=new Date(ps2);ov.setDate(ov.getDate()-14);for(let i=-2;i<=2;i++){const od=new Date(ov);od.setDate(od.getDate()+i);ovs.add(fmt(od))}}
const pd2=new Date(cy,cm,0).getDate();
for(let i=fd-1;i>=0;i--){h+='<div class="cd om">'+(pd2-i)+'</div>'}
for(let day=1;day<=dim2;day++){const ds=cy+'-'+String(cm+1).padStart(2,'0')+'-'+String(day).padStart(2,'0');let cls='cd';if(ds===tn)cls+=' today';if(pds.has(ds)){cls+=' prd';if(pss.has(ds)&&pes.has(ds))cls+=' prd-1';else if(pss.has(ds))cls+=' prd-s';else if(pes.has(ds))cls+=' prd-e'}if(prs.has(ds))cls+=' pred';if(ovs.has(ds)&&!pds.has(ds)&&!prs.has(ds))cls+=' ovu';h+='<div class="'+cls+'" data-date="'+ds+'" onclick="cdClick(\''+ds+'\')">'+day+'</div>'}
const rem=42-(fd+dim2);for(let i=1;i<=rem;i++){h+='<div class="cd om">'+i+'</div>'}
g.innerHTML=h;
}
function cdClick(ds){document.getElementById('pStart').value=ds;document.getElementById('pEnd').value='';document.getElementById('pg-cy').scrollIntoView({behavior:'smooth'})}
document.getElementById('cPrev').addEventListener('click',()=>{cm--;if(cm<0){cy--;cm=11}rcal()});
document.getElementById('cNext').addEventListener('click',()=>{cm++;if(cm>11){cy++;cm=0}rcal()});
document.querySelectorAll('#stags .stag').forEach(t=>t.addEventListener('click',()=>{t.classList.toggle('sel');const s=t.dataset.s;if(t.classList.contains('sel')){if(!ssym.includes(s))ssym.push(s)}else ssym=ssym.filter(x=>x!==s)}));
document.getElementById('btnPeriod').addEventListener('click',()=>{
const sd2=document.getElementById('pStart').value,ed2=document.getElementById('pEnd').value||sd2;
const flow=document.getElementById('pFlow').value,notes=document.getElementById('pNotes').value.trim();
if(!sd2){alert('请选择开始日期');return}
D.pd.push({id:Date.now(),startDate:sd2,endDate:ed2,flow,symptoms:[...ssym],notes});sd(D);rc();rd();
});
document.getElementById('btnUpdPeriod').addEventListener('click',()=>{
if(pid===null)return;const i=D.pd.findIndex(p=>p.id===pid);if(i===-1)return;
D.pd[i]={...D.pd[i],startDate:document.getElementById('pStart').value,endDate:document.getElementById('pEnd').value||document.getElementById('pStart').value,flow:document.getElementById('pFlow').value,symptoms:[...ssym],notes:document.getElementById('pNotes').value.trim()};
sd(D);pid=null;document.getElementById('btnPeriod').style.display='';
document.getElementById('btnUpdPeriod').style.display='none';document.getElementById('btnCancelPeriod').style.display='none';rc();rd();
});
document.getElementById('btnCancelPeriod').addEventListener('click',()=>{
pid=null;document.getElementById('pStart').value=now();document.getElementById('pEnd').value='';
document.getElementById('pFlow').value='medium';document.getElementById('pNotes').value='';ssym=[];
document.querySelectorAll('#stags .stag').forEach(t=>t.classList.remove('sel'));
document.getElementById('btnPeriod').style.display='';document.getElementById('btnUpdPeriod').style.display='none';
document.getElementById('btnCancelPeriod').style.display='none';
});
function rcs(){
const ps=D.pd.sort((a,b)=>a.startDate.localeCompare(b.startDate));
if(ps.length===0){document.getElementById('cStats').innerHTML='<p style="font-size:12px;color:var(--t3)">暂无数据</p>';return}
let tc2=0;for(let i=1;i<ps.length;i++)tc2+=Math.round((new Date(ps[i].startDate)-new Date(ps[i-1].startDate))/86400000);
const ac=ps.length>=2?Math.round(tc2/(ps.length-1)):'-';let tpd=0;
ps.forEach(p=>{tpd+=Math.round((new Date(p.endDate||p.startDate)-new Date(p.startDate))/86400000)+1});
const ap=Math.round(tpd/ps.length),last=ps[ps.length-1],np=new Date(last.startDate);
np.setDate(np.getDate()+(ac!=='-'?ac:28));
let h='<div style="display:grid;grid-template-columns:1fr 1fr;gap:7px;font-size:12px">';
h+='<div><span style="color:var(--t2)">平均周期</span><br><strong>'+ac+' 天</strong></div>';
h+='<div><span style="color:var(--t2)">平均经期</span><br><strong>'+ap+' 天</strong></div>';
h+='<div><span style="color:var(--t2)">记录次数</span><br><strong>'+ps.length+' 次</strong></div>';
h+='<div><span style="color:var(--t2)">预测下次</span><br><strong>'+fmt(np)+'</strong></div></div>';
h+='<div style="margin-top:10px;max-height:180px;overflow-y:auto">';
[...ps].reverse().slice(0,5).forEach(p=>{const days3=Math.round((new Date(p.endDate||p.startDate)-new Date(p.startDate))/86400000)+1;h+='<div class="pli"><div class="pdb"></div><div style="flex:1"><div style="font-size:12px;font-weight:500">'+p.startDate+(p.endDate!==p.startDate?' ~ '+p.endDate:'')+' ('+days3+'天)</div><div style="font-size:10px;color:var(--t2)">'+fv[p.flow||'medium']+((p.symptoms||[]).length?' · '+p.symptoms.map(s=>sv[s]||s).join('、'):'')+'</div></div><button class="btn btn-d" onclick="editp('+p.id+')">编辑</button><button class="btn btn-d" onclick="delp('+p.id+')">✕</button></div>'});
h+='</div>';document.getElementById('cStats').innerHTML=h;
}
function editp(id){const p=D.pd.find(x=>x.id===id);if(!p)return;document.getElementById('pStart').value=p.startDate;document.getElementById('pEnd').value=p.endDate||'';document.getElementById('pFlow').value=p.flow||'medium';document.getElementById('pNotes').value=p.notes||'';ssym=p.symptoms?[...p.symptoms]:[];document.querySelectorAll('#stags .stag').forEach(t=>t.classList.toggle('sel',ssym.includes(t.dataset.s)));pid=id;document.getElementById('btnPeriod').style.display='none';document.getElementById('btnUpdPeriod').style.display='';document.getElementById('btnCancelPeriod').style.display=''}
function delp(id){if(confirm('删除这条经期记录？')){D.pd=D.pd.filter(p=>p.id!==id);sd(D);rc();rd()}}

let hf='all';
function rh(filter){if(filter)hf=filter;
document.querySelectorAll('.hfilt .fchip').forEach(c=>c.classList.toggle('act',c.dataset.filter===hf));
const items=[];if(hf==='all'||hf==='exercise')D.ex.forEach(e=>items.push({...e,it:'ex'}));
if(hf==='all'||hf==='cycle')D.pd.forEach(p=>items.push({...p,it:'pd'}));
items.sort((a,b)=>new Date(b.date||b.startDate)-new Date(a.date||a.startDate));
const el=document.getElementById('timeline');
if(items.length===0){el.innerHTML='<div class="emp"><div class="eic">📋</div><p>暂无记录</p></div>';return}
el.innerHTML=items.map(r=>{if(r.it==='pd')return '<div class="ti"><div class="td">'+r.startDate+(r.endDate!==r.startDate?' ~ '+r.endDate:'')+'</div><div class="tc"><h4>🌸 经期</h4><p>流量: '+fv[r.flow||'medium']+((r.symptoms||[]).length?' · '+r.symptoms.map(s=>sv[s]||s).join('、'):'')+(r.notes?' · '+r.notes:'')+'</p></div></div>';return '<div class="ti"><div class="td">'+r.date+'</div><div class="tc"><h4>'+im[r.type]+' '+(nm[r.type]||(r.customName||'自定义'))+' · '+r.duration+'分钟</h4><p>'+iv[r.intensity||'moderate']+(r.notes?' · '+r.notes:'')+'</p></div></div>'}).join('');
}
document.querySelectorAll('.hfilt .fchip').forEach(c=>c.addEventListener('click',()=>rh(c.dataset.filter)));

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

document.getElementById('exDate').value=now();document.getElementById('pStart').value=now();rd();
</script>"""

# Reconstruct
new_file = html_css + clean_js + closing
p.write_text(new_file, encoding="utf-8")
print("JS rebuilt!")
print("File size:", len(new_file))

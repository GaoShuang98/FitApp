# -*- coding: utf-8 -*-
import pathlib, re

p = pathlib.Path(r"C:\Users\hgs\Documents\Codex\2026-07-01\xi\work\index.html")
f = p.read_text(encoding="utf-8")

# 1. Find and replace the select
sel_start = "exType\"><option value=\"running\">"
sel_end = "</select></div>"
i1 = f.find(sel_start)
i2 = f.find(sel_end, i1) + len(sel_end)

new_options = (
    'exType"><option value="running">🏃 跑步</option>'
    '<option value="walking">🚶 散步</option>'
    '<option value="yoga">🧘 瑜伽</option>'
    '<option value="swimming">🏊 游泳</option>'
    '<option value="cycling">🚴 骑行</option>'
    '<option value="gym">🏋️ 力量</option>'
    '<option value="dancing">💃 跳舞</option>'
    '<option value="pilates">🤸 普拉提</option>'
    '<option value="hiking">🥾 徒步</option>'
    '<option value="jump_rope">🪢 跳绳</option>'
    '<option value="tai_chi">☯ 太极</option>'
    '<option value="boxing">🥊 拳击</option>'
    '<option value="climbing">🧗 攀岩</option>'
    '<option value="rowing">🚣 划船</option>'
    '<option value="skiing">🎿 滑雪</option>'
    '<option value="basketball">🏀 篮球</option>'
    '<option value="soccer">⚽ 足球</option>'
    '<option value="badminton">🏸 羽毛球</option>'
    '<option value="table_tennis">🏓 乒乓球</option>'
    '<option value="tennis">🎾 网球</option>'
    '<option value="custom">📝 自定义</option>'
    '</select><input type="text" class="fi" id="exCustom" placeholder="输入运动名称" style="display:none;margin-top:8px"></div>'
)
f = f[:i1] + new_options + f[i2:]
print("Select updated")

# 2. Replace icon map
old_im = "const im={running:'🏃',walking:'🚶',yoga:'🧘',swimming:'🏊',cycling:'🚴',gym:'🏋️',dancing:'💃',pilates:'🤸',hiking:'🥾',other:'📝'};"
new_im = "const im={running:'🏃',walking:'🚶',yoga:'🧘',swimming:'🏊',cycling:'🚴',gym:'🏋️',dancing:'💃',pilates:'🤸',hiking:'🥾',jump_rope:'🪢',tai_chi:'☯',boxing:'🥊',climbing:'🧗',rowing:'🚣',skiing:'🎿',basketball:'🏀',soccer:'⚽',badminton:'🏸',table_tennis:'🏓',tennis:'🎾',custom:'📝'};"
if old_im in f:
    f = f.replace(old_im, new_im)
    print("Icon map updated")

# 3. Replace name map
old_nm = "const nm={running:'跑步',walking:'散步',yoga:'瑜伽',swimming:'游泳',cycling:'骑行',gym:'力量训练',dancing:'跳舞',pilates:'普拉提',hiking:'徒步',other:'其他'};"
new_nm = "const nm={running:'跑步',walking:'散步',yoga:'瑜伽',swimming:'游泳',cycling:'骑行',gym:'力量训练',dancing:'跳舞',pilates:'普拉提',hiking:'徒步',jump_rope:'跳绳',tai_chi:'太极',boxing:'拳击',climbing:'攀岩',rowing:'划船',skiing:'滑雪',basketball:'篮球',soccer:'足球',badminton:'羽毛球',table_tennis:'乒乓球',tennis:'网球',custom:'自定义'};"
if old_nm in f:
    f = f.replace(old_nm, new_nm)
    print("Name map updated")

# 4. Fix render code to handle custom names
# In rte() function: nm[e.type] -> (nm[e.type]||(e.customName||'自定义'))
old_rte = "+nm[e.type]+"
new_rte = "+(nm[e.type]||(e.customName||'自定义'))+"
if old_rte in f:
    f = f.replace(old_rte, new_rte)
    print("rte render updated")

# Also fix in the recent activity and timeline rendering
old_tl = "+im[r.type]+' '+nm[r.type]+"
new_tl = "+im[r.type]+' '+(nm[r.type]||(r.customName||'自定义'))+"
if old_tl in f:
    f = f.replace(old_tl, new_tl)
    print("Timeline render updated")

# Fix editable exercise listing too
if old_rte in f:
    f = f.replace(old_rte, new_rte)
    print("rte2 updated")

# 5. Fix edite() function to handle custom names on edit
old_edite = "document.getElementById('exType').value=e.type;"
new_edite = "document.getElementById('exType').value=e.type==='custom'?'custom':e.type;if(e.customName){document.getElementById('exCustom').value=e.customName;document.getElementById('exCustom').style.display=''};"
if old_edite in f:
    f = f.replace(old_edite, new_edite)
    print("edite updated")

p.write_text(f, encoding="utf-8")
print("All remaining fixes applied!")

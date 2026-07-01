# -*- coding: utf-8 -*-
import pathlib, base64

# Read current file - HTML/CSS is intact, JS section is corrupted
p = pathlib.Path(r'C:\Users\hgs\Documents\Codex\2026-07-01\xi\work\index.html')
f = p.read_text(encoding='utf-8')
s = f.find('<script>')
e = f.find('</script>') + len('</script>')
html_css = f[:s]
closing = f[e:]

# Chinese strings (constructed via \\u escapes - pure ASCII source, correct Unicode output)
CN = {
    # Exercise names
    'nm_running': '\u8dd1\u6b65', 'nm_walking': '\u6563\u6b65', 'nm_yoga': '\u7477\u4f3d',
    'nm_swimming': '\u6e38\u6cf3', 'nm_cycling': '\u9a91\u884c', 'nm_gym': '\u529b\u91cf\u8bad\u7ec3',
    'nm_dancing': '\u8df3\u821e', 'nm_aerobic': '\u8df3\u64cd', 'nm_pilates': '\u666e\u62c9\u63d0',
    'nm_hiking': '\u5f92\u6b65', 'nm_jump_rope': '\u8df3\u7ef3', 'nm_rowing': '\u5212\u8239',
    'nm_badminton': '\u7fbd\u6bdb\u7403', 'nm_custom': '\u81ea\u5b9a\u4e49',
    # Intensity
    'iv_light': '\u8f7b\u677e', 'iv_moderate': '\u9002\u4e2d', 'iv_intense': '\u9ad8\u5f3a\u5ea6',
    # Flow
    'fv_light': '\u5c11\u91cf', 'fv_medium': '\u4e2d\u91cf', 'fv_heavy': '\u5927\u91cf',
    # Symptoms
    'sv_cramps': '\u8179\u75db', 'sv_headache': '\u5934\u75db', 'sv_fatigue': '\u75b2\u52b3',
    'sv_bloating': '\u8179\u80c0', 'sv_mood': '\u60c5\u7eea\u6ce2\u52a8', 'sv_backache': '\u8170\u9178',
    # UI labels
    'no_record': '\u6682\u65e0\u8bb0\u5f55', 'no_data': '\u6682\u65e0\u6570\u636e',
    'no_exercise_today': '\u4eca\u5929\u8fd8\u6ca1\u6709\u8fd0\u52a8',
    'no_record_yet': '\u8fd8\u6ca1\u6709\u8bb0\u5f55',
    'today_ex_min': '\u4eca\u65e5\u8fd0\u52a8\uff08\u5206\uff09',
    'week_ex_min': '\u672c\u5468\u8fd0\u52a8\uff08\u5206\uff09',
    'period_records': '\u7ecf\u671f\u8bb0\u5f55',
    'recent_period_days': '\u6700\u8fd1\u7ecf\u671f\u5929\u6570',
    'last_time': '\u4e0a\u6b21',
    'days_ago': '\u5929\u524d',
    'current_period': '\u5f53\u524d\u7ecf\u671f\u4e2d',
    'avg_cycle': '\u5e73\u5747\u5468\u671f',
    'avg_period': '\u5e73\u5747\u7ecf\u671f',
    'record_count': '\u8bb0\u5f55\u6b21\u6570',
    'predict_next': '\u9884\u6d4b\u4e0b\u6b21',
    'enter_duration': '\u8bf7\u8f93\u5165\u8fd0\u52a8\u65f6\u957f',
    'enter_custom_name': '\u8bf7\u8f93\u5165\u81ea\u5b9a\u4e49\u8fd0\u52a8\u540d\u79f0',
    'select_start_date': '\u8bf7\u9009\u62e9\u5f00\u59cb\u65e5\u671f',
    'delete_record': '\u5220\u9664\u8fd9\u6761\u8bb0\u5f55\uff1f',
    'delete_period': '\u5220\u9664\u8fd9\u6761\u7ecf\u671f\u8bb0\u5f55\uff1f',
    'day': '\u5929',
    'minute': '\u5206\u949f',
    'edit': '\u7f16\u8f91',
    'update': '\u66f4\u65b0',
    'minutes_unit': '\u5206\u949f',
    'times': '\u6b21',
    'record_exercise': '\u8bb0\u5f55\u8fd0\u52a8',
    'update_exercise': '\u66f4\u65b0\u8fd0\u52a8',
    'record_period': '\u8bb0\u5f55\u7ecf\u671f',
    'update_record': '\u66f4\u65b0\u8bb0\u5f55',
    'cancel_edit': '\u53d6\u6d88\u7f16\u8f91',
    'period': '\u7ecf\u671f',
    'flow_label': '\u6d41\u91cf',
    'total': '\u603b\u8ba1',
    'month_labels': ['1\u6708','2\u6708','3\u6708','4\u6708','5\u6708','6\u6708','7\u6708','8\u6708','9\u6708','10\u6708','11\u6708','12\u6708'],
}

# Build clean JS
js = '''<script>
'use strict';
const SK='luna_v1';
function ld(){try{const d=localStorage.getItem(SK);return d?JSON.parse(d):{ex:[],pd:[]}}catch(e){return{ex:[],pd:[]}}}
function sd(d){localStorage.setItem(SK,JSON.stringify(d))}
let D=ld();
const fmt=d=>{const y=d.getFullYear(),m=String(d.getMonth()+1).padStart(2,'0'),day=String(d.getDate()).padStart(2,'0');return y+'-'+m+'-'+day};
const now=()=>fmt(new Date());
const im={running:''' + repr('\U0001f3c3') + ''',walking:''' + repr('\U0001f6b6') + ''',yoga:''' + repr('\U0001f9d8') + ''',swimming:''' + repr('\U0001f3ca') + ''',cycling:''' + repr('\U0001f6b4') + ''',gym:''' + repr('\U0001f3cb\ufe0f') + ''',dancing:''' + repr('\U0001f483') + ''',aerobic:''' + repr('\U0001f3cb') + ''',pilates:''' + repr('\U0001f938') + ''',hiking:''' + repr('\U0001f97e') + ''',jump_rope:''' + repr('\U0001faa2') + ''',rowing:''' + repr('\U0001f6a3') + ''',badminton:''' + repr('\U0001f3f8') + ''',custom:''' + repr('\U0001f4dd') + '''};
const nm={running:'CN0',walking:'CN1',yoga:'CN2',swimming:'CN3',cycling:'CN4',gym:'CN5',dancing:'CN6',aerobic:'CN7',pilates:'CN8',hiking:'CN9',jump_rope:'CN10',rowing:'CN11',badminton:'CN12',custom:'CN13'};
const icm={running:'run',walking:'walk',yoga:'yoga',swimming:'swim',cycling:'cyc',gym:'gym',dancing:'run',aerobic:'run',pilates:'yoga',hiking:'walk',jump_rope:'run',rowing:'swim',badminton:'run',custom:'run'};
const iv={'light':'CN14','moderate':'CN15','intense':'CN16'};
const fv={'light':'CN17','medium':'CN18','heavy':'CN19'};
const sv={'cramps':'CN20','headache':'CN21','fatigue':'CN22','bloating':'CN23','mood':'CN24','backache':'CN25'};
'''

# Replace placeholders with Chinese
cn_keys = ['nm_running','nm_walking','nm_yoga','nm_swimming','nm_cycling','nm_gym','nm_dancing','nm_aerobic','nm_pilates','nm_hiking','nm_jump_rope','nm_rowing','nm_badminton','nm_custom','iv_light','iv_moderate','iv_intense','fv_light','fv_medium','fv_heavy','sv_cramps','sv_headache','sv_fatigue','sv_bloating','sv_mood','sv_backache']
for i, k in enumerate(cn_keys):
    js = js.replace(f'CN{i}', CN[k])

print('JS part 1 written')
pathlib.Path(r'C:/Users/hgs/Documents/Codex/2026-07-01/xi/work/js_part1.txt').write_text(js, encoding='utf-8')
print('OK')


# -*- coding: utf-8 -*-
import pathlib, re

p = pathlib.Path(r"C:\Users\hgs\Documents\Codex\2026-07-01\xi\work\index.html")
f = p.read_text(encoding="utf-8")

# Comprehensive fix: replace all corrupted Chinese patterns in JS
# Each entry: (context_before, corrupted_pattern_suffix, correct_string)
fixes = [
    # Exercise names in nm
    ("running:'", "?'}", "\u8dd1\u6b65"),
    ("walking:'", "?'}", "\u6563\u6b65"),
    ("yoga:'", "?'}", "\u7477\u4f3d"),
    ("swimming:'", "?'}", "\u6e38\u6cf3"),
    ("cycling:'", "?'}", "\u9a91\u884c"),
    ("gym:'", "?'}", "\u529b\u91cf\u8bad\u7ec3"),
    ("dancing:'", "?'}", "\u8df3\u821e"),
    ("aerobic:'", "?'}", "\u8df3\u64cd"),
    ("pilates:'", "?'}", "\u666e\u62c9\u63d0"),
    ("hiking:'", "?'}", "\u5f92\u6b65"),
    ("jump_rope:'", "?'}", "\u8df3\u7ef3"),
    ("rowing:'", "?'}", "\u5212\u8239"),
    ("badminton:'", "?'}", "\u7fbd\u6bdb\u7403"),
    ("custom:'", "?'}", "\u81ea\u5b9a\u4e49"),
    # Intensity labels
    ("light':'", "?','moderate", "\u8f7b\u677e"),
    ("moderate':'", "?','intense", "\u9002\u4e2d"),
    ("intense':'", "?'}", "\u9ad8\u5f3a\u5ea6"),
    # Flow labels
    ("fv={'light':'", "?','medium", "\u5c11\u91cf"),
    ("medium':'", "?','heavy", "\u4e2d\u91cf"),
    ("heavy':'", "?'}", "\u5927\u91cf"),
    # Symptom labels
    ("cramps':'", "?','headache", "\u8179\u75db"),
    ("headache':'", "?','fatigue", "\u5934\u75db"),
    ("fatigue':'", "?','bloating", "\u75b2\u52b3"),
    ("bloating':'", "?','mood", "\u8179\u80c0"),
    ("mood':'", "?','backache", "\u60c5\u7eea\u6ce2\u52a8"),
    ("backache':'", "?'}", "\u8170\u9178"),
]

count = 0
for ctx, crpt, correct in fixes:
    pattern = ctx + crpt
    replacement = ctx + "'" + correct + crpt[-2:]  # crpt[-2:] is the suffix after the value
    if pattern in f:
        f = f.replace(pattern, replacement)
        count += 1
    else:
        # Try with ? varying length
        # Find the context and replace the closest ? pattern
        idx = f.find(ctx)
        if idx >= 0:
            # Find the corrupted value
            val_start = idx + len(ctx) + 1  # skip opening quote
            val_end = f.find("'", val_start)
            if val_end > val_start:
                f = f[:val_start] + correct + f[val_end:]
                count += 1

# Fix longer UI strings in innerHTML
ui_fixes = [
    ("'\u6682\u65e0\u8bb0\u5f55'", 4),  # 暂无记录
    ("'\u6682\u65e0\u6570\u636e'", 4),  # 暂无数据
    ("'\u4eca\u5929\u8fd8\u6ca1\u6709\u8fd0\u52a8'", 7),  # 今天还没有运动
    ("'\u8fd8\u6ca1\u6709\u8bb0\u5f55'", 5),  # 还没有记录
    ("'\u4eca\u65e5\u8fd0\u52a8\uff08\u5206\uff09'", 6),  # 今日运动（分）
    ("'\u672c\u5468\u8fd0\u52a8\uff08\u5206\uff09'", 6),  # 本周运动（分）
    ("'\u7ecf\u671f\u8bb0\u5f55'", 4),  # 经期记录
    ("'\u6700\u8fd1\u7ecf\u671f\u5929\u6570'", 6),  # 最近经期天数
    ("'\u4e0a\u6b21 '", 2),  # 上次
    ("'\u5929\u524d)'", 2),  # 天前)
    ("'\u5f53\u524d\u7ecf\u671f\u4e2d'", 6),  # 当前经期中
    ("'\u5e73\u5747\u5468\u671f'", 4),  # 平均周期
    ("'\u5e73\u5747\u7ecf\u671f'", 4),  # 平均经期
    ("'\u8bb0\u5f55\u6b21\u6570'", 4),  # 记录次数
    ("'\u9884\u6d4b\u4e0b\u6b21'", 4),  # 预测下次
    ("'\u8bf7\u8f93\u5165\u8fd0\u52a8\u65f6\u957f'", 7),  # 请输入运动时长
    ("'\u8bf7\u8f93\u5165\u81ea\u5b9a\u4e49\u8fd0\u52a8\u540d\u79f0'", 10),  # 请输入自定义运动名称
    ("'\u8bf7\u9009\u62e9\u5f00\u59cb\u65e5\u671f'", 7),  # 请选择开始日期
    ("'\u5220\u9664\u8fd9\u6761\u8bb0\u5f55\uff1f'", 7),  # 删除这条记录？
    ("'\u5220\u9664\u8fd9\u6761\u7ecf\u671f\u8bb0\u5f55\uff1f'", 10),  # 删除这条经期记录？
    ("'\u8bb0\u5f55\u8fd0\u52a8'", 4),  # 记录运动
    ("'\u66f4\u65b0\u8fd0\u52a8'", 4),  # 更新运动
    ("'\u8bb0\u5f55\u7ecf\u671f'", 4),  # 记录经期
    ("'\u66f4\u65b0\u8bb0\u5f55'", 4),  # 更新记录
    ("'\u53d6\u6d88\u7f16\u8f91'", 4),  # 取消编辑
    ("'\u7f16\u8f91'", 2),  # 编辑
    # Heatmap header
    ("'\u8fd0\u52a8\u70ed\u529b\u56fe'", 5),  # 运动热力图
    ("'\u603b\u8ba1 '", 2),  # 总计
]

# For UI strings, find corrupted version and replace
for correct, length in ui_fixes:
    corrupted = "'" + "?" * length + "'"
    if corrupted in f:
        f = f.replace(corrupted, correct)
        count += 1

# Fix month labels in heatmap JS
for i in range(1, 13):
    month_name = ['\u4e00\u6708','\u4e8c\u6708','\u4e09\u6708','\u56db\u6708','\u4e94\u6708','\u516d\u6708','\u4e03\u6708','\u516b\u6708','\u4e5d\u6708','\u5341\u6708','\u5341\u4e00\u6708','\u5341\u4e8c\u6708'][i-1]
    corrupted = f"{i}\u6708"  # 1?
    # This is tricky - let me skip this for now

p.write_text(f, encoding="utf-8")
print(f"Fixed {count} corrupted strings")

# Verify
v = p.read_text(encoding="utf-8")
for s in ['\u8dd1\u6b65','\u6682\u65e0\u6570\u636e','\u5e73\u5747\u5468\u671f']:
    print(s, 'OK' if s in v else 'MISSING')

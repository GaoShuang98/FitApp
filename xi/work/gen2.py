import pathlib
# Small test with Chinese
test = "你好世界 暂无数据 平均周期"
pathlib.Path(r"C:\Users\hgs\Documents\Codex\2026-07-01\xi\work\test3.txt").write_text(test, encoding="utf-8")
print("OK")

import time

# 遅い方法 vs 速い方法を比較
n = 100000

# 遅い
start = time.time()
result = ""
for i in range(n):
    result += "a"
print(f"文字連結足し算for文(遅い方法):\n {time.time() - start:.3f}秒")

# 速い
start = time.time()
result = "a" * n
print(f"文字連結掛け算for文使わない(速い方法):\n {time.time() - start:.3f}秒")

# 遅い
start = time.time()
result = 0
for i in range(n):
    result += i
print(f"for文\n 計算結果: {result}, {time.time() - start:.3f}秒")

# 速い
start = time.time()
result, i = 0, 0
while i < n:
    result += i
    i += 1
print(f"while文\n 計算結果: {result}, {time.time() - start:.3f}秒")
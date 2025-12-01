import sys
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
import bisect
import math
input = sys.stdin.readline

# キーポイント
# ・リスト内包表記
# [(変数を使った処理) for (変数名) in (変数を動かす範囲)]
# ・標準入力から数値リストを取得
# [int(item) for item in input().split()]
# ・フィルタリング
# [(変数を使った処理) for (変数名) in (変数を動かす範囲)　if (条件式)]

# ex1. リストへの格納方法
# 方法1 : 従来の for 文
l = []
for i in range(5):
    l.append(i*i)

# 方法2 : リスト内包表記
l2 = [i*i for i in range(5)]

print(l)
print(l2)

# ex2. リスト内包表記例
# 例1. range(3) の要素それぞれに 1 を足す処理をする -> [1,2,3]
l = [hoge+1 for hoge in range(3)]

# 例2. l の要素それぞれに 2 倍する処理をする -> [2,4,6]
l2 = [2*i for i in l]

# 例3. l2 の要素それぞれに、
# 「要素とそれから 1 を引いた値の2要素からなるリストを作る」
# 処理をする -> [[2,1], [4,3], [6,5]]
l3 = [[val, val - 1] for val in l2]

# ex3. 空白区切りを内包表記で取得する方法
# l = [int(item) for item in input().split(",")]
print(sum(l))

# ex4. 組み込み関数に渡す
# a = max([v*v for v in l]) のようにリスト内包表記で作ったリストを
# 関数に渡しても同じ結果になります。この場合リストを作る処理が一度行われるため、
# 計算速度・メモリ使用量が僅かではありますが大きくなります。
l = [-3, -1, 1, 2]
a = max(v*v for v in l)
b = min(v*v for v in l)
c = sum(v*v for v in l)
print(a,b,c)

# ex5. if文によるフィルタリング
l = [3, 1, 4, 1, 5]
l_only_even = [v for v in l if v%2==0]
l_only_odd = [v for v in l if v%2==1]
print(f"偶数：{l_only_even}")
print(f"奇数:{l_only_odd}")

# ex6. 二重ループを伴う内包表記
# 方法1
xs = [1, 2, 3]
ys = ["a", "b", "c"]
xys = []
for x in xs:
    for y in ys:
        xys.append([x,y])
print(xys)

# 方法2
xs = [1, 2, 3]
ys = ["a", "b", "c"]
xys = [[x,y] for x in xs for y in ys]
print(xys)

# 方法3
xs = [1, 2, 3]
ys = ["a", "b", "c"]
xys = [[[x,y] for x in xs] for y in ys]
print(xys)

# 方法4
xys = []
for y in ys:
    xys.append([[x,y] for x in xs])

# ex7
xs = [1,2,3]
ys = [4,5,6]

# 和が3の倍数である (x,y) のリスト
xys_filter = [[x,y] for x in xs for y in ys if (x+y)%3==0]
print(xys_filter)

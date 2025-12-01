import sys
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
import bisect
import math
input = sys.stdin.readline

# キーポイント
# ・二次元配列 a に対して len(a) とすることで a の行数を、
# len(a[0]) とすることで a の列数を取得できる
# ・[list(map(int, input().split())) for _ in range(N)] とすることで行数 
# N の二次元配列を入力から受け取ることができる
# ・[[0]*M for _ in range(N)] とすることですべての値が 0 のサイズ 
# N×M の二次元配列を作ることができる
# ・[[] for _ in range(N)] とすることでサイズ 
# N×0 の二次元配列(空リストを N 個含むリスト)を作ることができる

# ex1. 二重ループと二次元配列
a = [[1, 3, 5], [2, 4, 6]]
for i in range(len(a)):
    print(f"リストの第{i}成分は{a[i]}です。")
    for j in range(len(a[i])):
        print(f"リストの第 ({i}, {j}) 成分は {a[i][j]} です")
        
# ex2. 二次元配列を入力から取得する
# 方法1
# N, M = list(map(int, input().split()))
# a = []
# for i in range(N):
#     a.append(list(map(int, input().split())))

# 方法2
# N, M = list(map(int, input().split()))
# a = [None]*N
# for i in range(N):
#     a[i] = list(map(int, input().split()))

# 方法3
N, M = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(N)]
print(a)

# ex3. 要素がすべて 0 の二次元配列を作る
N = 2
M = 3
a = [[0 for _ in range(M)] for _ in range(N)]
# a = [[0] * M for _ in range(N)] としてもよい
print(a)

# ex4. このコードは不良なので注意すること
# 出力が期待する結果にならない
# この記法では二次元配列内のリストが
# すべて同じ実体を共有するためこのようなことが起こってしまいます。
a = [[0] * 2] * 3
print("更新前:", a) # 更新前: [[0, 0], [0, 0], [0, 0]]
a[0][0] = 1
print("更新後:", a) # 更新後: [[1, 0], [1, 0], [1, 0]]

# ex5. 各要素の長さが異なる二次元配列
a = [[] for _ in range(4)]
a[0].append(10)
a[0].append(20)
a[2].append(30)
a[3].append(40)
a[3].append(50)
a[3].append(60)
print(a)

# ex6. 多次元配列
N = 2
M = 2
D = 2
lst3d = [[[0]*D for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        for k in range(D):
            lst3d[i][j][k] = (i,j,k)
print(lst3d)


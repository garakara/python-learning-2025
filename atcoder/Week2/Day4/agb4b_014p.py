import sys
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
import bisect
import math
input = sys.stdin.readline

# キーポイント
# for 文を使うとループ処理を行うことができる
# range 関数を使うと指定した範囲の処理を行うことができる
# リストの各要素に対して処理を行うこともできる
# enumerate, zip, reversed なども便利

# ex1. range(start, stop)
print("ex1")
for i in range(2, 6):
    print(i, end=" ") # startの変数から開始, stopの数字前で完了

# ex2. range(start, stop, step)
print("\n\nex2")
for i in range(2, 6, 2):
    print(i, end=" ") # startの変数から開始, stopの数字前で完了, step幅で実行
print()

for i in range(2, -6, -2):
    print(i, end=" ") # 第三引数に負の整数を指定可能

# ex3. 文字列に対するfor文
print("\n\nex3")
S = "AtCoder"
for x in S:
    print(x, end=" ")

# ex4. リストのリスト
print("\n\nex4")
L = [[5, 10], [6, 20], [7, 50]]
for a, b in L:
    print("a は", a, "です。 b は", b, "です。")

# ex5. enumerate
# enumerate関数の第二引数がない場合は、インデックスは 0 から始まる
print("\nex5-1")
L = [5, 10]
for i, x  in enumerate(L):
    print(i, "番目 数値 は", x, "です。")
print("\nex5-2")
for i, x  in enumerate(L, 10):
    print(i, "番目 数値 は", x, "です。")

# ex6. リストを逆順に処理
print("\nex6")
L = [5, 10, 6, 80, 7, 50]
for a in reversed(L):
    print(a, end=" ")
    
# ex7. zip複数のリストを同時に前からループ処理したい場合
A = [3, 4, 5, 6, 7]
B = [10, 20, 40, 80, 160]
C = [10, 20, 40, 80, 160, 320]

# A と B から 1 つずつ要素を取得し a および b に格納する
print("\n\nex7-1")
for a, b in zip(A, B):
    print(a - b, end=" ")

# ふたつのリストの長さが異なる場合は短い方が終わるまで処理されます。
print("\n\nex7-2")
for a, b in zip(A, C):
    print(a + b, end=" ")

# ex8. break-else, breakで抜けなかった場合のみelse節が処理される。
print("\n\nex8-1")
for i in range(5):
    if i == 2:
        break
    print(i, end=" ")
else:
    print("else節が処理された")

print("\n\nex8-2")
for i in range(5):
    if i == 7:
        break
    print(i, end=" ")
else:
    print("\nelse節が処理された")

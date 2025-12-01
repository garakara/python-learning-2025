import sys
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
import bisect
import math
input = sys.stdin.readline

# キーポイント
# 関数の中で自身を呼び出すことを 再帰呼び出し と言う
# 再帰呼び出しをする関数を 再帰関数 と言う
# sys.setrecursionlimit で再帰深さの上限を変更できる

# ex1. 再帰関数
# 0 から n までの総和を求める
def sum_triangle(n):
    # 1. ベースケース
    if n == 0:
        return 0             # 0 から 0 までの総和は 0
    # 2. 再帰呼び出し
    s = sum_triangle(n - 1)  # 自身を呼び出して 0 から n-1 までの総和を求める

    # 3. 答えの計算
    return s + n             # n を足して 0 から n までの総和を求める


# ex2. 再帰関数の例（階乗）
# 入力 : 0 以上の整数 n
# 出力 : n の階乗 (1 から n までの総積) を返す
def factorial(n):
    # ベースケース : 0 の階乗は 1, 1 の階乗は 1
    if n == 0 or n == 1:
        return 1

    # 再帰呼び出し : 1 から n-1 までの総積を計算する
    s = factorial(n-1)

    # 答えの計算 : 1 から n までの総積を計算する
    return s * n

# ex3. フィボナッチ数
# 入力 : 0 以上の整数 n
# 出力 : fib(0) = 1, fib(1) = 1, fib(n) = fib(n-1) + fib(n-2) で定められた数列の n 項目を返す
def fib(n):
    # ベースケース : fib(0) = 1, fib(1) = 1
    if n == 0 or n == 1:
        return 1

    # 再帰呼び出し : fib(n-1) と fib(n-2) を計算する
    f1 = fib(n-1)
    f2 = fib(n-2)

    # 答えの計算 : fib(n) を計算する
    return f1 + f2

# ex4. 各桁の和
# 入力 : 0 以上の整数 n
# 出力 : n を 10 進法で表記したときの各桁の和
def digit_sum(n):
    # ベースケース : n が 1 桁ならば、各桁の和は n である
    if n <= 9:
        return n

    # n を 1 の位とそれより上の位に分ける
    ones = n % 10    # 1 の位は、n を 10 で割った余りで得られる
    other = n // 10  # 1 の位を取り除いて左に詰めることは、10 で割って切り捨てることに相当する

    # 再帰呼び出し : 1 より上の位の各桁の和を求める
    s = digit_sum(other)

    # 答えの計算 : 各桁の和を計算
    return s + ones

# ex5
N = int(input())

# p[i] : 組織 i の親組織 
p = [-1] + list(map(int, input().split()))

# 2 次元配列 children
# children[i] : 組織 i の子組織の一覧 であるような 2 次元配列
children = [[] for _ in range(N)]
for i in range(1, N):
    children[p[i]].append(i)

# 再帰関数 complete_time
# 入力 : 組織番号 x
# 出力 : 組織 x に子組織からの報告書が揃った時刻（報告書を親組織へ送った時刻）
def complete_time(x):
    # ここに実装する
    if len(children[x]) == 0:
        return 0
    
    # 子組織が存在する場合
    return max(complete_time(y) + 1 for y in children[x])

# 組織 0 の元に報告書が揃う時刻を出力
print(complete_time(0))


# ex1を実行する
# print(sum_triangle(5))
# ex2を実行する
# print(factorial(5))
# ex3を実行する
# print(fib(5))
# ex4を実行する
# print(digit_sum(175))

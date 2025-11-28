import sys
input = sys.stdin.readline

# 1. 階乗を再帰で書いてみる
def factorial(n):
    # 基底条件: どこで止まるか?
    if n == 0:
        return 1
    # 再帰呼び出し: 自分自身を呼ぶ
    return n * factorial(n - 1)

# 2. フィボナッチ
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# 紙に書いて、どう動くか追ってみる!

def solve(n):
    print(fib(n))

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    solve(n)
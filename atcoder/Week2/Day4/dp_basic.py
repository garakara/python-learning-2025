import time
import sys
input = sys.stdin.readline
n = int(input())

# フィナボッチ（数値が小さい時）
def fib1(n):
    if n <= 1:
        return n
    return fib1(n-1) + fib1(n-2)

# フィナボッチ（数値が大きい時）→　処理時間が長いのでメモを使う
memo = {}
def fib2(n):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    
    memo[n] = fib2(n-1) + fib2(n-2)
    return memo[n]

# フィナボッチ（数値が大きい時）→　処理時間が長いので配列dpを使う
def fib3(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        
        print(dp)
    
    return dp[n]


start = time.time()
fib1(n)
end = time.time()
time_diff = end - start
print(f"fib1の実行時間：{time_diff}") 

start = time.time()
fib2(n)
end = time.time()
time_diff = end - start
print(f"fib2の実行時間：{time_diff}") 

start = time.time()
fib3(n)
end = time.time()
time_diff = end - start
print(f"fib3の実行時間：{time_diff}") 
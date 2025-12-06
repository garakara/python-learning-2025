# DP再入門
memo = {}
def fib(n):
    if n<= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

import time
start = time.time()
print(fib(10))
print(f"{time.time()-start}秒")


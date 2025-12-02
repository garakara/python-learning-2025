import sys
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
import math

input = sys.stdin.readline
N = int(input())

def solve():
    def climb_stairs(n):
        if n <= 2:
            return n
        
        # dp[i] = i段目の上り方
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        
        print(dp)
        
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]

    print(climb_stairs(N))    
solve()
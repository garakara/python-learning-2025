import sys
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
import bisect
import math

def solve():
    # 入力高速化
    input = sys.stdin.readline
    
    # ここに解答コードを書く
    n = int(input())
    P = []
    
    for i in range(n):
        a, b = map(int, input().split())
        # b, a の順でペアにする
        P.append((b, a))
        
    P.sort()
    
    for i, j in P:
        print(j, i)

if __name__ == "__main__":
    solve()
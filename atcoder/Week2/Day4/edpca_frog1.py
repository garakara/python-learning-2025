import sys
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
import bisect
import math
input = sys.stdin.readline


# カエルが足場 
# N に辿り着くまでに支払うコストの総和の最小値を求めてください。
def solve():
    n = int(input())
    A = list(map(int, input().split()))
    
    D = [0] * (n)
    D[-1] = n - 1
    min = 9999
    
    print(D)
    
    def sol(index, D, min):
        # index が配列と一致をするとき
        if index == n:
            # D[0]==1の時は計算を実施
            for i in len(A):
                result += abs()
            if min > result:
                min = result

        # 条件1.Dの配列に1つ飛びで、1を入力する
        sol(index + 1,
            D(int(index)) = n,
            , min)

        # 条件2.Dの配列に2つ飛びで、1を入力する
    

if __name__ == '__main__':
    solve()
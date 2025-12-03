import sys
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
import math

# 問題文
# N日間で報告書を書く。i日目に書ける枚数はa[i]枚。k日連続で書くと疲れて1日休む必要がある。最大何枚書けるか?」
# input: N = 5, k = 2, a = [3, 5, 2, 4, 1]

input = sys.stdin.readline
N = map(int, input().split())
a = [int(x) for x in input().split()]

def max_reports():
    if N == 1:
        print(1)
    else:
        parents = a
        
        # 各組織の子組織リストを作成
        children = [[] for _ in range(N)]
        
    print(children)
    
max_reports()
import sys
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
import math
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
else:
    parents = list(map(int, input().split()))
    
    # 子組織リスト構築
    children = [[] for _ in range(n)]
    for i in range(n - 1):
        children[parents[i]].append(i + 1)
    
    # 再帰関数
    def count_reports(org):
        if not children[org]:
            return 1
        
        total = 1
        for child in children[org]:
            total += count_reports(child)
        
        return total
    
    # 全組織について計算
    for org in range(n):
        print(count_reports(org))
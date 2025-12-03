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
        children[parents[i]].append(i+1)  # ① 何を入れる?
    
    def count_reports(org):
        # 基底条件
        if not children[org]:  # ② 何を入れる?
            return 1  # ③ 何を返す?
        
        total = 1  # ④ 初期値は?
        
        for child in children[org]:
            total += count_reports(child)  # ⑤ 何を渡す?
        
        return total
    
    for org in range(n):
        print(count_reports(org))
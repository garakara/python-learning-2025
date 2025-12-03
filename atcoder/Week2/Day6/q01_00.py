import sys
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
import math
input = sys.stdin.readline

def max_reports():
    N = int(input())
    if N == 1:
        print(1)
    else:
        parents = list(map(int, input().split()))
        
        # 各組織の子組織リストを作成
        children = [[] for _ in range(N)]
        
        for i in range(N-1):
            parent = parents[i]
            child = 1+ i
            children[parent].append(child)
            
        print(f"子組織リスト: {children}")
            
        
    print(children)
    
max_reports()

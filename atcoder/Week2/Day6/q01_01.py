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
    
    # 各組織の子組織リストを作成
    children = [[] for _ in range(n)]
    
    for i in range(n-1):
        parent = parents[i]
        child = 1+ i
        children[parent].append(child)
        
    print(f"子組織リスト: {children}")

def count_reports(org, depth=0):
    indent = " " * depth
    print(f"{indent} -> 組織{org}の報告書を計算")
    
    # 子組織がいない場合
    if not children[org]:
        print(f"{indent} <-組織{org}は葉 ->1枚")
        return 1
    
    # 子組織の報告書を集める
    total = 1
    print(f"{indent} 組織{org}の子: {children[org]}")
    
    for child in children[org]:
        child_reports = count_reports(child, depth+1)
        print(f"{indent} 子組織{child}から{child_reports}枚")
        total += child_reports
    
    print(f"{indent}<- 組織{org}は合計{total}枚")
    return total

# 全組織について計算
results = []
for org in range(n):
    print(f"\n=== 組織{org} ===")
    count = count_reports(org)
    results.append(count)
    
print("\n結果")
for i, count in enumerate(results):
    print(count)
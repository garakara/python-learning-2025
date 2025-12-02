import sys
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
import math

# 問題文
# N日間で報告書を書く。i日目に書ける枚数はa[i]枚。k日連続で書くと疲れて1日休む必要がある。最大何枚書けるか?」
# input: N = 5, k = 2, a = [3, 5, 2, 4, 1]

input = sys.stdin.readline
N, k = map(int, input().split())
a = [int(x) for x in input().split()]

def max_reports(day, consective_days):
    # 配列最後まで実行を続ける
    if day > N-1:
        return 0
    
    # 連続日数達成しない場合は、その日の報告書の枚数を書いて、次の関数に引き継ぐ
    # 連続する場合は、その次の日の報告書をカウントするように、次の関数に引き継ぐ必要あり
    if consective_days < k :
        choice1 = a[day] + max_reports(day+1, consective_days+1)
    else:
        choice1 = 0
        
    choice2 = max_reports(day+1, 0)

    return max(choice1, choice2)
        
print(max_reports(0, 0))
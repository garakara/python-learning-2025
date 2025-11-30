# 高速化
import sys
input = sys.stdin.readline
import bisect

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# 各列を並び替えする
A.sort()
B.sort()
C.sort()

total = 0

# 配列Bを基準とする
for b in B:
    
    # 配列Aから「bより小さい要素の個数」
    count_a = bisect.bisect_left(A, b)

    # 配列Cから「bより大きい要素の個数」
    count_c = len(B) - bisect.bisect_right(C, b)
    
    total += count_a * count_c

print(total)
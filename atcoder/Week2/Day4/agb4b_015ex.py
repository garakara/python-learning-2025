import sys
input = sys.stdin.readline

N, S = map(int, input().split())
A = list(map(int, input().split()))
P = list(map(int, input().split()))

cnt = 0

for a in A:
    for p in P:
        if a + p == S:
            cnt += 1
            
print(cnt)
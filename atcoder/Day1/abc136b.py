import sys

input = sys.stdin.readline
n = int(input())
i, cnt = 0, 0

while i <= n:
    if 0 < i and i < 10:
        cnt += 1
    elif 100 <= i and i <= 999:
        cnt += 1
    elif 10000 <= i and i <= 99999:
        cnt += 1
    i += 1
    
print(cnt)
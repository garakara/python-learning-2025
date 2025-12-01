import sys
input = sys.stdin.readline

li = list(map(int, input().split()))
judge = "NO"

for i in range(len(li)-1):
    if li[i+1] == li[i]:
        judge = "YES"
        break

print(judge)
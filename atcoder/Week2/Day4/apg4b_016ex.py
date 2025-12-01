import sys
input = sys.stdin.readline

N, K = [int(x) for x in input().split()]
S = input().split()
        
result = [s for s in S if len(s)>=K]

for word in result:
    print(word, end=" ")
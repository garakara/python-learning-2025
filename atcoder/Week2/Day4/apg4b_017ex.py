import sys
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
import bisect
import math
input = sys.stdin.readline

N, M = [int(x) for x in input().split()]
A = [list(map(int, input().split())) for _ in range(M)]

R = [["-" for _ in range(N)] for _ in range(N)]
for i, j in A:
    R[i-1][j-1] = "o"
    R[j-1][i-1] = "x"

for k in R:
    for j in range(len(R)):
        print(k[j], end=" ")
    print()

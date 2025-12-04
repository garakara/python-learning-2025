import sys
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
import math

input = sys.stdin.readline

def solve():
    N, M = list(map(int, input().split()))
    total = 0

    for i in range(M+1):
        total += N ** i
    
    if total > 10 ** 9:
        return "inf"
    
    return total
    
if __name__ == '__main__':
    print(solve())
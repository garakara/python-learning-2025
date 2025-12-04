import sys
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
import math

input = sys.stdin.readline

def solve():
    data = -1
    n = int(input())
    if 400 % n == 0:
        data = 400 // n
    
    return data
        
if __name__ == '__main__':
    print(solve())
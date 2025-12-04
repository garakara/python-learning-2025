import sys
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
import math

s = input()
N = list(map(int, s))

def dfs(index, result, exp):
    if index == 4:
        if result == 7:
            print(exp + "=7")
            return True
        False
        
    # +のケース
    if dfs(index+1, result+N[index], exp + "+" + str(N[index])):
        return True
    # -のケース
    if dfs(index+1, result-N[index], exp + "-" + str(N[index])):
        return True
    False    
dfs(1, N[0], str(N[0]))


import sys
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
import math

que = deque()

s = input()
for i in s:
    if i == "0":
        que.append(0)
    elif i == "1":
        que.append(1)
    else:
        if len(que) != 0:
            que.pop()
        
for j in que:
    print(j, end="")
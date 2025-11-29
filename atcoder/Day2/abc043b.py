from collections import deque
import sys
input = sys.stdin.readline

def solve():
    s = input().strip()
    digits = [d for d in s]

    queue = deque()
    
    for i in digits:
        if i == "0":
            queue.append(0)
        elif i == "1":
            queue.append(1)
        elif i == "B":
            if queue:
                queue.pop()
    
    for j in queue:
        print(j, end="")

if __name__ == '__main__':
    solve()
    

from collections import deque

que = deque()
N = int(input())

for _ in range(N):
    word = [int(x) for x in input().split()]
    
    if word[0] == 1:
        que.append(word[1])
    if word[0] == 2:
        print(que.popleft())
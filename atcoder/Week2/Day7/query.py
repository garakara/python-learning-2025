# from collections import deque

# n = int(input())
# que = deque()

# for _ in range(n):
#     a = [int(x) for x in input().split()]
#     if a[0] == 1:
#         que.append(a[1])
#     elif a[0] == 2:
#         que.pop()
        
#     for i, j in enumerate(que):
#         if i == len(que) - 1:
#             print(j)
#         else:
#             print(j, end=" ")

n = int(input())
que = []

for _ in range(n):
    a = input().split()
    if a[0] == "1":
        que.append(a[1])
    elif a[0] == "2":
        que.pop()
        
    print(" ".join(que))

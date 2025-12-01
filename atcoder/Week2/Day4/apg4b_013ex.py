import sys
input = sys.stdin.readline

def solve_ex13(li):
    result = 1
    for j in li:
        result *= sum(j)

    print(result)

li = []
num = 3
N = int(input())

for i in range(num):
    li.append(list(map(int, input().split())))

solve_ex13(li)
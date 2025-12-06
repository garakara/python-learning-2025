X = int(input())
N = int(input())
W = [int(x) for x in input().split()]
lib = []
Q = int(input())
for i in range(Q):
    P = int(input())
    if P not in lib:
        X += W[P-1]
        lib.append(P)
        print(X)
    elif P in lib:
        X -= W[P-1]
        lib.remove(P)
        print(X)
        
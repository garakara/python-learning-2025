import bisect

N = input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

total = 0

for b in B:
    cnt1 = bisect.bisect_left(A, b)
    cnt2 = len(B) - bisect.bisect_right(C, b)

    total += cnt1 * cnt2
        
print(total)
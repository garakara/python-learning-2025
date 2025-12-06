# TLEで不完全状態

N, M, K = [int(x) for x in input().split()]
H = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0

H.sort()
B.sort()

def dfs(H ,B, cnt):
    # 配列が無くなったら終わり
    if not H or not B:
        return cnt
    
    # H > B の時
    if dfs(H, B.pop(0), cnt):
        return True
    
    # H <= B の時
    if dfs(H.pop(0), B.pop(0), cnt+1):
        return True
    
dfs(H,B,0)

if cnt >= K:
    print("Yes")
else:
    print("No")
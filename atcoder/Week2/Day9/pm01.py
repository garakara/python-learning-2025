N, M = list(map(int, input().split()))
checker = 1000000007
a = []
dp = [0] * (N+1)
dp[0] = 1
flag = True

# 罠の位置を格納
for _ in range(M):
    k = int(input())
    a.append(k)

for i in range(N+1):
    # 罠の番号と一致
    if i in a:
        continue
    
    if i + 1 <= N and i + 1 not in a:
        dp[i+1] = (dp[i+1]+dp[i]) % checker
        
    if i + 2 <= N and i + 2 not in a:
        dp[i+2] = (dp[i+2]+dp[i]) % checker
    
print(dp)
# if flag:
#     print(dp)
# else:
#     print(0)
n, m = list(map(int, input().split()))
broken = set(int(input()) for _ in range(m))
MOD = 1000000007

print(broken)

dp = [0] * (n + 1)
dp[0] = 1

for i in range(n+1):
    if i in broken:
        continue
    
    if i + 1 <= n and i + 1 not in broken:
        dp[i + 1] = (dp[i + 1] + dp[i]) % MOD
    
    if i + 2 <= n and i + 2 not in broken:
        dp[i + 2] = (dp[i + 2] + dp[i]) % MOD
        
print(dp[n])
        
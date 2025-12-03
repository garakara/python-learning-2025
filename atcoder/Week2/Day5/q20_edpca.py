n = int(input())
h = list(map(int, input().split()))

dp = [float('inf')] * n
dp[0] = 0

for i in range(n):
    if i + 1 < n:
        cost = abs(h[i+1] - h[i])
        dp[i+1] = min(dp[i+1], dp[i] + cost)
        
    if i + 2 < n:
        cost = abs(h[i+2] - h[i])
        dp[i+1] = min(dp[i+2], dp[i] + cost)

    print(dp)

        
print(dp[n-1])

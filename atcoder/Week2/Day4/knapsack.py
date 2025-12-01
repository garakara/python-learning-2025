# 問題: N個の品物、重さw[i]、価値v[i]
# 容量Wのナップサックに入れる最大価値

def knapsack(N, W, w, v):
    # dp[i][j] = i番目までの品物で重さj以下の最大価値
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        for j in range(W + 1):
            # 選ばない
            dp[i][j] = dp[i-1][j]
            
            # 選ぶ(入る場合)
            if j >= w[i-1]:
                dp[i][j] = max(dp[i][j], 
                               dp[i-1][j-w[i-1]] + v[i-1])
    
    return dp[N][W]

N, W = [int(x) for x in input().split()]


print(N,W,w,v)
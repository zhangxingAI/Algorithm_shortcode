n,k = map(int,input().split())

dp = [[0] * (k+1) for _ in range(n+1)]
for j in range(1, k+1):
    dp[1][j] = 1

for i in range(2, n+1):
    for j in range(1, k+1):
        for l in range(1,k+1):
            if l!=j:
                dp[i][j] += dp[i -1][l]

print(sum(dp[n][1:k+1]))
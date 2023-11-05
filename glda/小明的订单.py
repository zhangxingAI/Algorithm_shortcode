n = int(input())
s = list(map(int, input().split(' ')))
t = list(map(int, input().split(' ')))
a = list(map(int, input().split(' ')))
end = [0 for i in range(n+1)]
for i in range(1,n+1):
    end[i] = s[i-1]+t[i-1]
total = max(end)
dp = [[0 for i in range(total + 1)] for j in range(n+1)]

for i in range(n):
    for j in range(0,total+1):
        if j == s[i]+t[i]:
            dp[i][j] = max(dp[i - 1][j - t[i]] + a[i], dp[i - 1][j])
        else :
            dp[i][j] = dp[i][j-1]

print(dp[n-1][total])
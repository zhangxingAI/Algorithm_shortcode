
# 处理输入
n = int(input())
T = int(input())
a = [int(x) for x in input().split(" ")]
a = sorted(a)
dp = [0 for x in range(n+1)]
c1 = [0 for x in range(n+1)]
c2 = [0 for x in range(n+15)]
if n == 1:
    print(a[0])
elif n == 2:
    print(min(10*a[0],a[1]))
else:
    dp[1] = a[0]
    dp[2] = a[1]
    pre = n
    for i in range(3, n + 1):
        c1[i] = dp[i - 2] + a[0] + a[i - 1] + a[1] + a[1]
        c2[i] = dp[i - 1] + a[0] + min(a[i - 1], 10 * a[0])
        dp[i] = min(c1[i], c2[i])
        if (dp[i] > T):
            pre = i - 1
            break
    print(pre, dp[pre])
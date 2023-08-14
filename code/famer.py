def max_satisfaction(n, m, benefits):
    dp = [[0] * (m+2) for _ in range(n+2)]

    # 动态规划求解
    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(i):
                dp[i][j] = max(dp[i][j], dp[k][j-1] + benefits[i][j])

    # 寻找最大满意度
    max_satisfaction = 0
    for j in range(1, m+1):
        for i in range(1, n+1):
            max_satisfaction = max(max_satisfaction, dp[i][j])

    return max_satisfaction

# 读取输入
n, m = map(int, input().split())
distances = list(map(int, input().split()))
benefits = []
for _ in range(n):
    row = list(map(int, input().split()))
    benefits.append(row)

# 求解最大满意度
result = max_satisfaction(n, m, benefits)

# 输出结果
print(result)

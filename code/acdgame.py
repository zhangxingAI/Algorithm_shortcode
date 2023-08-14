def min_steps(n, q, sequence, queries):
    dp = [[float('inf')] * (10**5 + 1) for _ in range(n+2)]

    for i in range(1, n+1):
        for j in range(1, 10**5 + 1):
            if i > 1 and j % sequence[i-1] == 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j//sequence[i-1]])
            if i < n and j % sequence[i+1-1] == 0:
                dp[i][j] = min(dp[i][j], dp[i+1][j//sequence[i+1-1]])

    # 处理初始状态的特殊情况
    for i in range(1, n+1):
        dp[i][sequence[i-1]] = 0
        if i > 1 and sequence[i-2] % sequence[i-1] == 0:
            dp[i][sequence[i-2]] = 0
        if i < n and sequence[i] % sequence[i-1] == 0:
            dp[i][sequence[i]] = 0

    result = []
    for query in queries:
        x, y = query
        result.append(min(dp[x][y], dp[y][x]))

    return result

# 示例输入
n, q = map(int, input().split())
sequence = list(map(int, input().split()))
queries = []
for _ in range(q):
    query = tuple(map(int, input().split()))
    queries.append(query)

# 调用函数并输出结果
result = min_steps(n, q, sequence, queries)
for res in result:
    print(res)

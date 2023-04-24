import sys

def solve(M, N, K, trap):
    # 初始化桥
    bridge = [0] * (N + 2)
    # 标记陷阱
    for i in range(K):
        bridge[trap[i]] = 1

    # 初始化dp数组
    dp = [[0] * (M + 2) for _ in range(N + 2)]

    dp[0][M] = 1

    # 动态规划
    for i in range(1, len(dp)):
        for j in range(M+1):
            # 如果当前位置是陷阱，则不能跳到下一个位置
            k = j + bridge[i]
            if i == 1:
                dp[i][j] = dp[i - 1][k]
            elif i == 2:
                dp[i][j] = dp[i - 1][k] + dp[i - 2][k]
            else:
                dp[i][j] = dp[i - 1][k] + dp[i - 2][k] + dp[i - 3][k]

    # 统计方案数
    res = sum(dp[N + 1][:M+1])
    return res

if __name__ == "__main__":
    # 读入数据
    M, N, K = map(int, input().split())
    trap = list(map(int, input().split()))
    # 求解并输出结果
    s = solve(M, N, K, trap)
    print(s)

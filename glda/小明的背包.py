'''
小明的背包
题目描述
小明有一个容量为 V 的背包。

这天他去商场购物，商场一共有 N 件物品，第 i 件物品的体积为 $w_i$，价值为 $v_i$。

小明想知道在购买的物品总体积不超过 V 的情况下所能获得的最大价值为多少，请你帮他算算。

输入描述
输入第 1 行包含两个正整数 N,V，表示商场物品的数量和小明的背包容量。

第 $2\sim N+1$ 行包含 2 个正整数 w,v，表示物品的体积和价值。

$1\leq N\leq10^2$，$1\leq V \leq 10^3$，$1 \leq w_i,v_i \leq10^3$。

输出描述
输出一行整数表示小明所能获得的最大价值。

样例输入
5 20
1 6
2 5
3 8
5 15
3 3
样例输出
37

'''
n, v = map(int, input().split())
volumes = []
values = []
for i in range(n):
    volume, value = map(int, input().split())
    volumes.append(volume)
    values.append(value)

# ----递归----
# dp = [[0 for i in range(v + 1)] for j in range(n + 1)]
# for i in range(0, n + 1):
#     for j in range(0, v + 1):
#         # 当回溯的时候，是有可能为0的，所以要从0开始
#         # 接下来就是判断选不选第i件商品
#         if volumes[i] > j:
#             dp[i][j] = dp[i - 1][j]
#         else:
#             dp[i][j] = max(dp[i - 1][j - volumes[i]] + values[i], dp[i - 1][j])
#             # 对选还是不选做出比较
#
# print(dp[n][v])

# ----滚动-----
# dp = [0 for i in range(v + 1)]
# # i表示第i件商品选不选，j表示背包此状态下的容积，i件商品的容积之和不能大于它
#
# for i in range(1, n + 1):
#     for j in range(v, volumes[i], -1):
#         dp[j] = max(dp[j - volumes[i]] + values[i], dp[j])
#         # 对选还是不选做出比较
#
# print(dp[v])

# -----交替-----
dp = [[0] * (v + 1) for _ in range(2)]
old = 0
new = 1

for i in range(1, n + 1):
    old, new = new, old
    for j in range(0, v + 1):
        if volumes[i - 1] > j:
            dp[new][j] = dp[old][j]
        else:
            dp[new][j] = max(dp[old][j - volumes[i-1]] + values[i-1], dp[old][j])

print(dp[new][v])
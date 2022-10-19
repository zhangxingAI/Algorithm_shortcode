'''
给定一个按 非递减顺序 排列的数字数组 digits 。你可以用任意次数 digits[i] 来写的数字。例如，如果 digits = ['1','3','5']，我们可以写数字，如 '13', '551', 和 '1351315'。
返回 可以生成的小于或等于给定整数 n 的正整数的个数 。

示例 1：

输入：digits = ["1","3","5","7"], n = 100
输出：20
解释：
可写出的 20 个数字是：
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
示例 2：

输入：digits = ["1","4","9"], n = 1000000000
输出：29523
解释：
我们可以写 3 个一位数字，9 个两位数字，27 个三位数字，
81 个四位数字，243 个五位数字，729 个六位数字，
2187 个七位数字，6561 个八位数字和 19683 个九位数字。
总共，可以使用D中的数字写出 29523 个整数。
示例 3:

输入：digits = ["7"], n = 8
输出：1
'''


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        m = len(digits)
        s = str(n)
        k = len(s)
        dp = [[0,0] for _ in range(k)]
        dp[0][0] = sum(i<s[0] for i in digits)
        for i in digits:
            if i == s[0]:
                dp[0][1] = 1
                break
            else:
                dp[0][1] = 0
        for i in range(1,k):
            for d in digits:
                if d == s[i] and dp[i-1][1] == 1:
                    dp[i][1] = dp[i-1][1]
                    break
                else:
                    dp[i][1] = 0
            dp[i][0] = dp[i-1][0] * m + dp[i-1][1] * sum(j<s[i] for j in digits) +m
        return sum(dp[k-1])

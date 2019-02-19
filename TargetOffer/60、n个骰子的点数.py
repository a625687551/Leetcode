# -*- coding:utf-8 -*-
"""
把n个骰子扔在地上，所有骰子朝上一面的点数之和为S。输入n，打印出S所有可能的值出现的概率
"""


class Solution:
    def max_dice_point(self, n):
        if n < 1:
            return None
        dp = [[0 for x in range(6 * n)] for y in range(n)]
        for i in range(6):
            dp[0][i] = 1
        for i in range(1, n):
            for j in range(i, 6 * (i + 1)):
                dp[i][j] = dp[i - 1][j - 6] + dp[i - 1][j - 5] + dp[i - 1][j - 4] + dp[i - 1][j - 3] + dp[i - 1][
                    j - 2] + dp[i - 1][j - 1]
        count = dp[n-1]
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.max_dice_point(1))
    print(s.max_dice_point(3))

# -*- coding:utf-8 -*-
"""
把n个骰子扔在地上，所有骰子朝上一面的点数之和为S。输入n，打印出S所有可能的值出现的概率

第一步，确定问题解的表达式。可将f(n, s) 表示n个骰子点数的和为s的排列情况总数。
第二步，确定状态转移方程。n个骰子点数和为s的种类数只与n-1个骰子的和有关。因为一个骰子有六个点数，
那么第n个骰子可能出现1到6的点数。所以第n个骰子点数为1的话，f(n,s)=f(n-1,s-1)，当第n个骰子点数为2的话，f(n,s)=f(n-1,s-2)，
…，依次类推。在n-1个骰子的基础上，再增加一个骰子出现点数和为s的结果只有这6种情况！那么有：

f(n,s)=f(n-1,s-1)+f(n-1,s-2)+f(n-1,s-3)+f(n-1,s-4)+f(n-1,s-5)+f(n-1,s-6) ，0< n<=6n
f(n,s)=0, s< n or s>6n
https://blog.csdn.net/k346k346/article/details/50988681
"""
import numpy as np


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
        count = dp[n - 1]
        return count

    def max_dice_point_2(self, n):
        if n < 1:
            return 0
        dice = np.zeros((n, 6 * n), int)
        for i in range(6):
            dice[0][i] = 1
        for i in range(1, n):
            for j in range(i, 6 * (i + 1)):
                dice[i][j] = dice[i - 1][j - 1] + dice[i - 1][j - 2] + dice[i - 1][j - 3] + dice[i - 1][j - 4] + \
                             dice[i - 1][j - 5] + dice[i - 1][j - 6]

        return dice[-1]


if __name__ == '__main__':
    s = Solution()
    # print(s.max_dice_point(1))
    print(s.max_dice_point(3))
    print(s.max_dice_point_2(3))
    print(s.max_dice_point_2(6))
    # print(s.max_dice_point(5))

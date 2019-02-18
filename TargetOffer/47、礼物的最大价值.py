# -*- coding:utf-8 -*-
"""
在一个m*n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值〈价值大于 0).  你可以从棋盘的左上角开始拿格子里的礼物，井
每次向左或者向下移动一格，直到到达棋盘的右下角。给定一个棋盘及其上面的礼物，计算你最多能拿到多少价值的礼物?
动态规划问题
"""
import numpy as np


class Solution:
    def max_worth_gift(self, numbers):
        if not numbers:
            return 0
        rows = len(numbers)
        cols = len(numbers[0])
        max_value = np.ones((rows, cols))
        for i in range(rows):
            for j in range(cols):
                left, up = 0, 0
                if i > 0:
                    up = max_value[i - 1][j]
                if j > 0:
                    left = max_value[i][j - 1]
                max_value[i][j] = max(up, left) + numbers[i][j]
        print(max_value)
        return max_value[rows - 1][cols - 1]


if __name__ == '__main__':
    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    arr1 = [[1, 10, 3, 8],
            [12, 2, 9, 6],
            [5, 7, 4, 11],
            [3, 7, 16, 5]]
    s = Solution()
    # print(s.max_worth_gift(arr1))
    print(s.max_worth_gift(array))

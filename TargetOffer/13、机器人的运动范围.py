# -*- coding:utf-8 -*-
"""
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
"""

from functools import reduce

"""
目前这个算法有问题，不对
"""


class Solution:
    def __init__(self):
        self.vis = {}

    def movingCount(self, threshold, rows, cols):
        if threshold < 0 or rows < 0 or cols < 0:
            return 0
        return self.moving(threshold, rows, cols, 0, 0)

    def moving(self, threshold, rows, cols, row, col):
        if row >= rows or col >= cols or row < 0 or col < 0:
            return 0
        if reduce(lambda x, y: x + y, [int(x) for x in (str(row) + str(col))]) > threshold:
            return 0
        if (row, col) in self.vis:
            return 0
        self.vis[(row, col)] = 1
        return 1 + self.moving(threshold, rows, cols, row - 1, col) + self.moving(threshold, rows, cols, row + 1, col) \
               + self.moving(threshold, rows, cols, row, col - 1) + self.moving(threshold, rows, cols, row, col + 1)


if __name__ == '__main__':
    s = Solution()
    print(s.movingCount(6, 10, 10))
    print(s.movingCount(6, 4, 4))
    print(s.movingCount(18, 40, 40))

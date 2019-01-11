# -*- coding:utf-8 -*-

"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下
4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""


class Solution:
    def printMatrix(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        res = []
        if not row and not col:
            return res
        left, top, right, bottom = 0, 0, col - 1, row - 1
        while left <= right and top <= bottom:
            # left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            # top to bottom
            for i in range(top + 1, bottom + 1):
                res.append(matrix[i][right])
            # right to left
            if top != bottom:
                for i in range(right - 1, left-1, -1):
                    res.append(matrix[bottom][i])
            # bottom to top
            if left != right:
                for i in range(bottom - 1, top, -1):
                    res.append(matrix[i][left])
            left += 1
            top += 1
            right -= 1
            bottom -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.printMatrix([[1]]))
    print(s.printMatrix([[1, 2],
                         [3, 4]]))
    print(s.printMatrix([[1, 2, 3, 4],
                         [5, 6, 7, 8],
                         [9, 10, 11, 12],
                         [13, 14, 15, 16]]))

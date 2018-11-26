# -*- coding:utf-8 -*-
"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""
class Solution:
    def max_worth_gift(self, numbers):
        if not numbers:
            return 0
        rows = len(numbers)
        cols = len(numbers[0])
        max_value = 0
        for i in range(rows):
            for j in range(cols):
                left = numbers[i][j+1]
                bottom = numbers[i+i][j]
                



if __name__ == '__main__':
    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    s = Solution()
    print(s.max_worth_gift([5, 7, 6, 9, 11, 10, 8]))
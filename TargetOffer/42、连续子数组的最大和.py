# -*- coding:utf-8 -*-

"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变
PS 比较坑的是这个要求相对位置不能变化
"""


class Solution:
    def max_sum_array(self, array):
        if not array:
            return 0
        res = []
        middle_sum = 0
        for x in array:
            if middle_sum <= 0:
                middle_sum = x
            else:
                middle_sum += x
            if not res or middle_sum > res[-1]:
                res.append(middle_sum)
            else:
                res.append(res[-1])
        print(res)
        return max(res)

    def max_sum_array_1(self, array):
        """动态规划"""
        if not array:
            return 0
        res = []
        for i, v in enumerate(array):
            if i == 0 or res[-1] <= 0:
                res.append(v)
            else:
                res.append(res[-1] + v)
        print(res)
        return max(res)

if __name__ == '__main__':
    s = Solution()
    # print(s.max_sum_array([4, 5, 6, 7, 8]))
    print(s.max_sum_array_1([1, -2, 3, 10, -4, 7, 2, -5]))
    print(s.max_sum_array_1([-1, -2, -3, -10, -4, -7, -2, -5]))

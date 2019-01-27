# -*- coding:utf-8 -*-

"""
输入一个整数数组，数组里面有正数也有负数。数组中的一个或者连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)
PS 比较坑的是这个要求相对位置不能变化
思路：
1、枚举法：
2、动态规划法：
"""


class Solution:
    def max_sum_array(self, array):
        """动态规划"""
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
    print(s.max_sum_array([1, -2, 3, 10, -4, 7, 2, -5]))
    # print(s.max_sum_array([-1, -2, -3, -10, -4, -7, -2, -5]))
    print(s.max_sum_array_1([1, -2, 3, 10, -4, 7, 2, -5]))
    # print(s.max_sum_array_1([-1, -2, -3, -10, -4, -7, -2, -5]))

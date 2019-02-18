# !usr/bin/env python
# -*- coding: utf-8 -*-

"""
一、统计一个数字在排序数组中出现的次数。
二、0到n-1中缺失的数字
"""


class Solution:
    def __init__(self):
        self.stack = []

    def get_number_k_count(self, data, k):
        """直接调用库"""
        if not data:
            return 0
        return data.count(k)

    def get_number_k(self, data, k):
        """二分查找，查找数字的次数,这个重要的是要处理好边界问题"""
        left, right = 0, len(data) - 1
        firt_k = self.get_first_k(data, k, left, right)
        last_k = self.get_last_k(data, k, left, right)
        return last_k - firt_k + 1

    def get_first_k(self, data, k, left, right):
        while left <= right:
            middle = (left + right) // 2
            if data[middle] < k:
                left = middle + 1
            else:
                right = middle - 1
        return left

    def get_last_k(self, data, k, left, right):
        while left <= right:
            middle = (left + right) // 2
            if data[middle] <= k:
                left = middle + 1
            else:
                right = middle - 1
        return right


if __name__ == '__main__':
    s = Solution()
    print(s.get_number_k([1, 2, 3, 3, 3, 3, 4, 5], 6))
    print(s.get_number_k([1, 2, 3, 3, 3, 3, 4, 5], 3))
    print(s.get_number_k([1, 1, 1, 1, 1, 1, 1], 1))
    print(s.get_number_k_count([1, 2, 3, 3, 3, 3, 4, 5], 3))

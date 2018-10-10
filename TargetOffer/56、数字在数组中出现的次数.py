# -*- coding:utf-8 -*-

"""
统计一个数字在排序数组中出现的次数。
排序直接上二分
目前这个排序有问题
"""


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        first = self.find_first(data, k)
        last = self.find_last(data, k)
        return last - first + 1

    def find_first(self, data, k):
        start, end = 0, len(data) - 1
        while start <= end:
            mid = (start + end) // 2
            if data[mid] == k and (mid == 0 or data[mid] != data[mid - 1]):
                return mid
            elif data[mid] < k:
                start = mid + 1
            else:
                end = mid - 1
        return mid

    def find_last(self, data, k):
        start, end = 0, len(data) - 1
        while start <= end:
            mid = (start + end) // 2
            if data[mid] == k and (mid == len(data) - 1 or data[mid] != data[mid + 1]):
                return mid
            elif data[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
        return mid


if __name__ == '__main__':
    s = Solution()
    print(s.GetNumberOfK([1, 2, 3, 4, 5, 6, 6, 7, 7], 6))

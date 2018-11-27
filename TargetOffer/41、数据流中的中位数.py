# !usr/bin/env python
# -*- coding: utf-8 -*-

"""
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，
使用GetMedian()方法获取当前读取数据的中位数。
"""
import _heapq


class Solution:
    def __init__(self):
        self.left = []
        self.right = []

    def insert_num(self, num):
        if not self.left or num <= -self.left[0]:
            _heapq.heappush(self.left, -num)
        else:
            _heapq.heappush(self.right, num)
        if len(self.left) > len(self.right) + 1:
            tmp = - _heapq.heappop(self.left)
            _heapq.heappush(self.right, tmp)
        elif len(self.right) > len(self.left) + 1:
            tmp = - _heapq.heappop(self.right)
            _heapq.heappush(self.left, tmp)

    def get_median(self):
        if len(self.left) == len(self.right):
            return (float(-self.left[0]) + self.right[0])/2
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]


if __name__ == '__main__':
    l = [2, 3, 1, 0, 2, 5, 3]
    s = Solution()
    for x in l:
        s.insert_num(x)
        print(s.get_median())


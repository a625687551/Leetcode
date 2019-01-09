# coding: utf-8

import heapq
from functools import reduce


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        # max heap
        self.left = []
        self.right = []
        self.stack = []
        self.vis = {}

    def solution_over(self, data):
        return self.inverse_count(data[:], 0, len(data) - 1, data[:]) % 1000000

    def inverse_count(self, tmp, start, end, data):
        if end - start < 1:
            return 0
        if end - start == 1:
            if data[start] <= data[end]:
                return 0
            else:
                tmp[start], tmp[end] = data[end], data[start]
                return 1
        mid = (start + end) // 2
        cnt = self.inverse_count(data, start, mid, tmp) + self.inverse_count(data, mid + 1, end, tmp)
        i = start
        j = mid + 1
        ind = start
        while (i <= mid and j <= end):
            if data[i] <= data[j]:
                tmp[ind] = data[i]
                i += 1
            else:
                tmp[ind] = data[j]
                cnt += mid - i + 1
                j += 1
            ind += 1
        while i <= mid:
            tmp[ind] = data[i]
            i += 1
            ind += 1
        while j <= end:
            tmp[ind] = data[j]
            j += 1
            ind += 1
        return cnt


if __name__ == '__main__':
    l = [2, 3, 1, 0, 2, 5, 3]
    l2 = [1, 1, 1, 1, 1, 1, 1]

    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    s = Solution()
    s = Solution()
    # print(s.solution_over([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    print(s.solution_over(l))
    # print(s.solution_over([7, 5, 6, 4]))

# coding: utf-8

import heapq
import numpy as np
import random

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
        self.index = -1
        self.left = []
        self.right = []
        self.stack = []
        self.vis = {}

    def solution(self, index):
        if index <= 0:
            return 0
        ugly_list = [1]
        time_2, time_3, time_5 = 0, 0, 0
        for i in range(index-1):
            ug_new = min(ugly_list[time_2] * 2, ugly_list[time_3] * 3, ugly_list[time_5] * 5)
            ugly_list.append(ug_new)
            if ug_new % 2 == 0:
                time_2 += 1
            if ug_new % 3 == 0:
                time_3 += 1
            if ug_new % 5 == 0:
                time_5 += 1
        return ugly_list[-1]


if __name__ == '__main__':
    l = [2, 3, 1, 0, 2, 5, 3]
    l2 = [1, 1, 1, 1, 1, 1, 1]

    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]

    s = Solution()
    # print(s.solution_over([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    print(s.solution(10))
    # t = [31, 16, 46, 9, 8]
    # print([random.randint(1, 65) for _ in range(5)])

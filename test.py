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
        if index <= 0 or not index:
            return 0
        ugly_list = [1]
        t2, t3, t5 = 0, 0, 0
        for i in range(index - 1):
            ugly_new = min(ugly_list[t2] * 2, ugly_list[t3] * 3, ugly_list[t5] * 5)
            ugly_list.append(ugly_new)
            if ugly_new % 2 == 0:
                t2 += 1
            if ugly_new % 3 == 0:
                t3 += 1
            if ugly_new % 5 == 0:
                t5 += 1
        return ugly_list


if __name__ == '__main__':
    l = [2, 3, 1, 0, 2, 5, 3]
    l2 = [1, 1, 1, 1, 1, 1, 1]

    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    matrix = [['A', 'B', 'C', 'E', 'H', 'J', 'I', 'G'],
              ['S', 'F', 'C', 'S', 'L', 'O', 'P', 'Q'],
              ['A', 'D', 'E', 'E', 'M', 'N', 'O', 'E'],
              ['A', 'D', 'I', 'D', 'E', 'J', 'F', 'M'],
              ['V', 'C', 'E', 'I', 'F', 'G', 'G', 'S']]
    way = ['S', 'L', 'H', 'E', 'C', 'C', 'E', 'I', 'D', 'E', 'J', 'F', 'G', 'G', 'F', 'I', 'E']

    s = Solution()
    # print(s.solution_over([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    print(s.solution(10))
    b = [12, 13, 14, 17, 19, 38]
    a = [12, 13, 14, 17, 19, 38, 42, 43, 44, 45, 46, 47, 48, 49, 51, 53, 57, 58, 59, 60, 61, 62, 63, 70]

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

    def solution(self, num1, num2):
        while num2 != 0:
            sum_two = num1 ^ num2
            carray = (num1 & num2) << 1
            num1 = sum_two
            num2 = carray
        return num1



if __name__ == '__main__':
    l = [2, 3, 1, 0, 2, 5, 3]
    l2 = [1, 1, 1, 1, 1, 1, 1]

    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    s = Solution()
    # print(s.solution_over([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    # print(s.solution(7, array))
    t = [65, 47, 54]
    # print([random.randint(1, 65) for _ in range(5)])

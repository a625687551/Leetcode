# coding: utf-8

import heapq
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
        self.left = []
        self.right = []
        self.stack = []
        self.vis = {}

    def solution_over(self, data):
        if not data:
            return 0
        res = []
        for i, v in enumerate(array):
            if i == 0 or res[-1] <= 0:
                res.append(v)
            else:
                res.append(res[-1] + v)
        return max(res)

    def get_midian(self):
        if not self.right and not self.left:
            return None
        if len(self.right) == len(self.left):
            return (float(self.right[0]) - self.left[0]) // 2
        elif len(self.right) > len(self.left):
            return self.right[0]
        else:
            return - self.left[0]


if __name__ == '__main__':
    l = [2, 3, 1, 0, 2, 5, 3]
    l2 = [1, 1, 1, 1, 1, 1, 1]

    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    s = Solution()
    # print(s.solution_over([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    # print(s.solution_over(array))
    # print(s.solution_over([7, 5, 6, 4]))
    t = [17, 20, 23, 62]
    # print([random.randint(1, 65) for _ in range(5)])

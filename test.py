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

    def solution(self, num, size):
        if not num or not size or size <= 0 or len(num) < size:
            return []
        res, index = [], []
        for i in range(size):
            if len(index) > 0 and num[i] > num[index[-1]]:
                index.pop()
            index.append(i)
        res.append(num[index[0]])
        for i in range(size, len(num)):
            while index and num[i] > num[index[-1]]:
                index.pop()
            if index and index[0] <= (i - size):
                index.pop(0)
            index.append(i)
            res.append(num[index[0]])
        return res


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
    # print(s.solution(30))
    print(s.solution([2, 3, 4, 2, 6, 2, 5, 1], 3))
    # print(s.solution(10001))
    b = [51, 59, 60, 62]
    a = [12, 13, 14, 17, 19, 38, 42, 43, 44, 45, 46, 47, 48, 49, 51, 53, 57, 58, 59, 60, 61, 62, 63, 70]
    # print(sorted(random.choices(a, k=10)))

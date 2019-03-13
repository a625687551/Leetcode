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

    def solution(self, data):
        if not data or data <= 9:
            return data

        first, num_len = 0, 1
        for i in range(len(str(data))):
            temp = data - num_len * 9 ** 10 * i
            if temp > 0:
                data = temp
                num_len += 1
            else:
                first = 10 * i
                break

        k, s = data // num_len, data % num_len
        return str(k + first)[s]

    def trans_data_str(self, str_num):
        length = len(str_num)


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
    print(s.solution(array))
    # print(s.solution(10001))
    a = [13, 17, 19, 38, 42, 43, 45, 46, 51, 61]
    a = [12, 13, 14, 17, 19, 38, 42, 43, 44, 45, 46, 47, 48, 49, 51, 53, 57, 59, 60, 61, 62, 63, 70]
    # print(sorted(random.choices(a, k=10)))

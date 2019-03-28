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
        if not data:
            return 0
        return self.count_inverse(data, data, 0, len(data) - 1)

    def count_inverse(self, ori, temp, start, end):
        if end - start < 1:
            return 0
        if end - start == 1:
            if ori[start] >= ori[end]:
                return 0
            else:
                temp[start], temp[end] = ori[end], ori[start]
                return 1
        mid = (start + end) // 2
        cnt = self.count_inverse(ori, temp, start, mid) + self.count_inverse(ori, temp, mid + 1, end)
        i, j = start, mid + 1
        ind = start
        while i <= mid and j <= end:
            if ori[i] <= ori[j]:
                temp[ind] = ori[i]
                i += 1
            else:
                temp[ind] = ori[j]
                cnt += mid - i + 1
                j += 1
            ind += 1
        while i <= mid:
            temp[ind] = ori[i]
            i += 1
            ind += 1
        while j <= end:
            temp[ind] = ori[j]
            j += 1
        return cnt


if __name__ == '__main__':
    l = [2, 3, 1, 0, 2, 5, 3]
    l2 = [1, 1, 1, 1, 1, 1, 1]
    l3 = [3, 4, 5, 1, 2]
    ss = "wo ai ni"
    s1, s2 = "abcdef", "cdefab"

    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    matrix = [['A', 'B', 'C', 'E', 'H', 'J', 'I', 'G'],
              ['S', 'F', 'C', 'S', 'L', 'O', 'P', 'Q'],
              ['A', 'D', 'E', 'E', 'M', 'N', 'O', 'E'],
              ['A', 'D', 'I', 'D', 'E', 'J', 'F', 'M'],
              ['V', 'C', 'E', 'I', 'F', 'G', 'G', 'S']]
    way = ['S', 'L', 'H', 'E', 'C', 'C', 'E', 'I',
           'D', 'E', 'J', 'F', 'G', 'G', 'F', 'I', 'E']

    s = Solution()
    # print(s.solution_over([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    # print(s.solution(30))
    l = [364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993, 407, 416, 366, 315, 301, 601, 650, 418, 355, 460, 505,
         360, 965, 516, 648, 727, 667, 465, 849, 455, 181, 486, 149, 588, 233, 144, 174, 557, 67, 746, 550, 474, 162,
         268, 142, 463, 221, 882, 576, 604, 739, 288, 569, 256, 936, 275, 401, 497, 82, 935, 983, 583, 523, 697, 478,
         147, 795, 380, 973, 958, 115, 773, 870, 259, 655, 446, 863, 735, 784, 3, 671, 433, 630, 425, 930, 64, 266, 235,
         187, 284, 665, 874, 80, 45, 848, 38, 811, 267, 575]
    print(s.solution([7, 5, 6, 4]))
    print(s.solution(l))
    # print(s.solution(10001))
    a = [12, 13, 14, 17, 19, 38, 42, 43, 44, 45, 46, 47,
         48, 49, 51, 53, 57, 58, 59, 60, 61, 62, 63, 70]
    a = [12, 13, 14, 17, 19, 38, 42, 43, 44, 45, 46, 47,
         48, 49, 51, 53, 57, 58, 59, 60, 61, 62, 63, 70]

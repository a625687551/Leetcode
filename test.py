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
        self.index = -1
        self.left = []
        self.right = []
        self.stack = []
        self.vis = {}

    def solution(self, s):
        if not s:
            return -1
        sign, decimal, has_e = False, False, False
        for i, x in enumerate(s):
            if x == "e" or x == "E":
                if i == len(s) - 1:
                    return False
                if has_e:
                    return False
                has_e = True
            elif x in ["-", "+"]:
                if sign and s[i - 1] not in ["e", "E"]:
                    return False
                if not sign and i > 0 and s[i - 1] not in ["e", "E"]:
                    return False
                sign = True
            elif x == ".":
                if has_e or decimal:
                    return False
                decimal = True
            elif x > "9" or x < "0":
                return False
        return True


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
    t = [20, 31, 50, 15, 58]
    # print([random.randint(1, 65) for _ in range(5)])

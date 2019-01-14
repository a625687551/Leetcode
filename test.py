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

    def solution_over(self, n):
        if n <= 0 or not isinstance(n, int):
            return -1
        list_num = ["0"] * n
        while self.increament(list_num) is False:
            self.print_num(list_num)

    def print_num(self, num):
        for i, v in enumerate(num):
            if v != "0":
                print("".join(num[i:]))
                break

    def increament(self, num):
        is_overflow = False
        is_incre = 0
        len_num = len(num)
        n = len_num - 1
        while n >= 0:
            nsum = int(num[n]) + is_incre
            if n == len_num - 1:
                nsum += 1
            if nsum >= 10:
                if n == 0:
                    is_overflow = True
                else:
                    is_incre = 1
                    nsum = nsum % 10
                    num[n] = str(nsum)
            else:
                num[n] = str(nsum)
            n -= 1
        return is_overflow


if __name__ == '__main__':
    l = [2, 3, 1, 0, 2, 5, 3]
    l2 = [1, 1, 1, 1, 1, 1, 1]

    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    s = Solution()
    # print(s.solution_over([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    # print(s.solution_over(3))
    # print(s.solution_over([7, 5, 6, 4]))
    t = [4, 34, 41, 32, 37]
    # print([random.randint(1, 65) for _ in range(5)])

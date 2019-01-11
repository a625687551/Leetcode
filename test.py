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

    def solution_over(self, head, k):
        if not head or k < 0:
            return False
        first = second = head
        count = 0

        while first and first.next:
            first = first.next
            count += 1
            if count >= k:
                second = second.next
        if count < k:
            return False
        return second


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
    t = [56, 49, 29]
    print([random.randint(1, 65) for _ in range(5)])

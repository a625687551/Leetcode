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

    def solution(self, root):
        s = ""
        return self.serialize_sub(root, s)

    def serialize_sub(self, root, s):
        if not root:
            return "$,"
        s = str(root.val) + ","
        left = self.serialize_sub(root.left, s)
        right = self.serialize_sub(root.right, s)
        s += left + right
        return s

    def deserialize(self, s):
        self.index += 1
        l = s.split(",")
        if self.index >= len(s):
            return None
        root = None
        if l[self.index] != "$":
            root = TreeNode[int(l[self.index])]
            root.left = self.deserialize(s)
            root.right = self.deserialize(s)
        return root

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

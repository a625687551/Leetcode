# coding: utf-8

import heapq


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
        # min heap
        self.right = []
        self.stack = []

    def solution_over(self, root):
        if not root:
            return 0
        left_n = self.solution_over(root.left)
        right_n = self.solution_over(root.right)

        return left_n + 1 if left_n >= right_n else right_n + 1


if __name__ == '__main__':
    l = [2, 3, 1, 0, 2, 5, 3]

    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    s = Solution()
    print(s.solution_over([2, 3, 4, 2, 6, 2, 5, 1], 3))

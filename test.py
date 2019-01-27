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

    def solution(self, head):
        if not head:
            return head
        cur = head
        while cur:
            new = RandomListNode(cur.lable)
            new.next = cur.next
            cur.next = new
            cur = new.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        clone = head.next
        cur = clone
        p_cur = head
        while p_cur:
            p_cur.next = p_cur.next.next
            if cur.next:
                cur.next = cur.next.next
            cur = cur.next
            p_cur = p_cur.next
        return clone




    def judge(self, num):
        return num & 1


if __name__ == '__main__':
    l = [2, 3, 1, 0, 2, 5, 3]
    l2 = [1, 1, 1, 1, 1, 1, 1]

    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    s = Solution()
    # print(s.solution_over([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    # print(s.solution(array))
    t = [39, 42, 55, 35, 5]
    print([random.randint(1, 65) for _ in range(5)])

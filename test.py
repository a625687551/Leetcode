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

    def get_median(self):
        if len(self.left) == len(self.right):
            return float(-self.left[0] + self.right[0])/2
        elif len(self.right) > len(self.left):
            return self.right[0]
        else:
            return -self.left[0]

    def insert_num(self, num):
        if not self.left or num < -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        # balance
        if len(self.left) > len(self.right) + 1:
            temp = -heapq.heappop(self.left)
            heapq.heappush(self.right, temp)
        elif len(self.right) > len(self.left) + 1:
            temp = -heapq.heappop(self.right)
            heapq.heappush(self.left, temp)

if __name__ == '__main__':
    l = [2, 3, 1, 0, 2, 5, 3]

    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    s = Solution()
    for x in l:
        s.insert_num(x)
        print(s.get_median())

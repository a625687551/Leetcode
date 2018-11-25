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


class Solution():
    def __init__(self):
        self.index = -1

    def serialize(self, root):
        s = ""
        return self.serialize(root, s)

    def serialize_sub(self, root, s):
        if not root:
            return "$,"
        s = str(root.val) + ","
        left = self.serialize_sub(root.left, s)
        right = self.serialize_sub(root.right, s)
        s += left + right

    def deserialize_sub(self, s):
        pass


if __name__ == '__main__':
    l = [2, 3, 1, 0, 2, 5, 3]

    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    s = Solution()
    print(s.solution_over([5, 7, 6, 9, 11, 10, 8]))

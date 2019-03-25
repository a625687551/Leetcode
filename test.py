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

    def solution(self, nums, k):
        if not nums or not k:
            return True
        array = np.array(nums)
        rows, cols = array.shape
        for row in range(rows):
            for col in range(cols):
                if array[row][col] == k[0]:
                    if self.find_path(array, row, col, k[1:]):
                        return True
        return False

    def find_path(self, array, row, col, path):
        if not path:
            return True
        rows, cols = array.shape
        array[row][col] = 0
        if row + 1 < rows and array[row+1][col] == path[0]:
            return self.find_path(array, row+1, col, path[1:])
        elif row - 1 >= 0 and array[row-1][col] == path[0]:
            return self.find_path(array, row-1, col, path[1:])
        elif col + 1 < cols and array[row][col+1] == path[0]:
            return self.find_path(array, row, col+1, path[1:])
        elif col - 1 >= 0 and array[row][col-1] == path[0]:
            return self.find_path(array, row, col-1, path[1:])
        else:
            return False


if __name__ == '__main__':
    l = [2, 3, 1, 0, 2, 5, 3]
    l2 = [1, 1, 1, 1, 1, 1, 1]
    l3 = [3, 4, 5, 1, 2]
    ss = "wo ai ni"

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

    print(s.solution(matrix, way))
    # print(s.solution(10001))
    a = [12, 13, 14, 17, 19, 38, 42, 43, 44, 45, 46, 47,
         48, 49, 51, 53, 57, 58, 59, 60, 61, 62, 63, 70]
    a = [12, 13, 14, 17, 19, 38, 42, 43, 44, 45, 46, 47,
         48, 49, 51, 53, 57, 58, 59, 60, 61, 62, 63, 70]

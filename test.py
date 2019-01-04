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

    def solution_over(self, nums):
        if not nums or len(nums) != 5:
            return False
        new_list = sorted(nums)
        zero_num = 0
        num_gap = 0
        print(new_list)
        for i, x in enumerate(new_list[:4]):
            if x == 0:
                zero_num += 1
            else:
                if new_list[i+1] == new_list[i]:
                    return False
                num_gap += new_list[i+1] - new_list[i]
        print(zero_num, num_gap)
        if num_gap <= 4:
            return True
        else:
            return False
if __name__ == '__main__':
    l = [2, 3, 1, 0, 2, 5, 3]

    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    s = Solution()
    s = Solution()
    print(s.solution_over([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    # print(s.solution_over([7, 5, 6, 4]))

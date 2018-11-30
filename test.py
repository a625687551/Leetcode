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
        return self.inverse_count(root[:], 0, len(root) - 1, root[:])

    def inverse_count(self, temp, start, end, data):
        if end - start < 1:
            return 0
        if end - start == 1:
            if data[start] <= data[end]:
                return 0
            else:
                temp[start], temp[end] = data[end], data[start]

        mid = (start + end) // 2
        cnt = self.inverse_count(data, start, mid, temp) + self.inverse_count(data, mid + 1, end, temp)
        i = start
        j = mid + 1
        ind = start
        while i <= mid and j <= end:
            if data[i] <= data[j]:
                temp[ind] = data[i]
                i += 1
            else:
                temp[ind] = data[j]
                cnt += mid - i + 1
                j += 1
            ind += 1
        while i <= mid:
            temp[ind] = data[i]
            i += 1
            ind += 1
        while j <= end:
            temp[ind] = data[j]
            j += 1
            ind += 1
        return cnt


if __name__ == '__main__':
    l = [2, 3, 1, 0, 2, 5, 3]

    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    s = Solution()
    print(s.solution_over([7, 5, 6, 4]))

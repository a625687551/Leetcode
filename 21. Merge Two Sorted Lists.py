# !/usr/bin/python
# coding:  utf-8

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, a, b):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if a and b:
        	if a.val > b.val:
        		a, b = b, a
        	a.next = self.mergeTwoLists(a.next, b)
        return a or b

if __name__ == '__main__':
	a = [1,2,4]
	b = [1,3,4]
	sol = Solution()
	print(sol.mergeTwoLists(a, b))
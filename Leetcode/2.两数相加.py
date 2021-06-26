#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        p = result
        carry = 0
        while l1 or l2 or carry:
            num = 0
            if l1:
                num += l1.val
                l1 = l1.next
            if l2: 
                num += l2.val
                l2 = l2.next
            num += carry
            carry, num = divmod(num, 10)
            p.next = ListNode(num)
            p = p.next
        return result.next
            

# @lc code=end


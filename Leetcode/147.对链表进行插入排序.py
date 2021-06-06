#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        last_sort = head
        curr = head.next
        while curr:
            if last_sort.val <= curr.val:
                last_sort = last_sort.next
            else:
                prev = dummy
                while prev.next.val <= curr.val:
                    prev = prev.next
                last_sort.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = last_sort.next
        return dummy.next
# @lc code=end


#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, size, intv = head, 0, 1
        # 长度
        while h:
            h = h.next
            size += 1
        res = ListNode(0)
        res.next = head
        while intv < size:
            prev, h = res, res.next
            while h:
                h1, i = h, intv
                while i and h:
                    h, i = h.next, i-1
                if i:
                    break
                h2, i = h, intv
                while i and h:
                    h, i = h.next, i-1
                c1, c2 = intv, intv-i

                while c1 and c2:
                    if h1.val < h2.val:
                        prev.next, h1, c1 = h1, h1.next, c1-1
                    else:
                        prev.next, h2, c2 = h2, h2.next, c2-1
                    prev = prev.next
                prev.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    prev, c1, c2 = prev.next, c1-1, c2-1
                prev.next = h
            intv *= 2
        return res.next
            

# @lc code=end


# -*- coding:utf-8 -*-

"""
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        elif not pHead2:
            return pHead1

        p1, p2 = pHead1,  pHead2
        p = ListNode
        r = p
        while p1 and p2:
            if p1.val >= p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next
        if p1:
            p.next = p1
        elif p2:
            p.next = p2
        # 不知道这个方法如何
        # if p1 or p2:
        #     p.next = p1 or p2
        return r.next



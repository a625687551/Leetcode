# -*- coding:utf-8 -*-

"""
输入一个链表，反转链表后，输出新链表的表头。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        rev = None
        # 1->2->3->4->5
        # 1<-2<-3 4->5
        while pHead:
            tmp = pHead.next
            pHead.next = rev
            rev, pHead = pHead, tmp
        return rev


if __name__ == '__main__':
    s = Solution()
    print(s.FindKthToTail({1, 2, 3, 4, 5}, 1))

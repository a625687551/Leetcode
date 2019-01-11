# -*- coding:utf-8 -*-

"""
输入一个链表，输出该链表中倒数第k个结点。
"""


class ListNode:
    def __init__(self, item=None, pos_item=None):
        self.val = item
        self.next = pos_item

    def __repr__(self):
        return str(self.val)


class Solution:
    def FindKthToTail(self, head, k):
        if not head or k <= 0:
            return None
        first = second = head
        count = 0
        while first:
            first = first.next
            count += 1
            if count >= k:
                second = second.next
        if count < k:
            return None
        return second


if __name__ == '__main__':
    s = Solution()
    t = ListNode({1, 2, 3, 4, 5}, pos_item=0)
    print(t)
    print(t.next.next)
    # print(s.FindKthToTail(t.next, 1))

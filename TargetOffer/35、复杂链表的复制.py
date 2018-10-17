# -*- coding:utf-8 -*-

"""
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    def Clone(self, pHead):
        if not pHead:
            return None
        cur = pHead
        # 复制节点在原来节点之后
        while cur:
            new = RandomListNode(cur.label)
            new.next = cur.next
            cur.next = new
            cur = new.next
        # 赋值random节点
        cur = pHead
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        head = pHead.next
        cur = head
        pcur = pHead
        while pcur:
            pcur.next = pcur.next.next
            if cur.next:
                cur.next = cur.next.next
            cur = cur.next
            pcur = pcur.next

        return head


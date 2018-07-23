# -*- coding: utf-8 -*-

"""
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, p_node):
        if not p_node:
            return
        p_next = None
        if p_node.right:
            p_right = p_node.right
            while p_right.left:
                p_right = p_right.left
            p_next = p_right
        elif p_node.next:
            p_current = p_node
            p_parent = p_current.next
            while p_parent and p_current == p_node.right:
                p_current = p_parent
                p_parent = p_current.next
            p_next = p_parent
        return p_next
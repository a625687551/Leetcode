# -*- coding: utf-8 -*-
# @Time    : 2021/2/13 8:30 下午
# @Author  : wangjianfeng
# @File    : 101. Symmetric Tree.py
"""
难度：简单
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.check(root.left, root.right)

    def check(self, left: TreeNode, right: TreeNode) -> bool:
        if not (left or right):
            return True
        if not (left and right):
            return False
        if left.val != right.val:
            return False
        return self.check(left.left, right.right) & self.check(left.right, right.left)
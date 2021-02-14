# -*- coding: utf-8 -*-
# @Time    : 2021/2/13 8:42 下午
# @Author  : wangjianfeng
# @File    : 110. Balanced Binary Tree.py
"""
难度：简单
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        return abs(self.height(root.left) - self.height(root.right)) < 1 & self.isBalanced(root.right) & self.isBalanced(root.left)

    def height(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1


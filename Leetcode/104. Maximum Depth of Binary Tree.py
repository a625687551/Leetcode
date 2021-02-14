# -*- coding: utf-8 -*-
# @Time    : 2021/2/13 8:31 下午
# @Author  : wangjianfeng
# @File    : 104. Maximum Depth of Binary Tree.py
"""
难度：简单
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
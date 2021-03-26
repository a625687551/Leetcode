# -*- coding: utf-8 -*-
# @Time    : 2021/2/15 10:58 上午
# @Author  : wangjianfeng
# @File    : 98. Validate Binary Search Tree.py

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, node, lower, upper) -> bool:
        if not node:
            return True
        val = node.val
        if val <= lower or val >= upper:
            return False
        if not self.helper(node.right, val, upper):
            return False
        if not self.helper(node.left, lower, val):
            return False
        return True

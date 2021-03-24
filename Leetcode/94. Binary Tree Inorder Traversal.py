# -*- coding: utf-8 -*-
# @Time    : 2021/2/13 8:07 下午
# @Author  : wangjianfeng
# @File    : 94. Binary Tree Inorder Traversal.py
"""
难度：中等
二叉树的中序遍历
"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        颜色标记法
        :param root:
        :return:
        """
        if not root:
            return []
        white, grey = 0, 1
        result = []
        stack = [(white, root)]
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color == white:
                stack.append((white, node.right))
                stack.append((grey, node))
                stack.append((white, node.left))
            else:
                result.append(node.val)
        return result

# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 7:43 上午
# @Author  : wangjianfeng
# @File    : 99. 恢复二叉搜索树.py

from typing import List, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """中序遍历"""
        node = self.middle_loop(root, [])
        x, y = None, None
        pre = node[0]
        for i in range(1, len(node)):
            if pre.val > node[i].val:
                y = node[i]
                if not x:
                    x = pre
            pre = node[i]
        if x and y:
            x.val, y.val = y.val, x.val

    def middle_loop(self, root: TreeNode, node: List):
        if not root:
            return node
        node = self.middle_loop(root.left, node)
        node.append(root)
        node = self.middle_loop(root.right, node)
        return node

    def recoverTree_two(self, root: TreeNode) -> None:
        """莫里斯遍历"""
        node = self.middle_loop(root, [])


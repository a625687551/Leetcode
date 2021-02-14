# -*- coding: utf-8 -*-
# @Time    : 2021/2/13 8:43 下午
# @Author  : wangjianfeng
# @File    : 112. Path Sum.py
"""
难度：简单
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    1. DFS
    2. BFS
    """
    def hasPathSum_BFS(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        cur_layer_node = deque([root])
        cur_layer_value = deque([root.val])
        while cur_layer_node:
            cur_node = cur_layer_node.popleft()
            cur_val = cur_layer_value.popleft()
            if not cur_node.left and not cur_node.right:
                if cur_val == targetSum:
                    return True
            if cur_node.left:
                cur_layer_node.append(cur_node.left)
                cur_layer_value.append(cur_node.left.val + cur_val)
            if cur_node.right:
                cur_layer_node.append(cur_node.right)
                cur_layer_value.append(cur_node.right.val + cur_val)
        return False

    def hasPathSum_DFS(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        return self.hasPathSum_DFS(root.left, targetSum - root.val) or self.hasPathSum_DFS(root.right, targetSum - root.val)

    def hasPathSum_back(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
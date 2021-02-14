# -*- coding: utf-8 -*-
# @Time    : 2021/2/13 8:31 下午
# @Author  : wangjianfeng
# @File    : 107. Binary Tree Level Order Traversal II.py
"""
难度：简单
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
        使用队列来解决
        :param root:
        :return:
        """
        if not root:
            return []
        result = []
        cur_layer = [root]
        while cur_layer:
            cur_layer_val = []
            next_layer = []
            for node in cur_layer:
                if not node:
                    continue
                cur_layer_val.append(node.val)
                next_layer.extend([node.left, node.right])
            if cur_layer_val:
                result.insert(0, cur_layer_val)
            cur_layer = next_layer
        return result




# -*- coding: utf-8 -*-
# @Time    : 2021/2/15 10:58 上午
# @Author  : wangjianfeng
# @File    : 102. Binary Tree Level Order Traversal.py

from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res

        queue = deque([root])
        while queue:
            temp = []
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
        return res

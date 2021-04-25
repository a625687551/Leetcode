# -*- coding: utf-8 -*-
# @Time    : 2021/2/13 8:07 下午
# @Author  : wangjianfeng
# @File    : 103. Binary Tree Zigzag Level Order Traversal.py
"""
难度：中等
"""
from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res

        queue = deque([root])
        is_even = False
        while queue:
            temp = deque()
            queue_length = len(queue)
            for _ in range(queue_length):
                root = queue.popleft()
                if is_even:
                    temp.append(root.val)
                else:
                    temp.appendleft(root.val)
                if root.right:
                    queue.append(root.right)
                if root.left:
                    queue.append(root.left)

            res.append(list(temp))
            is_even = not is_even
        return res


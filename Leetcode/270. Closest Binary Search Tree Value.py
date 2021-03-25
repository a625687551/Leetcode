# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 8:25 下午
# @Author  : wangjianfeng
# @File    : 270. Closest Binary Search Tree Value.py

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        """递归加线性排序"""
        if not target:
            return 0
        if not root or not (root.left or root.right):
            return root.val
        in_order = self.middle_order(root)
        return min(in_order, key=lambda x: abs(x - target))

    def middle_order(self, root: TreeNode) -> List:
        if not root:
            return []
        return self.middle_order(root.left) + [root.val] + self.middle_order(
            root.right)

    def closestValue_second(self, root: TreeNode, target: float) -> int:
        """迭代 没成功"""
        stack, pred = [], float("-inf")
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            if pred == target:
                return pred
            elif pred < target and target < root.val:
                return min(pred, root.val, key=lambda x: abs(x - target))

            pred = root.val
            root = root.right
        return pred

    def closestValue_third(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key=lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest


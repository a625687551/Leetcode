# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 7:42 上午
# @Author  : wangjianfeng
# @File    : 226. Invert Binary Tree.py
"""
难度简单，树
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        递归来解决
        时间复杂度：每个元素都必须访问一次，所以是 O(n)
        空间复杂度：最坏的情况下，需要存放 O(h) 个函数调用(h是树的高度)，所以是 O(h)
        """
        if not root:
            return None
        root.right, root.left = root.left, root.right
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def invertTree_iteration(self, root: TreeNode) -> TreeNode:
        """
        迭代更新
        时间复杂度：同样每个节点都需要入队列/出队列一次，所以是 O(n)
        空间复杂度：最坏的情况下会包含所有的叶子节点，完全二叉树叶子节点是 n/2个，所以时间复杂度是 0(n)
        :param root:
        :return:
        """
        if not root:
            return None
        queue = [root]
        while queue:
            temp = queue.pop(0)
            temp.left, temp.right = temp.right, temp.left
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return root

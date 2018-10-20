# !usr/bin/env python
# -*- coding: utf-8 -*-

"""
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
"""


class Solution:
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True

        return self.depth(pRoot) != -1

    def depth(self, tree):
        if not tree:
            return 0
        left_n = self.depth(tree.left)
        right_n = self.depth(tree.right)
        if left_n == -1 or right_n == -1:
            return -1
        if abs(left_n - right_n) <= 1:
            return max(left_n, right_n) + 1
        return -1

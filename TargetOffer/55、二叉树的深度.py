# !usr/bin/env python
# -*- coding: utf-8 -*-

"""
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
"""


class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        left_n = self.TreeDepth(pRoot.left)
        right_n = self.TreeDepth(pRoot.right)

        return left_n + 1 if left_n >= right_n else right_n + 1

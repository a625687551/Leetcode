# !usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一棵二叉搜索树，请找出其中的第k小的结点。
例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
中序遍历即可找出第K个节点
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.stack = []

    def KthNode(self, pRoot, k):
        self.intraverse(pRoot)
        if 1 <= k <= len(self.stack):
            return self.stack[k - 1]
        else:
            return None

    def intraverse(self, root):
        if not root:
            return None
        self.intraverse(root.left)
        self.stack.append(root)
        self.intraverse(root.right)

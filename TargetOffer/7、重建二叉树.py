# -*- coding: utf-8 -*-

"""
题目：请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre and not tin:
            return None
        root = TreeNode(pre[0])
        if set(pre) != set(tin):
            return None
        i = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:i+1], tin[:i])
        root.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
        return root

pre = [1, 2, 3, 5, 6, 4]
tin = [5, 3, 6, 2, 4, 1]
test = Solution()
newTree = test.reConstructBinaryTree(pre, tin)
# !usr/bin/env python
# -*- coding: utf-8 -*-

"""
请实现两个函数，分别用来序列化和反序列化二叉树
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.index = -1

    def Serialize(self, root):
        s = ""
        return self.serialize_sub(root, s)

    def serialize_sub(self, root, s):
        if not root:
            return "$,"
        s = str(root.val) + ","
        left = self.serialize_sub(root.left, s)
        right = self.serialize_sub(root.right, s)
        s += left + right
        return s

    def Deserialize(self, s):
        self.index += 1
        l = s.split(",")
        if self.index >= len(s):
            return None
        root = None
        if l[self.index] != "$":
            root = TreeNode(int(l[self.index]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root

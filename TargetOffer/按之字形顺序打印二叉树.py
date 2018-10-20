# coding: utf-8

"""
请实现一个函数按照之字形打印二叉树，
即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""


class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        res = []
        self.level(pRoot, 0, res)
        for level in range(1, len(res), 2):
            res[level] = res[level][::-1]
        return res

    def level(self, root, level, res):
        if not root:
            return []
        if level == len(res):
            res.append([])
        res[level].append(root.val)
        if root.left:
            self.level(root.left, level + 1, res)
        if root.right:
            self.level(root.right, level + 1, res)

# -*- coding:utf-8 -*-

"""
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        res = []
        cur = [root]
        while len(cur):
            t = cur.pop(0)
            res.append(t.val)
            if t.left:
                cur.append(t.left)
            if t.right:
                cur.append(t.right)
        return res

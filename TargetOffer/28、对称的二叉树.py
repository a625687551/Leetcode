# !usr/bin/env python
# -*- coding: utf-8 -*-

"""
请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""


class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        new = pRoot
        return self.check(new, pRoot)

    def check(self, left, right):
        if not left and not right:
            return True
        if left and right and left.val == right.val:
            return self.check(left.left, right.right) and self.check(left.right, right.left)
        else:
            return False
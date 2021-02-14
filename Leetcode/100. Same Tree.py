# -*- coding: utf-8 -*-
# @Time    : 2021/2/13 8:29 下午
# @Author  : wangjianfeng
# @File    : 100. Same Tree.py
"""
难度：简单
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) & self.isSameTree(p.right, q.right)
        else:
            return False


if __name__ == '__main__':
    p = [1, 2, 3]
    q = [1, 2, 3]
    s = Solution()
    print(s.isSameTree(p, q))

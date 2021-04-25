# -*- coding: utf-8 -*-
# @Time    : 2021/2/15 5:36 下午
# @Author  : wangjianfeng
# @File    : 106. Construct Binary Tree from Inorder and Postorder Traversal.py
"""从中序与后序遍历序列构造二叉树"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        n = len(postorder)
        in_index = {ele: i for i, ele in enumerate(inorder)}

        return self.deserialize(inorder, postorder, in_index, 0, n - 1, 0,
                                n - 1)

    def deserialize(self, inorder, postorder, in_index, in_left, in_right, post_left, post_right):
        if post_left > post_right:
            return None
        """递归来实现"""
        in_root = in_index[postorder[post_right]]
        root = TreeNode(postorder[post_right])
        size_left_subtree = in_root - in_left

        root.left = self.deserialize(inorder, postorder, in_index,
                                     in_left, in_root-1,
                                     post_left,  post_left + size_left_subtree)
        root.right = self.deserialize(inorder, postorder, in_index,
                                      in_root + 1, in_right,
                                      post_left + size_left_subtree+1,
                                      post_right - 1)
        return root


if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    s = Solution()
    r = s.buildTree(inorder, postorder)
    print(r.left.val)

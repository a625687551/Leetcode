# -*- coding: utf-8 -*-
# @Time    : 2021/2/15 10:58 上午
# @Author  : wangjianfeng
# @File    : 105. Construct Binary Tree from Preorder and Inorder Traversal.py
"""从前序与中序遍历序列构造二叉树"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(preorder)
        index = {ele: i for i, ele in enumerate(inorder)}
        return self.deserialize(preorder, inorder, index, 0, n - 1, 0, n - 1)

    def deserialize(self, preorder, inorder, index, pre_left, pre_right,
                    in_left, in_right):
        """树在序列化时候采用递归，则反序列化也适用,这里用两个指针"""
        if pre_left > pre_right:
            return None
        in_root = index[preorder[pre_left]]
        root = TreeNode(preorder[pre_left])
        size_left_subtree = in_root - in_left

        root.left = self.deserialize(preorder, inorder, index, pre_left + 1,
                                     pre_left + size_left_subtree,
                                     in_left, in_root - 1)
        root.right = self.deserialize(preorder, inorder, index,
                                      pre_left + size_left_subtree + 1,
                                      pre_right, in_root + 1, in_right)
        return root


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    s = Solution()
    r = s.buildTree(preorder, inorder)
    print(r.left.val)

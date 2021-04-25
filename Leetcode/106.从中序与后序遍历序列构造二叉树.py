#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder or len(inorder) != len(postorder):
            return None
        in_index = {ele:i for i, ele in enumerate(inorder)}
        n = len(inorder)
        
        return self.deserialize(inorder, postorder, in_index, 0, n-1, 0, n-1)

    def deserialize(self, inorder, postorder, in_index, in_left, in_right, post_left, post_right):
        """反序列化"""
        if in_left > in_right or post_left > post_right:
            return None
        root_index = in_index[postorder[-1]]
        root = TreeNode(postorder[-1])
        left_subtree_size = root_index - in_left
        root.left = self.deserialize(inorder, postorder, in_index, in_left, root_index-1, post_left, post_left + left_subtree_size)
        root.right = self.deserialize(inorder, postorder, in_index, root_index +1, in_right, post_left+ size_left_subtree+1, post_right-1)
        return root
# @lc code=end


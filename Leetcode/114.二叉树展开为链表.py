#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return []
        result = []
        def prereverse(node:TreeNode):
            if not node:
                return None
            result.append(node)
            prereverse(node.left)
            prereverse(node.right)
            
        prereverse(root)
        size = len(result)
        for i in range(1, size):
            pre, cur = result[i-1], result[i]
            pre.left = None
            pre.right = cur
        # return result


# @lc code=end


#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, prevalue: int) -> int:
            if not node:
                return 0
            total = prevalue*10+node.val
            if not node.left and not node.right:
                return total
            else:
                return dfs(node.left, total)+dfs(node.right, total)
        
        return dfs(root, 0)


# @lc code=end


#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
from collections import deque

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        result = []

        def find_sum_path(node, router, remain_val):
            now = node.val
            router.append(now)
            remain_val -= now
            is_last = True
            if node.right:
                is_last = False
                find_sum_path(node.right, router[:], remain_val)
            if node.left:
                is_last = False
                find_sum_path(node.left, router[:], remain_val)
            if is_last and remain_val == 0:
                result.append(router)

        find_sum_path(root, [], targetSum)
        return result
        
# @lc code=end


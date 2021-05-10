#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        right_most_value = dict()
        max_depth = -1
        queue = collections.deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            right_most_value[depth] = node.val
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        return [right_most_value[depth] for depth in range(max_depth+1)]

# @lc code=end


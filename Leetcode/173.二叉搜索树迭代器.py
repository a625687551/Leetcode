#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#
import collections
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.bst_list = collections.deque([])
        self.build_inorder(root)

    def build_inorder(self, node: TreeNode):
        if not node:
            return
        self.build_inorder(node.left)
        self.bst_list.append(node.val)
        self.build_inorder(node.right)

    def next(self) -> int:
        if self.bst_list:
            return self.bst_list.popleft()
            

    def hasNext(self) -> bool:
        return len(self.bst_list) != 0 



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end


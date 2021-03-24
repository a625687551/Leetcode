# -*- coding: utf-8 -*-
# @Time    : 2021/2/15 10:55 上午
# @Author  : wangjianfeng
# @File    : 95. Unique Binary Search Trees II.py

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    1. 回溯
    2. 递归
    3. 动态规划
    """

    def generateTrees_back(self, n: int) -> List[TreeNode]:
        """回溯法"""
        return self.generate(1, n) if n else []

    def generate(self, start, end):
        if start > end:
            return [None, ]
        all_tree = []
        for i in range(start, end + 1):
            left_tree = self.generate(start, i - 1)
            right_tree = self.generate(i + 1, end)

            for l in left_tree:
                for r in right_tree:
                    current_tree = TreeNode(i)
                    current_tree.left = l
                    current_tree.right = r
                    all_tree.append(current_tree)
        return all_tree

    def generateTrees_dynamic(self, n: int) -> List[TreeNode]:
        """动态规划没搞定"""
        if not n:
            return []
        pre = [None]
        for i in range(n + 1):
            cur = []
            for tree in pre:
                # 插入到根结点
                new_root = TreeNode(i)
                new_root.left = tree
                cur.append(new_root)
                # 插入到右边，最多查找n次
                for j in range(i + 1):
                    tree_copy = self.copy_tree(tree)
                    right = tree_copy
                    for k in range(j):
                        if not right:
                            break
                        right = right.right
                    if not right:
                        break
                    child_root = TreeNode(i)
                    child_root.right = right.right
                    right.right = child_root
                    # right_tree = right.right
                    # right.right = child_root
                    # child_root.left = right_tree
                    cur.append(tree_copy)
            pre = cur
        return pre

    def copy_tree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        new_tree = TreeNode(root.val)
        new_tree.left = root.left
        new_tree.right = root.right
        return new_tree


if __name__ == '__main__':
    n = 3
    s = Solution()
    print(s.generateTrees_back(n))

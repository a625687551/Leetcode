# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 8:24 下午
# @Author  : wangjianfeng
# @File    : 257. Binary Tree Paths.py

from typing import List
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        """dfs 没成功"""
        paths = []
        if not root:
            return paths

        def construct_path(root, path):
            if not root:
                return path
            path += str(root.val)
            if not root.left and not root.right:
                paths.append(root)
            else:
                path += "->"
                construct_path(root.left, path)
                construct_path(root.right, path)
        construct_path(root, "")
        return paths

    def binaryTreePaths_BFS(self, root: TreeNode) -> List[str]:
        paths = []
        if not root:
            return []
        node_queue, path_queue = collections.deque([root]), collections.deque(
            [str(root.val)])
        while node_queue:
            node = node_queue.popleft()
            path = path_queue.popleft()
            if not node.right and not node.left:
                paths.append(path)
            else:
                if node.left:
                    node_queue.append(node.left)
                    path_queue.append(path + "->" + str(node.left.val))
                if node.right:
                    node_queue.append(node.right)
                    path_queue.append(path + "->" + str(node.right.val))

        return paths

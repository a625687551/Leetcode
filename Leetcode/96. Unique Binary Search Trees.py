# -*- config: utf-8 -*-
# @Time    : 2021/2/15 10:57 上午
# @Author  : wangjianfeng
# @File    : 96. Unique Binary Search Trees.py


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    1. 回溯 放弃吧 阿西吧
    2. 动态规划
    3. 数学：https://baike.baidu.com/item/catalan/7605685?fr=aladdin
    """

    def numTrees_back(self, n: int) -> int:
        """这个如果int很大会超时"""
        return len(self.generate(1, n)) if n else 0

    def generate(self, start, end):
        if start > end:
            return [None]
        all_tree = []
        for i in range(start, end + 1):
            left_tree = self.generate(start, i - 1)
            right_tree = self.generate(i + 1, end)
            for l in left_tree:
                for r in right_tree:
                    cur_tree = TreeNode(i)
                    cur_tree.left = l
                    cur_tree.right = r
                    all_tree.append(cur_tree)
        return all_tree

    def numTrees_math(self, n: int) -> int:
        """数学来计算，用卡特兰数"""
        c = 1
        for i in range(n):
            c = c * 2 * (2 * i + 1) / (i + 2)
        return int(c)

    def numTrees_dynamic(self, n: int) -> int:
        """动态规划"""
        result = [0]*(n+1)
        result[0], result[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                result[i] += result[j - 1] * result[i - j]
        return result[n]


if __name__ == '__main__':
    n = 3
    s = Solution()
    # print(s.numTrees_back(n))
    # print(s.numTrees_math(n))
    print(s.numTrees_dynamic(n))

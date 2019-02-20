# !/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
给定两个字符串，求解这两个字符串的最长公共子序列（Longest Common Sequence）。比如字符串1：BDCABA；字符串2：ABCBDAB
则这两个字符串的最长公共子序列长度为4，最长公共子序列是：BCBA
"""
import numpy as np


class Solution:
    def max_common(self, s1, s2):
        if not s1 or not s2:
            return None
        len1, len2 = len(s1), len(s2)
        matrix = np.zeros([len1 + 1, len2 + 1], int)
        end, max_len = 0, 0
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if i == 0 or j == 0:
                    matrix[i][j] = 0
                elif s1[i - 1] == s2[j - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1] + 1
                    if matrix[i][j] > max_len:
                        max_len = matrix[i][j]
                        end = i
                else:
                    matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
        # print(matrix)
        # print(max_num, end)
        return s1[end-max_len:end], matrix[len1][len2]


if __name__ == '__main__':
    s = Solution()
    print(s.max_common("abcdef", "cdefab"))
    print(s.max_common("cdefab", "abcdef"))
    print(s.max_common("xxxabcdef", "ttttcdefab"))
    print(s.max_common("ggggabced555", "ttttabced4444"))
    print(s.max_common("", "sdffh"))
    print(s.max_common("", ""))

# !/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
给定两个字符串，求解这两个字符串的最长公共子序列（Longest Common Sequence）。比如字符串1：BDCABA；字符串2：ABCBDAB
则这两个字符串的最长公共子序列长度为4，最长公共子序列是：BCBA
"""


class Solution:
    def max_common(self, s1, s2):
        if not s1 or not s2:
            return None
        i, j = len(s1), len(s2)
        for i in s1:
            for j in s2:
                pass


if __name__ == '__main__':
    s = Solution()
    print(s.max_common("abcdef", "cdefab"))
    print(s.max_common("", "sdffh"))
    print(s.max_common("", ""))

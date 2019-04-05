# !/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
问题描述：
利用字符操作，把字符串A转换成字符串B所需要的最少操作数（删除一个字符、插入一个字符、修改一个字符）
给定两个字符串A和B，求字符串A至少经过多少步字符操作变成字符串B
思路：
1）首先考虑A串的第一个字符
    假设存在两个字符串A和B，他们的长度分别是lenA和lenB。首先考虑第一个字符，由于他们是一样的，所以只需要计算A[2...lenA]和B[2...lenB]之间的距离即可。那么如果两个字符串的第一个字符不一样怎么办？可以考虑把第一个字符变成一样的（这里假设从A串变成B串）：
* 修改A串的第一个字符成B串的第一个字符，之后仅需要计算A[2...lenA]和B[2...lenB]的距离即可；
* 删除A串的第一个字符，之后仅需要计算A[2...lenA]和B[1...lenB]的距离即可；
* 把B串的第一个字符插入到A串的第一个字符之前，之后仅需要计算A[1...lenA]和B[2...lenB]的距离即可。
2）接下来考虑A串的第i个字符和B串的第j个字符。
  我们这个时候不考虑A的前i-1字符和B串的第j-1个字符。如果A串的第i个字符和B串的第j个字符相等，即A[i]=B[j]，则只需要计算A[i...lenA]和B[j...lenB]之间的距离即可。如果不想等，则：
* 修改A串的第i个字符成B串的第j个字符，之后仅需要计算A[i+1...lenA]和B[j+1...lenB]的距离即可；
* 删除A串的第i个字符，之后仅需要计算A[i+1...lenA]和B[j...lenB]的距离即可；
* 把B串的第j个字符插入到A串的第i个字符之前，之后仅需要计算A[i...lenA]和B[j+1...lenB]的距离即可。
在这里转移方程可以写出:
edit[i][j]
0  i=0,j=0
j  i=0,j>0
i  i>0,j=0
min(edit[i-1][j]+1,edit[i][j-1]+1,edit[i-1][j-1]+flag
其中flag等于0(A[i]==B[j]) 1(A[i]!=B[j])
"""
import numpy as np


class Solution(object):

    def min_edit_distance(self, s1, s2):
        if not s1 or not s2:
            return len(s1) or len(s2)
        len1, len2 = len(s1), len(s2)
        edit_matirx = np.zeros((len1 + 1, len2 + 1), int)
        for i in range(len1 + 1):
            for j in range(len2 + 1):
                if i == 0 or j == 0:
                    edit_matirx[i][j] = i or j
                elif s1[i-1] == s2[j-1]:
                    edit_matirx[i][j] = edit_matirx[i - 1][j - 1]
                else:
                    edit_matirx[i][j] = min(edit_matirx[i - 1][j - 1] + 1, edit_matirx[i - 1][j] + 1,
                                            edit_matirx[i][j - 1] + 1)
        # print(edit_matirx)
        return edit_matirx[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.min_edit_distance("hello", "hell"))
    print(s.min_edit_distance("abcd", "acd"))
    print(s.min_edit_distance("", ""))
    print(s.min_edit_distance("h", "hell"))

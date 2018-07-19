# -*- coding: utf-8 -*-

"""
题目：请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


class Solution(object):
    def replace_str(self, s):
        if not s:
            return
        return s.replace(" ", "%20")

    def replace_str_back(self, s):
        if not isinstance(s, str) or len(s) <= 0 or s == None:
            return ""
        s1 = []
        for x in s[::-1]:
            if x ==" ":
                x = "%20"
            s1.append(x)
        return "".join(s1[::-1])

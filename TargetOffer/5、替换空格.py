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
        if not isinstance(s, str) and not s:
            return ""
        ws = 0
        for item in s:
            if item == " ":
                ws += 1
        new_len = len(s) + ws * 2
        new_str = new_len * [None]
        index_old, index_new = len(s) - 1, new_len - 1
        while index_old and index_new >= index_old:
            if s[index_old] == " ":
                new_str[index_new - 2:index_new + 1] = ['%', '2', '0']
                index_new -= 3
                index_old -= 1
            else:
                new_str[index_new] = s[index_old]
                index_new -= 1
                index_old -= 1
        return "".join(new_str)

# -*- coding:utf-8 -*-
"""
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，
第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
如果当前字符流没有存在出现一次的字符，返回#字符。
注意这个而是字符流
"""


class Solution:
    # 这个是O(N)时间复杂度，O（N)空间复杂度
    def __init__(self):
        self.s = ""
        self.dict_num = {}

    def FirstAppearingOnce(self):
        for s in self.s:
            if self.dict_num[s] == 1:
                return s
        return "#"

    def Insert(self, char):
        self.s = self.s + char
        if char in self.dict_num:
            self.dict_num[char] = self.dict_num[char] + 1
        else:
            self.dict_num[char] = 1

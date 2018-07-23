# -*- coding: utf-8 -*-

"""
题目：请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


class Solution:
    def Fibonacci(self, n):
        temp = [0, 1]
        if n >= 2:
            for i in range(2, n+1):
                temp[i % 2] = temp[0] + temp[1]
        return temp[n % 2]
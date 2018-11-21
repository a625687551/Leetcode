# -*- coding: utf-8 -*-

"""
题目：请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


class Solution:
    def Fibonacci(self, n):
        temp = [0, 1]
        if n >= 2:
            for i in range(2, n + 1):
                temp[i % 2] = temp[0] + temp[1]
        return temp[n % 2]

    def fibonacci_1(self, n):
        if n == 1:
            return 0
        if n == 2:
            return 1
        temp = [0, 1]
        if n >= 2:
            pass


if __name__ == '__main__':
    s = Solution()
    print(s.Fibonacci(10))

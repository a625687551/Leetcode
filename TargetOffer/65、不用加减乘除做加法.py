# -*- coding:utf-8 -*-

"""
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
PS: 这里遇到负数就尴尬了，但是其他语言就没事

"""


class Solution:
    def Add(self, num1, num2):
        while num2 != 0:
            sum = num1 ^ num2
            carray = (num1 & num2) << 1
            num1 = sum
            num2 = carray
        return num1


if __name__ == '__main__':
    s = Solution()
    print(s.Add(1, 200))

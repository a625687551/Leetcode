# -*- coding:utf-8 -*-

"""
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
PS: 这里遇到负数就尴尬了，但是其他语言就没事

异或运算：相当于无进位加法
与运算，再左移一位：相当于进位
"""


class Solution:
    def Add(self, num1, num2):
        # if not num1 or num1 & 0:
        #     return num2
        # if not num2 or num2 & 0:
        #     return num1
        if not num1 or not num2:
            return num1 or num2

        while num2 != 0:
            # 相加不需要进位的位
            sum_two = 0xFFFFFFFF & (num1 ^ num2)
            # 相加需要进位的位
            carray = 0xFFFFFFFF & (num1 & num2) << 1
            num1 = sum_two
            num2 = carray
        return num1 if num1 <= 0x7FFFFFFF else ~(num1 ^ 0xFFFFFFFF)

    def Add_2(self, num1, num2):
        """这个不行"""
        # num1 = "{:0=4b}".format(num1)
        # num2 = "{:0=4b}".format(num2)
        while num2 != 0:
            sum_two = num1 ^ num2
            carray = (num1 & num2) << 1
            num1 = sum_two
            num2 = carray
        return num1


if __name__ == '__main__':
    s = Solution()
    # print(s.Add(1, 200))
    # print(s.Add(-1, 5))
    print(s.Add(1, 5))
    print(s.Add(-1, 5))

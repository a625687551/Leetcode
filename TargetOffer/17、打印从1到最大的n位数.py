# -*- coding:utf-8 -*-
"""
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
"""


class Solution:
    def print_n(self, n):
        if n <= 0:
            return
        list_num = ["0"] * n
        while self.increament(list_num) is False:
            self.print_num(list_num)

    def print_num(self, num):
        is_begin = False
        for i in range(len(num)):
            if num[i] != "0" and is_begin is False:
                is_begin = True
            if is_begin:
                tmp = ("".join(num[i:]))
                print(tmp)
                break

    def increament(self, num):
        is_overflow = False
        is_incre = 0  # 是否能够归零进一
        len_num = len(num)
        n = len_num - 1
        while n >= 0:
            nsum = int(num[n]) + is_incre
            if n == len_num - 1:
                nsum += 1
            if nsum >= 10:
                if n == 0:
                    is_overflow = True
                else:
                    is_incre = 1
                    nsum = nsum % 10
                    num[n] = str(nsum)
            else:
                num[n] = str(nsum)
            n -= 1
        return is_overflow

class Solution1:
    def Increment(self, number):
        isOverflow = False
        flag = 0
        lenth = len(number)
        n = lenth - 1
        while n >= 0:
            nSum = int(number[n]) + flag
            if n == lenth - 1:
                nSum += 1
            if nSum >= 10:
                if n == 0:
                    isOverflow = True
                else:
                    flag = 1
                    nSum = nSum % 10
                    number[n] = str(nSum)
            else:
                number[n] = str(nSum)
            n -= 1
        return isOverflow

    def PrintNumber(self, number):
        isBegin = False
        lenth = len(number)
        for i in range(lenth):
            if number[i] != '0' and isBegin is False:
                isBegin = True
            if isBegin:
                tmp = ("".join(number[i:]))
                print(tmp)
                break

    def Print1ToMaxOfNDigits(self, n):
        if n <= 0:
            return
        number = ['0'] * n
        while self.Increment(number) is False:
            self.PrintNumber(number)


if __name__ == '__main__':
    s = Solution()
    t = Solution1()
    print(s.print_n(3))
    # print(t.Print1ToMaxOfNDigits(3))

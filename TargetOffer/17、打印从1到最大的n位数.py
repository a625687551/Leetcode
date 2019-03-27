# -*- coding:utf-8 -*-
"""
题目：输入数字N，按顺序打印出从1到最大的n位十进制数，比如输入3则打印出从1,2,3到999
这里面需要考虑大数字问题，考虑溢出问题
"""


class Solution:
    def print_n(self, n):
        """这个主要考虑数据溢出处理问题"""
        if n <= 0:
            return
        list_num = ["0"] * n
        while self.increament(list_num) is False:
            self.print_num(list_num)

    def print_num(self, num):
        for i, v in enumerate(num):
            if v != "0":
                print("".join(num[i:]))
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
    # print(s.print_n(3))
    # print(t.Print1ToMaxOfNDigits(3))

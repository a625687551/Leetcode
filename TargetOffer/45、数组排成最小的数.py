# -*- coding:utf-8 -*-
"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""
import operator


class Solution:
    def PrintMinNumber(self, numbers):
        # # 这里的方法适合于python2.7,对于python3需要修改
        # if not numbers:
        #     return ""
        # lam = lambda n1, n2: int(str(n1) + str(n2)) - int(str(n2) + str(n1))
        # array = sorted(numbers, cmp=lam)
        # return "".join([str(i) for i in array])
        # python 3
        if not numbers:
            return ""
        lam = lambda n1, n2: int(str(n1) + str(n2)) - int(str(n2) + str(n1))
        array = sorted(numbers, key=lambda x, y: x + 6)
        return "".join(array)


if __name__ == '__main__':
    s = Solution()
    print(s.PrintMinNumber([3, 32, 321]))

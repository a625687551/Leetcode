# -*- coding:utf-8 -*-
"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""
import functools


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
        array = sorted(numbers, key=functools.cmp_to_key(lambda x, y: int(str(x) + str(y)) - int(str(y) + str(x))))
        return "".join(map(str, array))

    def print_min_num(self, numbers):
        """自定义的快速排序算法,这个本质上另类的快排"""
        if not numbers:
            return ""
        nums = list(map(str, numbers))
        return "".join(self.quick_sort(nums))

    def quick_sort(self, number):
        if len(number) < 2:
            return number[:]
        left = self.quick_sort([i for i in number[1:] if i + number[0] <= number[0] + i])
        right = self.quick_sort([i for i in number[1:] if i + number[0] > number[0] + i])
        return left + [number[0]] + right


if __name__ == '__main__':
    s = Solution()
    # print(s.PrintMinNumber([3, 32, 321]))
    print(s.print_min_num([3, 32, 321]))
    print(s.print_min_num([3, 5, 1, 4, 2]))
    # print(s.PrintMinNumber([3, 5, 1, 4, 2]))

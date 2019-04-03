# -*- coding:utf-8 -*-

"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变
PS 比较坑的是这个要求相对位置不能变化
"""


class Solution:
    def reOrderArray(self, array):
        if not array:
            return []
        odd = []
        even = []
        for i in array:
            if i & 1:
                odd.append(i)
            else:
                even.append(i)
        odd.extend(even)
        return odd

    def odd_before_even_resort(self, array):
        """双指针，ab从头尾巴往中间走，a++一直遇到偶数停止，b--一直遇到奇数，然后交换再继续"""
        if not array:
            return []
        start = 0
        end = len(array) - 1
        while start < end:
            print(start, end)
            while start < end and self.judge(array[start]):
                start += 1
            while start < end and not self.judge(array[end]):
                end -= 1
            if start < end:
                array[start], array[end] = array[end], array[start]
        return array

    def odd_before_even_normal(self, array):
        """bad one """
        if not array:
            return []
        odd, even = len(array) - 1, len(array) - 1
        while odd >= 0 and even >= 0:
            print(array)
            while even > 0 and not self.judge(array[even]):
                even -= 1
            if self.judge(array[even]):
                array[even], array[even - 1] = array[even - 1], array[even]
                odd = even
        return array

    def judge(self, number):
        """用异或来判断，异或结果是0 则是偶数，奇数1"""
        return number & 1


if __name__ == '__main__':
    lst = [[], [1], [1, 3, 5, 7, 9, 8, 6, 4, 2], [2, 4, 6, 8, 9, 7, 5, 3, 1], [1, 2, 3, 5, 4, 6, 7, 3, 5, 6]]
    s = Solution()
    # print(s.reOrderArray([4, 5, 6, 7, 8]))
    print(s.odd_before_even_resort([4, 5, 6, 7, 8]))
    # print(s.odd_before_even_normal([4, 5, 6, 7, 8]))
    # for x in lst:
    #     print(s.odd_before_even(x))

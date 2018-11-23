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
        # start = 0
        # end = len(array) - 1
        # while start < end:
        #     while start < end and self.judge(array[start]):
        #         start += 1
        #     while start < end and not self.judge(array[end]):
        #         end -= 1
        #     if start < end:
        #         array[start], array[end] = array[end], array[start]
        # return array
        odd = []
        even = []
        for i in array:
            if i & 1:
                odd.append(i)
            else:
                even.append(i)
        array = odd.extend(even)
        return array

    def judge(self, number):
        """用异或来判断，异或结果是0 则是偶数，奇数1"""
        return number & 1


if __name__ == '__main__':
    s = Solution()
    print(s.reOrderArray([4, 5, 6, 7, 8]))

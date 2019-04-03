# -*- coding:utf-8 -*-
"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0
"""


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # 桶排序O(k)的空间
        if not numbers:
            return 0
        num_dict = {}
        for x in numbers:
            if x in num_dict:
                num_dict[x] += 1
            else:
                num_dict[x] = 1
        for j in num_dict:
            if num_dict[j] > (len(numbers) // 2):
                return j
        return 0

    def solution_2(self, data):
        if not data:
            return []
        a = [data[0], 1]
        for k, v in enumerate(data[1:]):
            if a[0] == v:
                a[1] += 1
            elif a[0] != v and a[1] > 0:
                a[1] -= 1
            else:
                a = [v, 1]
        return a


if __name__ == '__main__':
    s = Solution()
    print(s.MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2]))
    print(s.solution_2([1, 2, 3, 2, 2, 2, 5, 4, 2]))

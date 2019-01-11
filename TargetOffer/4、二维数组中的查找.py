# -*- coding: utf-8 -*-

"""
已知一个二维数组，横向纵向都是递增的，例如：
1 2 3 4
2 3 4 5
3 4 5 6
5 6 7 8
查找其中的一个数，有则返回，无则返回None

算法1，为简单起见，只要求返回一个满足要求的元素
可以观察到，每次选取右上角的元素a是个很好的二分的方法，如果target<a，那么a
所在的列可以不用搜索了，如果target>a,那么a所在的行不用搜索了
可以分析 算法复杂度为O(2n)
"""


class Solution:
    # array 二维列表
    def Find(self, target, array):
        if not array:
            return False
        if len(array) == 1 and not array[0][0]:
            return False
        raw_num = len(array)
        col_num = len(array[0])

        # if isinstance(target, int) and isinstance(array[0][0], int):
        #     target = int(target)
        # elif isinstance(target, int) and isinstance(array[0][0], float):
        #     target = float(target)
        # elif type(target) != type(array[0][0]):
        #     return False
        if isinstance(target, (int, float)):
            target = type(array[0][0])(target)

        i = col_num - 1
        j = 0
        while i >= 0 and j < raw_num:
            if array[j][i] < target:
                j += 1
            elif array[j][i] > target:
                i -= 1
            else:
                return True
        return False

array = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]
array2 = []
array3 = [['a', 'b', 'c'],
          ['b', 'c', 'd']]
array4 = [[1, 2, 8, 9],
          [4, 7, 10, 13]]
array5 = [[]]
findtarget = Solution()
print(findtarget.Find(7, array5))
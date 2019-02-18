# -*- coding: utf-8 -*-

"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，
输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
思路：
双指针 
"""


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        i, j = 0, len(rotateArray) - 1
        while i < j:
            mid = (i + j) // 2
            if j - i == 1:
                return rotateArray[j]
            if rotateArray[i] < rotateArray[mid]:
                i = mid
            elif rotateArray[j] > rotateArray[mid]:
                j = mid
            else:
                return rotateArray[mid]


if __name__ == '__main__':
    s = Solution()
    print(s.minNumberInRotateArray([3, 4, 5, 1, 2]))
    print(s.minNumberInRotateArray([4, 5, 1, 2, 3]))

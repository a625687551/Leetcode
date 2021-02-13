# !/usr/bin/env python
# coding: utf-8


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        todo: 这里对栈的使用不熟悉
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums2 or not nums1:
            return []
        temp_dict = {}
        result = []
        for i in range(len(nums2)):
            while result and result[-1] < nums2[i]:
                temp_dict[result.pop()] = nums2[i]
            result.append(nums2[i])
        print(result, temp_dict)
        return [temp_dict.get(x, -1) for x in nums1]


if __name__ == '__main__':
    n1 = [4, 1, 2]
    n2 = [1, 3, 4, 2]
    s = Solution()
    print(s.nextGreaterElement(n1, n2))

# ！/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: List[int]) -> List[int]:
        """
        :param nums:
        :param target:
        :return:
        """
        temp_dict = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in temp_dict.keys():
                return [temp_dict[diff], index]
            else:
                temp_dict[value] = index


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))

# ！/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = {}
        for k, value in enumerate(nums):
        	diff = target - value
	        if(diff in s.keys()):
	        	return [s[diff], k]
	       	else:
	       		s[value] = k

if __name__ == '__main__':
	nums = [2, 7, 11, 15]
	target = 9
	s = Solution()
	print(s.twoSum(nums, target))

        
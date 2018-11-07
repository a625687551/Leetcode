# !/usr/bin/env python
# coding:utf-8

from collections import OrderedDict

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = OrderedDict.fromkeys(nums)
        return len(nums)

if __name__ == '__main__':
	a = [1,1,2]
	sol = Solution()
	print(sol.removeDuplicates(a))
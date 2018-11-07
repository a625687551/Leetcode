# !/usr/bin/env python
# coding:utf-8

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while  val in nums:
        	nums.remove(val)
        return nums


if __name__ == '__main__':
	main()
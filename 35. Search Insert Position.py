# !/usr/bin/env python
# coding:utf-8


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return bisect.bisect_left(nums, target)
        # return len([x for x in nums if x<target])


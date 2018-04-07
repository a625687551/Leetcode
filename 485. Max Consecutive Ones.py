# !/usr/bin/env python
# coding: utf-8


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = 0
        now = 0
        for i in nums:
            if i == 1:
                now += 1
                last = max(now, last)
            else:
                now = 0
        return last
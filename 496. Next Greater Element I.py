# !/usr/bin/env python
# coding: utf-8


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return [next((y for y in nums2[nums2.index(x):]if y>x), -1) for x in nums1]

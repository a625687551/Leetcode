# !/usr/bin/env python
# coding: utf-8


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bit(x^y).count("1")
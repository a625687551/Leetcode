# !/usr/bin/env python
# coding: utf-8

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while num >= i:
            num ^= i
            i <<= 1
        return num

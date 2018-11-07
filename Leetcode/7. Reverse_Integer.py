# !/usr/bin/env python
# coding: utf-8


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = (x > 0) - (x < 0)
        r = int(str(x * s)[::-1])
        return s * r * (r < 2 ** 31)

# !/usr/bin/env python
# coding: utf-8

import math

class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        mid = int(math.sqrt(area))
        while area % mid !=0:
            mid -= 1
        return [area//mid, mid]
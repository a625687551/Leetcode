# ！/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum([b-a for a, b in zip(prices,prices[1:]) if b>a])

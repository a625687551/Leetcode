# !/usr/bin/env python
# coding: utf-8


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r = num
        while r*r >num:
            r = (r + num/r)/2
        return int(r*r) == num


if __name__ == "__main__":
    s = Solution()
    print(s.isPerfectSquare(5))

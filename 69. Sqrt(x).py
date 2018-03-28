# !/usr/bin/env python
# coding:utf-8


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        g = 0
        while r * r > x:
            r = (r + x / r) / 2
            print(r)
            if abs(g - r) < 0.001:
                break
            g = r

        return int(r)

if __name__ == '__main__':
    a = 8
    s = Solution()
    print(s.mySqrt(a))
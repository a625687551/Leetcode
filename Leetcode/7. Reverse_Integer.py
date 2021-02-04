# !/usr/bin/env python
# coding: utf-8


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 正负标志符
        sign = (x > 0) - (x < 0)
        temp = int(str(sign * x)[::-1])
        return temp * sign * (temp < 2 ** 31)


if __name__ == '__main__':
    num = -123
    s = Solution()
    print(s.reverse(num))

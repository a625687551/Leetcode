# -*- coding:utf-8 -*-
"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""


class Solution:
    def NumberOf1(self, n):
        if not isinstance(n, int):
            return None
        n = abs(n)
        return sum([n >> i & 1 for i in range(64)])


if __name__ == '__main__':
    s = Solution()
    print(s.NumberOf1(12))
    print(s.NumberOf1(0))
    print(s.NumberOf1("145345"))
    print(s.NumberOf1(-1))

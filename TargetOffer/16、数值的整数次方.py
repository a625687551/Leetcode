# -*- coding:utf-8 -*-


class Solution:
    def Power(self, base, exponent):
        if not base:
            return 0.0
        if not exponent:
            return 1.0
        result = 1.0
        abs_exponent = abs(exponent)
        for x in range(abs_exponent):
            result *= base
        if exponent < 0:
            return 1.0 / result
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.Power(2, 5))

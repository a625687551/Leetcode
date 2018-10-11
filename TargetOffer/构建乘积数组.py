# !usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
下三角用连乘可以很容求得，上三角，从下向上也是连乘。
因此我们的思路就很清晰了，先算下三角中的连乘，即我们先算出B[i]中的一部分，
然后倒过来按上三角中的分布规律，把另一部分也乘进去。
"""


class Solution:
    def multiply(self, A):
        if not A:
            return []
        length_a = len(A)
        b = [None] * length_a
        b[0] = 1
        for i in range(1, length_a):
            b[i] = b[i - 1] * A[i - 1]
        tmp = 1
        for i in range(len(A) - 2, -1, -1):
            tmp = tmp * A[i + 1]
            b[i] = b[i] * tmp
        return b


if __name__ == '__main__':
    s = Solution()
    print(s.multiply([1, 2, 3, 4, 5]))

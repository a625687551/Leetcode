# -*- coding: utf-8 -*-

"""
题目：请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
思路：
1、递归：递归的复杂度以N的指数级别增长的，很多节点是重复的，重复的节点数随着N的增加而急剧增加
2、保存中间项，减少重复计算O（n)
"""


class Solution:
    def fibonacci_recursive(self, n):
        """递归"""
        if n <= 0:
            return 0
        if n == 1:
            return 1
        return self.fibonacci_recursive(n - 1) + self.fibonacci_recursive(n - 2)

    def Fibonacci(self, n):
        """保存中间项1"""
        if n <= 0:
            return 0
        temp = [0, 1]
        if n >= 2:
            for i in range(2, n + 1):
                temp[i % 2] = temp[0] + temp[1]
        return temp[n % 2]

    def fibonacci_1(self, n):
        """保存中间项2"""
        if n <= 0:
            return 0
        if n == 1:
            return 1
        temp = [0, 1]
        if n >= 2:
            for i in range(2, n+1):
                temp.append(temp[-1] + temp[-2])
        print(temp)
        return temp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.Fibonacci(10))
    print(s.fibonacci_1(10))
    # print(s.fibonacci_recursive(10))

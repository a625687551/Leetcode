# -*- coding:utf-8 -*-
"""
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
思路：
1、递归的调用加函数
2、虚函数求解
3、函数指针求解
4、模板类型求解
"""


class Solution:
    def Sum_Solution(self, n):
        result = (n > 0) and (n + self.Sum_Solution(n - 1))
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.Sum_Solution(10))
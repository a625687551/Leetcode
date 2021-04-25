# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 7:44 上午
# @Author  : wangjianfeng
# @File    : 42. 接雨水.py

from typing import List, Dict


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        stack = []
        sum, top = 0, 0
        for index, x in enumerate(height):
            if x > top:
                top = x
                # 计算一次面积
                if len(stack) > 1:
                    print(stack, )
                    temp = stack[0] * len(stack)
                    sum += temp
                stack = [top]

            else:
                stack.append(x)
        return sum


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    s = Solution()
    print(s.trap(height))

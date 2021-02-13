# -*- coding: utf-8 -*-
# @Time    : 2021/2/13 7:35 下午
# @Author  : wangjianfeng
# @File    : 682. Baseball Game.py
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        if not ops:
            return 0
        temp_list = []
        result = 0
        for i in ops:
            if i.lstrip("-").isnumeric():
                i = int(i)
                result += i
                temp_list.append(i)
            elif i == "+":
                temp = temp_list[-1] + temp_list[-2]
                result += temp
                temp_list.append(temp)
            elif i == "D":
                result += temp_list[-1] * 2
                temp_list.append(temp_list[-1] * 2)
            elif i == "C":
                result -= temp_list[-1]
                temp_list.pop()
            else:
                pass
        return result


if __name__ == '__main__':
    # ops = ["5", "2", "C", "D", "+"]
    ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    s = Solution()
    print(s.calPoints(ops))

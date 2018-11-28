# -*- coding:utf-8 -*-
"""
在一个m*n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值〈价值大于 0).  你可以从棋盘的左上角开始拿格子里的礼物，井
每次向左或者向下移动一格，直到到达棋盘的右下角。给定一个棋盘及其上面的礼物，计算你最多能拿到多少价值的礼物?
动态规划问题
"""


class Solution:
    def max_no_repetition(self, target):
        positon = {}
        cur_length = 0
        max_length = 0
        length = len(target)
        for i in range(length):
            pre_index = positon.get(target[i], -1)
            if pre_index < 0 or i - pre_index > cur_length:
                cur_length += 1
            else:
                if cur_length > max_length:
                    max_length = cur_length
                cur_length = i - pre_index
            positon[target[i]] = i
        if cur_length > max_length:
            max_length = cur_length
        return max_length


if __name__ == '__main__':
    s = Solution()
    print(s.max_no_repetition("arabcacfr"))

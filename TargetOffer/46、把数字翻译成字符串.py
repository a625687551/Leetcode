# -*- coding:utf-8 -*-
"""
在一个m*n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值〈价值大于 0).  你可以从棋盘的左上角开始拿格子里的礼物，井
每次向左或者向下移动一格，直到到达棋盘的右下角。给定一个棋盘及其上面的礼物，计算你最多能拿到多少价值的礼物?
动态规划问题
"""


class Solution:
    def trans_num_str(self, numbers):
        if numbers < 0:
            return 0
        str_num = str(numbers)
        return self.get_trans_count(str_num)

    def get_trans_count(self, str_num):
        length = len(str_num)
        counts = [0]*length
        for i in range(length - 1, -1, -1):
            if i < length - 1:
                count = counts[i + 1]
            else:
                count = 1

            if i < length - 1:
                digit1 = int(str_num[i])
                digit2 = int(str_num[i + 1])
                covered = digit1 * 10 + digit2
                if 10 <= covered <= 25:
                    if i < length - 2:
                        count += counts[i + 2]
                    else:
                        count += 1
            # print(count, i)
            counts[i] = count
        # print(counts)
        return counts[0]


if __name__ == '__main__':
    s = Solution()
    print(s.trans_num_str(12258))

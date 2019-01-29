# -*- coding:utf-8 -*-
"""
给定一个数字，按照如下规则翻译成字符串：0翻译成“a”，1翻译成“b”...25翻译成“z”。一个数字有多种翻译可能，
例如12258一共有5种，分别是bccfi，bwfi，bczi，mcfi，mzi。实现一个函数，用来计算一个数字有多少种不同的翻译方法。
动态规划问题
12258
                   /       \
              b+2258       m+258
              /   \         /   \
          bc+258 bw+58  mc+58  mz+8
          /  \      \        \     \
      bcc+58 bcz+8   bwf+8   mcf+8  mzi
        /        \       \     \
   bccf+8        bczi    bwfi   mcfi
     /
 bccfi

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

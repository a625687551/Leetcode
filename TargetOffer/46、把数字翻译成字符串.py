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
自下而上，也可以叫从右往左，动态规划，从最小的问题开始 ：
f(r)表示以r为开始（r最小取0）到最右端所组成的数字能够翻译成字符串的种数。对于长度为n的数字，f(n)=0,f(n-1)=1,求f(0)。
递推公式(转移矩阵)为 f(r-2) = f(r-1)+g(r-2,r-1)*f(r)；
其中，如果r-2，r-1能够翻译成字符，则g(r-2,r-1)=1，否则为0。
因此，对于12258：
f(5) = 0
f(4) = 1
f(3) = f(4)+0 = 1
f(2) = f(3)+f(4) = 2
f(1) = f(2)+f(3) = 3
f(0) = f(1)+f(2) = 5
作者：ryderchan
链接：https://www.jianshu.com/p/80e1841909b7
"""


class Solution:
    def trans_num_str(self, numbers):
        if numbers < 0:
            return 0
        str_num = str(numbers)
        print("old", self.get_trans_count(str_num))
        print("new", self.get_trans_count_2(str_num))
        return self.get_trans_count(str_num)

    def get_trans_count(self, str_num):
        length = len(str_num)
        counts = [0] * length
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

    def get_trans_count_2(self, str_num):
        length = len(str_num)
        res = [0]*(length-1) + [1, 1]
        for i in range(length - 2, -1, -1):
            # if "{}{}".format(str_num[i], str_num[i+1]) < "26":
            if str_num[i:i + 2] < "26":
                g = 1
            else:
                g = 0
            res[i] = res[i+1] + res[i+2]*g
        return res[0]

    def get_tran_count_3(self, num):
        """自前向后，类似爬楼梯"""
        size = len(num)
        if size <= 1:
            return 1
        dp = [0] * size
        dp[0] = 1
        dp[1] = 2 if 10 <= int(num[:2]) < 26 else 1
        for i in range(2, size):
            dp[i] = dp[i-1] + dp[i-2] if 10 <= int(num[i-1:i+1]) < 26 else dp[i-1]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    s.trans_num_str(12258)
    print(s.get_tran_count_3("12818"))

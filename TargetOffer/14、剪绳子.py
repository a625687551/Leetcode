# -*- coding:utf-8 -*-
"""
给你一根长度为n的绳子，请把绳子剪成m段 (m和n都是整数，n>1并且m>1)每段绳子的长度记为k[0],k[1],…,k[m].
请问k[0]k[1]…*k[m]可能的最大乘积是多少？例如，当绳子的长度为8时，我们把它剪成长度分别为2,3,3的三段，此时得到的最大乘积是18.
思路：两种方案
1、动态规划：O（n2)时间和O(n)的空间
2、贪婪算法：O（1）时间和空间
"""


class Solution:
    def max_cut_1(self, s_length):
        """动态规划"""
        if s_length < 2:
            return 0
        if s_length == 2:
            return 1
        if s_length == 3:
            return 2
        li = [0, 1, 2, 3]
        for i in range(4, s_length + 1):
            max_num = 0
            for j in range(1, i):
                temp = li[j] * li[i - j]
                if temp > max_num:
                    max_num = temp
            li.append(max_num)
        return li[-1]

    def max_cut_2(self, s_length):
        """贪婪算法，当n>=5时候尽可能的切成长度为3的绳子，n=4的时候尽可能切成2*2的绳子"""
        if s_length < 2:
            return 0
        if s_length == 2:
            return 1
        if s_length == 3:
            return 2
        time_three = s_length // 3

        if s_length - time_three*3 == 1:
            time_three -= 1
        time_two = (s_length - time_three*3) // 2
        return 3**time_three*2**time_two

if __name__ == '__main__':
    s = Solution()
    print(s.max_cut_1(8))
    print(s.max_cut_2(8))

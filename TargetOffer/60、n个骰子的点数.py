# -*- coding:utf-8 -*-
"""
一、例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。
Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
二、汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,
要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
"""


class Solution:
    def max_dice_point(self, n):
        if n < 1:
            return None
        dp = [[0 for x in range(6 * n)] for y in range(n)]
        for i in range(6):
            dp[0][i] = 1
        for i in range(1, n):
            for j in range(i, 6 * (i + 1)):
                dp[i][j] = dp[i - 1][j - 6] + dp[i - 1][j - 5] + dp[i - 1][j - 4] + dp[i - 1][j - 3] + dp[i - 1][
                    j - 2] + dp[i - 1][j - 1]
        count = dp[n-1]
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.max_dice_point(1))

# -*- coding:utf-8 -*-
"""
一、例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。
Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
二、汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,
要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
"""


class Solution:
    def rotate_string(self, s):
        if not s:
            return None
        return " ".join(s.split(" ")[::-1])

    def LeftRotateString(self, s, n):
        if not s:
            return ""
        length = len(s)
        if n >= length:
            n = n % length
        s = s[::-1]
        print(s)
        first = ""
        second = ""
        for i in range(length - n):
            first += s[i]
        first = first[::-1]
        for j in range(length - n, length, 1):
            second += s[j]
        second = second[::-1]
        return first + second

if __name__ == '__main__':
    s = Solution()
    # print(s.LeftRotateString("abcdefg", 7))
    print(s.rotate_string("student. a am I"))
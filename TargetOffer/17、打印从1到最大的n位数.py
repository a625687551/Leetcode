# -*- coding:utf-8 -*-
"""
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
"""


class Solution:
    def match(self, s, pattern):
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.match("a", ".*"))

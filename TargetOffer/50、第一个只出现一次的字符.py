# -*- coding:utf-8 -*-
"""
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 
如果没有则返回 -1（需要区分大小写）."""


class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1
        str_dict = {}
        for x in s:
            str_dict[x] = str_dict.get(x, 0) + 1
        for i, key in enumerate(s):
            if str_dict[key] == 1:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.FirstNotRepeatingChar("google"))

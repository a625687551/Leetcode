# !/usr/bin/env python
# coding: utf-8


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length<2:
            return s
        res = ""
        for i in range(length):
            res = max(self.helper(s,i,i), self.helper(s,i,i+1),res, key=len)
        return res

    def helper(self, s, l, r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

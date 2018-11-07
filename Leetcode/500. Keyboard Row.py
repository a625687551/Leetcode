# !/usr/bin/env python
# coding: utf-8

import re


class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)
        a=set('qwertyuiop')
        b=set('asdfghjkl')
        c=set('zxcvbnm')
        ans = []
        for word in words:
            w = set(word.lower())
            if ((w&a==w)|(w&b==w)|(w&c==w)):
                ans.append(word)
        return ans

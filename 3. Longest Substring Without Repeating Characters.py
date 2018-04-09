# !/usr/bin/env python
# coding: utf-8


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = max_length = 0
        used = {}

        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i-start+1)
            used[c] = i
        return max_length
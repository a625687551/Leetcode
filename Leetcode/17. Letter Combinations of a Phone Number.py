# !/usr/bin/env python
# coding: utf-8

from functools import reduce

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        kvmaps = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        return reduce(lambda a, digit:[x + y for x in a for y in kvmaps[digit]], digits, [""])
        # return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits)
        # return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])

s = Solution()
print(s.letterCombinations("34"))
# !/usr/bin/env python
# coding:utf-8


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        result = 0
        for x in range(0, len(s) - 1):
        	if roman[s[x]] < roman[s[x+1]]:
        		result -= roman[s[x]]
        	else:
        		result += roman[s[x]]
        return result + roman[s[-1]]

if __name__ == '__main__':
	s = "DCXXI"
	sol = Solution()
	print(sol.romanToInt(s))

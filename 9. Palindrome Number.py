# ！/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        
        ranger = 1        
        while x//ranger >=10:
            ranger *= 10
        
        while x:
            left = x//ranger
            right = x%10
            if left != right:
                return False
            
            x = (x%ranger)//10
            ranger //= 100
            
        return True

    def anothor(self, x):
    	return int(str(abs(x))[::-1]) == x

if __name__ == '__main__':
	x = 11

        
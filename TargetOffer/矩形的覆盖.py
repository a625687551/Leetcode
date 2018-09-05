# !usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def rectCover(self, number):
        # write code here
        if number < 1:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            return self.rectCover(number - 1) + self.rectCover(number - 2)


s = Solution()
print(s.rectCover(10))

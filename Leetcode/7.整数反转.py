#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x
        is_neg = 1 if x < 0 else 0
        x = abs(x)
        result = 0
        while x != 0:
            x, num = divmod(x, 10)
            result = result*10+num
            if result > 2**31-1 or result < -2**31: 
                return 0
                
        return -result if is_neg else result
# @lc code=end



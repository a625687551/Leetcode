#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if not n: 
            return 0
        res = dict()
        res[1] = 1
        res[2] = 2
        for i in range(3, n+1):
            res[i] = res[i-2]+ res[i-1]
        return res[n]
# @lc code=end


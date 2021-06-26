#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
# 这个和72编辑距离有异曲同工之妙，一个是正序一个是逆序
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n: 
            return 0
        dp = [[0]*(n + 1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][n] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j] + dp[i+1][j+1]
                else:
                    dp[i][j] = dp[i+1][j]
        return dp[0][0]


        
# @lc code=end

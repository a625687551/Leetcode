#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        size = len(s)
        dp = [[True]*size for _ in range(size)]
        for i in range(size-1, -1, -1):
            for j in range(i+1, size):
                dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
        f = [float("inf")] * size
        for i in range(size):
            if dp[0][i]:
                f[i] = 0
            else:
                for j in range(i):
                    if dp[j+1][i]:
                        f[i] = min(f[i], f[j] + 1)
        return f[size -1]
# @lc code=end


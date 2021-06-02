#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: 
            return 0
        size = len(s)
        dp = [0]*size
        max_val = 0
        for i in range(1, size):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = dp[i-2] + 2 if i-2>=0 else 2
                elif i-dp[i-1]>0 and s[i-dp[i-1]-1] == "(":
                    if i-dp[i-1] >= 2:
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                    else:
                        dp[i] = dp[i-1] + 2
                max_val = max(dp[i], max_val) 
        return max_val

# @lc code=end


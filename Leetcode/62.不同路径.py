#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = [[1]*n] + [[1] + [0]*(n-1) for _ in range(m-1)]
        for i in range(1, m): 
            for j in range(1, n):
               result[i][j] = result[i - 1][j] + result[i][j-1]
        return result[m-1][n-1]
# @lc code=end


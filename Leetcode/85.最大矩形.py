#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = 1 if j == 0 else dp[i][j-1] + 1

        ret = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                width = dp[i][j]
                area = width
                for k in range(i-1, -1, -1):
                    width = min(width, dp[k][j])
                    area = max(area, (i-k+1)*width)
                ret = max(ret, area)
        return ret
# @lc code=end


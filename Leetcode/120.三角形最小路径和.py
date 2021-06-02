#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        res = [[0]*m for _ in range(m)]
        # start point
        res[0][0] = triangle[0][0]   
        for i in range(1, m):
            res[i][0] = res[i-1][0] + triangle[i][0]
            for j in range(1, i):
                res[i][j] = min(res[i-1][j-1], res[i-1][j]) + triangle[i][j] 
            res[i][i] = res[i-1][i-1] + triangle[i][i]
        return min(res[-1])
# @lc code=end


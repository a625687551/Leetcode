#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
from typing import List
# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            if obstacleGrid[0][i] != 1:
                res[0][i] = 1
            if obstacleGrid[0][i] == 1:
                break
        for j in range(m):
            if obstacleGrid[j][0] !=1:
                res[j][0] = 1
            if obstacleGrid[j][0] ==1:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                    continue
                res[i][j] = res[i-1][j] + res[i][j-1]
        return res[-1][-1]      

# @lc code=end
if __name__ == '__main__':
    a = [[0,1],[0,0]]
    s = Solution()
    print(s.uniquePathsWithObstacles(a))


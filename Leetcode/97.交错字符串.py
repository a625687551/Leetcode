#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n,t = len(s1), len(s2), len(s3)
        if m+n != t: 
            return False
        res = [[False]*(n+1) for _ in range(m+1)]
        res[0][0] = True
        # 遍历第一行
        for i in range(1, n+1): 
            res[0][i] = res[0][i-1] and s2[i-1] == s3[i-1]
        # 遍历第一列
        for j in range(1, m+1):
            res[j][0] = res[j-1][0] and s1[j-1] == s3[j-1]
        # 遍历其他
        for i in range(1, m+1):
            for j in range(1, n+1):
                res[i][j] = (res[i - 1][j] and s1[i-1] == s3[i+j-1]) or (res[i][j-1] and s2[j-1] == s3[i+j-1])
        return res[-1][-1]
# @lc code=end


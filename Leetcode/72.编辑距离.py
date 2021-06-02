#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        # print(dp)
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j
        # print(dp)
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j-1], 
                        dp[i][j-1],
                        dp[i-1][j]
                        )+1
        return dp[-1][-1]

    def minDistance2(self, word1: str, word2: str) -> int:
        memo_dict = dict()
        def dp(i,j): 
            if i == -1: return j+1
            if j == -1: return i+1
            if (i, j) in memo_dict:
                return memo_dict[(i, j)]
            if word1[i] == word2[j]:
                memo_dict[(i, j)] = dp(i-1, j-1)
            else: 
                memo_dict[(i, j)] = min(
                    # 插入
                    dp(i, j-1)+1,
                    # 删除
                    dp(i-1,j)+1,
                    # 替换
                    dp(i-1, j-1) + 1
                )
            return memo_dict[(i, j)]
        return dp(len(word1)-1 , len(word2)-1)

    def minDistance1(self, word1: str, word2: str) -> int:
        def dp(i,j): 
            if i == -1: return j+1
            if j == -1: return i+1
            if word1[i] == word2[j]:
                return dp(i-1, j-1)
            else: 
                return min(
                    # 插入
                    dp(i, j-1)+1,
                    # 删除
                    dp(i-1,j)+1,
                    # 替换
                    dp(i-1, j-1) + 1
                )
        return dp(len(word1)-1 , len(word2)-1)
    
# @lc code=end


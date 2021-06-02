#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
from typing import List
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True
        return dp[-1]

# @lc code=end
if __name__ == '__main__':
    s = "leetcode"
    ws = ["leet","code"]
    ss = Solution()
    print(ss.wordBreak(s, ws))
    


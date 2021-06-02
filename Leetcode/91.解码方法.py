#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: 
            return 0
        size = len(s)
        res = [1] + [0]*size
        for i in range(1, size+1):
            # 位置不是0
            if s[i-1] != "0":
                res[i] += res[i-1]
            if i>1 and s[i-2] != "0" and int(s[i-2:i])<=26:
                res[i] += res[i-2]
        return res[size]
        

# @lc code=end


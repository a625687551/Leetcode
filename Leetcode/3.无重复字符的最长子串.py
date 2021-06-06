#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        size = len(s)
        l, res = -1, 0
        for i in range(size):
            if i!=0:
                occ.remove(s[i-1])
            while l+1 < size and s[l+1] not in occ:
                occ.add(s[l+1])
                l += 1
            res = max(res, l-i+1)
        return res
            


# @lc code=end


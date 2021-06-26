#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window, need = dict(), dict()
        for i in p:
            need[i] = need.get(i, 0) + 1
        left, right = 0, 0
        vaild = 0
        res = []
        while(right < len(s)): 
            c = s[right]
            right += 1
            if need.get(c):
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    vaild += 1
        
            while(right - left >= len(p)):
                if (vaild == len(need)):
                    res.append(left)
                d = s[left]
                left += 1
                if need.get(d):
                    if window[d] == need[d]:
                        vaild -= 1
                    window[d] -= 1
        return res

# @lc code=end


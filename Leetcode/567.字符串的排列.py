#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window, need = dict(), dict()
        for i in s1: 
            need[i] = need.get(i, 0) + 1
        left, right = 0, 0
        vaild = 0
        while(right <len(s2)):
            c = s2[right]
            right += 1
            if need.get(c):
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    vaild += 1

            while(right - left >=len(s1)):
                if (vaild == len(need)):
                    return True
                d = s2[left]
                left += 1
                if need.get(d):
                    if window[d] == need[d]:
                        vaild -=1
                    window[d] -= 1
        return False


# @lc code=end


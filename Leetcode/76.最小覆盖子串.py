#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, window = dict(), dict()
        size_s, size_t = len(s), len(t)
        left, right, vaild = 0, 0, 0
        start, length = 0, 1e5
        # 遍历组成字典
        for i in t:
            need[i] = need.get(i, 0) + 1
        # 开始向右窗口滑动
        while(right < size_s):
            temp = s[right]
            right += 1
            # 更新字典
            if need.get(temp):
                window[temp] = window.get(temp, 0) + 1
                if window[temp] == need[temp]:
                    vaild += 1
            # 缩小窗口
            while (vaild == len(need)):
                if (right - left < length):
                    start = left
                    length = right - left
                
                temp_left = s[left]
                left += 1

                if need.get(temp_left):
                    if window[temp_left] == need[temp_left]:
                        vaild -= 1
                    window[temp_left] -= 1
        return "" if length ==  1e5 else s[start:start + length]


# @lc code=end


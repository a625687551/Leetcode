#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        if not s: 
            return res
        for i in range(len(s)+1):
            # 处理奇数回文
            s1 = self.find_one_parlindrome(s, i, i)
            # 处理偶会文
            s2 = self.find_one_parlindrome(s, i, i+1)
            res = res if len(res)>=len(s1) else s1
            res = res if len(res)>=len(s2) else s2

        return res

    def find_one_parlindrome(self, s, left, right):
        while left>=0 and right<len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
# @lc code=end
# if __name__ == "__main__":
#     a = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
#     sss = Solution()
#     print(sss.longestPalindrome(a))


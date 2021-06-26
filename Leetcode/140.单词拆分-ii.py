#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def back_track(index):
            if index == len(s):
                return [[]]
            res = list()
            for i in range(index + 1, len(s)+1):
                word = s[index:i]
                if word in wordDict:
                    next_word_breaks = back_track(i)
                    for next in next_word_breaks:
                        res.append(next.copy() + [word])
            return res
        word_set = set()
        break_list = back_track(0)
        return [" ".join(words[::-1]) for words in break_list]
# @lc code=end


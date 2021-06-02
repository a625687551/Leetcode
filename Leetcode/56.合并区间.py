#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        for inter in intervals:
            if not result or result[-1][1] < inter[0]:
                result.append(inter)
            else:
                result[-1][1] = max(result[-1][1], inter[1])
        return result

# @lc code=end

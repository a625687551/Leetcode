#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
from typing import List
# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not newInterval:
            return intervals
        res = []
        left, right = newInterval
        is_in = False
        for l, r in intervals:
            if r < left:
                res.append([l, r])
            elif l >right:
                if not is_in:
                    res.append([left, right])
                    is_in = True
                res.append([l, r])
            else:
                left = min(left, l)
                right = max(right, r)
        # 如果最后都没有插入，那就放到最后
        if not is_in:
            res.append([left, right])
        return res
# @lc code=end
if __name__ == '__main__':
    a = [[1,3],[6,9]]
    b = [2,5]
    s = Solution()
    print(s.insert(a, b))


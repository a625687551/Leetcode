#
# @lc app=leetcode.cn id=164 lang=python3
#
# [164] 最大间距
#

# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        size = len(nums)
        if size < 2:
            return res
        else:
            res = nums[1] - nums[0]
            for i in range(1, size-1):
                res = max(res, nums[i+1]-nums[i])
            return res
# @lc code=end


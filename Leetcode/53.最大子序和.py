#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        max_result = nums[0]
        for x in nums:
            pre = max(pre+x, x)
            max_result = max(max_result, pre)
        return max_result
# @lc code=end


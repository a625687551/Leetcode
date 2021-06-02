#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        size = len(nums)
        dp = [0]*size
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, size):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[size-1]
# @lc code=end


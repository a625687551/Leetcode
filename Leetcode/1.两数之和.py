#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dp = {}
        for index, value in enumerate(nums):
            if target - value in dp.keys():
                return [dp[target-value], index]
            else:
                dp[value] = index
# @lc code=end


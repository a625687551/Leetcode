#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        size = len(nums)
        dp_max = [0]*size
        dp_min = [0]*size
        dp_max[0],dp_min[0] = nums[0], nums[0]
        for i in range(1, size):
            dp_max[i] = max(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
            dp_min[i] = min(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
        return max(dp_max)
# @lc code=end


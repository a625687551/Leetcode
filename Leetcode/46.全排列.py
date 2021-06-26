#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        res = []
        def back_track(first=0):
            if first == size:
                res.append(nums[:])
            for i in range(first, size):
                nums[first], nums[i] = nums[i], nums[first]
                back_track(first+1)
                nums[first], nums[i] = nums[i], nums[first]
        back_track()
        return res
# @lc code=end


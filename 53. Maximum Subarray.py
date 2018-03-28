# !/usr/bin/env python
# coding:utf-8


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        cursum = maxsum = nums[0]
        for num in nums[1:]:
            cursum = max(num, cursum + num)
            maxsum = max(cursum, maxsum)
        return maxsum


if __name__ == '__main__':
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = Solution()
    print(s.maxSubArray(A))

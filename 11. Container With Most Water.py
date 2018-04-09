# !/usr/bin/env python
# coding: utf-8


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        # if length == 2:
        #     return min(height[0], height[1])**2

        maxarea = l = 0
        r = length-1
        while(l<r):
            maxarea = max(maxarea, min(height[l], height[r])* (r-l))
            if height[l]<=height[r-1]:
                l += 1
            else:
                r -= 1
        return maxarea

s = Solution()
print(s.maxArea([2,1]))
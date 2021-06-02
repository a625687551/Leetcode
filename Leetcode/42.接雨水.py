#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        res = []
        stack = []
        n = len(height)
        for i, v in enumerate(height):
            while stack and v > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                current_height = min(height[left], height[i]) - height[top]
                res.append((i-left-1)*current_height)
            stack.append(i)
        return sum(res)
    def trap_double_point(self, height: List[int]) -> int:
        left, right = 0, len(height) -1
        left_max, right_max = 0, 0
        result = []
        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)
            if left_max <= right_max:
                result.append(left_max - height[left])
                left += 1
            else:
                result.append(right_max - height[right])
                right -= 1
        return sum(result)
# @lc code=end


#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0]*n, [n]*n
        memo_stack = []
        for i in range(n):
            while memo_stack and heights[memo_stack[-1]] > heights[i]:
                right[memo_stack[-1]] = i
                memo_stack.pop()
            left[i] = memo_stack[-1] if memo_stack else -1
            memo_stack.append(i)
        res = max((right[i] - left[i]-1)*heights[i] for i in range(n)) if n >0 else 0
        return res
# @lc code=end


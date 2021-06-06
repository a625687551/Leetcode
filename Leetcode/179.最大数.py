#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ss = map(str, nums)
        def cmp(a, b):
            if a+b > b+a:
                return 1
            elif a+b == b+a:
                return 0
            else:
                return -1
        ss = sorted(ss, key=functools.cmp_to_key(cmp), reverse=True)
        return "".join(ss) if ss[0] != "0" else "0"
# @lc code=end


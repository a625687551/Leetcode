#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, int(1e9)
        for price in prices:
            max_profit = max(price-min_price, max_profit)
            min_price = min(price, min_price)
        return max_profit
# @lc code=end


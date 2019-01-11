# -*- coding:utf-8 -*-

"""
假设把某个股票的价格按照时间先后顺序存储在数组中，请问买卖该股票的一次最大的利润是多少。例如：一个股票在某些时间的价格是
[9,11,8,5,7,12,16,14],如果我们在价格5的时候买入在价格16的时候卖出，则能获得收获最大的利润11
思路：
最大利润就是数组中的整数对的最大差值。普通：长度N的数组中存在O(N2)的数对，复杂度为O(n2)

"""


class Solution:
    def max_stock_gain(self, nums):
        if not nums or len(nums) < 2:
            return 0
        min_price = nums[0]
        max_diff = nums[0] - min_price
        for i in range(1, len(nums)-1):
            if nums[i - 1] < min_price:
                min_price = nums[i - 1]
            cur_diff = nums[i] - min_price
            if cur_diff > max_diff:
                max_diff = cur_diff
        return max_diff


if __name__ == '__main__':
    s = Solution()
    a = [9, 11, 8, 5, 7, 12, 16, 14]
    print(s.max_stock_gain(a))

# ！/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i, num in enumerate(numbers):
            if target - num in dict:
                return [dict[target-num]+1, i+1]
            dict[num] = i

if __name__ == '__main__':
    numbers = {2, 7, 11, 15}
    target = 9
    s = Solution()
    print(s.twoSum(numbers, target))


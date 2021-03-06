# -*- coding: utf-8 -*-

"""
在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是重复的数字2或者3。
这里有两种解决情况
1、对数组修改处理
2、不对数组修改处理，但是复制一个数组
3、不修改数组也不复制
"""


class Solution:
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        if not numbers:
            return False
        for i in numbers:
            if i < 0 or i > len(numbers) - 1:
                return False
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    index = numbers[i]
                    numbers[i], numbers[index] = numbers[index], numbers[i]
        return False

    def duplicate_new(self, nums):
        if not nums:
            return []
        res = []
        for k, v in enumerate(nums):
            while k != v:
                if nums[k] == nums[v]:
                    res.append(v)
                    break
                else:
                    nums[k], nums[v] = nums[v], nums[k]
                    v = nums[k]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.duplicate([2, 3, 1, 0, 2, 5, 3], {}))

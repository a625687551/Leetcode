# -*- coding:utf-8 -*-
"""
从扑克牌中随机抽取5张牌，判断是不是一个顺子，即这5张牌是不是是连续的。2-10是数字本身，A是1，J 是11，Q是12，K是13，
而大小王可以看成是任意数字
思路：
1.先排序
2.统计数组中0的个数
3、统计相邻的差值，如果空缺总数小于或者等于0的个数，那么这个数组就是连续的
"""


class Solution:
    def IsContinuous(self, numbers):
        if not numbers or len(numbers) != 5:
            return False
        new_list = sorted(numbers)
        zero_num = 0
        num_gap = 0
        print(new_list)
        for i, x in enumerate(new_list[:4]):
            if x == 0:
                zero_num += 1
            else:
                if new_list[i + 1] == new_list[i]:
                    return False
                num_gap += new_list[i + 1] - new_list[i]
        print(zero_num, num_gap)
        if num_gap <= 4:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.IsContinuous([0, 3, 1, 6, 4]))

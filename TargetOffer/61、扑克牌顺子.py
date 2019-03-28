# -*- coding:utf-8 -*-
"""
从扑克牌中随机抽取5张牌，判断是不是一个顺子，即这5张牌是不是是连续的。2-10是数字本身，A是1，J 是11，Q是12，K是13，
而大小王可以看成是任意数字,方便起见大小王是0
思路：
1.先排序
2.统计数组中0的个数
3、统计相邻的差值，如果空缺总数小于或者等于0的个数，那么这个数组就是连续的
另外的：
1、排序
2、计算所有相邻数字间隔总数
3、计算0的个数
4、如果2、3相等，就是顺子
5、如果出现对子，则不是顺子
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

    def is_continue(self, numbers):
        if not numbers or len(numbers) != 5:
            return False
        min_num, max_num = 14, -1
        for i, v in enumerate(numbers):
            if v < 0 or v > 13:
                return False
            if v == 0:
                continue
            if i > 0 and numbers[i] == numbers[i - 1]:
                return False
            max_num = v if v > max_num else max_num
            min_num = v if v < min_num else min_num
            if max_num - min_num >= 5:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.IsContinuous([0, 3, 1, 6, 4]))
    print(s.IsContinuous([0, 8, 9, 6, 7]))
    # print(s.is_continue([0, 3, 1, 6, 4]))

# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
位图排序
// 分类 -------------- 内部比较排序
// 数据结构 ---------- 数组
// 最差时间复杂度 ---- O(n^2)
// 最优时间复杂度 ---- 如果序列在一开始已经大部分排序过的话,会接近O(n)
// 平均时间复杂度 ---- O(n^2)
// 所需辅助空间 ------ O(1)
// 稳定性 ------------ 稳定
'''
import random

class Bitmap(object):
    def __init__(self, max):
        self.size = int((max + 31 - 1) / 31)
        self.array = [0 for i in range(self.size)]

    def bitindex(self, num):
        return num % 31

    def set_one(self, num):
        element_index = (num // 31)
        byte_index = self.bitindex(num)
        ele = self.array[element_index]
        print(num, byte_index, len(self.array))
        self.array[element_index] = ele | (1 << byte_index)

    def test_one(self, i):
        element_index = i // 31
        byte_index = self.bitindex(i)
        if self.array[element_index] & (1 << byte_index):
            return True
        return False


if __name__ == '__main__':
    # max_list = ord('z')  # ord('*')返回单字符在ASCII中对应的整数
    # shuffle_array = [x for x in 'qwelajkda']
    max_list = 100000
    shuffle_array = [random.randint(1, 100000) for x in range(10)]
    ret = []
    bitmap = Bitmap(max=max_list)
    for c in shuffle_array:
        bitmap.set_one(c)
    for i in range(max_list + 1):
        if bitmap.test_one(i):
            ret.append(i)
    print(u'原始数组是:%s' % shuffle_array)
    print(u'排序以后的数组是:%s' % ret)

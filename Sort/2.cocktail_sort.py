# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
鸡尾酒排序，是冒泡排序的一种改进，从两边逼近
// 分类 -------------- 内部比较排序
// 数据结构 ---------- 数组
// 最差时间复杂度 ---- O(n^2)
// 最优时间复杂度 ---- 如果序列在一开始已经大部分排序过的话,会接近O(n)
// 平均时间复杂度 ---- O(n^2)
// 所需辅助空间 ------ O(1)
// 稳定性 ------------ 稳定
'''


def cocktail_sort(lists):
    count = len(lists)
    left = 0
    right = count - 1
    while(left < right):
        for i in range(right):
            if lists[i] > lists[i+1]:
                lists[i], lists[i+1] = lists[i+1], lists[i]
        right -= 1
        for j in range(right, left, -1):
            if lists[j-1] > lists[j]:
                lists[j-1], lists[j] = lists[j], lists[j-1]
        left += 1
    return lists


if __name__ == '__main__':
    l = [50, 10, 30, 20, 60, 40, 1]
    # l = [29, 10, 14, 37, 14]
    f = cocktail_sort(l)
    print("finally {}".format(f))

# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
选择排序是一种直接排序，工作原理:初始时在序列中找到最小（大）元素，放到序列的起始位置作为已排序序列；然后，
再从剩余未排序元素中继续寻找最小（大）元素，放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
注意选择排序与冒泡排序的区别：冒泡排序通过依次交换相邻两个顺序不合法的元素位置，从而将当前最小（大）元素放到合适的位置；
而选择排序每遍历一次都记住了当前最小（大）元素的位置，最后仅需一次交换操作即可将其放到合适的位置
// 分类 -------------- 内部比较排序
// 数据结构 ---------- 数组
// 最差时间复杂度 ---- O(n^2)
// 最优时间复杂度 ---- O(n^2)
// 平均时间复杂度 ---- O(n^2)
// 所需辅助空间 ------ O(1)
// 稳定性 ------------ 不稳定
'''


def select_sort(lists):
    # 选择排序
    count = len(lists)
    for i in range(count):
        little = i
        for j in range(i+1, count):
            if lists[j] < lists[little]:
                little = j
        if little != i:
            lists[little], lists[i] = lists[i], lists[little]
        print(lists)
    return lists

if __name__ == '__main__':
    l = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
    # l = [50, 10, 30, 20, 60, 40, 1]
    # l = [29, 10, 15, 37, 14]
    f = select_sort(l)
    print("finally {}".format(f))

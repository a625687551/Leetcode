# !/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
归并排序的实现分为递归实现与非递归(迭代)实现。
递归实现的归并排序是算法设计中分治策略的典型应用，
我们将一个大问题分割成小问题分别解决，然后用所有小问题的答案来解决整个大问题。
非递归(迭代)实现的归并排序首先进行是两两归并，然后四四归并，然后是八八归并，一直下去直到归并了整个数组。
// 分类 -------------- 内部比较排序
// 数据结构 ---------- 数组
// 最差时间复杂度 ---- O(nlogn)
// 最优时间复杂度 ---- O(nlogn)
// 平均时间复杂度 ---- O(nlogn)
// 所需辅助空间 ------ O(n)
// 稳定性 ------------ 稳定
"""


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    n = len(lists)
    num = n // 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 加入剩下的元素
    result += left[i:]
    result += right[j:]
    return result


if __name__ == '__main__':
    l = [29, 10, 15, 37, 14]
    f = merge_sort(l)
    print("finally {}".format(f))

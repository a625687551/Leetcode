# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
插入排序就是讲一个数据插入到已排好的有序数据中，从而得到一个新的有序数列，算法适用于少量数据，时间复杂度O(n^2),是稳定的
一个排序方式，这个类似于打牌插入扑克
// 分类 ------------- 内部比较排序
// 数据结构 ---------- 数组
// 最差时间复杂度 ---- 最坏情况为输入序列是降序排列的,此时时间复杂度O(n^2)
// 最优时间复杂度 ---- 最好情况为输入序列是升序排列的,此时时间复杂度O(n)
// 平均时间复杂度 ---- O(n^2)
// 所需辅助空间 ------ O(1)
// 稳定性 ------------ 稳定
'''


def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                print(lists)
                # lists[j + 1] = lists[j]
                # lists[j] = key
                lists[j + 1], lists[j] = lists[j], key
            j = j - 1
    return lists


'''
二分插入排序可以减少比较操作次数
// 分类 -------------- 内部比较排序
// 数据结构 ---------- 数组
// 最差时间复杂度 ---- O(n^2)
// 最优时间复杂度 ---- O(nlogn)
// 平均时间复杂度 ---- O(n^2)
// 所需辅助空间 ------ O(1)
// 稳定性 ------------ 稳定
'''


def binary_insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        get = lists[i]
        left = 0
        right = i - 1
        while left <= right:
            mid = (right + left) // 2
            if lists[mid] > get:
                right = mid - 1
            else:
                left = mid + 1
        while i >= left + 1:
            lists[i] = lists[i-1]
            i = i - 1
        lists[left] = get
    return lists


'''
希尔排序是插入排序的更高效的改进，将全部元素分成几个区域来排序，然后在取得越来越小的步长来排序，最后一次
是插入排序（这时候几乎已经排好）
// 分类 -------------- 内部比较排序
// 数据结构 ---------- 数组
// 最差时间复杂度 ---- 根据步长序列的不同而不同。已知最好的为O(n(logn)^2)
// 最优时间复杂度 ---- O(n)
// 平均时间复杂度 ---- 根据步长序列的不同而不同。
// 所需辅助空间 ------ O(1)
// 稳定性 ------------ 不稳定
'''


def shell_sort(lists):
    count = len(lists)
    h = 0
    while (h <= count):
        # 初始步长
        h = h * 3 + 1
    while (h >= 1):
        for i in range(h, count):
            j = i - h
            get = lists[i]
            while ((j >= 0) and (lists[j] > get)):
                lists[j + h] = lists[j]
                j = j - h
            lists[j+h] = get
        # for i in range(h, count, h):
        #     if lists[i - h] > lists[i]:
        #         lists[i - h], lists[i] = lists[i], lists[i - h]
        # 缩减步长
        h = (h - 1) // 3

    return lists


if __name__ == '__main__':
    l = [29, 10, 14, 37, 14]
    # l = [5, 2, 9, 4, 7, 6, 1, 3, 8]
    f = insert_sort(l)
    # f = binary_insert_sort(l)
    # f = shell_sort(l)
    print("finally {}".format(f))

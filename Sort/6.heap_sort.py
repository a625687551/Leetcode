# !/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
堆排序是指利用堆这种数据结构所设计的一种选择排序算法。堆是一种近似完全二叉树的结构（通常堆是通过一维数组来实现的），
并满足性质：以最大堆（也叫大根堆、大顶堆）为例，其中父结点的值总是大于它的孩子节点。
步骤：
由输入的无序数组构造一个最大堆，作为初始的无序区
把堆顶元素（最大值）和堆尾元素互换
把堆（无序区）的尺寸缩小1，并调用heapify(A, 0)从新的堆顶元素开始进行堆调整
重复步骤2，直到堆的尺寸为1
Python 可以用heapq
// 分类 -------------- 内部比较排序
// 数据结构 ---------- 数组
// 最差时间复杂度 ---- O(nlogn)
// 最优时间复杂度 ---- O(nlogn)
// 平均时间复杂度 ---- O(nlogn)
// 所需辅助空间 ------ O(1)
// 稳定性 ------------ 不稳定
"""


def heap_sort(lists, i, size):
    # 堆排序
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    mt = i
    if i > size / 2:
        if lchild < size and lists[lchild] > lists[mt]:
            mt = lchild
        if rchild < size and lists[rchild] > lists[mt]:
            mt = rchild
        if mt != i:
            lists[mt], lists[i] = lists[i], lists[mt]
            heap_sort(lists, mt, size)


def build_heap(lists, size):
    for i in range(0, (size / 2))[::-1]:
        heap_sort(lists, i, size)


def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        heap_sort(lists, 0, i)


if __name__ == '__main__':
    l = [29, 10, 15, 37, 14]
    f = heap_sort(l)
    print("finally {}".format(f))

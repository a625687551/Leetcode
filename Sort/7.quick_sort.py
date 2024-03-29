# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
快速排序是由东尼·霍尔所发展的一种排序算法。在平均状况下，排序n个元素要O(nlogn)次比较。在最坏状况下则需要O(n^2)次比较，
但这种状况并不常见。事实上，快速排序通常明显比其他O(nlogn)算法更快，因为它的内部循环可以在大部分的架构上很有效率地被实现出来。
步骤：
1. 从序列中挑出一个元素，作为"基准"(pivot).
2. 把所有比基准值小的元素放在基准前面，所有比基准值大的元素放在基准的后面（相同的数可以到任一边），这个称为分区(partition)操作。
3. 对每个分区递归地进行步骤1~2，递归的结束条件是序列的大小是0或1，这时整体已经被排好序了。

// 分类 ------------ 内部比较排序
// 数据结构 --------- 数组
// 最差时间复杂度 ---- 每次选取的基准都是最大（或最小）的元素，导致每次只划分出了一个分区，需要进行n-1次划分才能结束递归，时间复杂度为O(n^2)
// 最优时间复杂度 ---- 每次选取的基准都是中位数，这样每次都均匀的划分出两个分区，只需要logn次划分就能结束递归，时间复杂度为O(nlogn)
// 平均时间复杂度 ---- O(nlogn)
// 所需辅助空间 ------ 主要是递归造成的栈空间的使用(用来保存left和right等局部变量)，取决于递归树的深度，一般为O(logn)，最差为O(n)
// 稳定性 ---------- 不稳定
'''


def quick_sort(lists, left, right):
    if left >= right:
        return lists
    # 以左边的点作为base
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists


def quick_sort_brief(lists):
    """递归方式"""
    if len(lists) <= 1:
        return lists
    low = []
    high = []
    base = lists[0]
    for x in lists[1:]:
        if x <= base:
            low.append(x)
        else:
            high.append(x)
    return quick_sort_brief(low) + [base] + quick_sort_brief(high)


def quick_sort_no_recursion(lists):
    """非递归快排"""
    if len(lists) < 2:
        return lists
    stack = [len(lists) -1, 0]
    while stack:
        l = stack.pop()
        r = stack.pop()
        index = partition(lists, l, r)
        if l < index -1:
            stack.append(l)
            stack.append(index -1)
        if r < index + 1:
            stack.append(r)
            stack.append(index + 1)
    return lists

def partition(arr, start, end):
    pivot = arr[start]
    while start < end:
        while start < end and arr[end] >= pivot:
            end -=1
        # arr[start] = arr[end]
        while start < end and arr[start] <= pivot:
            start += 1
        arr[end] = arr[start]
    arr[start] = pivot
    return start


if __name__ == '__main__':
    l = [29, 10, 14, 37, 14]
    f = quick_sort(l, left=0, right=len(l) - 1)
    print("finally {}".format(f))
    # print(quick_sort_brief(l))
    print(quick_sort_no_recursion(l))

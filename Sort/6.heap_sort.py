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

大顶堆：arr[i] >= arr[2i+1] && arr[i] >= arr[2i+2]  
小顶堆：arr[i] <= arr[2i+1] && arr[i] <= arr[2i+2]  
"""


class MinHeap(object):
    def __init__(self, nums):
        self.heap = []
        self.size = 0
        self.build_heap(nums)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def build_heap(self, nums):
        for x in nums:
            self.push(x)

    def push(self, x):
        self.heap.append(x)
        self.size += 1
        index = self.size -1
        while index:
            parent_index = index // 2
            if self.heap[parent_index] > self.heap[index]:
                self.swap(parent_index, index)
            index = parent_index

    def pop(self):
        top = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.size -= 1

        index = 0
        while index < self.size:
            left = index*2 + 1
            right = index*2 + 2
            small_index = index

            if left < self.size and self.heap[left] < self.heap[small_index]:
                small_index = left
            if right < self.size and self.heap[right] < self.heap[small_index]:
                small_index = right
            
            if small_index == index:
                break
            self.swap(small_index, index)
        return top


    def top(self):
        return self.heap[0]

def heap_sort(nums):
    h = MinHeap(nums)
    res = []
    while h.size > 0:
        res.append(h.pop())
    return res


if __name__ == '__main__':
    l = [29, 10, 15, 37, 14]
    f = heap_sort(l)
    print("finally {}".format(f))

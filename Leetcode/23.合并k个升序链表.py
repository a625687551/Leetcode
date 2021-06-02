#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#
"""
这里面最重要的是实现最小堆
"""
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class MinHeap(object):
    def __init__(self):
        self.heap = []
        self.size = 0

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def top(self):
        return self.heap[0]

    def push(self, val):
        self.heap.append(val)
        self.size += 1

        index = self.size - 1
        while index >0:
            parent = (index-1)//2
            if self.heap[parent].val > self.heap[index].val:
                self.swap(parent, index)
            index = parent

    def pop(self):
        top = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.size -= 1

        index = 0
        while index < self.size:
            left = 2*index + 1
            right = 2*index + 2
            small_index = index

            if left < self.size and self.heap[left].val < self.heap[small_index].val:
                small_index = left
            if right < self.size and self.heap[right].val < self.heap[small_index].val:
                small_index = right
            
            if small_index == index:
                break
            self.swap(small_index, index)
            index = small_index
        return top


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # head = ListNode()
        min_heap = MinHeap()
        for node in lists:
            if node:
                min_heap.push(node)
        head, p = None, None
        
        while min_heap.size > 0:
            node = min_heap.pop()
            if head is None:
                head = node
                p = head
            else:
                p.next = node
                p = p.next
            if node.next:
                min_heap.push(node.next)
        return head

# @lc code=end


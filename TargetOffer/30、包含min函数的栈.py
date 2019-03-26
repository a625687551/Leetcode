# -*- coding:utf-8 -*-

"""
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
"""


class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        self.stack.append(node)
        if not self.min_stack or self.min_stack[-1] > node:
            self.min_stack.append(node)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if not self.stack:
            return None
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_stack[-1]


s = Solution()
s.push(3)
print(s.min())
print(s.stack, s.min_stack)
s.push(4)
print(s.min())
print(s.stack, s.min_stack)
s.push(2)
print(s.min())
print(s.stack, s.min_stack)
s.push(3)
print(s.min())
s.pop()
print(s.min())
# -*- coding: utf-8 -*-
# @Time    : 2021/2/6 7:19 上午
# @Author  : wangjianfeng
# @File    : 155.min stack.py


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        self.stack = []

    def push(self, x: int) -> None:
        """
        这里0 的判断问题
        :param x:
        :return:
        """
        self.stack.append(x)
        if not self.min_stack or self.min_stack[-1] >= x:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        if not self.stack:
            return False
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min_stack:
            return False
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

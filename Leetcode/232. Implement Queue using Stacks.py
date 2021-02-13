# -*- coding: utf-8 -*-
# @Time    : 2021/2/6 8:36 上午
# @Author  : wangjianfeng
# @File    : 232. Implement Queue using Stacks.py


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.helper = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if x is None:
            return
        while self.stack:
            self.helper.append(self.stack.pop())
        self.stack.append(x)
        while self.helper:
            self.stack.append(self.helper.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack:
            return self.stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack:
            return self.stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
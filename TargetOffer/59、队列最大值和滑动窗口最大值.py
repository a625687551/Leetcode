# -*- coding:utf-8 -*-

"""
一、滑动窗口的最大值
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， 
{2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
二、队列的最大值
定义一个队列并实现函数max得到队列里的最大值，要求函数max、push_back.pop_front的时间复杂度都是O（1）
"""


class Solution:
    def maxInWindows(self, num, size):
        """滑动窗口的最大值"""
        res = []
        if not num or size <= 0 or len(num) < size:
            return res
        index = []  # 存储位置
        for i in range(size):
            if len(index) > 0 and num[i] >= num[index[-1]]:
                index.pop()
            index.append(i)
        res.append(num[index[0]])
        for i in range(size, len(num)):
            while len(index) > 0 and num[i] >= num[index[-1]]:
                index.pop()
            if len(index) > 0 and index[0] <= (i - size):
                index.pop(0)
            index.append(i)
            res.append(num[index[0]])
        return res

    def max_in_queue(self, num):
        """队列的最大值"""
        pass


if __name__ == '__main__':
    s = Solution()
    print(s.maxInWindows([2, 3, 4, 2, 6, 2, 5, 1], 3))

# -*- coding:utf-8 -*-
"""
每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。
其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。
每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,
从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,
并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？
(注：小朋友的编号是从0到n-1)
思路：
这个是数学中的约瑟夫环问题
1、构造一个环形链表, 时间复杂度mn 空间复杂度n
2、分析每次被删除的数字规律直接计算出来
"""


class Solution:
    def LastRemaining_Solution_1(self, n, m):
        if not n or not m or m < 1 or n < 1:
            return -1
        else:
            i = 0
            nums = [x for x in range(n)]
            # print(nums)
            while len(nums) > 1:
                i = (m + i - 1) % len(nums)
                # print(nums[i])
                nums.pop(i)
            return nums[0]

    def LastRemaining_Solution(self, n, m):
        if not n or not m or m < 1 or n < 1:
            return -1
        else:
            last = 0
            res_lst = [0]
            for i in range(1, n + 1):
                last = (last + m) % i
                res_lst.append(last)
            print(res_lst)
            return last


if __name__ == '__main__':
    s = Solution()
    # print(s.LastRemaining_Solution(5, 3))
    print(s.LastRemaining_Solution_1(10, 5))
    print(s.LastRemaining_Solution_1(77, 2))
    # print(s.LastRemaining_Solution(10, 5))
    # print(s.LastRemaining_Solution_1(5, 3))

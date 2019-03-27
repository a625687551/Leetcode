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
Step1.
首先定义一个关于 m 和 n 的函数：f(n, m)，表示在n个数字 0,1,2…,n-1 中每次删除第m个数字，最后剩下的那个数字。
注意：f(n, m)表示的是，在经过了多次删除后，最后剩下的那个数字，也就是说f(n,m)本质上是个数。
Step2.
n个数中，第一个被删除的数是(m - 1) % n，把它记为k，此时数组中还剩下0,1,2… k-1, k+1,…n-1 这几个数字。接下来从k+1开始计数，相当于在剩下的序列中，k+1排在最前面，从而形成k+1,… n-1,… 0,1,2…k-1。本题中，第一个被删除的是数字2，因此数组还剩下 0,1,3,4,5，相当于3,4,5,0,1。由于这个序列是不连续的，在2那个地方断开了，所以不能写为f(n-1, m)。在此记为g(n-1, m)。
最初序列最后剩下的数字，一定是删除一个数字后剩下的数字，因此f(n, m) = g(n-1, m)
Step3.
将[3,4,5,0,1]重新映射为[0,1,2,3,4]，映射的公式是：p(x) = (x - k - 1) % n。其中k = 2，n = 6。
  3 —-> 0
  4 —-> 1
  5 —-> 2
  0 —-> 3
  1 —-> 4
映射以后的序列是0,1,2,3,4，是一个连续的序列，因此可以用f(n-1, m)来表示。
此时的f(n-1, m)是不等于g(n-1, m)，因为二者对应的序列不同，存在一个映射关系。
该映射的逆映射是 p’(x) = (x + k + 1) % n
因此g(n-1, m) = p’[f(n-1, m)] = [f(n-1, m) + k + 1] % n
即：f(n, m) = [f(n-1, m) + k + 1] % n
带入k = (m - 1) % n, 得到f(n, m) = [f(n-1, m) +m] % n (n > 1)
Step4.
当n = 1时，只有一个人，此时剩余的数字为0
综上，约瑟夫环的公式是：
f(n, m) = 0           (n = 1)
f(n, m) = [f(n-1, m) +m] % n  (n > 1)
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

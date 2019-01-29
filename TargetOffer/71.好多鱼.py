# !/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
链接：https://www.nowcoder.com/questionTerminal/e3dd485dd23a42899228305658457927
来源：牛客网
牛牛有一个鱼缸。鱼缸里面已经有n条鱼，每条鱼的大小为fishSize[i] (1 ≤ i ≤ n,均为正整数)，
牛牛现在想把新捕捉的鱼放入鱼缸。鱼缸内存在着大鱼吃小鱼的定律。经过观察，牛牛发现一条鱼A的大小为另外一条鱼B大小的2倍到10倍
包括2倍大小和10倍大小)，鱼A会吃掉鱼B。考虑到这个，牛牛要放入的鱼就需要保证：
1、放进去的鱼是安全的，不会被其他鱼吃掉
2、这条鱼放进去也不能吃掉其他鱼
鱼缸里面已经存在的鱼已经相处了很久，不考虑他们互相捕食。放入的新鱼之间也不会相互捕食。
现在知道新放入鱼的大小范围[minSize,maxSize](考虑鱼的大小都是整数表示),牛牛想知道有多少种大小的鱼可以放入这个鱼缸。

输入描述:
输入数据包括3行.
第一行为新放入鱼的尺寸范围minSize,maxSize(1 ≤ minSize,maxSize ≤ 1000)，以空格分隔。
第二行为鱼缸里面已经有鱼的数量n(1 ≤ n ≤ 50)
第三行为已经有的鱼的大小fishSize[i](1 ≤ fishSize[i] ≤ 1000)，以空格分隔。

输出描述:
    输出有多少种大小的鱼可以放入这个鱼缸。考虑鱼的大小都是整数表示
思路：
根据已经在的鱼大小，找出需要排除的范围，然后在根据投入的范围，去掉之前排除的范围，剩下的就都是可以放入的大小种类了。
"""


class Solution(object):
    def solution(self, min_size, max_size, had_num, fish_sizes):
        res = []
        fish_sizes = [int(x) for x in fish_sizes.split()]
        for i in range(min_size, max_size + 1):
            for j in fish_sizes:
                if 2 <= i / j <= 10:
                    continue
                else:
                    res.append(i)
        print(res)
        return len(res)


if __name__ == '__main__':
    s = Solution()
    print(s.solution(1, 36, 1, "3"))
    print(s.solution(1, 12, 1, "1"))

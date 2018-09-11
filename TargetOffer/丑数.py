# -*- coding:utf-8 -*-
"""
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数
"""


class Solution:
    def GetUglyNumber_Solution(self, index):
        # 找到存起来，然后逐渐搞
        if index <= 0:
            return 0
        ugly_list = [1]
        t2, t3, t5 = 0, 0, 0
        for i in range(index-1):
            ugly_new = min(ugly_list[t2]*2, ugly_list[t3]*3, ugly_list[t5]*5)
            ugly_list.append(ugly_new)
            if ugly_new % 2 == 0:
                t2 += 1
            if ugly_new % 3 == 0:
                t3 += 1
            if ugly_new % 5 == 0:
                t5 += 1
        return ugly_list[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.GetUglyNumber_Solution(10))

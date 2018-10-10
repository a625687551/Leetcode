# -*- coding:utf-8 -*-
"""
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
"""


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        if n < 1:
            return 0
        count = 0
        i = 1
        while (n // i != 0):
            current = (n // i) % 10
            before = n // (i * 10)
            after = n - (n // i) * i
            if current == 0:
                count += before*i
            elif current == 1:
                count += before*i + after + 1
            else:
                count += (before + 1)*i
            i = i*10
        return count

if __name__ == '__main__':
    s = Solution()
    print(s.NumberOf1Between1AndN_Solution(12))

# -*- coding:utf-8 -*-

"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007

"""


class Solution:
    def InversePairs(self, data):
        return self.inverse_count(data[:], 0, len(data) - 1, data[:]) % 1000000007

    def inverse_count(self, tmp, start, end, data):
        if end - start < 1:
            return 0
        if end - start == 1:
            if data[start] <= data[end]:
                return 0
            else:
                tmp[start], tmp[end] = data[end], data[start]
                return 1
        mid = (start + end) // 2
        cnt = self.inverse_count(data, start, mid, tmp) + self.inverse_count(data, mid + 1, end, tmp)
        i = start
        j = mid + 1
        ind = start
        while i <= mid and j <= end:
            if data[i] <= data[j]:
                tmp[ind] = data[i]
                i += 1
            else:
                tmp[ind] = data[j]
                cnt += mid - i + 1
                j += 1
            ind += 1
        while i <= mid:
            tmp[ind] = data[i]
            i += 1
            ind += 1
        while j <= end:
            tmp[ind] = data[j]
            j += 1
            ind += 1
        return cnt


if __name__ == '__main__':
    l = [364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993, 407, 416, 366, 315, 301, 601, 650, 418, 355, 460, 505,
         360, 965, 516, 648, 727, 667, 465, 849, 455, 181, 486, 149, 588, 233, 144, 174, 557, 67, 746, 550, 474, 162,
         268, 142, 463, 221, 882, 576, 604, 739, 288, 569, 256, 936, 275, 401, 497, 82, 935, 983, 583, 523, 697, 478,
         147, 795, 380, 973, 958, 115, 773, 870, 259, 655, 446, 863, 735, 784, 3, 671, 433, 630, 425, 930, 64, 266, 235,
         187, 284, 665, 874, 80, 45, 848, 38, 811, 267, 575]
    s = Solution()
    print(s.InversePairs(l))

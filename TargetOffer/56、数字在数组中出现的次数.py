# -*- coding:utf-8 -*-

"""
1、数组中只出现一次的两个数字
2、数组中唯一只出现一次的数字。
一个数组中除一个数字出现了一次之外，别的数字都出现了3次，找出出现一次的数字
（全部的二进制相加对3取余，如果是0，则哪一位是0，否则是1）

"""


class Solution:
    def get_appear_once_two(self, data):
        if not data:
            return 0
        inter = 0
        for x in data:
            inter = inter ^ x
        return inter

    def get_appear_once_one(self, data):
        if not data:
            return 0
        res = [0] * 8
        for x in data:
            for k, v in enumerate([int(i) for i in "{:08b}".format(x)]):
                res[k] = res[k] + v
        print(res)
        out = "".join([str(x) for x in map(lambda x: x % 3, res)])
        return int(out, 2)


if __name__ == '__main__':
    s = Solution()
    print(s.get_appear_once_one([1, 1, 1, 2, 2, 2, 6]))
    # print(s.get_appear_once_two([1, 1, 2, 2, 3, 6]))

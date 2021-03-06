# -*- coding:utf-8 -*-
"""
数字序列“012345678910111213141516171819....”的格式序列化一个字符序列中。在这个序列中,第5位（从0开始计数）是5，
第13位是1，第19位是4，等等，请写一个函数，求任意第N为对应的数字
"""


class Solution:
    def num_in_nums(self, n):
        if n < 0:
            return -1
        digits = 1
        while True:
            middle = self.count_int(digits)
            if n < middle * digits:
                return self.digit_at_index(n, digits)
            n -= digits * middle
            digits += 1
        return digits

    def count_int(self, num):
        if num == 1:
            return 10
        return 9 * pow(10, num - 1)

    def digit_at_index(self, index, digits):
        num = self.begin_number(digits) + index // digits
        for x in range(1, digits - index % digits):
            num /= 10
        return num % 10

    def begin_number(self, digits):
        """m位数字的开始数字"""
        if digits == 1:
            return 0
        return pow(10, digits - 1)

    def other_solution(self, n):
        """这里需要归纳统计出来的，类似于一个递归"""
        if not n or n <= 9:
            return n
        first, start_len = 0, 1
        data = n - 1
        for i in range(len(str(data))):
            temp = data - start_len * 9 * 10 ** i
            if temp > 0:
                data = temp
                start_len += 1
            else:
                first = 10 ** i
                break
        k, s = data // start_len, data % start_len
        return str(first + k)[s]

    def solution_new(self, n):
        if not n or n <= 0:
            return 0
        if n <= 10:
            return n - 1
        digit, m = 0, n - 1
        while m > 0:
            m = m - 9 * 10 ** digit
            digit += 1
        index = m + 9 * 10 ** (digit - 1)
        return str(10 ** (digit - 1) + index // digit)[index % digit]


if __name__ == '__main__':
    a = "5526371163256555"
    s = Solution()
    print(s.num_in_nums(10))
    print(s.num_in_nums(30))
    print(s.num_in_nums(500))
    print(s.num_in_nums(1001))
    # print("other solution")
    print(s.other_solution(10))
    print(s.other_solution(30))
    print(s.other_solution(500))
    print(s.other_solution(1001))
    # new
    print(s.solution_new(10))
    print(s.solution_new(30))
    print(s.solution_new(500))
    print(s.solution_new(1001))

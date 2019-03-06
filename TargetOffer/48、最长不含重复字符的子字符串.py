# -*- coding:utf-8 -*-
"""
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。假设字符串中只包含a-z的字符。假如：
字符串“arabcacfr”中，最长的不含重复字符串的子字符串是“acfr"，长度为4
"""


class Solution:
    def max_no_repetition(self, target):
        if not target:
            return 0
        position = {}
        cur_length = 0
        max_length = 0
        length = len(target)
        for i in range(length):
            pre_index = position.get(target[i], -1)
            if pre_index < 0 or i - pre_index > cur_length:
                cur_length += 1
            else:
                if cur_length > max_length:
                    max_length = cur_length
                cur_length = i - pre_index
            position[target[i]] = i
            if cur_length > max_length:
                max_length = cur_length
        return max_length, position


if __name__ == '__main__':
    s = Solution()
    print(s.max_no_repetition("arabcacfr"))

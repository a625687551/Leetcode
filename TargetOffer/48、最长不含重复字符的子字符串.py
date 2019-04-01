# -*- coding:utf-8 -*-
"""
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。假设字符串中只包含a-z的字符。假如：
字符串“arabcacfr”中，最长的不含重复字符串的子字符串是“acfr"，长度为4
"""


class Solution:
    def max_no_repetition(self, data):
        if not data:
            return None
        position = {}
        cur_length, max_length = 0, 0
        for i, v in enumerate(data):
            pre_index = position.get(v, -1)
            if pre_index < 0 or i - pre_index > cur_length:
                cur_length += 1
            else:
                if cur_length > max_length:
                    max_length = cur_length
                cur_length = i - pre_index
            position[v] = i
            if cur_length > max_length:
                max_length = cur_length
        return max_length

    def solution_2(self, data):
        if not data:
            return ""
        pos = {}
        left, res = -1, 0
        for k, v in enumerate(data):
            if pos.get(v, -1) > left:
                left = pos.get(v, -1)
            pos[v] = k
            res = max(res, k - left)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.max_no_repetition("arabcacfr"))
    print(s.max_no_repetition("arabcaasdasfgjhcfr"))
    print(s.solution_2("arabcacfr"))
    print(s.solution_2("arabcaasdasfgjhcfr"))

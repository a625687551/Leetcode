# -*- coding: utf-8 -*-
# @Time    : 2021/2/13 8:07 下午
# @Author  : wangjianfeng
# @File    : 71. Simplify Path.py
"""
难度：中等
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        dir = path.split("/")
        result = []
        for x in dir:
            if x == "." or x == "":
                continue
            elif x == "..":
                if len(result) > 0:
                    result.pop()
            else:
                result.append(x)
        return "/" + "/".join(result)


if __name__ == '__main__':
    path = "/home/"
    s = Solution()
    print(s.simplifyPath(path))

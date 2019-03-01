# -*- coding:utf-8 -*-
"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
"""


class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
        res = []
        self.perm(ss, res, "")
        uniq = list(set(res))
        return sorted(uniq)

    def perm(self, ss, res, path):
        if ss == "":
            res.append(path)
        else:
            for i in range(len(ss)):
                self.perm(ss[:i] + ss[i + 1:], res, path + ss[i])


class Solution1:
    """利用青蛙跳台阶的效应一样"""

    def permutation(self, ss):
        if not ss:
            return
        self.perm(ss, ss)

    def perm(self, ss, begin):
        if not begin:
            print(ss)
        else:
            for i in ss:
                temp = i
                i = begin
                begin = temp
                self.perm(ss, )


if __name__ == '__main__':
    # s = Solution()
    # print(s.Permutation("abc"))
    s = Solution1()
    print(s.permutation("abc"))

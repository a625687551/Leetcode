# coding: utf-8


class Solution():
    def solution_over(self, base, expontent):
        if not base:
            return 0.0
        if not expontent:
            return 1
        res = 1.0
        expon = abs(expontent)
        for x in range(expon):
            res *= base
        if expontent < 0:
            return 1 / res
        return res


if __name__ == '__main__':
    l = [2, 3, 1, 0, 2, 5, 3]

    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    s = Solution()
    print(s.solution_over(2, -5))

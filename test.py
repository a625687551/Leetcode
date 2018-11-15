# coding: utf-8


class Solution():
    def solution_over(self, s):
        if not s and not isinstance(s, str):
            return s
        ws = 0
        for item in s:
            if item == " ":
                ws += 1
            else:
                continue
        new_len = len(s) + ws
        new_str = []


if __name__ == '__main__':
    l = [2, 3, 1, 0, 2, 5, 3]

    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    s = Solution()
    print(s.solution_over(array, 10))

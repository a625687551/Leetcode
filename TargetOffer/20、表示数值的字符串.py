# -*- coding:utf-8 -*-
"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""


class Solution:
    def isNumeric(self, s):
        if not s:
            return False
        # 标记符号 小数点 E是否出现过
        sign, decimal, has_e = False, False, False
        for i, x in enumerate(s):
            if x == "e" or x == "E":
                # e后面一定要接数字
                if i == len(s) - 1:
                    return False
                # 不能同时存在两个e
                if has_e:
                    return False
                has_e = True
            elif x == "+" or x == "-":
                # 第二次出现+-符号，则必须紧接在e之后
                if sign and s[i - 1] != "e" and s[i - 1] != "E":
                    return False
                # 第一次出现+-符号，且不是在字符串开头，则也必须紧接在e之后
                if not sign and i > 0 and s[i - 1] != "e" and s[i - 1] != "E":
                    return False
                sign = True
            elif x == ".":
                # e后面不能接小数点，小数点不能出现两次
                if has_e or decimal:
                    return False
                decimal = True
            # 不合法字符
            elif x < "0" or x > "9":
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isNumeric("+100"))
    print(s.isNumeric("-1E-16"))
    print(s.isNumeric("1.79769313486232E+308"))
    print(s.isNumeric("123.45e+6"))

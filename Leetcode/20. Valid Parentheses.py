# !/usr/bin/python
# coding:  utf-8

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        str_dict = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in str_dict.values():
                stack.append(char)
            elif char in str_dict.keys():
                if stack == [] or str_dict[char] != stack.pop():
                    return False
            else:
                return False

        return stack == []

    def isValid_v2(self, s:str)->bool:
        if not s:
            return False
        str_dict = {'(':')','{':'}','[':']', '?':'?'}
        stack = ["?"]
        for c in s:
            if c in str_dict:
                stack.append(c)
            elif str_dict[stack.pop()] != c:
                return False
        return len(stack) == 1







if __name__ == '__main__':
    s = "()"
    sol = Solution()
    # print(sol.isValid(s))
    print(sol.isValid_v2(s))

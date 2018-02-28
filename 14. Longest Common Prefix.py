# !/usr/bin/python
# coding:  utf-8


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
        	return ""
        # l = 0
        # for cg in zip(*strs):
        # 	if len(set(cg)) > 1:
        # 		return strs[0][:1]
        # 		l += 1
        # return strs[0][:l]
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)



if __name__ == '__main__':
	s = [""]
	sol = Solution()
	print(sol.longestCommonPrefix(s))
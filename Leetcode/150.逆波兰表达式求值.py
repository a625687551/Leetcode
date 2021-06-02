#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#
from operator import add, floordiv, mul, sub

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_func = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": lambda x,y: int(x/y)
        }
        stack = []
        for token in tokens:

            try:
                num = int(token)
            except ValueError:
                num2 = stack.pop()
                num1 = stack.pop()
                num = op_func[token](num1, num2)
            finally:
                stack.append(num)
        return stack[-1]
# @lc code=end


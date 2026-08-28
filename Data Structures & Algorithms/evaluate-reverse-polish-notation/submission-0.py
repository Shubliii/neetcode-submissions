class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        HM = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)   # truncate toward zero
        }

        stack = []

        for char in tokens:
            if char not in HM:
                stack.append(int(char))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(HM[char](a, b))

        return stack[-1]




        
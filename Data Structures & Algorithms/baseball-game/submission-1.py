class Solution:
    def calPoints(self, operations: List[str]) -> int:

        HM = {
            "+": lambda st: st[-1] + st[-2],
            "D": lambda st: st[-1] * 2
        }

        stack = []

        for op in operations:
            if op == "C":
                stack.pop()

            elif op in HM:
                stack.append(HM[op](stack))

            else:
                stack.append(int(op))

        return sum(stack)         

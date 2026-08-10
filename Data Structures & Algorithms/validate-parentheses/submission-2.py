class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        CtoO = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if c in CtoO:
                if stack and stack[-1] == CtoO[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
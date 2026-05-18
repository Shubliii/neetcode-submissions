class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        closeTOopen = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for c in s:

            if c in closeTOopen:

                if stack and stack[-1] == closeTOopen[c]:
                    stack.pop()

                else:
                    return False

            else:
                stack.append(c)

        if not stack:
            return True
        else:
            return False


        
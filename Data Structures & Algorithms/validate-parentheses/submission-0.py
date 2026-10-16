class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in pairs:  # closing bracket
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else:           # opening bracket
                stack.append(c)

        return not stack
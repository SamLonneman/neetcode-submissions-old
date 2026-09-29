class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []
        for c in s:
            if c in brackets.values():
                stack.append(c)
            elif c in brackets:
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

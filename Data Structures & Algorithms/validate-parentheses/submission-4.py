class Solution:
    def isValid(self, s: str) -> bool:
        # Associate end brackets with their corresponding start brackets
        brackets = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        # Initialize empty stack
        stack = []
        # For each character in the string
        for c in s:
            # If the character is a start bracket, push to stack
            if c in brackets.values():
                stack.append(c)
            # Else, if the character is an end bracket
            elif c in brackets:
                # If top of stack is corresponding start bracket, pop from stack
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                # Otherwise, this end bracket doesn't have a start, so invalid
                else:
                    return False
        # Finally, return whether the stack is empty because if it still has elements, then there are unclosed brackets
        return len(stack) == 0

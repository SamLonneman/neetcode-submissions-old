class Solution:

    # BACKTRACKING

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        Solution.addAllLeavesToRes(0, 0, n, [], res)
        return res
    
    def addAllLeavesToRes(o, c, n, stack, res):
        if o == c == n:
            res.append(''.join(stack))
        if o < n:
            stack.append('(')
            Solution.addAllLeavesToRes(o + 1, c, n, stack, res)
            stack.pop()
        if c < o:
            stack.append(')')
            Solution.addAllLeavesToRes(o, c + 1, n, stack, res)
            stack.pop()
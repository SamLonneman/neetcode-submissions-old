class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        return Solution.endings(0, 0, n)
    
    def endings(o, c, n):
        if o == c == n:
            return ['']
        res = []
        if o < n:
            res += ['(' + ending for ending in Solution.endings(o + 1, c, n)]
        if c < o:
            res += [')' + ending for ending in Solution.endings(o, c + 1, n)]
        return res

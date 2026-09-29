class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCounts = [0] * 26
        tCounts = [0] * 26
        for i in range(len(s)):
            sCounts[ord(s[i]) - ord('a')] += 1
            tCounts[ord(t[i]) - ord('a')] += 1
        return sCounts == tCounts
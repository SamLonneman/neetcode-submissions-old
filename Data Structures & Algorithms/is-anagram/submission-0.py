class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounts = defaultdict(int)
        tCounts = defaultdict(int)
        for c in s:
            sCounts[c] += 1
        for c in t:
            tCounts[c] += 1
        if len(sCounts) != len(tCounts):
            return False
        for c in s:
            if tCounts[c] != sCounts[c]:
                return False
        for c in t:
            if tCounts[c] != sCounts[c]:
                return False
        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanStr = ''
        for c in s.lower():
            if c.isalnum():
                cleanStr += c
        for i in range(len(cleanStr) // 2):
            if cleanStr[i] != cleanStr[-1 - i]:
                return False
        return True
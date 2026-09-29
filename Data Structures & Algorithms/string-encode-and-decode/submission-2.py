class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ''
        for s in strs:
            encoding += str(len(s)) + '#' + s
        return encoding

    def decode(self, s: str) -> List[str]:
        decoding = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoding.append(s[i:j])
            i = j
        return decoding

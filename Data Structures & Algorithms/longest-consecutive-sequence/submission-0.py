class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {}
        best = 0
        for num in nums:
            if num not in m:
                m[num] = num
                if num - 1 in m:
                    cache = m[num]
                    m[m[num]] = m[num - 1]
                    m[m[num - 1]] = cache
                if num + 1 in m:
                    cache = m[num]
                    m[m[num]] = m[num + 1]
                    m[m[num + 1]] = cache
                if abs(m[num] - m[m[num]]) + 1 > best:
                    best = abs(m[num] - m[m[num]]) + 1
        return best
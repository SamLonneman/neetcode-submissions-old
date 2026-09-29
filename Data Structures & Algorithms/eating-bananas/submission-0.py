class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Perform binary search on all possible k values (1 through max(piles))
        l = 1
        r = max(piles)
        # Store the current best time
        res = r
        while l <= r:
            k = l + (r - l) // 2
            # If you can eat all the bananas at this rate, store it as the best rate
            if sum([(n + k - 1) // k for n in piles]) <= h:
                res = k
                r = k - 1
            # Otherwise, try faster rates
            else:
                l = k + 1
        return res

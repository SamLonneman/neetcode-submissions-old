class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Get the frequency of each element in O(n) time
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num] += 1
        # Add elements into buckets indexed by frequency in O(n) time
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in frequencies:
            buckets[frequencies[num]].append(num)
        # Get top n elements in O(n) time
        result = list()
        for bucket in reversed(buckets):
            for num in bucket:
                result.append(num)
                if len(result) == k:
                    return result

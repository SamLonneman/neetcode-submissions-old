class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Get the frequency of each element in O(n) time
        numToFrequency = defaultdict(int)
        for num in nums:
            numToFrequency[num] += 1
        # Add elements into buckets indexed by frequency in O(n) time
        frequencyToNumList = [[] for _ in range(len(nums) + 1)]
        for num, frequency in numToFrequency.items():
            frequencyToNumList[frequency].append(num)
        # Get top n elements in O(n) time
        result = []
        for numList in reversed(frequencyToNumList):
            for num in numList:
                result.append(num)
                if len(result) == k:
                    return result

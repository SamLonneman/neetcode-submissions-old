class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix array holds products of left elements
        prefixes = [1] * len(nums)
        prefix = 1
        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            prefixes[i] = prefix
        # Postfix array holds products of right elements
        postfixes = [1] * len(nums)
        postfix = 1
        for i in reversed(range(len(nums) - 1)):
            postfix *= nums[i + 1]
            postfixes[i] = postfix
        # Get final result by multiplying left and right elements
        for i in range(len(nums)):
            nums[i] = prefixes[i] * postfixes[i]
        return nums

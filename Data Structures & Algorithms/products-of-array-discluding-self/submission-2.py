class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1] * len(nums)
        postfixes = [1] * len(nums)
        prefix = 1
        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            prefixes[i] = prefix
        postfix = 1
        for i in reversed(range(len(nums) - 1)):
            postfix *= nums[i + 1]
            postfixes[i] = postfix
        for i in range(len(nums)):
            nums[i] = prefixes[i] * postfixes[i]
        return nums

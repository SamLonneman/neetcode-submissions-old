class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                product *= num
        if zeros > 1:
            for i in range(len(nums)):
                nums[i] = 0
        elif zeros == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = product
                else:
                    nums[i] = 0
        else:
            for i in range(len(nums)):
                nums[i] = product // nums[i]
        return nums

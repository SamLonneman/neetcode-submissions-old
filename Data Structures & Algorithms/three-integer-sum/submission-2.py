class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            # Set up three pointers
            a = i
            b = i + 1
            c = len(nums) - 1
            # Avoid duplicates by skipping the same a
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Do 2 sum to find b and c such that nums[b] + nums[c] = -nums[a]
            while b < c:
                s = nums[b] + nums[c]
                target = -nums[a]
                if s < target:
                    b += 1
                elif s > target:
                    c -= 1
                else:
                    result.append([nums[a], nums[b], nums[c]])
                    # We have found a result, but there could be more with the same a
                    # Find the next unique b and next unique c
                    b += 1
                    while nums[b] == nums[b - 1] and b < c:
                        b += 1
                    while c + 1 == len(nums) or nums[c] == nums[c + 1] and b < c:
                        c -= 1
        return result
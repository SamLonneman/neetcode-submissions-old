class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxHeight = 0
        for i in range(len(height)):
            maxLeft[i] = maxHeight
            if height[i] > maxHeight:
                maxHeight = height[i]
        maxRight = [0] * len(height)
        maxHeight = 0
        for i in reversed(range(len(height))):
            maxRight[i] = maxHeight
            if height[i] > maxHeight:
                maxHeight = height[i]
        totalArea = 0
        for i in range(len(height)):
            totalArea += max(0, min(maxLeft[i], maxRight[i]) - height[i])
        return totalArea

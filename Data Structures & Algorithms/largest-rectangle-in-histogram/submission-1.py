class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # height:index pairs
        best = 0
        # Iterate through each height, building a non-decreasing stack
        for i in range(len(heights)):
            # While height is less than top of stack, pop elements, calculating their areas
            start = i
            while stack and heights[i] < stack[-1][0]:
                # Pop stack and calculate area stretching rightwards
                height, index = stack.pop()
                best = max(best, height * (i - index))
                start = index
            # When adding height to stack, be sure to have its index start from the last popped
            stack.append((heights[i], start))
        # In case there are elements left over, consider remaining rectangles
        while stack:
            height, index = stack.pop()
            best = max(best, height * (len(heights) - index))
        # Return the best
        return best

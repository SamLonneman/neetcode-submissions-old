class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # height:index pairs
        best = 0
        for i in range(len(heights)):
            # While less than the top of the stack
            start = i
            while stack and heights[i] < stack[-1][0]:
                # Consider each rectangle formed
                height, index = stack.pop()
                best = max(best, height * (i - index))
                start = index
            stack.append((heights[i], start))
        # In case there are elements left over, consider remaining rectangles
        while stack:
            height, index = stack.pop()
            best = max(best, height * (len(heights) - index))
        # Return the best
        return best

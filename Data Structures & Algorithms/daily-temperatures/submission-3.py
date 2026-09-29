class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Prepare final result array
        res = [0] * len(temperatures)
        # Build a non-increasing stack of temp:index pairs
        stack = []
        # For each temperature,
        for i in range(len(temperatures)):
            # If hotter than top of stack, pop from stack until cooler
            while stack and temperatures[i] > stack[-1][0]:
                index = stack.pop()[1]
                res[index] = i - index
            # Once cooler than top of stack, push to stack
            stack.append((temperatures[i], i))
        # Return result
        return res

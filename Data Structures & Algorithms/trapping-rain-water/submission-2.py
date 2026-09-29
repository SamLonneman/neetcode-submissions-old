class Solution:
    def trap(self, height: List[int]) -> int:
        # Two pointer method:
        # Start a pointer on either side
        # At any position, the water level is the minimum of the highest point to the left and the highest point to the right
        # At the left pointer, we only know the highest point to the left
        # At the right pointer, we only know the highest point to the right
        # So, to get an accurate water level every time, we can just calculate it at the side with the lower maximum since this is guaranteed to be the minimum.

        # Implementation: declare variables
        l = 0
        r = len(height) - 1
        l_max = height[l]
        r_max = height[r]
        total_water = 0
        # Until every spot has been checked,
        while l < r:
            # If the left max is smaller,
            if l_max < r_max:
                # Bring l inwards
                l += 1
                # Update l_max if necessary
                l_max = max(l_max, height[l])
                # Add water to total
                total_water += l_max - height[l]
            # If the right max is smaller,
            else:
                # Bring r inwards
                r -= 1
                # Update r_max if necessary
                r_max = max(r_max, height[r])
                total_water += r_max - height[r]
        # Return total water
        return total_water
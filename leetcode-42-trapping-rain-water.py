class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        maxH = max(height)
        max_indices = [i for i in range(len(height)) if height[i] == maxH]
        first_peak = max_indices[0]
        last_peak = max_indices[len(max_indices) - 1]
        
        water = 0
        
        # Before first_peak
        last_max = 0
        for i in range(0, first_peak):
            last_max = max(height[i], last_max)
            water += last_max - height[i]

        for i in range(first_peak, last_peak + 1):
            water += maxH - height[i]
        
        # After last_peak
        last_max = 0
        for i in range(len(height) - 1, last_peak, -1):
            last_max = max(height[i], last_max)
            water += last_max - height[i]
        
        return water

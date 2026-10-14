class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        maxWater = 0

        while left < right:

            area = 0
            width = right - left
            if heights[left] < heights[right]:
                area = heights[left] * width
                left += 1
            elif heights[left] > heights[right]:
                area =  heights[right] * width
                right -= 1
            elif heights[left] == heights[right]:
                area = heights[left] * width
                right -= 1
                left  += 1
        
            maxWater = max(maxWater, area)

        return maxWater
                
        
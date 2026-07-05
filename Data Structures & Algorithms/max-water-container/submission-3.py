class Solution:
    def maxArea(self, heights: List[int]) -> int:
        biggest = 0
        right = len(heights)-1
        left = 0
        current = heights[0]
        while left < right:
            current = heights[left]
            height = min(heights[right], heights[left])
            width = right - left
            amount = height * width
            if amount > biggest:
                biggest = amount
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return biggest
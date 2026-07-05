class Solution:
    def maxArea(self, heights: List[int]) -> int:
        biggest = 0
        for i in range(len(heights)):
            for n in range(1, len(heights)):
                height = min(heights[i], heights[n])
                width = n - i
                amount = height * width
                if amount > biggest:
                    biggest = amount
        return biggest
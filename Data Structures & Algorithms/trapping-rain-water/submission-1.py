class Solution:
    def trap(self, height: List[int]) -> int:
        biggest = 0
        current = height[0]
        for mid in range(1, len(height)-1):
            left = mid - 1
            right = mid + 1
            current = height[mid]
            left_max = max(height[:left+1])
            right_max = max(height[right-1:])
            výška_vody = min(left_max, right_max)
            voda = výška_vody - current
            if voda > 0:
                biggest += voda
               
        return biggest
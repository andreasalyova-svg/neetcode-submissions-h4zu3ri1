class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        biggest = 0
        for mid in range(0, len(prices)-1):
            current = mid 
            right = mid + 1
            left_min = min(prices[:current+1])
            right_max = max(prices[right:])
            end = right_max - left_min
            biggest = max(end, biggest)
        return biggest
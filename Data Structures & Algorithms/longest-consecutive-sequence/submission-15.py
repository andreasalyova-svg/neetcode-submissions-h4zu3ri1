class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        naj = 0
        rad = 1
        numset = set(nums)
        for num in numset:
            if num - 1 not in numset:
                rad = 1
                while num + rad in numset:
                    rad += 1
            naj = max(naj, rad)
        return naj
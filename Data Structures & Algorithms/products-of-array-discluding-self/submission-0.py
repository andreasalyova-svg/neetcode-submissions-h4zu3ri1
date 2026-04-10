class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r=1
        results = []
        for i in range(len(nums)):
            fums_1 = nums[:i]
            fums_2 = nums[i+1:]
            result = fums_1 + fums_2
            for i in result:
                r = i * r
            results.append(r)
            r = 1
        return results




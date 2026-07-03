class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        for i in range(len(nums)):
            right = len(nums) - 1
            left = i+1
            while right > left:
                s = nums[i] + nums[right] + nums[left]
                if s == 0:
                    l = [nums[i], nums[right], nums[left]]
                    l = sorted(l)
                    if l not in result:
                            result.append(l)
                    right -= 1
                    left += 1
                elif s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
        return result 
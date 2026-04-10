class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        numb = []
        for i in range(len(nums)):
            if nums[i] not in groups:
                groups[nums[i]] = 1
            elif nums[i] in groups:
                groups[nums[i]] += 1
            
        groups = sorted(groups.items(), key=lambda x: x[1])
        groups = groups[::-1]
        for num in range(k):
            numb.append(groups[num][0])
        return numb
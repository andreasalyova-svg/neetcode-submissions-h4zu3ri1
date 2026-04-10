class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        state = False
        doubles = []
        for num in nums:
            if state == True:
                break 
            if num not in doubles:
                state = False
                doubles.append(num)
            else:
                state = True
        return state
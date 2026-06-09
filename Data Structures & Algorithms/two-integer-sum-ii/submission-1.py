class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(numbers)):
            fums_1 = numbers[:i] + numbers[i:]
            for n in range(len(fums_1)):
                if numbers[i] + fums_1[n] == target:
                    re = [i+1, n+1]
                    return re
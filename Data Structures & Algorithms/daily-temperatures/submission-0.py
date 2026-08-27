class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: 
        l = [0] * len(temperatures)
        stack = []
        for i, tem in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < tem:
                prev_index = stack.pop()
                l[prev_index] = i - prev_index

            stack.append(i)
        return l
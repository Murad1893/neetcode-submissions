class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use a forward pass
        stack = []
        result = [0] * len(temperatures)

        # pop until current greater and keep updating indices as you go
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                pop = stack.pop()
                result[pop[1]] = i - pop[1]
            stack.append([temperatures[i], i])

        return result
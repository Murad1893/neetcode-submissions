class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                pop_idx, pop_temp = stack.pop()
                result[pop_idx] = i - pop_idx
            stack.append([i, temperatures[i]])

        return result
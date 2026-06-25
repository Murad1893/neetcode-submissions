class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        result = 0

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] >= heights[i]:
                pop_idx, pop_value = stack.pop()
                area = pop_value * (i - pop_idx)
                result = max(area, result)
                start = pop_idx
            stack.append([start, heights[i]])
          
        # another pass to eliminate remaining values
        end = len(heights)
        while stack:
            pop_idx, pop_value = stack.pop()
            area = pop_value * (end - pop_idx)
            result = max(area, result)

        return result  

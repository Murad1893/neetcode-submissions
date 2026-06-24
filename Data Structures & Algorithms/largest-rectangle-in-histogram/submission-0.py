class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Intuition:
        - Cannot apply 2 pointer logic (Container with most water) because we need to account for void space 
        (didn't have this issue with water because we were computing fill)
        """

        # pse array
        stack = []
        pse = [-1] * len(heights)
        nse = [len(heights)] * len(heights)  

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            stack.append(i)      
        
        stack = []
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)  

        print(pse, nse)

        area = 0
        for i in range(len(heights)):
            span = nse[i] - pse[i]
            area = max(area, (span - 1) * heights[i])

        return area